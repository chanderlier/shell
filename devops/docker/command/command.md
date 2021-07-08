将当前目录下的Dockerfile制作成docker image

```sh
docker build -t imagename:tag .
```
删除进程

```sh
docker rm CONTAINER ID
```
删除镜像

```sh
docker rmi IMAGE ID
```
列出docker正在运行的容器

```sh
docker ps
```
列出所有docker容器

```sh
docker ps -a
```
列出docker status 为runnning的容器

```
docker ps -f status=running
```
列出docker status 为exited的容器

```sh
docker ps -f status=exited
```
列出docker images

```sh
docker images
```
删除docker exit 状态的所有进程

```sh
docker rm $(docker ps -q -f status=exited)
```
进入到容器内部

```sh
docker exec -it container id /bin/bash
```
获取元数据信息

```sh
docker inspect image:tag
```
实时获取容器最近的100条日志

```
docker logs -f --tail=100 container
```

将主机/data/test目录拷贝到容器7373cebc60de的/data目录下

```sh
docker cp /data/test 7373cebc60de:/data
```