# docker-pull

## 使用：
先删除`images_to_copy.txt`文件内容或用`#`将文件内容注释掉，添加自己需要pull的镜像

格式：`目标镜像:目标镜像版本 阿里云镜像名称:阿里云镜像版本`

push到master，将在阿里云公开仓库生成 arm64 和 amd64 两个版本的镜像。

例如：

`python:3.12.4-slim-bullseye python:3.12.4-slim-bullseye`

将push两个版本的镜像到阿里云镜像仓库：

`registry.cn-chengdu.aliyuncs.com/mirror_d/python:3.12.4-slim-bullseye-amd64` 和  
`registry.cn-chengdu.aliyuncs.com/mirror_d/python:3.12.4-slim-bullseye-arm64`
