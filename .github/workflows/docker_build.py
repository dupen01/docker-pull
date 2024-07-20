import os
import sys

image_lines = open('images_to_copy.txt').readlines()
registry = os.environ.get('REGISTRY')
namespace = os.environ.get('NAMESPACE')


for line in image_lines:
    line = line.strip()
    if len(line) == 0 or line.startswith('#'):
        continue
    images = line.split(' ')
    source_img = images[0]
    target_img = images[1] if len(images) > 1 else source_img

    source_tag = source_img.split(':')
    source_img_name = source_tag[0]
    source_img_version = source_tag[1] if len(source_tag) > 1 else 'latest'

    target_tag = target_img.split(':')
    target_img_name = target_tag[0]
    target_img_version = target_tag[1] if len(target_tag) > 1 else 'latest'

    dockerfile = f"FROM {source_img}\n"
    dockerfile_dir_path = f'/tmp/{source_img_name}/{source_img_version}'
    if not os.path.exists(dockerfile_dir_path):
        os.makedirs(dockerfile_dir_path)
    dockerfile_path = os.path.join(dockerfile_dir_path, 'Dockerfile')
    with open(f"{dockerfile_path}", 'w') as f:
        f.write(dockerfile)

    target_img_fullname = f"{registry}/{namespace}/{target_img_name}:{target_img_version}"
    arm_img_name = target_img_fullname + "-arm64"
    amd_img_name = target_img_fullname + "-amd64"

    build_cmd = f"""
    docker build --platform=linux/amd64 -t {amd_img_name} --push -f {dockerfile_path} . && \
    docker build --platform=linux/arm64 -t {arm_img_name} --push -f {dockerfile_path} .
    """

    build_cmd_v2 = f"docker build -t {target_img_fullname} --push -f {dockerfile_path} ."
    ret = os.system(build_cmd_v2)
    if ret != 0:
        sys.exit(ret >> 8)
