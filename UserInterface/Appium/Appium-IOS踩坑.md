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

[Facebook的无缺陷版WebdriverAgent](https://github.com/facebookarchive/WebDriverAgent)

把这个项目下载下来，放在一个不需要权限的路径里面

然后使用终端cd到你存放WebDriverAgent的目录下，使用下面命令下载依赖

    ./Scripts/bootstrap.sh