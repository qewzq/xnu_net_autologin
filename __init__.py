from multiprocessing import freeze_support,Process
from random import choice
from pystray import MenuItem,Menu,Icon
from PIL import Image
from tkinter import Button, Entry, Label, Tk, messagebox, ttk
from time import strftime,localtime,sleep,time
from linecache import getline
from requests import session,packages
from requests.adapters import HTTPAdapter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from os import path,kill
import sys
# from plyer import notification
import pyi_splash

#关于里附上版本

dir_name = 'C:\\Users\\Public\\'
schoolnetloginweburl = "http://172.18.1.6/a79.htm"
projectname = "湘南学院校园网自动登录小程序"
author= "bilibili：柔情巧克力--"




outtime=(5,5)#超时时间(s)
delaytime = 10#检查时间间隔(s)
username = ""
password = ""
netclass = ""
# massage_out_time = 3

packages.urllib3.disable_warnings()
headers_list = [
    {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'
    }, {
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'
    }, {
        'user-agent': 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'
    }, {
        'user-agent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'
    }, {
        'user-agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    }
]


def test_msedgedriver():
    #未开发内容，测试中

    try:
        pyi_splash.update_text('Loaded ...')
        pyi_splash.close()
    except:
        pass


# def out_notice(text):
#     notification.notify(
#         message=text,
#         app_name=projectname,
#         timeout=massage_out_time  # 持续时间（秒）
#     )

def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = path.abspath(".")
    return path.join(base_path, relative_path)



iconfilename = resource_path(path.join(".","icon.ico"))

def prints(st):
    times = strftime("%Y-%m-%d %H:%M:%S", localtime())
    out = times + " |"+ st
    print(out)
    with open(dir_name +'login.log','a')as file:
        file.write(out+"\n")
        file.close()


def setlogin():
        root = Tk()    
        def on_close():
            print("close windows")
            root.destroy()
        def save():
            usernanme = entry1.get()
            password = entry2.get()
            netclass = acquire.get()
            if netclass == "校园网":
                netclass = "@xyw"
            if netclass == "中国电信":
                netclass = "@telecom"
            if netclass == "中国联通":
                netclass = "@unicom"
            if netclass == "中国移动":
                netclass = "@cmcc"
            fb = open(dir_name + 'userconfig.conf',mode='w',encoding='utf-8')
            fb.write(usernanme+'\n'+password+'\n'+netclass+'\n')
            fb.close()
            messagebox.showinfo(title=projectname,message='信息已保存') 
            root.destroy()
        # 窗口大小
        root.geometry("500x300")
        root.iconbitmap(iconfilename)

        #  窗口标题
        root.title(projectname+" by "+author)

        # 添加标签控件
        label = Label(root,text="输入校园网账号",font=("仿宋",25))
        label.grid(row=1, column=0)



        # 添加输入框
        entry1 = Entry(root,font=("仿宋",25))
        entry1.grid(row=2, column=0)




        label = Label(root,text="输入校园网密码",font=("仿宋",25))
        label.grid(row=3, column=0)
        entry2 = Entry(root,font=("仿宋",25))
        entry2.grid(row=4, column=0)



        label = Label(root, text='获取下拉框的值：')
        acquire = ttk.Combobox(root,font=("仿宋",20))
        acquire['value'] = ('校园网', '中国电信', '中国联通', '中国移动')
        acquire.current(0)
        acquire['state'] = 'readonly'

        acquire.grid(row=5, column=0)

        # 添加点击按钮
        button = Button(root,text="保存",font=("仿宋",25),command=save)
        button.grid(row=6, column=0)

        root.focus_set()
        entry1.focus()

        root.columnconfigure(0, weight=1)
        root.protocol('WM_DELETE_WINDOW', on_close)
        # 显示窗口
        root.mainloop()


def login(driver,username,password,netclass):
    prints("尝试登录中....")
    driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[2]/div[2]/form/input[2]').send_keys(username)
    driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[2]/div[2]/form/input[3]').send_keys(password)
    selectTag = Select(driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[2]/div[2]/select'))  # select标签
    selectTag.select_by_value(netclass)
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[2]/div[2]/form/input[1]').click()
    sleep(5)


p4  = Process(target=setlogin,)
def runmini():
   


    def setlogins():
        p4.start()

    def displays():
        Process(target=messagebox.showinfo(title=projectname,message='湘南学院欢迎您') == "ok",).start
        
    def abouts():
        Process(target=messagebox.showinfo(title=projectname,message='开发者bilibili：柔情巧克力--\n为广大广大师生提供便利\n医学牲写的乱,达到目的就行\n各位可私信我或自行更改哦'),).start
    
    def on_exit(icon,item):
        icon.stop()
        # sys.exit(0) # 退出程序，返回状态码0



    # 创建一个系统托盘对象
    menu = (
        MenuItem("湘南学院欢迎您", displays),
        MenuItem("设置账号密码", setlogins),
        
        Menu.SEPARATOR,
        MenuItem("关于",abouts),
        MenuItem("退出",on_exit)
    )
    p3 = Process(target=Icon("icon", Image.open(iconfilename), projectname, menu).run(),)
    p3.start()
    p3.join()    
    try:
        p4.terminate()
    except:
        pass
    p3.terminate()
    






def runmain():
    # os.system('python '+path+'\\login.py')

    

    try:
        username = getline("C:\\Users\\Public\\userconfig.conf", 1).strip('\n')
        password = getline("C:\\Users\\Public\\userconfig.conf", 2).strip('\n')
        netclass = getline("C:\\Users\\Public\\userconfig.conf", 3).strip('\n')
        # outtime = linecache.getline("C:\\Users\\Public\\userconfig.conf", 4).strip('\n')
        # delaytime = linecache.getline("C:\\Users\\Public\\userconfig.conf", 5).strip('\n')
    except:
        messagebox.showwarning(title=projectname,message='请先配置登录账号密码哦')
        setlogin()


    sessi = session()
    sessi.mount('http://', HTTPAdapter(max_retries=2)) 
    sessi.mount('https://', HTTPAdapter(max_retries=2))     
    sessi.keep_alive = False # 关闭多余连接



    def is_connected(url):
        try:
            sess = sessi.get(url, headers=choice(headers_list), stream=True, verify=False, timeout=(5,5))
            
            if sess.status_code == 200:
                sess.close()
                return sess.status_code == 200
            else:
                return False
        except :
            return False

    if username == "" or password == "" or netclass == "":
        messagebox.showwarning(title=projectname,message='请先配置登录账号密码哦')
        setlogin()

    while(1):
        if is_connected("https://cn.bing.com/"):
            prints("Network was connected.")
            sleep(delaytime)
            continue
        else:
            prints("\033[0;37;41mCan't connect to cn.bing.com!!!!!!\033[0m")
            prints("核实断网情况中....")
            if is_connected("https://www.baidu.com/"):#核实断网情况
                prints("Fack maseeage.")
                sleep(delaytime)
            else:
                prints("判断校园网平台是否登录中.....")
                try:
                    option = webdriver.EdgeOptions()
                    option.add_argument('--headless')   
                    driver = webdriver.Edge(options=option)
                    driver.get(schoolnetloginweburl)
                    sleep(7)
                    if driver.find_elements(By.NAME, "logout"):
                        driver.quit()
                        sleep(delaytime)
                        continue
                    else:
                        login(driver,username,password,netclass)
                        if driver.find_elements(By.NAME, "logout"):
                            prints("\033[0;37;42m登录成功\033[0m")
                            driver.quit()
                            # out_notice("校园网已自动重连")
                            sleep(delaytime)
                            continue
                        if driver.find_elements(By.NAME, "GobackButton"):
                            print("\033[0;37;41m登录失败!!!!!!\033[0m")
                            driver.refresh()
                            sleep(5)
                            login(driver,username,password,netclass)
                            if driver.find_elements(By.NAME, "logout"):
                                prints("\033[0;37;42m登录成功\033[0m")

                                driver.quit()
                                sleep(delaytime)
                                continue
                        else:
                            messagebox.showwarning(title=projectname,message='未知错误！！！！！！！')
                        continue
                except:
                    if is_connected(schoolnetloginweburl) == 200 :
                        messagebox.showwarning(title=projectname,message='未知错误！！！！！！！')
                    else:
                        continue




if __name__ == '__main__':
    freeze_support()

    test_msedgedriver()


    start = time()
 
    p1 = Process(target=runmini,)
    p2 = Process(target=runmain,)
    # 启动子进程
    p1.start()
    p2.start()
    # 等待fork的子进程终止再继续往下执行，可选填一个timeout参数

    
    p1.join()
    p2.terminate() 
    end = time()


    
    
