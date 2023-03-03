from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
from PIL import Image,ImageTk
import pytz
import requests

root=Tk()
root.geometry("900x400")
root.title("Weather GUI")



height=root.winfo_screenwidth()
width=root.winfo_screenheight()



img=Image.open("bg1.png")
imgr=img.resize((1600,800))


img1=ImageTk.PhotoImage(imgr)
b_label=Label(root,image=img1)
b_label.place(x=0,y=0,relheight=1,relwidth=1)

label=Label(root,text="WEATHER REPORT",font=("Arial",30,"bold"),bg="chocolate1")
label.pack(pady=20)
frm1=Frame(root,bg="orange")
frm1.pack(pady=20)




text=Text(frm1,width=20,height=4,font=(("Arial",20,"bold")))
text.pack(pady=40,padx=20)




def current_time(utc):
    local_time=datetime.utcfromtimestamp(utc)
    return local_time.time()

frm=Frame(root,bg="medium spring green")
frm.pack(pady=20)


title=Label(frm,text="CURRENT WEATHER",font=("Arial",25,"bold"),bg="magenta1")
title.grid(row=0,column=2,pady=20,padx=20)

txt1=Label(frm,text="Temperature(degrees)",font=("Arial",20,"bold"),bg="cyan2")
txt1.grid(pady=20,row=1,column=0,padx=10)
t=Label(frm,font=("Arial",20,"bold"),bg="VioletRed1")
t.grid(row=2,column=0,pady=7,padx=20)

txt2=Label(frm,text="Pressure (hPa)",font=("Arial",20,"bold"),bg="cyan2")
txt2.grid(row=1,column=1,pady=20,padx=10)
p=Label(frm,font=("Arial",20,"bold"),bg="VioletRed1")
p.grid(row=2,column=1,pady=7,padx=10)

txt3=Label(frm,text="Humidity (%)",font=("Arial",20,"bold"),bg="cyan2")
txt3.grid(pady=20,row=1,column=2,padx=10)
h=Label(frm,font=("Arial",20,"bold"),bg="VioletRed1")
h.grid(row=2,column=2,pady=7,padx=20)

txt4=Label(frm,text="Windspeed (metres/sec)",font=("Arial",20,"bold"),bg="cyan2")
txt4.grid(pady=20,row=1,column=3,padx=10)
ws=Label(frm,font=("Arial",20,"bold"),bg="VioletRed1")
ws.grid(row=2,column=3,pady=7,padx=20)

txt=Label(frm,text="Visibility (metres)",font=("Arial",20,"bold"),bg="cyan2")
txt.grid(pady=20,row=1,column=4,padx=10)
vis=Label(frm,font=("Arial",20,"bold"),bg="VioletRed1")
vis.grid(row=2,column=4,pady=7,padx=20)

txt6=Label(frm,text="Sunrise",font=("Arial",20,"bold"),bg="cyan2")

txt6.grid(row=3,column=1)
sunr=Label(frm,font=("Arial",20,"bold"),bg="VioletRed1")
sunr.grid(row=4,column=1)

txt7=Label(frm,text="Sunset",font=("Arial",20,"bold"),bg="cyan2")
txt7.grid(row=3,column=3)
suns=Label(frm,font=("Arial",20,"bold"),bg="VioletRed1")
suns.grid(row=4,column=3,padx=20,pady=10)


# city=input("enter city")

def getweather():
    city=text.get("1.0",END)
    api='c3e5dfcd0b9a4db36c943250188feed4'
    user_response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}") 

    response=user_response.json()
    print(response)
    visi=response['visibility']
    vis.config(text=(visi))
    print(visi)

    wsp=response['wind']['speed']
    ws.config(text=(wsp))




    temp=int(response['main']['temp']-273)
    t.config(text=(temp))
    print(temp)
    pres=response['main']['pressure']
    p.config(text=(pres))
    print(pres)
    humidity=response['main']['humidity']
    humid=h.config(text=(humidity))
    timezone=response['timezone']
    sun1=response['sys']['sunrise']
    sunrise_time=current_time(sun1+timezone)        
    sunr.config(text=(sunrise_time))

    sun2=response['sys']['sunset']
    sunset_time=current_time(sun2+timezone)
    suns.config(text=(sunset_time))
btn=Button(frm1,text="Get Weather",command=getweather,font=("Arial",16,"bold"),bg="yellow")
btn.pack(padx=20,pady=20)

root.mainloop()
