# SelfWifi
使用python实现校园网自动登录  

# 整体逻辑
首先检测周围的wifi名称 (校园网) 是否存在 存在就连接 
然后使用selenium库完成自动化点击网页的元素(当然是后台操作，也就是无头模式)
输入用户名 密码  运营商 然后自动点击自动登录
登陆之后调用windows系统自带的消息提示api(偶尔会失效 不过问题不大)

# 其他
之前也做过一个校园网的自动登录脚本,是通过网络抓包得到的,但是校园网有时候维护的时候他自己会更改自己的请求api，每次更改我都要重新改一遍很麻烦
空闲时间学了python之后发现有这么个selenium库很好用 于是又做了一次

另外修改的时候 建议看一遍代码 把一些地方填入你自己的信息 然后编译导出  
注意编译的时候最好选择无console方式编译成exe 这样运行的时候就没有黑色框框了
比如pyinstaller --noconsole --onefile .\newWifi.py

虽然这个项目开源了,但是对无代码基础的可能有点不太友好(包括没有python环境的朋友) 也许后面有时间我会更新一个比较便利的输入你的信息 然后导出exe的？
# 环境库安装
pip install requests

pip install selenium

pip install win10toast

欢迎各位光临我的个人博客:https://www.ylnxcute.top:1234/
博客目前只有早上8点到晚上12点在线 其他时间维护
