from tkinter import * 
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, PhotoImage, Toplevel
from threading import Thread
import threading
import requests
import json 
import random
import time
import plyer
from plyer import notification 

def sendMessage(pn, em, title, body):
  api_key = "pk_prod_HF62V1AYE64SNFQTXTF3YE9MRD0F"
  url = "https://api.courier.com/send"

  payload = {
    "message": {
      "to": {
        "phone_number": pn,
        "email": em
      },
      "content": {
          "title": title,
          "body": body
      }
    }
  }
  headers = {
      "Accept": "application/json",
      "Content-Type": "application/json",
      "Authorization": "Bearer " + api_key 
  }

  response = requests.request("POST", url, headers = headers, json = payload)
  return response

window=Tk ()
window.withdraw()
window.title('Productify')
window.geometry('1430x750')
window.resizable(0,0)

email = StringVar()
phonenumber = StringVar()

# frame1=Frame(window, height = 250, width = 400, highlightbackground='black',highlightthickness = 5)
# # frame1.grid(row=0, column=0, padx=20, pady=20, ipadx=0, ipady=375)
# frame1.place(x = 20, y = 19)
class login():

    def __init__(self):
        self.top = tk.Toplevel()
        self.top.geometry("500x400")
        self.top.title("Pomodoro Timer")
  
        self.style = ttk.Style()
        self.style.configure("TNotebook.Tab", font = ("Ubuntu", 16))
        self.style.configure("TNotebook", tabposition = "n")
       # self.style.configure("TButton", font = ("Ubuntu", 16))

        self.tabs = ttk.Notebook(self.top)
        self.tabs.pack(fill = "both", pady = 10, expand = True)
        

        self.tab1 = ttk.Frame(self.tabs, width = 500, height = 400)
        self.tab2 = ttk.Frame(self.tabs, width = 300, height = 400)

        

        self.tabs.add(self.tab1, text = " Login ")
        self.tabs.add(self.tab2, text = "Register")

        #self.grid_layout = ttk.Frame(self.tab1)

        self.enterUserLabel = ttk.Label(self.tab1, text = "Enter Username:", font = ("Ubuntu", 16))
        self.enterUserLabel.pack(side = TOP, pady = 30)

        self.enterUserArea = Text(self.tab1, height = 2, width = 30)
        self.enterUserArea.pack(side = TOP)

        self.enterPassLabel = ttk.Label(self.tab1, text = "Enter Password:", font = ("Ubuntu", 16))
        self.enterPassLabel.pack(side = TOP, pady = 30)

        self.enterPassArea = Text(self.tab1, height = 2, width = 30)
        self.enterPassArea.pack(side = TOP)
        
        self.submitInfo = ttk.Button(self.tab1, text = "Submit Info", command = self.login)
        self.submitInfo.pack(side = TOP, pady = 20)

        self.createUserLabel = ttk.Label(self.tab2, text = "Create Username:", font = ("Ubuntu", 16))
        self.createUserLabel.pack(side = TOP, anchor = 'nw', pady = 10)

        self.createUserArea = Text(self.tab2, height = 1, width = 30)
        self.createUserArea.pack(side = TOP, anchor = 'nw')

        self.createPassLabel = ttk.Label(self.tab2, text = "Create Password:", font = ("Ubuntu", 16))
        self.createPassLabel.pack(side = TOP, anchor = 'nw', pady = 10)

        self.createPassArea = Text(self.tab2, height = 1, width = 30)
        self.createPassArea.pack(side = TOP, anchor = 'nw')

        self.createPassAgainLabel = ttk.Label(self.tab2, text = "Enter Password again:", font = ("Ubuntu", 16))
        self.createPassAgainLabel.pack(side = TOP, anchor = 'nw', pady = 10)

        self.createPassAgainArea= Text(self.tab2, height = 1, width = 30)
        self.createPassAgainArea.pack(side = TOP, anchor = 'nw')

        self.createEmailLabel = ttk.Label(self.tab2, text = "Create Email:", font = ("Ubuntu", 16))
        self.createEmailLabel.pack(side = TOP, anchor = 'nw', pady = 10)
        
        self.createEmailArea = Text(self.tab2, height = 1, width = 30)
        self.createEmailArea.pack(side = TOP, anchor = 'nw')

        self.createPhoneNLabel = ttk.Label(self.tab2, text = "Create Phone #:", font = ("Ubuntu", 16))
        self.createPhoneNLabel.pack(side = TOP, anchor = 'nw', pady = 10)

        self.createPhoneNArea = Text(self.tab2, height = 1, width = 30)
        self.createPhoneNArea.pack(side = TOP, anchor = 'nw')

        self.submitAccInfo = ttk.Button(self.tab2, text = "Submit Info",  command = self.registerUser)
        self.submitAccInfo.place(x = "350", y = "150")

        self.top.mainloop()

    def registerUser(self):
        
        if (len(self.createUserArea.get("1.0", END))==1 or len(self.createPassArea.get("1.0", END))==1 
        or len(self.createPassAgainArea.get("1.0", END))==1 or len(self.createEmailArea.get("1.0", END))==1 or len(self.createPhoneNArea.get("1.0", END))==1):
            messagebox.showwarning(title="Missing Information", message="Please enter all required fields")
            return
        if self.createPassAgainArea.get("1.0",END) == self.createPassArea.get("1.0",END):
            file=open(self.createUserArea.get("1.0", END).strip()+".txt", "w")
            file.write(self.createUserArea.get("1.0", END) + "" + self.createPassArea.get("1.0", END) + "" + self.createEmailArea.get("1.0", END) + "" +  self.createPhoneNArea.get("1.0", END))
            messagebox.showinfo(title="Done", message="Registration complete!")
            file.close()
    
    def login(self):
        if len(self.enterUserArea.get("1.0", END)) == 1 or len(self.enterPassArea.get("1.0", END)) == 1:
            messagebox.showwarning(title="Missing Information", message="Please enter all required fields")
        else:
            try:
                f = open(self.enterUserArea.get("1.0", END).strip() + ".txt")
            except:
                messagebox.showerror(title="User invalid", message="User is not registered")
                return
            password = self.enterPassArea.get("1.0", END).strip()
            self.userinfo = []
            lines = f.read().splitlines()
            for line in lines:
                self.userinfo.extend(line.split())
            if self.userinfo[1].strip() == password:
                #print("login destroyed, main window deiconified")
                window.deiconify()
                self.top.destroy()
            else:
                messagebox.showwarning(title="Login Denied", message="Password is incorrect")
                return
            #print(password)
            #print(self.userinfo[1])
            global email
            email = self.userinfo[2]
            global phonenumber
            phonenumber = self.userinfo[3]


# email = StringVar()
# phonenumber = StringVar()
# button1=Button(frame1,text='Submit',font=('Arial',14), command = collectEmail)
# button1.place(x = 10, y= 90)


# button2=Button(frame1,text='Submit',font=('Arial',14), command = collectNum)
# button2.place(x = 10, y= 190)

# frame1.grid_propagate(False)

# labelx = Label(frame1, text='Notifications: Phone & Email ', font=('Times 22 bold', 18))
# labelx.place(x = 25, y = 5)

# label1 = Label(frame1, text='Enter your email: ', font=('Arial',14))
# label1.place(x = 10, y = 70)


# data=StringVar() #IntVar()

# textbox1=Entry(frame1, width = 18,textvariable=email, font=('Arial',14))
# textbox1.place(x = 160, y = 70 )


# label2 = Label(frame1, text='Enter your phone #: ', font=('Arial',14))
# label2.place(x= 10, y = 160)


# textbox2=Entry(frame1, width = 16, textvariable=phonenumber, font=('Arial',14))
# textbox2.place(x = 190, y = 160)




frame5=Frame(window, height = 310, width = 350, highlightbackground='black',highlightthickness = 5)
frame5.place(x = 10, y = 20)


# frame6=Frame(window, height = 130, width = 350, highlightbackground ='black',highlightthickness= 5)
# frame6.place(x=10, y = 348)

# darkMode =Button(frame6, text="Light Mode ", width = 17, height = 1, font=("poppins bold", 18))
# darkMode.place(x= 50, y = 65)
# lightMode = Button(frame6, text="Dark Mode ", width = 17, height = 1, font=("poppins bold", 18))
# lightMode.place(x= 50, y = 5)






def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("Notifier Set", "set notification?") 

        time.sleep(min_to_sec)

        notification.notify(title=get_title, message=get_msg, app_name="Productify", timeout=10)




frame5.grid_propagate(False)

# notification.notify(title="Title", message="msg", timeout=18, app_icon=None)     


main_label = Label(frame5, text="Notifications: Desktop",  font=("poppins bold", 18))
main_label.place(x=70, y = 20)

t_label = Label(frame5, text="Title to notify", font=("poppins", 10))
t_label.place(x=12, y=70)


title  =Entry(frame5, width="20", font=("poppins", 13))
title.place(x= 123, y = 70)

m_label = Label(frame5, text="Display Message", font=("poppins", 10))
m_label.place(x=12, y=128)

msg = Entry(frame5, width ="20", font=("poppins", 13))
msg.place(x=123, y = 120, height=30)

time_label = Label(frame5, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y = 175)

time1 = Entry(frame5, width = "3", font=("poppins", 13))
time1.place(x = 123, y = 175)

time_min_label = Label(frame5, text="min", font=("poppins", 10))
time_min_label.place(x=175, y = 180)

but = Button(frame5, text="SET NOTIFICATION", font=("poppins", 10, 'bold'), fg="#ffffff", bg="#528DFF", width = 35, relief = "raised", command= get_details)
but.place(x= 30, y = 230)



frame2=Frame(window, height = 500 , width = 550, highlightbackground='black',highlightthickness = 5)
frame2.place(x = 370, y = 20)


def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END,task)
        my_entry.delete(0, "end")

    else:
        messagebox.showwarning("warning", "Please enter a task")


def deleteTask():
    lb.delete(ACTIVE)
    finishedTask()

def finishedTask():
    if lb.size() == 0:
        # messagebox.showinfo("Hooray! You finished your tasks!")
        messagebox.showinfo("Congratulations", "Good Job on Finishing your tasks!")
        sendMessage(str(phonenumber), str(email), "Productify ", "Congrats on Finishing all your tasks for the Day!")

lb = Listbox(frame2, width=25,height=16, font=('Times',18), bd=0,fg='#464646',highlightthickness=0,selectbackground='#a6a6a6',activestyle="none")

lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Eat apple',
    'Finish hw',
    'Stay hydrated',
    'Go to the gym',
    'Call parents',
    'Take a nap',
    'Work on side projects'
    
]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame2)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    frame2,
    font=('times', 24),
    width = 15
)

my_entry.pack(pady=20)

button_frame=Frame(frame2)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)

addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(button_frame,text='Delete Task',font=('times 14'), bg='#ff8b61',padx=20,pady=10,command=deleteTask)

delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

def createQuote():
    url = "https://type.fit/api/quotes"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    fullquote = data[random.randint(0, len(data)-1)]
    author = fullquote['author']
    quote = fullquote['text']
    while author == "none":
        response = requests.request("GET", url)
        data = json.loads(response.text)
        fullquote = data[random.randint(0, len(data)-1)]
        author = fullquote['author']
        quote = fullquote['text']
    return author, quote

author, quote = createQuote()

def regenquote():
    author, quote = createQuote()
    quoteLabel.config(text = str(quote) + "\n\n-    " + str(author))
    ##print(str(phonenumber))
    ##print(str(email))
    requestid = sendMessage(str(phonenumber), str(email), "Inspirational Quote", "As " + author + " once said: \n" + quote )
    ##print(requestid)

frame3=Frame(window,  height = 220, width = 950, highlightbackground='black',highlightthickness = 5 )
frame3.place(x= 10, y = 495)
frame3.pack_propagate(False)
quoteLabel = Label(frame3, wraplength = "900", text = str(quote) + "\n\n-    " + str(author), font = ("Ubuntu", 15))
quoteLabel.pack(side = TOP, ipadx = "0", ipady = "30")
regenerateQuote = Button(frame3, text = "Motivate me", fg = "black", command = regenquote)
regenerateQuote.pack(side = BOTTOM, ipadx = "10", ipady = "10", pady = "10")

frame4=Frame(window, height = 725, width = 450, highlightbackground='black',highlightthickness = 5)
frame4.place(x= 980, y = 20) 
#frame3.grid_propagate(false)
class PomodoroTimer:

    def __init__(self):
        #print("hi`")

        self.style = ttk.Style()
        self.style.configure("TNotebook.Tab", font = ("Ubuntu", 16))
        self.style.configure("TButton", font = ("Ubuntu", 16))

        self.tabs = ttk.Notebook(frame4)
        self.tabs.pack(fill = "both", pady = 10, expand = True)

        self.tab1 = ttk.Frame(self.tabs, width = 600, height = 100)
        self.tab2 = ttk.Frame(self.tabs, width = 600, height = 100)
        self.tab3 = ttk.Frame(self.tabs, width = 600, height = 100)

        self.grid_layout = ttk.Frame(frame4)
        
        self.pomodoroTimerLabel = ttk.Label(self.tab1, text = "25:00", font = ("Ubuntu", 100))
        self.pomodoroTimerLabel.pack(pady = 200)

        self.shortBreakTimerLabel = ttk.Label(self.tab2, text = "5:00", font = ("Ubuntu", 100))
        self.shortBreakTimerLabel.pack(pady = 200)

        self.longBreakTimerLabel = ttk.Label(self.tab3, text = "15:00", font = ("Ubuntu", 100))
        self.longBreakTimerLabel.pack(pady = 200)

        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text = "Pomodoros: 0")
        self.pomodoro_counter_label.grid(row = 1, column = 0, columnspan = 3, ipady = 10)

        self.tabs.add(self.tab1, text = "Pomodoro")
        self.tabs.add(self.tab2, text = "Short Break")
        self.tabs.add(self.tab3, text = "Long Break")

        self.grid_layout.pack(pady = 10)

        self.stopped = False
        self.skipped = False
        self.pomodoros = 0
        self.running = False
        
        self.start_button = ttk.Button(self.grid_layout, text = "Start", command = self.start_timer_thread)
        self.start_button.grid(row = 0, column = 0)

        self.skip_button = ttk.Button(self.grid_layout, text = "Skip", command = self.skip_clock)
        self.skip_button.grid(row = 0, column = 1)

        self.reset_button = ttk.Button(self.grid_layout, text = "Reset", command = self.reset_clock)
        self.reset_button.grid(row = 0, column = 2)


    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target = self.start_timer)
            t.start()
            #print("run!")
            self.running = True

    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1
        #print(timer_id)
        if timer_id == 1:
            ##print("main work started")
            timeLeft = 60*25
           
            while timeLeft > 0 and not self.stopped:
                min, sec = divmod(timeLeft, 60)
                self.pomodoroTimerLabel.config(text = f"{min:02d}:{sec:02d}")
                frame4.update()
                time.sleep(1)
                timeLeft-=1
            if not self.stopped or self.skipped:
                self.pomodoros+=1
                self.pomodoro_counter_label.config(text = f"Pomodoros: {self.pomodoros}")
                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)
                    rid = sendMessage(str(phonenumber), str(email), "Pause Work!", "Good Job! Take a Short Break!")
                    #print(rid)
                else:
                    self.tabs.select(1)
                    rid = sendMessage(str(phonenumber), str(email), "Pause Work!", "Good Job! Take a Short Break!")
                    #print(rid)
                self.start_timer()
        elif timer_id == 2:
            timeLeft = 60*5
            while timeLeft > 0 and not self.stopped:
                min, sec = divmod(timeLeft, 60)
                self.shortBreakTimerLabel.config(text = f"{min:02d}:{sec:02d}")
                frame4.update()
                time.sleep(1)
                timeLeft-=1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                rid = sendMessage(phonenumber, email, "Break End", "Your Break Is Over :( Please Get Back to Work!")
                #print(rid)
                self.start_timer()
        elif timer_id==3:
            timeLeft = 60*15
            while timeLeft > 0 and not self.stopped:
                min, sec = divmod(timeLeft, 60)
                self.longBreakTimerLabel.config(text = f"{min:02d}:{sec:02d}")
                frame4.update()
                time.sleep(1)
                timeLeft-=1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                rid = sendMessage(phonenumber, email, "Break End", "Your Break Is Over :( Please Get Back to Work!")
                #print(rid)
                self.start_timer()
                
    def reset_clock(self):
        self.stopped = True
        self.skipped = False
        self.pomodoros = 0
        self.pomodoroTimerLabel.config(text = "25:00")
        self.shortBreakTimerLabel.config(text = "5:00")
        self.longBreakTimerLabel.config(text = "15:00")
        self.pomodoro_counter_label.config(text = "Pomodoros: 0")
        self.running = False
                            

    def skip_clock(self):
    
        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.pomodoroTimerLabel.config(text = "25:00")
        
        elif current_tab == 1:
            self.shortBreakTimerLabel.config(text = "5:00")
            
        elif current_tab == 2:
            self.longBreakTimerLabel.config(text = "15:00")
    
        self.stopped = True
        self.skipped = True
        self.running = False
PomodoroTimer() 
login()  
      


window.mainloop()
