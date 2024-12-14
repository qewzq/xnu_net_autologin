from multiprocessing import freeze_support,Process
from pystray import MenuItem,Menu,Icon
from PIL import Image
from tkinter import Button, Entry, Label, Tk, messagebox, ttk
from time import strftime,localtime,sleep,time
from linecache import getline
from requests import ConnectionError,get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from os import path,kill
import sys
# from plyer import notification
import pyi_splash


dir_name = 'C:\\Users\\Public\\'
schoolnetloginweburl = "http://172.18.1.6/a79.htm"
projectname = "湘南学院校园网自动登录小程序"
author= "bilibili：柔情巧克力--"
# massage_out_time = 3





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

    outtime=5#超时时间(s)
    delaytime = 10#检查时间间隔(s)
    username = ""
    password = ""
    netclass = ""

    try:
        username = getline("C:\\Users\\Public\\userconfig.conf", 1).strip('\n')
        password = getline("C:\\Users\\Public\\userconfig.conf", 2).strip('\n')
        netclass = getline("C:\\Users\\Public\\userconfig.conf", 3).strip('\n')
        # outtime = linecache.getline("C:\\Users\\Public\\userconfig.conf", 4).strip('\n')
        # delaytime = linecache.getline("C:\\Users\\Public\\userconfig.conf", 5).strip('\n')
    except:
        messagebox.showwarning(title=projectname,message='请先配置登录账号密码哦')
        setlogin()



    def is_connected(url):
        try:
            response = get(url, timeout=outtime)
            return response.status_code == 200
        except ConnectionError:
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


    
    
