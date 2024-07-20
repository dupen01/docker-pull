# docker-pull

## 使用：
### 1. fork 本项目
### 2. 添加私有镜像仓库的用户名和密码 
在项目`settings->Secrets and variables->Actions`添加私有仓库的用户名和密码。变量名使用：`REGISTRY_USER`和`REGISTRY_PASSWORD`，也可以在`registry_env.sh`文件内添加环境变量。
### 3.配置私有镜像仓库的地址和命名空间 
在`registry_env.sh`文件添加`REGISTRY`和`NAMESPACE`环境变量，分别是私有镜像仓库的地址和命名空间。
### 4. 填写需要copy的镜像列表 
在`images_to_copy.txt`文件内添加需要copy到私有仓库的镜像名，支持`#`注释。

格式：`目标镜像:目标镜像版本 阿里云镜像名称:阿里云镜像版本`

如果不需要改写镜像名称或tag，可仅填写原始镜像名称和tag，例如
```
# quay.io/minio/minio:RELEASE.2024-07-16T23-46-41Z  minio:20240716
nginx:1.27.0
nginx
```

### 5. push至master分支
等待 GitHub Action workflow 构建完成。

如果需要添加通知，可在 https://github.com/settings/notifications 地址将Action的通知策略的`Only notify for failed workflows`取消勾选，这样无论构建成功或失败都会收到通知。

