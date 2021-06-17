```dockerfile
FROM centos7.5.1804

ENV LANG=en_US.utf8

ENV LC_ALL=en_US.utf8

ARG workdir=/app

WORKDIR ${workdir}

COPY 文件/代码/启动脚本  镜像中的目录 (例如：COPY ./entrypoint.sh ./)

RUN 在镜像中执行一些命令，例如mkdir/yum install/chmod ...

EXPOSE 需要暴露的port

ENTRYPOINT ["启动脚本"] (例如：ENTRYPOINT ["./entrypoint.sh"])
```
### RUN
RUN命令是创建Docker镜像（image）的步骤，RUN命令对Docker容器（ container）造成的改变是会被反映到创建的Docker镜像上的。一个Dockerfile中可以有许多个RUN命令。

### CMD
CMD命令是当Docker镜像被启动后Docker容器将会默认执行的命令。一个Dockerfile仅仅最后一个CMD起作用。通过执行
```sh
docker run image  command
```
启动镜像可以重载CMD命令。

CMD很像开机启动项，你可以暂时这样理解,会被覆盖。
主要用法
第一种用法：运行一个可执行的文件并提供参数。
第二种用法：为ENTRYPOINT指定参数。
第三种用法(shell form)：是以”/bin/sh -c”的方法执行的命令。
### ENTRYPOINT
CMD和ENTRYPOINT这两个指令用于在Dockerfile和Docker Compose files里配置容器的运行命令。
Entrypoint指令用于设定容器启动时第一个运行的命令及其参数。

任何使用docker run <image>命令传入的参数都会附加在entrypoint指令之后，并且用此命令传入的参数会覆盖在Dockerfile中使用CMD指令设定的值。比如docker run <image> bash命令会将bash命令附加在entrypoint指令设定的值的后面。



总结
1. CMD和ENTRYPOINT在Dockerfiles中应该至少应该有一个被定义。
2. 当构建可执行容器时，应该定义ENTRYPOINT指令。
3. CMD要么用于给ENTRYPOINT提供默认参数，要么用于在容器中执行一个特定命令。
4. CMD可以通过容器启动命令docker run的参数来替换它。
5. 使用 RUN 指令安装应用和软件包，构建镜像。如果 Docker 镜像的用途是运行应用程序或服务，比如运行一个 MySQL，应该优先使用 Exec 格式的 ENTRYPOINT 指令。CMD 可为 ENTRYPOINT 提供额外的默认参数，同时可利用 docker run 命令行替换默认参数。



### COPY
COPY
复制指令，从上下文目录中复制文件或者目录到容器里指定路径。
```
COPY [--chown=<user>:<group>] <源路径1>...  <目标路径>
COPY [--chown=<user>:<group>] ["<源路径1>",...  "<目标路径>"]
```
### ADD
ADD 指令和 COPY 的使用格式一致（同样需求下，官方推荐使用 COPY）。功能也类似，不同之处如下：

ADD 的优点：在执行 <源文件> 为 tar 压缩文件的话，压缩格式为 gzip, bzip2 以及 xz 的情况下，会自动复制并解压到 <目标路径>。
ADD 的缺点：在不解压的前提下，无法复制 tar 压缩文件。会令镜像构建缓存失效，从而可能会令镜像构建变得比较缓慢。具体是否使用，可以根据是否需要自动解压来决定。

### ENV
设置环境变量，定义了环境变量，那么在后续的指令中，就可以使用这个环境变量。
### ARG
构建参数，与 ENV 作用一至。不过作用域不一样。ARG 设置的环境变量仅对 Dockerfile 内有效，也就是说只有 docker build 的过程中有效，构建好的镜像内不存在此环境变量。
### VOLUME
定义匿名数据卷。在启动容器时忘记挂载数据卷，会自动挂载到匿名卷。
作用：
1. 避免重要的数据，因容器重启而丢失，这是非常致命的。
2. 避免容器不断变大。
   
### WORKDIR
指定工作目录。用 WORKDIR 指定的工作目录，会在构建镜像的每一层中都存在。（WORKDIR 指定的工作目录，必须是提前创建好的）。

docker build 构建镜像过程中的，每一个 RUN 命令都是新建的一层。只有通过 WORKDIR 创建的目录才会一直存在。
### EXPOSE
仅仅只是声明端口。
作用：
1. 帮助镜像使用者理解这个镜像服务的守护端口，以方便配置映射。
2. 在运行时使用随机端口映射时，也就是 docker run -P 时，会自动随机映射 EXPOSE 的端口。 
   

### USER
用于指定执行后续命令的用户和用户组，这边只是切换后续命令执行的用户（用户和用户组必须提前已经存在）。