# sjj
1.APP windows端测试环境搭建
1.1.Java环境安装
1.1.1.安装JDK1.8
运行jdk-8u144-windows-i586_8.0.1440.1.exe,默认安装即可(例如我的安装目录: C:\Program Files\Java\jdk1.8.0)
1.1.2.配置Java环境变量(win7为例)
1.进⼊我的电脑 -> 属性 -> ⾼级系统设置 -> 环境变量
2.在系统变量下点击新建 -> 变量名: JAVA_HOME -> 变量值: C:\Program Files\Java\jdk1.8.0 ->点击确定按钮
3.在系统变量下点击新建 -> 变量名: CLASSPATH -> 变量值: .;%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar(***变量值最前⾯有⼀个".") -> 点击确定按钮
4.在系统变量下找到系统的path变量，进⼊在最后添加：;%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin(最前⾯是⼀个分号，如果path变量最后已有分号，可不⽤添加) -> 点击确定按钮
1.1.3.验证环境变量
1.打开命令行窗口
2.输入java 或javac 或java –version
3.输入命令后没有报错,且正常显示则说明Java环境安装成功

1.2.Android_SDK安装
1.2.1.Android-sdk下载
下载地址：http://www.androiddevtools.cn/

1.2.2.AndroidAPI下载
打开Android-sdk-windows文件夹，双击SDK manager.exe文件，安装Tools、Platform-tools、Build-tools、API等相关组件。在安装API时，根据要测试的模拟器或真机的Android版本而定，例如使用的真机是Android 10版本，则Android SDK要下载Android 10版本的API才可以。

在弹出的Android SDk Manager⻚⾯，点击Tools ，下拉框点击Options...

1.2.3.Android-sdk环境变量
首先确保AndroidSDK相关组件都已下载完毕。
sdk-- 软件开发工具包(Software Development Kit)
鼠标选中我的电脑右键，点击属性--高级系统设置--高级--环境变量
A．在系统变量新建ANDROID_HOME，对应变量值为：D:\Androidsdk\android-sdk-windows（sdk安装路径）

B．修改path，添加两个变量，将以下箭头所指的两个文件路径添加到path里

C．path里面添加
;%ANDROID_HOME%\tools; %ANDROID_HOME%\platform-tools;
确定后，打开命令行，输入adb，提示以下信息表示Android sdk环境变量配置成功。


2.adb命令简介
ADB全名Andorid Debug Bridge。 是⼀个Debug⼯具。为何称之为Bridge呢?
因为adb是⼀个标准的C/S结构的⼯具, 是要连接开发电脑和调试⼿机的
包含如下⼏个部分:
1.Client端，运⾏在开发机器中，即你的开发PC机。⽤来发送adb命令。
2.Daemon守护进程, 运⾏在调试设备中, 即的调试⼿机或模拟器。
3.Server端, 作为⼀个后台进程运⾏在开发机器中, 即你的开发PC机. ⽤来管理PC中的Client端和⼿机的Daemon之间的通信。Client<—>Server<—>Daemon
2.1.启动和关闭adb服务
在某些情况下，可能需要终止然后再启动服务端进程，例如adb不响应命令的时候，可以通过重启解决问题。
关闭adb服务，输入命令 adb kill-server
启动adb服务，输入命令 adb start-server
2.2.查询模拟器/真机状态
输入命令 adb devices

连接状态分为2种：
offline-未连接或未响应；
device-已经连接到服务商。注意这个状态并不表示Android系统已经完全启动起来，系统启动的过程中已经可以连接adb，但这个状态是正常的可操作状态。
adb shell getprop ro.build.version.release
2.3.查看⼿机运⾏⽇志
adb logcat
2.4.安装应用程序
输入命令 adb install -r <path_to_apk>
使用adb install命令从电脑中复制应用程序安装到模拟器或真机上，在这个命令中，必须指定待安装的.apk文件的路径。
例如：adb install -r D:\Documents\Downloads\Qunar.apk
提示Success，此时已经将应用程序安装到设备上了。

2.5.卸载应用程序
输入命令 adb uninstall <appPackage>
使用adb uninstall命令在模拟器或真机上卸载指定的应用程序，<appPackage>为要卸载的应用程序包名。
例如：adb uninstall com.Qunar
卸载包名为com.Qunar的应用程序，提示Success，在设备上已经卸载掉此应用程序了。

2.6.获取App的appPackage和appActivity
执行自动化测试之前，必须要获取所测试App的appPackage（包名）和appActivity（启动名），之后将这两个值填写到脚本指定参数里，来告诉要执行的是哪个App。
appPackage: 包名,决定程序的唯一性(不是应用的名字).
appActivity:启动名,目前可以理解为一个启动名对应一个页面.
获取方式有很多（任选其一即可）：
方式一:
先在设备里打开要获取的App
输入命令 adb shell dumpsys window windows | findstr mFocusedApp
例如：微博App，如图所示：
appPackage为com.sina.weibo
appActivity为com.sina.weibo.VisitorMainTabActivity


3.移动端测试工具安装
3.1.主流的移动端⾃动化⼯具
Macaca
1.⽀持语⾔：Java，Python，Node.js
2.⽀持Android和iOS系统
3.⽀持跨应⽤
Appium
1.⽀持语⾔：Java，C#，Python，php，perl，ruby，Node.js
2.⽀持Android和iOS系统
3.⽀持跨应⽤
⾃动化⼯具选择的关注点
1.是否⽀持native，webview
2.是否⽀持获取toast
3.是否⽀持跨应⽤
3.2.APPium简介
1.官⽹：www.appium.io,由SauceLab公司开发
2.Appium是由nodejs的express框架写的Http Server,Appium使⽤WebDriver的json wire协议，来驱动Apple系统的UIAutomation库、Android系统的UIAutomator框架
Appium 是一个自动化测试开源、跨平台工具。它允许测试人员在不同的平台（iOS，Android）使用同一套API来写自动化测试脚本，这样大大增加了 iOS 和 Android 测试套件间代码的复用性。支持 iOS 平台和 Android 平台上的原生应用，web 应用和混合应用。 
所谓的“移动原生应用”是指那些用 iOS 或者 Android SDK 写的应用。 
所谓的“移动 web 应用”是指使用移动浏览器访问的应用（Appium 支持 iOS 上的 Safari 和 Android 上的 Chrome）。 
所谓的“混合应用”是指原生代码封装网页视图——原生代码和 web 内容交互。比如，像 Phonegap，可以帮助开发者使用网页技术开发应用，然后用原生代码封装，这些就是混合应用。
Appium使用的供应商提供的框架：
IOS 9.3及以上：苹果的XCUITest
IOS 9.3及更低版本：苹果的UIAutomation
Android 4.2+：谷歌的UiAutomator/UiAutomator 2
Android 2.3+：谷歌的Instrumentation（Instrumentation由单独的项目Selendroid提供支持）
Windows：微软的WinAppDriver
3.3.APPium基本原理
3.3.1.C/S架构
Appium的核心是一个提供REST API的Web服务器。它接收来自客户端的连接，侦听命令，在移动设备上执行这些命令，并使用HTTP响应进行响应，表示命令执行的结果。
架构图：

3.3.2.Desired Capabilities
Desired capabilities是发送到Appium服务端的一组键和值（即映射或哈希），以告诉服务端我们感兴趣的是哪种类型的自动化会话。例如，我们可以将PlatformName功能设置为IOS，以告诉Appium我们需要一个IOS会话，而不是Android或Windows会话。



通用参数
关键字	描述
automationName	使用哪种自动化引擎
platformName	使用哪个移动OS平台
platformVersion	移动OS版本
deviceName	要使用的移动设备或模拟器的种类
3.3.3.ppium Server
Appium是用Node.js编写的服务端。它可以从源代码构建和安装，也可以直接从NPM安装：
$ npm install -g appium
$ appium
3.3.4.Appium Clients
Appium的客户端库（支持Java、Ruby、Python、PHP、JavaScript和C#），它们支持Appium对WebDriver协议的扩展。
下载地址：http://appium.io/downloads.html
3.3.5.Appium Desktop
Appium Desktop是在Appium Server上封装成一个有图形界面的服务端，可以在任何平台下载安装。它与运行Appium Server所需的所有内容捆绑在一起，因此不需要担心Node环境。它还附带了一个检查器，用来查看应用程序的层次结构等。在编写测试时，这会派上用场。

3.4.APPium安装
3.4.1.node.js安装
1.Node.js下载
下载地址：https://nodejs.org/en/

2.Node.js安装
双击 node-v8.11.4-x64.msi默认安装就好
安装完成后，环境变量自动添加到系统里，直接打开命令行，输入node -v，提示以下信息表示Node.js安装成功。
由于新版的Node.js已经集成了npm，同样在命令行输入 npm -v， 来测试是否安装成功。

3.4.2.appium_server安装
方式一：安装Appium Desktop
下载地址：http://appium.io/downloads.html
在Windows环境下安装Appium Desktop，执行appium-desktop-setup-1.9.0.exe默认安装即可。
安装完成后，Windows下默认安装路径，例如：
C:\Users\Administrator\AppData\Local\Programs\Appium 
安装完成后，自动在桌面添加应用程序的快捷方式，直接执行Appium来启动Appium Desktop。

点击Start Server v1.9.0来开启Appium服务，如下图服务开启成功。

然后点击放大镜，进入Desired capabilities配置



参数说明：
1.platformName：手机操作系统 
2.deviceName：手机设备名称，通过命令行 adb devices查看
3.platformVersion：android系统的版本号
4.appPackage：apk包名
5.appActivity：apk的launcherActivity启动页
6.noreset：默认值为 false，true表示每次不会重置启动app
7.unlocktype:屏幕解锁类型，根据测试机解锁方式设置，这里我的测试机是密码解锁

想了解更多appium服务器初始化参数：
http://appium.io/docs/cn/writing-running-appium/caps/





接下来点击start session

方式二: 命令行安装appium server
输入命令：npm install –g appium（安装需要翻墙）

安装完成后，在cmd命令行输入：appium，如果出现下图则表示安装成功

注意：以下这条很重要！！！
安装Appium Doctor检查appium运行环境
Appium Doctor是一个用于验证Appium安装环境的工具，可以诊断出Node.js、Android、IOS环境配置方面的常见问题。
在Windows环境下，直接打开命令行输入命令进行安装
npm install -g appium-doctor
安装完成后，在命令行执行appium-doctor，会检测Appium的基础环境是否正确，如提示以下信息，证明环境没有问题。


3.4.3.Appium-Python-Client安装
pip命令安装：pip install -U Appium-Python-Client
源码安装，下载地址：https://pypi.org/project/Appium-Python-Client/
点击Download files，下载后缀名为tar.gz包文件，解压tar.gz文件，cmd命令进入压缩文件所在文件夹时，使用 python setup.py install命令安装

安装完成后，输入pip list 查看安装版本

3.5.编写脚本
3.5.1.定义启动设备需要的参数
Desired capabilities：
desired_caps = {}
1.platformName：这里是手机操作系统
2.deviceName：手机设备名称，通过adb devices查看
3.platformVersion：android系统的版本号
4.appPackage：apk包名
5.appActivity：apk的launcherActivity启动页

3.5.2.启动APP
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
3.5.3.操作APP
元素定位:
1)Id定位
find_element_by_id(‘kw’)//通过id属性定位
2)Name定位
find_element_by_name(‘wd’)//通过名字进行定位
3)ClassName定位
find_element_by_class_name(‘cn’)//通过类名进行定位
4)TagName定位
find_element_by_tag_name(‘input’)//标签，一般用于一类元素的定位
5)LinkText定位
find_element_by_link_text(‘新闻’)//文本链接定位
6)PartialLinkText定位
find_element_by_partial_link_text(‘一个很长的’)//文本链接的部分文字
7)xpath定位
find_element_by_xpath('xpath表达式')
8)cssSelector定位
find_element_by_css_selector('css表达式')
输入:
element.send_keys('D\test.txt')
点击操作:
element.click()
3.5.4.退出
driver.quit()
Driver.closed()
完整脚本代码：
1.# >>1. 导入appium  
2.from appium import webdriver  
3.import time  
4.  
5.# >>2. 配置 server 启动参数  
6.desired_caps = {}  
7.# 设备信息  
8.desired_caps['platformName'] = 'Android'# 系统名称  
9.desired_caps['platformVersion'] = '7.1.1'# 系统版本  
10.desired_caps['deviceName'] = '192.168.77.101:5555'# 设备名称  
11.# app 信息  
12.desired_caps['appPackage'] = 'com.android.settings'# 需要启动的APP包名  
13.desired_caps['appActivity'] = '.Settings'# 需要启动的APP启动名  
14.# >>3. 声明驱动对象  
15.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)  
16.  
17.time.sleep(5)  
18.  
19.driver.quit()  
1.POM模式结构
	project--项目名称
		common--公共方法
			base.py--selenium方法二次封装
		page--封装项目所有页面,每一个pageClass都继承Base类
			loginpage.py--登录页面封装
			homepage.py--首页封装
		script--业务流程
			loginflow.py--登录流程,引用page中的loginpage文件
		case--测试用例
			test_login.py--登录功能测试用例
		data--存放测试数据
			Excel
			Txt
		config--存放配置文件
		log--测试脚本日志文件
		report--测试报告run_case.py执行用例
2.测试用例管理
	Unittest
	编写测试用例:
	特殊方法:
		setUp:在测试用例执行前执行
		tearDown:在测试用例执行后执行
		setUpClass:在测试类中的所有测试用例执行前执行一次,并需要@classmethod装饰器			tearDownClass:在测试类中的所有测试用例执行后执行一次,并需要@classmethod装饰		器
	测试用例编写:
		每个测试用例必须以test开头
		测试用例执行顺序按照ASCII码顺序执行,与编写顺序无关
	跳过测试:skip跳过测试类,跳过测试方法
	断言:assert
执行测试用例run_case.py:
	在当前文件执行:unittest.main()
	批量执行:
		测试套件:
			unittest.defaultTestLoader.discover(用例目录,pattern='用例文件.py')		测试执行:
			HTMLTestRunner.HTMLTestRunner(title='自动化测试报告',
									description='用例执行情况：',
									stream=测试报告内容
									verbosity=2).run
