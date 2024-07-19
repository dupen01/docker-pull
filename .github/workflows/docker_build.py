import os
import sys

image_lines = open('to_pull.txt').readlines()
registry = os.environ.get('REGISTRY')
namespace = os.environ.get('NAMESPACE')

daemon_txt = """{
  "features": {
    "containerd-snapshotter": true
  }
}"""

with open('/etc/docker/daemon.json', 'w') as f:
    f.write(daemon_txt)

ret1 = os.system("systemctl restart docker")
if ret1 != 0:
    sys.exit(ret1 >> 8)


for line in image_lines:
    line = line.strip()
    if len(line) == 0 or line.startswith('#'):
        continue
    images = line.split(' ')
    source_img = images[0]
    target_img = images[1] if len(images) > 1 else source_img

    source_img_name = source_img.split(':')[0]
    source_img_version = source_img.split(':')[1] if source_img.split(':')[1] else 'latest'

    dockerfile = f"FROM {source_img}\n"
    dockerfile_dir_path = f'/tmp/{source_img_name}/{source_img_version}'
    if not os.path.exists(dockerfile_dir_path):
        os.makedirs(dockerfile_dir_path)
    dockerfile_path = os.path.join(dockerfile_dir_path, 'Dockerfile')
    with open(f"{dockerfile_path}", 'w') as f:
        f.write(dockerfile)

    target_img_fullname = f"{registry}/{namespace}/{target_img}"

    build_cmd = f"""
    docker build --platform=linux/amd64,linux/arm64 \
    -t {target_img_fullname} --push \
    -f {dockerfile_path} .
    """
    print(build_cmd)
    ret = os.system(build_cmd)
    if ret != 0:
        sys.exit(ret >> 8)
