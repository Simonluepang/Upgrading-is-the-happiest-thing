Linux相关命令
==


### 常用指令

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
    
启动服务与关闭服务
--

    cd /java/tomcat/bin
    
    ./startup.sh
    
    ./shutdown.sh
    
查看日志
--

一般测试的项目里面，有个logs的目录文件，会存放日志文件，有个 xxx.out的文件，可以用 tail -f 动态实时查看后端日志

    cd /logs
    
    # 此时屏幕上会动态实时显示当前的日志，ctr+c 停止
    
    tail -f xxx.out
    
    # 何查看最近 1000 行日志
    
    tail -1000 xxx.out
    
查看端口
--

    # 如显示LISTEN则表示该端口号已被占用
    
    netstat -anp | grep 端口号
    
    # 查看当前所有已经使用的端口情况
    
    netstat -nultp
    
查找文件
--

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
    
搭建测试环境
==

在CenterOS 7下的Linux系统服务器
--

### 1.yum

检查yum环境

    rpm -qa | grep yum
    
### 2.Java

检查java环境

    rpm -qa | grep java
    
如果没有JAVA环境，查找java 1.8.0可以使用的安装包

    yum list | grep java-1.8.0-openjdk 
    
安装java所有文件

    yum -y install java-1.8.0-openjdk*
    
查看java版本号

    java -version
    
输入javac能看到输出内容就表明Java环境已经安装好了

    javac
    
### 3.Tomcat

安装Tomcat

    yum -y install tomcat
    
安装完成以后，查看安装目录

    cd /usr/share/tomcat
    
    ls
    
    ll
    
查看Tomcat的状态，Active: inactive (dead)表示服务还没有跑起来

    systemctl status tomcat
    
启动Tomcat，Active: active (running)表示服务已经正常的跑起来了，Main PID: 5216 (java)表示PID是5216  

    systemctl start tomcat.service    

访问Tomcat，默认端口号是8080，由于Tomcat的web页面是需要安装插件的

    yum install tomcat-webapps tomcat-admin-webadds
    
Tomcat相关命令

    * 停止Tomcat服务
    
    systemctl stop tomcat
    
    * 重启Tomcat
    
    systemctl restart tomcat
    
    * 开机启动
    
    systemctl enable tomcat
    
    * 启动Tomcat
    
    systemctl start tomcat
    
    * 查看tomcat状态
    
    systemctl status tomcat

### 4.Wget

查看系统有没有自带wget工具

    rpm -qa | grep wget
    
下载wget

    yum install wget
    
### 5.Jekins

下载地址：[http://mirrors.jenkins-ci.org/war/latest/jenkins.war](http://mirrors.jenkins-ci.org/war/latest/jenkins.war)

使用Xftp工具传到tomcat的"/usr/share/tomcat/webapps"目录下

首先现在webapps里面新建一个jekins目录

    mkdir /usr/share/tomcat/webapps/jekins
    
因为下载速度慢，所以更换阿里源

    cd /etc/yum.repos.d/
    
    mv CentOS-Base.repo CentOS-Base.repo.back # 建议备份或者改名
    
    wget -O CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
    
    yum makecache #生成缓存

然后回到jekins文件夹里面下载

    cd /usr/share/tomcat/webapps/jekins
    
    wget http://mirrors.jenkins-ci.org/war/latest/jenkins.war
    
下载完成以后，解压war包

    jar -xvf jenkins.war
    
解压完成以后，重启tomcat

    systemctl restart tomcat
    
    cd /usr/share/tomcat/.jenkins/secrets/initialAdminPassword
    
    cd /usr/share/tomcat/.jenkins/secrets
    
    vim initialAdminPassword
    
将获得的密码复制进浏览器输入框，continue以后选择左边的全部安装，然后jekins就安装好了

高频命令
--

### 命令 cd

1.进入上级目录

    cd ..
    
2.进入当前用户主目录

    cd ~
    
3.进入上两级目录

    cd ../..
    
4.进入当前目录

    cd .
    
5.进入指定文件夹

    cd /usr/isTester
    
### 命令 mv

1.移动一个文件夹

    mv ~/isTester/ /APP/www
    
2.移动一个文件

    mv isTester.ini /APP/www
    
3.移动一个文件，并重命名

    mv isTester.ini /APP/www/newTester.ini
    
4.移动文件至上级目录

    mv isTester.ini ../
    
5.一条命令，移动两个文件至同一个文件夹

    mv isTester.ini idoxu.tar -t /APP/www
    
### 命令 cp

1.复制文件到目录

    cp isTester.tar.gz /APP/www
    
2.复制2文件夹到目录

    cp -r isTester/ /APP/www
    
### 命令mkdir

1.新建一个文件夹

    mkdir isTester
    
2.新建三个文件夹

    mkdir isTester1 isTester2 isTester3
    
3.新建多层级文件夹

    mkdir -p main/second/20190429
    
### 命令history

1.查看历史命令执行记录

    history
    
2.查看命令mkdir的历史执行记录

    history | grep mkdir
    
3.执行历史记录中，序号为178的命令

    !178
    
### 命令 tail

1.实时刷新log日志

    tail -f isTester.log
    
2.实时刷新最新500条日志记录

    tail -500f isTester.log
    
### 命令 tar

1.压缩一个文件

    tar -cvf isTester.tar isTester.ini
    
2.压缩多个文件

    tar -cvf all.tar isTester.ini readme.ini
    
3.压缩文件夹

    tar -cvf isTester.tar isTester/
    
4.将当前目录中所有.jpg格式的文件打包

    tar -cvf isTester.tar *.jpg
    
5.将当前目录中所有的.jpg格式的文件打包成.tar.gz

    tar -zcvf isTester.tar.gz *.jpg
    
6.解压tar文件

    tar -xvf isTester.tar
    
7.解压tar.gz文件

    tar -zxvf isTester.tar.gz
    
### 命令 ls

1.列出当前目录中的所有子文件夹和文件

    ls

2.列出当前目录下所有的文件，包括隐藏文件
    
    ls -a
    
3.列出文件的详细信息

    ls -l
    
4.列出当前目录中所有以isTester开头的详细内容

    ls -l isTester*
    
### 命令 ps

1.查看所有进程

    ps -A
    
2.查看java进程

    ps -ef | grep java
    
3.查看所有进程信息，连同命令行

    ps -ef
    
### 命令 top

1.显示进程信息
    
    top

2.监控每个逻辑CPU的状况

    top
    
    1
    
3.高亮显示当前运行进程

    top
    
    b
    
4.显示完整命令

    top
    
    c
    
5.退出top程序

    top
    
    q
    
### 命令 wget

wget是一个下载文件的工具

1.下载isTester.jpg文件

    wget http://51.istester.com/isTester.png
    
2.下载文件，并更改储名

    wget -o Newname.jpg http://51.istester.com/isTester.png
    
3.以后台形式下载文件

    wget -b http://51.istester.com/isTester.png
    
### 命令 find

1.在/root/isTester 目录及其子目录下面查找名字为isTester.ini的文件 

    find /root/isTester/ -name isTester.ini
    
2.在当前目录及其子目录中查找任何扩展名为“ini”的文件

    find . -name "*ini"
    
3.在/root/isTester目录下查找更改时间在5日以内的文件

    find /root/isTester/ -mtime -5
    
4.在/root/isTester目录下查找更改时间在3日以前的文件

    find /root/isTester/ -mtime +3
    
5.在/root/isTester目录下查找所有的目录

    find /root/isTester/ -type d
    
6.在/root/isTester目录下查找所有的文件

    find /root/isTester/ -type f
    
### 命令 rm

1.删除目录下的文件

    rm /root/isTester/isTester.ini
    
2.强行删除目录下的文件

    rm -f /root/isTester/isTester.ini
    
3.删除目录下所有的.log文件

    rm -f /root/isTester/*.log
    
4.删除目录下的ido文件夹

    rm -r /root/isTester/ido/
5.强行删除目录下的ido文件夹

    rm -rf /root/isTester/ido/
    
6.删除目录下所有的内容

    rm -rf /root/isTester/*
    
### 创建文件

1.创建文件

    touch isTester.ini
    
    vi isTester.md
    
    cp isTester.ini isTester666.ini
    
2.同时创建两个文件

    touch isTester.ini idoxu.ini
    
3.同时创建2000个文件

    touch isTester{0001,2000}.ini
    
4.更改文件isTester.ini的时间为当前时间

    touch isTester.ini
    
### 查看文件

命令提示
#cat 由第一行开始显示档案内容 
#tac 从最后一行开始显示，可以看出 tac 是 cat 的倒着写！ 
#more 一页一页的显示档案内容 
#less 与 more 类似，但是比 more 更好的是，他可以往前翻页！ 
#head 只看头几行 
#tail 只看尾巴几行 
#nl 显示的时候，顺道输出 行号！

1.查看文件 isTester.ini的内容

    cat isTester.ini

2.看文件 isTester.ini前20行内容

    head -n 20 isTester.ini

3.看文件 isTester.ini最后30行内容

    tail -n 30 isTester.ini

4.显示文件isTester.ini 的第10至20行的内容

    head -n 20 isTester.ini | tail -n 10

5.倒序显示文件isTester.ini 前10行的内容

    tac isTester.ini | head -n 10

6.显示文件isTester.ini 前10行的内容，并显示行号

    nl isTester.ini | head -n 10
    
### 命令 yum & scp

假设当前服务器IP 192.168.1.23

1.从Linux服务器192.168.1.22 拷贝文件isTester.ini 到服务器192.168.1.23

    scp root@192.168.1.22:/root/idoxu/isTester.ini /root/idoxu
    
2.从Linux服务器192.168.1.22 拷贝目录 isTester/ 到服务器192.168.1.23

    scp -r root@192.168.1.22:/root/idoxu/isTester/ /root/idoxu

3.Linux下安装scp命令（假设是centos服务器，命令用yum）

    yum install openssh-clients
    
### 命令

1.查看当前服务器IP
    
    ifconfig
    
2.查看当前服务器硬盘空间

    df -h
    
3.查看目录isTester/ 所占用的空间

    du -sh isTester
    
4.清空当前终端屏幕

    clear
    
### 命令 vi + chmod

1.创建文件 isTester.ini

    vi isTester.ini

2.更新文件内容为"21 day Linux Learn ,I'm Idolaoxu,in shenzhen ."

    输入 i ，进入编辑模式，输入内容，esc进入命令模式 :wq 保存 。

3.将文件 isTester.ini 设为所有人皆可读取

    chmod +r isTester.ini

4.将 isTester.ini 设定为只有该文件拥有者可以执行

    chmod u+x isTester.ini

5.给文件 isTester.ini 设置所有权限

    chmod 777 isTester.ini