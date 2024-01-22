import tkinter
from time import strftime
import tkinter as tk
import tkinter
from datetime import datetime
import mysql.connector
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np


mydata=[]
class Face_Recognition_System:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1800x780+0+0")
        self.root.state('zoomed')
        self.root.title("Face Recognition System")
        root.config(bg="white")
        root.overrideredirect(True)

        self.root.wm_iconbitmap("camera.ico")
        self.screenwidth = int(root.winfo_screenwidth())
        self.screenheight = int(root.winfo_screenheight())
        # print(screenheight)
        # print(screenwidth)


        self.options_frame = tk.Frame(root,bg='#c3c3c3')
        w = root.winfo_screenheight()/18
        # print(w)
        global college_img
        img=Image.open(r"C:\Users\OsamaAyman\Desktop\Grad_proj\images\2.png")
        img=img.resize((int(self.screenwidth/10),int(self.screenheight/8)),Image.Resampling.LANCZOS)
        college_img=ImageTk.PhotoImage(img)

        College_label=Label(self.options_frame,image=college_img, background = '#c3c3c3')
        College_label.place(x=0,y=0,width=self.screenwidth/10,height=self.screenheight/8)

        home_btn = tk.Button (self.options_frame, text="Home", font=('Bold ', 18),fg= '#158aff', bd=0, bg='#c3c3c3',command=lambda :self.indicate(self.home_indicate,self.home_page))
        home_btn.place(x=10,y=self.screenheight/3)
        self.home_indicate = tk.Label(self.options_frame, text='',bg='#c3c3c3')
        self.home_indicate.place(x=4,y=self.screenheight/3,width=5,height=43)

        menu_btn = tk.Button (self.options_frame, text="Recognition", font=('Bold ', 18),fg= '#158aff', bd=0, bg='#c3c3c3',command=lambda :self.indicate(self.menu_indicate,self.recognition_page))
        menu_btn.place(x=10,y=self.screenheight/3+w)
        self.menu_indicate = tk.Label(self.options_frame, text='',bg='#c3c3c3')
        self.menu_indicate.place(x=4,y=self.screenheight/3+w,width=5,height=43)

        contact_btn = tk.Button (self.options_frame, text="Help", font=('Bold ', 18),fg= '#158aff', bd=0, bg='#c3c3c3',command=lambda :self.indicate(self.contact_indicate,self.contact_page))
        contact_btn.place(x=10,y=self.screenheight/3+2*w)
        self.contact_indicate = tk.Label(self.options_frame, text='',bg='#c3c3c3')
        self.contact_indicate.place(x=4,y=self.screenheight/3+2*w,width=5,height=43)

        about = tk.Button (self.options_frame, text="EXIT", font=('Bold ', 18),fg= '#158aff', bd=0,relief=RIDGE, bg='#c3c3c3',command=self.IExit)
        about.place(x=10,y=self.screenheight/3+3*w)
        self.about_indicate = tk.Label(self.options_frame, text='',bg='#c3c3c3')
        self.about_indicate.place(x=4,y=self.screenheight/3+3*w,width=5,height=43)


        self.options_frame.pack(side=tk.LEFT)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=self.screenwidth/10,height=self.screenheight)


        self.main_frame = tk.Frame(root,highlightbackground='#c3c3c3',highlightthickness=0)
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=self.screenwidth-self.screenwidth/10,height=self.screenheight)

        self.home_page()

        #========================= Display time =========================
        def time():
                string = strftime('%H:%M:%S %p')
                Ibl.config(text=string)
                Ibl.after(1000, time)

        Ibl = Label(self.options_frame, font =('Bold',16),background='#c3c3c3',foreground='#158aff',padx=0)
        Ibl.place(x=0,y=self.screenheight-self.screenheight/10,width=160,height=50)
        time()        
        #========================= END Display time =========================

        
        

    def home_page(self):
        global photoimg
               
        photowidth = int(self.screenwidth-self.screenwidth/10)
        photoheight = int(self.screenheight)
        img=Image.open(r"C:\Users\OsamaAyman\Desktop\Grad_proj\images\bg.jpg")
        img=img.resize((photowidth,photoheight),Image.Resampling.LANCZOS)
        photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.main_frame,image=photoimg)
        bg_img.place(x=0,y=0,width=self.screenwidth-self.screenwidth/10,height=self.screenheight)
    
        

        buttons_frame = tk.Frame(self.main_frame,bg="#c3c3c3",highlightbackground='white',highlightthickness=0)
        buttons_frame.pack(side=tk.TOP,anchor=E,pady=(20,0))
        buttons_frame.grid_propagate(False)
        buttons_frame.configure(width=self.screenwidth-self.screenwidth/10,height=self.screenheight/25)

        buttons_frame.columnconfigure(0,weight=99)
        buttons_frame.columnconfigure(1,weight=1)
        buttons_frame.columnconfigure(2,weight=1)
        buttons_frame.columnconfigure(3,weight=1)
        buttons_frame.columnconfigure(4,weight=99)

        buttons_frame.rowconfigure(0,weight=3)
        buttons_frame.rowconfigure(1,weight=8)




        self.student_button = tk.Button (buttons_frame, text="Student Details", font=('Bold ', 18),fg= '#158aff',padx=0, bd=0, bg='#c3c3c3',command=lambda :self.indicate(self.home_indicate,self.student_page))
        self.student_button.grid(row=0,column=1,padx=0)
        # self.student_indicate = tk.Label(buttons_frame, text='',bg='#158aff',width=22,pady=4)
        # self.student_indicate.grid(row=1,column=1,pady=3)

        self.attendance_button = tk.Button (buttons_frame, text="Attendance", font=('Bold ', 18),fg= '#158aff',padx=0, bd=0, bg='#c3c3c3',command=lambda :self.indicate(self.home_indicate,self.attendance_page))
        self.attendance_button.grid(row=0,column=2)
        # self.attendance_indicate = tk.Label(buttons_frame, text='',bg='#158aff',width=16,pady=4)
        # self.attendance_indicate.grid(row=1,column=2,pady=3)
       





    def recognition_page(self):
        global photoimg
               
        photowidth = int(self.screenwidth-self.screenwidth/10)
        photoheight = int(self.screenheight)
        img=Image.open(r"C:\Users\OsamaAyman\Desktop\Grad_proj\images\bg.jpg")
        img=img.resize((photowidth,photoheight),Image.Resampling.LANCZOS)
        photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.main_frame,image=photoimg)
        bg_img.place(x=0,y=0,width=self.screenwidth-self.screenwidth/10,height=self.screenheight)


         #FaceDetector button

        img5=Image.open(r"C:\Users\OsamaAyman\Desktop\Grad_proj\images\student.jpg")
        img5=img5.resize((int(self.screenwidth/6),int(self.screenwidth/6)),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recognition,bd=3 , background="#c3c3c3")
        b1.place(x=self.screenwidth/20,y=self.screenwidth/20,width = int(self.screenwidth/6), height=int(self.screenwidth/6))
        b1_label=Button(bg_img,text="Face Detector",cursor="hand2",font =('Bold ', 16),bg="#c3c3c3",fg="#158aff",bd=3,command=self.face_recognition)
        b1_label.place(x=self.screenwidth/20,y=self.screenwidth/20+int(self.screenwidth/6),width = int(self.screenwidth/6), height=int(self.screenwidth/60))


         #Train databutton

        img7=Image.open(r"C:\Users\OsamaAyman\Desktop\Grad_proj\images\train.jpg")
        img7=img7.resize((int(self.screenwidth/6),int(self.screenwidth/6)),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_classifier,bd=3 , background="#c3c3c3")
        b1.place(x=self.screenwidth/20,y=(self.screenwidth/20)*1.5+int(self.screenwidth/6)+int(self.screenwidth/40),width = int(self.screenwidth/6), height=int(self.screenwidth/6))

        b1_label=Button(bg_img,text="Train Data",cursor="hand2",font =('Bold ', 16),bg="#c3c3c3",fg="#158aff",bd=3 ,command=self.train_classifier)
        b1_label.place(x=self.screenwidth/20,y=(self.screenwidth/20)*1.5+int(self.screenwidth/6)*2+int(self.screenwidth/40),width = int(self.screenwidth/6), height=int(self.screenwidth/60))
        

        
    def contact_page(self):
        home_frame = tk.Frame(self.main_frame)
        lb= tk.Label(home_frame,text='bbbbbbbbbb Frame\n\nPage: 1',font=('bold',50))
        lb.pack()
        home_frame.pack()
    def about_page(self):
        home_frame = tk.Frame(self.main_frame)
        lb= tk.Label(home_frame,text='aaaaaaaaaa Frame\n\nPage: 1',font=('bold',50))
        lb.pack()
        home_frame.pack()
    def delete_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()
    def indicate(self,lb,page):
        self.home_indicate.config(bg="#c3c3c3")
        self.menu_indicate.config(bg="#c3c3c3")
        self.contact_indicate.config(bg="#c3c3c3")
        self.about_indicate.config(bg="#c3c3c3")
        self.delete_page()
        page()

        lb.config(bg='#158aff')
    def student_page(self):
        self.home_page()
        self.student_button.configure(bd=1,relief=SUNKEN)
        main_student_frame = tk.Frame(self.main_frame,bg="#243641",highlightbackground='red',highlightthickness=0)
        main_student_frame.pack(side=tk.TOP,anchor=CENTER,pady=0)
        main_student_frame.grid_propagate(False)
        main_student_frame.configure(width=(self.screenwidth-self.screenwidth/10),height=self.screenheight-self.screenheight/25)
        #============================ Variables ================

        self.var_dep = StringVar()
        self.var_std_id = StringVar()

        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_phone = StringVar()
        self.var_teacher = StringVar()

        
        left_frame=LabelFrame(main_student_frame, bd=1,font=("times new roman",14,"bold"),text="Student Details",bg='white',pady=10 ,padx=10, relief=RIDGE,fg="#00008B")
        left_frame.grid(row=1,column=0,sticky='WENS',padx=0,pady=5)

        left_frame.grid_propagate(False)
        left_frame.configure(width=(self.screenwidth-self.screenwidth/10)/2,height=self.screenheight-self.screenheight/25)
        
        # left_frame.rowconfigure(0,weight=1)
        # left_frame.rowconfigure(1,weight=3)
        # left_frame.rowconfigure(2,weight=3)


        left_frame.columnconfigure(0,weight=1)
        left_frame.columnconfigure(1,weight=1)

        img_left=Image.open(r"C:\Users\OsamaAyman\Desktop\Grad_proj\images\2.png")
        global photoimg_left
        photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(left_frame,image=photoimg_left,bg="#DDFFFD")
        f_lb1.grid(row=0,column=0,columnspan=2,sticky="WNE")

        current_course_frame=LabelFrame(left_frame, bd=4,font=("times new roman",14,"bold"),text="Current course information",bg='white',padx=10, relief=RIDGE,fg="#00008B")
        current_course_frame.grid(row=1,column=0,columnspan=2,sticky='WENS',padx=5,pady=5)


        # Department
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky="W")
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",14,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select department","Computer","IT","Civil","Medical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=4,pady=10,sticky="W")


    # Course
        dep_label=Label(current_course_frame,text="Course:",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=10,sticky="W")
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",14,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select course","Data structure","Computer networks","Embedded system","Computer vision")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=4,pady=10,sticky="W")

        # Year
        dep_label=Label(current_course_frame,text="Year:",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky="W")
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",14,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Year","2022-2023","2023-2024","2024-2025","2025-2026")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=4,pady=10)

        # Semester
        dep_label=Label(current_course_frame,text="Semester:",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,sticky="W")
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",14,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Semester","2022-2023","2023-2024","2024-2025","2025-2026")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=4,pady=10,sticky="W")


    #=========================== Class Student information=============================

        class_student_frame=LabelFrame(left_frame, bd=4,font=("times new roman",14,"bold"),text="Class Student Information",bg='white',padx=10, relief=RIDGE,fg="#00008B")
        class_student_frame.grid(row=2,column=0,columnspan=2,sticky='WENS',padx=5,pady=5)



        #student ID
        student_frame=Label(class_student_frame,text="StudentID:",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=0,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=0,column=1,padx=10,pady=5,sticky="W")

        #student name
        student_frame=Label(class_student_frame,text="Student name:",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=0,column=2,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=0,column=3,padx=10,pady=5,sticky="W")


        #Roll number
        student_frame=Label(class_student_frame,text="Roll number:-",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=1,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=1,column=1,padx=10,pady=5,sticky="W")


        #Gender
        student_frame=Label(class_student_frame,text="Gender:-",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=1,column=2,padx=10,sticky="W")

        # student_entry=ttk.Entry(class_student_frame,textvariable=var_gender,width=20,font=("times new roman",14,"bold"))
        # student_entry.grid(row=1,column=3,padx=10,pady=5,sticky="W")
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",14,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Select gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=4,pady=10)


        #Email
        student_frame=Label(class_student_frame,text="Email:-",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=2,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=2,column=1,padx=10,pady=5,sticky="W")

        #Phone number
        student_frame=Label(class_student_frame,text="Phone number:-",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=2,column=2,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=2,column=3,padx=10,pady=5,sticky="W")


        #Adress
        student_frame=Label(class_student_frame,text="Adress:-",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=3,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=3,column=1,padx=10,pady=5,sticky="W")


        #Date of birth
        student_frame=Label(class_student_frame,text="Date of birth:-",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=3,column=2,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=3,column=3,padx=10,pady=5,sticky="W")


        #Class division
        student_frame=Label(class_student_frame,text="Class division:",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=4,column=2,padx=10,sticky="W")

        # student_entry=ttk.Entry(class_student_frame,textvariable=var_div,width=20,font=("times new roman",14,"bold"))
        # student_entry.grid(row=4,column=3,padx=10,pady=5,sticky="W")
        Div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",14,"bold"),width=18,state="readonly")
        Div_combo["values"]=("Select div","A","B","C","D")
        Div_combo.current(0)
        Div_combo.grid(row=4,column=3,padx=4,pady=10)


        #Teacher
        student_frame=Label(class_student_frame,text="Teacher:",font=("times new roman",14,"bold"),bg="white")
        student_frame.grid(row=4,column=0,padx=10,sticky="W")

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",14,"bold"))
        student_entry.grid(row=4,column=1,padx=10,pady=5,sticky="W")



    #===================================== Radio buttons ======================================
        self.var_radio1 = StringVar()
        Radiobutton1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="yes")
        Radiobutton1.grid(row=5,column=0)

        # var_radio2 = StringVar()

        Radiobutton2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="no photo sample",value="No")
        Radiobutton2.grid(row=5,column=1)

    #=====================================  buttons frame ======================================

        # buttons_frame = Frame(class_student_frame,bd=2 , relief= RIDGE)
        # buttons_frame.grid(row=6 , column=0)

        buttons_frame=LabelFrame(left_frame, bd=4,font=("times new roman",14,"bold"),text="Class Student Information",bg='white',padx=10, relief=RIDGE,fg="#00008B" )
        buttons_frame.grid(row=3,column=0,columnspan=2,sticky='WENS',padx=5,pady=5)

        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)
        buttons_frame.columnconfigure(2, weight=1)
        buttons_frame.columnconfigure(3, weight=1)


        save_button = Button(buttons_frame,command =self.add_data,text="Save",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        save_button.grid(row=6,column=0,sticky="WENS",pady=2 ,padx=2)

        update_button = Button(buttons_frame,command=self.update_data,text="Update",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        update_button.grid(row=6,column=1,sticky="WENS",pady=2,padx=2)

        delete_button = Button(buttons_frame,command=self.delete_data,text="Delete",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        delete_button.grid(row=6,column=2,sticky="WENS",pady=2,padx=2)

        Reset_button = Button(buttons_frame,command=self.reset_data,text="Reset",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        Reset_button.grid(row=6,column=3,sticky="WENS",pady=2,padx=2)

        take_photo_button = Button(buttons_frame,command=self.generate_dataset,text="Take photo sample",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        take_photo_button.grid(row=7,column=0, columnspan=2,sticky="WENS",pady=2,padx=2)

        update_photo_button = Button(buttons_frame,text="Update photo sample",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        update_photo_button.grid(row=7,column=2 ,columnspan=2,sticky="WENS",pady=2,padx=2)


    #================= RIGHT FRAME =====================

        right_frame=LabelFrame(main_student_frame, bd=1,font=("times new roman",14,"bold"),text="Student Details",bg='white',pady=10 ,padx=10, relief=RIDGE,fg="#00008B")
        right_frame.grid(row=1,column=1,sticky='W',padx=0,pady=5)

        right_frame.grid_propagate(False)
        right_frame.configure(width=(self.screenwidth-self.screenwidth/10)/2,height=self.screenheight-self.screenheight/25)
        
        
        # right_frame.rowconfigure(0,weight=1)
        # right_frame.rowconfigure(1,weight=3)
        # right_frame.rowconfigure(2,weight=3)


        right_frame.columnconfigure(0,weight=1)
        right_frame.columnconfigure(1,weight=1)

        img_right=Image.open(r"C:\Users\OsamaAyman\Desktop\Grad_proj\images\2.png")
        global photoimg_right
        photoimg_right=ImageTk.PhotoImage(img_right)

        f_lb1=Label(right_frame,image=photoimg_right,bg="#DDFFFD")
        f_lb1.grid(row=0,column=0,columnspan=2,sticky="We")

        current_course_frame=LabelFrame(right_frame, bd=4,font=("times new roman",14,"bold"),text="Current course information",bg='white',padx=10, relief=RIDGE,fg="#00008B")
        current_course_frame.grid(row=1,column=0,columnspan=2,sticky='W',padx=5,pady=5)
        current_course_frame.grid_propagate(False)
        current_course_frame.configure(width=(self.screenwidth-self.screenwidth/10)/2 , height= self.screenheight/14)



        current_course_frame.columnconfigure(0,weight=1)
        current_course_frame.columnconfigure(1,weight=1)
        current_course_frame.columnconfigure(2,weight=1)
        current_course_frame.columnconfigure(3,weight=1)
        current_course_frame.columnconfigure(4,weight=1)



        # Department
        dep_label=Label(current_course_frame,text="Search by:",font=("times new roman",14,"bold"),bg="red")
        dep_label.grid(row=0,column=0,padx=1,sticky="wens")
        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",14,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select","Roll number","Phone number")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=4,pady=1,sticky="wens")

        search_entnry = ttk.Entry(current_course_frame,width=30,font=("times new roman",14,"bold"))
        search_entnry.grid(row=0,column=2,padx=1,sticky="wens")

        save_button = Button(current_course_frame,text="Search",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        save_button.grid(row=0,column=3,sticky="wens",pady=0 ,padx=2 ,ipady=0 , ipadx=1)

        showall_button = Button(current_course_frame,text="Show all",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
        showall_button.grid(row=0,column=4,sticky="wens",pady=0,padx=2 ,ipady=0 ,ipadx=1)






    #=================================== TABLE FRAME ==============================



        

        

        table_frame = Frame(right_frame,bd=0,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=self.screenheight/3.5,width=(self.screenwidth-self.screenwidth/10)/2.08)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","adress","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("adress",text="Adress")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")


        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("adress",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_studentdetails_cursor)
        self.fetch_data()

     #=============================== function decleration ====================
    def add_data(self):
        if self.var_dep.get() == "Select department" or self.var_std_name.get() == "" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_reocognizer")
                my_cursor =conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added succeffully",parent=self.root)
            except Exception as es:
                messagebox.showerror("error" , f"Due to : {str(es)}",parent=self.root)
    def attendance_page(self):
        self.home_page()
        self.attendance_button.configure(bd=1,relief=SUNKEN)

        main_attendance_frame = tk.Frame(self.main_frame,bg="#111111",highlightbackground='red',highlightthickness=0)
        main_attendance_frame.pack(side=tk.TOP,anchor=E,pady=0)
        main_attendance_frame.grid_propagate(False)
        main_attendance_frame.configure(width=self.screenwidth-self.screenwidth/10,height=self.screenheight-self.screenheight/25)
        #===========variables=============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()




    #lef tlable frame
        Left_frame=LabelFrame(main_attendance_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance  Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=0,y=0,width=(self.screenwidth-self.screenwidth/10)/2,height=self.screenheight-self.screenheight/25)



        img_left=Image.open(r"C:\Users\OsamaAyman\Desktop\Grad_proj\images\attendance1.png")
        img_left=img_left.resize((int((self.screenwidth-self.screenwidth/10)/2),int(self.screenheight/3)),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=int((self.screenwidth-self.screenwidth/10)/2),height=int(self.screenheight/3))

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=self.screenheight/3,width=(self.screenwidth-self.screenwidth/10)/2,height=self.screenheight-self.screenheight/25-(int(self.screenheight/3)))
        left_inside_frame.columnconfigure(0,weight=1)
        left_inside_frame.columnconfigure(1,weight=1)
        left_inside_frame.columnconfigure(2,weight=1)
        left_inside_frame.columnconfigure(3,weight=1)

        #Labeland entry
        #attendance ID
        attendanceId_label=Label(left_inside_frame,text="AttendanceId:",bg="white",font="comicsansns 11 bold")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_id,font="comicsansns 11 bold")
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5)

        #Name
        rollLabel=Label(left_inside_frame,text="Roll:",bg="white",font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)
        
        #date
        nameLabel=Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,pady=8)

        #Department
        depLabel=Label(left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=8)

        #time
        timeLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)

        #date
        dateLabel=Label(left_inside_frame,text="Date:",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)

        #attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance status:",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #buttons frame
       

        save_btn=Button(left_inside_frame,text="Import csv",command=self.importCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=4,column=0,pady=self.screenheight/20,sticky="nes")

        update_btn=Button(left_inside_frame,text="Export csv",command=self.exportCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=4,column=1,pady=self.screenheight/20,sticky="nesw")

        delete_btn=Button(left_inside_frame,text="Update",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=4,column=2,pady=self.screenheight/20,sticky="nesw")

        reset_btn=Button(left_inside_frame,text="Reset",width=15,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=4,column=3,pady=self.screenheight/20,sticky="nsw")

        
        #right lable frame
        Right_frame=LabelFrame(main_attendance_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=(self.screenwidth-self.screenwidth/10)/2,y=0,width=(self.screenwidth-self.screenwidth/10)/2,height=self.screenheight-self.screenheight/25)

       


        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=0,y=0,width=int((self.screenwidth-self.screenwidth/10)/2),height=int(self.screenheight/1.6))


        

        img_right=Image.open(r"C:\Users\OsamaAyman\Desktop\Grad_proj\images\attendance2.jpg")
        img_right=img_right.resize((int((self.screenwidth-self.screenwidth/10)/2),int(self.screenheight/4.19)),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=0,y=self.screenheight/1.6,height=self.screenheight/4.19)
        #==================scroll br table==============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendaceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
       

        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("id",text="Attendance ID")
        self.AttendaceReportTable.heading("roll",text="Roll")
        self.AttendaceReportTable.heading("name",text="Name")
        self.AttendaceReportTable.heading("department",text="Department")
        self.AttendaceReportTable.heading("time",text="Time")
        self.AttendaceReportTable.heading("date",text="Date")
        self.AttendaceReportTable.heading("attendance",text="Attendance")

        self.AttendaceReportTable["show"]="headings"
        
        self.AttendaceReportTable.column("id",width=200)
        self.AttendaceReportTable.column("roll",width=200)
        self.AttendaceReportTable.column("name",width=200)
        self.AttendaceReportTable.column("department",width=200)
        self.AttendaceReportTable.column("time",width=200)
        self.AttendaceReportTable.column("date",width=200)
        self.AttendaceReportTable.column("attendance",width=200)

        self.AttendaceReportTable.pack(fill=BOTH,expand=1)

        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_attendance_cursor)

        #==================fetch data================
    def fetchData(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)
    #=============attendance============
    def mark_attendance(self,i,r,n,d):
        with open("omar.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

#================== Face recognition =====================

    def face_recognition(self):
        def draw_boundray(img,classifier,scaleFactor,minNighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNighbors)
            coord=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence =int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_reocognizer")
                my_cursor =conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)
                separator="my_id"
                

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                

                if confidence> 77:
                    cv2.putText(img,f"ID:{i}",(x,y-90),cv2.FONT_ITALIC,0.9,(255,255,255),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-65),cv2.FONT_ITALIC,0.9,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-40),cv2.FONT_ITALIC,0.9,(255,255,255),2)
                    cv2.putText(img,f"Department:{d}",(x,y-15),cv2.FONT_ITALIC,0.9,(255,255,255),2)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_ITALIC,0.9,(255,255,255),2)

                coord=[x,y,w,y]
            return coord
        


            
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img 
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img= video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release() 
        cv2.destroyAllWindows()
    #=============import csv===============
    def importCsv(self):        
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALI File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)    

    #============export csv================        
    def exportCsv(self):
        try:
            if len(mydata)<1:
              messagebox.showerror("No Data","No Data found to export",parent=self.root)
              return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALI File","*.*")),parent=self.root)  
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                 messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)        

    def get_attendance_cursor(self,event=""):
        cursor_row=self.AttendaceReportTable.focus()
        content=self.AttendaceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
    def train_classifier(self):
            data_dir=("data" )
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            faces=[] 
            ids=[]

            for image in path:
                img=Image.open(image).convert('L') #Gray scale image 
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)

            #============= Train the Classifier And save ========
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training datasets completed !") 
                
        



#===============================================================================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_reocognizer")
        my_cursor =conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END , values=i)
            conn.commit()
        conn.close()



#============================================ get cursor ================

    def get_studentdetails_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        # print(data)
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])


        #=========== update function ===========


    def update_data(self):
        if self.var_dep.get() == "Select department" or self.var_std_name.get() == "" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Are you sure you want to Update this student details",parent=self.root)

                if Update>0:

                    conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_reocognizer")
                    my_cursor =conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                            self.var_dep.get(),
                            self.var_course.get(),

                            self.var_year.get(),
                            self.var_semester.get(),

                            self.var_std_name.get(),

                            self.var_div.get(),

                            self.var_roll.get(),

                            self.var_gender.get(),

                            self.var_dob.get(),

                            self.var_email.get(),

                            self.var_phone.get(),

                            self.var_address.get(),

                            self.var_teacher.get(),
                            self.var_radio1.get(),

                            self.var_std_id.get(),







                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

        

#================== delete funtion 
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_reocognizer")
                    my_cursor =conn.cursor()
                    sql="delete from student where Student_id= %s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details deleted successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)



#========================= Reset funtion

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")

        self.var_year.set("Select Year")

        self.var_semester.set("Select Semester")

        self.var_std_id.set("")

        self.var_std_name.set("")

        self.var_div.set("Select Division")

        self.var_roll.set("")

        self.var_gender.set("Male")

        self.var_dob.set("")

        self.var_email.set("")

        self.var_phone.set("")

        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


#======= Generate data set or Take photo Samples =========

    def generate_dataset(self):
        if self.var_dep.get() == "Select department" or self.var_std_name.get() == "" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_reocognizer")
                my_cursor =conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                                                    self.var_dep.get(),
                                                    self.var_course.get(),

                                                    self.var_year.get(),
                                                    self.var_semester.get(),

                                                    self.var_std_name.get(),

                                                    self.var_div.get(),

                                                    self.var_roll.get(),

                                                    self.var_gender.get(),

                                                    self.var_dob.get(),

                                                    self.var_email.get(),

                                                    self.var_phone.get(),

                                                    self.var_address.get(),

                                                    self.var_teacher.get(),
                                                    self.var_radio1.get(),

                                                    self.var_std_id.get()==id+1



                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                # ======== load predifiend data on face frontals from opencv =========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3
                    #minimum neighbour = 5
                    for (x, y, w, h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def IExit(self):
                self.home_indicate.config(bg="#c3c3c3")
                self.menu_indicate.config(bg="#c3c3c3")
                self.contact_indicate.config(bg="#c3c3c3")
                self.about_indicate.config(bg="#c3c3c3")
                self.root.destroy()
                # self.IExit=tkinter.messagebox.askyesno("Face Recognitin","Are you sure you want to close the app!",parent=self.root)
                # if  self.IExit >0:
                #     self.root.destroy()
                # else:
                #     return  

    

        
if __name__== "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()