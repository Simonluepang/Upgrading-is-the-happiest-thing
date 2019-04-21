# Linux相关命令

## 常用指令

1.查看目录中的文件

    ls

2.进入home目录

    cd /home

3.返回上一级目录 

    cd ..

4.创建一个名为dir1的文件夹

    mkdir dir1

5.删除一个名为dir1的文件夹，只能删除空目录

    rmdir dir1

6.删除dir1目录下的所有文件以及子文件夹

    rm -rf /dir1

7.创建一个二进制文件

    touch aa
    
8.创建一个文件

    vi aa.txt
    
9.删除一个文件

    rm -f aa.txt
    
10.如将/test1 目录下的 file1 复制到/test3 目录，并将文件名改为 file2

    cp /test1/file1 /test3/file2
    
11.对当前文件改名

    cp /test1/file1 /test1/file2
    
    rm -f /test1/file1
    
12.将/test1 目录下的 file1 移动到/test3 目录，并将文件名改为 file2

    mv /test1/file1 /test3/file2
    
13.当前目录所有文件移动到上一级目录

    mv * ../
    
14.显示进程 pid（如需显示JAVA进程pid）

    ps -ef|grep java
    
15.杀掉进程

    kill -9 [PID]
    
16.解压tar包

    tar -xvf file.tar
    
17.解压zip

    unzip file.zip
    
18.解压rar

    unrar e file.rar
    
19.查看服务器内存使用情况

    free -m
    
## 启动服务与关闭服务

    cd /java/tomcat/bin
    
    ./startup.sh
    
    ./shutdown.sh
    
## 查看日志

一般测试的项目里面，有个logs的目录文件，会存放日志文件，有个 xxx.out的文件，可以用 tail -f 动态实时查看后端日志

    cd /logs
    
    # 此时屏幕上会动态实时显示当前的日志，ctr+c 停止
    
    tail -f xxx.out
    
    # 何查看最近 1000 行日志
    
    tail -1000 xxx.out
    
## 查看端口

    # 如显示LISTEN则表示该端口号已被占用
    
    netstat -anp | grep 端口号
    
    # 查看当前所有已经使用的端口情况
    
    netstat -nultp
    
## 查找文件

1.查找一个文件大小在100k和400k之间的文件

    find . -type f -mtime -1 -size +100k -size-400k
    
2.根据名称查找文件的路径

    find / -name tnsnames.ora
    
    locate tnsnames.ora
    
3.在根目录下查找文件 httpd.conf，表示在整个硬盘查找

    find / -name httpd.conf
    
4.在/etc 目录下文件 httpd.conf

    find /etc -name httpd.conf
    
5.查找在系统中最后 10 分钟访问的文件(access time)

    find / -amin -10
    
6.查找在系统中最后 48 小时访问的文件(access time)

    find / -atime -2
    
7.查找在系统中为空的文件或者文件夹

    find / -empty
    
8.查找在系统中属于 group 为 cat 的文件

    find / -group cat
    
9.查找在系统中最后 5 分钟里修改过的文件(modify time)

    find / -mmin -5
    
10.查找在系统中最后 24 小时里修改过的文件(modify time)

    find / -mtime -1
    
11.查找在系统中属于 fred 这个用户的文件

    find / -user fred
    
12.查找出大于 10000000 字节的文件(c：字节，w：双字，k：KB，M：MB，G：GB)

    find / -size +10000c
    
13.查找出小于 1000KB 的文件

    find / -size -1000k
    
# 搭建测试环境

