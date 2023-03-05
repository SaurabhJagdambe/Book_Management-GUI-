from tkinter import *
from datetime import datetime


def not_return():
    def close():
        base7.destroy()

    base7 = Tk()
    base7.geometry("450x350")
    base7.title("Not Returned Books")
    frame = Frame(base7, bg="skyblue", height=350, width=450)
    frame.place(x=0, y=0)
    framex = Frame(base7, bg="white", height=50, width=50)
    framex.place(x=2, y=50)

    f1 = ("Times new roman", 16)
    f2 = ("Times new roman", 14)

    lb2 = Label(base7, text="Sr.No.   Book number   Enrollment number  Issue date", font=f2, bg="skyblue")
    lb2.place(x=2, y=10)

    yscroll = Scrollbar(framex)
    yscroll.pack(side=RIGHT, fill=Y)

    txt = Text(framex, yscrollcommand=yscroll.set, height=10, width=47, font=f2)
    txt.pack()

    yscroll.config(command=txt.yview)

    b3 = Button(base7, text="Close", font=f1, command=close)
    b3.place(x=370, y=300)

    lb5 = Label(base7, text="", font=f1, bg="skyblue", fg="red")
    lb5.place(x=150, y=264)

    obj = open("issue_book.txt", "r")
    ls = obj.readlines()
    obj.close()
    cnt = ls.count("NA\n")
    if cnt > 0:
        msg = ""
        i = 0
        c = 1
        while i < cnt:
            ind = ls.index("NA\n")
            msg = msg + "   " + str(c) + ")" + " " * (7) + \
                  ls[ind - 3][0:-1] + " " * (19) + \
                  ls[ind - 2][0:-1] + " " * (6) + ls[ind - 1]
            ls.pop(ind)
            ls.pop(ind - 1)
            ls.pop(ind - 2)
            ls.pop(ind - 3)
            c = c + 1
            i = i + 1
        txt.insert(INSERT, msg)
    else:
        lb5.config(text="All books are returned")

    base7.mainloop()

def book_hist():
    def close():
        base7.destroy()

    def reset():
        en1.delete(0, "end")
        txt.delete(1.0, "end")
        lb5.config(text="")

    def submit():
        obj = open("issue_book.txt", "r")
        ls = obj.readlines()
        obj.close()
        er = en1.get()
        cnt = ls.count(er + "\n")
        if cnt > 0:
            msg = ""
            i = 0
            c = 1
            while i < cnt:
                ind = ls.index(er + "\n")
                msg = msg + "   " + str(c) + ")" + " " * (7) + \
                      ls[ind + 1][0:-1] + " " * (11) + \
                      ls[ind + 2][0:-1] + " " * (7) + ls[ind + 3]
                ls.pop(ind + 3)
                ls.pop(ind + 2)
                ls.pop(ind + 1)
                ls.pop(ind)
                c = c + 1
                i = i + 1

            txt.insert(INSERT, msg)
        else:
            lb5.config(text="This book does not issued by any student")

    base7 = Tk()
    base7.geometry("450x400")
    base7.title("Book History")
    frame = Frame(base7, bg="skyblue", height=400, width=450)
    frame.place(x=0, y=0)
    framex = Frame(base7, bg="white", height=50, width=50)
    framex.place(x=2, y=90)

    f1 = ("Times new roman", 16)
    f2 = ("Times new roman", 14)

    lb1 = Label(base7, text="Enter book number", font=f1, bg="skyblue")
    lb1.place(x=2, y=5)

    lb2 = Label(base7, text="Sr.No.   Enrollment Number     Issue date    Return date", font=f2, bg="skyblue")
    lb2.place(x=2, y=60)

    en1 = Entry(base7, font=f1)
    en1.place(x=220, y=5)
    en1.focus()

    yscroll = Scrollbar(framex)
    yscroll.pack(side=RIGHT, fill=Y)

    txt = Text(framex, yscrollcommand=yscroll.set, height=10, width=47, font=f2)
    txt.pack()

    yscroll.config(command=txt.yview)

    b1 = Button(base7, text="Submit", font=f1, command=submit)
    b1.place(x=90, y=350)

    b2 = Button(base7, text="Reset", font=f1, command=reset)
    b2.place(x=200, y=350)

    b3 = Button(base7, text="Close", font=f1, command=close)
    b3.place(x=300, y=350)

    lb5 = Label(base7, text="", font=f1, bg="skyblue", fg="red")
    lb5.place(x=70, y=310)

    base7.mainloop()

def stu_hist():
    def close():
        base6.destroy()

    def reset():
        en1.delete(0, "end")
        txt.delete(1.0, "end")
        lb5.config(text="")

    def submit():
        obj = open("issue_book.txt", "r")
        ls = obj.readlines()
        obj.close()
        er = en1.get()
        cnt = ls.count(er + "\n")
        if cnt > 0:
            msg = ""
            i = 0
            c = 1
            while i < len(ls):
                ind = ls.index(er + "\n")
                msg = msg + "   " + str(c) + ")" + " " * (7) + \
                      ls[ind - 1][0:-1] + " " * (24) + \
                      ls[ind + 1][0:-1] + " " * (10) + ls[ind + 2]
                ls.pop(ind)
                c = c + 1
                i = i + 4
            txt.insert(INSERT, msg)
        else:
            lb5.config(text="This Student does not issue any book")

    base6 = Tk()
    base6.geometry("450x400")
    base6.title("Student History")
    frame = Frame(base6, bg="skyblue", height=400, width=450)
    frame.place(x=0, y=0)
    framex = Frame(base6, bg="white", height=50, width=50)
    framex.place(x=2, y=90)

    f1 = ("Times new roman", 16)
    f2 = ("Times new roman", 14)

    lb1 = Label(base6, text="Enter Enrollment number", font=f1, bg="skyblue")
    lb1.place(x=2, y=5)

    lb2 = Label(base6, text="Sr.No.   Book Number        Issue date        Return date", font=f2, bg="skyblue")
    lb2.place(x=2, y=60)

    en1 = Entry(base6, font=f1)
    en1.place(x=220, y=5)
    en1.focus()

    yscroll = Scrollbar(framex)
    yscroll.pack(side=RIGHT, fill=Y)

    txt = Text(framex, yscrollcommand=yscroll.set, height=10, width=47, font=f2)
    txt.pack()

    yscroll.config(command=txt.yview)

    b1 = Button(base6, text="Submit", font=f1, command=submit)
    b1.place(x=90, y=350)

    b2 = Button(base6, text="Reset", font=f1, command=reset)
    b2.place(x=200, y=350)

    b3 = Button(base6, text="Close", font=f1, command=close)
    b3.place(x=300, y=350)

    lb5 = Label(base6, text="", font=f1, bg="skyblue", fg="red")
    lb5.place(x=70, y=310)

    base6.mainloop()

def issue():
    def close():
        base5.destroy()

    def reset():
        en1.delete(0, "end")
        en2.delete(0, "end")
        lb5.config(text="")

    def submit():
        obj = open("all_books.txt", "r")
        obj1 = open("all_students.txt", "r")
        ls = obj.readlines()
        ls1 = obj1.readlines()
        obj.close()
        obj1.close()
        er = en1.get()
        bk = en2.get()
        cnt = ls1.count(er + "\n")
        if cnt > 0:
            cnt1 = ls.count(bk + "\n")
            if cnt1 > 0:
                time = datetime.now()
                date = time.strftime("%d/%m/%y")
                obj2 = open("issue_book.txt", "a")
                obj2.write(bk + "\n" + er + "\n" + date + "\n" + "NA\n")
                obj2.close()
                lb5.config(text="Book issued successfully", fg="green")
            else:
                lb5.config(text="Book number is incorrect")
        else:
            lb5.config(text="Enrollment number is incorrect")

    base5 = Tk()
    base5.geometry("450x250")
    base5.title("Issue Book")
    frame = Frame(base5, bg="skyblue", height=350, width=450)
    frame.place(x=0, y=0)
    f1 = ("Times new roman", 16)

    lb1 = Label(base5, text="Enter enrollment number", font=f1, bg="skyblue")
    lb1.place(x=2, y=5)

    lb2 = Label(base5, text="Enter book number", font=f1, bg="skyblue")
    lb2.place(x=2, y=50)

    en1 = Entry(base5, font=f1)
    en1.place(x=220, y=5)

    en2 = Entry(base5, font=f1)
    en2.place(x=220, y=50)

    b1 = Button(base5, text="Submit", font=f1, command=submit)
    b1.place(x=90, y=150)

    b2 = Button(base5, text="Reset", font=f1, command=reset)
    b2.place(x=200, y=150)

    b3 = Button(base5, text="Close", font=f1, command=close)
    b3.place(x=300, y=150)

    lb5 = Label(base5, text="", font=f1, bg="skyblue", fg="red")
    lb5.place(x=100, y=100)

    base5.mainloop()

def return_b():
    def close():
        base5.destroy()

    def reset():
        en1.delete(0, "end")
        en2.delete(0, "end")
        lb5.config(text="")

    def submit():
        obj = open("all_books.txt", "r")
        obj1 = open("all_students.txt", "r")
        obj3 = open("issue_book.txt", "r")
        ls = obj.readlines()
        ls1 = obj1.readlines()
        ls2 = obj3.readlines()
        obj.close()
        obj1.close()
        obj3.close()
        er = en1.get()
        bk = en2.get()
        cnt = ls1.count(er + "\n")
        if cnt > 0:
            cnt1 = ls.count(bk + "\n")
            if cnt1 > 0:
                i = 0
                while i < len(ls2):
                    if ls2[i] == bk + "\n" and ls2[i + 1] == er + "\n" and ls2[i + 3] == "NA\n":
                        time = datetime.now()
                        date = time.strftime("%d/%m/%y")
                        ls2[i + 3] = date + "\n"
                        obj2 = open("issue_book.txt", "w")
                        obj2.writelines(ls2)
                        obj2.close()
                        lb5.config(text="Book returned successfully", fg="green")
                    i = i + 1
            else:
                lb5.config(text="Book number is incorrect")
        else:
            lb5.config(text="Enrollment number is incorrect")

    base5 = Tk()
    base5.geometry("450x250")
    base5.title("Return Book")
    frame = Frame(base5, bg="skyblue", height=350, width=450)
    frame.place(x=0, y=0)
    f1 = ("Times new roman", 16)

    lb1 = Label(base5, text="Enter enrollment number", font=f1, bg="skyblue")
    lb1.place(x=2, y=5)

    lb2 = Label(base5, text="Enter book number", font=f1, bg="skyblue")
    lb2.place(x=2, y=50)

    en1 = Entry(base5, font=f1)
    en1.place(x=220, y=5)

    en2 = Entry(base5, font=f1)
    en2.place(x=220, y=50)

    b1 = Button(base5, text="Submit", font=f1, command=submit)
    b1.place(x=90, y=150)

    b2 = Button(base5, text="Reset", font=f1, command=reset)
    b2.place(x=200, y=150)

    b3 = Button(base5, text="Close", font=f1, command=close)
    b3.place(x=300, y=150)

    lb5 = Label(base5, text="", font=f1, bg="skyblue", fg="red")
    lb5.place(x=100, y=100)

    base5.mainloop()

def add_book():
    def close():
        base1.destroy()

    def reset():
        en1.delete(0, "end")
        en2.delete(0, "end")
        en3.delete(0, "end")
        en4.delete(0, "end")
        lb5.config(text="")

    def save():
        a = en1.get()
        b = en2.get()
        c = en3.get()
        d = en4.get()
        if len(a) > 0 and len(b) > 0 and len(c) > 0 and len(d) > 0:
            bk = open("all_books.txt", "a")
            bk.write(a.lower() + "\n")
            bk.write(b.lower() + "\n")
            bk.write(c.lower() + "\n")
            bk.write(d.lower() + "\n")
            bk.close()
            reset()
            lb5.config(text="Book added successfully",fg="green")
        else:
            lb5.config(text="Enter complete information")

    base1 = Tk()
    base1.geometry("450x350")
    base1.title("Add new Book")
    frame = Frame(base1, bg="skyblue", height=350, width=450)
    frame.place(x=0, y=0)
    f1 = ("Times new roman", 16)

    lb1 = Label(base1, text="Enter book title", font=f1, bg="skyblue")
    lb1.place(x=2, y=5)
    lb2 = Label(base1, text="Enter book author", font=f1, bg="skyblue")
    lb2.place(x=2, y=50)
    lb3 = Label(base1, text="Enter book publication", font=f1, bg="skyblue")
    lb3.place(x=2, y=100)
    lb4 = Label(base1, text="Enter book number", font=f1, bg="skyblue")
    lb4.place(x=2, y=150)
    lb5 = Label(base1, text="", font=f1, bg="skyblue",fg="red")
    lb5.place(x=100, y=200)

    en1 = Entry(base1, font=f1)
    en1.place(x=220, y=5)
    en2 = Entry(base1, font=f1)
    en2.place(x=220, y=50)
    en3 = Entry(base1, font=f1)
    en3.place(x=220, y=100)
    en4 = Entry(base1, font=f1)
    en4.place(x=220, y=150)

    b1 = Button(base1, text="Save", font=f1, command=save)
    b1.place(x=90, y=250)
    b2 = Button(base1, text="Reset", font=f1, command=reset)
    b2.place(x=190, y=250)
    b3 = Button(base1, text="Close", font=f1, command=close)
    b3.place(x=300, y=250)

    base1.mainloop()

def add_stu():
    def close():
        base2.destroy()

    def reset():
        en1.delete(0, "end")
        en2.delete(0, "end")
        en3.delete(0, "end")
        en4.delete(0, "end")
        lb5.config(text="")

    def save():
        obj = open("all_students.txt", "r")
        ls = obj.readlines()
        obj.close()
        a = en1.get()
        b = en2.get()
        c = en3.get()
        d = en4.get()
        cnt = ls.count(a + "\n")
        if cnt == 0:
            if len(a) > 0 and len(b) > 0 and len(c) > 0 and len(d) > 0:
                bk = open("all_students.txt", "a")
                bk.write(a.lower() + "\n")
                bk.write(b.lower() + "\n")
                bk.write(c.lower() + "\n")
                bk.write(d.lower() + "\n")
                bk.close()
                reset()
                lb5.config(text="Student added successfully",fg="green")
            else:
                lb5.config(text="Enter complete information")
        else:
            lb5.config(text="Enrollment number is already used")

    base2 = Tk()
    base2.geometry("450x350")
    base2.title("Add new student")
    frame = Frame(base2, bg="skyblue", height=350, width=450)
    frame.place(x=0, y=0)
    f1 = ("Times new roman", 16)

    lb1 = Label(base2, text="Enter enrollment number", font=f1, bg="skyblue")
    lb1.place(x=2, y=5)

    lb2 = Label(base2, text="Enter name", font=f1, bg="skyblue")
    lb2.place(x=2, y=50)

    lb3 = Label(base2, text="Enter mobile number", font=f1, bg="skyblue")
    lb3.place(x=2, y=100)

    lb4 = Label(base2, text="Enter E-mail ID", font=f1, bg="skyblue")
    lb4.place(x=2, y=150)

    en1 = Entry(base2, font=f1)

    en1.place(x=220, y=5)

    en2 = Entry(base2, font=f1)
    en2.place(x=220, y=50)

    en3 = Entry(base2, font=f1)
    en3.place(x=220, y=100)

    en4 = Entry(base2, font=f1)
    en4.place(x=220, y=150)

    b1 = Button(base2, text="Save", font=f1, command=save)
    b1.place(x=90, y=250)

    b2 = Button(base2, text="Reset", font=f1, command=reset)
    b2.place(x=190, y=250)

    b3 = Button(base2, text="Close", font=f1, command=close)
    b3.place(x=300, y=250)

    lb5 = Label(base2, text="", font=f1, bg="skyblue", fg="red")
    lb5.place(x=100, y=200)

    base2.mainloop()

def search_stu():
    def close():
        base3.destroy()

    def reset():
        en1.delete(0, "end")
        lb2.config(text="Name                 = ")
        lb3.config(text="Mobile number = ")
        lb4.config(text="E-mail ID          = ")
        lb5.config(text="")

    def search():
        obj = open("all_students.txt", "r")
        ls = obj.readlines()
        obj.close()
        a = en1.get()
        cnt = ls.count(a + "\n")
        if cnt > 0:
            reset()
            ind = ls.index(a + "\n")
            lb2.config(text="Name                 = " + ls[ind + 1][0:-1].title())
            lb3.config(text="Mobile number = " + ls[ind + 2][0:-1])
            lb4.config(text="E-mail ID          = " + ls[ind + 3][0:-1])
        else:
            lb5.config(text="Enrollment number is incorrect")

    base3 = Tk()
    base3.geometry("450x350")
    base3.title("Search Student")
    frame = Frame(base3, bg="skyblue", height=350, width=450)
    frame.place(x=0, y=0)
    frame2 = Frame(base3, bg="white", height=150, width=430)
    frame2.place(x=10, y=40)
    f1 = ("Times new roman", 16)

    lb1 = Label(base3, text="Enter enrollment number", font=f1, bg="skyblue")
    lb1.place(x=2, y=5)

    lb2 = Label(base3, text="Name                 =", font=f1, bg="white")
    lb2.place(x=25, y=50)

    lb3 = Label(base3, text="Mobile number = ", font=f1, bg="white")
    lb3.place(x=25, y=100)

    lb4 = Label(base3, text="E-mail ID          =", font=f1, bg="white")
    lb4.place(x=25, y=150)

    en1 = Entry(base3, font=f1)
    en1.place(x=220, y=5)

    b1 = Button(base3, text="Search", font=f1, command=search)
    b1.place(x=90, y=250)

    b2 = Button(base3, text="Reset", font=f1, command=reset)
    b2.place(x=190, y=250)

    b3 = Button(base3, text="Close", font=f1, command=close)
    b3.place(x=300, y=250)

    lb5 = Label(base3, text="", font=f1, bg="skyblue", fg="red")
    lb5.place(x=80, y=200)

    base3.mainloop()

def search_book():
    def close():
        base4.destroy()

    def reset():
        en1.delete(0, "end")
        lb2.config(text="Book  Title           = ")
        lb3.config(text="Book Author        = ")
        lb4.config(text="Book Publication = ")
        lb5.config(text="")

    def search():
        obj = open("all_books.txt", "r")
        ls = obj.readlines()
        obj.close()
        a = en1.get()
        cnt = ls.count(a + "\n")
        if cnt > 0:
            reset()
            ind = ls.index(a + "\n")
            lb2.config(text="Book  Title           = " + ls[ind - 3][0:-1].title())
            lb3.config(text="Book Author        = " + ls[ind - 2][0:-1])
            lb4.config(text="Book Publication = " + ls[ind - 1][0:-1])
        else:
            lb5.config(text="Book number is incorrect")

    base4 = Tk()
    base4.geometry("450x350")
    base4.title("Search Book")
    frame = Frame(base4, bg="skyblue", height=350, width=450)
    frame.place(x=0, y=0)
    frame2 = Frame(base4, bg="white", height=150, width=430)
    frame2.place(x=10, y=40)
    f1 = ("Times new roman", 16)

    lb1 = Label(base4, text="Enter book number", font=f1, bg="skyblue")
    lb1.place(x=2, y=5)

    lb2 = Label(base4, text="Book  Title           = ", font=f1, bg="white")
    lb2.place(x=25, y=50)

    lb3 = Label(base4, text="Book Author        = ", font=f1, bg="white")
    lb3.place(x=25, y=100)

    lb4 = Label(base4, text="Book Publication = ", font=f1, bg="white")
    lb4.place(x=25, y=150)

    en1 = Entry(base4, font=f1)
    en1.place(x=220, y=5)

    b1 = Button(base4, text="Search", font=f1, command=search)
    b1.place(x=90, y=250)

    b2 = Button(base4, text="Reset", font=f1, command=reset)
    b2.place(x=200, y=250)

    b3 = Button(base4, text="Close", font=f1, command=close)
    b3.place(x=300, y=250)

    lb5 = Label(base4, text="", font=f1, bg="skyblue", fg="red")
    lb5.place(x=100, y=200)

    base4.mainloop()

def exite():
    base.destroy()

base=Tk()
base.geometry("420x400")
base.title("Central Library")
frame=Frame(base,bg="#3A3B3C",height=600,width=1000)
frame.place(x=0,y=0)
f=("Times new roman",14)

l1=Label(base,text="Central Library",font=("Times new roman",34),bg="#3A3B3C",fg="white")
l1.place(x=80,y=0)

b1=Button(base,text="Issue Book",font=f,bg="gray",fg="white",width=18,command=issue)
b1.place(x=10,y=100)

b2=Button(base,text="Return Book",font=f,bg="gray",fg="white",width=18,command=return_b)
b2.place(x=10,y=150)

b3=Button(base,text="Add new book",font=f,bg="gray",fg="white",command=add_book,width=18)
b3.place(x=10,y=200)

b4=Button(base,text="Add new student",font=f,bg="gray",fg="white",width=18,command=add_stu)
b4.place(x=10,y=250)

b5=Button(base,text="Book history",font=f,bg="gray",fg="white",width=18,command=book_hist)
b5.place(x=10,y=300)

b6=Button(base,text="Student history",font=f,bg="gray",fg="white",width=18,command=stu_hist)
b6.place(x=220,y=100)

b7=Button(base,text="Search Book",font=f,bg="gray",fg="white",width=18,command=search_book)
b7.place(x=220,y=150)

b8=Button(base,text="Search student",font=f,bg="gray",fg="white",width=18,command=search_stu)
b8.place(x=220,y=200)

b9=Button(base,text="Not returned Books",font=f,bg="gray",fg="white",width=18,command=not_return)
b9.place(x=220,y=250)

b10=Button(base,text="Exit",font=f,bg="gray",fg="white",width=18,command=exite)
b10.place(x=220,y=300)

base.mainloop()