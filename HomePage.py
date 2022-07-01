# Imports 
from tkinter import *
import tkinter as tk
import os
from typing_extensions import Self
import webbrowser
import validators
import time as t
import cv2
from threading import Thread
from PIL import Image, ImageTk
from Button.state import changeState
from UserPage import UserPage
from Install.install import threadreq
import socket


#================================================HomePage=====================================================
class HomePage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("850x900")
        self.master.configure(bg='grey50')
        self.master.title('camera_testing')

        #Main frame 
        self.frame2 = tk.Frame(self.master, bg='grey50')

        self.button_border = tk.Frame(self.frame2, highlightbackground="black",highlightthickness=2, bd=0)

        # User button for User-Management
        self.user = tk.Button(self.frame2, bg="#242C35", height=3, width=20, bd=4, text='USER',font=("Helvetica",12,'bold'),
                              command=lambda: [self.new_window()], state=DISABLED, fg='white')
        #Start button to run Project                          
        self.start = tk.Button(self.frame2, bg="#242C35", height=3, width=20, bd=4, text='START',font=("Helvetica",12,'bold'), 
                                command= lambda : [self.threadlink(),Thread(traget=self.run()).start()], state=DISABLED, fg='white') #self.threadreq(), self.threadlink(),threadreq()
        #Camera button for camera management 
        self.cameraButton = tk.Button(self.frame2, bg="#242C35", height=3, width=20, text="CAMERA MANAGEMENT",font=("Helvetica",12,'bold'),
                                      command=lambda: [self.press(),
                                                       changeState(self.cameraButton, self.user, self.start)],
                                      state=NORMAL, fg='white')

        # Frame and button alignment
        self.user.pack(side =LEFT, anchor = NW,padx=30, pady=30, expand = True)
        self.start.pack(side = LEFT, expand = True, anchor = N,padx=30, pady=30)
        self.cameraButton.pack(side =LEFT, anchor = NE,padx=30, pady=30, expand = True)
        self.frame2.pack(fill="both", expand=True)

    # function to pop up Browser 
    def link(self):
        t.sleep(40)
        hostname = "".join(("//", socket.gethostbyname(socket.gethostname()))) 
        links = ":".join(("http",hostname,"8880"))
        webbrowser.open_new(links)

    # run Project file
    def run(self):
        print("Running Program")
        os.system("python Exe_MLSecurity/Runner.py")
        
    # def readIt(): ## this is the variable the button changes
    #     global read

    #     read = 1
    #     Tk.after(0, readFile)

    # def readFile(self): ## this is the task you want the button to do
    #     global read
    #     if read == 1:
    #         print("Running Program")
    #         os.system("python Exe_MLSecurity/Runner.py")
    #         if "task is over":
    #             read = 0
    #     if read == 1:
    #         Tk.after(0, readFile)
        
    # Threading link function    
    def threadlink(self):
        t1 = Thread(target=self.link)
        t1.start()

    # def threadreq(self):
    #     t2 = Thread(target=self.requirements)
    #     t2.start()
    # def threadpress(self):
    #     t3 = Thread(traget=self.run())
    #     t3.start()

    # hide camera frame 
    def hide_me(self, x):
        x.pack_forget()

    # Retrieve camera frame  
    def retrieve(self, x,z,*y):
        z.place_forget()
        x.pack(side =LEFT, anchor = NE,padx=30, pady=30, expand = True)
        for i in y:
            i.grid_forget()
            
    # Press Function execute when clicked on camera show all camera Management 
    # which include (close , camera link, stop, test camera)  
    def press(self):
        global camera
        camera = tk.StringVar()
        global cam_on
        cam_on = False


        self.frame3 = tk.Frame(self.frame2, highlightbackground="#242C35", highlightthickness=3,bg='grey50')

        self.lab2 = tk.Label(self.frame3, bg="#242C35",text="CAMERA URL",height=3, width=15,font=("Helvetica",10,'bold'), fg='white')

        # self.cameraButton.configure(command=self.hide_me(self.cameraButton))
        # camera entry
        camera = tk.Entry(self.frame3, textvariable=camera, width=10,font=("Helvetica",34,'bold'))

        # Test Camera button
        self.TestButton = tk.Button(self.frame3, bg="#242C35",text="TEST CAMERA",font=("Helvetica",10,'bold'),
                                    height=3, fg='white', width=15, command = lambda : [self.start_vid()])
        
        # stop camera button
        self.stop = tk.Button(self.frame3, bg="#242C35",text="STOP", font=("Helvetica",10,'bold'),
                                        height=3, fg='white', width=15,command=self.stop_vid)

        # close camera button 
        self.close = tk.Button(self.frame3,bg="#242C35", text="CLOSE",font=("Helvetica",10,'bold'),height=3, width=15, fg='white',
                        command=lambda: [self.retrieve(self.cameraButton, self.frame3, self.lab2, camera, 
                                                    self.TestButton, self.stop,self.close),self.stop_vid()])

        # Child Frame alignment
        self.display1 = tk.Label(self.frame3, bg="#242C35")
        self.lab2.pack(side =LEFT, anchor = NW,padx=30, pady=10, expand = True)
        camera.pack(side =LEFT, anchor = NW,padx=5, pady=10, expand = True)
        self.TestButton.pack(side =LEFT, anchor = NW,padx=30, pady=10, expand = True)
        self.stop.pack(side =LEFT, anchor = NW,padx=30, pady=10, expand = True)
        self.close.pack(side =LEFT, anchor = NW,padx=30, pady=10, expand = True)

        self.display1.place(relx=.5, rely=.57, height = 500, width = 500, anchor="center")
        self.frame3.place(relx=.5, rely=.57, anchor="center", height = 600 , width = 1100)
       
    # Function to show camera frame while checking camera link is valid or not
    def show_frame(self):
        try:
            if validators.url(camera.get()):
                if cam_on:
                    ret, frame = cap.read()
                    if ret:
                        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        img = Image.fromarray(cv2image).resize((480, 480))
                        imgtk = ImageTk.PhotoImage(image=img)
                        self.display1.imgtk = imgtk
                        self.display1.configure(image=imgtk)
        except:
            print("wrong")
        try:
            ret, frame = cap.read()
            if ret:
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image).resize((480, 480))
                imgtk = ImageTk.PhotoImage(image=img)
                self.display1.imgtk = imgtk
                self.display1.configure(image=imgtk)
        except:
            print("wrong")
        self.display1.after(1, self.show_frame)

    # Start video frames
    def start_vid(self):
        global cap , cam_on
        cap = cv2.VideoCapture(0)
        cam_on = True
        self.show_frame()

    # stop video frames
    def stop_vid(self):
        global cam_on
        cam_on = False
        if cap:
            cap.release()
            self.display1.config(image="")

    # function to open User Management 
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = UserPage(self.newWindow, path=os.path.join(os.getcwd(), 'Face_Recog', 'images'))

    # destroy window 
    def close_windows(self):
        self.master.destroy()
#==================================================================End==================================================