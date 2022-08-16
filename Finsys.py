import email
from ssl import HAS_SNI
from sys import is_finalizing
from unicodedata import name
import matplotlib.pyplot as plt
from calendar import c
from cgitb import enable, reset, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from textwrap import wrap
from tkinter import font
from tkinter.font import BOLD
from urllib.parse import parse_qs
from PIL import ImageTk, Image, ImageFile
from matplotlib.font_manager import json_dump
from numpy import choose, empty, histogram_bin_edges, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import Tk, Canvas

import customtkinter
import PIL.Image
from PIL import ImageGrab
from PIL import ImageTk, Image, ImageFile
import PIL.Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import re
from datetime import date,datetime, timedelta
import webbrowser

import datetime

finsysdb = mysql.connector.connect(
    host="localhost", user="root", password="", database="newfinsys", port="3306"
)
fbcursor = finsysdb.cursor(buffered=True)

root=Tk()
root.geometry("1366x768+0+0")

root.title("Fin sYs")

p1 = PhotoImage(file = 'images/favicon.png')
root.iconphoto(False, p1)

#-------------------------------------------------------------------------------------------------------------------------Images
# banking = PhotoImage(file="images/banking.PNG")
# sales = PhotoImage(file="images/sheet.PNG")
# expenses = PhotoImage(file="images/expense.PNG")
# payroll = PhotoImage(file="images/payroll.PNG")
# report = PhotoImage(file="images/reports.PNG")
# taxes = PhotoImage(file="images/taxes.PNG")
# accounts = PhotoImage(file="images/accounting.PNG")

pro_pic =PIL.Image.open("profilepic\propic.jpg")
# resized_pro_pic= pro_pic.resize((170,170))
prof_pics=ImageTk.PhotoImage(pro_pic)

imgr1 =PIL.Image.open("images\logs.png")
exprefreshIcon=ImageTk.PhotoImage(imgr1)

notic =PIL.Image.open("images/bell.png")
noti=ImageTk.PhotoImage(notic)

mnu =PIL.Image.open("images\menu bar.PNG")
mnus=ImageTk.PhotoImage(mnu)


srh =PIL.Image.open("images\search.PNG")
srh_img=ImageTk.PhotoImage(srh)

stn =PIL.Image.open("images/brightness-solid-24.png")
stn_img=ImageTk.PhotoImage(stn)

logo =PIL.Image.open("images\logo-icon.png")
resized_image= logo.resize((50,50))
mai_logo= ImageTk.PhotoImage(resized_image)

sig_up =PIL.Image.open("images/register.png")
resized_sign_up= sig_up.resize((500,400))
sign_up=ImageTk.PhotoImage(resized_sign_up)

lowstock = PhotoImage(file="images/lowstock.png")
outofstock = PhotoImage(file="images/outofstock.png")
inventory = PhotoImage(file="images/inventory.png")
noninventory = PhotoImage(file="images/noninventory.png")
service = PhotoImage(file="images/service.png")
bundle = PhotoImage(file="images/bundle.png")



#------------------------------------------------------------------------------------------------------------Login Button Function

def main_sign_in():
    usr_nm=nm_ent.get()
    usr_pass=pass_ent.get()
    if usr_nm=="" or usr_pass=="" or usr_nm=="Username" or usr_pass=="Password":
        messagebox.showerror("Login Failed","Enter username and password")
    else:
        sql_log_sql='select * from auth_user where username=%s'
        sql_log_val=(usr_nm,)
        fbcursor.execute(sql_log_sql,sql_log_val)
        check_login=fbcursor.fetchone()

        if check_login is None:
            messagebox.showerror("Login Failed","Create an account")
        else:
            if check_login[4]==usr_nm and check_login[1]==usr_pass:
                try:
                    main_frame_signup.pack_forget()
                except:
                    pass
                try:
                    main_frame_signin.pack_forget()
                except:
                    pass
                Sys_top_frame=Frame(root, height=70,bg="#213b52")
                Sys_top_frame.pack(fill=X,)

                #---------------------------------------------------------------------------------------Top Menu
                tp_lb_nm=LabelFrame(Sys_top_frame,bg="#213b52")#-----------------------------Logo Name Frame
                tp_lb_nm.grid(row=1,column=1,sticky='nsew')
                tp_lb_nm.grid_rowconfigure(0,weight=1)
                tp_lb_nm.grid_columnconfigure(0,weight=1)

                label = Label(tp_lb_nm, image = mai_logo,height=70,bg="#213b52",border=0)
                label.grid(row=2,column=1,sticky='nsew')
                label = Label(tp_lb_nm, text="Fin sYs",bg="#213b52", fg="white",font=('Calibri 30 bold'),border=0)
                label.grid(row=2,column=2,sticky='nsew')
            
                mnu_btn = Button(tp_lb_nm, image=mnus, bg="white", fg="black",border=0)
                mnu_btn.grid(row=2,column=4,padx=50)

                

                tp_lb_srh=LabelFrame(Sys_top_frame,bg="#213b52")#-------------------------Serch area Frame
                tp_lb_srh.grid(row=1,column=2,sticky='nsew')
                tp_lb_srh.grid_rowconfigure(0,weight=1)
                tp_lb_srh.grid_columnconfigure(0,weight=1)

                def srh_fn(event):
                    if srh_top.get()=="Search":
                        srh_top.delete(0,END)
                    else:
                        pass

                srh_top = Entry(tp_lb_srh, width=50, font=('Calibri 16'))
                srh_top.insert(0,"Search")
                srh_top.bind("<Button-1>",srh_fn)
                srh_top.grid(row=2,column=1,padx=(30,0), pady=20,sticky='nsew')

                srh_btn = Button(tp_lb_srh, image=srh_img, bg="#213b52", fg="black",border=0)
                srh_btn.grid(row=2,column=4,padx=(0,30))

                #------------------------------------------------------settings 
                def close_lst_2():
                        lst_prf2.place_forget()
                        set_btn4 = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
                        set_btn4.grid(row=2,column=5,padx=(0,30))
                        
                def settings():
                    

                    # create a list box
                    stng = ("Accounts And Settings","Customize From Style","Chart Of Accounts")

                    stngs = StringVar(value=stng)
                    global lst_prf2
                    lst_prf2 = Listbox(root,listvariable=stngs,height=3 ,selectmode='extended',bg="black",fg="white")

                    lst_prf2.place(relx=0.70, rely=0.10)
                    lst_prf2.bind('<<ListboxSelect>>', )
                    set_btn.grid_forget()
                    set_btn2 = Button(tp_lb_srh, image=stn_img,command=close_lst_2, bg="#213b52", fg="black",border=0)
                    set_btn2.grid(row=2,column=5,padx=(0,30))

                set_btn = Button(tp_lb_srh, image=stn_img,command=settings, bg="#213b52", fg="black",border=0)
                set_btn.grid(row=2,column=5,padx=(0,30))

                tp_lb_nm=LabelFrame(Sys_top_frame,bg="#213b52")#-----------------------------Notification
                tp_lb_nm.grid(row=1,column=3,sticky='nsew')
                tp_lb_nm.grid_rowconfigure(0,weight=1)
                tp_lb_nm.grid_columnconfigure(0,weight=1)
                srh_btn = Button(tp_lb_nm, image=noti, bg="#213b52", fg="black",border=0)
                srh_btn.grid(row=0,column=0,padx=35)
                
                tp_lb_npr=LabelFrame(Sys_top_frame,bg="#213b52")#---------------------------profile area name
                tp_lb_npr.grid(row=1,column=4,sticky='nsew')
                tp_lb_npr.grid_rowconfigure(0,weight=1)
                tp_lb_npr.grid_columnconfigure(0,weight=1)

                us_sql = "SELECT * FROM auth_user WHERE username=%s"
                us_val = (nm_ent.get(),)
                fbcursor.execute(us_sql,us_val)
                us_data = fbcursor.fetchone()

                cm_sql = "SELECT * FROM app1_company WHERE id_id=%s"
                cm_val = (us_data[0],)
                fbcursor.execute(cm_sql,cm_val)
                cm_data = fbcursor.fetchone()

                label = Label(tp_lb_npr, text=cm_data[1],bg="#213b52", fg="white", anchor="center",width=10,font=('Calibri 16 bold'),border=0)
                label.grid(row=1,column=1,sticky='nsew')
                label = Label(tp_lb_npr, text="Online",bg="#213b52", fg="white",width=15,font=('Calibri 12 bold'),border=0)
                label.grid(row=2,column=1,sticky='nsew')

                pro =PIL.Image.open("images/user.png")
                resized_pro= pro.resize((20,20))
                pro_pic= ImageTk.PhotoImage(resized_pro)
                
                def lst_frt():
                    lst_prf.place_forget()
                    srh_btn3 = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=profile)
                    srh_btn3.grid(row=2,column=2,padx=15)
                def lst_prf_slt(event):
                    def edit_profile():
                        def responsive_widgets_edit(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                            


                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/13
                            y2 = dheight/.53

                            dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
                            x1 + r1,y1,
                            x2 - r1,y1,
                            x2 - r1,y1,     
                            x2,y1,     
                            #--------------------
                            x2,y1 + r1,     
                            x2,y1 + r1,     
                            x2,y2 - r1,     
                            x2,y2 - r1,     
                            x2,y2,
                            #--------------------
                            x2 - r1,y2,     
                            x2 - r1,y2,     
                            x1 + r1,y2,
                            x1 + r1,y2,
                            x1,y2,
                            #--------------------
                            x1,y2 - r1,
                            x1,y2 - r1,
                            x1,y1 + r1,
                            x1,y1 + r1,
                            x1,y1,
                            )                              

                            
                            # dcanvas.coords("bg_polygen_pr",dwidth/16,dheight/.6,dwidth/1.07,dheight/9)
                            dcanvas.coords("my_pro",dwidth/2.3,dheight/12.5)
                            dcanvas.coords("pr_img",dwidth/2.3,dheight/5)
                            

                            dcanvas.coords("pr_hr_l",dwidth/16,dheight/6.5,dwidth/1.07,dheight/6.5)
                            dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                            dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                            dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                            dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                            dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                            dcanvas.coords("pr_crpass_lb",dwidth/17.075,dheight/1.33)
                            dcanvas.coords("pr_crpass_ent",dwidth/17.075,dheight/1.26)
                            dcanvas.coords("pr_re_pass_lb",dwidth/17.075,dheight/1.16)
                            dcanvas.coords("pr_re_pass_ent",dwidth/17.075,dheight/1.1)
                            dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                            dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                            dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                            dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)
                            dcanvas.coords("pr_new_pass_lb",dwidth/1.92,dheight/1.33)
                            dcanvas.coords("pr_new_pass_ent",dwidth/1.92,dheight/1.26)

                            
                            #-------------------------------------------------------------------------company section
                            dcanvas.coords("cmp_hd",dwidth/20,dheight/1)
                            dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/0.93)
                            dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/0.89)
                            dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/0.84)
                            dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/0.81)
                            dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/0.77)
                            dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.745)
                            dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.712)
                            dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.69)
                            dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.66)
                            dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.64)
                            dcanvas.coords("cmp_file_lb",dwidth/17.075,dheight/.615)
                            dcanvas.coords("cmp_file_ent",dwidth/17.075,dheight/.6)
                            

                            #--------------------------------------------------------------------------company right

                            dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/0.93)
                            dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/0.89)
                            dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/0.84)
                            dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/0.81)
                            dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/0.77)
                            dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.745)
                            dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.712)
                            dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.69)
                            dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.66)
                            dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.64)
                            dcanvas.coords("btn_edit",dwidth/2.4,dheight/.57)
                        sql_pro="select * from auth_user where username=%s"
                        sql_pro_val=(nm_ent.get(),)
                        fbcursor.execute(sql_pro,sql_pro_val,)
                        edi_dtl=fbcursor.fetchone()

                        def update_profile():
                            first_name=fr_name_ent.get()
                            pro_email=em_ent.get()
                            last_name=lst_nm_ent.get()
                            pro_username=usr_nm_ent.get()
                            pro_new_pass=pr_new_pass_ent.get()
                            if pro_new_pass==pr_re_pass_ent.get() and pr_re_pass_ent.get()==pro_new_pass:
                                if pr_crpass_ent.get()==edi_dtl[1]:
                                    prof_edit="update auth_user set first_name=%s,last_name=%s,email=%s,username=%s,password=%s where id=%s" #adding values into db
                                    prof_edit_val=(first_name,last_name,pro_email,pro_username,pro_new_pass,edi_dtl[0])
                                    fbcursor.execute(prof_edit,prof_edit_val)
                                    finsysdb.commit()

                                    #compnay
                                    cmp_name=cmp_nm_ent.get()
                                    cmp_cty=cmp_cty_ent.get()
                                    cmp_pin=cmp_pin_ent.get()
                                    cmp_phn=cmp_ph_ent.get()
                                    cmp_ind=cmp_indest_ent.get()
                                    cmp_addr=cmp_addr_ent.get()
                                    cmp_st=cmp_st_ent.get()
                                    cmp_em=cmp_em_ent.get()
                                    cmp_bname=cmp_lg_ent.get()
                                    cmp_typ=cmp_typ_ent.get()
                                    logo=cmp_file_ent.get()

                                    cmp_edit="update app1_company set cname=%s,caddress=%s,city=%s,state=%s,pincode=%s,cemail=%s,phone=%s,cimg=%s,bname=%s,industry=%s,ctype=%s where id_id =%s" #adding values into db
                                    cmp_edit_val=(cmp_name,cmp_addr,cmp_cty,cmp_st,cmp_pin,cmp_em,cmp_phn,logo,cmp_bname,cmp_ind,cmp_typ,edi_dtl[0])
                                    fbcursor.execute(cmp_edit,cmp_edit_val)
                                    finsysdb.commit()
                                    messagebox.showerror("Sucess","Updation Success")
                                else:
                                    messagebox.showerror("Updation Failed","Please check your current password")
                            else:

                                messagebox.showerror("Updation Failed","password and conform password does not match")
                        
                        sql_pro_cmp="select * from app1_company where id_id=%s"
                        sql_pro_cmp_val=(pro_dtl[0],)
                        fbcursor.execute(sql_pro_cmp,sql_pro_cmp_val,)
                        edi_cmp_dtl=fbcursor.fetchone()

                        Sys_mains_frame_pr.place_forget()
                        global Sys_mains_frame_pr_ed
                        Sys_mains_frame_pr_ed=Frame(tab1, height=750)
                        Sys_mains_frame_pr_ed.grid(row=0,column=0,sticky='nsew')
                        Sys_mains_frame_pr_ed.grid_rowconfigure(0,weight=1)
                        Sys_mains_frame_pr_ed.grid_columnconfigure(0,weight=1)

                        pr_canvas_ed=Canvas(Sys_mains_frame_pr_ed,height=766,width=1340,scrollregion=(0,0,766,1650),bg="#2f516f",border=0)
                        pr_canvas_ed.bind('<Configure>', responsive_widgets_edit)
                        
                        pr_myscrollbar_ed=Scrollbar(Sys_mains_frame_pr_ed,orient="vertical",command=pr_canvas_ed.yview)
                        pr_canvas_ed.configure(yscrollcommand=pr_myscrollbar_ed.set)

                        pr_myscrollbar_ed.pack(side="right",fill="y")
                        pr_canvas_ed.pack(fill=X)

                        rth2 = pr_canvas_ed.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_pr"),smooth=True,)


                        grd1c=Label(pr_canvas_ed, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                        win_inv1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

                        pr_img=Label(pr_canvas_ed,  image = prof_pics,bg="#213b52",width=170,height=170,  anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_img,tags=("pr_img"))

                        pr_canvas_ed.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
                        #----------------------------------------------------------------------------------------Personal info
                        pr_hd=Label(pr_canvas_ed, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                        win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

                        fir_name=Label(pr_canvas_ed, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

                        fr_name_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        fr_name_ent.delete(0,END)
                        fr_name_ent.insert(0,edi_dtl[5])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

                        pr_em_lb=Label(pr_canvas_ed, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

                        em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        em_ent.delete(0,END)
                        em_ent.insert(0,edi_dtl[7])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

                        pr_crpass_lb=Label(pr_canvas_ed, text="Enter your Current Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_lb,tag=("pr_crpass_lb"))

                        pr_crpass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_ent,tag=("pr_crpass_ent"))

                        pr_re_pass_lb=Label(pr_canvas_ed, text="Re-type new Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_lb,tag=("pr_re_pass_lb"))

                        pr_re_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_ent,tag=("pr_re_pass_ent"))


                        last_nm_lb=Label(pr_canvas_ed, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

                        lst_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        lst_nm_ent.delete(0,END)
                        lst_nm_ent.insert(0,edi_dtl[6])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

                        usr_nm_lb=Label(pr_canvas_ed, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

                        usr_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        usr_nm_ent.delete(0,END)
                        usr_nm_ent.insert(0,edi_dtl[4])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

                        pr_new_pass_lb=Label(pr_canvas_ed, text="Enter New Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_lb,tag=("pr_new_pass_lb"))

                        pr_new_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_ent,tag=("pr_new_pass_ent"))


                        # #------------------------------------------------------------------------------------------------COMPANY SECTION
                        cmp_hd=Label(pr_canvas_ed, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                        win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

                        cmp_nm_lb=Label(pr_canvas_ed, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

                        cmp_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_nm_ent.delete(0,END)
                        cmp_nm_ent.insert(0,edi_cmp_dtl[1])
                        
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

                        cmp_cty_lb=Label(pr_canvas_ed, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

                        cmp_cty_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_cty_ent.delete(0,END)
                        cmp_cty_ent.insert(0,edi_cmp_dtl[3])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

                        cmp_pin_lb=Label(pr_canvas_ed, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

                        cmp_pin_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_pin_ent.delete(0,END)
                        cmp_pin_ent.insert(0,edi_cmp_dtl[5])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

                        cmp_ph_lb=Label(pr_canvas_ed, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

                        cmp_ph_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_ph_ent.delete(0,END)
                        cmp_ph_ent.insert(0,edi_cmp_dtl[7])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

                        cmp_indest_lb=Label(pr_canvas_ed, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

                        cmp_indest_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_indest_ent.delete(0,END)
                        cmp_indest_ent.insert(0,edi_cmp_dtl[10])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

                        # #----------------------------------------------------------------------------------------------------RIGHT SIDE
                        cmp_addr_lb=Label(pr_canvas_ed, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

                        cmp_addr_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_addr_ent.delete(0,END)
                        cmp_addr_ent.insert(0,edi_cmp_dtl[2])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

                        cmp_st_lb=Label(pr_canvas_ed, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

                        cmp_st_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_st_ent.delete(0,END)
                        cmp_st_ent.insert(0,edi_cmp_dtl[4])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

                        cmp_em_lb=Label(pr_canvas_ed, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

                        cmp_em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_em_ent.delete(0,END)
                        cmp_em_ent.insert(0,edi_cmp_dtl[6])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

                        cmp_lg_nm=Label(pr_canvas_ed, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

                        cmp_lg_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_lg_ent.delete(0,END)
                        cmp_lg_ent.insert(0,edi_cmp_dtl[9])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

                        cmp_typ_lb=Label(pr_canvas_ed, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

                        cmp_typ_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_typ_ent.delete(0,END)
                        cmp_typ_ent.insert(0,edi_cmp_dtl[11])
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))

                        cmp_file_lb=Label(pr_canvas_ed, text="File",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_lb,tag=("cmp_file_lb"))
                        def fil_ents(event):
                    
                            cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
                            logo_crp=cmp_logo.split('/',-1)
                            
                            im1 = Image.open(r""+cmp_logo) 
                            im1 = im1.save("profilepic/propic.jpg")

                            cmp_file_ent.delete(0,END)
                            cmp_file_ent.insert(0,logo_crp[-1])

                        cmp_file_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
                        cmp_file_ent.delete(0,END)
                        cmp_file_ent.insert(0,edi_cmp_dtl[8])
                        cmp_file_ent.bind("<Button-1>",fil_ents)
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_ent,tag=("cmp_file_ent"))


                        btn_edit = Button(pr_canvas_ed, text='Update Profile', command=update_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
                        win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))

                    
                    selected_indices = lst_prf.curselection()
                    selected_langs = ",".join([lst_prf.get(i) for i in selected_indices])
                    lst_prf.place_forget()

                    def pr_responsive_widgets(event):
                            
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                        
                            
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/13
                            y2 = dheight/.6

                            dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
                            x1 + r1,y1,
                            x2 - r1,y1,
                            x2 - r1,y1,     
                            x2,y1,     
                            #--------------------
                            x2,y1 + r1,     
                            x2,y1 + r1,     
                            x2,y2 - r1,     
                            x2,y2 - r1,     
                            x2,y2,
                            #--------------------
                            x2 - r1,y2,     
                            x2 - r1,y2,     
                            x1 + r1,y2,
                            x1 + r1,y2,
                            x1,y2,
                            #--------------------
                            x1,y2 - r1,
                            x1,y2 - r1,
                            x1,y1 + r1,
                            x1,y1 + r1,
                            x1,y1,
                            )                   
            
                            dcanvas.coords("my_pro",dwidth/2.3,dheight/13)
                            dcanvas.coords("pr_img",dwidth/2.3,dheight/5)

                            dcanvas.coords("pr_hr_l",dwidth/16,dheight/6.5,dwidth/1.07,dheight/6.5)
                            dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                            dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                            dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                            
                            dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                            dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                            dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                            dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                            dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                            dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)

                            #-------------------------------------------------------------------------company section
                            dcanvas.coords("cmp_hd",dwidth/20,dheight/1.32)
                            dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/1.22)
                            dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/1.16)
                            dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/1.07)
                            dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/1.02)
                            dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/.95)
                            dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.91)
                            dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.86)
                            dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.83)
                            dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.78)
                            dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.755)

                            #--------------------------------------------------------------------------company right

                            dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/1.22)
                            dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/1.16)
                            dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/1.07)
                            dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/1.02)
                            dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/.95)
                            dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.91)
                            dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.86)
                            dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.83)
                            dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.78)
                            dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.755)
                            dcanvas.coords("btn_edit",dwidth/2.4,dheight/.71)

                    if selected_langs=="Profile":
                        # canvas.pack_forget()
                        # myscrollbar.pack_forget()
                        # Sys_mains_frame.pack_forget()
                        
                        sql_pro="select * from auth_user where username=%s"
                        sql_pro_val=(nm_ent.get(),)
                        fbcursor.execute(sql_pro,sql_pro_val,)
                        pro_dtl=fbcursor.fetchone()

                        sql_pro_cmp="select * from app1_company where id_id=%s"
                        sql_pro_cmp_val=(pro_dtl[0],)
                        fbcursor.execute(sql_pro_cmp,sql_pro_cmp_val,)
                        pro_cmp_dtl=fbcursor.fetchone()
                        

                        Sys_mains_frame_pr=Frame(tab1, height=750,bg="#2f516f",)
                        Sys_mains_frame_pr.grid(row=0,column=0,sticky='nsew')
                        Sys_mains_frame_pr.grid_rowconfigure(0,weight=1)
                        Sys_mains_frame_pr.grid_columnconfigure(0,weight=1)

                        pr_canvas=Canvas(Sys_mains_frame_pr,height=700,width=1340,scrollregion=(0,0,700,1300),bg="#2f516f",border=0)
                        pr_canvas.bind("<Configure>", pr_responsive_widgets)
                        
                        pr_myscrollbar=Scrollbar(Sys_mains_frame_pr,orient="vertical",command=pr_canvas.yview)
                        pr_canvas.configure(yscrollcommand=pr_myscrollbar.set)

                        pr_myscrollbar.pack(side="right",fill="y")
                        pr_canvas.pack(fill=X)

                        rth2 = pr_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",smooth=True,tags=("bg_polygen_pr"))

                        grd1c=Label(pr_canvas, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
                        win_inv1 = pr_canvas.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

                        pr_canvas.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
                        #----------------------------------------------------------------------------------------Personal info

        
                        pr_img=Label(pr_canvas, image = prof_pics,bg="#213b52",width=170,height=170, anchor="center",)
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=pr_img,tags=("pr_img"))

                        pr_hd=Label(pr_canvas, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                        win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

                        fir_name=Label(pr_canvas, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

                        fr_name_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        fr_name_ent.delete(0,END)
                        fr_name_ent.insert(0,pro_dtl[5])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

                        pr_em_lb=Label(pr_canvas, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

                        em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        em_ent.delete(0,END)
                        em_ent.insert(0,pro_dtl[7])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

                        last_nm_lb=Label(pr_canvas, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

                        lst_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        lst_nm_ent.delete(0,END)
                        lst_nm_ent.insert(0,pro_dtl[6])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

                        usr_nm_lb=Label(pr_canvas, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

                        usr_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        usr_nm_ent.delete(0,END)
                        usr_nm_ent.insert(0,pro_dtl[4])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

                        #------------------------------------------------------------------------------------------------COMPANY SECTION
                        cmp_hd=Label(pr_canvas, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
                        win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

                        cmp_nm_lb=Label(pr_canvas, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

                        cmp_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_nm_ent.delete(0,END)
                        cmp_nm_ent.insert(0,pro_cmp_dtl[1])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

                        cmp_cty_lb=Label(pr_canvas, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

                        cmp_cty_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_cty_ent.delete(0,END)
                        cmp_cty_ent.insert(0,pro_cmp_dtl[3])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

                        cmp_pin_lb=Label(pr_canvas, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

                        cmp_pin_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_pin_ent.delete(0,END)
                        cmp_pin_ent.insert(0,pro_cmp_dtl[5])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

                        cmp_ph_lb=Label(pr_canvas, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

                        cmp_ph_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_ph_ent.delete(0,END)
                        cmp_ph_ent.insert(0,pro_cmp_dtl[7])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

                        cmp_indest_lb=Label(pr_canvas, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

                        cmp_indest_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_indest_ent.delete(0,END)
                        cmp_indest_ent.insert(0,pro_cmp_dtl[10])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

                        #----------------------------------------------------------------------------------------------------RIGHT SIDE
                        cmp_addr_lb=Label(pr_canvas, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

                        cmp_addr_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_addr_ent.delete(0,END)
                        cmp_addr_ent.insert(0,pro_cmp_dtl[2])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

                        cmp_st_lb=Label(pr_canvas, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

                        cmp_st_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_st_ent.delete(0,END)
                        cmp_st_ent.insert(0,pro_cmp_dtl[4])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

                        cmp_em_lb=Label(pr_canvas, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

                        cmp_em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_em_ent.delete(0,END)
                        cmp_em_ent.insert(0,pro_cmp_dtl[6])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

                        cmp_lg_nm=Label(pr_canvas, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

                        cmp_lg_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_lg_ent.delete(0,END)
                        cmp_lg_ent.insert(0,pro_cmp_dtl[9])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

                        cmp_typ_lb=Label(pr_canvas, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
                        win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

                        cmp_typ_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
                        cmp_typ_ent.delete(0,END)
                        cmp_typ_ent.insert(0,pro_cmp_dtl[11])
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))


                        btn_edit = Button(pr_canvas, text='Edit Profile', command=edit_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
                        win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))
                    
                    elif selected_langs=="Log Out":
                        
                        Sys_top_frame2.pack_forget()
                        Sys_top_frame.pack_forget()
                        main_frame_signin.pack(fill=X,)
                    elif selected_langs== "Dashboard":
                        try:
                            Sys_mains_frame_pr_ed.place_forget()
                        except:
                            pass
                        try:
                            
                            Sys_mains_frame_pr.place_forget()
                        except:
                            pass

                    else:
                        pass

                def profile():
                    # create a list box
                    langs = ("Dashboard","Profile","Log Out")

                    langs_var = StringVar(value=langs)
                    global lst_prf
                    lst_prf = Listbox(root,listvariable=langs_var,height=3 ,selectmode='extended',bg="black",fg="white")

                    lst_prf.place(relx=0.90, rely=0.10)
                    lst_prf.bind('<<ListboxSelect>>', lst_prf_slt)
                    srh_btn.grid_forget()
                    srh_btn2 = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=lst_frt)
                    srh_btn2.grid(row=2,column=2,padx=15)
            
                srh_btn = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=profile)
                srh_btn.grid(row=2,column=2,padx=15)

                Sys_top_frame2=Frame(root, height=10,bg="#213b52")
                Sys_top_frame2.pack(fill=X,)
                
                s = ttk.Style()
                s.theme_use('default')
                s.configure('TNotebook.Tab', background="#213b52",foreground="white", width=150,anchor="center", padding=5)
                s.map('TNotebook.Tab',background=[("selected","#2f516f")])
                def right_nav():
                    
                    tabControl.pack_forget()
                    btn_nav.place_forget()
                    tabControl2.pack(expand = 1, fill ="both")
                    btn_nav2.place(relx=0, rely=0)
                    try:
                        btn_nav3.place_forget()
                    except:
                        pass
                def left_nav():
                    
                    tabControl2.pack_forget()
                    btn_nav2.place_forget()
                    tabControl.pack(expand = 1, fill ="both")
                    global btn_nav3
                    btn_nav3=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
                    btn_nav3.place(relx=0.97, rely=0)

                tabControl = ttk.Notebook(Sys_top_frame2)
                tab1 = ttk.Frame(tabControl)
                tab2 = ttk.Frame(tabControl)
                tab3=  ttk.Frame(tabControl)
                tab4 = ttk.Frame(tabControl)
                tab5 = ttk.Frame(tabControl)
                tab6=  ttk.Frame(tabControl)
                tab7 = ttk.Frame(tabControl)
                tab8 = ttk.Frame(tabControl)
                
                
                btn_nav=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
                btn_nav.place(relx=0.97, rely=0)
                tabControl.add(tab1,compound = LEFT, text ='Dashboard',)
                tabControl.add(tab2,compound = LEFT, text ='Banking')
                tabControl.add(tab3,compound = LEFT, text ='Sales')
                tabControl.add(tab4,compound = LEFT, text ='Expenses')
                tabControl.add(tab5,compound = LEFT, text ='Payroll') 
                tabControl.add(tab6,compound = LEFT, text ='Report')
                tabControl.add(tab7,compound = LEFT, text ='Taxes')
                tabControl.add(tab8,compound = LEFT, text ='Accounting')
                
                tabControl.pack(expand = 1, fill ="both")


                
                tabControl2 = ttk.Notebook(Sys_top_frame2)
                tab9 =  ttk.Frame(tabControl2)
                tab10=  ttk.Frame(tabControl2)
                tab11 = ttk.Frame(tabControl2)
                tab12=  ttk.Frame(tabControl2)
                tab13 = ttk.Frame(tabControl2)
                tab14 = ttk.Frame(tabControl2)
                tab15 =  ttk.Frame(tabControl2)

                btn_nav2=Button(Sys_top_frame2,text="<<", command=left_nav, width=3, bg="#213b52",fg="white")
                
                    
                tabControl2.add(tab9,compound = LEFT, text ='My Account')
                tabControl2.add(tab10,compound = LEFT, text ='Cash Management')
                tabControl2.add(tab11,compound = LEFT, text ='Production')
                tabControl2.add(tab12,compound = LEFT, text ='Quality Management')
                tabControl2.add(tab13,compound = LEFT, text ='Project Management')
                tabControl2.add(tab14,compound = LEFT, text ='Usage Decisions')
                tabControl2.add(tab15,compound = LEFT, text ='Account & Payable')

            
                #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Dash Board}
                tab1.grid_columnconfigure(0,weight=1)
                tab1.grid_rowconfigure(0,weight=1)
                
                Sys_mains_frame=Frame(tab1,bg="#2f516f",)
                Sys_mains_frame.grid(row=0,column=0,sticky='nsew')
                
                def responsive_wid(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
                
                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/1.021
                    y1 = dheight/13
                    y2 = dheight/6

                    dcanvas.coords("bg_polygen_dash",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )                    

                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/3.1
                    y1 = dheight/5
                    y2 = dheight/1.1

                    dcanvas.coords("bg_polygen_dash1",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    r1 = 25
                    x1 = dwidth/2.95
                    x2 = dwidth/1.529
                    y1 = dheight/5
                    y2 = dheight/1.1

                    dcanvas.coords("bg_polygen_dash2",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    r1 = 25
                    x1 = dwidth/1.49
                    x2 = dwidth/1.021
                    y1 = dheight/5
                    y2 = dheight/1.1

                    dcanvas.coords("bg_polygen_dash3",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/3.1
                    y1 = dheight/1.06
                    y2 = dheight/.59
                    
                    #-----------------------------------------second row
                    dcanvas.coords("bg_polygen_dash4",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    r1 = 25
                    x1 = dwidth/2.95
                    x2 = dwidth/1.529
                    y1 = dheight/1.06
                    y2 = dheight/.59

                    dcanvas.coords("bg_polygen_dash5",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    r1 = 25
                    x1 = dwidth/1.49
                    x2 = dwidth/1.021
                    y1 = dheight/1.06
                    y2 = dheight/.59

                    dcanvas.coords("bg_polygen_dash6",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    dcanvas.coords("head_lb",dwidth/2,dheight/8.4)
                    dcanvas.coords("prf_lb",dwidth/53,dheight/4.7)
                    
                    dcanvas.coords("prf_hr",dwidth/53,dheight/3.7,dwidth/3.15,dheight/3.7)
                    dcanvas.coords("net_prf",dwidth/53,dheight/3.2)
                    dcanvas.coords("graph",dwidth/53,dheight/2.2)
                    #--------------------------------------------------------------second
                    dcanvas.coords("exp_hd_lb",dwidth/2.9,dheight/4.7)
                    dcanvas.coords("exp_hr",dwidth/2.9,dheight/3.7,dwidth/1.54,dheight/3.7)
                    dcanvas.coords("graph_2",dwidth/2.9,dheight/2.2)
                    
                    #-----------------------------------------------------------third
                    dcanvas.coords("bnk_lb",dwidth/1.48,dheight/4.7)
                    dcanvas.coords("bank_hr",dwidth/1.48,dheight/3.7,dwidth/1.03,dheight/3.7)
                    #--------------------------------------------------------------forth
                    dcanvas.coords("incom_lb",dwidth/53,dheight/1.04)
                    
                    dcanvas.coords("incom_hr",dwidth/53,dheight/0.99,dwidth/3.15,dheight/0.99)

                
                    dcanvas.coords("graph_4",dwidth/53,dheight/0.85)
            
                    #-------------------------------------------------------------fifth
                    dcanvas.coords("inv_lb",dwidth/2.9,dheight/1.04)
                    dcanvas.coords("invs_hr",dwidth/2.9,dheight/0.99,dwidth/1.54,dheight/0.99)
                    dcanvas.coords("inv_lb2",dwidth/2.9,dheight/0.95)
                    dcanvas.coords("inv_lb3",dwidth/2.9,dheight/0.90)
                    dcanvas.coords("graph_5",dwidth/2.9,dheight/0.85)
                    #-------------------------------------------------------------sixth
                    dcanvas.coords("sales_lb",dwidth/1.48,dheight/1.04)
                    dcanvas.coords("sales_hr",dwidth/1.48,dheight/0.99,dwidth/1.03,dheight/0.99)
                    
                    


                    dcanvas.coords("grapg_6",dwidth/1.48,dheight/0.85)
                        
                Sys_mains_frame.grid_rowconfigure(0,weight=1)
                Sys_mains_frame.grid_columnconfigure(0,weight=1)

                canvas = Canvas(Sys_mains_frame,height=700,bg='#2f516f',scrollregion=(0,0,700,1200))
                sr_Scroll = Scrollbar(Sys_mains_frame,orient=VERTICAL)
                sr_Scroll.grid(row=0,column=1,sticky='ns')
                sr_Scroll.config(command=canvas.yview)
                canvas.bind("<Configure>", responsive_wid)
                canvas.config(yscrollcommand=sr_Scroll.set)
                canvas.grid(row=0,column=0,sticky='nsew')
                

                cmp_name=Label(canvas, text="Clown",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
            
                win_inv1 = canvas.create_window(0, 0, anchor="center", window=cmp_name,tag=("head_lb"))
                
                rth2 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash"),smooth=True,)
                # #----------------------------------------------------------------------------------------------------------------grid 1
                rth1 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash1"),smooth=True,)

                prf_lb=Label(canvas, text="PROFIT AND LOSS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=prf_lb, tag=("prf_lb"))

                canvas.create_line(0, 0, 0, 0,fill="gray", tag=("prf_hr") )

                net_prf=Label(canvas, text="NET INCOME: ₹ 0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=net_prf,tag=("net_prf"))

                figlast = plt.figure(figsize=(8, 4), dpi=50)

                x="Income"
                y=10 
                plt.barh(x,y, label="Undefined", color="blue") 
                plt.legend()
            
                plt.ylabel("")
                axes=plt.gca()
                axes.xaxis.grid()

                x="Expense"
                y=100
                plt.barh(x,y, color="red") 
                plt.legend()
            
                plt.ylabel("")
                axes=plt.gca()
                axes.xaxis.grid()
                        

                canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
                canvasbar
                canvasbar.draw()
                canvasbar.get_tk_widget()
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph"))
                # #----------------------------------------------------------------------------------------------------------------grid 2
                rth2 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash2"),smooth=True,)

                exp_hd_lb=Label(canvas, text="EXPENSES: ₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=exp_hd_lb, tag=("exp_hd_lb"))
                canvas.create_line(0, 0, 0, 0,fill="gray" ,tag=("exp_hr"))
                fig, ax = plt.subplots(figsize=(8, 4), dpi=50)

                size = 0.3
                vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

                cmap = plt.colormaps["tab20c"]
                outer_colors = cmap(np.arange(3)*4)
                # inner_colors = cmap([1, 2, 5, 6, 9, 10])

                ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
                    wedgeprops=dict(width=size, edgecolor='w'))

                # ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
                #        wedgeprops=dict(width=size, edgecolor='w'))

                ax.set(aspect="equal", title='Pie plot with `ax.pie`')

                canvasbar = FigureCanvasTkAgg(fig, master=canvas)
                canvasbar
                canvasbar.draw()
                canvasbar.get_tk_widget()
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_2"))

                # #----------------------------------------------------------------------------------------------------------------grid 3
                rth3 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash3"),smooth=True,)

                bnk_lb=Label(canvas, text="BANK ACCOUNTS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=bnk_lb,tag=("bnk_lb"))
                canvas.create_line(910, 195, 1290, 195,fill="gray",tag=("bank_hr"))
                # #----------------------------------------------------------------------------------------------------------------grid 4
                rth4 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash4"),smooth=True,)

                incom_lb=Label(canvas, text="INCOME: ₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=incom_lb,tag=("incom_lb"))
                canvas.create_line(0, 0, 0, 0,fill="gray",tag=("incom_hr") )

                # Pie chart, where the slices will be ordered and plotted counter-clockwise:
                labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
                sizes = [15, 30, 45, 10]
                explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

                fig1, ax1 = plt.subplots(figsize=(8, 4), dpi=50)
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                        shadow=True, startangle=90)
                ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

                canvasbar = FigureCanvasTkAgg(fig1, master=canvas)
                canvasbar
                canvasbar.draw()
                canvasbar.get_tk_widget()
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_4"))

                # #----------------------------------------------------------------------------------------------------------------grid 5
                rth5 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash5"),smooth=True,)
                inv_lb=Label(canvas, text="INVOICE",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb, tag=("inv_lb"))

                canvas.create_line(0, 0, 0, 0,fill="gray", tag=("invs_hr") )
                inv_lb2=Label(canvas, text="UNPAID:₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=inv_lb2, tag=("inv_lb2"))
                inv_lb3=Label(canvas, text="PAID:₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0,0 , anchor="nw", window=inv_lb3, tag=("inv_lb3"))

                figlast = plt.figure(figsize=(8, 4), dpi=50)

                x="Unpaid"
                y=10 
                plt.barh(x,y, label="Undefined", color="blue") 
                plt.legend()
            
                plt.ylabel("")
                axes=plt.gca()
                axes.xaxis.grid()

                x="Paid"
                y=100
                plt.barh(x,y, color="red") 
                plt.legend()
            
                plt.ylabel("")
                axes=plt.gca()
                axes.xaxis.grid()
                        

                canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
                canvasbar
                canvasbar.draw()
                canvasbar.get_tk_widget()
                win_inv1 = canvas.create_window(480, 780, anchor="nw", window=canvasbar.get_tk_widget(), tag=("graph_5"))
                #----------------------------------------------------------------------------------------------------------------grid 6
                rth6 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash6"),smooth=True,)
                sales_lb=Label(canvas, text="SALES $0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=sales_lb, tag=("sales_lb"))

                canvas.create_line(0, 0, 0, 0,fill="gray", tag=("sales_hr") )
                
                
                fig, ax = plt.subplots(figsize=(8, 4), dpi=50)
                ax.plot(range(10))
                ax.set_yticks([2, 5, 7], labels=['really, really, really', 'long', 'labels'])
            

                canvasbar = FigureCanvasTkAgg(fig, master=canvas)
                canvasbar
                canvasbar.draw()
                canvasbar.get_tk_widget()
                win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("grapg_6"))
                
                #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333Banking Section(Tab2)

                tab_bank = ttk.Notebook(tab2)
                tab2_1 =  ttk.Frame(tab_bank)
                tab2_2=  ttk.Frame(tab_bank)
                tab2_3 = ttk.Frame(tab_bank)

                tab_bank.add(tab2_1,compound = LEFT, text ='Online Banking')
                tab_bank.add(tab2_2,compound = LEFT, text ='Offline banking')
                tab_bank.add(tab2_3,compound = LEFT, text ='Bank Reconvilation')

                
                tab_bank.pack(expand = 1, fill ="both")

                #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Sales Tab}
                tab_sales = ttk.Notebook(tab3)
                tab3_1 =  ttk.Frame(tab_sales)
                tab3_2=  ttk.Frame(tab_sales)
                tab3_3 = ttk.Frame(tab_sales)
                tab3_4=  ttk.Frame(tab_sales)

                
                    
                tab_sales.add(tab3_1,compound = LEFT, text ='Sales Records')
                tab_sales.add(tab3_2,compound = LEFT, text ='Invoices')
                tab_sales.add(tab3_3,compound = LEFT, text ='Customers')
                tab_sales.add(tab3_4,compound = LEFT, text ='Product & Services')
            
                tab_sales.pack(expand = 1, fill ="both")

                #--------------------------------Invoices-----------------------------#
                tab3_2.grid_columnconfigure(0,weight=1)
                tab3_2.grid_rowconfigure(0,weight=1)

                inv_frame = Frame(tab3_2)
                inv_frame.grid(row=0,column=0,sticky='nsew')

                def inv_responsive_widgets(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget

                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/1.021
                    y1 = dheight/14 
                    y2 = dheight/3.505

                    dcanvas.coords("ipoly1",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    dcanvas.coords("ihline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                    dcanvas.coords("ilabel1",dwidth/2.5,dheight/8.00)

                    r2 = 25
                    x11 = dwidth/63
                    x21 = dwidth/1.021
                    y11 = dheight/2.8
                    y21 = dheight/0.8


                    dcanvas.coords("ipoly2",x11 + r2,y11,
                    x11 + r2,y11,
                    x21 - r2,y11,
                    x21 - r2,y11,     
                    x21,y11,     
                    #--------------------
                    x21,y11 + r2,     
                    x21,y11 + r2,     
                    x21,y21 - r2,     
                    x21,y21 - r2,     
                    x21,y21,
                    #--------------------
                    x21 - r2,y21,     
                    x21 - r2,y21,     
                    x11 + r2,y21,
                    x11 + r2,y21,
                    x11,y21,
                    #--------------------
                    x11,y21 - r2,
                    x11,y21 - r2,
                    x11,y11 + r2,
                    x11,y11 + r2,
                    x11,y11,
                    )


                   
                    dcanvas.coords("itree1",dwidth/12,dheight/1.8)

                    dcanvas.coords("ibutton1",dwidth/3.09,dheight/2.4)
                    dcanvas.coords("ibutton2",dwidth/2.1,dheight/2.4)
                    dcanvas.coords("ibutton3",dwidth/1.59,dheight/2.4)
                    dcanvas.coords("ibutton4",dwidth/1.28,dheight/2.4)



                inv_canvas=Canvas(inv_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

                inv_frame.grid_rowconfigure(0,weight=1)
                inv_frame.grid_columnconfigure(0,weight=1)

                vertibar=Scrollbar(inv_frame, orient=VERTICAL)
                vertibar.grid(row=0,column=1,sticky='ns')
                vertibar.config(command=inv_canvas.yview)
                
                inv_canvas.bind("<Configure>", inv_responsive_widgets)
                inv_canvas.config(yscrollcommand=vertibar.set)
                inv_canvas.grid(row=0,column=0,sticky='nsew')

                
                inv_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ipoly1"))

                label_1 = Label(inv_canvas,width=10,height=1,text="INVOICES", font=('arial 25'),background="#1b3857",fg="white") 
                window_label_1 = inv_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("ilabel1"))

                inv_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("ihline"))

                inv_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ipoly2"))

                fgthdi = ttk.Style()
                fgthdi.configure('mystyle105.Treeview.Heading', background='#2f516f',State='DISABLE')

                inv_tree = ttk.Treeview(inv_canvas, columns = (1,2,3,4,5,6,7), height = 10, show = "headings",style='mystyle105.Treeview')
                inv_tree.pack(side = 'top')
                inv_tree.heading(1, text="INVOICE NO")
                inv_tree.heading(2, text="INVOICE DATE")
                inv_tree.heading(3, text="CUSTOMER")
                inv_tree.heading(4, text="EMAIL ID")
                inv_tree.heading(5, text="DUE DATE")
                inv_tree.heading(6, text="GRAND TOTAL")
                inv_tree.heading(7, text="BALANCE DUE")
                
                inv_tree.column(1, width = 130)
                inv_tree.column(2, width = 130)
                inv_tree.column(3, width = 220)
                inv_tree.column(4, width = 210)
                inv_tree.column(5, width = 150)
                inv_tree.column(6, width = 130)
                inv_tree.column(7, width = 150)

                window_label_4 = inv_canvas.create_window(0, 0, anchor="nw", window=inv_tree,tags=('itree1'))

                # inv_sql="select * from auth_user where username=%s"
                # inv_val=(nm_ent.get(),)
                # fbcursor.execute(inv_sql,inv_val,)
                # inv_dtl=fbcursor.fetchone()

                # sql = "select * from app1_company where id_id=%s"
                # val = (inv_dtl[0],)
                # fbcursor.execute(sql, val,)
                # inv_dtls=fbcursor.fetchone()

                # c_sql_i1 = "SELECT * FROM app1_customer where cid_id=%s"
                # c_val_i1 = (inv_dtls[0],)
                # fbcursor.execute(c_sql_i1,c_val_i1,)
                # c_data_i1 = fbcursor.fetchall()

                # count0 = 0
                # for i in c_data_i1:
                #     if True:
                #        inv_tree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[5],i[1],i[2],i[6],i[17],i[41])) 
                #     else:
                #         pass
                # count0 += 1


                def add_invoice():
                    inv_frame.grid_forget()
                    inv_frame_1 = Frame(tab3_2)
                    inv_frame_1.grid(row=0,column=0,sticky='nsew')

                    def inv_responsive_widgets2(event):
                        try:
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                            
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("aipoly1",x1 + r1,y1,
                            x1 + r1,y1,
                            x2 - r1,y1,
                            x2 - r1,y1,     
                            x2,y1,     
                            #--------------------
                            x2,y1 + r1,     
                            x2,y1 + r1,     
                            x2,y2 - r1,     
                            x2,y2 - r1,     
                            x2,y2,
                            #--------------------
                            x2 - r1,y2,     
                            x2 - r1,y2,     
                            x1 + r1,y2,
                            x1 + r1,y2,
                            x1,y2,
                            #--------------------
                            x1,y2 - r1,
                            x1,y2 - r1,
                            x1,y1 + r1,
                            x1,y1 + r1,
                            x1,y1,
                            )

                            dcanvas.coords("ailabel1",dwidth/2.45,dheight/8.24)
                            dcanvas.coords("aihline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/2.8
                            y21 = dheight/0.36


                            dcanvas.coords("aipoly2",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            dcanvas.coords("ailabel2",dwidth/2.45,dheight/2.34)
                            dcanvas.coords("ailabel3",dwidth/22.80,dheight/1.90)
                            dcanvas.coords("ailabel4",dwidth/20.00,dheight/1.65)
                            dcanvas.coords("ailabel5",dwidth/20.00,dheight/1.37)
                            dcanvas.coords("ailabel6",dwidth/3.34,dheight/1.37)
                            dcanvas.coords("ailabel7",dwidth/21.66 ,dheight/1.12)
                            dcanvas.coords("ailabel8",dwidth/3.34,dheight/1.12)
                            dcanvas.coords("ailabel9",dwidth/19.10,dheight/0.947)
                            dcanvas.coords("ailabel10",dwidth/19.40,dheight/0.717)
                            dcanvas.coords("ailabel11",dwidth/16.50,dheight/0.638)
                            dcanvas.coords("ailabel12",dwidth/8.40,dheight/0.638)
                            dcanvas.coords("ailabel13",dwidth/3.34,dheight/0.638)
                            dcanvas.coords("ailabel14",dwidth/2.28,dheight/0.638)
                            dcanvas.coords("ailabel15",dwidth/1.73,dheight/0.638)
                            dcanvas.coords("ailabel16",dwidth/1.52,dheight/0.638)
                            dcanvas.coords("ailabel17",dwidth/1.325,dheight/0.638)
                            dcanvas.coords("ailabel18",dwidth/1.165,dheight/0.638)
                            dcanvas.coords("ailabel19",dwidth/16.50,dheight/0.604)
                            dcanvas.coords("ailabel20",dwidth/16.50,dheight/0.562)
                            dcanvas.coords("ailabel21",dwidth/16.50,dheight/0.526)
                            dcanvas.coords("ailabel22",dwidth/16.50,dheight/0.496)
                            dcanvas.coords("ailabel23",dwidth/1.53,dheight/0.45)
                            dcanvas.coords("ailabel24",dwidth/1.54,dheight/0.435)
                            dcanvas.coords("ailabel25",dwidth/1.54,dheight/0.42)
                            dcanvas.coords("ailabel26",dwidth/1.54,dheight/0.406)
                            dcanvas.coords("ailabel27",dwidth/1.54,dheight/0.392)
                            dcanvas.coords("ailabel28",dwidth/1.72,dheight/1.12)

                            dcanvas.coords("aientry1",dwidth/3.0,dheight/1.295)
                            dcanvas.coords("aientry2",dwidth/18.00,dheight/0.91)
                            dcanvas.coords("aientry3",dwidth/4.00,dheight/0.604)
                            dcanvas.coords("aientry4",dwidth/2.51,dheight/0.604)
                            dcanvas.coords("aientry5",dwidth/1.8,dheight/0.604)
                            dcanvas.coords("aientry6",dwidth/1.565,dheight/0.604)
                            dcanvas.coords("aientry7",dwidth/1.357,dheight/0.604)
                            dcanvas.coords("aientry8",dwidth/4.00,dheight/0.562)
                            dcanvas.coords("aientry9",dwidth/4.00,dheight/0.526)
                            dcanvas.coords("aientry10",dwidth/4.00,dheight/0.496)
                            dcanvas.coords("aientry11",dwidth/2.51,dheight/0.562)
                            dcanvas.coords("aientry12",dwidth/2.51,dheight/0.526)
                            dcanvas.coords("aientry13",dwidth/2.51,dheight/0.496)
                            dcanvas.coords("aientry14",dwidth/1.8,dheight/0.562)
                            dcanvas.coords("aientry15",dwidth/1.8,dheight/0.526)
                            dcanvas.coords("aientry16",dwidth/1.8,dheight/0.496)
                            dcanvas.coords("aientry17",dwidth/1.565,dheight/0.562)
                            dcanvas.coords("aientry18",dwidth/1.565,dheight/0.526)
                            dcanvas.coords("aientry19",dwidth/1.565,dheight/0.496)
                            dcanvas.coords("aientry20",dwidth/1.357,dheight/0.562)
                            dcanvas.coords("aientry21",dwidth/1.357,dheight/0.526)
                            dcanvas.coords("aientry22",dwidth/1.357,dheight/0.496)
                            dcanvas.coords("aientry23",dwidth/1.33,dheight/0.452)
                            dcanvas.coords("aientry24",dwidth/1.33,dheight/0.4365)
                            dcanvas.coords("aientry25",dwidth/1.33,dheight/0.4215)
                            dcanvas.coords("aientry26",dwidth/1.33,dheight/0.407)
                            dcanvas.coords("aientry27",dwidth/1.33,dheight/0.393)

                            dcanvas.coords("aicombo1",dwidth/18.00,dheight/1.295)
                            dcanvas.coords("aicombo2",dwidth/3.00,dheight/1.074)
                            dcanvas.coords("aicombo3",dwidth/18.00,dheight/0.695)
                            dcanvas.coords("aicombo4",dwidth/10.10,dheight/0.604)
                            dcanvas.coords("aicombo5",dwidth/1.21,dheight/0.604)
                            dcanvas.coords("aicombo6",dwidth/10.10,dheight/0.562)
                            dcanvas.coords("aicombo7",dwidth/10.10,dheight/0.526)
                            dcanvas.coords("aicombo8",dwidth/10.10,dheight/0.496)
                            dcanvas.coords("aicombo9",dwidth/1.21,dheight/0.562)
                            dcanvas.coords("aicombo10",dwidth/1.21,dheight/0.526)
                            dcanvas.coords("aicombo11",dwidth/1.21,dheight/0.496)

                            dcanvas.coords("aibutton1",dwidth/4.74,dheight/1.295)
                            dcanvas.coords("aibutton2",dwidth/1.28,dheight/0.377)
                            dcanvas.coords("aibutton3",dwidth/23,dheight/3.415)

                            #-------------------------------H Lines-----------------------------------#
                            dcanvas.coords("ailine1",dwidth/21,dheight/0.645,dwidth/1.055,dheight/0.645)
                            dcanvas.coords("ailine2",dwidth/21,dheight/0.617,dwidth/1.055,dheight/0.617)
                            dcanvas.coords("ailine3",dwidth/21,dheight/0.576,dwidth/1.055,dheight/0.576)
                            dcanvas.coords("ailine4",dwidth/21,dheight/0.536,dwidth/1.055,dheight/0.536)
                            dcanvas.coords("ailine5",dwidth/21,dheight/0.506,dwidth/1.055,dheight/0.506)
                            dcanvas.coords("ailine6",dwidth/21,dheight/0.476,dwidth/1.055,dheight/0.476)
                            #-------------------------------V Lines-----------------------------------#
                            dcanvas.coords("ailine7",dwidth/21,dheight/0.645,dwidth/21,dheight/0.476)
                            dcanvas.coords("ailine8",dwidth/1.055,dheight/0.645,dwidth/1.055,dheight/0.476)
                            dcanvas.coords("ailine9",dwidth/11,dheight/0.645,dwidth/11,dheight/0.476)
                            dcanvas.coords("ailine10",dwidth/4.15,dheight/0.645,dwidth/4.15,dheight/0.476)
                            dcanvas.coords("ailine11",dwidth/2.55,dheight/0.645,dwidth/2.55,dheight/0.476)
                            dcanvas.coords("ailine12",dwidth/1.83,dheight/0.645,dwidth/1.83,dheight/0.476)
                            dcanvas.coords("ailine13",dwidth/1.58,dheight/0.645,dwidth/1.58,dheight/0.476)
                            dcanvas.coords("ailine14",dwidth/1.37,dheight/0.645,dwidth/1.37,dheight/0.476)
                            dcanvas.coords("ailine15",dwidth/1.22,dheight/0.645,dwidth/1.22,dheight/0.476)

                            #-------------------------------V Lines-----------------------------------#
                            dcanvas.coords("ailine16",dwidth/1.58,dheight/0.455,dwidth/1.58,dheight/0.383)
                            dcanvas.coords("ailine17",dwidth/1.348,dheight/0.455,dwidth/1.348,dheight/0.383)
                            dcanvas.coords("ailine18",dwidth/1.084,dheight/0.455,dwidth/1.084,dheight/0.383)
                            #-------------------------------H Lines-----------------------------------#
                            dcanvas.coords("ailine19",dwidth/1.58,dheight/0.455,dwidth/1.084,dheight/0.455)
                            dcanvas.coords("ailine20",dwidth/1.58,dheight/0.383,dwidth/1.084,dheight/0.383)
                            dcanvas.coords("ailine21",dwidth/1.58,dheight/0.439,dwidth/1.084,dheight/0.439)
                            dcanvas.coords("ailine22",dwidth/1.58,dheight/0.424,dwidth/1.084,dheight/0.424)
                            dcanvas.coords("ailine23",dwidth/1.58,dheight/0.41,dwidth/1.084,dheight/0.41)
                            dcanvas.coords("ailine24",dwidth/1.58,dheight/0.396,dwidth/1.084,dheight/0.396)
                        except:
                            pass

                        try:
                            dcanvas.coords("aidate1",dwidth/17.8,dheight/1.074)
                            dcanvas.coords("aidate2",dwidth/1.65,dheight/1.074)
                        except:
                            pass



                    inv_canvas_1=Canvas(inv_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1800))

                    inv_frame_1.grid_columnconfigure(0,weight=1)
                    inv_frame_1.grid_rowconfigure(0,weight=1)
                    
                    vertibar=Scrollbar(inv_frame_1, orient=VERTICAL)
                    vertibar.grid(row=0,column=1,sticky='ns')
                    vertibar.config(command=inv_canvas_1.yview)

                    inv_canvas_1.bind("<Configure>", inv_responsive_widgets2)
                    inv_canvas_1.config(yscrollcommand=vertibar.set)
                    inv_canvas_1.grid(row=0,column=0,sticky='nsew')

                    def sales_add_new_inv():

                        customername = aicomb_1.get()
                        email = aientry_1.get()
                        terms = comb_t_2.get()
                        # invoicedate = 
                        # duedate
                        bname = ai_b_entry_1.get('1.0', 'end-1c')
                        placosupply = ai_p_comb_2.get()
                        product = ai_comb_p_1.get()
                        hsn = ai_entry_p_1.get()
                        description = ai_entry_p_1_2.get('1.0', 'end-1c')
                        qty = ai_entry_p_1_3.get()
                        price = ai_entry_p_1_4.get()
                        total = ai_entry_p_1_5.get()
                        tax = ai_comb_p_1_2.get()
                        # subtotal
                        # grandtotal
                        # product2 = 
                        # hsn2 = 
                        # description2 = 
                        # qty2 = 
                        # price2 = 
                        # total2 = 
                        # tax2 = 
                        # product3
                        # hsn3
                        # description3
                        # qty3
                        # price3
                        # total3
                        # tax3
                        # product4
                        # hsn4
                        # description4
                        # qty4
                        # price4
                        # total4
                        # tax4
                        # amtrecvd
                        # taxamount
                        # baldue


                        usr_sql = "SELECT id FROM auth_user WHERE username=%s"
                        usr_val = (nm_ent.get(),)
                        fbcursor.execute(usr_sql,usr_val)
                        usr_data = fbcursor.fetchone()

                        cmp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                        cmp_val = (usr_data[0],)
                        fbcursor.execute(cmp_sql,cmp_val)
                        cmp_data = fbcursor.fetchone()
                        cid = cmp_data[0]

                        inv_sql_1 = "INSERT INTO app1_invoice (cid_id) VALUES(%s)"
                        inv_val_1=(cid)
                        fbcursor.execute(inv_sql_1,inv_val_1)
                        finsysdb.commit()

                        #----------Refresh Insert Tree--------#

                        for record in cus_tree.get_children():
                                cus_tree.delete(record)

                        sql_pr="select * from auth_user where username=%s"
                        sql_pr_val=(nm_ent.get(),)
                        fbcursor.execute(sql_pr,sql_pr_val,)
                        pr_dtl=fbcursor.fetchone()

                        sql = "select * from app1_company where id_id=%s"
                        val = (pr_dtl[0],)
                        fbcursor.execute(sql, val,)
                        cmp_dtl=fbcursor.fetchone()

                        c_sql_1 = "SELECT * FROM app1_customer where cid_id=%s"
                        c_val_1 = (cmp_dtl[0],)
                        fbcursor.execute(c_sql_1,c_val_1,)
                        i_data_1 = fbcursor.fetchall()

                        count0 = 0
                        for i in i_data_1:
                            if True:
                                inv_tree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[5],i[1],i[2],i[6],i[17],i[41]))
                            else:
                                pass
                        count0 += 1

                            
                        inv_frame_1.destroy()
                        inv_frame.grid(row=0,column=0,sticky='nsew')


                    inv_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly1"))

                    
                    label_1 = Label(inv_canvas_1,width=10,height=1,text="INVOICE", font=('arial 20'),background="#1b3857",fg="white") 
                    window_label_1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ailabel1"))

                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("aihline"))

                    inv_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly2"))

                    label_1 = Label(inv_canvas_1,width=10,height=1,text="Fin sYs", font=('arial 20'),background="#1b3857",fg="white") 
                    window_label_1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ailabel2"))

                    usr_sql = "SELECT * FROM auth_user WHERE username=%s"
                    usr_val = (nm_ent.get(),)
                    fbcursor.execute(usr_sql,usr_val)
                    usr_data = fbcursor.fetchone()

                    cmp_sql = "SELECT * FROM app1_company WHERE id_id=%s"
                    cmp_val = (usr_data[0],)
                    fbcursor.execute(cmp_sql,cmp_val)
                    cmp_data = fbcursor.fetchone()

                    label_2 = Label(inv_canvas_1,width=15,height=1,text=cmp_data[1], font=('arial 16'),background="#1b3857",fg="skyblue") 
                    window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel3"))

                    label_2 = Label(inv_canvas_1,width=15,height=1,text=cmp_data[6], font=('arial 16'),background="#1b3857",fg="skyblue") 
                    window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel4"))

                    label_2 = Label(inv_canvas_1,width=15,height=1,text="Select Customer", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel5"))

                    def inv_c_details(event):
                        inv_to_str = aicomb_1.get()
                        sql = "select * from app1_customer where firstname=%s  and cid_id=%s"
                        val = (inv_to_str,cmp_dtl[0],)
                        fbcursor.execute(sql,val)
                        inv_c_sel = fbcursor.fetchone()
                        aientry_1.delete(0,END)
                        aientry_1.insert(0,inv_c_sel[9])
                        ai_b_entry_1.delete('1.0',END)
                        ai_b_entry_1.insert('1.0',inv_c_sel[2]+" "+inv_c_sel[3]+ '\n' +inv_c_sel[4]+ '\n' +inv_c_sel[12]+ '\n' +inv_c_sel[13]+ '\n' +inv_c_sel[14]+ '\n' +inv_c_sel[15]+ '\n' +inv_c_sel[16])
                        

                    sql_pr="select * from auth_user where username=%s"
                    sql_pr_val=(nm_ent.get(),)
                    fbcursor.execute(sql_pr,sql_pr_val,)
                    pr_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (pr_dtl[0],)
                    fbcursor.execute(sql, val,)
                    cmp_dtl=fbcursor.fetchone()
                    

                    sql_pr_cmp="select firstname from app1_customer where cid_id=%s"
                    sql_pr_cmp_val=(cmp_dtl[0],)
                    fbcursor.execute(sql_pr_cmp,sql_pr_cmp_val,)
                    pr_cmp_dtl=fbcursor.fetchall()
                    p_i1 = []

                    for i in pr_cmp_dtl:
                        # p_i1.append(str(i[0])+" "+str(i[1]))
                        # print(p_i1)
                        p_i1.append(i[0])

                    
                    
                    aicomb_1 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                    aicomb_1["values"] = p_i1
                    aicomb_1.bind("<<ComboboxSelected>>",inv_c_details)
                    window_aicomb_1 = inv_canvas_1.create_window(0, 0, anchor="nw", width=200, height=30,window=aicomb_1, tags=("aicombo1"))
                    

                    

                    def add_inv_customer():
                        #inv_frame.grid_forget()
                        inv_frame_1.grid_forget()
                        inv_frame_2 = Frame(tab3_2)
                        inv_frame_2.grid(row=0,column=0,sticky='nsew')

                        def inc_responsive_widgets2(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                        
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("acpoly1",x1 + r1,y1,
                            x1 + r1,y1,
                            x2 - r1,y1,
                            x2 - r1,y1,     
                            x2,y1,     
                            #--------------------
                            x2,y1 + r1,     
                            x2,y1 + r1,     
                            x2,y2 - r1,     
                            x2,y2 - r1,     
                            x2,y2,
                            #--------------------
                            x2 - r1,y2,     
                            x2 - r1,y2,     
                            x1 + r1,y2,
                            x1 + r1,y2,
                            x1,y2,
                            #--------------------
                            x1,y2 - r1,
                            x1,y2 - r1,
                            x1,y1 + r1,
                            x1,y1 + r1,
                            x1,y1,
                            )

                            dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
                            dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/2.8
                            y21 = dheight/0.45


                            dcanvas.coords("acpoly2",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
                            dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
                            dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
                            dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
                            dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
                            dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
                            dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
                            dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
                            dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
                            dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
                            dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
                            dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
                            dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
                            dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
                            dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
                            dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
                            dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
                            dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
                            dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
                            dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
                            dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
                            dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
                            dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
                            dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
                            dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

                            dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
                            dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

                            dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
                            dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
                            dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
                            dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
                            dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
                            dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
                            dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
                            dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
                            dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
                            dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
                            dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
                            dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
                            dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
                            dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
                            dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
                            dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
                            dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
                            dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
                            dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

                            dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
                            dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

                            dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
                            dcanvas.coords("acbutton2",dwidth/23,dheight/3.415)


                        inv_canvas_2=Canvas(inv_frame_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

                        inv_frame_2.grid_columnconfigure(0,weight=1)
                        inv_frame_2.grid_rowconfigure(0,weight=1)

                        
                        vertibar=Scrollbar(inv_frame_2, orient=VERTICAL)
                        vertibar.grid(row=0,column=1,sticky='ns')
                        vertibar.config(command=inv_canvas_2.yview)

                        inv_canvas_2.bind("<Configure>", inc_responsive_widgets2)
                        inv_canvas_2.config(yscrollcommand=vertibar.set)
                        inv_canvas_2.grid(row=0,column=0,sticky='nsew')

                        def sales_add_inv_cus():
                            title = ic_comb_cus_1.get()
                            firstname = ic_entry_cus_1.get()
                            lastname = ic_entry_cus_2.get()
                            company = ic_entry_cus_3.get()
                            location = ic_cus_4.get()
                            gsttype = ic_comb_cus_2.get()
                            gstin = ic_entry_cus_5.get()
                            panno = ic_entry_cus_6.get()
                            email = ic_entry_cus_7.get()
                            website = ic_entry_cus_8.get()
                            mobile = ic_entry_cus_9.get()
                            street = ic_entry_cus_10.get()
                            city = ic_entry_cus_12.get()
                            state = ic_entry_cus_13.get()
                            pincode = ic_entry_cus_p12.get()
                            country = ic_entry_cus_c13.get()
                            shipstreet = ic_entry_cus_11.get()
                            shipcity = ic_entry_cus_14.get()
                            shipstate = ic_entry_cus_15.get()
                            shippincode = ic_entry_cus_p14.get()
                            shipcountry = ic_entry_cus_c15.get()

                            usri_sql = "SELECT id FROM auth_user WHERE username=%s"
                            usri_val = (nm_ent.get(),)
                            fbcursor.execute(usri_sql,usri_val)
                            usri_data = fbcursor.fetchone()

                            cmpi_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                            cmpi_val = (usri_data[0],)
                            fbcursor.execute(cmpi_sql,cmpi_val)
                            cmpi_data = fbcursor.fetchone()
                            cid = cmpi_data[0]

                            if ic_chk_str_1.get() == True:

                                cus_sql = "INSERT INTO app1_customer (title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                cus_val=(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid)
                                fbcursor.execute(cus_sql,cus_val)
                                finsysdb.commit()

                                #----------Refresh Insert Tree--------#

                                for record in cus_tree.get_children():
                                        cus_tree.delete(record)

                                sql_pr="select * from auth_user where username=%s"
                                sql_pr_val=(nm_ent.get(),)
                                fbcursor.execute(sql_pr,sql_pr_val,)
                                pr_dtl=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dtl[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dtl=fbcursor.fetchone()

                                c_sql_1 = "SELECT * FROM app1_customer where cid_id=%s"
                                c_val_1 = (cmp_dtl[0],)
                                fbcursor.execute(c_sql_1,c_val_1,)
                                c_data_1 = fbcursor.fetchall()

                                count0 = 0
                                for i in c_data_1:
                                    if True:
                                        cus_tree.insert(parent='',index='end',iid=i,text='',values=('',i[2]+" "+i[3],i[6],i[7],i[8],i[9],i[11])) 
                                    else:
                                        pass
                                count0 += 1

                                inv_frame_2.destroy()
                                inv_frame_1.grid(row=0,column=0,sticky='nsew')
                            
                            else:
                                pass
                        

                        inv_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

                        label_1 = Label(inv_canvas_2,width=15,height=1,text="ADD CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
                        window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

                        inv_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

                        inv_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))

                        label_1 = Label(inv_canvas_2,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
                        window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))

                        inv_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))

                        label_2 = Label(inv_canvas_2,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel3"))

                        ic_comb_cus_1 = ttk.Combobox(inv_canvas_2, font=('arial 10'),foreground="white")
                        ic_comb_cus_1['values'] = ("Mr","Mrs","Miss","Ms",)
                        ic_comb_cus_1.current(0)
                        window_ic_comb_cus_1 = inv_canvas_2.create_window(0, 0, anchor="nw", width=245, height=30,window=ic_comb_cus_1, tags=("accombo1"))

                        label_2 = Label(inv_canvas_2,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel4"))

                        ic_entry_cus_1=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_1 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_1, tags=("acentry1"))

                        label_2 = Label(inv_canvas_2,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel5"))

                        ic_entry_cus_2=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_2 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_2, tags=("acentry2"))

                        label_2 = Label(inv_canvas_2,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel6"))

                        ic_entry_cus_3=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_3 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_3, tags=("acentry3"))

                        label_2 = Label(inv_canvas_2,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel7"))

                        ic_cus_4=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_cus_4 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_cus_4, tags=("acentry4"))

                        label_2 = Label(inv_canvas_2,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel8"))

                        ic_comb_cus_2 = ttk.Combobox(inv_canvas_2, font=('arial 10'),foreground="white")
                        ic_comb_cus_2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
                        ic_comb_cus_2.current(0)
                        window_ic_comb_cus_2 = inv_canvas_2.create_window(0, 0, anchor="nw", width=245, height=30,window=ic_comb_cus_2, tags=("accombo2"))

                        label_2 = Label(inv_canvas_2,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel9"))


                        def ic_gst_in(event):
                            if ic_entry_cus_5.get()=="29APPCK7465F1Z1":
                                ic_entry_cus_5.delete(0,END)
                            else:
                                pass
                        
                        ic_entry_cus_5=Entry(inv_canvas_2,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'))
                        window_ic_entry_cus_5 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_5, tags=("acentry5"))
                        ic_entry_cus_5.insert(0,"29APPCK7465F1Z1")
                        ic_entry_cus_5.bind("<Button-1>",ic_gst_in)

                        label_2 = Label(inv_canvas_2,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel10"))

                        def ic_pan_no(event):
                            if ic_entry_cus_6.get()=="APPCK7465F":
                                ic_entry_cus_6.delete(0,END)
                            else:
                                pass

                        ic_entry_cus_6=Entry(inv_canvas_2,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'))
                        window_ic_entry_cus_6 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_6, tags=("acentry6"))
                        ic_entry_cus_6.insert(0,"APPCK7465F")
                        ic_entry_cus_6.bind("<Button-1>",ic_pan_no)

                        label_2 = Label(inv_canvas_2,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel11"))

                        ic_entry_cus_7=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_7 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_7, tags=("acentry7"))

                        label_2 = Label(inv_canvas_2,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel12"))

                        ic_entry_cus_8=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_8 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_8, tags=("acentry8"))

                        label_2 = Label(inv_canvas_2,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel13"))

                        ic_entry_cus_9=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_9 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_9, tags=("acentry9"))

                        def copy_icus_details():
                            ic_entry_cus_11.delete(0, END)
                            ic_entry_cus_11.insert(0,ic_entry_cus_10.get())
                            ic_entry_cus_14.delete(0, END)
                            ic_entry_cus_14.insert(0,ic_entry_cus_12.get())
                            ic_entry_cus_15.delete(0, END)
                            ic_entry_cus_15.insert(0,ic_entry_cus_13.get())
                            ic_entry_cus_p14.delete(0, END)
                            ic_entry_cus_p14.insert(0,ic_entry_cus_p12.get())
                            ic_entry_cus_c15.delete(0, END)
                            ic_entry_cus_c15.insert(0,ic_entry_cus_c13.get())

                        label_1 = Label(inv_canvas_2,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
                        window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel14"))

                        label_2 = Label(inv_canvas_2,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel16"))

                        ic_entry_cus_10=Entry(inv_canvas_2,width=95,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_10 = inv_canvas_2.create_window(0, 0, anchor="nw", height=60,window=ic_entry_cus_10, tags=("acentry10"))

                        label_1 = Label(inv_canvas_2,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
                        window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel15"))

                        ic_chk_str = StringVar()
                        ic_chkbtn1 = Checkbutton(inv_canvas_2, text = "Same As Billing Address", variable = ic_chk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f",command=copy_icus_details)
                        ic_chkbtn1.select()
                        window_ic_chkbtn_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=ic_chkbtn1, tags=("accheck1"))

                        label_2 = Label(inv_canvas_2,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel17"))

                        ic_entry_cus_11=Entry(inv_canvas_2,width=95,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_11 = inv_canvas_2.create_window(0, 0, anchor="nw", height=60,window=ic_entry_cus_11, tags=("acentry11"))

                        label_2 = Label(inv_canvas_2,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel18"))

                        ic_entry_cus_12=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_12 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_12, tags=("acentry12"))
                        
                        label_2 = Label(inv_canvas_2,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel19"))

                        ic_entry_cus_13=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_13 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_13, tags=("acentry13"))

                        label_2 = Label(inv_canvas_2,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel20"))

                        ic_entry_cus_14=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_14 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_14, tags=("acentry14"))

                        label_2 = Label(inv_canvas_2,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel21"))

                        ic_entry_cus_15=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_15 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_15, tags=("acentry15"))

                        label_2 = Label(inv_canvas_2,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel22"))

                        ic_entry_cus_p12=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_p12 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_p12, tags=("acentry16"))
                        
                        label_2 = Label(inv_canvas_2,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel23"))

                        ic_entry_cus_c13=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_c13 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_c13, tags=("acentry17"))

                        label_2 = Label(inv_canvas_2,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel24"))

                        ic_entry_cus_p14=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_p14 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_p14, tags=("acentry18"))

                        label_2 = Label(inv_canvas_2,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel25"))

                        ic_entry_cus_c15=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ic_entry_cus_c15 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_c15, tags=("acentry19"))

                        ic_chk_str_1 = BooleanVar()
                        ic_chkbtn2 = Checkbutton(inv_canvas_2, text = "Agree to terms and conditions", variable = ic_chk_str_1, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
                        ic_chkbtn2.select()
                        window_ic_chkbtn_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=ic_chkbtn2,tags=("accheck2"))

                        ic_cus_btn2=Button(inv_canvas_2,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12',command=sales_add_inv_cus)
                        window_ic_cus_btn2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=ic_cus_btn2,tags=("acbutton1"))

                        def inv_back_1_():
                            inv_frame_2.grid_forget()
                            inv_frame_1.grid(row=0,column=0,sticky='nsew')

                        bck_btn1=Button(inv_canvas_2,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=inv_back_1_)
                        window_bck_btn1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('acbutton2'))
                        


                    aibtn2=Button(inv_canvas_1,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=add_inv_customer)
                    window_aibtn2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=aibtn2, tags=('aibutton1'))

                    label_2 = Label(inv_canvas_1,width=15,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel6'))

                    aientry_1=Entry(inv_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_aientry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30,window=aientry_1,tags=('aientry1'))


                    label_2 = Label(inv_canvas_1,width=15,height=1,text="Terms", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel8'))


                    label_2 = Label(inv_canvas_1,width=6,height=1,text="Bill To:", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel9'))


                    ai_b_entry_1=scrolledtext.ScrolledText(inv_canvas_1,width=30,background='#2f516f',foreground="white")
                    window_ai_b_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=150, window=ai_b_entry_1,tags=('aientry2'))

                    label_2 = Label(inv_canvas_1,width=12,height=1,text="Place of supply", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel10'))

                    ai_p_comb_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
                    ai_p_comb_2['values'] = ("Kerala","Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Other Territory",)
                    ai_p_comb_2.current(0)
                    window_ai_p_comb_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=251, height=30,window=ai_p_comb_2,tags=('aicombo3'))


                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine1'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine2'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine3'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine4'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine5'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine6'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine7'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine8'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine9'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine10'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine11'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine12'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine13'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine14'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine15'))


                    label_2 = Label(inv_canvas_1,width=2,height=1,text="#", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel11'))

                    label_3 = Label(inv_canvas_1,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_3 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_3,tags=('ailabel12'))

                    label_4 = Label(inv_canvas_1,width=4,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel13'))

                    label_4 = Label(inv_canvas_1,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel14'))

                    label_4 = Label(inv_canvas_1,width=4,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel15'))

                    label_4 = Label(inv_canvas_1,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel16'))

                    label_4 = Label(inv_canvas_1,width=6,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel17'))

                    label_4 = Label(inv_canvas_1,width=7,height=1,text="TAX (%)", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel18'))

                    def i_details_1(event):
                        inv_to_str_1 = ai_comb_p_1.get()

                        sql = "select * from app1_inventory where name=%s and cid_id=%s"
                        val = (inv_to_str_1,cmp_dtl_i[0],)
                        fbcursor.execute(sql,val)
                        inv_sel_1 = fbcursor.fetchone()

                        sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                        val = (inv_to_str_1,cmp_dtl_i[0],)
                        fbcursor.execute(sql,val)
                        inv_sel_2 = fbcursor.fetchone()

                        sql = "select * from app1_bundle where name=%s and cid_id=%s"
                        val = (inv_to_str_1,cmp_dtl_i[0],)
                        fbcursor.execute(sql,val)
                        inv_sel_3 = fbcursor.fetchone() 

                        if inv_sel_1 is not None:
                            
                            ai_entry_p_1.delete(0,END)
                            ai_entry_p_1.insert(0,inv_sel_1[4])
                            ai_entry_p_1_2.delete('1.0',END)
                            ai_entry_p_1_2.insert('1.0',inv_sel_1[11])
                            ai_entry_p_1_4.delete(0,END)
                            ai_entry_p_1_4.insert(0,inv_sel_1[12])
                            ai_comb_p_1_2.delete(0,'end')
                            ai_comb_p_1_2.insert(0, inv_sel_1[14])
                            inv_canvas_1.itemconfig('aientry6',state='normal')
                            inv_canvas_1.itemconfig('aientry7',state='normal')
                            inv_canvas_1.itemconfig('aicombo5',state='normal')

                        elif inv_sel_2 is not None:
                            
                            ai_entry_p_1.delete(0,END)
                            ai_entry_p_1.insert(0,inv_sel_2[4])
                            ai_entry_p_1_2.delete('1.0',END)
                            ai_entry_p_1_2.insert('1.0',inv_sel_2[7])
                            ai_entry_p_1_4.delete(0,END)
                            ai_entry_p_1_4.insert(0,inv_sel_2[8])
                            ai_comb_p_1_2.delete(0,'end')
                            ai_comb_p_1_2.insert(0, inv_sel_2[10])
                            inv_canvas_1.itemconfig('aientry6',state='normal')
                            inv_canvas_1.itemconfig('aientry7',state='normal')
                            inv_canvas_1.itemconfig('aicombo5',state='normal')

                        elif inv_sel_3 is not None:
                            
                            ai_entry_p_1.delete(0,END)
                            ai_entry_p_1.insert(0,inv_sel_3[3])
                            ai_entry_p_1_2.delete('1.0',END)
                            ai_entry_p_1_2.insert('1.0',inv_sel_3[4])
                            inv_canvas_1.itemconfig('aientry6',state='hidden')
                            inv_canvas_1.itemconfig('aientry7',state='hidden')
                            inv_canvas_1.itemconfig('aicombo5',state='hidden')
                            
                        else:
                            pass

                    def i_details_2(event):
                        inv_to_str_2 = ai_comb_p_2.get()

                        sql = "select * from app1_inventory where name=%s and cid_id=%s"
                        val = (inv_to_str_2,cmp_dtl_i[0],)
                        fbcursor.execute(sql,val)
                        inv_se_1 = fbcursor.fetchone()

                        sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                        val = (inv_to_str_2,cmp_dtl_i[0],)
                        fbcursor.execute(sql,val)
                        inv_se_2 = fbcursor.fetchone()

                        sql = "select * from app1_bundle where name=%s and cid_id=%s"
                        val = (inv_to_str_2,cmp_dtl_i[0],)
                        fbcursor.execute(sql,val)
                        inv_se_3 = fbcursor.fetchone() 

                        if inv_se_1 is not None:
                            
                            ai_entry_p_2.delete(0,END)
                            ai_entry_p_2.insert(0,inv_se_1[4])
                            ai_entry_p_2_1.delete('1.0',END)
                            ai_entry_p_2_1.insert('1.0',inv_se_1[11])
                            ai_entry_2_3.delete(0,END)
                            ai_entry_2_3.insert(0,inv_se_1[12])
                            ai_comb_P_2_2.delete(0,'end')
                            ai_comb_P_2_2.insert(0, inv_se_1[14])
                            inv_canvas_1.itemconfig('aientry17',state='normal')
                            inv_canvas_1.itemconfig('aientry20',state='normal')
                            inv_canvas_1.itemconfig('aicombo9',state='normal')

                        elif inv_se_2 is not None:
                            
                            ai_entry_p_2.delete(0,END)
                            ai_entry_p_2.insert(0,inv_se_2[4])
                            ai_entry_p_2_1.delete('1.0',END)
                            ai_entry_p_2_1.insert('1.0',inv_se_2[7])
                            ai_entry_2_3.delete(0,END)
                            ai_entry_2_3.insert(0,inv_se_2[8])
                            ai_comb_P_2_2.delete(0,'end')
                            ai_comb_P_2_2.insert(0, inv_se_2[10])
                            inv_canvas_1.itemconfig('aientry17',state='normal')
                            inv_canvas_1.itemconfig('aientry20',state='normal')
                            inv_canvas_1.itemconfig('aicombo9',state='normal')

                        elif inv_se_3 is not None:
                            
                            ai_entry_p_2.delete(0,END)
                            ai_entry_p_2.insert(0,inv_se_3[3])
                            ai_entry_p_2_1.delete('1.0',END)
                            ai_entry_p_2_1.insert('1.0',inv_se_3[4])
                            inv_canvas_1.itemconfig('aientry17',state='hidden')
                            inv_canvas_1.itemconfig('aientry20',state='hidden')
                            inv_canvas_1.itemconfig('aicombo9',state='hidden')
                            
                        else:
                            pass

                    def i_details_3(event):
                        inv_to_str_3 = ai_comb_p_3.get()

                        sql = "select * from app1_inventory where name=%s and cid_id=%s"
                        val = (inv_to_str_3,cmp_dtl_i[0],)
                        fbcursor.execute(sql,val)
                        inv_s_1 = fbcursor.fetchone()

                        sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                        val = (inv_to_str_3,cmp_dtl_i[0],)
                        fbcursor.execute(sql,val)
                        inv_s_2 = fbcursor.fetchone()

                        sql = "select * from app1_bundle where name=%s and cid_id=%s"
                        val = (inv_to_str_3,cmp_dtl_i[0],)
                        fbcursor.execute(sql,val)
                        inv_s_3 = fbcursor.fetchone() 

                        if inv_s_1 is not None:
                            
                            ai_entry_3.delete(0,END)
                            ai_entry_3.insert(0,inv_s_1[4])
                            ai_entry_3_1.delete('1.0',END)
                            ai_entry_3_1.insert('1.0',inv_s_1[11])
                            ai_entry_3_3.delete(0,END)
                            ai_entry_3_3.insert(0,inv_s_1[12])
                            ai_comb_P_3_2.delete(0,'end')
                            ai_comb_P_3_2.insert(0, inv_s_1[14])
                            inv_canvas_1.itemconfig('aientry18',state='normal')
                            inv_canvas_1.itemconfig('aientry21',state='normal')
                            inv_canvas_1.itemconfig('aicombo10',state='normal')

                        elif inv_s_2 is not None:
                            
                            ai_entry_3.delete(0,END)
                            ai_entry_3.insert(0,inv_s_2[4])
                            ai_entry_3_1.delete('1.0',END)
                            ai_entry_3_1.insert('1.0',inv_s_2[7])
                            ai_entry_3_3.delete(0,END)
                            ai_entry_3_3.insert(0,inv_s_2[8])
                            ai_comb_P_3_2.delete(0,'end')
                            ai_comb_P_3_2.insert(0, inv_s_2[10])
                            inv_canvas_1.itemconfig('aientry18',state='normal')
                            inv_canvas_1.itemconfig('aientry21',state='normal')
                            inv_canvas_1.itemconfig('aicombo10',state='normal')

                        elif inv_s_3 is not None:
                            
                            ai_entry_3.delete(0,END)
                            ai_entry_3.insert(0,inv_s_3[3])
                            ai_entry_3_1.delete('1.0',END)
                            ai_entry_3_1.insert('1.0',inv_s_3[4])
                            inv_canvas_1.itemconfig('aientry18',state='hidden')
                            inv_canvas_1.itemconfig('aientry21',state='hidden')
                            inv_canvas_1.itemconfig('aicombo10',state='hidden')
                            
                        else:
                            pass

                    def i_details_4(event):
                        inv_to_str_4 = ai_comb_p_4.get()

                        sql = "select * from app1_inventory where name=%s and cid_id=%s"
                        val = (inv_to_str_4,cmp_dtl_i[0],)
                        fbcursor.execute(sql,val)
                        inv_ss_1 = fbcursor.fetchone()

                        sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                        val = (inv_to_str_4,cmp_dtl_i[0],)
                        fbcursor.execute(sql,val)
                        inv_ss_2 = fbcursor.fetchone()

                        sql = "select * from app1_bundle where name=%s and cid_id=%s"
                        val = (inv_to_str_4,cmp_dtl_i[0],)
                        fbcursor.execute(sql,val)
                        inv_ss_3 = fbcursor.fetchone() 

                        if inv_ss_1 is not None:
                            
                            ai_entry_4.delete(0,END)
                            ai_entry_4.insert(0,inv_ss_1[4])
                            ai_entry_4_1.delete('1.0',END)
                            ai_entry_4_1.insert('1.0',inv_ss_1[11])
                            ai_entry_4_3.delete(0,END)
                            ai_entry_4_3.insert(0,inv_ss_1[12])
                            ai_comb_P_4_2.delete(0,'end')
                            ai_comb_P_4_2.insert(0, inv_ss_1[14])
                            inv_canvas_1.itemconfig('aientry19',state='normal')
                            inv_canvas_1.itemconfig('aientry22',state='normal')
                            inv_canvas_1.itemconfig('aicombo11',state='normal')

                        elif inv_ss_2 is not None:
                            
                            ai_entry_4.delete(0,END)
                            ai_entry_4.insert(0,inv_ss_2[4])
                            ai_entry_4_1.delete('1.0',END)
                            ai_entry_4_1.insert('1.0',inv_ss_2[7])
                            ai_entry_4_3.delete(0,END)
                            ai_entry_4_3.insert(0,inv_ss_2[8])
                            ai_comb_P_4_2.delete(0,'end')
                            ai_comb_P_4_2.insert(0, inv_ss_2[10])
                            inv_canvas_1.itemconfig('aientry19',state='normal')
                            inv_canvas_1.itemconfig('aientry22',state='normal')
                            inv_canvas_1.itemconfig('aicombo11',state='normal')

                        elif inv_ss_3 is not None:
                            
                            ai_entry_4.delete(0,END)
                            ai_entry_4.insert(0,inv_ss_3[3])
                            ai_entry_4_1.delete('1.0',END)
                            ai_entry_4_1.insert('1.0',inv_ss_3[4])
                            inv_canvas_1.itemconfig('aientry19',state='hidden')
                            inv_canvas_1.itemconfig('aientry22',state='hidden')
                            inv_canvas_1.itemconfig('aicombo11',state='hidden')
                            
                        else:
                            pass
                        
                        

                    sql_i="select * from auth_user where username=%s"
                    val_i=(nm_ent.get(),)
                    fbcursor.execute(sql_i,val_i,)
                    p_dtl=fbcursor.fetchone()

                    sql = "select * from app1_company where id_id=%s"
                    val = (p_dtl[0],)
                    fbcursor.execute(sql, val,)
                    cmp_dtl_i=fbcursor.fetchone()
                    

                    i_sql = "SELECT name FROM app1_inventory where cid_id=%s"
                    i_val = (cmp_dtl_i[0],)
                    fbcursor.execute(i_sql,i_val)
                    i_data = fbcursor.fetchall()
                    
                    ii_sql = "SELECT name FROM app1_noninventory where cid_id=%s"
                    ii_val = (cmp_dtl_i[0],)
                    fbcursor.execute(ii_sql,ii_val)
                    ii_data = fbcursor.fetchall()

                    iii_sql = "SELECT name FROM app1_bundle where cid_id=%s"
                    iii_val = (cmp_dtl_i[0],)
                    fbcursor.execute(iii_sql,iii_val)
                    iii_data = fbcursor.fetchall()

                    inv_data = []   
                    
                    for i in i_data:
                        inv_data.append(i[0])
                    for i in ii_data:
                        inv_data.append(i[0])
                    for i in iii_data:
                        inv_data.append(i[0])

                    label_2 = Label(inv_canvas_1,width=2,height=1,text="1", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_1.create_window(90, 1020, anchor="nw", window=label_2,tags=('ailabel19'))

                    ai_comb_p_1 = ttk.Combobox(inv_canvas_1, font=('arial 10'),values=inv_data)
                    window_ai_comb_p_1 = inv_canvas_1.create_window(0, 0, anchor="nw", width=180, height=30,window=ai_comb_p_1,tags=('aicombo4'))
                    ai_comb_p_1.bind("<<ComboboxSelected>>",i_details_1)

                    ai_entry_p_1=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                    window_ai_entry_p_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1,tags=('aientry3'))

                    ai_entry_p_1_2=scrolledtext.ScrolledText(inv_canvas_1,width=21,background='#2f516f',foreground="white")
                    window_ai_entry_p_1_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_2,tags=('aientry4'))

                    ai_entry_p_1_3=Spinbox(inv_canvas_1,width=13,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                    window_ai_entry_p_1_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_3,tags=('aientry5'))

                    ai_entry_p_1_4=Spinbox(inv_canvas_1,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                    window_ai_entry_p_1_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_4,tags=('aientry6'))

                    def multiply_num_i1(event):
                        num1= float(ai_entry_p_1_3.get())
                        num2= float(ai_entry_p_1_4.get())
                        mul_i= round(num1 * num2)
                        ai_entry_p_1_5.delete(0, END)
                        ai_entry_p_1_5.insert(0,mul_i)

                        

                    ai_entry_p_1_5=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
                    window_ai_entry_p_1_5 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_5,tags=('aientry7'))
                    ai_entry_p_1_5.bind("<Button-1>",multiply_num_i1)


                    ai_comb_p_1_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                    ai_comb_p_1_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
                    ai_comb_p_1_2.current(0)
                    window_ai_comb_p_1_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_p_1_2,tags=('aicombo5'))


                    label_2 = Label(inv_canvas_1,width=2,height=1,text="2", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel20'))

                    ai_comb_p_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),values=inv_data)
                    window_ai_comb_p_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=180, height=30,window=ai_comb_p_2,tags=('aicombo6'))
                    ai_comb_p_2.bind("<<ComboboxSelected>>",i_details_2)

                    ai_entry_p_2=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                    window_ai_entry_p_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_2,tags=('aientry8'))

                    ai_entry_p_2_1=scrolledtext.ScrolledText(inv_canvas_1,width=21,background='#2f516f',foreground="white")
                    window_ai_entry_p_2_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_2_1,tags=('aientry11'))

                    ai_entry_2_2=Spinbox(inv_canvas_1,width=13,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                    window_ai_entry_2_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_2_2,tags=('aientry14'))

                    ai_entry_2_3=Spinbox(inv_canvas_1,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                    window_ai_entry_2_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_2_3,tags=('aientry17'))

                    def multiply_num_i2(event):
                        num1= float(ai_entry_2_2.get())
                        num2= float(ai_entry_2_3.get())
                        mul_i= round(num1 * num2)
                        ai_entry_2_4.delete(0, END)
                        ai_entry_2_4.insert(0,mul_i)

                        

                    ai_entry_2_4=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
                    window_ai_entry_2_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_2_4,tags=('aientry20'))
                    ai_entry_2_4.bind("<Button-1>",multiply_num_i2)

                    ai_comb_P_2_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                    ai_comb_P_2_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
                    ai_comb_P_2_2.current(0)
                    window_ai_comb_P_2_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_P_2_2,tags=('aicombo9'))


                    label_2 = Label(inv_canvas_1,width=2,height=1,text="3", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel21'))

                    ai_comb_p_3 = ttk.Combobox(inv_canvas_1, font=('arial 10'),values=inv_data)
                    window_ai_comb_p_3 = inv_canvas_1.create_window(0, 0, anchor="nw", width=180, height=30,window=ai_comb_p_3,tags=('aicombo7'))
                    ai_comb_p_3.bind("<<ComboboxSelected>>",i_details_3)

                    ai_entry_3=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                    window_ai_entry_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3,tags=('aientry9'))

                    ai_entry_3_1=scrolledtext.ScrolledText(inv_canvas_1,width=21,background='#2f516f',foreground="white")
                    window_ai_entry_3_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_1,tags=('aientry12'))

                    ai_entry_3_2=Spinbox(inv_canvas_1,width=13,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                    window_ai_entry_3_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_2,tags=('aientry15'))

                    ai_entry_3_3=Spinbox(inv_canvas_1,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                    window_ai_entry_3_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_3,tags=('aientry18'))

                    def multiply_num_i3(event):
                        num1= float(ai_entry_3_2.get())
                        num2= float(ai_entry_3_3.get())
                        mul_i= round(num1 * num2)
                        ai_entry_3_4.delete(0, END)
                        ai_entry_3_4.insert(0,mul_i)

                        

                    ai_entry_3_4=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
                    window_ai_entry_3_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_4,tags=('aientry21'))
                    ai_entry_3_4.bind("<Button-1>",multiply_num_i3)

                    ai_comb_P_3_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                    ai_comb_P_3_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
                    ai_comb_P_3_2.current(0)
                    window_ai_comb_P_3_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_P_3_2,tags=('aicombo10'))

                    label_2 = Label(inv_canvas_1,width=2,height=1,text="4", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel22'))

                    ai_comb_p_4 = ttk.Combobox(inv_canvas_1, font=('arial 10'),values=inv_data)
                    window_ai_comb_p_4 = inv_canvas_1.create_window(0, 0, anchor="nw", width=180, height=30,window=ai_comb_p_4,tags=('aicombo8'))
                    ai_comb_p_4.bind("<<ComboboxSelected>>",i_details_4)

                    ai_entry_4=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                    window_ai_entry_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4,tags=('aientry10'))

                    ai_entry_4_1=scrolledtext.ScrolledText(inv_canvas_1,width=21,background='#2f516f',foreground="white")
                    window_ai_entry_4_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_1,tags=('aientry13'))

                    ai_entry_4_2=Spinbox(inv_canvas_1,width=13,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                    window_ai_entry_4_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_2,tags=('aientry16'))

                    ai_entry_4_3=Spinbox(inv_canvas_1,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                    window_ai_entry_4_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_3,tags=('aientry19'))

                    def multiply_num_i4(event):
                        num1= float(ai_entry_4_2.get())
                        num2= float(ai_entry_4_3.get())
                        mul_i= round(num1 * num2)
                        ai_entry_4_4.delete(0, END)
                        ai_entry_4_4.insert(0,mul_i)

                        


                    ai_entry_4_4=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
                    window_ai_entry_4_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_4,tags=('aientry22'))
                    ai_entry_4_4.bind("<Button-1>",multiply_num_i4)

                    ai_comb_P_4_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                    ai_comb_P_4_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
                    ai_comb_P_4_2.current(0)
                    window_ai_comb_P_4_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_P_4_2,tags=('aicombo11'))

                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine16'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine17'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine18'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine19'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine20'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine21'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine22'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine23'))
                    inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine24'))
                    

                    label_5 = Label(inv_canvas_1,width=10,height=1,text="Sub Total", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel23'))

                    label_5 = Label(inv_canvas_1,width=12,height=1,text="Tax Amount", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel24'))

                    label_5 = Label(inv_canvas_1,width=12,height=1,text="Grand Total", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel25'))

                    label_5 = Label(inv_canvas_1,width=12,height=1,text="Amount Received", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel26'))

                    label_5 = Label(inv_canvas_1,width=12,height=1,text="Balance Due", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel27'))

                    
                    mytext=StringVar()
                    sub_entry_1=Label(inv_canvas_1,width=30,justify=RIGHT,background='#2f516f',foreground="white")
                    window_sub_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=sub_entry_1,tags=('aientry23'))

                    tax_entry_1=Label(inv_canvas_1,width=30,justify=RIGHT,background='#2f516f',foreground="white")
                    window_tax_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=tax_entry_1,tags=('aientry24'))

                    grand_entry_1=Label(inv_canvas_1,width=30,justify=RIGHT,background='#2f516f',foreground="white")
                    window_grand_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=grand_entry_1,tags=('aientry25'))

                    amount_entry_1=Label(inv_canvas_1,width=30,justify=RIGHT,background='#2f516f',foreground="white")
                    window_amount_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=amount_entry_1,tags=('aientry26'))

                    bal_entry_1=Label(inv_canvas_1,width=30,justify=RIGHT, background='#2f516f',foreground="white")
                    window_bal_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=bal_entry_1,tags=('aientry27'))
                    

                    ai_save_btn1=Button(inv_canvas_1,text='Save', width=15,height=2,foreground="white",background="#1b3857",font='arial 12',command=sales_add_new_inv)
                    window_ai_save_btn1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=ai_save_btn1,tags=('aibutton2'))

                    def inv_back_1_():
                        inv_frame_1.grid_forget()
                        inv_frame.grid(row=0,column=0,sticky='nsew')

                    bck_btn1=Button(inv_canvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=inv_back_1_)
                    window_bck_btn1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('aibutton3'))

                    label_2 = Label(inv_canvas_1,width=14,height=1,text="Invoice Date:", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel7'))

                    label_2 = Label(inv_canvas_1,width=15,height=1,text="Due Date:", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel28'))



                    def term_date(event):
                        current_date = aid_entry_1.get()
                        current_date_temp = datetime.datetime.strptime(current_date, "%m/%d/%y")
                        if comb_t_2.get() == 'Due on Receipt':
                            newdate = current_date_temp + datetime.timedelta(days=0)
                            aid_entry_2.delete(0, END)
                            aid_entry_2.set_date(newdate)
                        elif comb_t_2.get() == 'NET 15':
                            newdate = current_date_temp + datetime.timedelta(days=15)
                            aid_entry_2.delete(0, END)
                            aid_entry_2.set_date(newdate)
                        elif comb_t_2.get() == 'NET 30':
                            newdate = current_date_temp + datetime.timedelta(days=30)
                            aid_entry_2.delete(0, END)
                            aid_entry_2.set_date(newdate)
                        elif comb_t_2.get() == 'NET 60':
                            newdate = current_date_temp + datetime.timedelta(days=60)
                            aid_entry_2.delete(0, END)
                            aid_entry_2.set_date(newdate)
                        elif comb_t_2.get() == 'Add New Term':
                            pass
                        else:
                            pass

                    comb_t_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'))
                    comb_t_2['values'] = ("Due on Receipt","NET 15","NET 30","NET 60","Add New Term",)
                    comb_t_2.current(0)
                    window_comb_t_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=251, height=30,window=comb_t_2,tags=('aicombo2'))
                    comb_t_2.bind("<<ComboboxSelected>>",term_date)

                    aid_entry_1=DateEntry(inv_canvas_1,width=40,justify=LEFT,foreground='white')
                    window_aid_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=aid_entry_1,tags=('aidate1'))

                    aid_entry_2=DateEntry(inv_canvas_1,width=40,justify=LEFT,foreground='white')
                    window_aid_entry_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=aid_entry_2,tags=('aidate2'))

                    
                    

                #-------------------------------Edit Section-----------------------------------#

                def edit_invoice():
                    inv_frame.grid_forget()
                    inv_frame_edit_1 = Frame(tab3_2)
                    inv_frame_edit_1.grid(row=0,column=0,sticky='nsew')

                    def inv_eresponsive_widgets2(event):
                        try:
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                            
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("aipoly1",x1 + r1,y1,
                            x1 + r1,y1,
                            x2 - r1,y1,
                            x2 - r1,y1,     
                            x2,y1,     
                            #--------------------
                            x2,y1 + r1,     
                            x2,y1 + r1,     
                            x2,y2 - r1,     
                            x2,y2 - r1,     
                            x2,y2,
                            #--------------------
                            x2 - r1,y2,     
                            x2 - r1,y2,     
                            x1 + r1,y2,
                            x1 + r1,y2,
                            x1,y2,
                            #--------------------
                            x1,y2 - r1,
                            x1,y2 - r1,
                            x1,y1 + r1,
                            x1,y1 + r1,
                            x1,y1,
                            )

                            dcanvas.coords("ailabel1",dwidth/2.45,dheight/8.24)
                            dcanvas.coords("aihline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/2.8
                            y21 = dheight/0.36


                            dcanvas.coords("aipoly2",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            dcanvas.coords("ailabel2",dwidth/2.45,dheight/2.34)
                            dcanvas.coords("ailabel3",dwidth/22.80,dheight/1.90)
                            dcanvas.coords("ailabel4",dwidth/20.00,dheight/1.65)
                            dcanvas.coords("ailabel5",dwidth/20.00,dheight/1.37)
                            dcanvas.coords("ailabel6",dwidth/3.34,dheight/1.37)
                            dcanvas.coords("ailabel7",dwidth/21.66 ,dheight/1.12)
                            dcanvas.coords("ailabel8",dwidth/3.34,dheight/1.12)
                            dcanvas.coords("ailabel9",dwidth/19.10,dheight/0.947)
                            dcanvas.coords("ailabel10",dwidth/19.40,dheight/0.717)
                            dcanvas.coords("ailabel11",dwidth/16.50,dheight/0.638)
                            dcanvas.coords("ailabel12",dwidth/8.40,dheight/0.638)
                            dcanvas.coords("ailabel13",dwidth/3.34,dheight/0.638)
                            dcanvas.coords("ailabel14",dwidth/2.28,dheight/0.638)
                            dcanvas.coords("ailabel15",dwidth/1.73,dheight/0.638)
                            dcanvas.coords("ailabel16",dwidth/1.52,dheight/0.638)
                            dcanvas.coords("ailabel17",dwidth/1.325,dheight/0.638)
                            dcanvas.coords("ailabel18",dwidth/1.165,dheight/0.638)
                            dcanvas.coords("ailabel19",dwidth/16.50,dheight/0.604)
                            dcanvas.coords("ailabel20",dwidth/16.50,dheight/0.562)
                            dcanvas.coords("ailabel21",dwidth/16.50,dheight/0.526)
                            dcanvas.coords("ailabel22",dwidth/16.50,dheight/0.496)
                            dcanvas.coords("ailabel23",dwidth/1.53,dheight/0.45)
                            dcanvas.coords("ailabel24",dwidth/1.54,dheight/0.435)
                            dcanvas.coords("ailabel25",dwidth/1.54,dheight/0.42)
                            dcanvas.coords("ailabel26",dwidth/1.54,dheight/0.406)
                            dcanvas.coords("ailabel27",dwidth/1.54,dheight/0.392)
                            dcanvas.coords("ailabel28",dwidth/1.72,dheight/1.12)
                            dcanvas.coords("ailabel29",dwidth/1.67,dheight/0.947)

                            dcanvas.coords("aientry1",dwidth/3.0,dheight/1.295)
                            dcanvas.coords("aientry2",dwidth/18.00,dheight/0.91)
                            dcanvas.coords("aientry3",dwidth/4.00,dheight/0.604)
                            dcanvas.coords("aientry4",dwidth/2.51,dheight/0.604)
                            dcanvas.coords("aientry5",dwidth/1.8,dheight/0.604)
                            dcanvas.coords("aientry6",dwidth/1.565,dheight/0.604)
                            dcanvas.coords("aientry7",dwidth/1.357,dheight/0.604)
                            dcanvas.coords("aientry8",dwidth/4.00,dheight/0.562)
                            dcanvas.coords("aientry9",dwidth/4.00,dheight/0.526)
                            dcanvas.coords("aientry10",dwidth/4.00,dheight/0.496)
                            dcanvas.coords("aientry11",dwidth/2.51,dheight/0.562)
                            dcanvas.coords("aientry12",dwidth/2.51,dheight/0.526)
                            dcanvas.coords("aientry13",dwidth/2.51,dheight/0.496)
                            dcanvas.coords("aientry14",dwidth/1.8,dheight/0.562)
                            dcanvas.coords("aientry15",dwidth/1.8,dheight/0.526)
                            dcanvas.coords("aientry16",dwidth/1.8,dheight/0.496)
                            dcanvas.coords("aientry17",dwidth/1.565,dheight/0.562)
                            dcanvas.coords("aientry18",dwidth/1.565,dheight/0.526)
                            dcanvas.coords("aientry19",dwidth/1.565,dheight/0.496)
                            dcanvas.coords("aientry20",dwidth/1.357,dheight/0.562)
                            dcanvas.coords("aientry21",dwidth/1.357,dheight/0.526)
                            dcanvas.coords("aientry22",dwidth/1.357,dheight/0.496)
                            dcanvas.coords("aientry23",dwidth/1.33,dheight/0.452)
                            dcanvas.coords("aientry24",dwidth/1.33,dheight/0.4365)
                            dcanvas.coords("aientry25",dwidth/1.33,dheight/0.4215)
                            dcanvas.coords("aientry26",dwidth/1.33,dheight/0.407)
                            dcanvas.coords("aientry27",dwidth/1.33,dheight/0.393)
                            dcanvas.coords("aientry28",dwidth/18.00,dheight/1.295)
                            dcanvas.coords("aientry29",dwidth/1.65,dheight/0.91)

                            dcanvas.coords("aicombo2",dwidth/3.00,dheight/1.074)
                            dcanvas.coords("aicombo3",dwidth/18.00,dheight/0.695)
                            dcanvas.coords("aicombo4",dwidth/10.10,dheight/0.604)
                            dcanvas.coords("aicombo5",dwidth/1.21,dheight/0.604)
                            dcanvas.coords("aicombo6",dwidth/10.10,dheight/0.562)
                            dcanvas.coords("aicombo7",dwidth/10.10,dheight/0.526)
                            dcanvas.coords("aicombo8",dwidth/10.10,dheight/0.496)
                            dcanvas.coords("aicombo9",dwidth/1.21,dheight/0.562)
                            dcanvas.coords("aicombo10",dwidth/1.21,dheight/0.526)
                            dcanvas.coords("aicombo11",dwidth/1.21,dheight/0.496)

                            dcanvas.coords("aibutton1",dwidth/4.74,dheight/1.295)
                            dcanvas.coords("aibutton2",dwidth/1.28,dheight/0.377)
                            dcanvas.coords("aibutton3",dwidth/23,dheight/3.415)

                            #-------------------------------H Lines-----------------------------------#
                            dcanvas.coords("ailine1",dwidth/21,dheight/0.645,dwidth/1.055,dheight/0.645)
                            dcanvas.coords("ailine2",dwidth/21,dheight/0.617,dwidth/1.055,dheight/0.617)
                            dcanvas.coords("ailine3",dwidth/21,dheight/0.576,dwidth/1.055,dheight/0.576)
                            dcanvas.coords("ailine4",dwidth/21,dheight/0.536,dwidth/1.055,dheight/0.536)
                            dcanvas.coords("ailine5",dwidth/21,dheight/0.506,dwidth/1.055,dheight/0.506)
                            dcanvas.coords("ailine6",dwidth/21,dheight/0.476,dwidth/1.055,dheight/0.476)
                            #-------------------------------V Lines-----------------------------------#
                            dcanvas.coords("ailine7",dwidth/21,dheight/0.645,dwidth/21,dheight/0.476)
                            dcanvas.coords("ailine8",dwidth/1.055,dheight/0.645,dwidth/1.055,dheight/0.476)
                            dcanvas.coords("ailine9",dwidth/11,dheight/0.645,dwidth/11,dheight/0.476)
                            dcanvas.coords("ailine10",dwidth/4.15,dheight/0.645,dwidth/4.15,dheight/0.476)
                            dcanvas.coords("ailine11",dwidth/2.55,dheight/0.645,dwidth/2.55,dheight/0.476)
                            dcanvas.coords("ailine12",dwidth/1.83,dheight/0.645,dwidth/1.83,dheight/0.476)
                            dcanvas.coords("ailine13",dwidth/1.58,dheight/0.645,dwidth/1.58,dheight/0.476)
                            dcanvas.coords("ailine14",dwidth/1.37,dheight/0.645,dwidth/1.37,dheight/0.476)
                            dcanvas.coords("ailine15",dwidth/1.22,dheight/0.645,dwidth/1.22,dheight/0.476)

                            #-------------------------------V Lines-----------------------------------#
                            dcanvas.coords("ailine16",dwidth/1.58,dheight/0.455,dwidth/1.58,dheight/0.383)
                            dcanvas.coords("ailine17",dwidth/1.348,dheight/0.455,dwidth/1.348,dheight/0.383)
                            dcanvas.coords("ailine18",dwidth/1.084,dheight/0.455,dwidth/1.084,dheight/0.383)
                            #-------------------------------H Lines-----------------------------------#
                            dcanvas.coords("ailine19",dwidth/1.58,dheight/0.455,dwidth/1.084,dheight/0.455)
                            dcanvas.coords("ailine20",dwidth/1.58,dheight/0.383,dwidth/1.084,dheight/0.383)
                            dcanvas.coords("ailine21",dwidth/1.58,dheight/0.439,dwidth/1.084,dheight/0.439)
                            dcanvas.coords("ailine22",dwidth/1.58,dheight/0.424,dwidth/1.084,dheight/0.424)
                            dcanvas.coords("ailine23",dwidth/1.58,dheight/0.41,dwidth/1.084,dheight/0.41)
                            dcanvas.coords("ailine24",dwidth/1.58,dheight/0.396,dwidth/1.084,dheight/0.396)

                        except:
                            pass

                        try:
                            dcanvas.coords("aidate1",dwidth/17.8,dheight/1.074)
                            dcanvas.coords("aidate2",dwidth/1.65,dheight/1.074)
                        except:
                            pass



                    inv_canvas_edit_1=Canvas(inv_frame_edit_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1800))

                    inv_frame_edit_1.grid_columnconfigure(0,weight=1)
                    inv_frame_edit_1.grid_rowconfigure(0,weight=1)
                    
                    vertibar=Scrollbar(inv_frame_edit_1, orient=VERTICAL)
                    vertibar.grid(row=0,column=1,sticky='ns')
                    vertibar.config(command=inv_canvas_edit_1.yview)

                    inv_canvas_edit_1.bind("<Configure>", inv_eresponsive_widgets2)
                    inv_canvas_edit_1.config(yscrollcommand=vertibar.set)
                    inv_canvas_edit_1.grid(row=0,column=0,sticky='nsew')

                    

                    inv_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly1"))

                    
                    label_1 = Label(inv_canvas_edit_1,width=10,height=1,text="INVOICE", font=('arial 20'),background="#1b3857",fg="white") 
                    window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ailabel1"))

                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("aihline"))

                    inv_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly2"))

                    label_1 = Label(inv_canvas_edit_1,width=10,height=1,text="Fin sYs", font=('arial 20'),background="#1b3857",fg="white") 
                    window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ailabel2"))

                    label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Company name", font=('arial 16'),background="#1b3857",fg="skyblue") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel3"))

                    label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Company email-id", font=('arial 16'),background="#1b3857",fg="skyblue") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel4"))

                    label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Select Customer", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel5"))


                    eientry_1=Entry(inv_canvas_edit_1,width=42,justify=LEFT,background='#2f516f',foreground="white")
                    window_eientry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=eientry_1,tags=('aientry28'))


                    label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel6'))

                    eaientry_1=Entry(inv_canvas_edit_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_eaientry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=eaientry_1,tags=('aientry1'))


                    label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Terms", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel8'))

                    ecomb_t_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
                    ecomb_t_2['values'] = ("Due on Receipt","NET 15","NET 30","NET 60","Add New Term",)
                    ecomb_t_2.current(0)
                    window_ecomb_t_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=251, height=30,window=ecomb_t_2,tags=('aicombo2'))


                    label_2 = Label(inv_canvas_edit_1,width=6,height=1,text="Bill To:", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel9'))

                    
                    eai_b_entry_1=scrolledtext.ScrolledText(inv_canvas_edit_1,width=30,background='#2f516f',foreground="white")
                    window_eai_b_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=150, window=eai_b_entry_1,tags=('aientry2'))

                    label_2 = Label(inv_canvas_edit_1,width=10,height=1,text="Invoice No:", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel29'))

                    ein_b_entry_1=Entry(inv_canvas_edit_1,width=42,justify=LEFT,background='#2f516f',foreground="white")
                    window_ein_b_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=ein_b_entry_1,tags=('aientry29'))

                    label_2 = Label(inv_canvas_edit_1,width=12,height=1,text="Place of supply", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel10'))

                    eai_p_comb_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
                    eai_p_comb_2['values'] = ("Kerala","Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Other Territory",)
                    eai_p_comb_2.current(0)
                    window_eai_p_comb_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=251, height=30,window=eai_p_comb_2,tags=('aicombo3'))


                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine1'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine2'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine3'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine4'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine5'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine6'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine7'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine8'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine9'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine10'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine11'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine12'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine13'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine14'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine15'))


                    label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="#", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel11'))

                    label_3 = Label(inv_canvas_edit_1,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_3,tags=('ailabel12'))

                    label_4 = Label(inv_canvas_edit_1,width=4,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel13'))

                    label_4 = Label(inv_canvas_edit_1,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel14'))

                    label_4 = Label(inv_canvas_edit_1,width=4,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel15'))

                    label_4 = Label(inv_canvas_edit_1,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel16'))

                    label_4 = Label(inv_canvas_edit_1,width=6,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel17'))

                    label_4 = Label(inv_canvas_edit_1,width=7,height=1,text="TAX (%)", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel18'))

                    label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="1", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_edit_1.create_window(90, 1020, anchor="nw", window=label_2,tags=('ailabel19'))

                    eai_comb_p_1 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
                    eai_comb_p_1['values'] = ("Select Product",)
                    eai_comb_p_1.current(0)
                    window_eai_comb_p_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=180, height=30,window=eai_comb_p_1,tags=('aicombo4'))

                    eai_entry_p_1=Entry(inv_canvas_edit_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                    window_eai_entry_p_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1,tags=('aientry3'))

                    eai_entry_p_1_2=scrolledtext.ScrolledText(inv_canvas_edit_1,width=21,background='#2f516f',foreground="white")
                    window_eai_entry_p_1_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1_2,tags=('aientry4'))

                    eai_entry_p_1_3=Spinbox(inv_canvas_edit_1,width=13,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                    window_eai_entry_p_1_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1_3,tags=('aientry5'))

                    eai_entry_p_1_4=Spinbox(inv_canvas_edit_1,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                    window_eai_entry_p_1_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1_4,tags=('aientry6'))

                    eai_entry_p_1_5=Entry(inv_canvas_edit_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
                    window_eai_entry_p_1_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1_5,tags=('aientry7'))

                    eai_comb_p_1_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
                    eai_comb_p_1_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
                    eai_comb_p_1_2.current(0)
                    window_eai_comb_p_1_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=150, height=30,window=eai_comb_p_1_2,tags=('aicombo5'))


                    label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="2", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel20'))

                    eai_comb_P_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
                    eai_comb_P_2['values'] = ("Select Product",)
                    eai_comb_P_2.current(0)
                    window_eai_comb_P_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=180, height=30,window=eai_comb_P_2,tags=('aicombo6'))

                    eai_entry_p_2=Entry(inv_canvas_edit_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                    window_eai_entry_p_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_2,tags=('aientry8'))

                    eai_entry_p_2_1=scrolledtext.ScrolledText(inv_canvas_edit_1,width=21,background='#2f516f',foreground="white")
                    window_eai_entry_p_2_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_2_1,tags=('aientry11'))

                    eai_entry_2_2=Spinbox(inv_canvas_edit_1,width=13,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                    window_eai_entry_2_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_2_2,tags=('aientry14'))

                    eai_entry_2_3=Spinbox(inv_canvas_edit_1,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                    window_eai_entry_2_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_2_3,tags=('aientry17'))

                    eai_entry_2_4=Entry(inv_canvas_edit_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
                    window_eai_entry_2_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_2_4,tags=('aientry20'))

                    eai_comb_P_2_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
                    eai_comb_P_2_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
                    eai_comb_P_2_2.current(0)
                    window_eai_comb_P_2_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=150, height=30,window=eai_comb_P_2_2,tags=('aicombo9'))


                    label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="3", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel21'))

                    eai_comb_p_3 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
                    eai_comb_p_3['values'] = ("Select Product",)
                    eai_comb_p_3.current(0)
                    window_eai_comb_p_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=180, height=30,window=eai_comb_p_3,tags=('aicombo7'))

                    eai_entry_3=Entry(inv_canvas_edit_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                    window_eai_entry_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3,tags=('aientry9'))

                    eai_entry_3_1=scrolledtext.ScrolledText(inv_canvas_edit_1,width=21,background='#2f516f',foreground="white")
                    window_eai_entry_3_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3_1,tags=('aientry12'))

                    eai_entry_3_2=Spinbox(inv_canvas_edit_1,width=13,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                    window_eai_entry_3_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3_2,tags=('aientry15'))

                    eai_entry_3_3=Spinbox(inv_canvas_edit_1,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                    window_eai_entry_3_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3_3,tags=('aientry18'))

                    eai_entry_3_4=Entry(inv_canvas_edit_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
                    window_eai_entry_3_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3_4,tags=('aientry21'))

                    eai_comb_P_3_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
                    eai_comb_P_3_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
                    eai_comb_P_3_2.current(0)
                    window_eai_comb_P_3_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=150, height=30,window=eai_comb_P_3_2,tags=('aicombo10'))

                    label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="4", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel22'))

                    eai_comb_p_4 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
                    eai_comb_p_4['values'] = ("Select Product",)
                    eai_comb_p_4.current(0)
                    window_eai_comb_p_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=180, height=30,window=eai_comb_p_4,tags=('aicombo8'))

                    eai_entry_4=Entry(inv_canvas_edit_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
                    window_eai_entry_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4,tags=('aientry10'))

                    eai_entry_4_1=scrolledtext.ScrolledText(inv_canvas_edit_1,width=21,background='#2f516f',foreground="white")
                    window_eai_entry_4_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4_1,tags=('aientry13'))

                    eai_entry_4_2=Spinbox(inv_canvas_edit_1,width=13,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                    window_eai_entry_4_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4_2,tags=('aientry16'))

                    eai_entry_4_3=Spinbox(inv_canvas_edit_1,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                    window_eai_entry_4_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4_3,tags=('aientry19'))

                    eai_entry_4_4=Entry(inv_canvas_edit_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
                    window_eai_entry_4_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4_4,tags=('aientry22'))

                    eai_comb_P_4_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
                    eai_comb_P_4_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
                    eai_comb_P_4_2.current(0)
                    window_eai_comb_P_4_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=150, height=30,window=eai_comb_P_4_2,tags=('aicombo11'))

                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine16'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine17'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine18'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine19'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine20'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine21'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine22'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine23'))
                    inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine24'))
                    

                    label_5 = Label(inv_canvas_edit_1,width=10,height=1,text="Sub Total", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel23'))

                    label_5 = Label(inv_canvas_edit_1,width=12,height=1,text="Tax Amount", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel24'))

                    label_5 = Label(inv_canvas_edit_1,width=12,height=1,text="Grand Total", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel25'))

                    label_5 = Label(inv_canvas_edit_1,width=12,height=1,text="Amount Received", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel26'))

                    label_5 = Label(inv_canvas_edit_1,width=12,height=1,text="Balance Due", font=('arial 10'),background="#1b3857",fg="white") 
                    window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel27'))

                    esub_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
                    window_esub_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=esub_entry_1,tags=('aientry23'))

                    etax_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
                    window_etax_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=etax_entry_1,tags=('aientry24'))

                    egrand_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
                    window_egrand_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=egrand_entry_1,tags=('aientry25'))

                    eamount_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
                    window_eamount_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eamount_entry_1,tags=('aientry26'))

                    ebal_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
                    window_ebal_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=ebal_entry_1,tags=('aientry27'))
                    

                    eai_save_btn1=Button(inv_canvas_edit_1,text='Save', width=15,height=2,foreground="white",background="#1b3857",font='arial 12')
                    window_eai_save_btn1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=eai_save_btn1,tags=('aibutton2'))

                    def einv_back_1_():
                        inv_frame_edit_1.grid_forget()
                        inv_frame.grid(row=0,column=0,sticky='nsew')

                    eibck_btn1=Button(inv_canvas_edit_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=einv_back_1_)
                    window_eibck_btn1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=eibck_btn1,tags=('aibutton3'))

                    label_2 = Label(inv_canvas_edit_1,width=14,height=1,text="Invoice Date:", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel7'))

                    label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Due Date:", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel28'))

                    eaid_entry_1=DateEntry(inv_canvas_edit_1,width=40,justify=LEFT,foreground='white')
                    window_eaid_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eaid_entry_1,tags=('aidate1'))

                    eaid_entry_2=DateEntry(inv_canvas_edit_1,width=40,justify=LEFT,foreground='white')
                    window_eaid_entry_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eaid_entry_2,tags=('aidate2'))

                #-------------------------------View Section-----------------------------------#

                def view_invoice():
                    inv_frame.grid_forget()
                    inv_frame_view_1 = Frame(tab3_2)
                    inv_frame_view_1.grid(row=0,column=0,sticky='nsew')

                    def inv_eresponsive_widgets3(event):
                        
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget
                            
                        dcanvas.coords("aivbutton1",dwidth/1.45,dheight/8.24)
                        dcanvas.coords("aivbutton2",dwidth/1.20,dheight/8.24)

                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/14 
                        y2 = dheight/3.505

                        dcanvas.coords("aiipoly1",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        dcanvas.coords("aiilabel1",dwidth/2.45,dheight/8.24)

                        r2 = 25
                        x11 = dwidth/63
                        x21 = dwidth/1.021
                        y11 = dheight/2.8
                        y21 = dheight/0.36


                        dcanvas.coords("aiipoly2",x11 + r2,y11,
                        x11 + r2,y11,
                        x21 - r2,y11,
                        x21 - r2,y11,     
                        x21,y11,     
                        #--------------------
                        x21,y11 + r2,     
                        x21,y11 + r2,     
                        x21,y21 - r2,     
                        x21,y21 - r2,     
                        x21,y21,
                        #--------------------
                        x21 - r2,y21,     
                        x21 - r2,y21,     
                        x11 + r2,y21,
                        x11 + r2,y21,
                        x11,y21,
                        #--------------------
                        x11,y21 - r2,
                        x11,y21 - r2,
                        x11,y11 + r2,
                        x11,y11 + r2,
                        x11,y11,
                        )

                    
                        r2 = 5
                        x11 = dwidth/12
                        x21 = dwidth/1.1
                        y11 = dheight/2.5
                        y21 = dheight/0.38


                        dcanvas.coords("aivpoly1",x11 + r2,y11,
                        x11 + r2,y11,
                        x21 - r2,y11,
                        x21 - r2,y11,     
                        x21,y11,     
                        #--------------------
                        x21,y11 + r2,     
                        x21,y11 + r2,     
                        x21,y21 - r2,     
                        x21,y21 - r2,     
                        x21,y21,
                        #--------------------
                        x21 - r2,y21,     
                        x21 - r2,y21,     
                        x11 + r2,y21,
                        x11 + r2,y21,
                        x11,y21,
                        #--------------------
                        x11,y21 - r2,
                        x11,y21 - r2,
                        x11,y11 + r2,
                        x11,y11 + r2,
                        x11,y11,
                        )

                        dcanvas.coords("aivlabel1",dwidth/9.40,dheight/1.85)
                        dcanvas.coords("aivlabel2",dwidth/9,dheight/1.70)
                        dcanvas.coords("aivlabel3",dwidth/9,dheight/1.55)
                        dcanvas.coords("aivlabel4",dwidth/9.45,dheight/1.42)
                        dcanvas.coords("aivlabel5",dwidth/9.50,dheight/1.32)
                        dcanvas.coords("aivlabel6",dwidth/9.35,dheight/1.22)
                        dcanvas.coords("aivlabel7",dwidth/9.70,dheight/1.14)
                        dcanvas.coords("aivlabel8",dwidth/9.50,dheight/1.0)
                        dcanvas.coords("aivlabel9",dwidth/1.45,dheight/1.0)
                        dcanvas.coords("aivlabel10",dwidth/1.44,dheight/0.95)
                        dcanvas.coords("aivlabel11",dwidth/1.46,dheight/0.90)
                        dcanvas.coords("aivlabel12",dwidth/1.48,dheight/0.85)

                        dcanvas.coords("aivtree1",dwidth/7.5,dheight/0.75)

                        dcanvas.coords("aivline16",dwidth/1.56,dheight/0.6,dwidth/1.56,dheight/0.52)
                        dcanvas.coords("aivline17",dwidth/1.346,dheight/0.6,dwidth/1.346,dheight/0.52)
                        dcanvas.coords("aivline18",dwidth/1.182,dheight/0.6,dwidth/1.182,dheight/0.52)
                        dcanvas.coords("aivline19",dwidth/1.56,dheight/0.6,dwidth/1.182,dheight/0.6)
                        dcanvas.coords("aivline20",dwidth/1.56,dheight/0.52,dwidth/1.182,dheight/0.52)
                        dcanvas.coords("aivline21",dwidth/1.56,dheight/0.572,dwidth/1.182,dheight/0.572)
                        dcanvas.coords("aivline22",dwidth/1.56,dheight/0.545,dwidth/1.182,dheight/0.545)

                        dcanvas.coords("aivlabel13",dwidth/1.54,dheight/0.59)
                        dcanvas.coords("aivlabel14",dwidth/1.54,dheight/0.565)
                        dcanvas.coords("aivlabel15",dwidth/1.5,dheight/0.54)

                        dcanvas.coords("aivline23",dwidth/10,dheight/0.4,dwidth/1.12,dheight/0.4)

                        dcanvas.coords("aivlabel16",dwidth/4,dheight/0.395)

                        dcanvas.coords("aivbutton3",dwidth/23,dheight/3.415)

                    inv_canvas_view_1=Canvas(inv_frame_view_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1800))

                    inv_frame_view_1.grid_columnconfigure(0,weight=1)
                    inv_frame_view_1.grid_rowconfigure(0,weight=1)
                    
                    vertibar=Scrollbar(inv_frame_view_1, orient=VERTICAL)
                    vertibar.grid(row=0,column=1,sticky='ns')
                    vertibar.config(command=inv_canvas_view_1.yview)

                    inv_canvas_view_1.bind("<Configure>", inv_eresponsive_widgets3)
                    inv_canvas_view_1.config(yscrollcommand=vertibar.set)
                    inv_canvas_view_1.grid(row=0,column=0,sticky='nsew')

                    inv_canvas_view_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aiipoly1"))

                    
                    label_1 = Label(inv_canvas_view_1,width=10,height=1,text="INVOICE", font=('arial 20'),background="#1b3857",fg="white") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aiilabel1"))

                    eai_dwnl_btn1=Button(inv_canvas_view_1,text='Download Pdf', width=15,height=2,foreground="skyblue",background="#1b3857",font='arial 12')
                    window_eai_dwnl_btn1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=eai_dwnl_btn1,tags=('aivbutton1'))

                    eai_prnt_btn1=Button(inv_canvas_view_1,text='Print', width=15,height=2,foreground="skyblue",background="#1b3857",font='arial 12')
                    window_eai_prnt_btn1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=eai_prnt_btn1,tags=('aivbutton2'))

                    inv_canvas_view_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aiipoly2"))

                    inv_canvas_view_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="white",tags=("aivpoly1"))

                    label_1 = Label(inv_canvas_view_1,width=11,height=1,text="Unknown", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel1"))

                    label_1 = Label(inv_canvas_view_1,width=13,height=1,text="Addressline 1", font=('arial 12 '),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel2"))

                    label_1 = Label(inv_canvas_view_1,width=13,height=1,text="Addressline 2", font=('arial 12 '),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel3"))

                    label_1 = Label(inv_canvas_view_1,width=11,height=1,text="Pincode", font=('arial 12'),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel4"))

                    label_1 = Label(inv_canvas_view_1,width=11,height=1,text="Email ID", font=('arial 12'),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel5"))

                    label_1 = Label(inv_canvas_view_1,width=15,height=1,text="Phone Number", font=('arial 12'),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel6"))

                    label_1 = Label(inv_canvas_view_1,width=13,height=1,text="TAX INVOICE", font=('arial 20 bold'),background="white",fg="skyblue") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel7"))

                    label_1 = Label(inv_canvas_view_1,width=11,height=1,text="Bill To", font=('arial 14 bold'),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel8"))

                    label_1 = Label(inv_canvas_view_1,width=11,height=1,text="Invoice No", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel9"))

                    label_1 = Label(inv_canvas_view_1,width=11,height=1,text="Invoice Date", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel10"))

                    label_1 = Label(inv_canvas_view_1,width=11,height=1,text="Due Date", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel11"))

                    label_1 = Label(inv_canvas_view_1,width=11,height=1,text="Terms", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel12"))

                    fgthvi = ttk.Style()
                    fgthvi.configure('mystyle1.Treeview.Heading', background='skyblue',State='DISABLE')

                    iview_tree = ttk.Treeview(inv_canvas_view_1, columns = (1,2,3,4,5,6,7), height = 10, show = "headings",style='mystyle1.Treeview')
                    iview_tree.pack(side = 'top')
                    iview_tree.heading(1)
                    iview_tree.heading(2, text="PRODUCT/SERVICES")
                    iview_tree.heading(3, text="HSN")
                    iview_tree.heading(4, text="QTY")
                    iview_tree.heading(5, text="PRICE")
                    iview_tree.heading(6, text="TOTAL")
                    iview_tree.heading(7, text="TAX(%)")
                    
                    iview_tree.column(1, width = 20)
                    iview_tree.column(2, width = 200)
                    iview_tree.column(3, width = 200)
                    iview_tree.column(4, width = 100)
                    iview_tree.column(5, width = 150)
                    iview_tree.column(6, width = 150)
                    iview_tree.column(7, width = 150)

                    window = inv_canvas_view_1.create_window(0, 0, anchor="nw", height=25, window=iview_tree,tags=('aivtree1'))

                    inv_canvas_view_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline16'))
                    inv_canvas_view_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline17'))
                    inv_canvas_view_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline18'))
                    inv_canvas_view_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline19'))
                    inv_canvas_view_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline20'))
                    inv_canvas_view_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline21'))
                    inv_canvas_view_1.create_line(0, 0, 0, 0, fill='black',width=1, tags=('aivline22'))

                    label_1 = Label(inv_canvas_view_1,width=11,height=1,text="Subtotal", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel13"))

                    label_1 = Label(inv_canvas_view_1,width=11,height=1,text="Tax Amount", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel14"))

                    label_1 = Label(inv_canvas_view_1,width=5,height=1,text="Total", font=('arial 12 bold'),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel15"))

                    inv_canvas_view_1.create_line(0, 0, 0, 0, fill='grey',width=1, tags=('aivline23'))

                    label_1 = Label(inv_canvas_view_1,width=75,height=0,text="Invoice was created on a computer and is valid without the signature and seal.", font=('arial 12'),background="white",fg="black") 
                    window_label_1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aivlabel16"))

                    def vinv_back_1_():
                        inv_frame_view_1.grid_forget()
                        inv_frame.grid(row=0,column=0,sticky='nsew')

                    vibck_btn1=Button(inv_canvas_view_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=vinv_back_1_)
                    window_vibck_btn1 = inv_canvas_view_1.create_window(0, 0, anchor="nw", window=vibck_btn1,tags=('aivbutton3'))

         

                btn1=Button(inv_canvas,text='Add Invoices', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_invoice)
                window_btn1 = inv_canvas.create_window(0, 0, anchor="nw", window=btn1,tags=('ibutton1'))

                eibtn1=Button(inv_canvas,text='Edit', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=lambda:edit_invoice())
                window_eibtn1 = inv_canvas.create_window(0, 0, anchor="nw", window=eibtn1, tags=("ibutton2"))

                vibtn1=Button(inv_canvas,text='View', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=lambda:view_invoice())
                window_vibtn1 = inv_canvas.create_window(0, 0, anchor="nw", window=vibtn1, tags=("ibutton3"))

                dibtn1=Button(inv_canvas,text='Delete', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_dibtn1 = inv_canvas.create_window(0, 0, anchor="nw", window=dibtn1, tags=("ibutton4"))

                #-------------------------------Customers-----------------------------#
                tab3_3.grid_columnconfigure(0,weight=1)
                tab3_3.grid_rowconfigure(0,weight=1)

                cus_frame = Frame(tab3_3)
                cus_frame.grid(row=0,column=0,sticky='nsew')

                def cus_responsive_widgets(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget

                    dcanvas.coords("ctree1",dwidth/12,dheight/1.8)
                    

                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/1.021
                    y1 = dheight/14 
                    y2 = dheight/3.505

                    dcanvas.coords("cpoly1",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    dcanvas.coords("chline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                    dcanvas.coords("clabel1",dwidth/2.5,dheight/8.00)

                    r2 = 25
                    x11 = dwidth/63
                    x21 = dwidth/1.021
                    y11 = dheight/2.8
                    y21 = dheight/0.8


                    dcanvas.coords("cpoly2",x11 + r2,y11,
                    x11 + r2,y11,
                    x21 - r2,y11,
                    x21 - r2,y11,     
                    x21,y11,     
                    #--------------------
                    x21,y11 + r2,     
                    x21,y11 + r2,     
                    x21,y21 - r2,     
                    x21,y21 - r2,     
                    x21,y21,
                    #--------------------
                    x21 - r2,y21,     
                    x21 - r2,y21,     
                    x11 + r2,y21,
                    x11 + r2,y21,
                    x11,y21,
                    #--------------------
                    x11,y21 - r2,
                    x11,y21 - r2,
                    x11,y11 + r2,
                    x11,y11 + r2,
                    x11,y11,
                    )

                    dcanvas.coords("cbutton1",dwidth/2.1,dheight/2.4)
                    dcanvas.coords("cbutton2",dwidth/1.59,dheight/2.4)
                    dcanvas.coords("cbutton3",dwidth/1.28,dheight/2.26)
                    dcanvas.coords("ccombo1",dwidth/1.179,dheight/1.52)


                cus_canvas=Canvas(cus_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

                cus_frame.grid_rowconfigure(0,weight=1)
                cus_frame.grid_columnconfigure(0,weight=1)

                vertibar=Scrollbar(cus_frame, orient=VERTICAL)
                vertibar.grid(row=0,column=1,sticky='ns')
                vertibar.config(command=cus_canvas.yview)
                cus_canvas.bind("<Configure>", cus_responsive_widgets)
                cus_canvas.config(yscrollcommand=vertibar.set)
                cus_canvas.grid(row=0,column=0,sticky='nsew')

                cus_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("cpoly1"))

                label_1 = Label(cus_canvas,width=12,height=1,text="CUSTOMERS", font=('arial 25'),background="#1b3857",fg="white") 
                window_label_1 = cus_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("clabel1"))

                cus_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("chline"))

                
                cus_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("cpoly2"))



                fgthi = ttk.Style()
                fgthi.configure('mystyle105.Treeview.Heading', background='#2f516f',State='DISABLE')

                cus_tree = ttk.Treeview(cus_canvas, columns = (1,2,3,4,5,6,7), height = 10, show = "headings",style='mystyle105.Treeview')
                cus_tree.pack(side = 'top')
                cus_tree.heading(1)
                cus_tree.heading(2, text="CUSTOMER")
                cus_tree.heading(3, text="GST TYPE")
                cus_tree.heading(4, text="GSTIN")
                cus_tree.heading(5, text="PAN NO")
                cus_tree.heading(6, text="EMAIL ID")
                cus_tree.heading(7, text="MOBILE NO")
                
                cus_tree.column(1, width = 50)
                cus_tree.column(2, width = 200)
                cus_tree.column(3, width = 220)
                cus_tree.column(4, width = 150)
                cus_tree.column(5, width = 150)
                cus_tree.column(6, width = 200)
                cus_tree.column(7, width = 150)
                window_label_4 = cus_canvas.create_window(0, 0, anchor="nw", window=cus_tree,tags=('ctree1'))

                sql_pr="select * from auth_user where username=%s"
                sql_pr_val=(nm_ent.get(),)
                fbcursor.execute(sql_pr,sql_pr_val,)
                pr_dtl=fbcursor.fetchone()

                sql = "select * from app1_company where id_id=%s"
                val = (pr_dtl[0],)
                fbcursor.execute(sql, val,)
                cmp_dtl=fbcursor.fetchone()

                c_sql_1 = "SELECT * FROM app1_customer where cid_id=%s"
                c_val_1 = (cmp_dtl[0],)
                fbcursor.execute(c_sql_1,c_val_1,)
                c_data_1 = fbcursor.fetchall()

                count0 = 0
                for i in c_data_1:
                    if True:
                       cus_tree.insert(parent='',index='end',iid=i,text='',values=('',i[2]+" "+i[3],i[6],i[7],i[8],i[9],i[11])) 
                    else:
                        pass
                count0 += 1


                def add_customer():
                    cus_frame.grid_forget()
                    cus_frame_1 = Frame(tab3_3)
                    cus_frame_1.grid(row=0,column=0,sticky='nsew')

                    def cus_responsive_widgets2(event):
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget
                        
                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/14 
                        y2 = dheight/3.505

                        dcanvas.coords("acpoly1",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
                        dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                        r2 = 25
                        x11 = dwidth/63
                        x21 = dwidth/1.021
                        y11 = dheight/2.8
                        y21 = dheight/0.45


                        dcanvas.coords("acpoly2",x11 + r2,y11,
                        x11 + r2,y11,
                        x21 - r2,y11,
                        x21 - r2,y11,     
                        x21,y11,     
                        #--------------------
                        x21,y11 + r2,     
                        x21,y11 + r2,     
                        x21,y21 - r2,     
                        x21,y21 - r2,     
                        x21,y21,
                        #--------------------
                        x21 - r2,y21,     
                        x21 - r2,y21,     
                        x11 + r2,y21,
                        x11 + r2,y21,
                        x11,y21,
                        #--------------------
                        x11,y21 - r2,
                        x11,y21 - r2,
                        x11,y11 + r2,
                        x11,y11 + r2,
                        x11,y11,
                        )

                        dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
                        dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
                        dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
                        dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
                        dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
                        dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
                        dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
                        dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
                        dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
                        dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
                        dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
                        dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
                        dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
                        dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
                        dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
                        dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
                        dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
                        dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
                        dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
                        dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
                        dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
                        dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
                        dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
                        dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
                        dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

                        dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
                        dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

                        dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
                        dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
                        dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
                        dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
                        dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
                        dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
                        dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
                        dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
                        dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
                        dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
                        dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
                        dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
                        dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
                        dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
                        dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
                        dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
                        dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
                        dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
                        dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

                        dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
                        dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

                        dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
                        dcanvas.coords("acbutton3",dwidth/23,dheight/3.415)


                    cus_canvas_1=Canvas(cus_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

                    cus_frame_1.grid_columnconfigure(0,weight=1)
                    cus_frame_1.grid_rowconfigure(0,weight=1)

                    
                    vertibar=Scrollbar(cus_frame_1, orient=VERTICAL)
                    vertibar.grid(row=0,column=1,sticky='ns')
                    vertibar.config(command=cus_canvas_1.yview)

                    cus_canvas_1.bind("<Configure>", cus_responsive_widgets2)
                    cus_canvas_1.config(yscrollcommand=vertibar.set)
                    cus_canvas_1.grid(row=0,column=0,sticky='nsew')
                    
                    def sales_add_new_cus():
                        title = comb_cus_1.get()
                        firstname = entry_cus_f1.get()
                        lastname = entry_cus_l2.get()
                        company = entry_cus_com3.get()
                        location = cus_loc4.get()
                        gsttype = comb_cus_g2.get()
                        gstin = entry_cus_gin5.get()
                        panno = entry_cus_pan6.get()
                        email = entry_cus_em7.get()
                        website = entry_cus_web8.get()
                        mobile = entry_cus_mob9.get()
                        street = entry_cus_10.get()
                        city = entry_cus_12.get()
                        state = entry_cus_13.get()
                        pincode = entry_cus_p12.get()
                        country = entry_cus_c13.get()
                        shipstreet = entry_cus_11.get()
                        shipcity = entry_cus_14.get()
                        shipstate = entry_cus_15.get()
                        shippincode = entry_cus_pin.get()
                        shipcountry = entry_cus_c15.get()

                        usr_sql = "SELECT id FROM auth_user WHERE username=%s"
                        usr_val = (nm_ent.get(),)
                        fbcursor.execute(usr_sql,usr_val)
                        usr_data = fbcursor.fetchone()

                        cmp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                        cmp_val = (usr_data[0],)
                        fbcursor.execute(cmp_sql,cmp_val)
                        cmp_data = fbcursor.fetchone()
                        cid = cmp_data[0]

                        if chk_str_1.get() == True:

                            cus_sql = "INSERT INTO app1_customer (title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            cus_val=(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid)
                            fbcursor.execute(cus_sql,cus_val)
                            finsysdb.commit()

                            #----------Refresh Insert Tree--------#

                            for record in cus_tree.get_children():
                                    cus_tree.delete(record)

                            sql_pr="select * from auth_user where username=%s"
                            sql_pr_val=(nm_ent.get(),)
                            fbcursor.execute(sql_pr,sql_pr_val,)
                            pr_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pr_dtl[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dtl=fbcursor.fetchone()

                            c_sql_1 = "SELECT * FROM app1_customer where cid_id=%s"
                            c_val_1 = (cmp_dtl[0],)
                            fbcursor.execute(c_sql_1,c_val_1,)
                            c_data_1 = fbcursor.fetchall()

                            count0 = 0
                            for i in c_data_1:
                                if True:
                                    cus_tree.insert(parent='',index='end',iid=i,text='',values=('',i[2]+" "+i[3],i[6],i[7],i[8],i[9],i[11])) 
                                else:
                                    pass
                            count0 += 1

                            
                            cus_frame_1.destroy()
                            cus_frame.grid(row=0,column=0,sticky='nsew')

                        else:
                            pass
                       

                    cus_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

                    label_1 = Label(cus_canvas_1,width=15,height=1,text="ADD CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
                    window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

                    cus_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

                    cus_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))

                    label_1 = Label(cus_canvas_1,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
                    window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))

                    cus_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))

                    label_2 = Label(cus_canvas_1,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel3"))

                    comb_cus_1 = ttk.Combobox(cus_canvas_1, font=('arial 10'))
                    comb_cus_1['values'] = ("Mr","Mrs","Miss","Ms",)
                    comb_cus_1.current(0)
                    window_comb_cus_1 = cus_canvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_cus_1, tags=("accombo1"))

                    label_2 = Label(cus_canvas_1,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel4"))

                    entry_cus_f1=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_f1 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_f1, tags=("acentry1"))

                    label_2 = Label(cus_canvas_1,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel5"))

                    entry_cus_l2=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_l2 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_l2, tags=("acentry2"))

                    label_2 = Label(cus_canvas_1,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel6"))

                    entry_cus_com3=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_com3 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_com3, tags=("acentry3"))

                    label_2 = Label(cus_canvas_1,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel7"))

                    cus_loc4=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_cus_loc4 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=cus_loc4, tags=("acentry4"))

                    label_2 = Label(cus_canvas_1,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel8"))

                    comb_cus_g2 = ttk.Combobox(cus_canvas_1, font=('arial 10'))
                    comb_cus_g2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
                    comb_cus_g2.current(0)
                    window_comb_cus_g2 = cus_canvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_cus_g2, tags=("accombo2"))

                    label_2 = Label(cus_canvas_1,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel9"))

                    def ac_gst_in(event):
                        if entry_cus_gin5.get()=="29APPCK7465F1Z1":
                            entry_cus_gin5.delete(0,END)
                        else:
                            pass
                    
                    entry_cus_gin5=Entry(cus_canvas_1,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'))
                    window_entry_cus_gin5 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_gin5, tags=("acentry5"))
                    entry_cus_gin5.insert(0,"29APPCK7465F1Z1")
                    entry_cus_gin5.bind("<Button-1>",ac_gst_in)


                    label_2 = Label(cus_canvas_1,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel10"))

                    def ac_pan_no(event):
                        if entry_cus_pan6.get()=="APPCK7465F":
                            entry_cus_pan6.delete(0,END)
                        else:
                            pass

                    entry_cus_pan6=Entry(cus_canvas_1,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'))
                    window_entry_cus_pan6 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_pan6, tags=("acentry6"))
                    entry_cus_pan6.insert(0,"APPCK7465F")
                    entry_cus_pan6.bind("<Button-1>",ac_pan_no)

                    label_2 = Label(cus_canvas_1,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel11"))

                    entry_cus_em7=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_em7 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_em7, tags=("acentry7"))

                    label_2 = Label(cus_canvas_1,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel12"))

                    entry_cus_web8=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_web8 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_web8, tags=("acentry8"))

                    label_2 = Label(cus_canvas_1,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel13"))

                    entry_cus_mob9=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_mob9 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_mob9, tags=("acentry9"))

                    def copy_cus_details():
                        entry_cus_11.delete(0, END)
                        entry_cus_11.insert(0,entry_cus_10.get())
                        entry_cus_14.delete(0, END)
                        entry_cus_14.insert(0,entry_cus_12.get())
                        entry_cus_15.delete(0, END)
                        entry_cus_15.insert(0,entry_cus_13.get())
                        entry_cus_pin.delete(0, END)
                        entry_cus_pin.insert(0,entry_cus_p12.get())
                        entry_cus_c15.delete(0, END)
                        entry_cus_c15.insert(0,entry_cus_c13.get())

                    label_1 = Label(cus_canvas_1,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
                    window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel14"))

                    label_2 = Label(cus_canvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel16"))

                    entry_cus_10=Entry(cus_canvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_10 = cus_canvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_cus_10, tags=("acentry10"))

                    label_1 = Label(cus_canvas_1,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
                    window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel15"))

                    label_2 = Label(cus_canvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel17"))

                    entry_cus_11=Entry(cus_canvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_11 = cus_canvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_cus_11, tags=("acentry11"))

                    label_2 = Label(cus_canvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel18"))

                    entry_cus_12=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_12 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_12, tags=("acentry12"))
                    
                    label_2 = Label(cus_canvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel19"))

                    entry_cus_13=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_13 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_13, tags=("acentry13"))

                    label_2 = Label(cus_canvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel20"))

                    entry_cus_14=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_14 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_14, tags=("acentry14"))

                    label_2 = Label(cus_canvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel21"))

                    entry_cus_15=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_15 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_15, tags=("acentry15"))

                    label_2 = Label(cus_canvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel22"))

                    entry_cus_p12=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_p12 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_p12, tags=("acentry16"))
                    
                    label_2 = Label(cus_canvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel23"))

                    entry_cus_c13=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_c13 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_c13, tags=("acentry17"))

                    label_2 = Label(cus_canvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel24"))

                    entry_cus_pin=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_pin = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_pin, tags=("acentry18"))

                    label_2 = Label(cus_canvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                    window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel25"))

                    entry_cus_c15=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                    window_entry_cus_c15 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_c15, tags=("acentry19"))

                    chk_str = StringVar()
                    chkbtn1 = Checkbutton(cus_canvas_1, text = "Same As Billing Address", variable = chk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f",command=copy_cus_details)
                    chkbtn1.select()
                    window_chkbtn_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=chkbtn1, tags=("accheck1"))

                    chk_str_1 = BooleanVar()
                    chkbtn2 = Checkbutton(cus_canvas_1, text = "Agree to terms and conditions", variable = chk_str_1, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
                    chkbtn2.select()
                    window_chkbtn_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=chkbtn2,tags=("accheck2"))

                    def ac_back_1_():
                        cus_frame_1.grid_forget()
                        cus_frame.grid(row=0,column=0,sticky='nsew')

                    ac_bck_btn1=Button(cus_canvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=ac_back_1_)
                    window_ac_bck_btn1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=ac_bck_btn1,tags=('acbutton3'))

                    cus_btn2=Button(cus_canvas_1,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12',command=sales_add_new_cus)
                    window_cus_btn2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=cus_btn2,tags=("acbutton1"))

                btn1=Button(cus_canvas,text='Add Customer', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_customer)
                window_btn1 = cus_canvas.create_window(0, 0, anchor="nw", window=btn1, tags=("cbutton2"))

                def edit_customer(event):
                    if cus_comb_1.get() == 'Edit':
                        cus_frame.grid_forget()
                        cus_eframe_1 = Frame(tab3_3)
                        cus_eframe_1.grid(row=0,column=0,sticky='nsew')

                        def ecus_responsive_widgets2(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                            
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("acpoly1",x1 + r1,y1,
                            x1 + r1,y1,
                            x2 - r1,y1,
                            x2 - r1,y1,     
                            x2,y1,     
                            #--------------------
                            x2,y1 + r1,     
                            x2,y1 + r1,     
                            x2,y2 - r1,     
                            x2,y2 - r1,     
                            x2,y2,
                            #--------------------
                            x2 - r1,y2,     
                            x2 - r1,y2,     
                            x1 + r1,y2,
                            x1 + r1,y2,
                            x1,y2,
                            #--------------------
                            x1,y2 - r1,
                            x1,y2 - r1,
                            x1,y1 + r1,
                            x1,y1 + r1,
                            x1,y1,
                            )

                            dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
                            dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/2.8
                            y21 = dheight/0.45


                            dcanvas.coords("acpoly2",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
                            dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
                            dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
                            dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
                            dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
                            dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
                            dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
                            dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
                            dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
                            dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
                            dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
                            dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
                            dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
                            dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
                            dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
                            dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
                            dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
                            dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
                            dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
                            dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
                            dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
                            dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
                            dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
                            dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
                            dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

                            dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
                            dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

                            dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
                            dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
                            dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
                            dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
                            dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
                            dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
                            dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
                            dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
                            dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
                            dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
                            dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
                            dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
                            dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
                            dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
                            dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
                            dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
                            dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
                            dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
                            dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

                            dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
                            dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

                            dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
                            dcanvas.coords("acbutton3",dwidth/23,dheight/3.415)


                        cus_ecanvas_1=Canvas(cus_eframe_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

                        cus_eframe_1.grid_columnconfigure(0,weight=1)
                        cus_eframe_1.grid_rowconfigure(0,weight=1)

                        
                        vertibar=Scrollbar(cus_eframe_1, orient=VERTICAL)
                        vertibar.grid(row=0,column=1,sticky='ns')
                        vertibar.config(command=cus_ecanvas_1.yview)

                        cus_ecanvas_1.bind("<Configure>", ecus_responsive_widgets2)
                        cus_ecanvas_1.config(yscrollcommand=vertibar.set)
                        cus_ecanvas_1.grid(row=0,column=0,sticky='nsew')

                        c_editid = cus_tree.item(cus_tree.focus())["values"][4]
                        print(c_editid)
                        c_editid_1 = cus_tree.item(cus_tree.focus())["values"][5]
                        print(c_editid_1)

                        sql = "select * from app1_company where id_id=%s"
                        val = (pr_dtl[0],)
                        fbcursor.execute(sql, val,)
                        cmp_dtl=fbcursor.fetchone()
                        print(cmp_dtl)

                        sql = 'select * from app1_customer where panno = %s and email = %s and cid_id = %s'
                        val =  (c_editid,c_editid_1,cmp_dtl[0],)
                        fbcursor.execute(sql,val)
                        edit_cus = fbcursor.fetchone()
    

                        def sales_edit_new_cus():
                            title = comb_ecus_1.get()
                            firstname = entry_ecus_1.get()
                            lastname = entry_ecus_2.get()
                            company = entry_ecus_3.get()
                            location = ecus_4.get()
                            gsttype = comb_ecus_2.get()
                            gstin = entry_ecus_5.get()
                            panno = entry_ecus_6.get()
                            email = entry_ecus_7.get()
                            website = entry_ecus_8.get()
                            mobile = entry_ecus_9.get()
                            street = entry_ecus_10.get()
                            city = entry_ecus_12.get()
                            state = entry_ecus_13.get()
                            pincode = entry_ecus_p12.get()
                            country = entry_ecus_c13.get()
                            shipstreet = entry_ecus_11.get()
                            shipcity = entry_ecus_14.get()
                            shipstate = entry_ecus_15.get()
                            shippincode = entry_ecus_pin14.get()
                            shipcountry = entry_ecus_co15.get()

                            usre_sql = "SELECT id FROM auth_user WHERE username=%s"
                            usre_val = (nm_ent.get(),)
                            fbcursor.execute(usre_sql,usre_val)
                            usre_data = fbcursor.fetchone()

                            cmpne_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                            cmpne_val = (usre_data[0],)
                            fbcursor.execute(cmpne_sql,cmpne_val)
                            cmpne_data = fbcursor.fetchone()
                            cid = cmpne_data[0]

                            if echk_str_1.get() == True:

                                cus_sql = "UPDATE app1_customer set title=%s,firstname=%s,lastname=%s,company=%s,location=%s,gsttype=%s,gstin=%s,panno=%s,email=%s,website=%s,mobile=%s,street=%s,city=%s,state=%s,pincode=%s,country=%s,shipstreet=%s,shipcity=%s,shipstate=%s,shippincode=%s,shipcountry=%s,cid_id=%s where panno=%s and email = %s"
                                cus_val=(title,firstname,lastname,company,location,gsttype,gstin,panno,email,website,mobile,street,city,state,pincode,country,shipstreet,shipcity,shipstate,shippincode,shipcountry,cid,c_editid,c_editid_1)
                                fbcursor.execute(cus_sql,cus_val)
                                finsysdb.commit()

                                #----------Refresh Insert Tree--------#

                                for record in cus_tree.get_children():
                                        cus_tree.delete(record)

                                sql_pr_1="select * from auth_user where username=%s"
                                sql_pr1_val=(nm_ent.get(),)
                                fbcursor.execute(sql_pr_1,sql_pr1_val,)
                                pr_dtl_1=fbcursor.fetchone()

                                sql_2 = "select * from app1_company where id_id=%s"
                                val_2 = (pr_dtl_1[0],)
                                fbcursor.execute(sql_2, val_2,)
                                cmp_dtl_2=fbcursor.fetchone()

                                c_sql_2 = "SELECT * FROM app1_customer where cid_id=%s"
                                c_val_2 = (cmp_dtl_2[0],)
                                fbcursor.execute(c_sql_2,c_val_2,)
                                c_data_2 = fbcursor.fetchall()

                                count1 = 0
                                for i in c_data_2:
                                    if True:
                                        cus_tree.insert(parent='',index='end',iid=i,text='',values=('',i[2]+" "+i[3],i[6],i[7],i[8],i[9],i[11])) 
                                    else:
                                        pass
                                count1 += 1

                                cus_eframe_1.destroy()
                                cus_frame.grid(row=0,column=0,sticky='nsew')

                            else:
                                pass


                        cus_ecanvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

                        label_1 = Label(cus_ecanvas_1,width=15,height=1,text="EDIT CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
                        window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

                        cus_ecanvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

                        cus_ecanvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))

                        label_1 = Label(cus_ecanvas_1,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
                        window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))

                        cus_ecanvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))

                        label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel3"))

                        comb_ecus_1 = ttk.Combobox(cus_ecanvas_1, font=('arial 10'))
                        comb_ecus_1['values'] = ("Mr","Mrs","Miss","Ms",)
                        comb_ecus_1.current(0)
                        window_comb_ecus_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_ecus_1, tags=("accombo1"))
                        comb_ecus_1.delete(0,'end')
                        comb_ecus_1.insert(0, edit_cus[1])

                        label_2 = Label(cus_ecanvas_1,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel4"))

                        entry_ecus_1=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_1, tags=("acentry1"))
                        entry_ecus_1.delete(0,'end')
                        entry_ecus_1.insert(0, edit_cus[2])

                        label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel5"))

                        entry_ecus_2=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_2, tags=("acentry2"))
                        entry_ecus_2.delete(0,'end')
                        entry_ecus_2.insert(0, edit_cus[3])

                        label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel6"))

                        entry_ecus_3=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_3 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_3, tags=("acentry3"))
                        entry_ecus_3.delete(0,'end')
                        entry_ecus_3.insert(0, edit_cus[4])


                        label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel7"))

                        ecus_4=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_ecus_4 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=ecus_4, tags=("acentry4"))
                        ecus_4.delete(0,'end')
                        ecus_4.insert(0, edit_cus[5])


                        label_2 = Label(cus_ecanvas_1,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel8"))

                        comb_ecus_2 = ttk.Combobox(cus_ecanvas_1, font=('arial 10'))
                        comb_ecus_2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
                        comb_ecus_2.current(0)
                        window_comb_ecus_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_ecus_2, tags=("accombo2"))
                        comb_ecus_2.delete(0,'end')
                        comb_ecus_2.insert(0, edit_cus[6])

                        label_2 = Label(cus_ecanvas_1,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel9"))
                        

                        entry_ecus_5=Entry(cus_ecanvas_1,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'))
                        window_entry_ecus_5 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_5, tags=("acentry5"))
                        entry_ecus_5.delete(0,'end')
                        entry_ecus_5.insert(0, edit_cus[7])

                        label_2 = Label(cus_ecanvas_1,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel10"))

                        entry_ecus_6=Entry(cus_ecanvas_1,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'))
                        window_entry_ecus_6 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_6, tags=("acentry6"))
                        entry_ecus_6.delete(0,'end')
                        entry_ecus_6.insert(0, edit_cus[8])

                        label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel11"))

                        entry_ecus_7=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_7 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_7, tags=("acentry7"))
                        entry_ecus_7.delete(0,'end')
                        entry_ecus_7.insert(0, edit_cus[9])


                        label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel12"))

                        entry_ecus_8=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_8 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_8, tags=("acentry8"))
                        entry_ecus_8.delete(0,'end')
                        entry_ecus_8.insert(0, edit_cus[10])

                        label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel13"))
                        

                        entry_ecus_9=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_9 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_9, tags=("acentry9"))
                        entry_ecus_9.delete(0,'end')
                        entry_ecus_9.insert(0, edit_cus[11])

                        label_1 = Label(cus_ecanvas_1,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
                        window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel14"))

                        label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel16"))

                        entry_ecus_10=Entry(cus_ecanvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_10 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_ecus_10, tags=("acentry10"))
                        entry_ecus_10.delete(0,'end')
                        entry_ecus_10.insert(0, edit_cus[12])


                        label_1 = Label(cus_ecanvas_1,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
                        window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel15"))

                        echk_str = StringVar()
                        echkbtn1 = Checkbutton(cus_ecanvas_1, text = "Same As Billing Address", variable = echk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
                        echkbtn1.select()
                        window_echkbtn_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=echkbtn1, tags=("accheck1"))

                        label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel17"))

                        entry_ecus_11=Entry(cus_ecanvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_11 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_ecus_11, tags=("acentry11"))
                        entry_ecus_11.delete(0,'end')
                        entry_ecus_11.insert(0, edit_cus[17])

                        label_2 = Label(cus_ecanvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel18"))

                        entry_ecus_12=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_12 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_12, tags=("acentry12"))
                        entry_ecus_12.delete(0,'end')
                        entry_ecus_12.insert(0, edit_cus[13])
                        
                        label_2 = Label(cus_ecanvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel19"))

                        entry_ecus_13=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_13 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_13, tags=("acentry13"))
                        entry_ecus_13.delete(0,'end')
                        entry_ecus_13.insert(0, edit_cus[14])

                        label_2 = Label(cus_ecanvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel20"))

                        entry_ecus_14=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_14 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_14, tags=("acentry14"))
                        entry_ecus_14.delete(0,'end')
                        entry_ecus_14.insert(0, edit_cus[18])

                        label_2 = Label(cus_ecanvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel21"))

                        entry_ecus_15=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_15 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_15, tags=("acentry15"))
                        entry_ecus_15.delete(0,'end')
                        entry_ecus_15.insert(0, edit_cus[19])

                        label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel22"))

                        entry_ecus_p12=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_p12 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_p12, tags=("acentry16"))
                        entry_ecus_p12.delete(0,'end')
                        entry_ecus_p12.insert(0, edit_cus[15])
                        
                        label_2 = Label(cus_ecanvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel23"))

                        entry_ecus_c13=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_c13 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_c13, tags=("acentry17"))
                        entry_ecus_c13.delete(0,'end')
                        entry_ecus_c13.insert(0, edit_cus[16])

                        label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel24"))

                        entry_ecus_pin14=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_pin14 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_pin14, tags=("acentry18"))
                        entry_ecus_pin14.delete(0,'end')
                        entry_ecus_pin14.insert(0, edit_cus[20])

                        label_2 = Label(cus_ecanvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel25"))

                        entry_ecus_co15=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ecus_co15 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_co15, tags=("acentry19"))
                        entry_ecus_co15.delete(0,'end')
                        entry_ecus_co15.insert(0, edit_cus[21])

                        echk_str_1 = BooleanVar()
                        echkbtn2 = Checkbutton(cus_ecanvas_1, text = "Agree to terms and conditions", variable = echk_str_1, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
                        echkbtn2.select()
                        window_echkbtn_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=echkbtn2,tags=("accheck2"))

                        def ec_back_1_():
                            cus_eframe_1.grid_forget()
                            cus_frame.grid(row=0,column=0,sticky='nsew')

                        ec_bck_btn1=Button(cus_ecanvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=ec_back_1_)
                        window_ec_bck_btn1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=ec_bck_btn1,tags=('acbutton3'))

                        ecus_btn2=Button(cus_ecanvas_1,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12',command=sales_edit_new_cus)
                        window_ecus_btn2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=ecus_btn2,tags=("acbutton1"))
                    else:  
                        pass

                # ecbtn1=Button(cus_canvas,text='Edit', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=lambda:edit_customer())
                # window_ecbtn1 = cus_canvas.create_window(0, 0, anchor="nw", window=ecbtn1, tags=("cbutton2"))

                cus_comb_1 = ttk.Combobox(cus_canvas,font=('arial 10'))
                cus_comb_1['values'] = ("Actions","Edit","Delete")
                cus_comb_1.current(0)
                window_cus_comb_1 = cus_canvas.create_window(0, 0, anchor="nw", width=110,height=30,window=cus_comb_1,tags=('cbutton3'))
                cus_comb_1.bind("<<ComboboxSelected>>",edit_customer)

                # dcbtn1=Button(cus_canvas,text='Delete', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                # window_dcbtn1 = cus_canvas.create_window(0, 0, anchor="nw", window=dcbtn1, tags=("cbutton3"))

                #---------------------------Product & Services------------------------#
                tab3_4.grid_columnconfigure(0,weight=1)
                tab3_4.grid_rowconfigure(0,weight=1)

                pro_frame = Frame(tab3_4)
                pro_frame.grid(row=0,column=0,sticky='nsew')

                def pro_responsive_widgets(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget

                    r1 = 25
                    x1 = dwidth/63
                    x2 = dwidth/1.021
                    y1 = dheight/14 
                    y2 = dheight/3.505

                    dcanvas.coords("ppoly1",x1 + r1,y1,
                    x1 + r1,y1,
                    x2 - r1,y1,
                    x2 - r1,y1,     
                    x2,y1,     
                    #--------------------
                    x2,y1 + r1,     
                    x2,y1 + r1,     
                    x2,y2 - r1,     
                    x2,y2 - r1,     
                    x2,y2,
                    #--------------------
                    x2 - r1,y2,     
                    x2 - r1,y2,     
                    x1 + r1,y2,
                    x1 + r1,y2,
                    x1,y2,
                    #--------------------
                    x1,y2 - r1,
                    x1,y2 - r1,
                    x1,y1 + r1,
                    x1,y1 + r1,
                    x1,y1,
                    )

                    dcanvas.coords("phline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
                    dcanvas.coords("plabel1",dwidth/2.75,dheight/8.00)

                    r2 = 25
                    x11 = dwidth/63
                    x21 = dwidth/1.021
                    y11 = dheight/2.8
                    y21 = dheight/0.750


                    dcanvas.coords("ppoly2",x11 + r2,y11,
                    x11 + r2,y11,
                    x21 - r2,y11,
                    x21 - r2,y11,     
                    x21,y11,     
                    #--------------------
                    x21,y11 + r2,     
                    x21,y11 + r2,     
                    x21,y21 - r2,     
                    x21,y21 - r2,     
                    x21,y21,
                    #--------------------
                    x21 - r2,y21,     
                    x21 - r2,y21,     
                    x11 + r2,y21,
                    x11 + r2,y21,
                    x11,y21,
                    #--------------------
                    x11,y21 - r2,
                    x11,y21 - r2,
                    x11,y11 + r2,
                    x11,y11 + r2,
                    x11,y11,
                    )



                    dcanvas.coords("pimage1",dwidth/5.29,dheight/2.15)
                    dcanvas.coords("pimage2",dwidth/2.05,dheight/2.15)

                    dcanvas.coords("plabel2",dwidth/5.60,dheight/1.60)
                    dcanvas.coords("plabel3",dwidth/2.09,dheight/1.60)
                    
                    dcanvas.coords("pcombo1",dwidth/1.18,dheight/1.10)

                    dcanvas.coords("pbutton1",dwidth/2.2,dheight/1.4)
                    dcanvas.coords("pbutton2",dwidth/1.645,dheight/1.4)
                    dcanvas.coords("pbutton3",dwidth/1.315,dheight/1.35)

                    dcanvas.coords("ptree1",dwidth/12,dheight/1.21)

                pro_canvas=Canvas(pro_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

                pro_frame.grid_rowconfigure(0,weight=1)
                pro_frame.grid_columnconfigure(0,weight=1)

                vertibar=Scrollbar(pro_frame, orient=VERTICAL)
                vertibar.grid(row=0,column=1,sticky='ns')
                vertibar.config(command=pro_canvas.yview)
                
                pro_canvas.bind("<Configure>", pro_responsive_widgets)
                pro_canvas.config(yscrollcommand=vertibar.set)
                pro_canvas.grid(row=0,column=0,sticky='nsew')

                
                pro_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ppoly1"))
                
                label_1 = Label(pro_canvas,width=23,height=1,text="PRODUCT AND SERVICES", font=('arial 25'),background="#1b3857",fg="white") 
                window_label_1 = pro_canvas.create_window(480, 85, anchor="nw", window=label_1, tags=("plabel1"))

                pro_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("phline"))

                pro_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ppoly2"))


                image_1 = Image.open("images/lowstock.png")
                resize_image = image_1.resize((90,90))
                image_1 = ImageTk.PhotoImage(resize_image)
                btlogo = Label(pro_canvas, width=90, height=90, background="#1b3857", image = image_1) 
                window_image = pro_canvas.create_window(0, 0, anchor="nw", window=btlogo,tags=('pimage1'))
                btlogo.photo = image_1

                label_2 = Label(pro_canvas,width=14,height=1,text="LOW STOCK : ", font=('arial 18'),background="#1b3857",fg="white") 
                window_label_2 = pro_canvas.create_window(0, 0, anchor="nw", window=label_2,tags=('plabel2'))

                image_2 = Image.open("images/outofstock.png")
                resize_image_1 = image_2.resize((90,90))
                image_2 = ImageTk.PhotoImage(resize_image_1)
                btlogo_1 = Label(pro_canvas, width=90, height=90, background="#1b3857", image = image_2) 
                window_image_1 = pro_canvas.create_window(0, 0, anchor="nw", window=btlogo_1,tags=('pimage2'))
                btlogo_1.photo = image_2

                label_2 = Label(pro_canvas,width=15,height=1,text="OUT OF STOCK : ", font=('arial 18'),background="#1b3857",fg="white") 
                window_label_2 = pro_canvas.create_window(0, 0, anchor="nw", window=label_2,tags=('plabel3'))


                def add_product():
                    pro_frame.grid_forget()
                    pro_frame_1 = Frame(tab3_4)
                    pro_frame_1.grid(row=0,column=0,sticky='nsew')

                    def pro_responsive_widgets_1(event):
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget
                        
                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/14 
                        y2 = dheight/3.505

                        dcanvas.coords("appoly1",x1 + r1,y1,
                        x1 + r1,y1,
                        x2 - r1,y1,
                        x2 - r1,y1,     
                        x2,y1,     
                        #--------------------
                        x2,y1 + r1,     
                        x2,y1 + r1,     
                        x2,y2 - r1,     
                        x2,y2 - r1,     
                        x2,y2,
                        #--------------------
                        x2 - r1,y2,     
                        x2 - r1,y2,     
                        x1 + r1,y2,
                        x1 + r1,y2,
                        x1,y2,
                        #--------------------
                        x1,y2 - r1,
                        x1,y2 - r1,
                        x1,y1 + r1,
                        x1,y1 + r1,
                        x1,y1,
                        )

                        dcanvas.coords("aplabel1",dwidth/3,dheight/8.24)
                        dcanvas.coords("aphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                        r2 = 25
                        x11 = dwidth/63
                        x21 = dwidth/1.021
                        y11 = dheight/2.8
                        y21 = dheight/0.60


                        dcanvas.coords("appoly2",x11 + r2,y11,
                        x11 + r2,y11,
                        x21 - r2,y11,
                        x21 - r2,y11,     
                        x21,y11,     
                        #--------------------
                        x21,y11 + r2,     
                        x21,y11 + r2,     
                        x21,y21 - r2,     
                        x21,y21 - r2,     
                        x21,y21,
                        #--------------------
                        x21 - r2,y21,     
                        x21 - r2,y21,     
                        x11 + r2,y21,
                        x11 + r2,y21,
                        x11,y21,
                        #--------------------
                        x11,y21 - r2,
                        x11,y21 - r2,
                        x11,y11 + r2,
                        x11,y11 + r2,
                        x11,y11,
                        )

                        r2 = 25
                        x11 = dwidth/7
                        x21 = dwidth/2.07
                        y11 = dheight/2.0
                        y21 = dheight/1.1


                        dcanvas.coords("appoly3",x11 + r2,y11,
                        x11 + r2,y11,
                        x21 - r2,y11,
                        x21 - r2,y11,     
                        x21,y11,     
                        #--------------------
                        x21,y11 + r2,     
                        x21,y11 + r2,     
                        x21,y21 - r2,     
                        x21,y21 - r2,     
                        x21,y21,
                        #--------------------
                        x21 - r2,y21,     
                        x21 - r2,y21,     
                        x11 + r2,y21,
                        x11 + r2,y21,
                        x11,y21,
                        #--------------------
                        x11,y21 - r2,
                        x11,y21 - r2,
                        x11,y11 + r2,
                        x11,y11 + r2,
                        x11,y11,
                        )

                        dcanvas.coords("apimage1",dwidth/4.2,dheight/1.73)
                        
                        dcanvas.coords("aplabel2",dwidth/3.9,dheight/1.75)
                        dcanvas.coords("aplabel3",dwidth/6.30,dheight/1.54)
                        dcanvas.coords("apbutton1",dwidth/4.1,dheight/1.30)

                        r2 = 25
                        x11 = dwidth/1.93
                        x21 = dwidth/1.15
                        y11 = dheight/2.0
                        y21 = dheight/1.1


                        dcanvas.coords("appoly4",x11 + r2,y11,
                        x11 + r2,y11,
                        x21 - r2,y11,
                        x21 - r2,y11,     
                        x21,y11,     
                        #--------------------
                        x21,y11 + r2,     
                        x21,y11 + r2,     
                        x21,y21 - r2,     
                        x21,y21 - r2,     
                        x21,y21,
                        #--------------------
                        x21 - r2,y21,     
                        x21 - r2,y21,     
                        x11 + r2,y21,
                        x11 + r2,y21,
                        x11,y21,
                        #--------------------
                        x11,y21 - r2,
                        x11,y21 - r2,
                        x11,y11 + r2,
                        x11,y11 + r2,
                        x11,y11,
                        )

                        dcanvas.coords("apimage2",dwidth/1.61,dheight/1.73)
                        
                        dcanvas.coords("aplabel4",dwidth/1.58,dheight/1.75)
                        dcanvas.coords("aplabel5",dwidth/1.85,dheight/1.54)
                        dcanvas.coords("apbutton2",dwidth/1.6,dheight/1.30)

                        r2 = 25
                        x11 = dwidth/7
                        x21 = dwidth/2.07
                        y11 = dheight/1.0
                        y21 = dheight/0.719


                        dcanvas.coords("appoly5",x11 + r2,y11,
                        x11 + r2,y11,
                        x21 - r2,y11,
                        x21 - r2,y11,     
                        x21,y11,     
                        #--------------------
                        x21,y11 + r2,     
                        x21,y11 + r2,     
                        x21,y21 - r2,     
                        x21,y21 - r2,     
                        x21,y21,
                        #--------------------
                        x21 - r2,y21,     
                        x21 - r2,y21,     
                        x11 + r2,y21,
                        x11 + r2,y21,
                        x11,y21,
                        #--------------------
                        x11,y21 - r2,
                        x11,y21 - r2,
                        x11,y11 + r2,
                        x11,y11 + r2,
                        x11,y11,
                        )

                        
                        dcanvas.coords("apimage3",dwidth/4.2,dheight/0.93)
                        
                        dcanvas.coords("aplabel6",dwidth/3.9,dheight/0.95)
                        dcanvas.coords("aplabel7",dwidth/6.30,dheight/0.88)
                        dcanvas.coords("apbutton3",dwidth/4.1,dheight/0.80)

                        r2 = 25
                        x11 = dwidth/1.93
                        x21 = dwidth/1.15
                        y11 = dheight/1.0
                        y21 = dheight/0.719


                        dcanvas.coords("appoly6",x11 + r2,y11,
                        x11 + r2,y11,
                        x21 - r2,y11,
                        x21 - r2,y11,     
                        x21,y11,     
                        #--------------------
                        x21,y11 + r2,     
                        x21,y11 + r2,     
                        x21,y21 - r2,     
                        x21,y21 - r2,     
                        x21,y21,
                        #--------------------
                        x21 - r2,y21,     
                        x21 - r2,y21,     
                        x11 + r2,y21,
                        x11 + r2,y21,
                        x11,y21,
                        #--------------------
                        x11,y21 - r2,
                        x11,y21 - r2,
                        x11,y11 + r2,
                        x11,y11 + r2,
                        x11,y11,
                        )

                        dcanvas.coords("apimage4",dwidth/1.61,dheight/0.93)

                        dcanvas.coords("aplabel8",dwidth/1.58,dheight/0.95)
                        dcanvas.coords("aplabel9",dwidth/1.85,dheight/0.88)
                        dcanvas.coords("apbutton4",dwidth/1.6,dheight/0.80)
                        dcanvas.coords("apbutton5",dwidth/23,dheight/3.415)


                    p_canvas_1=Canvas(pro_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1000))

                    pro_frame_1.grid_columnconfigure(0,weight=1)
                    pro_frame_1.grid_rowconfigure(0,weight=1)
                    
                    vertibar=Scrollbar(pro_frame_1, orient=VERTICAL)
                    vertibar.grid(row=0,column=1,sticky='ns')
                    vertibar.config(command=p_canvas_1.yview)

                    p_canvas_1.bind("<Configure>", pro_responsive_widgets_1)
                    p_canvas_1.config(yscrollcommand=vertibar.set)
                    p_canvas_1.grid(row=0,column=0,sticky='nsew')
                    
                    
                    p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("appoly1"))

                    label_1 = Label(p_canvas_1,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                    window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aplabel1"))

                    p_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("aphline"))

                    p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("appoly2"))

                    p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly3"))

                    def invcall(event):
                        p_canvas_1.itemconfig('apimage1',state='hidden')
                        p_canvas_1.itemconfig('aplabel2',state='normal')
                        p_canvas_1.itemconfig('aplabel3',state='normal')
                        p_canvas_1.itemconfig('apbutton1',state='normal')

                    image_i1 = Image.open("images/inventory.png")
                    resize_image = image_i1.resize((200,150))
                    image_i1 = ImageTk.PhotoImage(resize_image)
                    btlogoi = Label(p_canvas_1, width=200, height=150, background="#1b3857", image = image_i1) 
                    window_image = p_canvas_1.create_window(0, 0, anchor="nw", window=btlogoi,tags=('apimage1'))
                    btlogoi.photo = image_i1
                    btlogoi.bind("<Button-1>",invcall)

                    label_1 = Label(p_canvas_1,width=10,height=1,text="Inventory", font=('arial 20'),background="#2f516f",fg="white") 
                    window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel2'),state=HIDDEN)

                    label_1 = Label(p_canvas_1,width=45,height=2,text="Inventory is the goods available for sale and raw materials \nused to produce goods available for sale.", font=('arial 12'),background="#2f516f",fg="white") 
                    window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel3'),state=HIDDEN)

                    def inv_add_item():
                        pro_frame_1.grid_forget()
                        pro_frame_2 = Frame(tab3_4)
                        pro_frame_2.grid(row=0,column=0,sticky='nsew')

                        def pro_responsive_widgets_2(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                        
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("ippoly1",x1 + r1,y1,
                            x1 + r1,y1,
                            x2 - r1,y1,
                            x2 - r1,y1,     
                            x2,y1,     
                            #--------------------
                            x2,y1 + r1,     
                            x2,y1 + r1,     
                            x2,y2 - r1,     
                            x2,y2 - r1,     
                            x2,y2,
                            #--------------------
                            x2 - r1,y2,     
                            x2 - r1,y2,     
                            x1 + r1,y2,
                            x1 + r1,y2,
                            x1,y2,
                            #--------------------
                            x1,y2 - r1,
                            x1,y2 - r1,
                            x1,y1 + r1,
                            x1,y1 + r1,
                            x1,y1,
                            )

                            dcanvas.coords("iplabel1",dwidth/3,dheight/8.24)
                            dcanvas.coords("iphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/2.8
                            y21 = dheight/0.29


                            dcanvas.coords("ippoly2",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            r2 = 25
                            x11 = dwidth/24
                            x21 = dwidth/1.050
                            y11 = dheight/2.1
                            y21 = dheight/1.35


                            dcanvas.coords("ippoly3",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            dcanvas.coords("iplabel2",dwidth/2.5,dheight/1.77)
                            dcanvas.coords("ipbutton1",dwidth/1.8,dheight/1.77)

                            dcanvas.coords("iplabel3",dwidth/23.2,dheight/1.23)
                            dcanvas.coords("iplabel4",dwidth/23.3,dheight/1.02)
                            dcanvas.coords("iplabel5",dwidth/1.9,dheight/1.02)
                            dcanvas.coords("iplabel6",dwidth/1.9,dheight/0.92)
                            dcanvas.coords("iplabel7",dwidth/27,dheight/0.865)
                            dcanvas.coords("iplabel8",dwidth/1.915,dheight/0.865)
                            dcanvas.coords("iplabel9",dwidth/50,dheight/0.76)
                            dcanvas.coords("iplabel10",dwidth/2.95,dheight/0.76)
                            dcanvas.coords("iplabel11",dwidth/1.54,dheight/0.76)
                            dcanvas.coords("iplabel12",dwidth/38,dheight/0.675)
                            dcanvas.coords("iplabel13",dwidth/26.8,dheight/0.606)
                            dcanvas.coords("iplabel14",dwidth/28.3,dheight/0.538)
                            dcanvas.coords("iplabel15",dwidth/1.9,dheight/0.538)
                            dcanvas.coords("iplabel16",dwidth/28.4,dheight/0.485)
                            dcanvas.coords("iplabel17",dwidth/29.3,dheight/0.438)
                            dcanvas.coords("iplabel18",dwidth/28,dheight/0.401)
                            dcanvas.coords("iplabel19",dwidth/1.91,dheight/0.401)
                            dcanvas.coords("iplabel20",dwidth/28,dheight/0.37)
                            dcanvas.coords("iplabel21",dwidth/26,dheight/0.35)
                            dcanvas.coords("iplabel22",dwidth/1.9,dheight/0.35)

                            dcanvas.coords("ipentry1",dwidth/23.2,dheight/1.165)
                            dcanvas.coords("ipentry2",dwidth/23.2,dheight/0.975)
                            dcanvas.coords("ipentry3",dwidth/1.9,dheight/0.975)
                            dcanvas.coords("ipentry4",dwidth/1.9,dheight/0.83)
                            dcanvas.coords("ipentry5",dwidth/23.2,dheight/0.73)
                            dcanvas.coords("ipentry6",dwidth/1.52,dheight/0.73)
                            dcanvas.coords("ipentry7",dwidth/23.2,dheight/0.59)
                            dcanvas.coords("ipentry8",dwidth/23.2,dheight/0.525)
                            dcanvas.coords("ipentry9",dwidth/23.2,dheight/0.43)
                            dcanvas.coords("ipentry10",dwidth/23.2,dheight/0.394)
                            dcanvas.coords("ipentry11",dwidth/23.2,dheight/0.344)

                            dcanvas.coords("ipcombo1",dwidth/23.2,dheight/0.83)
                            dcanvas.coords("ipcombo2",dwidth/23.2,dheight/0.654)
                            dcanvas.coords("ipcombo3",dwidth/1.9,dheight/0.525)
                            dcanvas.coords("ipcombo4",dwidth/23.2,dheight/0.474)
                            dcanvas.coords("ipcombo5",dwidth/1.89,dheight/0.394)
                            dcanvas.coords("ipcombo6",dwidth/23.2,dheight/0.364)
                            dcanvas.coords("ipcombo7",dwidth/1.89,dheight/0.344)

                            dcanvas.coords("ipcbutton1",dwidth/23.2,dheight/0.51)
                            dcanvas.coords("ipcbutton2",dwidth/23.2,dheight/0.385)

                            dcanvas.coords("ipbutton2",dwidth/2.45,dheight/0.654)
                            dcanvas.coords("ipbutton3",dwidth/2.45,dheight/0.474)
                            dcanvas.coords("ipbutton4",dwidth/2.45,dheight/0.364)
                            dcanvas.coords("ipbutton5",dwidth/2.38,dheight/0.325)

                            dcanvas.coords("iphline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)

                            try:
                                dcanvas.coords("ipdate1",dwidth/2.9,dheight/0.73)
                            except:
                                pass


                        p_canvas_2=Canvas(pro_frame_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                        pro_frame_2.grid_columnconfigure(0,weight=1)
                        pro_frame_2.grid_rowconfigure(0,weight=1)
                    
                        vertibar=Scrollbar(pro_frame_2, orient=VERTICAL)
                        vertibar.grid(row=0,column=1,sticky='ns')
                        vertibar.config(command=p_canvas_2.yview)

                        p_canvas_2.bind("<Configure>", pro_responsive_widgets_2)
                        p_canvas_2.config(yscrollcommand=vertibar.set)
                        p_canvas_2.grid(row=0,column=0,sticky='nsew')

                        def add_new_pro_inv():
                            name = entry_inv_item_1.get()
                            sku = entry_inv_item_2.get()
                            hsn = entry_inv_item_h2.get()
                            unit = comb_inv_item_u1.get()
                            category = entry_inv_item_3.get()
                            initialqty = entry_inv_item_4.get()
                            date = entry_inv_item_aod5.get_date()
                            stockalrt = entry_inv_item_6.get()
                            invacnt = comb_inv_item_i2.get()
                            description = entry_inv_item_7.get('1.0', 'end-1c')
                            salesprice = entry_inv_item_8.get()
                            incomeacnt = comb_inv_item_in4.get()
                            tax = comb_inv_item_t3.get()
                            purchaseinfo = entry_inv_item_9.get('1.0', 'end-1c')
                            cost = entry_inv_item_10.get()
                            expacnt = comb_inv_item_ex6.get()
                            purtax = comb_inv_item_pu5.get()
                            revcharge = entry_inv_item_11.get()
                            presupplier = comb_inv_item_pr7.get()

                            usrp_sql = "SELECT id FROM auth_user WHERE username=%s"
                            usrp_val = (nm_ent.get(),)
                            fbcursor.execute(usrp_sql,usrp_val)
                            usrp_data = fbcursor.fetchone()

                            cmpp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                            cmpp_val = (usrp_data[0],)
                            fbcursor.execute(cmpp_sql,cmpp_val)
                            cmpp_data = fbcursor.fetchone()
                            cid = cmpp_data[0]
                            
                            i_p_sql = "INSERT INTO app1_inventory(name,sku,hsn,unit,category,initialqty,date,stockalrt,invacnt,description,salesprice,incomeacnt,tax,purchaseinfo,cost,expacnt,purtax,revcharge,presupplier,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            i_p_val = (name,sku,hsn,unit,category,initialqty,date,stockalrt,invacnt,description,salesprice,incomeacnt,tax,purchaseinfo,cost,expacnt,purtax,revcharge,presupplier,cid)
                            fbcursor.execute(i_p_sql,i_p_val)
                            finsysdb.commit()

                            #_________Refresh insert tree________#
     
                            for record in pro_tree.get_children():
                                pro_tree.delete(record)


                            sql_p="select * from auth_user where username=%s"
                            sql_p_val=(nm_ent.get(),)
                            fbcursor.execute(sql_p,sql_p_val,)
                            pr_dt=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pr_dt[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dt=fbcursor.fetchone()

                            p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                            p_val_1 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_1,p_val_1,)
                            p_data_1 = fbcursor.fetchall()
                            
                            count0 = 0
                            for i in p_data_1:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                else:
                                    pass
                            count0 += 1

                            p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                            p_val_2 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_2,p_val_2,)
                            p_data_2 = fbcursor.fetchall()

                            count1 = 0
                            for i in p_data_2:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                else:
                                    pass
                            count1 += 1

                            p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                            p_val_3 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_3,p_val_3,)
                            p_data_3 = fbcursor.fetchall()
                            

                            count2 = 0
                            for i in p_data_3:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                else:
                                    pass
                            count2 += 1

                            p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                            p_val_4 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_4,p_val_4,)
                            p_data_4 = fbcursor.fetchall()
                            

                            count3 = 0
                            for i in p_data_4:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                else:
                                    pass
                            count3 += 1

                            pro_frame_2.destroy()
                            pro_frame.grid(row=0,column=0,sticky='nsew')



                        p_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('ippoly1'))

                        label_1 = Label(p_canvas_2,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel1'))

                        p_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iphline'))

                        p_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('ippoly2'))

                        p_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('ippoly3'))

                        label_1 = Label(p_canvas_2,width=10,height=2,text="INVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel2'))

                        btn_item_1=Button(p_canvas_2,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
                        window_btn_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=btn_item_1, tags=('ipbutton1'))

                        label_1 = Label(p_canvas_2,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel3'))

                        entry_inv_item_1=Entry(p_canvas_2,width=200,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_entry_inv_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_1, tags=('ipentry1'))

                        label_1 = Label(p_canvas_2,width=4,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel4'))

                        def p_sku_1(event):
                            if entry_inv_item_2.get()=="N41554":
                                entry_inv_item_2.delete(0,END)
                            else:
                                pass
                        
                        entry_inv_item_2=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_entry_inv_item_2 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_2, tags=('ipentry2'))
                        entry_inv_item_2.insert(0,"N41554")
                        entry_inv_item_2.bind("<Button-1>",p_sku_1)


                        label_1 = Label(p_canvas_2,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel5'))

                        entry_inv_item_h2=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_entry_inv_item_h2 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_h2, tags=('ipentry3'))

                        #Define a callback function
                        def callback(url):
                            webbrowser.open_new_tab(url)

                        link_1 = Label(p_canvas_2,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
                        window_link_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=link_1, tags=('iplabel6'))
                        link_1.bind("<Button-1>", lambda e:
                        callback("https://gstcouncil.gov.in/sites/default/files/goods-rates-booklet-03July2017.pdf"))

                        label_1 = Label(p_canvas_2,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel7'))

                        comb_inv_item_u1 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                        comb_inv_item_u1['values'] = ("Choose...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards",)
                        comb_inv_item_u1.current(0)
                        window_comb_inv_item_u1 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_u1, tags=('ipcombo1'))

                        label_1 = Label(p_canvas_2,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel8'))

                        entry_inv_item_3=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_entry_inv_item_3 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_3,tags=('ipentry4'))

                        label_1 = Label(p_canvas_2,width=24,height=1,text="Initial quantity on hand", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel9'))

                        entry_inv_item_4=Entry(p_canvas_2,width=60,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_entry_inv_item_4 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_4,tags=('ipentry5'))

                        label_1 = Label(p_canvas_2,width=10,height=1,text="As of date", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel10'))
            
                        label_1 = Label(p_canvas_2,width=14,height=1,text="Low stock alert", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel11'))

                        entry_inv_item_6=Entry(p_canvas_2,width=60,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_entry_inv_item_6 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_6,tags=('ipentry6'))

                        label_1 = Label(p_canvas_2,width=22,height=1,text="Inventory asset account", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(35, 910, anchor="nw", window=label_1,tags=('iplabel12'))

                        comb_inv_item_i2 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                        comb_inv_item_i2['values'] = ("Inventory Asset",)
                        comb_inv_item_i2.current(0)
                        window_comb_inv_item_i2 = p_canvas_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_item_i2,tags=('ipcombo2'))

                        def inv_acc_create_1():
                            pro_frame_2.grid_forget()
                            pro_frame_2_1 = Frame(tab3_4)
                            pro_frame_2_1.grid(row=0,column=0,sticky='nsew')
                            def pro_responsive_widgets_2_1(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("iapoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("ialabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("iahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.52


                                dcanvas.coords("iapoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("iabutton3",dwidth/23,dheight/3.415)

                                dcanvas.coords("ialabel2",dwidth/23,dheight/1.91)
                                dcanvas.coords("ialabel3",dwidth/1.9,dheight/1.91)
                                dcanvas.coords("ialabel4",dwidth/23.3,dheight/1.41)
                                dcanvas.coords("ialabel5",dwidth/1.9,dheight/1.41)
                                dcanvas.coords("ialabel6",dwidth/1.9,dheight/0.95)

                                dcanvas.coords("iaentry1",dwidth/1.9,dheight/1.74)
                                dcanvas.coords("iaentry2",dwidth/1.9,dheight/1.32)

                                dcanvas.coords("iacombo1",dwidth/23,dheight/1.74)
                                dcanvas.coords("iacombo2",dwidth/23,dheight/1.32)
                                dcanvas.coords("iacombo3",dwidth/1.9,dheight/1.09)
                                dcanvas.coords("iacombo4",dwidth/1.9,dheight/0.91)

                                dcanvas.coords("iatext1",dwidth/23,dheight/1.15)
                                dcanvas.coords("iacheck1",dwidth/1.9,dheight/1.155)

                                dcanvas.coords("iabutton1",dwidth/2.3,dheight/0.73)

                            p_canvas_2_1=Canvas(pro_frame_2_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_2_1.grid_columnconfigure(0,weight=1)
                            pro_frame_2_1.grid_rowconfigure(0,weight=1)
                            
                            vertibar=Scrollbar(pro_frame_2_1, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_2_1.yview)

                            p_canvas_2_1.bind("<Configure>", pro_responsive_widgets_2_1)
                            p_canvas_2_1.config(yscrollcommand=vertibar.set)
                            p_canvas_2_1.grid(row=0,column=0,sticky='nsew')


                            p_canvas_2_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly1'))

                            label_1 = Label(p_canvas_2_1,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ialabel1'))

                            p_canvas_2_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iahline'))

                            p_canvas_2_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly2'))

                            label_1 = Label(p_canvas_2_1,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel2'))

                            comb_inv_1_1 = ttk.Combobox(p_canvas_2_1, font=('arial 10'))
                            comb_inv_1_1['values'] = ("Current Assets",)
                            comb_inv_1_1.current(0)
                            window_comb_inv_1_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_1_1,tags=('iacombo1'))

                            label_1 = Label(p_canvas_2_1,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel3'))

                            entry_inv_1_2=Entry(p_canvas_2_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_inv_1_2 = p_canvas_2_1.create_window(0, 0, anchor="nw", height=30,window=entry_inv_1_2,tags=('iaentry1'))

                            label_1 = Label(p_canvas_2_1,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel4'))

                            comb_inv_1_2 = ttk.Combobox(p_canvas_2_1, font=('arial 10'))
                            comb_inv_1_2['values'] = ("Inventory",)
                            comb_inv_1_2.current(0)
                            window_comb_inv_1_2 = p_canvas_2_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_1_2,tags=('iacombo2'))

                            label_1 = Label(p_canvas_2_1,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel5'))

                            entry_inv_1_4=Entry(p_canvas_2_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_inv_1_4 = p_canvas_2_1.create_window(0, 0, anchor="nw", height=30,window=entry_inv_1_4,tags=('iaentry2'))

                            inv_text_1 = Text(p_canvas_2_1,width=67, height=14, background='black',foreground='white')
                            inv_text_1.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                            window_inv_text_1 = p_canvas_2_1.create_window(0, 0, anchor="nw",window=inv_text_1,tags=('iatext1'))

                            def sub_check_1():
                                comb_inv_1_3.config(state=NORMAL if chk_str_inv_1_1.get() else DISABLED)
                                

                            chk_str_inv_1_1 = IntVar()
                            chkbtn_inv_1_1 = Checkbutton(p_canvas_2_1, text = "Is sub-account", variable = chk_str_inv_1_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=sub_check_1)
                            window_chkbtn_inv_1_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=chkbtn_inv_1_1,tags=('iacheck1'))

                            comb_inv_1_3 = ttk.Combobox(p_canvas_2_1, font=('arial 10'),state=DISABLED)
                            comb_inv_1_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                            window_comb_inv_1_3 = p_canvas_2_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_1_3,tags=('iacombo3'))

                            label_1 = Label(p_canvas_2_1,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel6'))

                            
                            comb_inv_1_4 = ttk.Combobox(p_canvas_2_1, font=('arial 10'))
                            comb_inv_1_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                            window_comb_inv_1_4 = p_canvas_2_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_1_4,tags=('iacombo4'))


                            inv_sub_btn_1_1=Button(p_canvas_2_1,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                            window_inv_sub_btn_1_1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=inv_sub_btn_1_1,tags=('iabutton1'))

                            def i_back_1_():
                                pro_frame_2_1.grid_forget()
                                pro_frame_2.grid(row=0,column=0,sticky='nsew')

                            bck_btn1=Button(p_canvas_2_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=i_back_1_)
                            window_bck_btn1 = p_canvas_2_1.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('iabutton3'))

                            

                        asset_btn=Button(p_canvas_2,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_acc_create_1)
                        window_asset_btn = p_canvas_2.create_window(0, 0, anchor="nw", window=asset_btn,tags=('ipbutton2'))

                        label_1 = Label(p_canvas_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel13'))

                        entry_inv_item_7=scrolledtext.ScrolledText(p_canvas_2,width=145,background='#2f516f',foreground="white")
                        window_entry_entry_inv_item_7 = p_canvas_2.create_window(0, 0, anchor="nw", height=60,window=entry_inv_item_7,tags=('ipentry7'))

                        label_1 = Label(p_canvas_2,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel14'))

                        def inv_tax_check():

                            if chk_str_inv_item.get() == True:
                                gst = 0.0
                                np = 0.0
                                gst = entry_inv_item_8.get()-[float(entry_inv_item_8.get())*(100/(100+28))]
                                np = entry_inv_item_8.get()-gst
                                print(np)
                            else:
                                pass
                        
                        entry_inv_item_8=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_entry_inv_item_8 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_8,tags=('ipentry8'))

                        chk_str_inv_item = BooleanVar()
                        chkbtn_inv_item_1 = Checkbutton(p_canvas_2, text = "Inclusive of tax", variable = chk_str_inv_item,  font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=inv_tax_check)
                        window_chkbtn_inv_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=chkbtn_inv_item_1,tags=('ipcbutton1'))

                        label_1 = Label(p_canvas_2,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel15'))

                        comb_inv_item_t3 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                        comb_inv_item_t3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                        comb_inv_item_t3.current(0)
                        window_comb_inv_item_t3 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_t3,tags=('ipcombo3'))

                        label_1 = Label(p_canvas_2,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel16'))

                        comb_inv_item_in4 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                        comb_inv_item_in4['values'] = ("Choose...","Billable Expense Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales of Product Income","Uncategorised Income",)
                        comb_inv_item_in4.current(0)
                        window_comb_inv_item_in4 = p_canvas_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_item_in4,tags=('ipcombo4'))

                        def inv_inc_acc_1():
                            pro_frame_2.grid_forget()
                            pro_frame_2_2 = Frame(tab3_4)
                            pro_frame_2_2.grid(row=0,column=0,sticky='nsew')

                            def pro_responsive_widgets_2_2(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("iapoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("ialabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("iahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.52


                                dcanvas.coords("iapoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("iabutton3",dwidth/23,dheight/3.415)

                                dcanvas.coords("ialabel2",dwidth/23,dheight/1.91)
                                dcanvas.coords("ialabel3",dwidth/1.9,dheight/1.91)
                                dcanvas.coords("ialabel4",dwidth/23.3,dheight/1.41)
                                dcanvas.coords("ialabel5",dwidth/1.9,dheight/1.41)
                                dcanvas.coords("ialabel6",dwidth/1.9,dheight/0.95)

                                dcanvas.coords("iaentry1",dwidth/1.9,dheight/1.74)
                                dcanvas.coords("iaentry2",dwidth/1.9,dheight/1.32)

                                dcanvas.coords("iacombo1",dwidth/23,dheight/1.74)
                                dcanvas.coords("iacombo2",dwidth/23,dheight/1.32)
                                dcanvas.coords("iacombo3",dwidth/1.9,dheight/1.09)
                                dcanvas.coords("iacombo4",dwidth/1.9,dheight/0.91)

                                dcanvas.coords("iatext1",dwidth/23,dheight/1.15)
                                dcanvas.coords("iacheck1",dwidth/1.9,dheight/1.155)

                                dcanvas.coords("iabutton1",dwidth/2.3,dheight/0.73)

                            p_canvas_2_2=Canvas(pro_frame_2_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_2_2.grid_columnconfigure(0,weight=1)
                            pro_frame_2_2.grid_rowconfigure(0,weight=1)
                            
                            vertibar=Scrollbar(pro_frame_2_2, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_2_2.yview)

                            p_canvas_2_2.bind("<Configure>", pro_responsive_widgets_2_2)
                            p_canvas_2_2.config(yscrollcommand=vertibar.set)
                            p_canvas_2_2.grid(row=0,column=0,sticky='nsew')


                            p_canvas_2_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly1'))

                            label_1 = Label(p_canvas_2_2,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1, tags=('ialabel1'))

                            p_canvas_2_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iahline'))

                            p_canvas_2_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly2'))

                            label_1 = Label(p_canvas_2_2,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel2'))

                            comb_inv_2_1 = ttk.Combobox(p_canvas_2_2, font=('arial 10'))
                            comb_inv_2_1['values'] = ("Income",)
                            comb_inv_2_1.current(0)
                            window_comb_inv_2_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_2_1,tags=('iacombo1'))

                            label_1 = Label(p_canvas_2_2,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel3'))

                            entry_inv_2_2=Entry(p_canvas_2_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_inv_2_2 = p_canvas_2_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_2_2,tags=('iaentry1'))

                            label_1 = Label(p_canvas_2_2,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel4'))

                            comb_inv_2_2 = ttk.Combobox(p_canvas_2_2, font=('arial 10'))
                            comb_inv_2_2['values'] = ("Sales of Product Income",)
                            comb_inv_2_2.current(0)
                            window_comb_inv_2_2 = p_canvas_2_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_2_2,tags=('iacombo2'))

                            label_1 = Label(p_canvas_2_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel5'))

                            entry_inv_2_4=Entry(p_canvas_2_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_inv_2_4 = p_canvas_2_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_2_4,tags=('iaentry2'))

                            inv_text_2 = Text(p_canvas_2_2,width=67, height=14, background='black',foreground='white')
                            inv_text_2.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                            window_inv_text_2 = p_canvas_2_2.create_window(0, 0, anchor="nw",window=inv_text_2,tags=('iatext1'))

                            def sub_check_2():
                                comb_inv_2_3.config(state=NORMAL if chk_str_inv_2_1.get() else DISABLED)

                            chk_str_inv_2_1 = IntVar()
                            chkbtn_inv_2_1 = Checkbutton(p_canvas_2_2, text = "Is sub-account", variable = chk_str_inv_2_1, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=sub_check_2)
                            window_chkbtn_inv_2_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=chkbtn_inv_2_1,tags=('iacheck1'))

                            comb_inv_2_3 = ttk.Combobox(p_canvas_2_2, font=('arial 10'),state=DISABLED)
                            comb_inv_2_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                            window_comb_inv_2_3 = p_canvas_2_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_2_3,tags=('iacombo3'))

                            label_1 = Label(p_canvas_2_2,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel6'))

                            comb_inv_2_4 = ttk.Combobox(p_canvas_2_2, font=('arial 10'))
                            comb_inv_2_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                            window_comb_inv_2_4 = p_canvas_2_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_2_4,tags=('iacombo4'))

                            inv_sub_btn_2_1=Button(p_canvas_2_2,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                            window_inv_sub_btn_2_1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=inv_sub_btn_2_1,tags=('iabutton1'))

                            def i_back_2_():
                                pro_frame_2_2.grid_forget()
                                pro_frame_2.grid(row=0,column=0,sticky='nsew')

                            bck_btn1=Button(p_canvas_2_2,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=i_back_2_)
                            window_bck_btn1 = p_canvas_2_2.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('iabutton3'))


                        account_btn=Button(p_canvas_2,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_inc_acc_1)
                        window_account_btn = p_canvas_2.create_window(0, 0, anchor="nw", window=account_btn,tags=('ipbutton3'))

                        p_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iphline1'))

                        label_1 = Label(p_canvas_2,width=22,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel17'))

                        entry_inv_item_9=scrolledtext.ScrolledText(p_canvas_2,width=145,background='#2f516f',foreground="white")
                        window_entry_entry_inv_item_9 = p_canvas_2.create_window(0, 0, anchor="nw", height=60,window=entry_inv_item_9,tags=('ipentry9'))

                        label_1 = Label(p_canvas_2,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel18'))
                        
                        entry_inv_item_10=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_entry_inv_item_10 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_10,tags=('ipentry10'))

                        chk_str_inv_item_1 = StringVar()
                        chkbtn_inv_item_2 = Checkbutton(p_canvas_2, text = "Inclusive of purchase tax", variable = chk_str_inv_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                        chkbtn_inv_item_2.select()
                        window_chkbtn_inv_item_2 = p_canvas_2.create_window(0, 0, anchor="nw", window=chkbtn_inv_item_2,tags=('ipcbutton2'))

                        label_1 = Label(p_canvas_2,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(700, 1530, anchor="nw", window=label_1,tags=('iplabel19'))

                        comb_inv_item_pu5 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                        comb_inv_item_pu5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                        comb_inv_item_pu5.current(0)
                        window_comb_inv_item_pu5 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_pu5,tags=('ipcombo5'))

                        label_1 = Label(p_canvas_2,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel20'))

                        comb_inv_item_ex6 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                        comb_inv_item_ex6['values'] = ("Cost of sales",)
                        comb_inv_item_ex6.current(0)
                        window_comb_inv_item_ex6 = p_canvas_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_item_ex6,tags=('ipcombo6'))

                        def inv_exp_acc_1():
                            pro_frame_2.grid_forget()
                            pro_frame_2_3 = Frame(tab3_4)
                            pro_frame_2_3.grid(row=0,column=0,sticky='nsew')

                            def pro_responsive_widgets_2_3(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("iapoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("ialabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("iahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.52


                                dcanvas.coords("iapoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("iabutton3",dwidth/23,dheight/3.415)

                                dcanvas.coords("ialabel2",dwidth/23,dheight/1.91)
                                dcanvas.coords("ialabel3",dwidth/1.9,dheight/1.91)
                                dcanvas.coords("ialabel4",dwidth/23.3,dheight/1.41)
                                dcanvas.coords("ialabel5",dwidth/1.9,dheight/1.41)
                                dcanvas.coords("ialabel6",dwidth/1.9,dheight/0.95)

                                dcanvas.coords("iaentry1",dwidth/1.9,dheight/1.74)
                                dcanvas.coords("iaentry2",dwidth/1.9,dheight/1.32)

                                dcanvas.coords("iacombo1",dwidth/23,dheight/1.74)
                                dcanvas.coords("iacombo2",dwidth/23,dheight/1.32)
                                dcanvas.coords("iacombo3",dwidth/1.9,dheight/1.09)
                                dcanvas.coords("iacombo4",dwidth/1.9,dheight/0.91)

                                dcanvas.coords("iatext1",dwidth/23,dheight/1.15)
                                dcanvas.coords("iacheck1",dwidth/1.9,dheight/1.155)

                                dcanvas.coords("iabutton1",dwidth/2.3,dheight/0.73)

                            p_canvas_2_3=Canvas(pro_frame_2_3, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
                            
                            pro_frame_2_3.grid_columnconfigure(0,weight=1)
                            pro_frame_2_3.grid_rowconfigure(0,weight=1)

                            vertibar=Scrollbar(pro_frame_2_3, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_2_3.yview)

                            p_canvas_2_3.bind("<Configure>", pro_responsive_widgets_2_3)
                            p_canvas_2_3.config(yscrollcommand=vertibar.set)
                            p_canvas_2_3.grid(row=0,column=0,sticky='nsew')


                            p_canvas_2_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly1'))

                            label_1 = Label(p_canvas_2_3,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1, tags=('ialabel1'))

                            p_canvas_2_3.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iahline'))

                            p_canvas_2_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('iapoly2'))

                            label_1 = Label(p_canvas_2_3,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel2'))

                            comb_inv_3_1 = ttk.Combobox(p_canvas_2_3, font=('arial 10'))
                            comb_inv_3_1['values'] = ("Cost of Goods Sold",)
                            window_comb_inv_3_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_3_1,tags=('iacombo1'))

                            label_1 = Label(p_canvas_2_3,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel3'))

                            entry_inv_3_2=Entry(p_canvas_2_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_inv_3_2 = p_canvas_2_3.create_window(0, 0, anchor="nw", height=30,window=entry_inv_3_2,tags=('iaentry1'))

                            label_1 = Label(p_canvas_2_3,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel4'))

                            comb_inv_3_2 = ttk.Combobox(p_canvas_2_3, font=('arial 10'))
                            comb_inv_3_2['values'] = ("Suppliers and Materials-COS",)
                            window_comb_inv_3_2 = p_canvas_2_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_3_2,tags=('iacombo2'))

                            label_1 = Label(p_canvas_2_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel5'))

                            entry_inv_3_4=Entry(p_canvas_2_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_inv_3_4 = p_canvas_2_3.create_window(0, 0, anchor="nw", height=30,window=entry_inv_3_4,tags=('iaentry2'))

                            inv_text_3 = Text(p_canvas_2_3,width=67, height=14, background='black',foreground='white')
                            inv_text_3.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                            window_inv_text_3 = p_canvas_2_3.create_window(0, 0, anchor="nw",window=inv_text_3,tags=('iatext1'))

                            def sub_check_3():
                                comb_inv_3_3.config(state=NORMAL if chk_str_inv_3_1.get() else DISABLED)
                                

                            chk_str_inv_3_1 = IntVar()
                            chkbtn_inv_3_1 = Checkbutton(p_canvas_2_3, text = "Is sub-account", variable = chk_str_inv_3_1,  font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            chkbtn_inv_3_1.select()
                            window_chkbtn_inv_3_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=chkbtn_inv_3_1,tags=('iacheck1'))

                            comb_inv_3_3 = ttk.Combobox(p_canvas_2_3, font=('arial 10'),state=DISABLED)
                            comb_inv_3_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                            window_comb_inv_3_3 = p_canvas_2_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_3_3,tags=('iacombo3'))

                            label_1 = Label(p_canvas_2_3,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=label_1,tags=('ialabel6'))

                            comb_inv_3_4 = ttk.Combobox(p_canvas_2_3, font=('arial 10'))
                            comb_inv_3_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                            window_comb_inv_3_4 = p_canvas_2_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_3_4,tags=('iacombo4'))

                            inv_sub_btn_3_1=Button(p_canvas_2_3,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                            window_inv_sub_btn_3_1 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=inv_sub_btn_3_1,tags=('iabutton1'))

                            def i_back_3_():
                                pro_frame_2_3.grid_forget()
                                pro_frame_2.grid(row=0,column=0,sticky='nsew')

                            bck_btn3=Button(p_canvas_2_3,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=i_back_3_)
                            window_bck_btn3 = p_canvas_2_3.create_window(0, 0, anchor="nw", window=bck_btn3,tags=('iabutton3'))


                        expense_btn=Button(p_canvas_2,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_exp_acc_1)
                        window_expense_btn = p_canvas_2.create_window(0, 0, anchor="nw", window=expense_btn,tags=('ipbutton4'))

                        label_1 = Label(p_canvas_2,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel21'))

                        def p_rc_1(event):
                            if entry_inv_item_11.get()=="0":
                                entry_inv_item_11.delete(0,END)
                            else:
                                pass

                        entry_inv_item_11=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_entry_inv_item_11 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_11,tags=('ipentry11'))
                        entry_inv_item_11.insert(0,"0")
                        entry_inv_item_11.bind("<Button-1>",p_rc_1)

                        label_1 = Label(p_canvas_2,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel22'))

                        comb_inv_item_pr7 = ttk.Combobox(p_canvas_2, font=('arial 10'))
                        comb_inv_item_pr7['values'] = ("Select Supplier",)
                        comb_inv_item_pr7.current(0)
                        window_comb_inv_item_pr7 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_pr7,tags=('ipcombo7'))

                        inv_sub_btn1=Button(p_canvas_2,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_new_pro_inv)
                        window_inv_sub_btn1 = p_canvas_2.create_window(0, 0, anchor="nw", window=inv_sub_btn1,tags=('ipbutton5'))

                        entry_inv_item_aod5=DateEntry(p_canvas_2,width=60,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_inv_item_aod5 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_aod5,tags=('ipdate1'))


                    p_btn_1=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=inv_add_item)
                    window_p_btn_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_1,tags=('apbutton1'),state=HIDDEN)

                    p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly4"))

                    def noncall(event):
                        p_canvas_1.itemconfig('apimage2',state='hidden')
                        p_canvas_1.itemconfig('aplabel4',state='normal')
                        p_canvas_1.itemconfig('aplabel5',state='normal')
                        p_canvas_1.itemconfig('apbutton2',state='normal')

                    image_n1 = Image.open("images/noninventory.png")
                    resize_image = image_n1.resize((200,150))
                    image_n1 = ImageTk.PhotoImage(resize_image)
                    btlogon = Label(p_canvas_1, width=200, height=150, background="#1b3857", image = image_n1) 
                    window_image = p_canvas_1.create_window(0, 0, anchor="nw", window=btlogon,tags=('apimage2'))
                    btlogon.photo = image_n1
                    btlogon.bind("<Button-1>",noncall)


                    label_1 = Label(p_canvas_1,width=11,height=1,text="Non-Inventory", font=('arial 20'),background="#2f516f",fg="white") 
                    window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel4'),state=HIDDEN)

                    label_1 = Label(p_canvas_1,width=46,height=2,text="A non-inventory is a type of product that is procured, sold, \nconsumed in production but we do not keep inventories for it.", font=('arial 12'),background="#2f516f",fg="white") 
                    window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel5'),state=HIDDEN)

                    def non_add_item():
                        pro_frame_1.grid_forget()
                        pro_frame_3 = Frame(tab3_4)
                        pro_frame_3.grid(row=0,column=0,sticky='nsew')
                        def pro_responsive_widgets_3(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                        
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("nppoly1",x1 + r1,y1,
                            x1 + r1,y1,
                            x2 - r1,y1,
                            x2 - r1,y1,     
                            x2,y1,     
                            #--------------------
                            x2,y1 + r1,     
                            x2,y1 + r1,     
                            x2,y2 - r1,     
                            x2,y2 - r1,     
                            x2,y2,
                            #--------------------
                            x2 - r1,y2,     
                            x2 - r1,y2,     
                            x1 + r1,y2,
                            x1 + r1,y2,
                            x1,y2,
                            #--------------------
                            x1,y2 - r1,
                            x1,y2 - r1,
                            x1,y1 + r1,
                            x1,y1 + r1,
                            x1,y1,
                            )

                            dcanvas.coords("nplabel1",dwidth/3,dheight/8.24)
                            dcanvas.coords("nphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/2.8
                            y21 = dheight/0.29


                            dcanvas.coords("nppoly2",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            r2 = 25
                            x11 = dwidth/24
                            x21 = dwidth/1.050
                            y11 = dheight/2.1
                            y21 = dheight/1.35


                            dcanvas.coords("nppoly3",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            dcanvas.coords("nplabel2",dwidth/3,dheight/1.77)
                            dcanvas.coords("npbutton1",dwidth/1.8,dheight/1.77)

                            dcanvas.coords("nplabel3",dwidth/23.2,dheight/1.23)
                            dcanvas.coords("nplabel4",dwidth/23.3,dheight/1.02)
                            dcanvas.coords("nplabel5",dwidth/1.9,dheight/1.02)
                            dcanvas.coords("nplabel6",dwidth/1.9,dheight/0.92)
                            dcanvas.coords("nplabel7",dwidth/27,dheight/0.865)
                            dcanvas.coords("nplabel8",dwidth/1.915,dheight/0.865)
                            dcanvas.coords("nplabel12",dwidth/26,dheight/0.675)
                            dcanvas.coords("nplabel13",dwidth/26.8,dheight/0.606)
                            dcanvas.coords("nplabel14",dwidth/28.3,dheight/0.538)
                            dcanvas.coords("nplabel15",dwidth/1.9,dheight/0.538)
                            dcanvas.coords("nplabel16",dwidth/28.4,dheight/0.485)
                            dcanvas.coords("nplabel17",dwidth/50,dheight/0.438)
                            dcanvas.coords("nplabel18",dwidth/26,dheight/0.420)
                            dcanvas.coords("nplabel20",dwidth/28,dheight/0.368)
                            dcanvas.coords("nplabel21",dwidth/2.6,dheight/0.368)
                            dcanvas.coords("nplabel22",dwidth/1.5,dheight/0.368)

                            dcanvas.coords("nplabel9",dwidth/23.2,dheight/0.392)
                            dcanvas.coords("nplabel10",dwidth/1.9,dheight/0.392)


                            dcanvas.coords("npentry1",dwidth/23.2,dheight/1.165)
                            dcanvas.coords("npentry2",dwidth/23.2,dheight/0.975)
                            dcanvas.coords("npentry3",dwidth/1.9,dheight/0.975)
                            dcanvas.coords("npentry4",dwidth/1.9,dheight/0.83)
                            dcanvas.coords("npentry7",dwidth/23.2,dheight/0.59)
                            dcanvas.coords("npentry8",dwidth/23.2,dheight/0.525)
                            dcanvas.coords("npentry9",dwidth/23.2,dheight/0.43)
                            dcanvas.coords("npentry10",dwidth/23.2,dheight/0.412)
                            dcanvas.coords("npentry11",dwidth/2.6,dheight/0.362)

                            dcanvas.coords("npcentry2",dwidth/23.2,dheight/0.385)
                            dcanvas.coords("npcentry3",dwidth/1.9,dheight/0.385)

                            dcanvas.coords("npcombo1",dwidth/23.2,dheight/0.83)
                            dcanvas.coords("npcombo3",dwidth/1.9,dheight/0.525)
                            dcanvas.coords("npcombo4",dwidth/23.2,dheight/0.474)
                            dcanvas.coords("npcombo6",dwidth/23.2,dheight/0.362)
                            dcanvas.coords("npcombo7",dwidth/1.5,dheight/0.362)

                            dcanvas.coords("npbutton2",dwidth/23.2,dheight/0.654)
                            dcanvas.coords("npbutton3",dwidth/2.45,dheight/0.474)
                            dcanvas.coords("npbutton4",dwidth/3.37,dheight/0.362)
                            dcanvas.coords("npbutton5",dwidth/2.38,dheight/0.345)

                            dcanvas.coords("npcbutton1",dwidth/23.2,dheight/0.51)
                            dcanvas.coords("npcbutton2",dwidth/23.2,dheight/0.378)

                            dcanvas.coords("npline1",dwidth/21,dheight/0.73,dwidth/1.055,dheight/0.73)
                            dcanvas.coords("nphline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)


                        p_canvas_3=Canvas(pro_frame_3, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                        pro_frame_3.grid_columnconfigure(0,weight=1)
                        pro_frame_3.grid_rowconfigure(0,weight=1)
                    
                        vertibar=Scrollbar(pro_frame_3, orient=VERTICAL)
                        vertibar.grid(row=0,column=1,sticky='ns')
                        vertibar.config(command=p_canvas_3.yview)

                        p_canvas_3.bind("<Configure>", pro_responsive_widgets_3)
                        p_canvas_3.config(yscrollcommand=vertibar.set)
                        p_canvas_3.grid(row=0,column=0,sticky='nsew')

                        def add_new_pro_non():
                            name = entry_non_item_1.get()
                            sku = entry_non_iitem_2.get()
                            hsn = entry_non_item_2.get()
                            unit = comb_inv_item_1.get()
                            category = entry_non_item_3.get()
                            descr = entry_non_item_7.get('1.0', 'end-1c')
                            saleprice = entry_non_item_8.get()
                            income = comb_non_item_4.get()
                            tax = comb_non_item_3.get()
                            purchasedescr = entry_non_item_9.get('1.0', 'end-1c')
                            cost = entry_non_item_10.get()
                            expenseaccount = comb_non_item_6.get()
                            purchasetax = comb_non_item_5.get()
                            revcharge = entry_non_item_11.get()
                            presupplier = comb_non_item_7.get()

                            usrp1_sql = "SELECT id FROM auth_user WHERE username=%s"
                            usrp1_val = (nm_ent.get(),)
                            fbcursor.execute(usrp1_sql,usrp1_val)
                            usrp1_data = fbcursor.fetchone()

                            cmpp1_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                            cmpp1_val = (usrp1_data[0],)
                            fbcursor.execute(cmpp1_sql,cmpp1_val)
                            cmpp1_data = fbcursor.fetchone()
                            cid = cmpp1_data[0]

                            n_p_sql = "INSERT INTO app1_noninventory(name,sku,hsn,unit,category,descr,saleprice,income,tax,purchasedescr,cost,expenseaccount,purchasetax,revcharge,presupplier,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            n_p_val = (name,sku,hsn,unit,category,descr,saleprice,income,tax,purchasedescr,cost,expenseaccount,purchasetax,revcharge,presupplier,cid)
                            fbcursor.execute(n_p_sql,n_p_val)
                            finsysdb.commit()

                            #_________Refresh insert tree________#

                            for record in pro_tree.get_children():
                                pro_tree.delete(record)

     
                            sql_p="select * from auth_user where username=%s"
                            sql_p_val=(nm_ent.get(),)
                            fbcursor.execute(sql_p,sql_p_val,)
                            pr_dt=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pr_dt[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dt=fbcursor.fetchone()

                            p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                            p_val_1 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_1,p_val_1,)
                            p_data_1 = fbcursor.fetchall()
                            
                            count0 = 0
                            for i in p_data_1:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                else:
                                    pass
                            count0 += 1

                            p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                            p_val_2 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_2,p_val_2,)
                            p_data_2 = fbcursor.fetchall()

                            count1 = 0
                            for i in p_data_2:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                else:
                                    pass
                            count1 += 1

                            p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                            p_val_3 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_3,p_val_3,)
                            p_data_3 = fbcursor.fetchall()
                            

                            count2 = 0
                            for i in p_data_3:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                else:
                                    pass
                            count2 += 1

                            p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                            p_val_4 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_4,p_val_4,)
                            p_data_4 = fbcursor.fetchall()
                            

                            count3 = 0
                            for i in p_data_4:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                else:
                                    pass
                            count3 += 1

                            pro_frame_3.destroy()
                            pro_frame.grid(row=0,column=0,sticky='nsew')
                            


                        p_canvas_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('nppoly1'))

                        label_1 = Label(p_canvas_3,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel1'))

                        p_canvas_3.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('nphline'))

                        p_canvas_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('nppoly2'))

                        p_canvas_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('nppoly3'))

                        label_1 = Label(p_canvas_3,width=15,height=2,text="NON-INVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel2'))

                        btn_non_item_2=Button(p_canvas_3,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
                        window_btn_non_item_2 = p_canvas_3.create_window(0, 0, anchor="nw", window=btn_non_item_2, tags=('npbutton1'))

                        label_1 = Label(p_canvas_3,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel3'))

                        entry_non_item_1=Entry(p_canvas_3,width=200,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_non_item_1 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_1, tags=('npentry1'))

                        label_1 = Label(p_canvas_3,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel4'))

                        def ps_2(event):
                            if entry_non_iitem_2.get()=="N41554":
                                entry_non_iitem_2.delete(0,END)
                            else:
                                pass

                        entry_non_iitem_2=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_non_iitem_2 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_iitem_2, tags=('npentry2'))
                        entry_non_iitem_2.insert(0,"N41554")
                        entry_non_iitem_2.bind("<Button-1>",ps_2)

                        label_1 = Label(p_canvas_3,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel5'))

                        entry_non_item_2=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_non_item_2 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_2, tags=('npentry3'))

                        #Define a callback function
                        def callback_1(url):
                            webbrowser.open_new_tab(url)

                        link_2 = Label(p_canvas_3,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
                        window_link_2 = p_canvas_3.create_window(0, 0, anchor="nw", window=link_2, tags=('nplabel6'))
                        link_2.bind("<Button-1>", lambda e:
                        callback_1("https://gstcouncil.gov.in/sites/default/files/goods-rates-booklet-03July2017.pdf"))


                        label_1 = Label(p_canvas_3,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1, tags=('nplabel7'))

                        comb_inv_item_1 = ttk.Combobox(p_canvas_3, font=('arial 10'))
                        comb_inv_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards","OTH Others",)
                        comb_inv_item_1.current(0)
                        window_comb_inv_item_1 = p_canvas_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_1, tags=('npcombo1'))

                        label_1 = Label(p_canvas_3,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel8'))

                        entry_non_item_3=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_inv_item_3 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_3,tags=('npentry4'))

                        p_canvas_3.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('npline1'))

                        label_1 = Label(p_canvas_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel12'))


                        def d_non_check():

                            if chk_str_non_item.get() == True:
                                p_canvas_3.itemconfig('nplabel13',state='normal')
                                p_canvas_3.itemconfig('npentry7',state='normal')
                                p_canvas_3.itemconfig('nplabel14',state='normal')
                                p_canvas_3.itemconfig('npentry8',state='normal')
                                p_canvas_3.itemconfig('npcbutton1',state='normal')
                                p_canvas_3.itemconfig('nplabel15',state='normal')
                                p_canvas_3.itemconfig('npcombo3',state='normal')
                                p_canvas_3.itemconfig('nplabel16',state='normal')
                                p_canvas_3.itemconfig('npcombo4',state='normal')
                                p_canvas_3.itemconfig('npbutton3',state='normal')
                            else:
                                pass                     


                        chk_str_non_item = BooleanVar()
                        chkbtn_non_item = Checkbutton(p_canvas_3, text = "I sell this product/service to my customers.", variable = chk_str_non_item, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=d_non_check)
                        window_chkbtn_non_item = p_canvas_3.create_window(0, 0, anchor="nw", window=chkbtn_non_item,tags=('npbutton2'))

                        label_1 = Label(p_canvas_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel13'),state=HIDDEN)

                        entry_non_item_7=scrolledtext.ScrolledText(p_canvas_3,width=145,background='#2f516f',foreground="white")
                        window_entry_non_item_7 = p_canvas_3.create_window(0, 0, anchor="nw", height=60,window=entry_non_item_7,tags=('npentry7'),state=HIDDEN)

                        label_1 = Label(p_canvas_3,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel14'),state=HIDDEN)
                        
                        entry_non_item_8=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_non_item_8 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_8,tags=('npentry8'),state=HIDDEN)

                        chk_str_non_item_1 = StringVar()
                        chkbtn_non_item_1 = Checkbutton(p_canvas_3, text = "Inclusive of tax", variable = chk_str_non_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                        chkbtn_non_item_1.select()
                        window_chkbtn_non_item_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=chkbtn_non_item_1,tags=('npcbutton1'),state=HIDDEN)

                        label_1 = Label(p_canvas_3,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel15'),state=HIDDEN)

                        comb_non_item_3 = ttk.Combobox(p_canvas_3, font=('arial 10'))
                        comb_non_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                        #comb_non_item_3.current(0)
                        window_comb_non_item_3 = p_canvas_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_item_3,tags=('npcombo3'),state=HIDDEN)

                        label_1 = Label(p_canvas_3,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel16'),state=HIDDEN)

                        comb_non_item_4 = ttk.Combobox(p_canvas_3, font=('arial 10'))
                        comb_non_item_4['values'] = ("Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discount","Sales of Product Income","Services","Unapplied Cash Payment Income","Uncategorised Income",)
                        #comb_non_item_4.current(0)
                        window_comb_non_item_4 = p_canvas_3.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_non_item_4,tags=('npcombo4'),state=HIDDEN)

                        def non_inc_acc_1():
                            pro_frame_3.grid_forget()
                            pro_frame_3_1 = Frame(tab3_4)
                            pro_frame_3_1.grid(row=0,column=0,sticky='nsew')

                            def pro_responsive_widgets_non_1(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("napoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("nalabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("nahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.52


                                dcanvas.coords("napoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("nabutton3",dwidth/23,dheight/3.415)

                                dcanvas.coords("nalabel2",dwidth/23,dheight/1.91)
                                dcanvas.coords("nalabel3",dwidth/1.9,dheight/1.91)
                                dcanvas.coords("nalabel4",dwidth/23.3,dheight/1.41)
                                dcanvas.coords("nalabel5",dwidth/1.9,dheight/1.41)
                                dcanvas.coords("nalabel6",dwidth/1.9,dheight/0.95)

                                dcanvas.coords("naentry1",dwidth/1.9,dheight/1.74)
                                dcanvas.coords("naentry2",dwidth/1.9,dheight/1.32)

                                dcanvas.coords("nacombo1",dwidth/23,dheight/1.74)
                                dcanvas.coords("nacombo2",dwidth/23,dheight/1.32)
                                dcanvas.coords("nacombo3",dwidth/1.9,dheight/1.09)
                                dcanvas.coords("nacombo4",dwidth/1.9,dheight/0.91)

                                dcanvas.coords("natext1",dwidth/23,dheight/1.15)
                                dcanvas.coords("nacheck1",dwidth/1.9,dheight/1.155)

                                dcanvas.coords("nabutton1",dwidth/2.3,dheight/0.73)

                            p_canvas_3_1=Canvas(pro_frame_3_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_3_1.grid_columnconfigure(0,weight=1)
                            pro_frame_3_1.grid_rowconfigure(0,weight=1)
                            
                            vertibar=Scrollbar(pro_frame_3_1, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_3_1.yview)

                            p_canvas_3_1.bind("<Configure>", pro_responsive_widgets_non_1)
                            p_canvas_3_1.config(yscrollcommand=vertibar.set)
                            p_canvas_3_1.grid(row=0,column=0,sticky='nsew')

                            
                            p_canvas_3_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('napoly1'))

                            label_1 = Label(p_canvas_3_1,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1, tags=('nalabel1'))

                            p_canvas_3_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('nahline'))

                            p_canvas_3_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('napoly2'))

                            label_1 = Label(p_canvas_3_1,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel2'))

                            comb_non_2_1 = ttk.Combobox(p_canvas_3_1, font=('arial 10') )
                            comb_non_2_1['values'] = ("Income",)
                            comb_non_2_1.current(0)
                            window_comb_non_2_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_2_1,tags=('nacombo1'))

                            label_1 = Label(p_canvas_3_1,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel3'))

                            entry_non_2_2=Entry(p_canvas_3_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_non_2_2 = p_canvas_3_1.create_window(0, 0, anchor="nw", height=30,window=entry_non_2_2,tags=('naentry1'))

                            label_1 = Label(p_canvas_3_1,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel4'))

                            comb_non_2_2 = ttk.Combobox(p_canvas_3_1, font=('arial 10'),foreground="white")
                            comb_non_2_2['values'] = ("Discounts/Refunds Given","Non-Profit Income","Other Primary Income","Revenue-General","Sales-Retail","Sales-Wholesale","Sales of Product Income","Service/Fee Income","Unapplied Cash Payment Inncome",)
                            comb_non_2_2.current(0)
                            window_comb_non_2_2 = p_canvas_3_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_2_2,tags=('nacombo2'))

                            label_1 = Label(p_canvas_3_1,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel5'))

                            entry_non_2_4=Entry(p_canvas_3_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_non_2_4 = p_canvas_3_1.create_window(0, 0, anchor="nw", height=30,window=entry_non_2_4,tags=('naentry2'))

                            non_text_2 = Text(p_canvas_3_1,width=67, height=14, background='black',foreground='white')
                            non_text_2.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                            window_non_text_2 = p_canvas_3_1.create_window(0, 0, anchor="nw",window=non_text_2,tags=('natext1'))

                            chk_str_non_2_1 = StringVar()
                            chkbtn_non_2_1 = Checkbutton(p_canvas_3_1, text = "Is sub-account", variable = chk_str_non_2_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            chkbtn_non_2_1.select()
                            window_chkbtn_non_2_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=chkbtn_non_2_1,tags=('nacheck1'))

                            comb_non_2_3 = ttk.Combobox(p_canvas_3_1, font=('arial 10'))
                            comb_non_2_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                            comb_non_2_3.current(0)
                            window_comb_non_2_3 = p_canvas_3_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_2_3,tags=('nacombo3'))

                            label_1 = Label(p_canvas_3_1,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=label_1,tags=('nalabel6'))

                            comb_non_2_4 = ttk.Combobox(p_canvas_3_1, font=('arial 10'))
                            comb_non_2_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                            comb_non_2_4.current(0)
                            window_comb_non_2_4 = p_canvas_3_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_2_4,tags=('nacombo4'))

                            non_sub_btn_2_1=Button(p_canvas_3_1,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                            window_non_sub_btn_2_1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=non_sub_btn_2_1,tags=('nabutton1'))

                            def n_back_1_():
                                pro_frame_3_1.grid_forget()
                                pro_frame_3.grid(row=0,column=0,sticky='nsew')

                            nbck_btn1=Button(p_canvas_3_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=n_back_1_)
                            window_nbck_btn1 = p_canvas_3_1.create_window(0, 0, anchor="nw", window=nbck_btn1,tags=('nabutton3'))

                        account_non_btn=Button(p_canvas_3,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=non_inc_acc_1)
                        window_account_non_btn = p_canvas_3.create_window(0, 0, anchor="nw", window=account_non_btn,tags=('npbutton3'),state=HIDDEN)

                        p_canvas_3.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('nphline1'))

                        label_1 = Label(p_canvas_3,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(26, 1300, anchor="nw", window=label_1,tags=('nplabel17'))

                        def p_non_check():
                            
                            if chk_str_non_pitem.get() == True:
                                p_canvas_3.itemconfig('nplabel18',state='normal')
                                p_canvas_3.itemconfig('npentry10',state='normal')
                                p_canvas_3.itemconfig('nplabel9',state='normal')
                                p_canvas_3.itemconfig('npcentry2',state='normal')
                                p_canvas_3.itemconfig('npcbutton2',state='normal')
                                p_canvas_3.itemconfig('nplabel10',state='normal')
                                p_canvas_3.itemconfig('npcentry3',state='normal')
                                p_canvas_3.itemconfig('nplabel20',state='normal')
                                p_canvas_3.itemconfig('npcombo6',state='normal')
                                p_canvas_3.itemconfig('npbutton4',state='normal')
                                p_canvas_3.itemconfig('nplabel21',state='normal')
                                p_canvas_3.itemconfig('npentry11',state='normal')
                                p_canvas_3.itemconfig('nplabel22',state='normal')
                                p_canvas_3.itemconfig('npcombo7',state='normal')
                            else:
                                pass

                        chk_str_non_pitem = BooleanVar()
                        chkbtn_non_pitem = Checkbutton(p_canvas_3, text = "I Purchase this product/service from Supplier.", variable = chk_str_non_pitem, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=p_non_check)
                        window_chkbtn_non_pitem = p_canvas_3.create_window(0, 0, anchor="nw", window=chkbtn_non_pitem,tags=('npentry9'))


                        label_1 = Label(p_canvas_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel18'),state=HIDDEN)

                        entry_non_item_9=scrolledtext.ScrolledText(p_canvas_3,width=145,background='#2f516f',foreground="white")
                        window_entry_non_item_9 = p_canvas_3.create_window(0, 0, anchor="nw", height=60,window=entry_non_item_9,tags=('npentry10'),state=HIDDEN)

                        label_1 = Label(p_canvas_3,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel9'),state=HIDDEN)
                        
                        entry_non_item_10=Entry(p_canvas_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_non_item_10 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_10,tags=('npcentry2'),state=HIDDEN)

                        chk_str_non_item_2 = StringVar()
                        chkbtn_non_item_2 = Checkbutton(p_canvas_3, text = "Inclusive of purchase tax", variable = chk_str_non_item_2, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                        chkbtn_non_item_2.select()
                        window_chkbtn_non_item_2 = p_canvas_3.create_window(0, 0, anchor="nw", window=chkbtn_non_item_2,tags=('npcbutton2'),state=HIDDEN)

                        label_1 = Label(p_canvas_3,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel10'),state=HIDDEN)

                        comb_non_item_5 = ttk.Combobox(p_canvas_3, font=('arial 10'))
                        comb_non_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                        #comb_non_item_5.current(0)
                        window_comb_non_item_5 = p_canvas_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_item_5,tags=('npcentry3'),state=HIDDEN)

                        label_1 = Label(p_canvas_3,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel20'),state=HIDDEN)

                        comb_non_item_6 = ttk.Combobox(p_canvas_3, font=('arial 10'))
                        comb_non_item_6['values'] = ("Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities",)
                        #comb_non_item_6.current(0)
                        window_comb_non_item_6 = p_canvas_3.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_non_item_6,tags=('npcombo6'),state=HIDDEN)

                        def non_exp_acc_1():
                            pro_frame_3.grid_forget()
                            pro_frame_3_2 = Frame(tab3_4)
                            pro_frame_3_2.grid(row=0,column=0,sticky='nsew')

                            def pro_responsive_widgets_non_2(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("eapoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("ealabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("eahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.52


                                dcanvas.coords("eapoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("eabutton3",dwidth/23,dheight/3.415)

                                dcanvas.coords("ealabel2",dwidth/23,dheight/1.91)
                                dcanvas.coords("ealabel3",dwidth/1.9,dheight/1.91)
                                dcanvas.coords("ealabel4",dwidth/23.3,dheight/1.41)
                                dcanvas.coords("ealabel5",dwidth/1.9,dheight/1.41)
                                dcanvas.coords("ealabel6",dwidth/1.9,dheight/0.95)

                                dcanvas.coords("eaentry1",dwidth/1.9,dheight/1.74)
                                dcanvas.coords("eaentry2",dwidth/1.9,dheight/1.32)

                                dcanvas.coords("eacombo1",dwidth/23,dheight/1.74)
                                dcanvas.coords("eacombo2",dwidth/23,dheight/1.32)
                                dcanvas.coords("eacombo3",dwidth/1.9,dheight/1.09)
                                dcanvas.coords("eacombo4",dwidth/1.9,dheight/0.91)

                                dcanvas.coords("eatext1",dwidth/23,dheight/1.15)
                                dcanvas.coords("eacheck1",dwidth/1.9,dheight/1.155)

                                dcanvas.coords("eabutton1",dwidth/2.3,dheight/0.73)

                            p_canvas_3_2=Canvas(pro_frame_3_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_3_2.grid_columnconfigure(0,weight=1)
                            pro_frame_3_2.grid_rowconfigure(0,weight=1)
                            
                            vertibar=Scrollbar(pro_frame_3_2, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_3_2.yview)

                            p_canvas_3_2.bind("<Configure>", pro_responsive_widgets_non_2)
                            p_canvas_3_2.config(yscrollcommand=vertibar.set)
                            p_canvas_3_2.grid(row=0,column=0,sticky='nsew')


                            p_canvas_3_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('eapoly1'))

                            label_1 = Label(p_canvas_3_2,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1, tags=('ealabel1'))

                            p_canvas_3_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('eahline'))

                            p_canvas_3_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('eapoly2'))

                            label_1 = Label(p_canvas_3_2,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel2'))

                            comb_non_3_1 = ttk.Combobox(p_canvas_3_2, font=('arial 10'))
                            comb_non_3_1['values'] = ("Expense",)
                            comb_non_3_1.current(0)
                            window_comb_non_3_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_3_1,tags=('eacombo1'))

                            label_1 = Label(p_canvas_3_2,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel3'))

                            entry_non_3_2=Entry(p_canvas_3_2,width=90,justify=LEFT,background='#2f516f')
                            window_entry_non_3_2 = p_canvas_3_2.create_window(0, 0, anchor="nw", height=30,window=entry_non_3_2,tags=('eaentry1'))

                            label_1 = Label(p_canvas_3_2,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel4'))

                            comb_non_3_2 = ttk.Combobox(p_canvas_3_2, font=('arial 10'))
                            comb_non_3_2['values'] = ("Advertising/Promotional","Amortisation Expense","Auto","Bad Debts","Bank Charges","Borrowing Cost","Charitable Contributions","Commision and Fees","Cost of Labour","Dues and Subscriptions","Equipment Rental","Finance Costs","Income Tax Expense","Insurance","Interest Paid","Legal and Professional Fees","Loss on Discontinued Operations, Net of Tax","Management Compensation","Meals and Entertainment","Office/General Administrative Expenses","Other Miscellaneous Service Cost","Other Selling Expenses","Payroll Expenses","Rent or Lease of Building","Repair and Maintanance","Shipping and Delivery Expense","Shipping, Freight and Delivery","Supplies and Materials","Taxes Paid","Travel Expenses-Gereral and Admin Expenses","Travel Expenses-Selling Expense","Unapplied Cash Bill Payment Expense","Utilities",)
                            comb_non_3_2.current(0)
                            window_comb_non_3_2 = p_canvas_3_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_3_2,tags=('eacombo2'))

                            label_1 = Label(p_canvas_3_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel5'))

                            entry_non_3_4=Entry(p_canvas_3_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_non_3_4 = p_canvas_3_2.create_window(0, 0, anchor="nw", height=30,window=entry_non_3_4,tags=('eaentry2'))

                            non_text_3 = Text(p_canvas_3_2,width=67, height=14, background='black',foreground='white')
                            non_text_3.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                            window_non_text_3 = p_canvas_3_2.create_window(0, 0, anchor="nw",window=non_text_3,tags=('eatext1'))

                            chk_str_non_3_1 = StringVar()
                            chkbtn_non_3_1 = Checkbutton(p_canvas_3_2, text = "Is sub-account", variable = chk_str_non_3_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            chkbtn_non_3_1.select()
                            window_chkbtn_non_3_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=chkbtn_non_3_1,tags=('eacheck1'))

                            comb_non_3_3 = ttk.Combobox(p_canvas_3_2, font=('arial 10'))
                            comb_non_3_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                            comb_non_3_3.current(0)
                            window_comb_non_3_3 = p_canvas_3_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_3_3,tags=('eacombo3'))

                            label_1 = Label(p_canvas_3_2,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=label_1,tags=('ealabel6'))

                            comb_non_3_4 = ttk.Combobox(p_canvas_3_2, font=('arial 10'))
                            comb_non_3_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                            comb_non_3_4.current(0)
                            window_comb_non_3_4 = p_canvas_3_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_non_3_4,tags=('eacombo4'))

                            non_sub_btn_3_1=Button(p_canvas_3_2,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                            window_non_sub_btn_3_1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=non_sub_btn_3_1,tags=('eabutton1'))

                            def n_back_2_():
                                pro_frame_3_2.grid_forget()
                                pro_frame_3.grid(row=0,column=0,sticky='nsew')

                            ebck_btn1=Button(p_canvas_3_2,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=n_back_2_)
                            window_ebck_btn1 = p_canvas_3_2.create_window(0, 0, anchor="nw", window=ebck_btn1,tags=('eabutton3'))

                        expense_non_btn=Button(p_canvas_3,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=non_exp_acc_1)
                        window_expense_non_btn = p_canvas_3.create_window(0, 0, anchor="nw", window=expense_non_btn,tags=('npbutton4'),state=HIDDEN)

                        label_1 = Label(p_canvas_3,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel21'),state=HIDDEN)

                        def pr_2(event):
                            if entry_non_item_11.get()=="0":
                                entry_non_item_11.delete(0,END)
                            else:
                                pass

                        entry_non_item_11=Entry(p_canvas_3,width=50,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_non_item_11 = p_canvas_3.create_window(0, 0, anchor="nw", height=30,window=entry_non_item_11,tags=('npentry11'),state=HIDDEN)
                        entry_non_item_11.insert(0,"0")
                        entry_non_item_11.bind("<Button-1>",pr_2)


                        label_1 = Label(p_canvas_3,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_3.create_window(0, 0, anchor="nw", window=label_1,tags=('nplabel22'),state=HIDDEN)

                        comb_non_item_7 = ttk.Combobox(p_canvas_3, font=('arial 10'))
                        comb_non_item_7['values'] = ("Select Supplier",)
                        #comb_non_item_7.current(0)
                        window_comb_non_item_7 = p_canvas_3.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_non_item_7,tags=('npcombo7'),state=HIDDEN)

                        non_sub_btn1=Button(p_canvas_3,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_new_pro_non)
                        window_non_sub_btn1 = p_canvas_3.create_window(0, 0, anchor="nw", window=non_sub_btn1,tags=('npbutton5'))

                    p_btn_2=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=non_add_item)
                    window_p_btn_2 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_2,tags=('apbutton2'),state=HIDDEN)

                    p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly5"))

                    def sercall(event):
                        p_canvas_1.itemconfig('apimage3',state='hidden')
                        p_canvas_1.itemconfig('aplabel6',state='normal')
                        p_canvas_1.itemconfig('aplabel7',state='normal')
                        p_canvas_1.itemconfig('apbutton3',state='normal')

                    image_s1 = Image.open("images/service.png")
                    resize_image = image_s1.resize((200,150))
                    image_s1 = ImageTk.PhotoImage(resize_image)
                    btlogos = Label(p_canvas_1, width=200, height=150, background="#1b3857", image = image_s1) 
                    window_image = p_canvas_1.create_window(0, 0, anchor="nw", window=btlogos,tags=('apimage3'))
                    btlogos.photo = image_s1
                    btlogos.bind("<Button-1>",sercall)


                    label_1 = Label(p_canvas_1,width=10,height=1,text="Services", font=('arial 20'),background="#2f516f",fg="white") 
                    window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel6'),state=HIDDEN)

                    label_1 = Label(p_canvas_1,width=45,height=2,text="A service is a transaction in which no physical goods are \ntransferred from the seller to the buyer.", font=('arial 12'),background="#2f516f",fg="white") 
                    window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel7'),state=HIDDEN)

                    def ser_add_item():
                        pro_frame_1.grid_forget()
                        pro_frame_4 = Frame(tab3_4)
                        pro_frame_4.grid(row=0,column=0,sticky='nsew')

                        def pro_responsive_widgets_4(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                        
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("sppoly1",x1 + r1,y1,
                            x1 + r1,y1,
                            x2 - r1,y1,
                            x2 - r1,y1,     
                            x2,y1,     
                            #--------------------
                            x2,y1 + r1,     
                            x2,y1 + r1,     
                            x2,y2 - r1,     
                            x2,y2 - r1,     
                            x2,y2,
                            #--------------------
                            x2 - r1,y2,     
                            x2 - r1,y2,     
                            x1 + r1,y2,
                            x1 + r1,y2,
                            x1,y2,
                            #--------------------
                            x1,y2 - r1,
                            x1,y2 - r1,
                            x1,y1 + r1,
                            x1,y1 + r1,
                            x1,y1,
                            )

                            dcanvas.coords("splabel1",dwidth/3,dheight/8.24)
                            dcanvas.coords("sphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/2.8
                            y21 = dheight/0.29


                            dcanvas.coords("sppoly2",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            r2 = 25
                            x11 = dwidth/24
                            x21 = dwidth/1.050
                            y11 = dheight/2.1
                            y21 = dheight/1.35


                            dcanvas.coords("sppoly3",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            dcanvas.coords("splabel2",dwidth/3,dheight/1.77)
                            dcanvas.coords("spbutton1",dwidth/1.8,dheight/1.77)

                            dcanvas.coords("splabel3",dwidth/23.2,dheight/1.23)
                            dcanvas.coords("splabel4",dwidth/23.3,dheight/1.02)
                            dcanvas.coords("splabel5",dwidth/1.9,dheight/1.02)
                            dcanvas.coords("splabel7",dwidth/27,dheight/0.865)
                            dcanvas.coords("splabel8",dwidth/1.915,dheight/0.865)
                            dcanvas.coords("splabel12",dwidth/26,dheight/0.675)
                            dcanvas.coords("splabel13",dwidth/26.8,dheight/0.606)
                            dcanvas.coords("splabel14",dwidth/28.3,dheight/0.538)
                            dcanvas.coords("splabel15",dwidth/1.9,dheight/0.538)
                            dcanvas.coords("splabel16",dwidth/28.4,dheight/0.485)
                            dcanvas.coords("splabel17",dwidth/50,dheight/0.438)
                            dcanvas.coords("splabel18",dwidth/26,dheight/0.420)
                            dcanvas.coords("splabel9",dwidth/23.2,dheight/0.392)
                            dcanvas.coords("splabel10",dwidth/1.9,dheight/0.392)
                            dcanvas.coords("splabel20",dwidth/28,dheight/0.368)
                            dcanvas.coords("splabel21",dwidth/2.6,dheight/0.368)
                            dcanvas.coords("splabel22",dwidth/1.5,dheight/0.368)

                            dcanvas.coords("splabel23",dwidth/2.6,dheight/0.485)

                            dcanvas.coords("splabel24",dwidth/1.53,dheight/0.485)
                            

                            dcanvas.coords("spentry1",dwidth/23.2,dheight/1.165)
                            dcanvas.coords("spentry2",dwidth/23.2,dheight/0.975)
                            dcanvas.coords("spentry3",dwidth/1.9,dheight/0.975)
                            dcanvas.coords("spentry4",dwidth/1.9,dheight/0.83)
                            dcanvas.coords("spentry7",dwidth/23.2,dheight/0.59)
                            dcanvas.coords("spentry8",dwidth/23.2,dheight/0.525)
                            dcanvas.coords("spentry9",dwidth/23.2,dheight/0.43)
                            dcanvas.coords("spentry10",dwidth/23.2,dheight/0.412)
                            dcanvas.coords("spentry11",dwidth/2.6,dheight/0.362)

                            dcanvas.coords("spentry12",dwidth/2.6,dheight/0.474)

                            dcanvas.coords("spcentry2",dwidth/23.2,dheight/0.385)
                            dcanvas.coords("spcentry3",dwidth/1.9,dheight/0.385)

                            dcanvas.coords("spcombo1",dwidth/23.2,dheight/0.83)
                            dcanvas.coords("spcombo3",dwidth/1.9,dheight/0.525)
                            dcanvas.coords("spcombo4",dwidth/23.2,dheight/0.474)
                            dcanvas.coords("spcombo6",dwidth/23.2,dheight/0.362)
                            dcanvas.coords("spcombo7",dwidth/1.5,dheight/0.362)

                            dcanvas.coords("spcombo8",dwidth/1.5,dheight/0.474)

                            dcanvas.coords("spbutton2",dwidth/23.2,dheight/0.654)
                            dcanvas.coords("spbutton3",dwidth/3.37,dheight/0.474)
                            dcanvas.coords("spbutton4",dwidth/3.37,dheight/0.362)
                            dcanvas.coords("spbutton5",dwidth/2.38,dheight/0.345)

                            dcanvas.coords("spcbutton1",dwidth/23.2,dheight/0.51)
                            dcanvas.coords("spcbutton2",dwidth/23.2,dheight/0.378)

                            dcanvas.coords("spline1",dwidth/21,dheight/0.73,dwidth/1.055,dheight/0.73)

                            dcanvas.coords("sphline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)

                        p_canvas_4=Canvas(pro_frame_4, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                        pro_frame_4.grid_columnconfigure(0,weight=1)
                        pro_frame_4.grid_rowconfigure(0,weight=1)
                
                        vertibar=Scrollbar(pro_frame_4, orient=VERTICAL)
                        vertibar.grid(row=0,column=1,sticky='ns')
                        vertibar.config(command=p_canvas_4.yview)

                        p_canvas_4.bind("<Configure>", pro_responsive_widgets_4)
                        p_canvas_4.config(yscrollcommand=vertibar.set)
                        p_canvas_4.grid(row=0,column=0,sticky='nsew')

                        def add_new_pro_ser():
                            name = entry_ser_item_1.get()
                            sku = entry_ser_iitem_2.get()
                            sac = entry_ser_item_2.get()
                            unit = comb_ser_item_1.get()
                            categ = entry_ser_item_3.get()
                            descr = entry_ser_item_7.get('1.0', 'end-1c')
                            saleprice = entry_ser_item_s8.get()
                            income = comb_ser_item_6.get()
                            tax = comb_ser_item_3.get()
                            abatement = entry_ser_iitem_11.get()
                            sertype = comb_ser_iitem_7.get()
                            purchasedescr = entry_ser_item_9.get('1.0', 'end-1c')
                            cost = entry_ser_item_10.get()
                            expenseaccount = comb_ser_item_e6.get()
                            purchasetax = comb_ser_item_5.get()
                            revcharge = entry_sser_item_11.get()
                            presupplier = comb_ser_item_ps7.get()

                            usrp2_sql = "SELECT id FROM auth_user WHERE username=%s"
                            usrp2_val = (nm_ent.get(),)
                            fbcursor.execute(usrp2_sql,usrp2_val)
                            usrp2_data = fbcursor.fetchone()

                            cmpp2_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                            cmpp2_val = (usrp2_data[0],)
                            fbcursor.execute(cmpp2_sql,cmpp2_val)
                            cmpp2_data = fbcursor.fetchone()
                            cid = cmpp2_data[0]

                            s_p_sql = "INSERT INTO app1_service(name,sku,sac,unit,categ,descr,saleprice,income,tax,abatement,sertype,purchasedescr,cost,expenseaccount,purchasetax,revcharge,presupplier,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            s_p_val = (name,sku,sac,unit,categ,descr,saleprice,income,tax,abatement,sertype,purchasedescr,cost,expenseaccount,purchasetax,revcharge,presupplier,cid)
                            fbcursor.execute(s_p_sql,s_p_val)
                            finsysdb.commit()

                            #_________Refresh insert tree________#

                            for record in pro_tree.get_children():
                                pro_tree.delete(record)

     
                            sql_p="select * from auth_user where username=%s"
                            sql_p_val=(nm_ent.get(),)
                            fbcursor.execute(sql_p,sql_p_val,)
                            pr_dt=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pr_dt[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dt=fbcursor.fetchone()

                            p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                            p_val_1 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_1,p_val_1,)
                            p_data_1 = fbcursor.fetchall()
                            
                            count0 = 0
                            for i in p_data_1:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                else:
                                    pass
                            count0 += 1

                            p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                            p_val_2 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_2,p_val_2,)
                            p_data_2 = fbcursor.fetchall()

                            count1 = 0
                            for i in p_data_2:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                else:
                                    pass
                            count1 += 1

                            p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                            p_val_3 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_3,p_val_3,)
                            p_data_3 = fbcursor.fetchall()
                            

                            count2 = 0
                            for i in p_data_3:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                else:
                                    pass
                            count2 += 1

                            p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                            p_val_4 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_4,p_val_4,)
                            p_data_4 = fbcursor.fetchall()
                            

                            count3 = 0
                            for i in p_data_4:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                else:
                                    pass
                            count3 += 1

                            pro_frame_4.destroy()
                            pro_frame.grid(row=0,column=0,sticky='nsew')


                        p_canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sppoly1'))

                        label_1 = Label(p_canvas_4,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel1'))

                        p_canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('sphline'))

                        p_canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sppoly2'))

                        p_canvas_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('sppoly3'))

                        label_1 = Label(p_canvas_4,width=15,height=2,text="SERVICES", font=('arial 20'),background="#2f516f",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel2'))

                        btn_ser_item_2=Button(p_canvas_4,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
                        window_btn_ser_item_2 = p_canvas_4.create_window(0, 0, anchor="nw", window=btn_ser_item_2, tags=('spbutton1'))

                        label_1 = Label(p_canvas_4,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel3'))

                        entry_ser_item_1=Entry(p_canvas_4,width=200,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ser_item_1 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_item_1, tags=('spentry1'))

                        label_1 = Label(p_canvas_4,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel4'))

                        def ps_3(event):
                            if entry_ser_iitem_2.get()=="N41554":
                                entry_ser_iitem_2.delete(0,END)
                            else:
                                pass

                        entry_ser_iitem_2=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ser_iitem_2 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_iitem_2, tags=('spentry2'))
                        entry_ser_iitem_2.insert(0,"N41554")
                        entry_ser_iitem_2.bind("<Button-1>",ps_3)

                        label_1 = Label(p_canvas_4,width=9,height=1,text="SAC Code", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel5'))

                        def p_sac_1(event):
                            if entry_ser_item_2.get()=="Eg: 998841-Coke and refined petroleum product manufacturing services":
                                entry_ser_item_2.delete(0,END)
                            else:
                                pass
                        entry_ser_item_2=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ser_item_2 = p_canvas_4.create_window(710, 630, anchor="nw", height=30,window=entry_ser_item_2, tags=('spentry3'))
                        entry_ser_item_2.insert(0,"Eg: 998841-Coke and refined petroleum product manufacturing services")
                        entry_ser_item_2.bind("<Button-1>",p_sac_1)


                        label_1 = Label(p_canvas_4,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel7'))

                        comb_ser_item_1 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                        comb_ser_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG-BAGS","BAL-BALE","BDL-BUNDLES","BKL-BUCKLES","BOX-BOX","BOU-BILLIONS OF UNITS","BTL-BOTTLES","BUN-BUNCHES","CAN-CANS","CBM-CUBIC METER","CMS-CENTIMETER","CCM-CUBIC CENTIMETER","CTN-CARTONS","DOZ-DOZEN","DRM-DRUM","GGR-GREAT GROSS","GMS-GRAMS","GRS-GROSS","GYD-GRODD YARDS","KGS-KILOGRAMS","KLR-KILOLITER","KME-KILOMETRE","MTS-METRIC TON","MLT-MILLILITRE","MTR-METERS","NOS-NUMBER","PAC-PACKS","PCS-PIECES","PRS-PAIRS","QTL-QUINTAL","ROL-ROLLS","SQF-SQUARE FEET","SET-SETS","SQM-SQUARE METERS","SQY-SQUARE YARDS","TBS-TABLETS","TGM-TEN GROSS","THD-THOUSAND","TON-TONNES","TUB-TUBES","UGS-US GALLONS","UNT-UNITS","YDS-YARDS","OTH-OTHERS",)
                        comb_ser_item_1.current(0)
                        window_comb_ser_item_1 = p_canvas_4.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_item_1, tags=('spcombo1'))

                        label_1 = Label(p_canvas_4,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(705, 710, anchor="nw", window=label_1,tags=('splabel8'))

                        entry_ser_item_3=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ser_item_3 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_item_3,tags=('spentry4'))

                        p_canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('spline1'))


                        label_1 = Label(p_canvas_4,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel12'))

                        def d_ser_check():

                            if chk_str_ser_item.get() == True:
                                p_canvas_4.itemconfig('splabel13',state='normal')
                                p_canvas_4.itemconfig('spentry7',state='normal')
                                p_canvas_4.itemconfig('splabel14',state='normal')
                                p_canvas_4.itemconfig('spentry8',state='normal')
                                p_canvas_4.itemconfig('spcbutton1',state='normal')
                                p_canvas_4.itemconfig('splabel15',state='normal')
                                p_canvas_4.itemconfig('spcombo3',state='normal')
                                p_canvas_4.itemconfig('splabel16',state='normal')
                                p_canvas_4.itemconfig('spcombo4',state='normal')
                                p_canvas_4.itemconfig('spbutton3',state='normal')
                                p_canvas_4.itemconfig('splabel23',state='normal')
                                p_canvas_4.itemconfig('spentry12',state='normal')
                                p_canvas_4.itemconfig('splabel24',state='normal')
                                p_canvas_4.itemconfig('spcombo8',state='normal')
                            else:
                                pass

                        chk_str_ser_item = BooleanVar()
                        chkbtn_ser_item = Checkbutton(p_canvas_4, text = "I sell this product/service to my customers.", variable = chk_str_ser_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=d_ser_check)
                        window_chkbtn_ser_item = p_canvas_4.create_window(0, 0, anchor="nw", window=chkbtn_ser_item,tags=('spbutton2'))

                        label_d1 = Label(p_canvas_4,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_d1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_d1,tags=('splabel13'),state=HIDDEN)

                        entry_ser_item_7=scrolledtext.ScrolledText(p_canvas_4,width=145,background='#2f516f',foreground="white")
                        window_entry_ser_item_7 = p_canvas_4.create_window(0, 0, anchor="nw", height=60,window=entry_ser_item_7,tags=('spentry7'),state=HIDDEN)


                        label_1 = Label(p_canvas_4,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel14'),state=HIDDEN)
                        
                        entry_ser_item_s8=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ser_item_s8 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_item_s8,tags=('spentry8'),state=HIDDEN)

                        chk_str_ser_item_1 = IntVar()
                        chkbtn_ser_item_1 = Checkbutton(p_canvas_4, text = "Inclusive of tax", variable = chk_str_ser_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                        chkbtn_ser_item_1.select()
                        window_chkbtn_ser_item_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=chkbtn_ser_item_1,tags=('spcbutton1'),state=HIDDEN)

                        label_1 = Label(p_canvas_4,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel15'),state=HIDDEN)

                        comb_ser_item_3 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                        comb_ser_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                        comb_ser_item_3.current(0)
                        window_comb_ser_item_3 = p_canvas_4.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_item_3,tags=('spcombo3'),state=HIDDEN)

                        label_1 = Label(p_canvas_4,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel16'),state=HIDDEN)

                        
                        comb_ser_item_6 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                        comb_ser_item_6['values'] = ("Choose...","Billable Expense income","Product Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discounts","Sales of Product Income","Cost of sales","Equipment Rental for Jobs","Uncategorised Income","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Depreciation Expense","Dues and Subscriptions","Housekeeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Internet Expenses","Meals and Enetrtainments","Office Suppliers","Postage and Delivery","Printing and Reprooduction","Professional Fees","Purchases","Rent Expense","Repair and Maintananace","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities","Finance charge Income","Insurance Proceeds Received","Interest Income","Proceeds From Sale os Assets","Shipping and delivery Income","Ask My Accountant","CGST Write-off","GST Write-off","IGST Write-off","Miscellaneous Expense","Political Contributions","Reconcilation Discrepancies","SGST Write-off","Vehicles","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi kalyan Cess","Input Krishi kalyan Cess RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Krishi Kalyan Cess Payable","Input VAT 5%","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output SGST Tax RCM","Output Service Tax","Output Service Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","SGST Payable","Service Tax Payable","Srvice Tax Suspense","Swachh Barath Cess Payable","TDS Payable","VAT Payable","VAT Suspense","Deferred CGST","Deferred GST Input credit","Deferred IGST","Deferred SGST","Deferred Service Tax Input Credit","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Sevice Tax Refund","TDS Receivable","Uncategorised Asset","Undeposited Fund","Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and maintanance","Sales Discount","Sales of Product Income","Uncategorised Income","accumulated Depreciation","Building and Improvements","Furniture and Equipments","Land","Leasehold Improvements","Vehicles","Retained Earnings","Cost of Sales","Equipment Rental for Jobs","Freight and Shipping Costs","Merchant Account Fees","Purchases-Hardware for Resales","Purchases-Software for Resales","Subcontracted Services","Tools and Craft Suppliers",)
                        comb_ser_item_6.current(0)
                        window_comb_ser_item_6 = p_canvas_4.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_ser_item_6,tags=('spcombo4'),state=HIDDEN)

                        def ser_inc_acc_1():
                            pro_frame_4.grid_forget()
                            pro_frame_4_1 = Frame(tab3_4)
                            pro_frame_4_1.grid(row=0,column=0,sticky='nsew')

                            def pro_responsive_widgets_4_1(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("sapoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("salabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("sahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.52


                                dcanvas.coords("sapoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("sabutton3",dwidth/23,dheight/3.415)

                                dcanvas.coords("salabel2",dwidth/23,dheight/1.91)
                                dcanvas.coords("salabel3",dwidth/1.9,dheight/1.91)
                                dcanvas.coords("salabel4",dwidth/23.3,dheight/1.41)
                                dcanvas.coords("salabel5",dwidth/1.9,dheight/1.41)
                                dcanvas.coords("salabel6",dwidth/1.9,dheight/0.95)

                                dcanvas.coords("saentry1",dwidth/1.9,dheight/1.74)
                                dcanvas.coords("saentry2",dwidth/1.9,dheight/1.32)

                                dcanvas.coords("sacombo1",dwidth/23,dheight/1.74)
                                dcanvas.coords("sacombo2",dwidth/23,dheight/1.32)
                                dcanvas.coords("sacombo3",dwidth/1.9,dheight/1.09)
                                dcanvas.coords("sacombo4",dwidth/1.9,dheight/0.91)

                                dcanvas.coords("satext1",dwidth/23,dheight/1.15)
                                dcanvas.coords("sacheck1",dwidth/1.9,dheight/1.155)

                                dcanvas.coords("sabutton1",dwidth/2.3,dheight/0.73)

                            p_canvas_4_1=Canvas(pro_frame_4_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_4_1.grid_columnconfigure(0,weight=1)
                            pro_frame_4_1.grid_rowconfigure(0,weight=1)
                            
                            vertibar=Scrollbar(pro_frame_4_1, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_4_1.yview)

                            p_canvas_4_1.bind("<Configure>", pro_responsive_widgets_4_1)
                            p_canvas_4_1.config(yscrollcommand=vertibar.set)
                            p_canvas_4_1.grid(row=0,column=0,sticky='nsew')


                            p_canvas_4_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sapoly1'))

                            label_1 = Label(p_canvas_4_1,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1, tags=('salabel1'))

                            p_canvas_4_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('sahline'))

                            p_canvas_4_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sapoly2'))

                            label_1 = Label(p_canvas_4_1,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel2'))

                            comb_ser_2_1 = ttk.Combobox(p_canvas_4_1, font=('arial 10'),foreground="white")
                            comb_ser_2_1['values'] = ("Account Receivable(Debtors)","Current Assets","Bank","Fixed Assets","Non-Current Assets","Accounts Payable(Creditors)","Credit Card","Current Liabilities","Non-Current Liabilities","Equity","Income","Other Income","Cost of Goods Sold","Expenses","Other Expenses",)
                            comb_ser_2_1.current(0)
                            window_comb_ser_2_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_2_1,tags=('sacombo1'))

                            label_1 = Label(p_canvas_4_1,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel3'))

                            entry_ser_2_2=Entry(p_canvas_4_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ser_2_2 = p_canvas_4_1.create_window(0, 0, anchor="nw", height=30,window=entry_ser_2_2,tags=('saentry1'))

                            label_1 = Label(p_canvas_4_1,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel4'))

                            comb_ser_2_2 = ttk.Combobox(p_canvas_4_1, font=('arial 10'),foreground="white")
                            comb_ser_2_2['values'] = ("Account Receivable(Debtors)",)
                            comb_ser_2_2.current(0)
                            window_comb_ser_2_2 = p_canvas_4_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_2_2,tags=('sacombo2'))

                            label_1 = Label(p_canvas_4_1,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel5'))

                            entry_ser_2_4=Entry(p_canvas_4_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ser_2_4 = p_canvas_4_1.create_window(0, 0, anchor="nw", height=30,window=entry_ser_2_4,tags=('saentry2'))

                            ser_text_2 = Text(p_canvas_4_1,width=67, height=14, background='black',foreground='white')
                            ser_text_2.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                            window_ser_text_2 = p_canvas_4_1.create_window(0, 0, anchor="nw",window=ser_text_2,tags=('satext1'))

                            chk_str_ser_2_1 = StringVar()
                            chkbtn_ser_2_1 = Checkbutton(p_canvas_4_1, text = "Is sub-account", variable = chk_str_ser_2_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            chkbtn_ser_2_1.select()
                            window_chkbtn_ser_2_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=chkbtn_ser_2_1,tags=('sacheck1'))

                            comb_ser_2_3 = ttk.Combobox(p_canvas_4_1, font=('arial 10'),foreground="white")
                            comb_ser_2_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                            comb_ser_2_3.current(0)
                            window_comb_ser_2_3 = p_canvas_4_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_2_3,tags=('sacombo3'))

                            label_1 = Label(p_canvas_4_1,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=label_1,tags=('salabel6'))

                            comb_ser_2_4 = ttk.Combobox(p_canvas_4_1, font=('arial 10'),foreground="white")
                            comb_ser_2_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                            comb_ser_2_4.current(0)
                            window_comb_ser_2_4 = p_canvas_4_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_2_4,tags=('sacombo4'))

                            ser_sub_btn_2_1=Button(p_canvas_4_1,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                            window_ser_sub_btn_2_1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=ser_sub_btn_2_1,tags=('sabutton1'))

                            def s_back_1_():
                                pro_frame_4_1.grid_forget()
                                pro_frame_4.grid(row=0,column=0,sticky='nsew')

                            bck_btn1=Button(p_canvas_4_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=s_back_1_)
                            window_bck_btn1 = p_canvas_4_1.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('sabutton3'))

                        income_ser_btn=Button(p_canvas_4,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=ser_inc_acc_1)
                        window_income_ser_btn = p_canvas_4.create_window(0, 0, anchor="nw", window=income_ser_btn,tags=('spbutton3'),state=HIDDEN)

                        label_1 = Label(p_canvas_4,width=10,height=1,text="Abatement %", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel23'),state=HIDDEN)

                        def pa_1(event):
                            if entry_ser_iitem_11.get()=="0":
                                entry_ser_iitem_11.delete(0,END)
                            else:
                                pass

                        entry_ser_iitem_11=Entry(p_canvas_4,width=50,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ser_iitem_11 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_iitem_11,tags=('spentry12'),state=HIDDEN)
                        entry_ser_iitem_11.insert(0,"0")
                        entry_ser_iitem_11.bind("<Button-1>",pa_1)

                        label_1 = Label(p_canvas_4,width=14,height=1,text="Service Type", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel24'),state=HIDDEN)

                        comb_ser_iitem_7 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                        comb_ser_iitem_7['values'] = ("Choose...","Stock Broking","Genral Insurance","Courier","Advertsing Agency","Consulting Engineer","Custom House Agent","Steamer Agent","Clearing and Forwarding","Man power Recruiting","Air Travel Agent","Tour operator","Rent a Cab","Architect","Interior Director","Management Consultment","Chartered Accountant","Cost Accountant","Company Scretary","Real Estate Agent","Security Agency","Credit Rating Agency","Market Research Agency","Underwriter","Beauty Parlor","Cargo Handling","Cable Operators","Dry Cleaning","Event Management","Fashion Designer","Life Insurance","Scientific and Technical Consultancy","Photography","Convention Services","Video Tape Production","Sound Recording","Broadcating","Insurance Auxilary Service","banking and Other Financial","Port Services","Authorised Service Station","Health Club and Fitness Centres","Rail Travel Agent","Storage and Warehousing","Business Auxilary","Commercial Coaching","Erection or Installation","Franchise Service","Internet Cafe","Maintanance or Repair","Technical Testing","Technical Inspection","Foreign Exchange Broking","Port","Airport Services","Air Transport","Business Exhibition","Goods Transport","Construction of Commerce Complex","Intellectual Property Service","Opinion Poll Service","Outdoor Catering","Television and Radio Program Production","Survey and Exploration of Minerals","Pandal and Shamiana","Travel Agent","Forward Contract Brokerage","Transport Through Pipeline","Site Preparation","Dredging","Survey and Map Making","Cleaning Service","Clubs and Association Service","Packaging Service","Mailing List Compilation","Residential Complex Construction","Share Transfer Agent","ATM Maintanance","Recovery Agent","Sale of Space for Advertisement","Sponsorship","International Air Travel","Containerised Rail Transport","Business Support Service","Action Service","Public Relation Management","Ship Management","Internet Telephony","Cruise Ship Tour","Credit Card","Telecommunication Service","Mining of Minerals, Oil or Gas","Recting Immovable Property","Works Contract","Development of Consent","Asset Management","Design Services","Information Technology Services","ULIP Management","Stock Exchange Service","Service for Transaction in Goods","Clearing House Services","Supply of Tangiable","Online Inforamtion Retrieval","Mandap keeper",)
                        comb_ser_iitem_7.current(0)
                        window_comb_ser_iitem_7 = p_canvas_4.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_ser_iitem_7,tags=('spcombo8'),state=HIDDEN)

                        p_canvas_4.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('sphline1'))

                        label_1 = Label(p_canvas_4,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel17'))

                        def p_ser_check():

                            if chk_str_ser_pitem.get() == True:
                                p_canvas_4.itemconfig('splabel18',state='normal')
                                p_canvas_4.itemconfig('spentry10',state='normal')
                                p_canvas_4.itemconfig('splabel9',state='normal')
                                p_canvas_4.itemconfig('spcentry2',state='normal')
                                p_canvas_4.itemconfig('spcbutton2',state='normal')
                                p_canvas_4.itemconfig('splabel10',state='normal')
                                p_canvas_4.itemconfig('spcentry3',state='normal')
                                p_canvas_4.itemconfig('splabel20',state='normal')
                                p_canvas_4.itemconfig('spcombo6',state='normal')
                                p_canvas_4.itemconfig('spbutton4',state='normal')
                                p_canvas_4.itemconfig('splabel21',state='normal')
                                p_canvas_4.itemconfig('spentry11',state='normal')
                                p_canvas_4.itemconfig('splabel22',state='normal')
                                p_canvas_4.itemconfig('spcombo7',state='normal')
                            else:
                                pass

                        chk_str_ser_pitem = BooleanVar()
                        chkbtn_ser_pitem = Checkbutton(p_canvas_4, text = "I Purchase this product/service from Supplier.", variable = chk_str_ser_pitem, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=p_ser_check)
                        window_chkbtn_ser_pitem = p_canvas_4.create_window(0, 0, anchor="nw", window=chkbtn_ser_pitem,tags=('spentry9'))


                        label_1 = Label(p_canvas_4,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel18'),state=HIDDEN)

                        entry_ser_item_9=scrolledtext.ScrolledText(p_canvas_4,width=145,background='#2f516f',foreground="white")
                        window_entry_ser_item_9 = p_canvas_4.create_window(0, 0, anchor="nw", height=60,window=entry_ser_item_9,tags=('spentry10'),state=HIDDEN)

                        label_1 = Label(p_canvas_4,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel9'),state=HIDDEN)
                        
                        entry_ser_item_10=Entry(p_canvas_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_ser_item_10 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_ser_item_10,tags=('spcentry2'),state=HIDDEN)

                        chk_str_sser_item_2 = StringVar()
                        chkbtn_sser_item_2 = Checkbutton(p_canvas_4, text = "Inclusive of Tax", variable = chk_str_sser_item_2, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                        chkbtn_sser_item_2.select()
                        window_chkbtn_sser_item_2 = p_canvas_4.create_window(0, 0, anchor="nw", window=chkbtn_sser_item_2,tags=('spcbutton2'),state=HIDDEN)

                        label_1 = Label(p_canvas_4,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel10'),state=HIDDEN)

                        comb_ser_item_5 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                        comb_ser_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                        comb_ser_item_5.current(0)
                        window_comb_ser_item_5 = p_canvas_4.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_item_5,tags=('spcentry3'),state=HIDDEN)

                        label_1 = Label(p_canvas_4,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel20'),state=HIDDEN)

                        comb_ser_item_e6 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                        comb_ser_item_e6['values'] = ("Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities",)
                        comb_ser_item_e6.current(0)
                        window_comb_ser_item_e6 = p_canvas_4.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_ser_item_e6,tags=('spcombo6'),state=HIDDEN)

                        def ser_exp_acc_1():
                            pro_frame_4.grid_forget()
                            pro_frame_4_2 = Frame(tab3_4)
                            pro_frame_4_2.grid(row=0,column=0,sticky='nsew')

                            def pro_responsive_widgets_4_2(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("xapoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("xalabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("xahline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.52


                                dcanvas.coords("xapoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("xabutton3",dwidth/23,dheight/3.415)

                                dcanvas.coords("xalabel2",dwidth/23,dheight/1.91)
                                dcanvas.coords("xalabel3",dwidth/1.9,dheight/1.91)
                                dcanvas.coords("xalabel4",dwidth/23.3,dheight/1.41)
                                dcanvas.coords("xalabel5",dwidth/1.9,dheight/1.41)
                                dcanvas.coords("xalabel6",dwidth/1.9,dheight/0.95)

                                dcanvas.coords("xaentry1",dwidth/1.9,dheight/1.74)
                                dcanvas.coords("xaentry2",dwidth/1.9,dheight/1.32)

                                dcanvas.coords("xacombo1",dwidth/23,dheight/1.74)
                                dcanvas.coords("xacombo2",dwidth/23,dheight/1.32)
                                dcanvas.coords("xacombo3",dwidth/1.9,dheight/1.09)
                                dcanvas.coords("xacombo4",dwidth/1.9,dheight/0.91)

                                dcanvas.coords("xatext1",dwidth/23,dheight/1.15)
                                dcanvas.coords("xacheck1",dwidth/1.9,dheight/1.155)

                                dcanvas.coords("xabutton1",dwidth/2.3,dheight/0.73)

                            p_canvas_4_2=Canvas(pro_frame_4_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_4_2.grid_columnconfigure(0,weight=1)
                            pro_frame_4_2.grid_rowconfigure(0,weight=1)
                            
                            vertibar=Scrollbar(pro_frame_4_2, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_4_2.yview)

                            p_canvas_4_2.bind("<Configure>", pro_responsive_widgets_4_2)
                            p_canvas_4_2.config(yscrollcommand=vertibar.set)
                            p_canvas_4_2.grid(row=0,column=0,sticky='nsew')


                            p_canvas_4_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('xapoly1'))

                            label_1 = Label(p_canvas_4_2,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1, tags=('xalabel1'))

                            p_canvas_4_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('xahline'))

                            p_canvas_4_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('xapoly2'))

                            label_1 = Label(p_canvas_4_2,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel2'))

                            comb_ser_3_1 = ttk.Combobox(p_canvas_4_2, font=('arial 10'),foreground="white")
                            comb_ser_3_1['values'] = ("Account Receivable(Debtors)","Current Assets","Bank","Fixed Assets","Non-Current Assets","Accounts Payable(Creditors)","Credit Card","Current Liabilities","Non-Current Liabilities","Equity","Income","Other Income","Cost of Goods Sold","Expenses","Other Expenses",)
                            comb_ser_3_1.current(0)
                            window_comb_ser_3_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_3_1,tags=('xacombo1'))

                            label_1 = Label(p_canvas_4_2,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel3'))

                            entry_ser_3_2=Entry(p_canvas_4_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ser_3_2 = p_canvas_4_2.create_window(0, 0, anchor="nw", height=30,window=entry_ser_3_2,tags=('xaentry1'))

                            label_1 = Label(p_canvas_4_2,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel4'))

                            comb_ser_3_2 = ttk.Combobox(p_canvas_4_2, font=('arial 10'),foreground="white")
                            comb_ser_3_2['values'] = ("Account Receivable(Debtors)",)
                            comb_ser_3_2.current(0)
                            window_comb_ser_3_2 = p_canvas_4_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_3_2,tags=('xacombo2'))

                            label_1 = Label(p_canvas_4_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel5'))

                            entry_ser_3_4=Entry(p_canvas_4_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ser_3_4 = p_canvas_4_2.create_window(0, 0, anchor="nw", height=30,window=entry_ser_3_4,tags=('xaentry2'))

                            ser_text_3 = Text(p_canvas_4_2,width=67, height=14, background='black',foreground='white')
                            ser_text_3.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                            window_ser_text_3 = p_canvas_4_2.create_window(0, 0, anchor="nw",window=ser_text_3,tags=('xatext1'))

                            chk_str_ser_3_1 = StringVar()
                            chkbtn_ser_3_1 = Checkbutton(p_canvas_4_2, text = "Is sub-account", variable = chk_str_ser_3_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            chkbtn_ser_3_1.select()
                            window_chkbtn_ser_3_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=chkbtn_ser_3_1,tags=('xacheck1'))

                            comb_ser_3_3 = ttk.Combobox(p_canvas_4_2, font=('arial 10'),foreground="white")
                            comb_ser_3_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                            comb_ser_3_3.current(0)
                            window_comb_ser_3_3 = p_canvas_4_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_3_3,tags=('xacombo3'))

                            label_1 = Label(p_canvas_4_2,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=label_1,tags=('xalabel6'))

                            comb_ser_3_4 = ttk.Combobox(p_canvas_4_2, font=('arial 10'),foreground="white")
                            comb_ser_3_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                            comb_ser_3_4.current(0)
                            window_comb_ser_3_4 = p_canvas_4_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_ser_3_4,tags=('xacombo4'))

                            ser_sub_btn_3_1=Button(p_canvas_4_2,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                            window_ser_sub_btn_3_1 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=ser_sub_btn_3_1,tags=('xabutton1'))

                            def s_back_2_():
                                pro_frame_4_2.grid_forget()
                                pro_frame_4.grid(row=0,column=0,sticky='nsew')

                            sbck_btn2=Button(p_canvas_4_2,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=s_back_2_)
                            window_sbck_btn2 = p_canvas_4_2.create_window(0, 0, anchor="nw", window=sbck_btn2,tags=('xabutton3'))

                        expense_ser_btn=Button(p_canvas_4,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=ser_exp_acc_1)
                        window_expense_ser_btn = p_canvas_4.create_window(0, 0, anchor="nw", window=expense_ser_btn,tags=('spbutton4'),state=HIDDEN)

                        label_1 = Label(p_canvas_4,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel21'),state=HIDDEN)

                        def pr_3(event):
                            if entry_sser_item_11.get()=="0":
                                entry_sser_item_11.delete(0,END)
                            else:
                                pass

                        entry_sser_item_11=Entry(p_canvas_4,width=50,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_sser_item_11 = p_canvas_4.create_window(0, 0, anchor="nw", height=30,window=entry_sser_item_11,tags=('spentry11'),state=HIDDEN)
                        entry_sser_item_11.insert(0,"0")
                        entry_sser_item_11.bind("<Button-1>",pr_3)

                        label_1 = Label(p_canvas_4,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_4.create_window(0, 0, anchor="nw", window=label_1,tags=('splabel22'),state=HIDDEN)

                        comb_ser_item_ps7 = ttk.Combobox(p_canvas_4, font=('arial 10'))
                        comb_ser_item_ps7['values'] = ("Select Supplier",)
                        comb_ser_item_ps7.current(0)
                        window_comb_ser_item_ps7 = p_canvas_4.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_ser_item_ps7,tags=('spcombo7'),state=HIDDEN)

                        ser_sub_btn1=Button(p_canvas_4,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_new_pro_ser)
                        window_ser_sub_btn1 = p_canvas_4.create_window(0, 0, anchor="nw", window=ser_sub_btn1,tags=('spbutton5'))

                    p_btn_3=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=ser_add_item)
                    window_p_btn_3 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_3,tags=('apbutton3'),state=HIDDEN)

                    p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly6"))

                    def buncall(event):
                        p_canvas_1.itemconfig('apimage4',state='hidden')
                        p_canvas_1.itemconfig('aplabel8',state='normal')
                        p_canvas_1.itemconfig('aplabel9',state='normal')
                        p_canvas_1.itemconfig('apbutton4',state='normal')

                    image_b1 = Image.open("images/bundle.png")
                    resize_image = image_b1.resize((200,150))
                    image_b1 = ImageTk.PhotoImage(resize_image)
                    btlogob = Label(p_canvas_1, width=200, height=150, background="#1b3857", image = image_b1) 
                    window_image = p_canvas_1.create_window(0, 0, anchor="nw", window=btlogob,tags=('apimage4'))
                    btlogob.photo = image_b1
                    btlogob.bind("<Button-1>",buncall)

                    label_1 = Label(p_canvas_1,width=10,height=1,text="Bundle", font=('arial 20'),background="#2f516f",fg="white") 
                    window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel8'),state=HIDDEN)

                    label_1 = Label(p_canvas_1,width=46,height=2,text="A bundle is a group of software programs or hardware \ndevices that are grouped together and sold as one.", font=('arial 12'),background="#2f516f",fg="white") 
                    window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel9'),state=HIDDEN)

                    def bun_add_item():
                        pro_frame_1.grid_forget()
                        pro_frame_5 = Frame(tab3_4)
                        pro_frame_5.grid(row=0,column=0,sticky='nsew')
                        
                        def pro_responsive_widgets_5(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget
                        
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/14 
                            y2 = dheight/3.505

                            dcanvas.coords("bppoly1",x1 + r1,y1,
                            x1 + r1,y1,
                            x2 - r1,y1,
                            x2 - r1,y1,     
                            x2,y1,     
                            #--------------------
                            x2,y1 + r1,     
                            x2,y1 + r1,     
                            x2,y2 - r1,     
                            x2,y2 - r1,     
                            x2,y2,
                            #--------------------
                            x2 - r1,y2,     
                            x2 - r1,y2,     
                            x1 + r1,y2,
                            x1 + r1,y2,
                            x1,y2,
                            #--------------------
                            x1,y2 - r1,
                            x1,y2 - r1,
                            x1,y1 + r1,
                            x1,y1 + r1,
                            x1,y1,
                            )

                            dcanvas.coords("bplabel1",dwidth/3,dheight/8.24)
                            dcanvas.coords("bphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                            r2 = 25
                            x11 = dwidth/63
                            x21 = dwidth/1.021
                            y11 = dheight/2.8
                            y21 = dheight/0.45


                            dcanvas.coords("bppoly2",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            r2 = 25
                            x11 = dwidth/24
                            x21 = dwidth/1.050
                            y11 = dheight/2.1
                            y21 = dheight/1.35


                            dcanvas.coords("bppoly3",x11 + r2,y11,
                            x11 + r2,y11,
                            x21 - r2,y11,
                            x21 - r2,y11,     
                            x21,y11,     
                            #--------------------
                            x21,y11 + r2,     
                            x21,y11 + r2,     
                            x21,y21 - r2,     
                            x21,y21 - r2,     
                            x21,y21,
                            #--------------------
                            x21 - r2,y21,     
                            x21 - r2,y21,     
                            x11 + r2,y21,
                            x11 + r2,y21,
                            x11,y21,
                            #--------------------
                            x11,y21 - r2,
                            x11,y21 - r2,
                            x11,y11 + r2,
                            x11,y11 + r2,
                            x11,y11,
                            )

                            dcanvas.coords("bplabel2",dwidth/3,dheight/1.77)
                            dcanvas.coords("bpbutton1",dwidth/1.8,dheight/1.77)

                            dcanvas.coords("bplabel3",dwidth/23.2,dheight/1.23)
                            dcanvas.coords("bplabel4",dwidth/1.9,dheight/1.23)
                            dcanvas.coords("bplabel5",dwidth/25,dheight/1.02)
                            dcanvas.coords("bplabel6",dwidth/22.7,dheight/0.8)


                            dcanvas.coords("bpentry1",dwidth/23.2,dheight/1.165)
                            dcanvas.coords("bpentry2",dwidth/1.9,dheight/1.165)
                            dcanvas.coords("bpentry3",dwidth/23.2,dheight/0.97)

                            #-----------------------------H Lines---------------------------------#
                            dcanvas.coords("bpline1",dwidth/21.5,dheight/0.77,dwidth/1.075,dheight/0.77)
                            dcanvas.coords("bpline2",dwidth/21.5,dheight/0.72,dwidth/1.075,dheight/0.72)
                            dcanvas.coords("bpline3",dwidth/21.5,dheight/0.67,dwidth/1.075,dheight/0.67)
                            dcanvas.coords("bpline4",dwidth/21.5,dheight/0.619,dwidth/1.075,dheight/0.619)
                            dcanvas.coords("bpline5",dwidth/21.5,dheight/0.57,dwidth/1.075,dheight/0.57)
                            dcanvas.coords("bpline6",dwidth/21.5,dheight/0.535,dwidth/1.075,dheight/0.535)
                            #-----------------------------V Lines---------------------------------#
                            dcanvas.coords("bpline7",dwidth/21.5,dheight/0.77,dwidth/21.5,dheight/0.535)
                            dcanvas.coords("bpline8",dwidth/1.075,dheight/0.77,dwidth/1.075,dheight/0.535)
                            dcanvas.coords("bpline9",dwidth/4.8,dheight/0.77,dwidth/4.8,dheight/0.535)
                            dcanvas.coords("bpline10",dwidth/2.7,dheight/0.77,dwidth/2.7,dheight/0.535)
                            dcanvas.coords("bpline11",dwidth/1.84,dheight/0.77,dwidth/1.84,dheight/0.535)
                            dcanvas.coords("bpline12",dwidth/1.575,dheight/0.77,dwidth/1.575,dheight/0.535)
                            dcanvas.coords("bpline13",dwidth/1.366,dheight/0.77,dwidth/1.366,dheight/0.535)
                            dcanvas.coords("bpline14",dwidth/1.21,dheight/0.77,dwidth/1.21,dheight/0.535)

                            dcanvas.coords("bplabel7",dwidth/13,dheight/0.754)
                            dcanvas.coords("bplabel8",dwidth/3.85,dheight/0.754)
                            dcanvas.coords("bplabel9",dwidth/2.35,dheight/0.754)
                            dcanvas.coords("bplabel10",dwidth/1.75,dheight/0.754)
                            dcanvas.coords("bplabel11",dwidth/1.515,dheight/0.754)
                            dcanvas.coords("bplabel12",dwidth/1.325,dheight/0.754)
                            dcanvas.coords("bplabel13",dwidth/1.17,dheight/0.754)

                            dcanvas.coords("bpcombo1",dwidth/17,dheight/0.709)
                            dcanvas.coords("bpcombo2",dwidth/17,dheight/0.651)
                            dcanvas.coords("bpcombo3",dwidth/17,dheight/0.604)
                            dcanvas.coords("bpcombo4",dwidth/17,dheight/0.56)

                            dcanvas.coords("bpentry4",dwidth/4.6,dheight/0.709)
                            dcanvas.coords("bpentry5",dwidth/4.6,dheight/0.651)
                            dcanvas.coords("bpentry6",dwidth/4.6,dheight/0.604)
                            dcanvas.coords("bpentry7",dwidth/4.6,dheight/0.56)

                            dcanvas.coords("bpentry8",dwidth/2.6,dheight/0.709)
                            dcanvas.coords("bpentry9",dwidth/2.6,dheight/0.651)
                            dcanvas.coords("bpentry10",dwidth/2.6,dheight/0.604)
                            dcanvas.coords("bpentry11",dwidth/2.6,dheight/0.56)

                            dcanvas.coords("bpspin1",dwidth/1.81,dheight/0.709)
                            dcanvas.coords("bpspin2",dwidth/1.81,dheight/0.651)
                            dcanvas.coords("bpspin3",dwidth/1.81,dheight/0.604)
                            dcanvas.coords("bpspin4",dwidth/1.81,dheight/0.56)

                            dcanvas.coords("bpspin5",dwidth/1.56,dheight/0.709)
                            dcanvas.coords("bpspin6",dwidth/1.56,dheight/0.651)
                            dcanvas.coords("bpspin7",dwidth/1.56,dheight/0.604)
                            dcanvas.coords("bpspin8",dwidth/1.56,dheight/0.56)

                            dcanvas.coords("bpspin9",dwidth/1.351,dheight/0.709)
                            dcanvas.coords("bpspin10",dwidth/1.351,dheight/0.651)
                            dcanvas.coords("bpspin11",dwidth/1.351,dheight/0.604)
                            dcanvas.coords("bpspin12",dwidth/1.351,dheight/0.56)

                            dcanvas.coords("bpspin13",dwidth/1.195,dheight/0.709)
                            dcanvas.coords("bpspin14",dwidth/1.195,dheight/0.651)
                            dcanvas.coords("bpspin15",dwidth/1.195,dheight/0.604)
                            dcanvas.coords("bpspin16",dwidth/1.195,dheight/0.56)

                            dcanvas.coords("bpbutton2",dwidth/2.3,dheight/0.52)




                        p_canvas_5=Canvas(pro_frame_5, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                        pro_frame_5.grid_columnconfigure(0,weight=1)
                        pro_frame_5.grid_rowconfigure(0,weight=1)
                        
                        vertibar=Scrollbar(pro_frame_5, orient=VERTICAL)
                        vertibar.grid(row=0,column=1,sticky='ns')
                        vertibar.config(command=p_canvas_5.yview)

                        p_canvas_5.bind("<Configure>", pro_responsive_widgets_5)
                        p_canvas_5.config(yscrollcommand=vertibar.set)
                        p_canvas_5.grid(row=0,column=0,sticky='nsew')

                        def add_new_pro_bun():

                            name = entry_bun_item_1.get()
                            sku = entry_bun_iitem_2.get()
                            description = entry_bun_item_7.get('1.0', 'end-1c')
                            product1 = bun_comb_1.get()
                            product2 = bun_comb_2.get()
                            product3 = bun_comb_3.get()
                            product4 = bun_comb_4.get()
                            hsn1 = bun_entry_1.get()
                            hsn2 = bun_entry_2.get()
                            hsn3 = bun_entry_3.get()
                            hsn4 = bun_entry_4.get()
                            description1 = bun_entry_5.get('1.0', 'end-1c')
                            description2 = bun_entry_6.get('1.0', 'end-1c')
                            description3 = bun_entry_7.get('1.0', 'end-1c')
                            description4 = bun_entry_8.get('1.0', 'end-1c')
                            qty1 = bun_entry_9.get()
                            qty2 = bun_entry_10.get()
                            qty3 = bun_entry_11.get()
                            qty4 = bun_entry_12.get()
                            price1 = bun_entry_13.get()
                            price2 = bun_entry_14.get()
                            price3 = bun_entry_15.get()
                            price4 = bun_entry_16.get()
                            total1 = bun_entry_17.get()
                            total2 = bun_entry_18.get()
                            total3 = bun_entry_19.get()
                            total4 = bun_entry_20.get()
                            tax1 = bun_entry_21.get()
                            tax2 = bun_entry_22.get()
                            tax3 = bun_entry_23.get()
                            tax4 = bun_entry_24.get()


                            usrp3_sql = "SELECT id FROM auth_user WHERE username=%s"
                            usrp3_val = (nm_ent.get(),)
                            fbcursor.execute(usrp3_sql,usrp3_val)
                            usrp3_data = fbcursor.fetchone()

                            cmpp3_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                            cmpp3_val = (usrp3_data[0],)
                            fbcursor.execute(cmpp3_sql,cmpp3_val)
                            cmpp3_data = fbcursor.fetchone()
                            cid = cmpp3_data[0]

                            b_p_sql = "INSERT INTO app1_bundle(name,sku,description,product1,product2,product3,product4,hsn1,hsn2,hsn3,hsn4,description1,description2,description3,description4,qty1,qty2,qty3,qty4,price1,price2,price3,price4,total1,total2,total3,total4,tax1,tax2,tax3,tax4,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            b_p_val = (name,sku,description,product1,product2,product3,product4,hsn1,hsn2,hsn3,hsn4,description1,description2,description3,description4,qty1,qty2,qty3,qty4,price1,price2,price3,price4,total1,total2,total3,total4,tax1,tax2,tax3,tax4,cid)
                            fbcursor.execute(b_p_sql,b_p_val)
                            finsysdb.commit()

                            #_________Refresh insert tree________#

                            for record in pro_tree.get_children():
                                pro_tree.delete(record)

     
                            sql_p="select * from auth_user where username=%s"
                            sql_p_val=(nm_ent.get(),)
                            fbcursor.execute(sql_p,sql_p_val,)
                            pr_dt=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pr_dt[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dt=fbcursor.fetchone()

                            p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                            p_val_1 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_1,p_val_1,)
                            p_data_1 = fbcursor.fetchall()
                            
                            count0 = 0
                            for i in p_data_1:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                else:
                                    pass
                            count0 += 1

                            p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                            p_val_2 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_2,p_val_2,)
                            p_data_2 = fbcursor.fetchall()

                            count1 = 0
                            for i in p_data_2:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                else:
                                    pass
                            count1 += 1

                            p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                            p_val_3 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_3,p_val_3,)
                            p_data_3 = fbcursor.fetchall()
                            

                            count2 = 0
                            for i in p_data_3:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                else:
                                    pass
                            count2 += 1

                            p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                            p_val_4 = (cmp_dt[0],)
                            fbcursor.execute(p_sql_4,p_val_4,)
                            p_data_4 = fbcursor.fetchall()
                            

                            count3 = 0
                            for i in p_data_4:
                                if True:
                                    pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                else:
                                    pass
                            count3 += 1

                            pro_frame_5.destroy()
                            pro_frame.grid(row=0,column=0,sticky='nsew')


                        p_canvas_5.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('bppoly1'))

                        label_1 = Label(p_canvas_5,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel1'))

                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('bphline'))

                        p_canvas_5.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('bppoly2'))

                        p_canvas_5.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('bppoly3'))
                        
                        label_1 = Label(p_canvas_5,width=15,height=2,text="BUNDLE", font=('arial 20'),background="#2f516f",fg="white") 
                        window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel2'))

                        btn_bun_item_2=Button(p_canvas_5,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
                        window_btn_bun_item_2 = p_canvas_5.create_window(0, 0, anchor="nw", window=btn_bun_item_2, tags=('bpbutton1'))

                        label_1 = Label(p_canvas_5,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel3'))

                        entry_bun_item_1=Entry(p_canvas_5,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_bun_item_1 = p_canvas_5.create_window(55, 530, anchor="nw", height=30,window=entry_bun_item_1, tags=('bpentry1'))

                        label_1 = Label(p_canvas_5,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel4'))

                        def ps_4(event):
                            if entry_bun_iitem_2.get()=="N41554":
                                entry_bun_iitem_2.delete(0,END)
                            else:
                                pass

                        entry_bun_iitem_2=Entry(p_canvas_5,width=90,justify=LEFT,background='#2f516f',foreground="white")
                        window_entry_bun_iitem_2 = p_canvas_5.create_window(0, 0, anchor="nw", height=30,window=entry_bun_iitem_2, tags=('bpentry2'))
                        entry_bun_iitem_2.insert(0,"N41554")
                        entry_bun_iitem_2.bind("<Button-1>",ps_4)


                        label_1 = Label(p_canvas_5,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel5'))

                        entry_bun_item_7=scrolledtext.ScrolledText(p_canvas_5,width=146,background='#2f516f',foreground="white")
                        window_entry_bun_item_7 = p_canvas_5.create_window(0, 0, anchor="nw", height=60,window=entry_bun_item_7, tags=('bpentry3'))

                        label_1 = Label(p_canvas_5,width=30,height=1,text="Products/services included in the bundle", font=('arial 12'),background="#1b3857",fg="white") 
                        window_label_1 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_1, tags=('bplabel6'))

                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline1'))
                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline2'))
                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline3'))
                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline4'))
                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline5'))
                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline6'))
                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline7'))
                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline8'))
                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline9'))
                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline10'))
                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline11'))
                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline12'))
                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline13'))
                        p_canvas_5.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bpline14'))
                        

                        label_3 = Label(p_canvas_5,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_3 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_3,tags=('bplabel7'))

                        label_4 = Label(p_canvas_5,width=10,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_4 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_4,tags=('bplabel8'))

                        label_4 = Label(p_canvas_5,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_4 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_4,tags=('bplabel9'))

                        label_4 = Label(p_canvas_5,width=5,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_4 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_4,tags=('bplabel10'))

                        label_4 = Label(p_canvas_5,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_4 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_4,tags=('bplabel11'))

                        label_4 = Label(p_canvas_5,width=8,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_4 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_4,tags=('bplabel12'))

                        label_4 = Label(p_canvas_5,width=8,height=1,text="TAX", font=('arial 10'),background="#1b3857",fg="white") 
                        window_label_4 = p_canvas_5.create_window(0, 0, anchor="nw", window=label_4,tags=('bplabel13'))

                        def bun_details_1(event):
                            bun_to_str_1 = bun_comb_1.get()
                            try:
                                sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                val = (bun_to_str_1,cmp_dtli[0],)
                                fbcursor.execute(sql,val)
                                bun_sel_1 = fbcursor.fetchone()
                                bun_entry_1.delete(0,END)
                                bun_entry_1.insert(0,bun_sel_1[4])
                                bun_entry_5.delete('1.0',END)
                                bun_entry_5.insert('1.0',bun_sel_1[11])
                                bun_entry_13.delete(0,END)
                                bun_entry_13.insert(0,bun_sel_1[12])
                                bun_entry_21.delete(0,END)
                                bun_entry_21.insert(0,bun_sel_1[14])
                            except:
                                sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                val = (bun_to_str_1,cmp_dtli[0],)
                                fbcursor.execute(sql,val)
                                bun_sel_1 = fbcursor.fetchone()
                                bun_entry_1.delete(0,END)
                                bun_entry_1.insert(0,bun_sel_1[4])
                                bun_entry_5.delete('1.0',END)
                                bun_entry_5.insert('1.0',bun_sel_1[7])
                                bun_entry_13.delete(0,END)
                                bun_entry_13.insert(0,bun_sel_1[8])
                                bun_entry_21.delete(0,END)
                                bun_entry_21.insert(0,bun_sel_1[10])

                        def bun_details_2(event):
                            bun_to_str_2 = bun_comb_2.get()
                            try:
                                sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                val = (bun_to_str_2,cmp_dtli[0],)
                                fbcursor.execute(sql,val)
                                bun_sel_2 = fbcursor.fetchone()
                                bun_entry_2.delete(0,END)
                                bun_entry_2.insert(0,bun_sel_2[4])
                                bun_entry_6.delete('1.0',END)
                                bun_entry_6.insert('1.0',bun_sel_2[11])
                                bun_entry_14.delete(0,END)
                                bun_entry_14.insert(0,bun_sel_2[12])
                                bun_entry_22.delete(0,END)
                                bun_entry_22.insert(0,bun_sel_2[14])
                            except:
                                sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                val = (bun_to_str_2,cmp_dtli[0],)
                                fbcursor.execute(sql,val)
                                bun_sel_2 = fbcursor.fetchone()
                                bun_entry_2.delete(0,END)
                                bun_entry_2.insert(0,bun_sel_2[4])
                                bun_entry_6.delete('1.0',END)
                                bun_entry_6.insert('1.0',bun_sel_2[7])
                                bun_entry_14.delete(0,END)
                                bun_entry_14.insert(0,bun_sel_2[8])
                                bun_entry_22.delete(0,END)
                                bun_entry_22.insert(0,bun_sel_2[10])

                        def bun_details_3(event):
                            bun_to_str_3 = bun_comb_3.get()
                            try:
                                sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                val = (bun_to_str_3,cmp_dtli[0],)
                                fbcursor.execute(sql,val)
                                bun_sel_3 = fbcursor.fetchone()
                                bun_entry_3.delete(0,END)
                                bun_entry_3.insert(0,bun_sel_3[4])
                                bun_entry_7.delete('1.0',END)
                                bun_entry_7.insert('1.0',bun_sel_3[11])
                                bun_entry_15.delete(0,END)
                                bun_entry_15.insert(0,bun_sel_3[12])
                                bun_entry_23.delete(0,END)
                                bun_entry_23.insert(0,bun_sel_3[14])
                            except:
                                sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                val = (bun_to_str_3,cmp_dtli[0],)
                                fbcursor.execute(sql,val)
                                bun_sel_3 = fbcursor.fetchone()
                                bun_entry_3.delete(0,END)
                                bun_entry_3.insert(0,bun_sel_3[4])
                                bun_entry_7.delete('1.0',END)
                                bun_entry_7.insert('1.0',bun_sel_3[7])
                                bun_entry_15.delete(0,END)
                                bun_entry_15.insert(0,bun_sel_3[8])
                                bun_entry_23.delete(0,END)
                                bun_entry_23.insert(0,bun_sel_3[10])

                        def bun_details_4(event):
                            bun_to_str_4 = bun_comb_4.get()
                            try:
                                sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                val = (bun_to_str_4,cmp_dtli[0],)
                                fbcursor.execute(sql,val)
                                bun_sel_4 = fbcursor.fetchone()
                                bun_entry_4.delete(0,END)
                                bun_entry_4.insert(0,bun_sel_4[4])
                                bun_entry_8.delete('1.0',END)
                                bun_entry_8.insert('1.0',bun_sel_4[11])
                                bun_entry_16.delete(0,END)
                                bun_entry_16.insert(0,bun_sel_4[12])
                                bun_entry_24.delete(0,END)
                                bun_entry_24.insert(0,bun_sel_4[14])
                            except:
                                sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                val = (bun_to_str_4,cmp_dtli[0],)
                                fbcursor.execute(sql,val)
                                bun_sel_4 = fbcursor.fetchone()
                                bun_entry_4.delete(0,END)
                                bun_entry_4.insert(0,bun_sel_4[4])
                                bun_entry_8.delete('1.0',END)
                                bun_entry_8.insert('1.0',bun_sel_4[7])
                                bun_entry_16.delete(0,END)
                                bun_entry_16.insert(0,bun_sel_4[8])
                                bun_entry_24.delete(0,END)
                                bun_entry_24.insert(0,bun_sel_4[10])
                            

                        sql_pi="select * from auth_user where username=%s"
                        pi_val=(nm_ent.get(),)
                        fbcursor.execute(sql_pi,pi_val,)
                        pi_dtl=fbcursor.fetchone()

                        sql = "select * from app1_company where id_id=%s"
                        val = (pi_dtl[0],)
                        fbcursor.execute(sql, val,)
                        cmp_dtli=fbcursor.fetchone()
                        print(cmp_dtli)

                        bi_sql = "SELECT name FROM app1_inventory where cid_id=%s"
                        bi_val = (cmp_dtli[0],)
                        fbcursor.execute(bi_sql,bi_val)
                        bi_data = fbcursor.fetchall()
                       
                        bii_sql = "SELECT name FROM app1_noninventory where cid_id=%s"
                        bii_val = (cmp_dtli[0],)
                        fbcursor.execute(bii_sql,bii_val)
                        bii_data = fbcursor.fetchall()

                        b_data = []   
                        
                        for i in bi_data:
                            b_data.append(i[0])
                        for i in bii_data:
                            b_data.append(i[0])
                            


                        bun_comb_1 = ttk.Combobox(p_canvas_5, font=('arial 10'),values=b_data)
                        # bun_comb_1['values'] = ("Choose",b_data,)
                        bun_comb_1.bind("<<ComboboxSelected>>",bun_details_1)
                        window_bun_comb_1 = p_canvas_5.create_window(0, 0, anchor="nw", width=180, height=30,window=bun_comb_1,tags=('bpcombo1'))

                        bun_comb_2 = ttk.Combobox(p_canvas_5, font=('arial 10'),values=b_data)
                        # bun_comb_2['values'] = ("Choose",b_data,)
                        bun_comb_2.bind("<<ComboboxSelected>>",bun_details_2)
                        window_bun_comb_2 = p_canvas_5.create_window(0, 0, anchor="nw", width=180, height=30,window=bun_comb_2,tags=('bpcombo2'))

                        bun_comb_3 = ttk.Combobox(p_canvas_5, font=('arial 10'),values=b_data)
                        # bun_comb_3['values'] = ("Choose",b_data,)
                        bun_comb_3.bind("<<ComboboxSelected>>",bun_details_3)
                        window_bun_comb_3 = p_canvas_5.create_window(0, 0, anchor="nw", width=180, height=30,window=bun_comb_3,tags=('bpcombo3'))

                        bun_comb_4 = ttk.Combobox(p_canvas_5, font=('arial 10'),values=b_data)
                        # bun_comb_4['values'] = ("Choose",b_data,)
                        bun_comb_4.bind("<<ComboboxSelected>>",bun_details_4)
                        window_bun_comb_4 = p_canvas_5.create_window(0, 0, anchor="nw", width=180, height=30,window=bun_comb_4,tags=('bpcombo4'))

                       

                        bun_entry_1=Entry(p_canvas_5,width=30,justify=LEFT,background='#2f516f',foreground="white")
                        window_bun_entry_1 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_1,tags=('bpentry4'))
                        

                        bun_entry_2=Entry(p_canvas_5,width=30,justify=LEFT,background='#2f516f',foreground="white")
                        window_bun_entry_2 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_2,tags=('bpentry5'))
                        

                        bun_entry_3=Entry(p_canvas_5,width=30,justify=LEFT,background='#2f516f',foreground="white")
                        window_bun_entry_3 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_3,tags=('bpentry6'))
                        
                        bun_entry_4=Entry(p_canvas_5,width=30,justify=LEFT,background='#2f516f',foreground="white")
                        window_bun_entry_4 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_4,tags=('bpentry7'))



                        bun_entry_5=scrolledtext.ScrolledText(p_canvas_5,width=23,background='#2f516f',foreground="white")
                        window_bun_entry_5 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_5,tags=('bpentry8'))

                        bun_entry_6=scrolledtext.ScrolledText(p_canvas_5,width=23,background='#2f516f',foreground="white")
                        window_bun_entry_6 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_6,tags=('bpentry9'))

                        bun_entry_7=scrolledtext.ScrolledText(p_canvas_5,width=23,background='#2f516f',foreground="white")
                        window_bun_entry_7 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_7,tags=('bpentry10'))

                        bun_entry_8=scrolledtext.ScrolledText(p_canvas_5,width=23,background='#2f516f',foreground="white")
                        window_bun_entry_8 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_8,tags=('bpentry11'))


                        bun_entry_9=Spinbox(p_canvas_5,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_9 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_9,tags=('bpspin1'))
                        bun_entry_9.delete(0, END)
                        bun_entry_9.insert(0, '0')

                        bun_entry_10=Spinbox(p_canvas_5,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_10 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_10,tags=('bpspin2'))
                        bun_entry_10.delete(0, END)
                        bun_entry_10.insert(0, '0')

                        bun_entry_11=Spinbox(p_canvas_5,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_11 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_11,tags=('bpspin3'))
                        bun_entry_11.delete(0, END)
                        bun_entry_11.insert(0, '0')

                        bun_entry_12=Spinbox(p_canvas_5,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_12 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_12,tags=('bpspin4'))
                        bun_entry_12.delete(0, END)
                        bun_entry_12.insert(0, '0')

                        
                        bun_entry_13=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_13 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_13,tags=('bpspin5'))
                        bun_entry_13.delete(0, END)
                        bun_entry_13.insert(0, '0.0')
                        
                        bun_entry_14=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_14 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_14,tags=('bpspin6'))
                        bun_entry_14.delete(0, END)
                        bun_entry_14.insert(0, '0.0')

                        bun_entry_15=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_15 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_15,tags=('bpspin7'))
                        bun_entry_15.delete(0, END)
                        bun_entry_15.insert(0, '0.0')

                        bun_entry_16=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_16 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_16,tags=('bpspin8'))
                        bun_entry_16.delete(0, END)
                        bun_entry_16.insert(0, '0.0')

                        def multiply_num_1(event):
                            num1= float(bun_entry_9.get())
                            num2= float(bun_entry_13.get())
                            mul= round(num1 * num2)
                            bun_entry_17.delete(0, END)
                            bun_entry_17.insert(0,mul)
                        
                        bun_entry_17=Entry(p_canvas_5,width=16,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_17 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_17,tags=('bpspin9'))
                        bun_entry_17.bind("<Button-1>",multiply_num_1)

                        def multiply_num_2(event):
                            num1= float(bun_entry_10.get())
                            num2= float(bun_entry_14.get())
                            mul= round(num1 * num2)
                            bun_entry_18.delete(0, END)
                            bun_entry_18.insert(0,mul)
                       
                        
                        bun_entry_18=Entry(p_canvas_5,width=16,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_18 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_18,tags=('bpspin10'))
                        bun_entry_18.bind("<Button-1>",multiply_num_2)

                        def multiply_num_3(event):
                            num1= float(bun_entry_11.get())
                            num2= float(bun_entry_15.get())
                            mul= round(num1 * num2)
                            bun_entry_19.delete(0, END)
                            bun_entry_19.insert(0,mul)
                        
                        bun_entry_19=Entry(p_canvas_5,width=16,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_19 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_19,tags=('bpspin11'))
                        bun_entry_19.bind("<Button-1>",multiply_num_3)

                        def multiply_num_4(event):
                            num1= float(bun_entry_12.get())
                            num2= float(bun_entry_16.get())
                            mul= round(num1 * num2)
                            bun_entry_20.delete(0, END)
                            bun_entry_20.insert(0,mul)
                       
                        bun_entry_20=Entry(p_canvas_5,width=16,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_20 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_20,tags=('bpspin12'))
                        bun_entry_20.bind("<Button-1>",multiply_num_4)

                        
                        bun_entry_21=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_21 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_21,tags=('bpspin13'))
                        bun_entry_21.delete(0, END)
                        bun_entry_21.insert(0, '0.0')

                        bun_entry_22=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_22 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_22,tags=('bpspin14'))
                        bun_entry_22.delete(0, END)
                        bun_entry_22.insert(0, '0.0')

                        bun_entry_23=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_23 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_23,tags=('bpspin15'))
                        bun_entry_23.delete(0, END)
                        bun_entry_23.insert(0, '0.0')

                        bun_entry_24=Spinbox(p_canvas_5,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                        window_bun_entry_24 = p_canvas_5.create_window(0, 0, anchor="nw", height=30, window=bun_entry_24,tags=('bpspin16'))
                        bun_entry_24.delete(0, END)
                        bun_entry_24.insert(0, '0.0')

                        bun_sub_btn1=Button(p_canvas_5,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_new_pro_bun)
                        window_bun_sub_btn1 = p_canvas_5.create_window(0, 0, anchor="nw", window=bun_sub_btn1,tags=('bpbutton2'))


                    p_btn_4=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=bun_add_item)
                    window_p_btn_4 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_4,tags=('apbutton4'),state=HIDDEN)

                    def pro_back_1():
                        pro_frame_1.grid_forget()
                        pro_frame.grid(row=0,column=0,sticky='nsew')

                    pbck_btn1=Button(p_canvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=pro_back_1)
                    window_pbck_btn1 = p_canvas_1.create_window(0, 0, anchor="nw", window=pbck_btn1,tags=('apbutton5'))


                pbtn1=Button(pro_canvas,text='Add Products', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_product)
                window_pbtn1 = pro_canvas.create_window(0, 0, anchor="nw", window=pbtn1,tags=('pbutton2'))

                def pro_edit_item(event):
                    if pro_comb_1.get() == 'Edit':
                        if pro_tree.item(pro_tree.focus())["values"][1] == 'Inventory':
                            pro_frame.grid_forget()
                            pro_frame_edit_1 = Frame(tab3_4)
                            pro_frame_edit_1.grid(row=0,column=0,sticky='nsew')

                            def pro_responsive_widgets_2(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("ieppoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("ieplabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("iephline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.29


                                dcanvas.coords("ieppoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                r2 = 25
                                x11 = dwidth/24
                                x21 = dwidth/1.050
                                y11 = dheight/2.1
                                y21 = dheight/1.35


                                dcanvas.coords("ieppoly3",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("ieplabel2",dwidth/2.4,dheight/1.77)
                                dcanvas.coords("iepbutton1",dwidth/1.8,dheight/1.77)

                                dcanvas.coords("ieplabel3",dwidth/23.2,dheight/1.23)
                                dcanvas.coords("ieplabel4",dwidth/23.3,dheight/1.02)
                                dcanvas.coords("ieplabel5",dwidth/1.9,dheight/1.02)
                                dcanvas.coords("ieplabel6",dwidth/1.9,dheight/0.92)
                                dcanvas.coords("ieplabel7",dwidth/27,dheight/0.865)
                                dcanvas.coords("ieplabel8",dwidth/1.915,dheight/0.865)
                                dcanvas.coords("ieplabel9",dwidth/50,dheight/0.76)
                                dcanvas.coords("ieplabel10",dwidth/2.95,dheight/0.76)
                                dcanvas.coords("ieplabel11",dwidth/1.54,dheight/0.76)
                                dcanvas.coords("ieplabel12",dwidth/38,dheight/0.675)
                                dcanvas.coords("ieplabel13",dwidth/26.8,dheight/0.606)
                                dcanvas.coords("ieplabel14",dwidth/28.3,dheight/0.538)
                                dcanvas.coords("ieplabel15",dwidth/1.9,dheight/0.538)
                                dcanvas.coords("ieplabel16",dwidth/28.4,dheight/0.485)
                                dcanvas.coords("ieplabel17",dwidth/29.3,dheight/0.438)
                                dcanvas.coords("ieplabel18",dwidth/28,dheight/0.401)
                                dcanvas.coords("ieplabel19",dwidth/1.91,dheight/0.401)
                                dcanvas.coords("ieplabel20",dwidth/28,dheight/0.37)
                                dcanvas.coords("ieplabel21",dwidth/26,dheight/0.35)
                                dcanvas.coords("ieplabel22",dwidth/1.9,dheight/0.35)

                                dcanvas.coords("iepentry1",dwidth/23.2,dheight/1.165)
                                dcanvas.coords("iepentry2",dwidth/23.2,dheight/0.975)
                                dcanvas.coords("iepentry3",dwidth/1.9,dheight/0.975)
                                dcanvas.coords("iepentry4",dwidth/1.9,dheight/0.83)
                                dcanvas.coords("iepentry5",dwidth/23.2,dheight/0.73)
                                dcanvas.coords("iepentry6",dwidth/1.52,dheight/0.73)
                                dcanvas.coords("iepentry7",dwidth/23.2,dheight/0.59)
                                dcanvas.coords("iepentry8",dwidth/23.2,dheight/0.525)
                                dcanvas.coords("iepentry9",dwidth/23.2,dheight/0.43)
                                dcanvas.coords("iepentry10",dwidth/23.2,dheight/0.394)
                                dcanvas.coords("iepentry11",dwidth/23.2,dheight/0.344)

                                dcanvas.coords("iepcombo1",dwidth/23.2,dheight/0.83)
                                dcanvas.coords("iepcombo2",dwidth/23.2,dheight/0.654)
                                dcanvas.coords("iepcombo3",dwidth/1.9,dheight/0.525)
                                dcanvas.coords("iepcombo4",dwidth/23.2,dheight/0.474)
                                dcanvas.coords("iepcombo5",dwidth/1.89,dheight/0.394)
                                dcanvas.coords("iepcombo6",dwidth/23.2,dheight/0.364)
                                dcanvas.coords("iepcombo7",dwidth/1.89,dheight/0.344)

                                dcanvas.coords("iepcbutton1",dwidth/23.2,dheight/0.51)
                                dcanvas.coords("iepcbutton2",dwidth/23.2,dheight/0.385)

                                dcanvas.coords("iepbutton2",dwidth/2.45,dheight/0.654)
                                dcanvas.coords("iepbutton3",dwidth/2.45,dheight/0.474)
                                dcanvas.coords("iepbutton4",dwidth/2.45,dheight/0.364)
                                dcanvas.coords("iepbutton5",dwidth/2.38,dheight/0.325)

                                dcanvas.coords("iepbuttn1",dwidth/23,dheight/3.415)

                                dcanvas.coords("iephline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)

                                try:
                                    dcanvas.coords("iepdate1",dwidth/2.9,dheight/0.73)
                                except:
                                    pass


                            p_canvas_edit_1=Canvas(pro_frame_edit_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_edit_1.grid_columnconfigure(0,weight=1)
                            pro_frame_edit_1.grid_rowconfigure(0,weight=1)
                        
                            vertibar=Scrollbar(pro_frame_edit_1, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_edit_1.yview)

                            p_canvas_edit_1.bind("<Configure>", pro_responsive_widgets_2)
                            p_canvas_edit_1.config(yscrollcommand=vertibar.set)
                            p_canvas_edit_1.grid(row=0,column=0,sticky='nsew')

                            inv_peditid = pro_tree.item(pro_tree.focus())["values"][2]
                            print(inv_peditid)

                            inv_peditid_1 = pro_tree.item(pro_tree.focus())["values"][3]
                            print(inv_peditid_1)

                            sql_pi="select * from auth_user where username=%s"
                            pi_val=(nm_ent.get(),)
                            fbcursor.execute(sql_pi,pi_val,)
                            pi_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pi_dtl[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dtli=fbcursor.fetchone()
                            print(cmp_dtli)

                            sql = 'select * from app1_inventory where name = %s and sku = %s and cid_id = %s'
                            val =  (inv_peditid,inv_peditid_1,cmp_dtli[0],)
                            fbcursor.execute(sql,val)
                            edit_pinv = fbcursor.fetchone()

                            def edit_new_pro_inv():
                                name = edit_inv_pitem_1.get()
                                sku = edit_inv_pitem_2.get()
                                hsn = edit_inv_pitem_h1.get()
                                unit = comb_inv_edit_p1.get()
                                category = edit_inv_pitem_3.get()
                                initialqty = edit_inv_pitem_4.get()
                                date = edit_inv_pitem_aod5.get_date()
                                stockalrt = edit_inv_pitem_6.get()
                                invacnt = comb_inv_edit_i2.get()
                                description = edit_inv_pitem_7.get('1.0', 'end-1c')
                                salesprice = edit_inv_pitem_8.get()
                                incomeacnt = comb_inv_edit_in4.get()
                                tax = comb_inv_edit_t3.get()
                                purchaseinfo = edit_inv_pitem_9.get('1.0', 'end-1c')
                                cost = edit_inv_pitem_10.get()
                                expacnt = comb_inv_edit_ex6.get()
                                purtax = comb_inv_edit_pu5.get()
                                revcharge = edit_inv_pitem_11.get()
                                presupplier = comb_inv_edit_pr7.get()

                                usrp_sql = "SELECT id FROM auth_user WHERE username=%s"
                                usrp_val = (nm_ent.get(),)
                                fbcursor.execute(usrp_sql,usrp_val)
                                usrp_data = fbcursor.fetchone()

                                cmpp_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                cmpp_val = (usrp_data[0],)
                                fbcursor.execute(cmpp_sql,cmpp_val)
                                cmpp_data = fbcursor.fetchone()
                                cid = cmpp_data[0]
                                
                                i_p_sql = "UPDATE app1_inventory set  name=%s,sku=%s,hsn=%s,unit=%s,category=%s,initialqty=%s,date=%s,stockalrt=%s,invacnt=%s,description=%s,salesprice=%s,incomeacnt=%s,tax=%s,purchaseinfo=%s,cost=%s,expacnt=%s,purtax=%s,revcharge=%s,presupplier=%s,cid_id=%s where name=%s and sku = %s"
                                i_p_val = (name,sku,hsn,unit,category,initialqty,date,stockalrt,invacnt,description,salesprice,incomeacnt,tax,purchaseinfo,cost,expacnt,purtax,revcharge,presupplier,cid,inv_peditid,inv_peditid_1)
                                fbcursor.execute(i_p_sql,i_p_val)
                                finsysdb.commit()

                                #_________Refresh insert tree________#
            
                                for record in pro_tree.get_children():
                                    pro_tree.delete(record)


                                sql_p="select * from auth_user where username=%s"
                                sql_p_val=(nm_ent.get(),)
                                fbcursor.execute(sql_p,sql_p_val,)
                                pr_dt=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dt[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dt=fbcursor.fetchone()

                                p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                                p_val_1 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_1,p_val_1,)
                                p_data_1 = fbcursor.fetchall()
                                
                                count0 = 0
                                for i in p_data_1:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                    else:
                                        pass
                                count0 += 1

                                p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                                p_val_2 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_2,p_val_2,)
                                p_data_2 = fbcursor.fetchall()

                                count1 = 0
                                for i in p_data_2:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count1 += 1

                                p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                                p_val_3 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_3,p_val_3,)
                                p_data_3 = fbcursor.fetchall()
                                

                                count2 = 0
                                for i in p_data_3:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count2 += 1

                                p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                                p_val_4 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_4,p_val_4,)
                                p_data_4 = fbcursor.fetchall()
                                

                                count3 = 0
                                for i in p_data_4:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                    else:
                                        pass
                                count3 += 1

                                pro_frame_edit_1.destroy()
                                pro_frame.grid(row=0,column=0,sticky='nsew')



                            p_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('ieppoly1'))

                            label_1 = Label(p_canvas_edit_1,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ieplabel1'))

                            p_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iephline'))

                            p_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('ieppoly2'))

                            p_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('ieppoly3'))

                            label_1 = Label(p_canvas_edit_1,width=10,height=2,text="INVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ieplabel2'))


                            label_1 = Label(p_canvas_edit_1,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ieplabel3'))

                            edit_inv_pitem_1=Entry(p_canvas_edit_1,width=200,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_inv_pitem_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_1, tags=('iepentry1'))
                            edit_inv_pitem_1.delete(0,'end')
                            edit_inv_pitem_1.insert(0, edit_pinv[2])

                            label_1 = Label(p_canvas_edit_1,width=4,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ieplabel4'))

                            def pei_sku_1(event):
                                if edit_inv_pitem_2.get()==edit_pinv[3]:
                                    edit_inv_pitem_2.delete(0,END)
                                else:
                                    pass
                            
                            edit_inv_pitem_2=Entry(p_canvas_edit_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_inv_pitem_2 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_2, tags=('iepentry2'))
                            # edit_inv_pitem_2.insert(0,"N41554")
                            edit_inv_pitem_2.bind("<Button-1>",pei_sku_1)
                            edit_inv_pitem_2.delete(0,'end')
                            edit_inv_pitem_2.insert(0, edit_pinv[3])


                            label_1 = Label(p_canvas_edit_1,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ieplabel5'))

                            edit_inv_pitem_h1=Entry(p_canvas_edit_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_inv_pitem_h1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_h1, tags=('iepentry3'))
                            edit_inv_pitem_h1.delete(0,'end')
                            edit_inv_pitem_h1.insert(0, edit_pinv[4])

                            #Define a callback function
                            def ecallback(url):
                                webbrowser.open_new_tab(url)

                            link_e1 = Label(p_canvas_edit_1,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
                            window_link_e1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=link_e1, tags=('ieplabel6'))
                            link_e1.bind("<Button-1>", lambda e:
                            ecallback("https://gstcouncil.gov.in/sites/default/files/goods-rates-booklet-03July2017.pdf"))

                            label_1 = Label(p_canvas_edit_1,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=('ieplabel7'))

                            comb_inv_edit_p1 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                            comb_inv_edit_p1['values'] = ("Choose...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards",)
                            comb_inv_edit_p1.current(0)
                            window_comb_inv_edit_p1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_edit_p1, tags=('iepcombo1'))
                            comb_inv_edit_p1.delete(0,'end')
                            comb_inv_edit_p1.insert(0, edit_pinv[5])


                            label_1 = Label(p_canvas_edit_1,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel8'))

                            edit_inv_pitem_3=Entry(p_canvas_edit_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_inv_pitem_3 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_3,tags=('iepentry4'))
                            edit_inv_pitem_3.delete(0,'end')
                            edit_inv_pitem_3.insert(0, edit_pinv[6])

                            label_1 = Label(p_canvas_edit_1,width=24,height=1,text="Initial quantity on hand", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel9'))

                            edit_inv_pitem_4=Entry(p_canvas_edit_1,width=60,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_inv_pitem_4 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_4,tags=('iepentry5'))
                            edit_inv_pitem_4.delete(0,'end')
                            edit_inv_pitem_4.insert(0, edit_pinv[7])

                            label_1 = Label(p_canvas_edit_1,width=10,height=1,text="As of date", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel10'))
                
                            label_1 = Label(p_canvas_edit_1,width=14,height=1,text="Low stock alert", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel11'))

                            edit_inv_pitem_6=Entry(p_canvas_edit_1,width=60,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_inv_pitem_6 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_6,tags=('iepentry6'))
                            edit_inv_pitem_6.delete(0,'end')
                            edit_inv_pitem_6.insert(0, edit_pinv[9])

                            label_1 = Label(p_canvas_edit_1,width=22,height=1,text="Inventory asset account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(35, 910, anchor="nw", window=label_1,tags=('ieplabel12'))

                            comb_inv_edit_i2 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                            comb_inv_edit_i2['values'] = ("Inventory Asset",)
                            comb_inv_edit_i2.current(0)
                            window_comb_inv_edit_i2 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_edit_i2,tags=('iepcombo2'))
                            comb_inv_edit_i2.delete(0,'end')
                            comb_inv_edit_i2.insert(0, edit_pinv[10])

                            
                            label_1 = Label(p_canvas_edit_1,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel13'))

                            edit_inv_pitem_7=scrolledtext.ScrolledText(p_canvas_edit_1,width=145,background='#2f516f',foreground="white")
                            window_edit_inv_pitem_7 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=60,window=edit_inv_pitem_7,tags=('iepentry7'))
                            edit_inv_pitem_7.insert(1.0,edit_pinv[11])

                            label_1 = Label(p_canvas_edit_1,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel14'))
                            
                            edit_inv_pitem_8=Entry(p_canvas_edit_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_inv_pitem_8 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_8,tags=('iepentry8'))
                            edit_inv_pitem_8.delete(0,'end')
                            edit_inv_pitem_8.insert(0, edit_pinv[12])

                            chk_str_einv_item = StringVar()
                            chkbtn_inv_pitem_1 = Checkbutton(p_canvas_edit_1, text = "Inclusive of tax", variable = chk_str_einv_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            chkbtn_inv_pitem_1.select()
                            window_chkbtn_inv_pitem_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=chkbtn_inv_pitem_1,tags=('iepcbutton1'))

                            label_1 = Label(p_canvas_edit_1,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel15'))

                            comb_inv_edit_t3 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                            comb_inv_edit_t3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                            comb_inv_edit_t3.current(0)
                            window_comb_inv_edit_t3 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_edit_t3,tags=('iepcombo3'))
                            comb_inv_edit_t3.delete(0,'end')
                            comb_inv_edit_t3.insert(0, edit_pinv[14])

                            label_1 = Label(p_canvas_edit_1,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel16'))

                            comb_inv_edit_in4 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                            comb_inv_edit_in4['values'] = ("Choose...","Billable Expense Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales of Product Income","Uncategorised Income",)
                            comb_inv_edit_in4.current(0)
                            window_comb_inv_edit_in4 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_edit_in4,tags=('iepcombo4'))
                            comb_inv_edit_in4.delete(0,'end')
                            comb_inv_edit_in4.insert(0, edit_pinv[13])


                            p_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iephline1'))

                            label_1 = Label(p_canvas_edit_1,width=22,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel17'))

                            edit_inv_pitem_9=scrolledtext.ScrolledText(p_canvas_edit_1,width=145,background='#2f516f',foreground="white")
                            window_edit_inv_pitem_9 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=60,window=edit_inv_pitem_9,tags=('iepentry9'))
                            edit_inv_pitem_9.insert(1.0,edit_pinv[15])

                            label_1 = Label(p_canvas_edit_1,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel18'))
                            
                            edit_inv_pitem_10=Entry(p_canvas_edit_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_inv_pitem_10 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_10,tags=('iepentry10'))
                            edit_inv_pitem_10.delete(0,'end')
                            edit_inv_pitem_10.insert(0, edit_pinv[16])


                            chk_str_inv_pitem_1 = StringVar()
                            chkbtn_inv_pitem_2 = Checkbutton(p_canvas_edit_1, text = "Inclusive of purchase tax", variable = chk_str_inv_pitem_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            chkbtn_inv_pitem_2.select()
                            window_chkbtn_inv_pitem_2 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=chkbtn_inv_pitem_2,tags=('iepcbutton2'))

                            label_1 = Label(p_canvas_edit_1,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(700, 1530, anchor="nw", window=label_1,tags=('ieplabel19'))

                            comb_inv_edit_pu5 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                            comb_inv_edit_pu5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                            comb_inv_edit_pu5.current(0)
                            window_comb_inv_edit_pu5 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_edit_pu5,tags=('iepcombo5'))
                            comb_inv_edit_pu5.delete(0,'end')
                            comb_inv_edit_pu5.insert(0, edit_pinv[18])

                            label_1 = Label(p_canvas_edit_1,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel20'))

                            comb_inv_edit_ex6 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                            comb_inv_edit_ex6['values'] = ("Cost of sales",)
                            comb_inv_edit_ex6.current(0)
                            window_comb_inv_edit_ex6 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_edit_ex6,tags=('iepcombo6'))
                            comb_inv_edit_ex6.delete(0,'end')
                            comb_inv_edit_ex6.insert(0, edit_pinv[17])

                            label_1 = Label(p_canvas_edit_1,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel21'))

                            def p_erc_1(event):
                                if edit_inv_pitem_11.get()=="0":
                                    edit_inv_pitem_11.delete(0,END)
                                else:
                                    pass

                            edit_inv_pitem_11=Entry(p_canvas_edit_1,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_inv_pitem_11 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_11,tags=('iepentry11'))
                            # edit_inv_pitem_11.insert(0,"0")
                            edit_inv_pitem_11.bind("<Button-1>",p_erc_1)
                            edit_inv_pitem_11.delete(0,'end')
                            edit_inv_pitem_11.insert(0, edit_pinv[19])
                            

                            label_1 = Label(p_canvas_edit_1,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1,tags=('ieplabel22'))

                            comb_inv_edit_pr7 = ttk.Combobox(p_canvas_edit_1, font=('arial 10'))
                            comb_inv_edit_pr7['values'] = ("Select Supplier",)
                            comb_inv_edit_pr7.current(0)
                            window_comb_inv_edit_pr7 = p_canvas_edit_1.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_edit_pr7,tags=('iepcombo7'))
                            comb_inv_edit_pr7.delete(0,'end')
                            comb_inv_edit_pr7.insert(0, edit_pinv[20])

                            einv_sub_btn1=Button(p_canvas_edit_1,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=edit_new_pro_inv)
                            window_einv_sub_btn1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=einv_sub_btn1,tags=('iepbutton5'))

                            def i_eback_1_():
                                pro_frame_edit_1.grid_forget()
                                pro_frame.grid(row=0,column=0,sticky='nsew')

                            bck_eibtn1=Button(p_canvas_edit_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=i_eback_1_)
                            window_bck_eibtn1 = p_canvas_edit_1.create_window(0, 0, anchor="nw", window=bck_eibtn1,tags=('iepbuttn1'))

                            edit_inv_pitem_aod5=DateEntry(p_canvas_edit_1,width=60,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_inv_pitem_aod5 = p_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=edit_inv_pitem_aod5,tags=('iepdate1'))
                            edit_inv_pitem_aod5.delete(0, 'end')
                            edit_inv_pitem_aod5.insert(0, edit_pinv[8])

                        elif pro_tree.item(pro_tree.focus())["values"][1] == 'Noninventory':
                            pro_frame.grid_forget()
                            pro_frame_edit_2 = Frame(tab3_4)
                            pro_frame_edit_2.grid(row=0,column=0,sticky='nsew')

                            def pro_responsive_widgets_e3(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("neppoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("neplabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("nephline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.29


                                dcanvas.coords("neppoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                r2 = 25
                                x11 = dwidth/24
                                x21 = dwidth/1.050
                                y11 = dheight/2.1
                                y21 = dheight/1.35


                                dcanvas.coords("neppoly3",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("neplabel2",dwidth/2.4,dheight/1.77)
                                dcanvas.coords("nepbutton1",dwidth/1.8,dheight/1.77)

                                dcanvas.coords("neplabel3",dwidth/23.2,dheight/1.23)
                                dcanvas.coords("neplabel4",dwidth/23.3,dheight/1.02)
                                dcanvas.coords("neplabel5",dwidth/1.9,dheight/1.02)
                                dcanvas.coords("neplabel6",dwidth/1.9,dheight/0.92)
                                dcanvas.coords("neplabel7",dwidth/27,dheight/0.865)
                                dcanvas.coords("neplabel8",dwidth/1.915,dheight/0.865)
                                dcanvas.coords("neplabel12",dwidth/26,dheight/0.675)
                                dcanvas.coords("neplabel13",dwidth/26.8,dheight/0.606)
                                dcanvas.coords("neplabel14",dwidth/28.3,dheight/0.538)
                                dcanvas.coords("neplabel15",dwidth/1.9,dheight/0.538)
                                dcanvas.coords("neplabel16",dwidth/28.4,dheight/0.485)
                                dcanvas.coords("neplabel17",dwidth/50,dheight/0.438)
                                dcanvas.coords("neplabel18",dwidth/26,dheight/0.420)
                                dcanvas.coords("neplabel20",dwidth/28,dheight/0.368)
                                dcanvas.coords("neplabel21",dwidth/2.6,dheight/0.368)
                                dcanvas.coords("neplabel22",dwidth/1.5,dheight/0.368)

                                dcanvas.coords("neplabel9",dwidth/23.2,dheight/0.392)
                                dcanvas.coords("neplabel10",dwidth/1.9,dheight/0.392)


                                dcanvas.coords("nepentry1",dwidth/23.2,dheight/1.165)
                                dcanvas.coords("nepentry2",dwidth/23.2,dheight/0.975)
                                dcanvas.coords("nepentry3",dwidth/1.9,dheight/0.975)
                                dcanvas.coords("nepentry4",dwidth/1.9,dheight/0.83)
                                dcanvas.coords("nepentry7",dwidth/23.2,dheight/0.59)
                                dcanvas.coords("nepentry8",dwidth/23.2,dheight/0.525)
                                dcanvas.coords("nepentry9",dwidth/23.2,dheight/0.43)
                                dcanvas.coords("nepentry10",dwidth/23.2,dheight/0.412)
                                dcanvas.coords("nepentry11",dwidth/2.6,dheight/0.362)

                                dcanvas.coords("nepcentry2",dwidth/23.2,dheight/0.385)
                                dcanvas.coords("nepcentry3",dwidth/1.9,dheight/0.385)

                                dcanvas.coords("nepcombo1",dwidth/23.2,dheight/0.83)
                                dcanvas.coords("nepcombo3",dwidth/1.9,dheight/0.525)
                                dcanvas.coords("nepcombo4",dwidth/23.2,dheight/0.474)
                                dcanvas.coords("nepcombo6",dwidth/23.2,dheight/0.362)
                                dcanvas.coords("nepcombo7",dwidth/1.5,dheight/0.362)

                                dcanvas.coords("nepbutton2",dwidth/23.2,dheight/0.654)
                                dcanvas.coords("nepbutton3",dwidth/2.45,dheight/0.474)
                                dcanvas.coords("nepbutton4",dwidth/3.37,dheight/0.362)
                                dcanvas.coords("nepbutton5",dwidth/2.38,dheight/0.345)

                                dcanvas.coords("nepcbutton1",dwidth/23.2,dheight/0.51)
                                dcanvas.coords("nepcbutton2",dwidth/23.2,dheight/0.378)

                                dcanvas.coords("nepline1",dwidth/21,dheight/0.73,dwidth/1.055,dheight/0.73)
                                dcanvas.coords("nephline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)

                                dcanvas.coords("nepbuttn1",dwidth/23,dheight/3.415)

                                

                            p_canvas_edit_2=Canvas(pro_frame_edit_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_edit_2.grid_columnconfigure(0,weight=1)
                            pro_frame_edit_2.grid_rowconfigure(0,weight=1)
                        
                            vertibar=Scrollbar(pro_frame_edit_2, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_edit_2.yview)

                            p_canvas_edit_2.bind("<Configure>", pro_responsive_widgets_e3)
                            p_canvas_edit_2.config(yscrollcommand=vertibar.set)
                            p_canvas_edit_2.grid(row=0,column=0,sticky='nsew')

                            non_peditid = pro_tree.item(pro_tree.focus())["values"][2]
                            print(non_peditid)

                            non_peditid_1 = pro_tree.item(pro_tree.focus())["values"][3]
                            print(non_peditid_1)

                            sql_pn="select * from auth_user where username=%s"
                            pn_val=(nm_ent.get(),)
                            fbcursor.execute(sql_pn,pn_val,)
                            pn_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pn_dtl[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dtln=fbcursor.fetchone()
                            print(cmp_dtln)

                            sql = 'select * from app1_noninventory where name = %s and sku = %s and cid_id = %s'
                            val =  (non_peditid,non_peditid_1,cmp_dtln[0],)
                            fbcursor.execute(sql,val)
                            edit_pnon = fbcursor.fetchone()

                            def edit_new_pro_non():
                                name = edit_non_item_1.get()
                                sku = edit_non_iitem_2.get()
                                hsn = edit_non_item_2.get()
                                unit = comb_enon_item_1.get()
                                category = edit_non_item_3.get()
                                descr = edit_non_item_7.get('1.0', 'end-1c')
                                saleprice = edit_non_item_8.get()
                                income = comb_enon_item_4.get()
                                tax = comb_enon_item_3.get()
                                purchasedescr = edit_non_item_9.get('1.0', 'end-1c')
                                cost = edit_non_item_10.get()
                                expenseaccount = comb_enon_item_6.get()
                                purchasetax = comb_enon_item_5.get()
                                revcharge = edit_non_item_11.get()
                                presupplier = comb_enon_item_7.get()

                                usrp1_sql = "SELECT id FROM auth_user WHERE username=%s"
                                usrp1_val = (nm_ent.get(),)
                                fbcursor.execute(usrp1_sql,usrp1_val)
                                usrp1_data = fbcursor.fetchone()

                                cmpp1_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                cmpp1_val = (usrp1_data[0],)
                                fbcursor.execute(cmpp1_sql,cmpp1_val)
                                cmpp1_data = fbcursor.fetchone()
                                cid = cmpp1_data[0]

                                n_p_sql = "UPDATE app1_noninventory set name=%s,sku=%s,hsn=%s,unit=%s,category=%s,descr=%s,saleprice=%s,income=%s,tax=%s,purchasedescr=%s,cost=%s,expenseaccount=%s,purchasetax=%s,revcharge=%s,presupplier=%s,cid_id=%s where name=%s and sku = %s"
                                n_p_val = (name,sku,hsn,unit,category,descr,saleprice,income,tax,purchasedescr,cost,expenseaccount,purchasetax,revcharge,presupplier,cid,non_peditid,non_peditid_1)
                                fbcursor.execute(n_p_sql,n_p_val)
                                finsysdb.commit()

                                #_________Refresh insert tree________#

                                for record in pro_tree.get_children():
                                    pro_tree.delete(record)

        
                                sql_p="select * from auth_user where username=%s"
                                sql_p_val=(nm_ent.get(),)
                                fbcursor.execute(sql_p,sql_p_val,)
                                pr_dt=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dt[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dt=fbcursor.fetchone()

                                p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                                p_val_1 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_1,p_val_1,)
                                p_data_1 = fbcursor.fetchall()
                                
                                count0 = 0
                                for i in p_data_1:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                    else:
                                        pass
                                count0 += 1

                                p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                                p_val_2 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_2,p_val_2,)
                                p_data_2 = fbcursor.fetchall()

                                count1 = 0
                                for i in p_data_2:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count1 += 1

                                p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                                p_val_3 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_3,p_val_3,)
                                p_data_3 = fbcursor.fetchall()
                                

                                count2 = 0
                                for i in p_data_3:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count2 += 1

                                p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                                p_val_4 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_4,p_val_4,)
                                p_data_4 = fbcursor.fetchall()
                                

                                count3 = 0
                                for i in p_data_4:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                    else:
                                        pass
                                count3 += 1

                                pro_frame_edit_2.destroy()
                                pro_frame.grid(row=0,column=0,sticky='nsew')

                            p_canvas_edit_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('neppoly1'))

                            label_1 = Label(p_canvas_edit_2,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1, tags=('neplabel1'))

                            p_canvas_edit_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iephline'))

                            p_canvas_edit_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('neppoly2'))

                            p_canvas_edit_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('neppoly3'))

                            label_1 = Label(p_canvas_edit_2,width=13,height=2,text="NONINVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1, tags=('neplabel2'))

                            label_1 = Label(p_canvas_edit_2,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1, tags=('neplabel3'))

                            edit_non_item_1=Entry(p_canvas_edit_2,width=200,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_non_item_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_1, tags=('nepentry1'))
                            edit_non_item_1.delete(0,'end')
                            edit_non_item_1.insert(0, edit_pnon[2])

                            label_1 = Label(p_canvas_edit_2,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1, tags=('neplabel4'))

                            def pns_2(event):
                                if edit_non_iitem_2.get()==edit_pnon[3]:
                                    edit_non_iitem_2.delete(0,END)
                                else:
                                    pass

                            edit_non_iitem_2=Entry(p_canvas_edit_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_non_iitem_2 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_iitem_2, tags=('nepentry2'))
                            edit_non_iitem_2.insert(0,"N41554")
                            edit_non_iitem_2.bind("<Button-1>",pns_2)
                            edit_non_iitem_2.delete(0,'end')
                            edit_non_iitem_2.insert(0, edit_pnon[3])

                            label_1 = Label(p_canvas_edit_2,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1, tags=('neplabel5'))

                            edit_non_item_2=Entry(p_canvas_edit_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_non_item_2 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_2, tags=('nepentry3'))
                            edit_non_item_2.delete(0,'end')
                            edit_non_item_2.insert(0, edit_pnon[4])

                            #Define a callback function
                            def ncallback_1(url):
                                webbrowser.open_new_tab(url)

                            link_2 = Label(p_canvas_edit_2,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
                            window_link_2 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=link_2, tags=('neplabel6'))
                            link_2.bind("<Button-1>", lambda e:
                            ncallback_1("https://gstcouncil.gov.in/sites/default/files/goods-rates-booklet-03July2017.pdf"))


                            label_1 = Label(p_canvas_edit_2,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1, tags=('neplabel7'))

                            comb_enon_item_1 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                            comb_enon_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards","OTH Others",)
                            comb_enon_item_1.current(0)
                            window_comb_enon_item_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_enon_item_1, tags=('nepcombo1'))
                            comb_enon_item_1.delete(0,'end')
                            comb_enon_item_1.insert(0, edit_pnon[5])
                            

                            label_1 = Label(p_canvas_edit_2,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel8'))

                            edit_non_item_3=Entry(p_canvas_edit_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_inv_item_3 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_3,tags=('nepentry4'))
                            edit_non_item_3.delete(0,'end')
                            edit_non_item_3.insert(0, edit_pnon[6])

                            p_canvas_edit_2.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('nepline1'))

                            label_1 = Label(p_canvas_edit_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel12'))


                            def d_enon_check():

                                if chk_str_enon_item.get() == True:
                                    p_canvas_edit_2.itemconfig('neplabel13',state='normal')
                                    p_canvas_edit_2.itemconfig('nepentry7',state='normal')
                                    p_canvas_edit_2.itemconfig('neplabel14',state='normal')
                                    p_canvas_edit_2.itemconfig('nepentry8',state='normal')
                                    p_canvas_edit_2.itemconfig('nepcbutton1',state='normal')
                                    p_canvas_edit_2.itemconfig('neplabel15',state='normal')
                                    p_canvas_edit_2.itemconfig('nepcombo3',state='normal')
                                    p_canvas_edit_2.itemconfig('neplabel16',state='normal')
                                    p_canvas_edit_2.itemconfig('nepcombo4',state='normal')
                                    p_canvas_edit_2.itemconfig('nepbutton3',state='normal')
                                else:
                                    pass                     


                            chk_str_enon_item = BooleanVar()
                            chkbtn_enon_item = Checkbutton(p_canvas_edit_2, text = "I sell this product/service to my customers.", variable = chk_str_enon_item, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=d_enon_check)
                            window_chkbtn_enon_item = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=chkbtn_enon_item,tags=('nepbutton2'))

                            label_1 = Label(p_canvas_edit_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel13'),state=HIDDEN)
                            

                            edit_non_item_7=scrolledtext.ScrolledText(p_canvas_edit_2,width=145,background='#2f516f',foreground="white")
                            window_edit_non_item_7 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=60,window=edit_non_item_7,tags=('nepentry7'),state=HIDDEN)
                            edit_non_item_7.insert(1.0,edit_pnon[7])

                            label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel14'),state=HIDDEN)
                            
                            edit_non_item_8=Entry(p_canvas_edit_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_non_item_8 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_8,tags=('nepentry8'),state=HIDDEN)
                            edit_non_item_8.delete(0,'end')
                            edit_non_item_8.insert(0, edit_pnon[8])

                            chk_str_non_item_e1 = BooleanVar()
                            chkbtn_non_item_e1 = Checkbutton(p_canvas_edit_2, text = "Inclusive of tax", variable = chk_str_non_item_e1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            chkbtn_non_item_e1.select()
                            window_chkbtn_non_item_e1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=chkbtn_non_item_e1,tags=('nepcbutton1'),state=HIDDEN)

                            label_1 = Label(p_canvas_edit_2,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel15'),state=HIDDEN)

                            comb_enon_item_3 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                            comb_enon_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                            #comb_non_item_3.current(0)
                            window_comb_enon_item_3 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_enon_item_3,tags=('nepcombo3'),state=HIDDEN)
                            comb_enon_item_3.delete(0,'end')
                            comb_enon_item_3.insert(0, edit_pnon[10])

                            label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel16'),state=HIDDEN)

                            comb_enon_item_4 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                            comb_enon_item_4['values'] = ("Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discount","Sales of Product Income","Services","Unapplied Cash Payment Income","Uncategorised Income",)
                            #comb_non_item_4.current(0)
                            window_comb_enon_item_4 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_enon_item_4,tags=('nepcombo4'),state=HIDDEN)
                            comb_enon_item_4.delete(0,'end')
                            comb_enon_item_4.insert(0, edit_pnon[9])

                            p_canvas_edit_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('nephline1'))

                            label_1 = Label(p_canvas_edit_2,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(26, 1300, anchor="nw", window=label_1,tags=('neplabel17'))

                            def p_enon_check():
                                
                                if chk_str_enon_pitem.get() == True:
                                    p_canvas_edit_2.itemconfig('neplabel18',state='normal')
                                    p_canvas_edit_2.itemconfig('nepentry10',state='normal')
                                    p_canvas_edit_2.itemconfig('neplabel9',state='normal')
                                    p_canvas_edit_2.itemconfig('nepcentry2',state='normal')
                                    p_canvas_edit_2.itemconfig('nepcbutton2',state='normal')
                                    p_canvas_edit_2.itemconfig('neplabel10',state='normal')
                                    p_canvas_edit_2.itemconfig('nepcentry3',state='normal')
                                    p_canvas_edit_2.itemconfig('neplabel20',state='normal')
                                    p_canvas_edit_2.itemconfig('nepcombo6',state='normal')
                                    p_canvas_edit_2.itemconfig('nepbutton4',state='normal')
                                    p_canvas_edit_2.itemconfig('neplabel21',state='normal')
                                    p_canvas_edit_2.itemconfig('nepentry11',state='normal')
                                    p_canvas_edit_2.itemconfig('neplabel22',state='normal')
                                    p_canvas_edit_2.itemconfig('nepcombo7',state='normal')
                                else:
                                    pass

                            chk_str_enon_pitem = BooleanVar()
                            chkbtn_enon_pitem = Checkbutton(p_canvas_edit_2, text = "I Purchase this product/service from Supplier.", variable = chk_str_enon_pitem, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=p_enon_check)
                            window_chkbtn_enon_pitem = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=chkbtn_enon_pitem,tags=('nepentry9'))


                            label_1 = Label(p_canvas_edit_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel18'),state=HIDDEN)

                            edit_non_item_9=scrolledtext.ScrolledText(p_canvas_edit_2,width=145,background='#2f516f',foreground="white")
                            window_edit_non_item_9 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=60,window=edit_non_item_9,tags=('nepentry10'),state=HIDDEN)
                            edit_non_item_9.insert(1.0,edit_pnon[11])

                            label_1 = Label(p_canvas_edit_2,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel9'),state=HIDDEN)
                            
                            edit_non_item_10=Entry(p_canvas_edit_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_non_item_10 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_10,tags=('nepcentry2'),state=HIDDEN)
                            edit_non_item_10.delete(0,'end')
                            edit_non_item_10.insert(0, edit_pnon[12])

                            chk_str_enon_item_2 = BooleanVar()
                            chkbtn_enon_item_2 = Checkbutton(p_canvas_edit_2, text = "Inclusive of purchase tax", variable = chk_str_enon_item_2, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            chkbtn_enon_item_2.select()
                            window_chkbtn_enon_item_2 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=chkbtn_enon_item_2,tags=('nepcbutton2'),state=HIDDEN)

                            label_1 = Label(p_canvas_edit_2,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel10'),state=HIDDEN)

                            comb_enon_item_5 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                            comb_enon_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                            #comb_non_item_5.current(0)
                            window_comb_enon_item_5 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_enon_item_5,tags=('nepcentry3'),state=HIDDEN)
                            comb_enon_item_5.delete(0,'end')
                            comb_enon_item_5.insert(0, edit_pnon[14])

                            label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel20'),state=HIDDEN)

                            comb_enon_item_6 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                            comb_enon_item_6['values'] = ("Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities",)
                            #comb_non_item_6.current(0)
                            window_comb_enon_item_6 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_enon_item_6,tags=('nepcombo6'),state=HIDDEN)
                            comb_enon_item_6.delete(0,'end')
                            comb_enon_item_6.insert(0, edit_pnon[13])


                            label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel21'),state=HIDDEN)

                            def pr_e2(event):
                                if edit_non_item_11.get()==edit_pnon[15]:
                                    edit_non_item_11.delete(0,END)
                                else:
                                    pass

                            edit_non_item_11=Entry(p_canvas_edit_2,width=50,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_non_item_11 = p_canvas_edit_2.create_window(0, 0, anchor="nw", height=30,window=edit_non_item_11,tags=('nepentry11'),state=HIDDEN)
                            edit_non_item_11.insert(0,"0")
                            edit_non_item_11.bind("<Button-1>",pr_e2)
                            edit_non_item_11.delete(0,'end')
                            edit_non_item_11.insert(0, edit_pnon[15])


                            label_1 = Label(p_canvas_edit_2,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=label_1,tags=('neplabel22'),state=HIDDEN)

                            comb_enon_item_7 = ttk.Combobox(p_canvas_edit_2, font=('arial 10'))
                            comb_enon_item_7['values'] = ("Select Supplier",)
                            #comb_non_item_7.current(0)
                            window_comb_enon_item_7 = p_canvas_edit_2.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_enon_item_7,tags=('nepcombo7'),state=HIDDEN)
                            comb_enon_item_7.delete(0,'end')
                            comb_enon_item_7.insert(0, edit_pnon[16])

                            enon_sub_btn1=Button(p_canvas_edit_2,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=edit_new_pro_non)
                            window_enon_sub_btn1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=enon_sub_btn1,tags=('nepbutton5'))

                            def no_eback_1_():
                                pro_frame_edit_2.grid_forget()
                                pro_frame.grid(row=0,column=0,sticky='nsew')

                            bck_enbtn1=Button(p_canvas_edit_2,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=no_eback_1_)
                            window_bck_enbtn1 = p_canvas_edit_2.create_window(0, 0, anchor="nw", window=bck_enbtn1,tags=('nepbuttn1'))
                        
                        elif pro_tree.item(pro_tree.focus())["values"][1] == 'Service':
                            pro_frame.grid_forget()
                            pro_frame_edit_3 = Frame(tab3_4)
                            pro_frame_edit_3.grid(row=0,column=0,sticky='nsew')

                            def pro_responsive_widgets_e4(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("sppoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("splabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("sphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.29


                                dcanvas.coords("sppoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                r2 = 25
                                x11 = dwidth/24
                                x21 = dwidth/1.050
                                y11 = dheight/2.1
                                y21 = dheight/1.35


                                dcanvas.coords("sppoly3",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("seplabel2",dwidth/2.3,dheight/1.77)
                                dcanvas.coords("sepbutton1",dwidth/1.8,dheight/1.77)

                                dcanvas.coords("seplabel3",dwidth/23.2,dheight/1.23)
                                dcanvas.coords("seplabel4",dwidth/23.3,dheight/1.02)
                                dcanvas.coords("seplabel5",dwidth/1.9,dheight/1.02)
                                dcanvas.coords("seplabel7",dwidth/27,dheight/0.865)
                                dcanvas.coords("seplabel8",dwidth/1.915,dheight/0.865)
                                dcanvas.coords("seplabel12",dwidth/26,dheight/0.675)
                                dcanvas.coords("seplabel13",dwidth/26.8,dheight/0.606)
                                dcanvas.coords("seplabel14",dwidth/28.3,dheight/0.538)
                                dcanvas.coords("seplabel15",dwidth/1.9,dheight/0.538)
                                dcanvas.coords("seplabel16",dwidth/28.4,dheight/0.485)
                                dcanvas.coords("seplabel17",dwidth/50,dheight/0.438)
                                dcanvas.coords("seplabel18",dwidth/26,dheight/0.420)
                                dcanvas.coords("seplabel9",dwidth/23.2,dheight/0.392)
                                dcanvas.coords("seplabel10",dwidth/1.9,dheight/0.392)
                                dcanvas.coords("seplabel20",dwidth/28,dheight/0.368)
                                dcanvas.coords("seplabel21",dwidth/2.6,dheight/0.368)
                                dcanvas.coords("seplabel22",dwidth/1.5,dheight/0.368)

                                dcanvas.coords("seplabel23",dwidth/2.6,dheight/0.485)

                                dcanvas.coords("seplabel24",dwidth/1.53,dheight/0.485)
                                

                                dcanvas.coords("sepentry1",dwidth/23.2,dheight/1.165)
                                dcanvas.coords("sepentry2",dwidth/23.2,dheight/0.975)
                                dcanvas.coords("sepentry3",dwidth/1.9,dheight/0.975)
                                dcanvas.coords("sepentry4",dwidth/1.9,dheight/0.83)
                                dcanvas.coords("sepentry7",dwidth/23.2,dheight/0.59)
                                dcanvas.coords("sepentry8",dwidth/23.2,dheight/0.525)
                                dcanvas.coords("sepentry9",dwidth/23.2,dheight/0.43)
                                dcanvas.coords("sepentry10",dwidth/23.2,dheight/0.412)
                                dcanvas.coords("sepentry11",dwidth/2.6,dheight/0.362)

                                dcanvas.coords("sepentry12",dwidth/2.6,dheight/0.474)

                                dcanvas.coords("sepcentry2",dwidth/23.2,dheight/0.385)
                                dcanvas.coords("sepcentry3",dwidth/1.9,dheight/0.385)

                                dcanvas.coords("sepcombo1",dwidth/23.2,dheight/0.83)
                                dcanvas.coords("sepcombo3",dwidth/1.9,dheight/0.525)
                                dcanvas.coords("sepcombo4",dwidth/23.2,dheight/0.474)
                                dcanvas.coords("sepcombo6",dwidth/23.2,dheight/0.362)
                                dcanvas.coords("sepcombo7",dwidth/1.5,dheight/0.362)

                                dcanvas.coords("sepcombo8",dwidth/1.5,dheight/0.474)

                                dcanvas.coords("sepbutton2",dwidth/23.2,dheight/0.654)
                                dcanvas.coords("sepbutton3",dwidth/3.37,dheight/0.474)
                                dcanvas.coords("sepbutton4",dwidth/3.37,dheight/0.362)
                                dcanvas.coords("sepbutton5",dwidth/2.38,dheight/0.345)

                                dcanvas.coords("sepcbutton1",dwidth/23.2,dheight/0.51)
                                dcanvas.coords("sepcbutton2",dwidth/23.2,dheight/0.378)

                                dcanvas.coords("sepline1",dwidth/21,dheight/0.73,dwidth/1.055,dheight/0.73)

                                dcanvas.coords("sephline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)
                                dcanvas.coords("sepbuttn1",dwidth/23,dheight/3.415) 

                                

                            p_canvas_edit_3=Canvas(pro_frame_edit_3, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_edit_3.grid_columnconfigure(0,weight=1)
                            pro_frame_edit_3.grid_rowconfigure(0,weight=1)
                        
                            vertibar=Scrollbar(pro_frame_edit_3, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=p_canvas_edit_3.yview)

                            p_canvas_edit_3.bind("<Configure>", pro_responsive_widgets_e4)
                            p_canvas_edit_3.config(yscrollcommand=vertibar.set)
                            p_canvas_edit_3.grid(row=0,column=0,sticky='nsew')

                            ser_peditid = pro_tree.item(pro_tree.focus())["values"][2]
                            print(ser_peditid)

                            ser_peditid_1 = pro_tree.item(pro_tree.focus())["values"][3]
                            print(ser_peditid_1)

                            sql_pn="select * from auth_user where username=%s"
                            pn_val=(nm_ent.get(),)
                            fbcursor.execute(sql_pn,pn_val,)
                            pn_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pn_dtl[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dtln=fbcursor.fetchone()
                            print(cmp_dtln)

                            sql = 'select * from app1_service where name = %s and sku = %s and cid_id = %s'
                            val =  (ser_peditid,ser_peditid_1,cmp_dtln[0],)
                            fbcursor.execute(sql,val)
                            edit_pser = fbcursor.fetchone()

                            def edit_new_pro_ser():
                                name = edit_ser_item_1.get()
                                sku = edit_ser_iitem_2.get()
                                sac = edit_ser_item_2.get()
                                unit = comb_eser_item_1.get()
                                categ = edit_ser_item_3.get()
                                descr = edit_ser_item_7.get('1.0', 'end-1c')
                                saleprice = edit_ser_item_s8.get()
                                income = comb_eser_item_6.get()
                                tax = comb_eser_item_3.get()
                                abatement = edit_ser_iitem_11.get()
                                sertype = comb_eser_iitem_7.get()
                                purchasedescr = edit_ser_item_9.get('1.0', 'end-1c')
                                cost = edit_ser_item_10.get()
                                expenseaccount = comb_eser_item_e6.get()
                                purchasetax = comb_eser_item_5.get()
                                revcharge = edit_sser_item_11.get()
                                presupplier = comb_eser_item_ps7.get()

                                usrp2_sql = "SELECT id FROM auth_user WHERE username=%s"
                                usrp2_val = (nm_ent.get(),)
                                fbcursor.execute(usrp2_sql,usrp2_val)
                                usrp2_data = fbcursor.fetchone()

                                cmpp2_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                cmpp2_val = (usrp2_data[0],)
                                fbcursor.execute(cmpp2_sql,cmpp2_val)
                                cmpp2_data = fbcursor.fetchone()
                                cid = cmpp2_data[0]

                                s_p_sql = "UPDATE app1_service set name=%s,sku=%s,sac=%s,unit=%s,categ=%s,descr=%s,saleprice=%s,income=%s,tax=%s,abatement=%s,sertype=%s,purchasedescr=%s,cost=%s,expenseaccount=%s,purchasetax=%s,revcharge=%s,presupplier=%s,cid_id=%s where name=%s and sku = %s"
                                s_p_val = (name,sku,sac,unit,categ,descr,saleprice,income,tax,abatement,sertype,purchasedescr,cost,expenseaccount,purchasetax,revcharge,presupplier,cid,ser_peditid,ser_peditid_1)
                                fbcursor.execute(s_p_sql,s_p_val)
                                finsysdb.commit()

                                #_________Refresh insert tree________#

                                for record in pro_tree.get_children():
                                    pro_tree.delete(record)

        
                                sql_p="select * from auth_user where username=%s"
                                sql_p_val=(nm_ent.get(),)
                                fbcursor.execute(sql_p,sql_p_val,)
                                pr_dt=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dt[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dt=fbcursor.fetchone()

                                p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                                p_val_1 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_1,p_val_1,)
                                p_data_1 = fbcursor.fetchall()
                                
                                count0 = 0
                                for i in p_data_1:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                    else:
                                        pass
                                count0 += 1

                                p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                                p_val_2 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_2,p_val_2,)
                                p_data_2 = fbcursor.fetchall()

                                count1 = 0
                                for i in p_data_2:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count1 += 1

                                p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                                p_val_3 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_3,p_val_3,)
                                p_data_3 = fbcursor.fetchall()
                                

                                count2 = 0
                                for i in p_data_3:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count2 += 1

                                p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                                p_val_4 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_4,p_val_4,)
                                p_data_4 = fbcursor.fetchall()
                                

                                count3 = 0
                                for i in p_data_4:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                    else:
                                        pass
                                count3 += 1

                                pro_frame_edit_3.destroy()
                                pro_frame.grid(row=0,column=0,sticky='nsew')

                            p_canvas_edit_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sppoly1'))

                            label_1 = Label(p_canvas_edit_3,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1, tags=('splabel1'))

                            p_canvas_edit_3.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('sphline'))

                            p_canvas_edit_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('sppoly2'))

                            p_canvas_edit_3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('sppoly3'))

                            label_1 = Label(p_canvas_edit_3,width=10,height=2,text="SERVICE", font=('arial 20'),background="#2f516f",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1, tags=('seplabel2'))

                            label_1 = Label(p_canvas_edit_3,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1, tags=('seplabel3'))

                            edit_ser_item_1=Entry(p_canvas_edit_3,width=200,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_ser_item_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_item_1, tags=('sepentry1'))
                            edit_ser_item_1.delete(0,'end')
                            edit_ser_item_1.insert(0, edit_pser[2])

                            label_1 = Label(p_canvas_edit_3,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1, tags=('seplabel4'))

                            def pse_3(event):
                                if edit_ser_iitem_2.get()=="N41554":
                                    edit_ser_iitem_2.delete(0,END)
                                else:
                                    pass

                            edit_ser_iitem_2=Entry(p_canvas_edit_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_ser_iitem_2 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_iitem_2, tags=('sepentry2'))
                            edit_ser_iitem_2.insert(0,"N41554")
                            edit_ser_iitem_2.bind("<Button-1>",pse_3)
                            edit_ser_iitem_2.delete(0,'end')
                            edit_ser_iitem_2.insert(0, edit_pser[3])

                            label_1 = Label(p_canvas_edit_3,width=9,height=1,text="SAC Code", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1, tags=('seplabel5'))

                            def p_sac_e1(event):
                                if edit_ser_item_2.get()==edit_pser[4]:
                                    edit_ser_item_2.delete(0,END)
                                else:
                                    pass
                            edit_ser_item_2=Entry(p_canvas_edit_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_ser_item_2 = p_canvas_edit_3.create_window(710, 630, anchor="nw", height=30,window=edit_ser_item_2, tags=('sepentry3'))
                            edit_ser_item_2.insert(0,"Eg: 998841-Coke and refined petroleum product manufacturing services")
                            edit_ser_item_2.bind("<Button-1>",p_sac_e1)
                            edit_ser_item_2.delete(0,'end')
                            edit_ser_item_2.insert(0, edit_pser[4])


                            label_1 = Label(p_canvas_edit_3,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1, tags=('seplabel7'))

                            comb_eser_item_1 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                            comb_eser_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG-BAGS","BAL-BALE","BDL-BUNDLES","BKL-BUCKLES","BOX-BOX","BOU-BILLIONS OF UNITS","BTL-BOTTLES","BUN-BUNCHES","CAN-CANS","CBM-CUBIC METER","CMS-CENTIMETER","CCM-CUBIC CENTIMETER","CTN-CARTONS","DOZ-DOZEN","DRM-DRUM","GGR-GREAT GROSS","GMS-GRAMS","GRS-GROSS","GYD-GRODD YARDS","KGS-KILOGRAMS","KLR-KILOLITER","KME-KILOMETRE","MTS-METRIC TON","MLT-MILLILITRE","MTR-METERS","NOS-NUMBER","PAC-PACKS","PCS-PIECES","PRS-PAIRS","QTL-QUINTAL","ROL-ROLLS","SQF-SQUARE FEET","SET-SETS","SQM-SQUARE METERS","SQY-SQUARE YARDS","TBS-TABLETS","TGM-TEN GROSS","THD-THOUSAND","TON-TONNES","TUB-TUBES","UGS-US GALLONS","UNT-UNITS","YDS-YARDS","OTH-OTHERS",)
                            comb_eser_item_1.current(0)
                            window_comb_eser_item_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_eser_item_1, tags=('sepcombo1'))
                            comb_eser_item_1.delete(0,'end')
                            comb_eser_item_1.insert(0, edit_pser[5])

                            label_1 = Label(p_canvas_edit_3,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(705, 710, anchor="nw", window=label_1,tags=('seplabel8'))

                            edit_ser_item_3=Entry(p_canvas_edit_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_ser_item_3 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_item_3,tags=('sepentry4'))
                            edit_ser_item_3.delete(0,'end')
                            edit_ser_item_3.insert(0, edit_pser[6])

                            p_canvas_edit_3.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('sepline1'))


                            label_1 = Label(p_canvas_edit_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel12'))

                            def d_eser_check():

                                if chk_str_eser_item.get() == True:
                                    p_canvas_edit_3.itemconfig('seplabel13',state='normal')
                                    p_canvas_edit_3.itemconfig('sepentry7',state='normal')
                                    p_canvas_edit_3.itemconfig('seplabel14',state='normal')
                                    p_canvas_edit_3.itemconfig('sepentry8',state='normal')
                                    p_canvas_edit_3.itemconfig('sepcbutton1',state='normal')
                                    p_canvas_edit_3.itemconfig('seplabel15',state='normal')
                                    p_canvas_edit_3.itemconfig('sepcombo3',state='normal')
                                    p_canvas_edit_3.itemconfig('seplabel16',state='normal')
                                    p_canvas_edit_3.itemconfig('sepcombo4',state='normal')
                                    p_canvas_edit_3.itemconfig('sepbutton3',state='normal')
                                    p_canvas_edit_3.itemconfig('seplabel23',state='normal')
                                    p_canvas_edit_3.itemconfig('sepentry12',state='normal')
                                    p_canvas_edit_3.itemconfig('seplabel24',state='normal')
                                    p_canvas_edit_3.itemconfig('sepcombo8',state='normal')
                                else:
                                    pass

                            chk_str_eser_item = BooleanVar()
                            chkbtn_eser_item = Checkbutton(p_canvas_edit_3, text = "I sell this product/service to my customers.", variable = chk_str_eser_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=d_eser_check)
                            window_chkbtn_eser_item = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=chkbtn_eser_item,tags=('sepbutton2'))

                            label_d1 = Label(p_canvas_edit_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_d1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_d1,tags=('seplabel13'),state=HIDDEN)

                            edit_ser_item_7=scrolledtext.ScrolledText(p_canvas_edit_3,width=145,background='#2f516f',foreground="white")
                            window_edit_ser_item_7 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=60,window=edit_ser_item_7,tags=('sepentry7'),state=HIDDEN)
                            edit_ser_item_7.insert(1.0,edit_pser[7])


                            label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel14'),state=HIDDEN)
                            
                            edit_ser_item_s8=Entry(p_canvas_edit_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_ser_item_s8 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_item_s8,tags=('sepentry8'),state=HIDDEN)
                            edit_ser_item_s8.delete(0,'end')
                            edit_ser_item_s8.insert(0, edit_pser[8])

                            chk_str_eser_item_1 = BooleanVar()
                            chkbtn_eser_item_1 = Checkbutton(p_canvas_edit_3, text = "Inclusive of tax", variable = chk_str_eser_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            chkbtn_eser_item_1.select()
                            window_chkbtn_eser_item_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=chkbtn_eser_item_1,tags=('sepcbutton1'),state=HIDDEN)

                            label_1 = Label(p_canvas_edit_3,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel15'),state=HIDDEN)

                            comb_eser_item_3 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                            comb_eser_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                            comb_eser_item_3.current(0)
                            window_comb_eser_item_3 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_eser_item_3,tags=('sepcombo3'),state=HIDDEN)
                            comb_eser_item_3.delete(0,'end')
                            comb_eser_item_3.insert(0, edit_pser[10])

                            label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel16'),state=HIDDEN)

                            
                            comb_eser_item_6 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                            comb_eser_item_6['values'] = ("Choose...","Billable Expense income","Product Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discounts","Sales of Product Income","Cost of sales","Equipment Rental for Jobs","Uncategorised Income","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Depreciation Expense","Dues and Subscriptions","Housekeeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Internet Expenses","Meals and Enetrtainments","Office Suppliers","Postage and Delivery","Printing and Reprooduction","Professional Fees","Purchases","Rent Expense","Repair and Maintananace","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities","Finance charge Income","Insurance Proceeds Received","Interest Income","Proceeds From Sale os Assets","Shipping and delivery Income","Ask My Accountant","CGST Write-off","GST Write-off","IGST Write-off","Miscellaneous Expense","Political Contributions","Reconcilation Discrepancies","SGST Write-off","Vehicles","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi kalyan Cess","Input Krishi kalyan Cess RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Krishi Kalyan Cess Payable","Input VAT 5%","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output SGST Tax RCM","Output Service Tax","Output Service Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","SGST Payable","Service Tax Payable","Srvice Tax Suspense","Swachh Barath Cess Payable","TDS Payable","VAT Payable","VAT Suspense","Deferred CGST","Deferred GST Input credit","Deferred IGST","Deferred SGST","Deferred Service Tax Input Credit","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Sevice Tax Refund","TDS Receivable","Uncategorised Asset","Undeposited Fund","Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and maintanance","Sales Discount","Sales of Product Income","Uncategorised Income","accumulated Depreciation","Building and Improvements","Furniture and Equipments","Land","Leasehold Improvements","Vehicles","Retained Earnings","Cost of Sales","Equipment Rental for Jobs","Freight and Shipping Costs","Merchant Account Fees","Purchases-Hardware for Resales","Purchases-Software for Resales","Subcontracted Services","Tools and Craft Suppliers",)
                            comb_eser_item_6.current(0)
                            window_comb_eser_item_6 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_eser_item_6,tags=('sepcombo4'),state=HIDDEN)
                            comb_eser_item_6.delete(0,'end')
                            comb_eser_item_6.insert(0, edit_pser[9])

                            label_1 = Label(p_canvas_edit_3,width=10,height=1,text="Abatement %", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel23'),state=HIDDEN)

                            def pa_e1(event):
                                if edit_ser_iitem_11.get()==edit_pser[11]:
                                    edit_ser_iitem_11.delete(0,END)
                                else:
                                    pass

                            edit_ser_iitem_11=Entry(p_canvas_edit_3,width=50,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_ser_iitem_11 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_iitem_11,tags=('sepentry12'),state=HIDDEN)
                            edit_ser_iitem_11.insert(0,"0")
                            edit_ser_iitem_11.bind("<Button-1>",pa_e1)
                            edit_ser_iitem_11.delete(0,'end')
                            edit_ser_iitem_11.insert(0, edit_pser[11])

                            label_1 = Label(p_canvas_edit_3,width=14,height=1,text="Service Type", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel24'),state=HIDDEN)

                            comb_eser_iitem_7 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                            comb_eser_iitem_7['values'] = ("Choose...","Stock Broking","Genral Insurance","Courier","Advertsing Agency","Consulting Engineer","Custom House Agent","Steamer Agent","Clearing and Forwarding","Man power Recruiting","Air Travel Agent","Tour operator","Rent a Cab","Architect","Interior Director","Management Consultment","Chartered Accountant","Cost Accountant","Company Scretary","Real Estate Agent","Security Agency","Credit Rating Agency","Market Research Agency","Underwriter","Beauty Parlor","Cargo Handling","Cable Operators","Dry Cleaning","Event Management","Fashion Designer","Life Insurance","Scientific and Technical Consultancy","Photography","Convention Services","Video Tape Production","Sound Recording","Broadcating","Insurance Auxilary Service","banking and Other Financial","Port Services","Authorised Service Station","Health Club and Fitness Centres","Rail Travel Agent","Storage and Warehousing","Business Auxilary","Commercial Coaching","Erection or Installation","Franchise Service","Internet Cafe","Maintanance or Repair","Technical Testing","Technical Inspection","Foreign Exchange Broking","Port","Airport Services","Air Transport","Business Exhibition","Goods Transport","Construction of Commerce Complex","Intellectual Property Service","Opinion Poll Service","Outdoor Catering","Television and Radio Program Production","Survey and Exploration of Minerals","Pandal and Shamiana","Travel Agent","Forward Contract Brokerage","Transport Through Pipeline","Site Preparation","Dredging","Survey and Map Making","Cleaning Service","Clubs and Association Service","Packaging Service","Mailing List Compilation","Residential Complex Construction","Share Transfer Agent","ATM Maintanance","Recovery Agent","Sale of Space for Advertisement","Sponsorship","International Air Travel","Containerised Rail Transport","Business Support Service","Action Service","Public Relation Management","Ship Management","Internet Telephony","Cruise Ship Tour","Credit Card","Telecommunication Service","Mining of Minerals, Oil or Gas","Recting Immovable Property","Works Contract","Development of Consent","Asset Management","Design Services","Information Technology Services","ULIP Management","Stock Exchange Service","Service for Transaction in Goods","Clearing House Services","Supply of Tangiable","Online Inforamtion Retrieval","Mandap keeper",)
                            comb_eser_iitem_7.current(0)
                            window_comb_eser_iitem_7 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_eser_iitem_7,tags=('sepcombo8'),state=HIDDEN)
                            comb_eser_iitem_7.delete(0,'end')
                            comb_eser_iitem_7.insert(0, edit_pser[12])

                            p_canvas_edit_3.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('sephline1'))

                            label_1 = Label(p_canvas_edit_3,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel17'))

                            def p_eser_check():

                                if chk_str_eser_pitem.get() == True:
                                    p_canvas_edit_3.itemconfig('seplabel18',state='normal')
                                    p_canvas_edit_3.itemconfig('sepentry10',state='normal')
                                    p_canvas_edit_3.itemconfig('seplabel9',state='normal')
                                    p_canvas_edit_3.itemconfig('sepcentry2',state='normal')
                                    p_canvas_edit_3.itemconfig('sepcbutton2',state='normal')
                                    p_canvas_edit_3.itemconfig('seplabel10',state='normal')
                                    p_canvas_edit_3.itemconfig('sepcentry3',state='normal')
                                    p_canvas_edit_3.itemconfig('seplabel20',state='normal')
                                    p_canvas_edit_3.itemconfig('sepcombo6',state='normal')
                                    p_canvas_edit_3.itemconfig('sepbutton4',state='normal')
                                    p_canvas_edit_3.itemconfig('seplabel21',state='normal')
                                    p_canvas_edit_3.itemconfig('sepentry11',state='normal')
                                    p_canvas_edit_3.itemconfig('seplabel22',state='normal')
                                    p_canvas_edit_3.itemconfig('sepcombo7',state='normal')
                                else:
                                    pass

                            chk_str_eser_pitem = BooleanVar()
                            chkbtn_eser_pitem = Checkbutton(p_canvas_edit_3, text = "I Purchase this product/service from Supplier.", variable = chk_str_eser_pitem, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f",command=p_eser_check)
                            window_chkbtn_eser_pitem = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=chkbtn_eser_pitem,tags=('sepentry9'))


                            label_1 = Label(p_canvas_edit_3,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel18'),state=HIDDEN)

                            edit_ser_item_9=scrolledtext.ScrolledText(p_canvas_edit_3,width=145,background='#2f516f',foreground="white")
                            window_edit_ser_item_9 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=60,window=edit_ser_item_9,tags=('sepentry10'),state=HIDDEN)
                            edit_ser_item_9.insert(1.0,edit_pser[13])

                            label_1 = Label(p_canvas_edit_3,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel9'),state=HIDDEN)
                            
                            edit_ser_item_10=Entry(p_canvas_edit_3,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_ser_item_10 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_ser_item_10,tags=('sepcentry2'),state=HIDDEN)
                            edit_ser_item_10.delete(0,'end')
                            edit_ser_item_10.insert(0, edit_pser[14])

                            chk_str_esser_item_2 = BooleanVar()
                            chkbtn_esser_item_2 = Checkbutton(p_canvas_edit_3, text = "Inclusive of Tax", variable = chk_str_esser_item_2, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                            chkbtn_esser_item_2.select()
                            window_chkbtn_esser_item_2 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=chkbtn_esser_item_2,tags=('sepcbutton2'),state=HIDDEN)

                            label_1 = Label(p_canvas_edit_3,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel10'),state=HIDDEN)

                            comb_eser_item_5 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                            comb_eser_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
                            comb_eser_item_5.current(0)
                            window_comb_eser_item_5 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_eser_item_5,tags=('sepcentry3'),state=HIDDEN)
                            comb_eser_item_5.delete(0,'end')
                            comb_eser_item_5.insert(0, edit_pser[16])

                            label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel20'),state=HIDDEN)

                            comb_eser_item_e6 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                            comb_eser_item_e6['values'] = ("Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities",)
                            comb_eser_item_e6.current(0)
                            window_comb_eser_item_e6 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=330, height=30,window=comb_eser_item_e6,tags=('sepcombo6'),state=HIDDEN)
                            comb_eser_item_e6.delete(0,'end')
                            comb_eser_item_e6.insert(0, edit_pser[15])

                            label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel21'),state=HIDDEN)

                            def pr_e3(event):
                                if edit_sser_item_11.get()=="0":
                                    edit_sser_item_11.delete(0,END)
                                else:
                                    pass

                            edit_sser_item_11=Entry(p_canvas_edit_3,width=50,justify=LEFT,background='#2f516f',foreground="white")
                            window_edit_sser_item_11 = p_canvas_edit_3.create_window(0, 0, anchor="nw", height=30,window=edit_sser_item_11,tags=('sepentry11'),state=HIDDEN)
                            edit_sser_item_11.insert(0,"0")
                            edit_sser_item_11.bind("<Button-1>",pr_e3)
                            edit_sser_item_11.delete(0,'end')
                            edit_sser_item_11.insert(0, edit_pser[17])

                            label_1 = Label(p_canvas_edit_3,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=label_1,tags=('seplabel22'),state=HIDDEN)

                            comb_eser_item_ps7 = ttk.Combobox(p_canvas_edit_3, font=('arial 10'))
                            comb_eser_item_ps7['values'] = ("Select Supplier",)
                            comb_eser_item_ps7.current(0)
                            window_comb_eser_item_ps7 = p_canvas_edit_3.create_window(0, 0, anchor="nw", width=345, height=30,window=comb_eser_item_ps7,tags=('sepcombo7'),state=HIDDEN)
                            comb_eser_item_ps7.delete(0,'end')
                            comb_eser_item_ps7.insert(0, edit_pser[18])

                            eser_sub_btn1=Button(p_canvas_edit_3,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=edit_new_pro_ser)
                            window_eser_sub_btn1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=eser_sub_btn1,tags=('sepbutton5'))

                            def s_eback_1_():
                                pro_frame_edit_3.grid_forget()
                                pro_frame.grid(row=0,column=0,sticky='nsew')

                            bck_esbtn1=Button(p_canvas_edit_3,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=s_eback_1_)
                            window_bck_esbtn1 = p_canvas_edit_3.create_window(0, 0, anchor="nw", window=bck_esbtn1,tags=('sepbuttn1'))
                        elif pro_tree.item(pro_tree.focus())["values"][1] == 'Bundle':
                            pro_frame.grid_forget()
                            pro_frame_edit_4 = Frame(tab3_4)
                            pro_frame_edit_4.grid(row=0,column=0,sticky='nsew')

                            def pro_responsive_widgets_e5(event):
                                dwidth = event.width
                                dheight = event.height
                                dcanvas = event.widget
                            
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/14 
                                y2 = dheight/3.505

                                dcanvas.coords("beppoly1",x1 + r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )

                                dcanvas.coords("beplabel1",dwidth/3,dheight/8.24)
                                dcanvas.coords("bephline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                                r2 = 25
                                x11 = dwidth/63
                                x21 = dwidth/1.021
                                y11 = dheight/2.8
                                y21 = dheight/0.45


                                dcanvas.coords("beppoly2",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                r2 = 25
                                x11 = dwidth/24
                                x21 = dwidth/1.050
                                y11 = dheight/2.1
                                y21 = dheight/1.35


                                dcanvas.coords("beppoly3",x11 + r2,y11,
                                x11 + r2,y11,
                                x21 - r2,y11,
                                x21 - r2,y11,     
                                x21,y11,     
                                #--------------------
                                x21,y11 + r2,     
                                x21,y11 + r2,     
                                x21,y21 - r2,     
                                x21,y21 - r2,     
                                x21,y21,
                                #--------------------
                                x21 - r2,y21,     
                                x21 - r2,y21,     
                                x11 + r2,y21,
                                x11 + r2,y21,
                                x11,y21,
                                #--------------------
                                x11,y21 - r2,
                                x11,y21 - r2,
                                x11,y11 + r2,
                                x11,y11 + r2,
                                x11,y11,
                                )

                                dcanvas.coords("beplabel2",dwidth/2.3,dheight/1.77)
                                dcanvas.coords("bepbutton1",dwidth/1.8,dheight/1.77)

                                dcanvas.coords("beplabel3",dwidth/23.2,dheight/1.23)
                                dcanvas.coords("beplabel4",dwidth/1.9,dheight/1.23)
                                dcanvas.coords("beplabel5",dwidth/25,dheight/1.02)
                                dcanvas.coords("beplabel6",dwidth/22.7,dheight/0.8)


                                dcanvas.coords("bepentry1",dwidth/23.2,dheight/1.165)
                                dcanvas.coords("bepentry2",dwidth/1.9,dheight/1.165)
                                dcanvas.coords("bepentry3",dwidth/23.2,dheight/0.97)

                                #-----------------------------H Lines---------------------------------#
                                dcanvas.coords("bepline1",dwidth/21.5,dheight/0.77,dwidth/1.075,dheight/0.77)
                                dcanvas.coords("bepline2",dwidth/21.5,dheight/0.72,dwidth/1.075,dheight/0.72)
                                dcanvas.coords("bepline3",dwidth/21.5,dheight/0.67,dwidth/1.075,dheight/0.67)
                                dcanvas.coords("bepline4",dwidth/21.5,dheight/0.619,dwidth/1.075,dheight/0.619)
                                dcanvas.coords("bepline5",dwidth/21.5,dheight/0.57,dwidth/1.075,dheight/0.57)
                                dcanvas.coords("bepline6",dwidth/21.5,dheight/0.535,dwidth/1.075,dheight/0.535)
                                #-----------------------------V Lines---------------------------------#
                                dcanvas.coords("bepline7",dwidth/21.5,dheight/0.77,dwidth/21.5,dheight/0.535)
                                dcanvas.coords("bepline8",dwidth/1.075,dheight/0.77,dwidth/1.075,dheight/0.535)
                                dcanvas.coords("bepline9",dwidth/4.8,dheight/0.77,dwidth/4.8,dheight/0.535)
                                dcanvas.coords("bepline10",dwidth/2.7,dheight/0.77,dwidth/2.7,dheight/0.535)
                                dcanvas.coords("bepline11",dwidth/1.84,dheight/0.77,dwidth/1.84,dheight/0.535)
                                dcanvas.coords("bepline12",dwidth/1.575,dheight/0.77,dwidth/1.575,dheight/0.535)
                                dcanvas.coords("bepline13",dwidth/1.366,dheight/0.77,dwidth/1.366,dheight/0.535)
                                dcanvas.coords("bepline14",dwidth/1.21,dheight/0.77,dwidth/1.21,dheight/0.535)

                                dcanvas.coords("beplabel7",dwidth/13,dheight/0.754)
                                dcanvas.coords("beplabel8",dwidth/3.85,dheight/0.754)
                                dcanvas.coords("beplabel9",dwidth/2.35,dheight/0.754)
                                dcanvas.coords("beplabel10",dwidth/1.75,dheight/0.754)
                                dcanvas.coords("beplabel11",dwidth/1.515,dheight/0.754)
                                dcanvas.coords("beplabel12",dwidth/1.325,dheight/0.754)
                                dcanvas.coords("beplabel13",dwidth/1.17,dheight/0.754)

                                dcanvas.coords("bepcombo1",dwidth/17,dheight/0.709)
                                dcanvas.coords("bepcombo2",dwidth/17,dheight/0.651)
                                dcanvas.coords("bepcombo3",dwidth/17,dheight/0.604)
                                dcanvas.coords("bepcombo4",dwidth/17,dheight/0.56)

                                dcanvas.coords("bepentry4",dwidth/4.6,dheight/0.709)
                                dcanvas.coords("bepentry5",dwidth/4.6,dheight/0.651)
                                dcanvas.coords("bepentry6",dwidth/4.6,dheight/0.604)
                                dcanvas.coords("bepentry7",dwidth/4.6,dheight/0.56)

                                dcanvas.coords("bepentry8",dwidth/2.6,dheight/0.709)
                                dcanvas.coords("bepentry9",dwidth/2.6,dheight/0.651)
                                dcanvas.coords("bepentry10",dwidth/2.6,dheight/0.604)
                                dcanvas.coords("bepentry11",dwidth/2.6,dheight/0.56)

                                dcanvas.coords("bepspin1",dwidth/1.81,dheight/0.709)
                                dcanvas.coords("bepspin2",dwidth/1.81,dheight/0.651)
                                dcanvas.coords("bepspin3",dwidth/1.81,dheight/0.604)
                                dcanvas.coords("bepspin4",dwidth/1.81,dheight/0.56)

                                dcanvas.coords("bepspin5",dwidth/1.56,dheight/0.709)
                                dcanvas.coords("bepspin6",dwidth/1.56,dheight/0.651)
                                dcanvas.coords("bepspin7",dwidth/1.56,dheight/0.604)
                                dcanvas.coords("bepspin8",dwidth/1.56,dheight/0.56)

                                dcanvas.coords("bepspin9",dwidth/1.351,dheight/0.709)
                                dcanvas.coords("bepspin10",dwidth/1.351,dheight/0.651)
                                dcanvas.coords("bepspin11",dwidth/1.351,dheight/0.604)
                                dcanvas.coords("bepspin12",dwidth/1.351,dheight/0.56)

                                dcanvas.coords("bepspin13",dwidth/1.195,dheight/0.709)
                                dcanvas.coords("bepspin14",dwidth/1.195,dheight/0.651)
                                dcanvas.coords("bepspin15",dwidth/1.195,dheight/0.604)
                                dcanvas.coords("bepspin16",dwidth/1.195,dheight/0.56)

                                dcanvas.coords("bepbutton2",dwidth/2.3,dheight/0.52)
                                dcanvas.coords("bepbuttn1",dwidth/23,dheight/3.415) 




                            pro_canvas_edit_4=Canvas(pro_frame_edit_4, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

                            pro_frame_edit_4.grid_columnconfigure(0,weight=1)
                            pro_frame_edit_4.grid_rowconfigure(0,weight=1)
                            
                            vertibar=Scrollbar(pro_frame_edit_4, orient=VERTICAL)
                            vertibar.grid(row=0,column=1,sticky='ns')
                            vertibar.config(command=pro_canvas_edit_4.yview)

                            pro_canvas_edit_4.bind("<Configure>", pro_responsive_widgets_e5)
                            pro_canvas_edit_4.config(yscrollcommand=vertibar.set)
                            pro_canvas_edit_4.grid(row=0,column=0,sticky='nsew')

                            bun_peditid = pro_tree.item(pro_tree.focus())["values"][2]

                            bun_peditid_1 = pro_tree.item(pro_tree.focus())["values"][3]

                            sql_pn="select * from auth_user where username=%s"
                            pn_val=(nm_ent.get(),)
                            fbcursor.execute(sql_pn,pn_val,)
                            pn_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pn_dtl[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dtln=fbcursor.fetchone()
                            print(cmp_dtln)

                            sql = 'select * from app1_bundle where name = %s and sku = %s and cid_id = %s'
                            val =  (bun_peditid,bun_peditid_1,cmp_dtln[0],)
                            fbcursor.execute(sql,val)
                            edit_pbun = fbcursor.fetchone()

                            def edit_new_pro_bun():

                                name = entry_ebun_item_1.get()
                                sku = entry_ebun_iitem_2.get()
                                description = entry_ebun_item_7.get('1.0', 'end-1c')
                                product1 = ebun_comb_1.get()
                                product2 = ebun_comb_2.get()
                                product3 = ebun_comb_3.get()
                                product4 = ebun_comb_4.get()
                                hsn1 = ebun_entry_1.get()
                                hsn2 = ebun_entry_2.get()
                                hsn3 = ebun_entry_3.get()
                                hsn4 = ebun_entry_4.get()
                                description1 = ebun_entry_5.get('1.0', 'end-1c')
                                description2 = ebun_entry_6.get('1.0', 'end-1c')
                                description3 = ebun_entry_7.get('1.0', 'end-1c')
                                description4 = ebun_entry_8.get('1.0', 'end-1c')
                                qty1 = ebun_entry_9.get()
                                qty2 = ebun_entry_10.get()
                                qty3 = ebun_entry_11.get()
                                qty4 = ebun_entry_12.get()
                                price1 = ebun_entry_13.get()
                                price2 = ebun_entry_14.get()
                                price3 = ebun_entry_15.get()
                                price4 = ebun_entry_16.get()
                                total1 = ebun_entry_17.get()
                                total2 = ebun_entry_18.get()
                                total3 = ebun_entry_19.get()
                                total4 = ebun_entry_20.get()
                                tax1 = ebun_entry_21.get()
                                tax2 = ebun_entry_22.get()
                                tax3 = ebun_entry_23.get()
                                tax4 = ebun_entry_24.get()


                                usrp3_sql = "SELECT id FROM auth_user WHERE username=%s"
                                usrp3_val = (nm_ent.get(),)
                                fbcursor.execute(usrp3_sql,usrp3_val)
                                usrp3_data = fbcursor.fetchone()

                                cmpp3_sql = "SELECT cid FROM app1_company WHERE id_id=%s"
                                cmpp3_val = (usrp3_data[0],)
                                fbcursor.execute(cmpp3_sql,cmpp3_val)
                                cmpp3_data = fbcursor.fetchone()
                                cid = cmpp3_data[0]

                                b_p_sql = "UPDATE app1_bundle set name=%s,sku=%s,description=%s,product1=%s,product2=%s,product3=%s,product4=%s,hsn1=%s,hsn2=%s,hsn3=%s,hsn4=%s,description1=%s,description2=%s,description3=%s,description4=%s,qty1=%s,qty2=%s,qty3=%s,qty4=%s,price1=%s,price2=%s,price3=%s,price4=%s,total1=%s,total2=%s,total3=%s,total4=%s,tax1=%s,tax2=%s,tax3=%s,tax4=%s,cid_id=%s where name=%s and sku = %s"
                                b_p_val = (name,sku,description,product1,product2,product3,product4,hsn1,hsn2,hsn3,hsn4,description1,description2,description3,description4,qty1,qty2,qty3,qty4,price1,price2,price3,price4,total1,total2,total3,total4,tax1,tax2,tax3,tax4,cid,bun_peditid,bun_peditid_1)
                                fbcursor.execute(b_p_sql,b_p_val)
                                finsysdb.commit()

                                #_________Refresh insert tree________#

                                for record in pro_tree.get_children():
                                    pro_tree.delete(record)

        
                                sql_p="select * from auth_user where username=%s"
                                sql_p_val=(nm_ent.get(),)
                                fbcursor.execute(sql_p,sql_p_val,)
                                pr_dt=fbcursor.fetchone()

                                sql = "select * from app1_company where id_id=%s"
                                val = (pr_dt[0],)
                                fbcursor.execute(sql, val,)
                                cmp_dt=fbcursor.fetchone()

                                p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                                p_val_1 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_1,p_val_1,)
                                p_data_1 = fbcursor.fetchall()
                                
                                count0 = 0
                                for i in p_data_1:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                                    else:
                                        pass
                                count0 += 1

                                p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                                p_val_2 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_2,p_val_2,)
                                p_data_2 = fbcursor.fetchall()

                                count1 = 0
                                for i in p_data_2:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count1 += 1

                                p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                                p_val_3 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_3,p_val_3,)
                                p_data_3 = fbcursor.fetchall()
                                

                                count2 = 0
                                for i in p_data_3:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                                    else:
                                        pass
                                count2 += 1

                                p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                                p_val_4 = (cmp_dt[0],)
                                fbcursor.execute(p_sql_4,p_val_4,)
                                p_data_4 = fbcursor.fetchall()
                                

                                count3 = 0
                                for i in p_data_4:
                                    if True:
                                        pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                                    else:
                                        pass
                                count3 += 1

                                pro_frame_edit_4.destroy()
                                pro_frame.grid(row=0,column=0,sticky='nsew')


                            pro_canvas_edit_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('beppoly1'))

                            label_1 = Label(pro_canvas_edit_4,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
                            window_label_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_1, tags=('beplabel1'))

                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('bephline'))

                            pro_canvas_edit_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('beppoly2'))

                            pro_canvas_edit_4.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('beppoly3'))
                            
                            label_1 = Label(pro_canvas_edit_4,width=15,height=2,text="BUNDLE", font=('arial 20'),background="#2f516f",fg="white") 
                            window_label_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_1, tags=('beplabel2'))

                            label_1 = Label(pro_canvas_edit_4,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_1, tags=('beplabel3'))

                            entry_ebun_item_1=Entry(pro_canvas_edit_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ebun_item_1 = pro_canvas_edit_4.create_window(55, 530, anchor="nw", height=30,window=entry_ebun_item_1, tags=('bepentry1'))
                            entry_ebun_item_1.delete(0,'end')
                            entry_ebun_item_1.insert(0, edit_pbun[2])


                            label_1 = Label(pro_canvas_edit_4,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_1, tags=('beplabel4'))

                            def ps_e4(event):
                                if entry_ebun_iitem_2.get()==edit_pbun[3]:
                                    entry_ebun_iitem_2.delete(0,END)
                                else:
                                    pass

                            entry_ebun_iitem_2=Entry(pro_canvas_edit_4,width=90,justify=LEFT,background='#2f516f',foreground="white")
                            window_entry_ebun_iitem_2 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30,window=entry_ebun_iitem_2, tags=('bepentry2'))
                            entry_ebun_iitem_2.delete(0,'end')
                            entry_ebun_iitem_2.insert(0, edit_pbun[3])
                            entry_ebun_iitem_2.bind("<Button-1>",ps_e4)


                            label_1 = Label(pro_canvas_edit_4,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_1, tags=('beplabel5'))

                            entry_ebun_item_7=scrolledtext.ScrolledText(pro_canvas_edit_4,width=146,background='#2f516f',foreground="white")
                            window_entry_ebun_item_7 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=60,window=entry_ebun_item_7, tags=('bepentry3'))
                            entry_ebun_item_7.insert(1.0,edit_pbun[4])

                            label_1 = Label(pro_canvas_edit_4,width=30,height=1,text="Products/services included in the bundle", font=('arial 12'),background="#1b3857",fg="white") 
                            window_label_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_1, tags=('beplabel6'))

                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline1'))
                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline2'))
                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline3'))
                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline4'))
                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline5'))
                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline6'))
                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline7'))
                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline8'))
                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline9'))
                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline10'))
                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline11'))
                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline12'))
                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline13'))
                            pro_canvas_edit_4.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('bepline14'))
                            

                            label_3 = Label(pro_canvas_edit_4,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_3 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_3,tags=('beplabel7'))

                            label_4 = Label(pro_canvas_edit_4,width=10,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_4,tags=('beplabel8'))

                            label_4 = Label(pro_canvas_edit_4,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_4,tags=('beplabel9'))

                            label_4 = Label(pro_canvas_edit_4,width=5,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_4,tags=('beplabel10'))

                            label_4 = Label(pro_canvas_edit_4,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_4,tags=('beplabel11'))

                            label_4 = Label(pro_canvas_edit_4,width=8,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_4,tags=('beplabel12'))

                            label_4 = Label(pro_canvas_edit_4,width=8,height=1,text="TAX", font=('arial 10'),background="#1b3857",fg="white") 
                            window_label_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=label_4,tags=('beplabel13'))

                            def bun_details_e1(event):
                                ebun_to_str_1 = ebun_comb_1.get()
                                try:
                                    sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                    val = (ebun_to_str_1,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    ebun_sel_1 = fbcursor.fetchone()
                                    ebun_entry_1.delete(0,END)
                                    ebun_entry_1.insert(0,ebun_sel_1[4])
                                    ebun_entry_5.delete('1.0',END)
                                    ebun_entry_5.insert('1.0',ebun_sel_1[11])
                                    ebun_entry_13.delete(0,END)
                                    ebun_entry_13.insert(0,ebun_sel_1[12])
                                    ebun_entry_21.delete(0,END)
                                    ebun_entry_21.insert(0,ebun_sel_1[14])
                                except:
                                    sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                    val = (ebun_to_str_1,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    ebun_sel_1 = fbcursor.fetchone()
                                    ebun_entry_1.delete(0,END)
                                    ebun_entry_1.insert(0,ebun_sel_1[4])
                                    ebun_entry_5.delete('1.0',END)
                                    ebun_entry_5.insert('1.0',ebun_sel_1[7])
                                    ebun_entry_13.delete(0,END)
                                    ebun_entry_13.insert(0,ebun_sel_1[8])
                                    ebun_entry_21.delete(0,END)
                                    ebun_entry_21.insert(0,ebun_sel_1[10])

                            def bun_details_e2(event):
                                ebun_to_str_2 = ebun_comb_2.get()
                                try:
                                    sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                    val = (ebun_to_str_2,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    ebun_sel_2 = fbcursor.fetchone()
                                    ebun_entry_2.delete(0,END)
                                    ebun_entry_2.insert(0,ebun_sel_2[4])
                                    ebun_entry_6.delete('1.0',END)
                                    ebun_entry_6.insert('1.0',ebun_sel_2[11])
                                    ebun_entry_14.delete(0,END)
                                    ebun_entry_14.insert(0,ebun_sel_2[12])
                                    ebun_entry_22.delete(0,END)
                                    ebun_entry_22.insert(0,ebun_sel_2[14])
                                except:
                                    sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                    val = (ebun_to_str_2,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    ebun_sel_2 = fbcursor.fetchone()
                                    ebun_entry_2.delete(0,END)
                                    ebun_entry_2.insert(0,ebun_sel_2[4])
                                    ebun_entry_6.delete('1.0',END)
                                    ebun_entry_6.insert('1.0',ebun_sel_2[7])
                                    ebun_entry_14.delete(0,END)
                                    ebun_entry_14.insert(0,ebun_sel_2[8])
                                    ebun_entry_22.delete(0,END)
                                    ebun_entry_22.insert(0,ebun_sel_2[10])

                            def bun_details_e3(event):
                                ebun_to_str_3 = ebun_comb_3.get()
                                try:
                                    sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                    val = (ebun_to_str_3,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    ebun_sel_3 = fbcursor.fetchone()
                                    ebun_entry_3.delete(0,END)
                                    ebun_entry_3.insert(0,ebun_sel_3[4])
                                    ebun_entry_7.delete('1.0',END)
                                    ebun_entry_7.insert('1.0',ebun_sel_3[11])
                                    ebun_entry_15.delete(0,END)
                                    ebun_entry_15.insert(0,ebun_sel_3[12])
                                    ebun_entry_23.delete(0,END)
                                    ebun_entry_23.insert(0,ebun_sel_3[14])
                                except:
                                    sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                    val = (ebun_to_str_3,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    ebun_sel_3 = fbcursor.fetchone()
                                    ebun_entry_3.delete(0,END)
                                    ebun_entry_3.insert(0,ebun_sel_3[4])
                                    ebun_entry_7.delete('1.0',END)
                                    ebun_entry_7.insert('1.0',ebun_sel_3[7])
                                    ebun_entry_15.delete(0,END)
                                    ebun_entry_15.insert(0,ebun_sel_3[8])
                                    ebun_entry_23.delete(0,END)
                                    ebun_entry_23.insert(0,ebun_sel_3[10])

                            def bun_details_e4(event):
                                ebun_to_str_4 = ebun_comb_4.get()
                                try:
                                    sql = "select * from app1_inventory where name=%s and cid_id=%s"
                                    val = (ebun_to_str_4,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    ebun_sel_4 = fbcursor.fetchone()
                                    ebun_entry_4.delete(0,END)
                                    ebun_entry_4.insert(0,ebun_sel_4[4])
                                    ebun_entry_8.delete('1.0',END)
                                    ebun_entry_8.insert('1.0',ebun_sel_4[11])
                                    ebun_entry_16.delete(0,END)
                                    ebun_entry_16.insert(0,ebun_sel_4[12])
                                    ebun_entry_24.delete(0,END)
                                    ebun_entry_24.insert(0,ebun_sel_4[14])
                                except:
                                    sql = "select * from app1_noninventory where name=%s and cid_id=%s"
                                    val = (ebun_to_str_4,cmp_dtli[0],)
                                    fbcursor.execute(sql,val)
                                    ebun_sel_4 = fbcursor.fetchone()
                                    ebun_entry_4.delete(0,END)
                                    ebun_entry_4.insert(0,ebun_sel_4[4])
                                    ebun_entry_8.delete('1.0',END)
                                    ebun_entry_8.insert('1.0',ebun_sel_4[7])
                                    ebun_entry_16.delete(0,END)
                                    ebun_entry_16.insert(0,ebun_sel_4[8])
                                    ebun_entry_24.delete(0,END)
                                    ebun_entry_24.insert(0,ebun_sel_4[10])
                                

                            sql_pi="select * from auth_user where username=%s"
                            pi_val=(nm_ent.get(),)
                            fbcursor.execute(sql_pi,pi_val,)
                            pi_dtl=fbcursor.fetchone()

                            sql = "select * from app1_company where id_id=%s"
                            val = (pi_dtl[0],)
                            fbcursor.execute(sql, val,)
                            cmp_dtli=fbcursor.fetchone()
                            print(cmp_dtli)

                            ebi_sql = "SELECT name FROM app1_inventory where cid_id=%s"
                            ebi_val = (cmp_dtli[0],)
                            fbcursor.execute(ebi_sql,ebi_val)
                            ebi_data = fbcursor.fetchall()
                        
                            ebii_sql = "SELECT name FROM app1_noninventory where cid_id=%s"
                            ebii_val = (cmp_dtli[0],)
                            fbcursor.execute(ebii_sql,ebii_val)
                            ebii_data = fbcursor.fetchall()

                            eb_data = []   
                            
                            for i in ebi_data:
                                eb_data.append(i[0])
                            for i in ebii_data:
                                eb_data.append(i[0])            


                            ebun_comb_1 = ttk.Combobox(pro_canvas_edit_4, font=('arial 10'),values=eb_data)
                            # bun_comb_1['values'] = ("Choose",b_data,)
                            ebun_comb_1.bind("<<ComboboxSelected>>",bun_details_e1)
                            window_ebun_comb_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", width=180, height=30,window=ebun_comb_1,tags=('bepcombo1'))
                            ebun_comb_1.delete(0,'end')
                            ebun_comb_1.insert(0, edit_pbun[5])

                            ebun_comb_2 = ttk.Combobox(pro_canvas_edit_4, font=('arial 10'),values=eb_data)
                            # bun_comb_2['values'] = ("Choose",b_data,)
                            ebun_comb_2.bind("<<ComboboxSelected>>",bun_details_e2)
                            window_ebun_comb_2 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", width=180, height=30,window=ebun_comb_2,tags=('bepcombo2'))
                            ebun_comb_2.delete(0,'end')
                            ebun_comb_2.insert(0, edit_pbun[6])

                            ebun_comb_3 = ttk.Combobox(pro_canvas_edit_4, font=('arial 10'),values=eb_data)
                            # bun_comb_3['values'] = ("Choose",b_data,)
                            ebun_comb_3.bind("<<ComboboxSelected>>",bun_details_e3)
                            window_ebun_comb_3 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", width=180, height=30,window=ebun_comb_3,tags=('bepcombo3'))
                            ebun_comb_3.delete(0,'end')
                            ebun_comb_3.insert(0, edit_pbun[7])

                            ebun_comb_4 = ttk.Combobox(pro_canvas_edit_4, font=('arial 10'),values=eb_data)
                            # bun_comb_4['values'] = ("Choose",b_data,)
                            ebun_comb_4.bind("<<ComboboxSelected>>",bun_details_e4)
                            window_ebun_comb_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", width=180, height=30,window=ebun_comb_4,tags=('bepcombo4'))
                            ebun_comb_4.delete(0,'end')
                            ebun_comb_4.insert(0, edit_pbun[8])
                        

                            ebun_entry_1=Entry(pro_canvas_edit_4,width=30,justify=LEFT,background='#2f516f',foreground="white")
                            window_ebun_entry_1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_1,tags=('bepentry4'))
                            ebun_entry_1.delete(0,'end')
                            ebun_entry_1.insert(0, edit_pbun[9])
                            
                            ebun_entry_2=Entry(pro_canvas_edit_4,width=30,justify=LEFT,background='#2f516f',foreground="white")
                            window_ebun_entry_2 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_2,tags=('bepentry5'))
                            ebun_entry_2.delete(0,'end')
                            ebun_entry_2.insert(0, edit_pbun[10])

                            ebun_entry_3=Entry(pro_canvas_edit_4,width=30,justify=LEFT,background='#2f516f',foreground="white")
                            window_ebun_entry_3 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_3,tags=('bepentry6'))
                            ebun_entry_3.delete(0,'end')
                            ebun_entry_3.insert(0, edit_pbun[11])
                            
                            ebun_entry_4=Entry(pro_canvas_edit_4,width=30,justify=LEFT,background='#2f516f',foreground="white")
                            window_ebun_entry_4 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_4,tags=('bepentry7'))
                            ebun_entry_4.delete(0,'end')
                            ebun_entry_4.insert(0, edit_pbun[12])


                            ebun_entry_5=scrolledtext.ScrolledText(pro_canvas_edit_4,width=23,background='#2f516f',foreground="white")
                            window_ebun_entry_5 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_5,tags=('bepentry8'))
                            ebun_entry_5.insert(1.0,edit_pbun[13])

                            ebun_entry_6=scrolledtext.ScrolledText(pro_canvas_edit_4,width=23,background='#2f516f',foreground="white")
                            window_ebun_entry_6 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_6,tags=('bepentry9'))
                            ebun_entry_6.insert(1.0,edit_pbun[14])

                            ebun_entry_7=scrolledtext.ScrolledText(pro_canvas_edit_4,width=23,background='#2f516f',foreground="white")
                            window_ebun_entry_7 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_7,tags=('bepentry10'))
                            ebun_entry_7.insert(1.0,edit_pbun[15])

                            ebun_entry_8=scrolledtext.ScrolledText(pro_canvas_edit_4,width=23,background='#2f516f',foreground="white")
                            window_ebun_entry_8 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_8,tags=('bepentry11'))
                            ebun_entry_8.insert(1.0,edit_pbun[16])


                            ebun_entry_9=Spinbox(pro_canvas_edit_4,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_9 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_9,tags=('bepspin1'))
                            ebun_entry_9.delete(0, END)
                            ebun_entry_9.insert(0, edit_pbun[17])

                            ebun_entry_10=Spinbox(pro_canvas_edit_4,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_10 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_10,tags=('bepspin2'))
                            ebun_entry_10.delete(0, END)
                            ebun_entry_10.insert(0, edit_pbun[18])

                            ebun_entry_11=Spinbox(pro_canvas_edit_4,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_11 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_11,tags=('bepspin3'))
                            ebun_entry_11.delete(0, END)
                            ebun_entry_11.insert(0, edit_pbun[19])

                            ebun_entry_12=Spinbox(pro_canvas_edit_4,width=14,from_=0 ,to=1000,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_12 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_12,tags=('bepspin4'))
                            ebun_entry_12.delete(0, END)
                            ebun_entry_12.insert(0, edit_pbun[20])

                            
                            ebun_entry_13=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_13 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_13,tags=('bepspin5'))
                            ebun_entry_13.delete(0, END)
                            ebun_entry_13.insert(0, edit_pbun[21])
                            
                            ebun_entry_14=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_14 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_14,tags=('bepspin6'))
                            ebun_entry_14.delete(0, END)
                            ebun_entry_14.insert(0, edit_pbun[22])

                            ebun_entry_15=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_15 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_15,tags=('bepspin7'))
                            ebun_entry_15.delete(0, END)
                            ebun_entry_15.insert(0, edit_pbun[23])

                            ebun_entry_16=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_16 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_16,tags=('bepspin8'))
                            ebun_entry_16.delete(0, END)
                            ebun_entry_16.insert(0, edit_pbun[24])

                            def multiply_num_e1(event):
                                num1= float(ebun_entry_9.get())
                                num2= float(ebun_entry_13.get())
                                mul= round(num1 * num2)
                                ebun_entry_17.delete(0, END)
                                ebun_entry_17.insert(0,mul)
                            
                            ebun_entry_17=Entry(pro_canvas_edit_4,width=16,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_17 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_17,tags=('bepspin9'))
                            ebun_entry_17.bind("<Button-1>",multiply_num_e1)
                            ebun_entry_17.delete(0, END)
                            ebun_entry_17.insert(0, edit_pbun[25])

                            def multiply_num_e2(event):
                                num1= float(ebun_entry_10.get())
                                num2= float(ebun_entry_14.get())
                                mul= round(num1 * num2)
                                ebun_entry_18.delete(0, END)
                                ebun_entry_18.insert(0,mul)
                        
                            
                            ebun_entry_18=Entry(pro_canvas_edit_4,width=16,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_18 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_18,tags=('bepspin10'))
                            ebun_entry_18.bind("<Button-1>",multiply_num_e2)
                            ebun_entry_18.delete(0, END)
                            ebun_entry_18.insert(0, edit_pbun[26])

                            def multiply_num_e3(event):
                                num1= float(ebun_entry_11.get())
                                num2= float(ebun_entry_15.get())
                                mul= round(num1 * num2)
                                ebun_entry_19.delete(0, END)
                                ebun_entry_19.insert(0,mul)
                            
                            ebun_entry_19=Entry(pro_canvas_edit_4,width=16,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_19 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_19,tags=('bepspin11'))
                            ebun_entry_19.bind("<Button-1>",multiply_num_e3)
                            ebun_entry_19.delete(0, END)
                            ebun_entry_19.insert(0, edit_pbun[27])

                            def multiply_num_e4(event):
                                num1= float(ebun_entry_12.get())
                                num2= float(ebun_entry_16.get())
                                mul= round(num1 * num2)
                                ebun_entry_20.delete(0, END)
                                ebun_entry_20.insert(0,mul)
                        
                            ebun_entry_20=Entry(pro_canvas_edit_4,width=16,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_20 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_20,tags=('bepspin12'))
                            ebun_entry_20.bind("<Button-1>",multiply_num_e4)
                            ebun_entry_20.delete(0, END)
                            ebun_entry_20.insert(0, edit_pbun[28])
                            
                            ebun_entry_21=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_21 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_21,tags=('bepspin13'))
                            ebun_entry_21.delete(0, END)
                            ebun_entry_21.insert(0, edit_pbun[29])

                            ebun_entry_22=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_22 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_22,tags=('bepspin14'))
                            ebun_entry_22.delete(0, END)
                            ebun_entry_22.insert(0, edit_pbun[30])

                            ebun_entry_23=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_23 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_23,tags=('bepspin15'))
                            ebun_entry_23.delete(0, END)
                            ebun_entry_23.insert(0, edit_pbun[31])

                            ebun_entry_24=Spinbox(pro_canvas_edit_4,width=16,from_=0 ,to=1000000,justify=LEFT,background='#2f516f',foreground='white')
                            window_ebun_entry_24 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", height=30, window=ebun_entry_24,tags=('bepspin16'))
                            ebun_entry_24.delete(0, END)
                            ebun_entry_24.insert(0, edit_pbun[32])

                            ebun_sub_btn1=Button(pro_canvas_edit_4,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=edit_new_pro_bun)
                            window_ebun_sub_btn1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=ebun_sub_btn1,tags=('bepbutton2'))

                            def b_eback_1_():
                                pro_frame_edit_4.grid_forget()
                                pro_frame.grid(row=0,column=0,sticky='nsew')

                            bck_ebbtn1=Button(pro_canvas_edit_4,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=b_eback_1_)
                            window_bck_ebbtn1 = pro_canvas_edit_4.create_window(0, 0, anchor="nw", window=bck_ebbtn1,tags=('bepbuttn1'))
                        else:
                            pass


                # pebtn1=Button(pro_canvas,text='Edit', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=pro_edit_item)
                # window_pebtn1 = pro_canvas.create_window(0, 0, anchor="nw", window=pebtn1,tags=('pbutton2'))

                pro_comb_1 = ttk.Combobox(pro_canvas,font=('arial 10'))
                pro_comb_1['values'] = ("Actions","Edit","Delete")
                pro_comb_1.current(0)
                window_pro_comb_1 = pro_canvas.create_window(0, 0, anchor="nw", width=110,height=30,window=pro_comb_1,tags=('pbutton3'))
                pro_comb_1.bind("<<ComboboxSelected>>",pro_edit_item)

                # pdbtn1=Button(pro_canvas,text='Delete', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                # window_pdbtn1 = pro_canvas.create_window(0, 0, anchor="nw", window=pdbtn1,tags=('pbutton3'))

                fgth = ttk.Style()
                fgth.theme_use("default")
                fgth.configure("Treeview", background="#2f516f", foreground="white",fieldbackground="#2f516f",rowheight=25,font=(None,11))
                fgth.configure("Treeview.Heading",background="#1b3857",activeforeground="black",foreground="white",font=(None,11))  

                pro_tree = ttk.Treeview(pro_canvas, columns = (1,2,3,4,5,6),show = "headings")
                # pro_tree.pack(side = 'top')
                pro_tree.heading(1)
                pro_tree.heading(2, text="TYPE")
                pro_tree.heading(3, text="NAME")
                pro_tree.heading(4, text="SKU")
                pro_tree.heading(5, text="HSN/SAC")
                pro_tree.heading(6, text="QUANTITY")
                
                pro_tree.column(1, width = 50)
                pro_tree.column(2, width = 250)
                pro_tree.column(3, width = 300)
                pro_tree.column(4, width = 150)
                pro_tree.column(5, width = 200)
                pro_tree.column(6, width = 150)
                window_label_4 = pro_canvas.create_window(0, 0, anchor="nw", window=pro_tree,tags=('ptree1'))

                sql_p="select * from auth_user where username=%s"
                sql_p_val=(nm_ent.get(),)
                fbcursor.execute(sql_p,sql_p_val,)
                pr_dt=fbcursor.fetchone()

                sql = "select * from app1_company where id_id=%s"
                val = (pr_dt[0],)
                fbcursor.execute(sql, val,)
                cmp_dt=fbcursor.fetchone()

                p_sql_1 = "SELECT * FROM app1_inventory where cid_id=%s"
                p_val_1 = (cmp_dt[0],)
                fbcursor.execute(p_sql_1,p_val_1,)
                p_data_1 = fbcursor.fetchall()
                
                count0 = 0
                for i in p_data_1:
                    if True:
                       pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Inventory',i[2],i[3],i[4],i[7])) 
                    else:
                        pass
                count0 += 1

                p_sql_2 = "SELECT * FROM app1_noninventory where cid_id=%s"
                p_val_2 = (cmp_dt[0],)
                fbcursor.execute(p_sql_2,p_val_2,)
                p_data_2 = fbcursor.fetchall()

                count1 = 0
                for i in p_data_2:
                    if True:
                       pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Noninventory',i[2],i[3],i[4],'')) 
                    else:
                        pass
                count1 += 1

                p_sql_3 = "SELECT * FROM app1_service where cid_id=%s"
                p_val_3 = (cmp_dt[0],)
                fbcursor.execute(p_sql_3,p_val_3,)
                p_data_3 = fbcursor.fetchall()
                

                count2 = 0
                for i in p_data_3:
                    if True:
                       pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Service',i[2],i[3],i[4],'')) 
                    else:
                        pass
                count2 += 1

                p_sql_4 = "SELECT * FROM app1_bundle where cid_id=%s"
                p_val_4 = (cmp_dt[0],)
                fbcursor.execute(p_sql_4,p_val_4,)
                p_data_4 = fbcursor.fetchall()
                

                count3 = 0
                for i in p_data_4:
                    if True:
                       pro_tree.insert(parent='',index='end',iid=i,text='',values=('','Bundle',i[2],i[3],'','')) 
                    else:
                        pass
                count3 += 1



                #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Expenses Tab}
                tab_exp = ttk.Notebook(tab4)
                tab4_1 =  ttk.Frame(tab_exp)
                tab4_2=  ttk.Frame(tab_exp)
                tab_exp.add(tab4_1,compound = LEFT, text ='Expenses')
                tab_exp.add(tab4_2,compound = LEFT, text ='Supliers')
                tab_exp.pack(expand = 1, fill ="both")
                #33333333333333333333333333333333333333333333333333333333333333333333333333333333333{Pay Roll Tab}
                tab_payroll = ttk.Notebook(tab5)
                tab5_1 =  ttk.Frame(tab_payroll)
                tab5_2=  ttk.Frame(tab_payroll)
                
                tab_payroll.add(tab5_1,compound = LEFT, text ='Employee')
                tab_payroll.add(tab5_2,compound = LEFT, text ='Payslip')

                tab_payroll.pack(expand = 1, fill ="both")

                #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Report Tab}

                tab_report = ttk.Notebook(tab6)
                tab6_1 =  ttk.Frame(tab_report)
                tab6_2=  ttk.Frame(tab_report)
                tab6_3 = ttk.Frame(tab_report)
                tab6_4=  ttk.Frame(tab_report)

                
                    
                tab_report.add(tab6_1,compound = LEFT, text ='Profit & Loss')
                tab_report.add(tab6_2,compound = LEFT, text ='Balance Sheet')
                tab_report.add(tab6_3,compound = LEFT, text ='Accounts Receivables')
                tab_report.add(tab6_4,compound = LEFT, text ='Accounts Payables')
            
                tab_report.pack(expand = 1, fill ="both")

                #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Taxes}

                tab_tax = ttk.Notebook(tab7)
                tab7_1 =  ttk.Frame(tab_tax)
                tab7_2=  ttk.Frame(tab_tax)

                tab_tax.add(tab7_1,compound = LEFT, text ='GST')
                tab_tax.add(tab7_2,compound = LEFT, text ='New')

                tab_tax.pack(expand = 1, fill ="both")

                #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Accounting}
                tab_account = ttk.Notebook(tab8)
                tab8_1 =  ttk.Frame(tab_account)
                tab8_2=  ttk.Frame(tab_account)

                tab_account.add(tab8_1,compound = LEFT, text ='Chart Of Accounts')
                tab_account.add(tab8_2,compound = LEFT, text ='Reconcile')
            
            
                tab_account.pack(expand = 1, fill ="both")
                #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Cash Management}
                tab_cash = ttk.Notebook(tab10)
                
                tab10_1 =  ttk.Frame(tab_cash)
                tab10_2=  ttk.Frame(tab_cash)
                tab10_3 = ttk.Frame(tab_cash)

                tab_cash.add(tab10_1,compound = LEFT, text ='Cash Position')
                tab_cash.add(tab10_2,compound = LEFT, text ='Cash Flow Analyzer')
                tab_cash.add(tab10_3,compound = LEFT, text ='Check Cash Flow')

                tab_cash.pack(expand = 1, fill ="both")
                #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{My Account}
                Sys_mains_frame=Frame(tab9, height=750,bg="#2f516f")
                Sys_mains_frame.pack(fill=X)
                
            else:
                messagebox.showerror("Login Failed","Invalid username or password")
                pass

#---------------------------------------------------------------------------------------------------------------Company Second Portion
def cmpny_crt2():
    

    cmp_name=cmp_nm.get()
    cmp_address=cmp_cmpn.get()
    cmp_ctys=cmp_cty.get()
    state=cmp_stat.get()
    cmp_pins=cmp_pin.get()
    cmp_emails=cmp_email.get()
    cmp_phs=cmp_ph.get()
    cmp_filess=cmp_files.get()
    if cmp_name is not None:
        sql_log_sql='select id from auth_user where username=%s'
        sql_log_sql_val=(sys_usr.get(),)
        
        fbcursor.execute(sql_log_sql,sql_log_sql_val,)
        id=fbcursor.fetchone()
        
        signup_cmp_sql="insert into app1_company(cname,caddress,city,state,pincode,cemail,phone,cimg,id_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
        signup_cmp_sql_val=(cmp_name,cmp_address,cmp_ctys,state,cmp_pins,cmp_emails,cmp_phs,cmp_filess,id[0])
        fbcursor.execute(signup_cmp_sql,signup_cmp_sql_val,)
        finsysdb.commit()
    else:
        messagebox.showerror("Company Creation Failed","Enter your company details")

    main_frame_cmpny.pack_forget()
    global main_frame_cmpny2,nm_nm2,industry_tp,cmp_type,bs_act_man,paid_typ
    main_frame_cmpny2=Frame(root, height=750,bg="#213b52")
    main_frame_cmpny2.pack(fill=X,)

    cmpny_dt_frm2=Frame(main_frame_cmpny2, height=650, width=500,bg="white")
    cmpny_dt_frm2.pack(pady=105)

    def responsive_wid_cmp2(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("cmpny_hd1",dwidth/40,dheight/15)
        dcanvas.coords("nm_nm2",dwidth/6,dheight/5)
        dcanvas.coords("cmpny_cntry",dwidth/6,dheight/3.2)
        dcanvas.coords("cmpny_cntry2",dwidth/6,dheight/2.35)
        dcanvas.coords("r1",dwidth/2.2,dheight/1.8)
        dcanvas.coords("r2",dwidth/2.2,dheight/1.6)
        dcanvas.coords("cmpny_cntry3",dwidth/6,dheight/1.38)
        dcanvas.coords("button_cmp2",dwidth/4.3,dheight/1.2)
        dcanvas.coords("button_cmp3",dwidth/1.9,dheight/1.2)

        dcanvas.coords("cmp_lbl1",dwidth/6,dheight/3.8)
        dcanvas.coords("cmp_lbl2",dwidth/6,dheight/2.7)
        dcanvas.coords("cmp_lbl3",dwidth/6,dheight/2)
        dcanvas.coords("cmp_lbl4",dwidth/6,dheight/1.46)
        

    lf_cmpy2= Canvas(cmpny_dt_frm2,height=650, width=500)
    lf_cmpy2.bind("<Configure>", responsive_wid_cmp2)
    lf_cmpy2.pack(fill=X)

    def name_ent2(event):
        if nm_nm2.get()=="Legal Business Name":
            nm_nm2.delete(0,END)
        else:
            pass


    cmpny_hd1=Label(lf_cmpy2, text="Let's Start Building Your FinsYs",font=('Calibri 28 bold'), fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_hd1, tag=("cmpny_hd1"))

    

    nm_nm2 = Entry(cmpny_dt_frm2, width=30, font=('Calibri 16'),borderwidth=2)
    nm_nm2.insert(0,"Legal Business Name")
    nm_nm2.bind("<Button-1>",name_ent2)
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=nm_nm2, tag=("nm_nm2"))

    cmp_lbl1=Label(cmpny_dt_frm2, text="Your Industry",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl1, tag=("cmp_lbl1"))

    industry_tp= StringVar()
    cmpny_cntry = ttk.Combobox(cmpny_dt_frm2,textvariable=industry_tp,width=29,font=('Calibri 16'))
    
    cmpny_cntry['values'] = ('Accounting Services','Consultants, doctors, Lawyers and similar','Information Tecnology','Manufacturing','Professional, Scientific and Technical Services','Restaurant/Bar and similar','Retail and Smilar','Other Finanacial Services')
   
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry, tag=("cmpny_cntry"))

    cmp_lbl2=Label(cmpny_dt_frm2, text="Company type",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl2, tag=("cmp_lbl2"))

    cmp_type = StringVar()
    cmpny_cntry2 = ttk.Combobox(cmpny_dt_frm2,textvariable=cmp_type,width=29,font=('Calibri 16'))
    
    cmpny_cntry['values'] = ('Private Limited Company','Public Limited Company','Joint-Venture Company','Partnership Firm Company','One Person Company','Branch Office Company','Non Government Organization')
    
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry2, tag=("cmpny_cntry2"))
    
    cmp_lbl3=Label(cmpny_dt_frm2, text="Do you have an Accountant, Bookkeeper or Tax Pro ?",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl3, tag=("cmp_lbl3"))

    bs_act_man=StringVar()
    r1=Radiobutton(cmpny_dt_frm2, text = "Yes", variable = bs_act_man, value ="Yes",font=('Calibri 16'))
    r1.select()
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=r1, tag=("r1"))

    r2=Radiobutton(cmpny_dt_frm2, text = "No", variable = bs_act_man, value ="No",font=('Calibri 16'))
    r2.select()
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=r2, tag=("r2"))


    cmp_lbl4=Label(cmpny_dt_frm2, text="How do you like to get paid?",font=('Calibri 12') ,fg="black")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmp_lbl4, tag=("cmp_lbl4"))
    
    paid_typ = StringVar()
    cmpny_cntry3 = ttk.Combobox(cmpny_dt_frm2,textvariable=paid_typ,width=29,font=('Calibri 16'))
    cmpny_cntry['values'] = ('Cash','Cheque','Credit card/Debit card','Bank Transfer','Paypal/Other service')
   
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=cmpny_cntry3, tag=("cmpny_cntry3"))

    button_cmp2 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=cmpny_crt1,text="Previous",bg="#213b52")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=button_cmp2, tag=("button_cmp2"))
    button_cmp3 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=fun_sign_in,text="Submit",bg="#213b52")
    win_inv1 = lf_cmpy2.create_window(0, 0, anchor="nw", window=button_cmp3, tag=("button_cmp3"))
#-------------------------------------------------------------------------------------------------------------------company creation

def cmpny_crt1():
    
    first_name=fst_nm.get()
    last_name=lst_nm.get()
    email=sys_em.get()
    username=sys_usr.get()
    password=sys_pass.get()
    con_password=sys_cf.get()
    join_dt=datetime.today()
    sql_signup='select * from auth_user'
    fbcursor.execute(sql_signup)
    check_none=fbcursor.fetchone()
    global main_frame_cmpny,cmp_nm,cmp_cmpn,cmp_cty,cmp_pin,cmp_email,cmp_ph,cmp_files,cmp_stat
    if check_none is not None:
        if check_none[4]!=username and check_none[1]!=password:
            
            if password==con_password and con_password==password :
                
                signup_sql="insert into auth_user(first_name,last_name,email,username,password,date_joined) VALUES(%s,%s,%s,%s,%s,%s)" #adding values into db
                signup_sql_val=(first_name,last_name,email,username,password,join_dt,)
                fbcursor.execute(signup_sql,signup_sql_val,)
                finsysdb.commit()
                try:
                    main_frame_cmpny2.pack_forget()
                except:
                    pass
                try:
                    main_frame_signup.pack_forget()
                except:
                    pass
                
                main_frame_cmpny=Frame(root, height=750,bg="#213b52")
                main_frame_cmpny.pack(fill=X,)

                cmpny_dt_frm=Frame(main_frame_cmpny, height=650, width=500,bg="white")
                cmpny_dt_frm.pack(pady=50)

                def name_ent(event):
                    if cmp_nm.get()=="Company Name":
                        cmp_nm.delete(0,END)
                    else:
                        pass

                def cmp_add(event):
                    if cmp_cmpn.get()=="Company Address":
                            cmp_cmpn.delete(0,END)
                    else:
                        pass
                def cty_ent(event):
                    if cmp_cty.get()=="City":
                        cmp_cty.delete(0,END)
                    else:
                        pass

                def em_ent(event):
                    if cmp_email.get()=="Email":
                            cmp_email.delete(0,END)
                    else:
                        pass
                def ph_ent(event):
                    if cmp_ph.get()=="Phone Number":
                        cmp_ph.delete(0,END)
                    else:
                        pass

                def fil_ent(event):
                    
                    cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
                    logo_crp=cmp_logo.split('/',-1)
                    im1 = Image.open(r""+cmp_logo) 
                    im1 = im1.save("profilepic/propic.jpg")
                    
                    cmp_files.delete(0,END)
                    cmp_files.insert(0,logo_crp[-1])
                
                def responsive_wid_cmp1(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
            

                    dcanvas.coords("cmpny_hd",dwidth/2,dheight/13)
                    dcanvas.coords("nm_nm",dwidth/2,dheight/5)
                    dcanvas.coords("cmp_cmpn",dwidth/2,dheight/3.5)
                    dcanvas.coords("cmp_cty",dwidth/2,dheight/2.7)
                    dcanvas.coords("cmpny_cntry",dwidth/2,dheight/2.2)
                    dcanvas.coords("cmp_pin",dwidth/2,dheight/1.85)
                    dcanvas.coords("cmp_email",dwidth/2,dheight/1.6)
                    dcanvas.coords("cmp_ph",dwidth/2,dheight/1.4)
                    dcanvas.coords("cmp_files",dwidth/2,dheight/1.25)
                    dcanvas.coords("button_cmp",dwidth/2,dheight/1.1)


                lf_cmpy1= Canvas(cmpny_dt_frm,height=650, width=500)
                lf_cmpy1.bind("<Configure>", responsive_wid_cmp1)
                lf_cmpy1.pack(fill=X)

                cmpny_hd=Label(lf_cmpy1, text="We're Happy you're Here!",font=('Calibri 30 bold'), fg="black")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_hd, tag=("cmpny_hd"))


                cmp_nm = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_nm.insert(0,"Company Name")
                cmp_nm.bind("<Button-1>",name_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_nm, tag=("nm_nm"))

                cmp_cmpn = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cmpn.insert(0,"Company Address")
                cmp_cmpn.bind("<Button-1>",cmp_add)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cmpn, tag=("cmp_cmpn"))

                cmp_cty = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cty.insert(0,"City")
                cmp_cty.bind("<Button-1>",cty_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cty, tag=("cmp_cty"))

                cmp_stat = StringVar()
                cmpny_cntry = ttk.Combobox(lf_cmpy1,textvariable=cmp_stat,width=29,font=('Calibri 16'))
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_cntry, tag=("cmpny_cntry"))
                cmpny_cntry['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
                cmpny_cntry.current(0)

                cmp_pin = Spinbox(lf_cmpy1,from_=1,to=1000000,width=29, font=('Calibri 16'),borderwidth=2)
                cmp_pin.delete(0,END)
                cmp_pin.insert(0,"Pincode")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_pin, tag=("cmp_pin"))

                def validateb211(value):
        
                        """
                        Validat the email entry
                        :param value:
                        :return:
                        """
                        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                        if re.fullmatch(pattern, value) is None:
                            
                            return False

                        cmp_email.config(fg="black")
                        return True

                def on_invalidb211():
                        cmp_email.config(fg="red")
                        

                cmp_email = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_email.insert(0,"Email")
                cmp_email.bind("<Button-1>",em_ent)
                vcmdb211 = (lf_cmpy1.register(validateb211), '%P')
                ivcmdb211 = (lf_cmpy1.register(on_invalidb211),)
                cmp_email.config(validate='focusout', validatecommand=vcmdb211, invalidcommand=ivcmdb211)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_email, tag=("cmp_email"))

                cmp_ph = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_ph.insert(0,"Phone Number")
                cmp_ph.bind("<Button-1>",ph_ent)
                def validate_telb51(value):
        
                        pattern = r'^[0-9]\d{9}$'
                        if re.fullmatch(pattern, value) is None:
                            
                            return False
                        cmp_ph.config(fg="black")
                        return True

                def on_invalid_telb51():
                        cmp_ph.config(fg="red")
                        
                v_tel_cmdb51 = (lf_cmpy1.register(validate_telb51), '%P')
                iv_tel_cmdb51 = (lf_cmpy1.register(on_invalid_telb51),)
                cmp_ph.config(validate='focusout', validatecommand=v_tel_cmdb51, invalidcommand=iv_tel_cmdb51)

                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_ph, tag=("cmp_ph"))

                cmp_files = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_files.insert(0,"No file Chosen")
                cmp_files.bind("<Button-1>",fil_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_files, tag=("cmp_files"))

                button_cmp = customtkinter.CTkButton(master=lf_cmpy1,command=cmpny_crt2,text="Next",bg="#213b52")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=button_cmp, tag=("button_cmp"))
            else:
                messagebox.showerror("Sign Up Failed","password and conform password does not match")
        else:
            messagebox.showerror("Sign Up Failed","Username and password already exist")
    else:
        if password==con_password and con_password==password :
                
                signup_sql="insert into auth_user(first_name,last_name,email,username,password) VALUES(%s,%s,%s,%s,%s)" #adding values into db
                signup_sql_val=(first_name,last_name,email,username,password,)
                fbcursor.execute(signup_sql,signup_sql_val,)
                finsysdb.commit()
                try:
                    main_frame_cmpny2.pack_forget()
                except:
                    pass
                try:
                    main_frame_signup.pack_forget()
                except:
                    pass
                
                main_frame_cmpny=Frame(root, height=750,bg="#213b52")
                main_frame_cmpny.pack(fill=X,)

                cmpny_dt_frm=Frame(main_frame_cmpny, height=650, width=500,bg="white")
                cmpny_dt_frm.pack(pady=50)

                def name_ent(event):
                    if nm_nm.get()=="Company Name":
                        nm_nm.delete(0,END)
                    else:
                        pass

                def cmp_add(event):
                    if cmp_cmpn.get()=="Company Address":
                            cmp_cmpn.delete(0,END)
                    else:
                        pass
                def cty_ent(event):
                    if cmp_cty.get()=="City":
                        cmp_cty.delete(0,END)
                    else:
                        pass

                def em_ent(event):
                    if cmp_email.get()=="Email":
                            cmp_email.delete(0,END)
                    else:
                        pass
                def ph_ent(event):
                    if cmp_ph.get()=="Phone Number":
                        cmp_ph.delete(0,END)
                    else:
                        pass

                def fil_ent(event):
                    
                    cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
                    logo_crp=cmp_logo.split('/',-1)
                    im1 = Image.open(r""+cmp_logo) 
                    im1 = im1.save("profilepic/propic.jpg")
                    
                    cmp_files.delete(0,END)
                    cmp_files.insert(0,logo_crp[-1])
                
                def responsive_wid_cmp1(event):
                    dwidth = event.width
                    dheight = event.height
                    dcanvas = event.widget
            

                    dcanvas.coords("cmpny_hd",dwidth/2,dheight/13)
                    dcanvas.coords("nm_nm",dwidth/2,dheight/5)
                    dcanvas.coords("cmp_cmpn",dwidth/2,dheight/3.5)
                    dcanvas.coords("cmp_cty",dwidth/2,dheight/2.7)
                    dcanvas.coords("cmpny_cntry",dwidth/2,dheight/2.2)
                    dcanvas.coords("cmp_pin",dwidth/2,dheight/1.85)
                    dcanvas.coords("cmp_email",dwidth/2,dheight/1.6)
                    dcanvas.coords("cmp_ph",dwidth/2,dheight/1.4)
                    dcanvas.coords("cmp_files",dwidth/2,dheight/1.25)
                    dcanvas.coords("button_cmp",dwidth/2,dheight/1.1)


                lf_cmpy1= Canvas(cmpny_dt_frm,height=650, width=500)
                lf_cmpy1.bind("<Configure>", responsive_wid_cmp1)
                lf_cmpy1.pack(fill=X)

                cmpny_hd=Label(lf_cmpy1, text="We're Happy you're Here!",font=('Calibri 30 bold'), fg="black")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_hd, tag=("cmpny_hd"))


                nm_nm = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
                nm_nm.insert(0,"Company Name")
                nm_nm.bind("<Button-1>",name_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=nm_nm, tag=("nm_nm"))

                cmp_cmpn = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cmpn.insert(0,"Company Address")
                cmp_cmpn.bind("<Button-1>",cmp_add)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cmpn, tag=("cmp_cmpn"))

                cmp_cty = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_cty.insert(0,"City")
                cmp_cty.bind("<Button-1>",cty_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_cty, tag=("cmp_cty"))

                invset_bg_var = StringVar()
                cmpny_cntry = ttk.Combobox(lf_cmpy1,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmpny_cntry, tag=("cmpny_cntry"))
                cmpny_cntry['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
                cmpny_cntry.current(0)

                cmp_pin = Spinbox(lf_cmpy1,from_=1,to=1000000,width=29, font=('Calibri 16'),borderwidth=2)
                cmp_pin.delete(0,END)
                cmp_pin.insert(0,"Pincode")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_pin, tag=("cmp_pin"))
            

                cmp_email = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_email.insert(0,"Email")
                cmp_email.bind("<Button-1>",em_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_email, tag=("cmp_email"))

                cmp_ph = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_ph.insert(0,"Phone Number")
                cmp_ph.bind("<Button-1>",ph_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_ph, tag=("cmp_ph"))

                cmp_files = Entry(lf_cmpy1, width=30, font=('Calibri 16'),borderwidth=2)
                cmp_files.insert(0,"No file Chosen")
                cmp_files.bind("<Button-1>",fil_ent)
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=cmp_files, tag=("cmp_files"))

                button_cmp = customtkinter.CTkButton(master=lf_cmpy1,command=cmpny_crt2,text="Next",bg="#213b52")
                win_inv1 = lf_cmpy1.create_window(0, 0, anchor="center", window=button_cmp, tag=("button_cmp"))
        else:
                messagebox.showerror("Sign Up Failed","password and conform password does not match")
  
#--------------------------------------------------------------------------------------------------------Sign in frame in signup section
def fun_sign_in():
    bs_nm=nm_nm2.get()
    ind_type=industry_tp.get()
    com_typ=cmp_type.get()
    acount_manage=bs_act_man.get()
    paid_type=paid_typ.get()

    sql_log_sql='select id from auth_user where username=%s'
    sql_log_sql_val=(sys_usr.get(),)
        
    fbcursor.execute(sql_log_sql,sql_log_sql_val,)
    id=fbcursor.fetchone()
    signup_cmp_sql="update app1_company set bname=%s,industry=%s,ctype=%s,abt=%s,paid=%s  where id_id=%s" #adding values into db
    signup_cmp_sql_val=(bs_nm,ind_type,com_typ,acount_manage,paid_type,id[0],)
    fbcursor.execute(signup_cmp_sql,signup_cmp_sql_val,)
    finsysdb.commit()


    try:
        main_frame_signup.pack_forget()
    except:
        pass
    try:
        main_frame_cmpny2.pack_forget()
    except:
        pass

    main_frame_signin.pack(fill=X,)
    
#---------------------------------------------------------------------------------------------------------------------Sign Up Section
def func_sign_up():
    
    global main_frame_signup,fst_nm,lst_nm,sys_em,sys_usr,sys_pass,sys_cf
    main_frame_signin.pack_forget()

    main_frame_signup=Frame(root, height=750)
    main_frame_signup.pack(fill=X,)

    def responsive_wid_signup(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("round_signup",dwidth/2,-dheight/.5,dwidth/.7,dheight/.5)
        dcanvas.coords("sign_in_lb",dwidth/6,dheight/12)
        dcanvas.coords("fst_nm",dwidth/8.5,dheight/5)
        dcanvas.coords("lst_nm",dwidth/8.5,dheight/3.5)
        dcanvas.coords("sys_em",dwidth/8.5,dheight/2.7)
        dcanvas.coords("sys_usr",dwidth/8.5,dheight/2.2)
        dcanvas.coords("sys_pass",dwidth/8.5,dheight/1.85)
        dcanvas.coords("sys_cf",dwidth/8.5,dheight/1.6)
        dcanvas.coords("button_sign",dwidth/6,dheight/1.4)
        dcanvas.coords("lft_lab",dwidth/1.4,dheight/18)
        dcanvas.coords("lft_lab2",dwidth/1.52,dheight/10)
        dcanvas.coords("btn_signup2",dwidth/1.36,dheight/6.6)
        dcanvas.coords("label_img",dwidth/1.8,dheight/5)
        
        


    lf_signup= Canvas(main_frame_signup,width=1500, height=1500)
    lf_signup.bind("<Configure>", responsive_wid_signup)
    lf_signup.pack(fill=X)

    lf_signup.create_oval(0,0,0,0,fill="#213b52", tag=("round_signup"))

    # #--------------------------------------------------------------------------------sign up section
    sign_in_lb=Label(lf_signup, text="Sign Up",font=('Calibri 30 bold'), fg="black")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sign_in_lb, tag=("sign_in_lb"))

    def nme(event):
        if fst_nm.get()=="Firstname":
            fst_nm.delete(0,END)
        else:
            pass

    def nme1(event):
        if lst_nm.get()=="Lastname":
            lst_nm.delete(0,END)
        else:
            pass
        
    def nme2(event):
        if sys_em.get()=="Email":
            sys_em.delete(0,END)
        else:
            pass
        
        
    def nme3(event):
        if sys_usr.get()=="Username":
            sys_usr.delete(0,END)
        else:
            pass
        
    def nme4(event):
        if sys_pass.get()=="Password":
            sys_pass.delete(0,END)
            messagebox.showerror("Password Format","The password length must be greater than or equal to 8 \n>The password must contain one or more uppercase characters\n>The password must contain one or more lowercase characters\n>The password must contain one or more numeric values\n>The password must contain one or more special characters")
        else:
            pass
    
    def nme5(event):
        if sys_cf.get()=="Confirm Password":
            sys_cf.delete(0,END)
        else:
            pass
    
    

    fst_nm = Entry(lf_signup, width=25, font=('Calibri 16'))
    fst_nm.insert(0,"Firstname")
    fst_nm.bind("<Button-1>",nme)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=fst_nm, tag=("fst_nm"))

    lst_nm = Entry(lf_signup,  width=25, font=('Calibri 16'))
    lst_nm.insert(0,"Lastname")
    lst_nm.bind("<Button-1>",nme1)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lst_nm, tag=("lst_nm"))

    
    sys_em = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_em.insert(0,"Email")
    sys_em.bind("<Button-1>",nme2)
    def validateb211(value):
        
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value) is None:
                            
            return False

        sys_em.config(fg="black")
        return True

    def on_invalidb211():
        
        sys_em.config(fg="red")

    vcmdb211 = (lf_signup.register(validateb211), '%P')
    ivcmdb211 = (lf_signup.register(on_invalidb211),)
    sys_em.config(validate='focusout', validatecommand=vcmdb211, invalidcommand=ivcmdb211)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_em, tag=("sys_em"))

    sys_usr = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_usr.insert(0,"Username")
    sys_usr.bind("<Button-1>",nme3)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_usr, tag=("sys_usr"))

    sys_pass = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_pass.insert(0,"Password")
    sys_pass.bind("<Button-1>",nme4)
    def pas_val_fun(value):
        
        pattern = r'(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
        if re.fullmatch(pattern, value) is None:
                            
            return False

        sys_pass.config(fg="black")
        return True

    def pass_inval_fun():
        sys_pass.config(fg="red")

    pas_val = (lf_signup.register(pas_val_fun), '%P')
    pass_inval = (lf_signup.register(pass_inval_fun),)

    sys_pass.config(validate='focusout', validatecommand=pas_val, invalidcommand=pass_inval)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_pass, tag=("sys_pass"))

    sys_cf = Entry(lf_signup, width=25, font=('Calibri 16'))
    sys_cf.insert(0,"Confirm Password")
    sys_cf.bind("<Button-1>",nme5)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sys_cf, tag=("sys_cf"))

    button_sign = customtkinter.CTkButton(master=lf_signup, command=cmpny_crt1,text="Sign Up",bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=button_sign, tag=("button_sign"))

    label_img = Label(lf_signup, image = sign_up,bg="#213b52", width=800,anchor="w")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=label_img, tag=("label_img"))
    
    

    lft_lab=Label(lf_signup, text="One of us ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab, tag=("lft_lab"))
    lft_lab2=Label(lf_signup, text="click here for work with FinsYs.",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab2, tag=("lft_lab2"))

    btn_signup2 = Button(lf_signup, text='Sign In', command=fun_sign_in, bg="white", fg="black",borderwidth = 3,height=1,width=10)
    win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=btn_signup2, tag=("btn_signup2"))


main_frame_signin=Frame(root, height=750)
main_frame_signin.pack(fill=X,)


def sig_nm(event):
        if nm_ent.get()=="Username":
            nm_ent.delete(0,END)
        else:
            pass

def sig_pass(event):
        if pass_ent.get()=="Password":
            pass_ent.delete(0,END)
        else:
            pass


def responsive_wid_login(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
   

        dcanvas.coords("sign_inlb",dwidth/1.4,dheight/4)

        dcanvas.coords("nm_ent",dwidth/1.5,dheight/2.7)
        dcanvas.coords("pass_ent",dwidth/1.5,dheight/2.2)
        dcanvas.coords("button",dwidth/1.4,dheight/1.8)
        dcanvas.coords("round_login",-dwidth/2,-dheight/.5,dwidth/2,dheight/.5)
        dcanvas.coords("lft_lab",dwidth/4,dheight/18)
        dcanvas.coords("lft_lab2",dwidth/6,dheight/10)
        dcanvas.coords("btn2",dwidth/3.7,dheight/6.6)
        dcanvas.coords("img",dwidth/16,dheight/5.5)
    

lf_signup= Canvas(main_frame_signin,width=1366,height=750)
lf_signup.bind("<Configure>", responsive_wid_login)
lf_signup.pack(fill=X)

sign_inlb=Label(lf_signup, text="Sign In",font=('Calibri 30 bold'), fg="black")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=sign_inlb, tag=("sign_inlb"))

nm_ent = Entry(lf_signup, width=25, font=('Calibri 16'))
nm_ent.insert(0,"Username")
nm_ent.bind("<Button-1>",sig_nm)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=nm_ent, tag=("nm_ent"))

pass_ent = Entry(lf_signup, width=25, font=('Calibri 16'))
pass_ent.insert(0,"Password")
pass_ent.bind("<Button-1>",sig_pass)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=pass_ent, tag=("pass_ent"))

button = customtkinter.CTkButton(master=main_frame_signin,command=main_sign_in,text="Log In",bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=button, tag=("button"))

# #------------------------------------------------------------------------------------------------------------------------left canvas

lf_signup.create_oval(0,0,0,0,fill="#213b52", tag=("round_login"))

img = Label(lf_signup, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=img, tag=("img"))

lft_lab=Label(lf_signup, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab, tag=("lft_lab"))
lft_lab2=Label(lf_signup, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=lft_lab2, tag=("lft_lab2"))

btn2 = Button(main_frame_signin, text = 'Sign Up', command = func_sign_up, bg="white", fg="black",borderwidth = 3,height=1,width=10)
win_inv1 = lf_signup.create_window(0, 0, anchor="nw", window=btn2, tag=("btn2"))

root.mainloop()