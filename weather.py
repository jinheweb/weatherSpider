import requests,re,os
from bs4 import BeautifulSoup
from tkinter import *

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

header = {"Accept": "text/html,application
/xhtml+xml,application/
xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
              "User - Agent": "Mozilla / 5.0(Windows 
NT 10.0;WOW64)
 AppleWebKit / 537.36(KHTML, likeGecko) 
 Chrome / 66.0.3359.
 139Safari / 537.36"}
list=["hb", "db", "hd", "hz", "hn", "xb", "xn", "gat"]





def get_html(x):
    url = "http://www.weather.com.cn/textFC/" + str(x) 
+ ".shtml"
    res = requests.get(url, headers=header)
    html = res.text.encode('iso-8859-1')
    soup = BeautifulSoup(html, 'lxml')
    return soup



def city_name(x):
    name = re.findall(r' target="_blank">(.*?)</a></td>',
str(get_html(x)))
    return name
    #print (name)
def city_number(x):
    number = re.findall(r'href="http://www.weather.
com.cn
/weather/(.*?).shtml"',str(get_html(x)))
    return number
def new_list(x):
    keys = city_name(x)
    values = city_number(x)
    list = dict(zip(keys,values))
    del list['详情']
    return list


dir = {}
for x in list:
    a = new_list(x)
    dir.update(a)
    #dir = dict(a.items()+dir.items())
#print (dir)

def chaxun():
    a = entry.get()
    if a in dir:
        return dir[a]
    else:
        print("输入城市不存在")
        return
def wendu():
    url = "http://www.weather.com.cn/weather1d/"
+str(chaxun())+".shtml"
    res = requests.get(url)
    html = res.text.encode('iso-8859-1')
    soup = BeautifulSoup(html, 'lxml')
    a = soup.find_all('input')
    b = str(a[7]).split('"')
    return (b[5])




def xianshi():
    var.set(wendu())



label = Label(frame1,text="请输入想要查询天气的
城市名称：")
.grid(row=0,column=0)

v1=StringVar()
entry = Entry(frame1,textvariable=v1)
entry.grid(row=0,column=1)


var = StringVar()
var.set("                      锦河工作室")
label1 = Label(frame2,textvariable=var)
.grid(row=1,column=1)

button = Button(frame2,text="查询",
command=xianshi,fg="red")
.grid(row=1,column=0)
frame1.pack()
frame2.pack()
mainloop()




#print(url_list())
#get_html()
#print (new_soup())
#print(get_list())
#print(get_html(list[0]))
#print(city_name())
#print(city_number(list[0]))
#print(new_list())
#chaxun()
#print(wendu())