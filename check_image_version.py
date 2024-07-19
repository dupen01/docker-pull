image_tags = open('./to_pull.txt').readlines()

for tag in image_tags:
    tag = tag.strip()
    if len(tag) == 0 or tag.startswith('#'):
        continue
    source_tag = tag.split(' ')[0]
    target_tag = tag.split(' ')[1]
    if not source_tag.startswith('#'):
        if not source_tag.__contains__(':'):
            raise Exception(f"No version is specified. Please add a version: {source_tag}")