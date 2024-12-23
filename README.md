# docker-pull
## 说明
1. 利用 GitHub 的服务器资源和私有镜像仓库实现 Copy Docker Hub 或其他国外镜像仓库的镜像到国内私有或公开镜像仓库；
2. 需要自行准备私有镜像仓库的账号，比如阿里云、华为云等；
3. 支持自动构建多平台的镜像，例如copy到私有仓库后，拉取同一个镜像地址，在x86架构的PC机上拉取的是amd64版本，在arm架构的服务器上拉取的就是arm64版本的镜像，不需要关心镜像CPU架构问题。

## 使用：
### 1. fork 本项目
### 2. 添加私有镜像仓库的用户名和密码 
在项目`settings->Secrets and variables->Actions`添加私有仓库的用户名和密码。变量名使用：`REGISTRY_USER`和`REGISTRY_PASSWORD`，也可以在`registry_env.sh`文件内添加环境变量。
### 3.配置私有镜像仓库的地址和命名空间 
在`registry_env.sh`文件添加`REGISTRY`和`NAMESPACE`环境变量，分别是私有镜像仓库的地址和命名空间。
### 4. 填写需要copy的镜像列表 
在`images_to_copy.txt`文件内添加需要copy到私有仓库的镜像名，支持 `#`, `//`, `--` 注释。

格式：`目标镜像名称:目标镜像tag  私有仓库镜像名称:私有仓库镜像tag`

如果不需要改写镜像名称或tag，可仅填写原始镜像名称和tag，例如
```
# quay.io/minio/minio:RELEASE.2024-07-16T23-46-41Z  minio:20240716
nginx:1.27.0
nginx
```

### 5. push至master分支
等待 GitHub Action workflow 自动构建完成。

### 6. 通知
如果需要添加通知，可在 https://github.com/settings/notifications 地址将Action的通知策略的`Only notify for failed workflows`取消勾选，这样无论构建成功或失败都会收到通知，默认仅失败通知。

