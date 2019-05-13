[这个教程很详细](https://www.jianshu.com/p/81899f2b64b0)

### 1.首先安装homebrew

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

### 2.安装node.js和npm

[安装地址](https://nodejs.org/en/)

然后！坑来了！这个时候跟着教程往下使用npm安装的时候各种报错

首先就是这个错误

    npm WARN checkPermissions Missing write access to /usr/local/lib/node_modules

解决办法：

1.修改npm包所安装目录的权限，然后输入密码

    sudo chown -R $USER /usr/local

2.出现下方字样时，就基本完成了

    chown :/usr/local: Operation not permitted

3.然后查看目录是否已经切换权限

    ls -l /usr/local

然后报了一个其他的错误

    xcode-select: error: tool 'xcodebuild' requires Xcode, but active developer directory '/Library/Deve

这个错误是因为安装了xcode，但是并不是系统默认的位置，需要使用以下命令将xcode的位置修改为当前安装的路径下

    sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer

### 3.安装必要的库

1.安装可以使appium连接IOS设备的库，libimobiledevice

    brew install libimobiledevice --HEAD

2.在IOS10+的系统上使用appium的话需要安装ios-deploy

    npm install -g ios-deploy

### 4.安装appium-doctor

    npm install appium-doctor -g

执行appium-doctor指令，查看相关配置是否完整

    appium-doctor --ios

### 5.安装carthage

    brew install carthage

### 6.安装cnpm

    npm install -g cnpm --registry=https://registry.npm.taobao.org

### 7.安装appium

    cnpm install -g appium

### 8.替换appium.app中的WebdriverAgent

[Facebook的无缺陷版WebdriverAgent下载地址](https://github.com/facebookarchive/WebDriverAgent)

把这个项目下载下来，放在一个不需要权限的路径里面

然后使用终端cd到你存放WebDriverAgent的目录下，使用下面命令下载依赖

    ./Scripts/bootstrap.sh

### 9.安装java以及配置JDK

1.从官网上下载java

[java官网下载地址](https://www.oracle.com/technetwork/java/javase/downloads/index.html)

下载完成以后一路点击继续，安装成功以后，在终端中查看java版本，以确认java正确安装成功

    java -version

2.配置PATH和CLASS_PATH

首先打开终端terminal，在终端下打开profile文件

    sudo vim /etc/profile

然后输入i，进入insert模式

在文件最后添加以下内容，jdk的版本号需要做更改

    JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk-10.0.2.jdk/Contents/Home"

    CLASS_PATH="$JAVA_HOME/lib"

    PATH=".:$PATH:$JAVA_HOME.bin"

点击esc退出insert模式，输入 :wd! 来保存并退出profile，然后执行命令使修改的内容立即生效而不用重启

    source /etc/profile

测试java程序编译与运行

    touch Hello.java    # 新建java文件

    vim Hello.py        # 使用vim打开文件

然后在文件中输入以下代码

    class Hello {

         public static void main(String[] args) {
               System.out.println("Hello, world!");
         }
    }

在终端编译该java文件

    javac Hello.java

执行测试程序

    java Hello

#### mac终端登录默认为-bash-3.2$解决办法

[解决办法](https://jingyan.baidu.com/article/c74d6000c277e80f6a595d8c.html)

#### mac电脑任何命令都是command not found

配置路径以后，之前安装好的都无法使用了，说明mac的环境变量已经被更改了，所以输入以下代码就可以

    export PATH=/usr/local/opt/coreutils/libexec/gnubin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/Wireshark.app/Contents/MacOS

[解决问题地址](https://www.jianshu.com/p/1dfa8cc85548)

### 10.真机安装webdriverAgent

有开发者账号的情况下，可以这么做

[有开发者账号的情况下真机安装webdriverAgent](https://testerhome.com/topics/7220)

没有开发者账号的话就需要使用导入.p12和.mobileprovision的方法

[IOS证书和描述文件的申请](http://ask.dcloud.net.cn/article/152)