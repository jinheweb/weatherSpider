import requests,re,os
from bs4 import BeautifulSoup
from tkinter import *
root = Tk()


def get_html():
    url = "http://www.weather.com.cn/forecast/index.shtml"
    header = {"Accept": "text/html,application/xhtml+xml,
application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) 
AppleWebKit/537.36 (KHTML, like Gecko) 
Chrome/66.0.3359.139 Safari/537.36"}
    res = requests.get(url,headers=header)
    html = res.text.encode('iso-8859-1')

    soup = BeautifulSoup(html, 'lxml')
    return soup
def city_name():
    name = re.findall(r' target="_blank">(.*?)</a></li>'str(get_html()))
    return (name[0:140])
def city_number():
    number = re.findall(r'<li><a href="http://www.weather.com.cn
/weather1d/(.*?).shtml'
,str(get_html()))
    return number[0:140]
def new_list():
    keys = city_name()
    values = city_number()
    list = dict(zip(keys,values))
    return list
def chaxun():
    x = entry.get()
    if x in new_list():
        return new_list()[x]
    else:
        print("输入城市不存在")
        return
def wendu():
    url = "http://www.weather.com.cn/weather1d/"+str(chaxun())+".shtml"
    res = requests.get(url)
    html = res.text.encode('iso-8859-1')
    soup = BeautifulSoup(html, 'lxml')
    a = soup.find_all('input')
    b = str(a[7]).split('"')
    print (b[5])




label = Label(root,text="请输入想要查询天气的城市名称：").grid(row=0,column=0)
v1=StringVar()

entry = Entry(root,textvariable=v1)
entry.grid(row=0,column=1)
button = Button(root,text="查询",command=wendu).grid(row=1,column=0)
label2 = Label(root,text="wendu").grid(row=1,column=1)



mainloop()






#print(get_html())
#print(city_name())
#print(city_number())
#print(new_list())
#chaxun()
#print(wendu())