
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql


# --------------------------------------------- Login Function ------------------------------------------------------
def clear():
    userentry.delete(0, END)
    passentry.delete(0, END)


def close():
    win.destroy()


def login():
    if user_name.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=win)
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="doctorapp")
            cur = con.cursor()

            cur.execute("select * from user_information where username=%s and password = %s",
                        (user_name.get(), password.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid User Name And Password", parent=win)

            else:
                messagebox.showinfo("Success", "Successfully Login", parent=win)
                close()
                dashboard()
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=win)


# ---------------------------------------------------------End Login Function ---------------------------------------

# --------------------------------------DashBoard Panel -------------------------------------------------------------


def dashboard():
    def book():
        if doctor_var.get() == "" or day.get() == "" or month.get() == "" or year.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=des)

        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="doctorapp")
            cur = con.cursor()

            cur.execute(
                "update user_information set doctor ='" + doctor_var.get() + "', day ='" + day.get() + "', month = '" + month.get() + "', year = '" + year.get() + "' where username ='" + user_name.get() + "'")
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Booked Appointment ", parent=des)

    des = Tk()
    des.title("Admin Panel Doctor App")
    des.maxsize(width=800, height=500)
    des.minsize(width=800, height=500)

    # set window color
    des.configure(bg='slategray2')

    # heading label
    heading = Label(des, text=f"User Name : {user_name.get()}", font='Verdana 20 bold', bg='slategray2')
    heading.place(x=220, y=50)

    f = Frame(des, height=1, width=800, bg="green")
    f.place(x=0, y=95)

    con = pymysql.connect(host="localhost", user="root", password="", database="doctorapp")
    cur = con.cursor()

    cur.execute("select * from user_information where username ='" + user_name.get() + "'")
    row = cur.fetchall()

    a = Frame(des, height=1, width=400, bg="green")
    a.place(x=0, y=195)

    b = Frame(des, height=100, width=1, bg="green")
    b.place(x=400, y=97)

    for data in row:
        first_name = Label(des, text=f"First Name : {data[1]}", font='Verdana 10 bold', bg='slategray2')
        first_name.place(x=20, y=100)

        last_name = Label(des, text=f"Last Name : {data[2]}", font='Verdana 10 bold', bg='slategray2')
        last_name.place(x=20, y=130)

        age = Label(des, text=f"Age : {data[3]}", font='Verdana 10 bold', bg='slategray2')
        age.place(x=20, y=160)

        gender = Label(des, text=f"ID : {data[0]}", font='Verdana 10 bold', bg='slategray2')
        gender.place(x=250, y=100)

        city = Label(des, text=f"City : {data[5]}", font='Verdana 10 bold', bg='slategray2')
        city.place(x=250, y=130)

        add = Label(des, text=f"Address : {data[6]}", font='Verdana 10 bold', bg='slategray2')
        add.place(x=250, y=160)

    # Book Doctor Appointment App
    heading = Label(des, text="Book Appointment", font='Verdana 20 bold', bg='slategray2')
    heading.place(x=470, y=100)

    # Book DoctorLabel
    Doctor = Label(des, text="Doctor:", font='Verdana 10 bold', bg='slategray2')
    Doctor.place(x=480, y=145)

    Day = Label(des, text="Day:", font='Verdana 10 bold', bg='slategray2')
    Day.place(x=480, y=165)

    Month = Label(des, text="Month:", font='Verdana 10 bold', bg='slategray2')
    Month.place(x=480, y=185)

    Year = Label(des, text="Year:", font='Verdana 10 bold', bg='slategray2')
    Year.place(x=480, y=205)

    # Book Doctor Entry Box

    doctor_var = tk.StringVar()
    day = StringVar()
    month = tk.StringVar()
    year = StringVar()

    Doctor_box = ttk.Combobox(des, width=30, textvariable=doctor_var, state='readonly')
    Doctor_box['values'] = ('Andy', 'Charlie', 'Shetal', 'Danish', 'Sunil')
    Doctor_box.current(0)
    Doctor_box.place(x=550, y=145)

    Day = Entry(des, width=33, textvariable=day,)
    Day.place(x=550, y=168)

    Month_Box = ttk.Combobox(des, width=30, textvariable=month, state='readonly')
    Month_Box['values'] = (
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
    'December')
    Month_Box.current(0)
    Month_Box.place(x=550, y=188)

    Year = Entry(des, width=33, textvariable=year)
    Year.place(x=550, y=208)

    # button

    btn = Button(des, text="Search", font='Verdana 10 bold', width=20, command=book, bg='steelblue3', bd=3)
    btn.place(x=553, y=250)

    con = pymysql.connect(host="localhost", user="root", password="", database="doctorapp")
    cur = con.cursor()

    cur.execute("select * from user_information where username ='" + user_name.get() + "'")
    rows = cur.fetchall()

    # book Appointment Details
    heading = Label(des, text=f"{user_name.get()} Appointments", font='Verdana 15 bold',bg='slategray2')
    heading.place(x=20, y=250)

    for book in rows:
        d1 = Label(des, text=f"Doctor: {book[9]}", font='Verdana 10 bold', bg='slategray2')
        d1.place(x=20, y=300)

        d2 = Label(des, text=f"Day: {book[10]}", font='Verdana 10 bold', bg='slategray2')
        d2.place(x=20, y=320)

        d3 = Label(des, text=f"Month: {book[11]}", font='Verdana 10 bold', bg='slategray2')
        d3.place(x=20, y=340)

        d4 = Label(des, text=f"Year: {book[12]}", font='Verdana 10 bold',bg='slategray2')
        d4.place(x=20, y=360)


# ------------------------------------------End Dashboard Panel -----------------------------------------------------

# ----------------------------------------------------------- Signup Window -----------------------------------------


def signup():
    # signup database connect
    def action():
        if first_name.get() == "" or last_name.get() == "" or age.get() == "" or city.get() == "" or add.get() == "" or user_name.get() == "" or password.get() == "" or very_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=winsignup)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=winsignup)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="doctorapp")
                cur = con.cursor()
                cur.execute("select * from user_information where username=%s", user_name.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User Name Already Exits", parent=winsignup)
                else:
                    cur.execute(
                        "insert into user_information(first_name,last_name,age,gender,city,address,username,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            first_name.get(),
                            last_name.get(),
                            age.get(),
                            var.get(),
                            city.get(),
                            add.get(),
                            user_name.get(),
                            password.get()
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Ragistration Successfull", parent=winsignup)
                    clear()
                    switch()

            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=winsignup)

    # close signup function
    def switch():
        winsignup.destroy()

    # clear data function
    def clear():
        first_name.delete(0, END)
        last_name.delete(0, END)
        age.delete(0, END)
        var.set("Male")
        city.delete(0, END)
        add.delete(0, END)
        user_name.delete(0, END)
        password.delete(0, END)
        very_pass.delete(0, END)

    # start Signup Window

    winsignup = Tk()
    winsignup.title("Doctor Appointment App")
    winsignup.maxsize(width=500, height=600)
    winsignup.minsize(width=500, height=600)

    # set window color
    winsignup.configure(bg='slategray2')

    # heading label
    heading = Label(winsignup, text="Signup", font='Verdana 24 bold', bg='slategray2')
    heading.place(x=30, y=60)

    # form data label
    first_name = Label(winsignup, text="First Name :", font='Verdana 12 bold', bg='slategray2')
    first_name.place(x=30, y=140)

    last_name = Label(winsignup, text="Last Name :", font='Verdana 12 bold', bg='slategray2')
    last_name.place(x=30, y=170)

    age = Label(winsignup, text="Age :", font='Verdana 12 bold', bg='slategray2')
    age.place(x=30, y=200)

    Gender = Label(winsignup, text="Gender :", font='Verdana 12 bold', bg='slategray2')
    Gender.place(x=30, y=250)

    city = Label(winsignup, text="City :", font='Verdana 12 bold', bg='slategray2')
    city.place(x=30, y=300)

    add = Label(winsignup, text="Address :", font='Verdana 12 bold', bg='slategray2')
    add.place(x=30, y=330)

    user_name = Label(winsignup, text="User Name :", font='Verdana 12 bold', bg='slategray2')
    user_name.place(x=30, y=360)

    password = Label(winsignup, text="Password :", font='Verdana 12 bold', bg='slategray2')
    password.place(x=30, y=390)

    very_pass = Label(winsignup, text="Verify Password:", font='Verdana 12 bold', bg='slategray2')
    very_pass.place(x=30, y=420)

    # Entry Box -----------------------------------------------------------------------------------------------------

    first_name = StringVar()
    last_name = StringVar()
    age = IntVar(winsignup, value='0')
    var = StringVar()
    city = StringVar()
    add = StringVar()
    user_name = StringVar()
    password = StringVar()
    very_pass = StringVar()

    first_name = Entry(winsignup, width=25, textvariable=first_name, bg='gainsboro', font='Verdana 12 bold')
    first_name.place(x=190, y=140)

    last_name = Entry(winsignup, width=25, textvariable=last_name, bg='gainsboro', font='Verdana 12 bold')
    last_name.place(x=190, y=170)

    age = Entry(winsignup, width=25, textvariable=age, bg='gainsboro', font='Verdana 12 bold')
    age.place(x=190, y=200)

    Radio_button_male = ttk.Radiobutton(winsignup, text='MALE', value="Male", variable=var).place(x=190, y=240)
    Radio_button_female = ttk.Radiobutton(winsignup, text='FEMALE', value="Female", variable=var).place(x=190, y=270)

    city = Entry(winsignup, width=25, textvariable=city, bg='gainsboro', font='Verdana 12 bold')
    city.place(x=190, y=300)

    add = Entry(winsignup, width=25, textvariable=add, bg='gainsboro', font='Verdana 12 bold')
    add.place(x=190, y=330)

    user_name = Entry(winsignup, width=25, textvariable=user_name, bg='gainsboro', font='Verdana 12 bold')
    user_name.place(x=190, y=360)

    password = Entry(winsignup, width=25, textvariable=password, bg='gainsboro', font='Verdana 12 bold')
    password.place(x=190, y=390)

    very_pass = Entry(winsignup, width=25, show="*", textvariable=very_pass, bg='gainsboro', font='Verdana 12 bold')
    very_pass.place(x=190, y=420)

    # button login and clear

    btn_signup = Button(winsignup, text="Signup", font='Verdana 10 bold', command=action, bg='steelblue3', bd=3)
    btn_signup.place(x=200, y=460)

    btn_login = Button(winsignup, text="Clear", font='Verdana 10 bold', command=clear, bg='steelblue3', bd=3)
    btn_login.place(x=280, y=460)

    sign_up_btn = Button(winsignup, text="Switch To Login", command=switch, bg='steelblue3', bd=3)
    sign_up_btn.place(x=350, y=20)

    winsignup.mainloop()


# ----------------------------------------------------------------End Singup Window-----------------------------------


# ------------------------------------------------------------ Login Window -----------------------------------------

win = Tk()

# app title
win.title("Doctor Appointment App")

# window size
win.maxsize(width=500, height=500)
win.minsize(width=500, height=500)


#set window color
win.configure(bg='slategray2')


# heading label
heading = Label(win, text="Login", font='Verdana 27 bold', bg='slategray2')
heading.place(x=50, y=150)

username = Label(win, text="User Name :", font='Verdana 14 bold', bg='slategray2')
username.place(x=50, y=220)

userpass = Label(win, text="Password :", font='Verdana 14 bold', bg='slategray2')
userpass.place(x=50, y=280)

# Entry Box
user_name = StringVar()
password = StringVar()

userentry = Entry(win, width=25, textvariable=user_name, bg='gainsboro', font='Verdana 12 bold')
userentry.focus()
userentry.place(x=190, y=220)

passentry = Entry(win, width=25, show="*", textvariable=password, bg='gainsboro', font='Verdana 12 bold')
passentry.place(x=190, y=280)

# button login and clear

btn_login = Button(win, text="Login", font='Verdana 10 bold', command=login, bg='steelblue3', bd=3)
btn_login.place(x=200, y=350)

btn_login = Button(win, text="Clear", font='Verdana 10 bold', command=clear, bg='steelblue3', bd=3)
btn_login.place(x=260, y=350)

# signup button

sign_up_btn = Button(win, text="Switch To Sign up", command=signup, bg='steelblue3', bd=3)
sign_up_btn.place(x=350, y=20)

win.mainloop()

# ------------------------------------------------ End Login Window ---------------------------------------------------



