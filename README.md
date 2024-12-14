#湘南学院校园网自动登录软件

作者：bilibili：柔情巧克力--

##直接下载使用
直接在Release下载
可以定制断网检测时间，可以调整源码自编译

拥有日志文件，文件位置："C:\Users\Public\login.log"

-----

##自编译

环境：
Python 3.11
pyinstaller 6.11.1


命令
自己git到本地
pip install pyinstaller，multiprocessing，pystray，PIL，tkinter，linecache，requests，selenium
pyinstaller  __init__.spec
exe在dist目录下
