#Importing
from tkinter import *
root=Tk()
def send():
    send="You=>"+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"Bot=>Hi there!May I know your name?")
    elif(e.get()=="hi"):
        txt.insert(END,"\n"+"Bot=>Hi there!May I know your name?")
    elif(e.get()=="Sejal"):
        txt.insert(END,"\n"+"Bot=>Thank you,Sejal.How can I help you?")
    elif(e.get()=="courses"):
        txt.insert(END,"\n"+"Bot=>A)DSAI,B)B.Com,C)BSc IT,D)Bsc in Mathematics")
    elif(e.get()=="A"):
        txt.insert(END,"\n"+"Bot=>DSAI is a 2 year postgraduate course.To enable graduates to excel professionally by adapting to the dynamic needs of the academia, industry and research in the field of Data Science and Artificial Intelligence.")
    elif(e.get()=="B"):
        txt.insert(END,"\n"+"Bot=>B.Com is an undergraduate degree in commerce and related subjects. The course is designed to provide students with a wide range of managerial skills and understanding in streams like finance, accounting, taxation and management”.")
    elif(e.get()=="C"):
        txt.insert(END,"\n"+"Bot=>BSc IT is basically about storing, processing, securing, and managing information. This degree is primarily focused on subjects such as software, databases, and networking.")
    elif(e.get()=="D"):
        txt.insert(END,"\n"+"Bot=>This is a three year undergraduate program.This program describe the root of math and logic. The subjects are Calculus, Real Analysis, Mechanics, Linear Algebra etc.")
    elif(e.get()=="information about scholarships"):
            txt.insert(END,"\n"+"Bot=>There are Many Scholarships that you can opt for which can make your course almost 50% cheaper.Please visit this link more details https://www.scholarships.co/")
    elif(e.get()=="library working hours"):
            txt.insert(END,"\n"+"Bot=>Library is open from 10am to 4pm from Monday to Saturday.")
    elif(e.get()=="I want to apply for the summer program"):
         txt.insert(END,"\n"+"Bot=>please visit program section on our official website")
    elif(e.get()=="thank you"):
        txt.insert(END,"\n"+"Bot=>You're Welcome! Please let us know if you have any other queries")
    elif(e.get()=="Sure"):
        txt.insert(END,"\n"+"Bot=>Thank you.")
    elif(e.get()=="schedule of dsai time table"):
        txt.insert(END,"\n"+"Bot=>“Here’s your yearly timetable (link to the PDF file).")
    else:
        txt.insert(END,"\n"+"Bot=>Sorry I didnt get it")
    e.delete(0,END)
    
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
txt.config(bg='black',fg='white')


e=Entry(root,width=100)
send=Button(root,text="Send",command=send,bg='blue',activebackground='lightblue').grid(row=1,column=1)
#Button=Button(bg='blue',activebackground='lightblue')
e.grid(row=1,column=0)
root.title("College Enquiry Chatbot")

#Create a main menu bar

menu=Menu(root)

fileMenu=Menu(root)
fileMenu.add_command(label='Save')
fileMenu.add_command(label='Save As')

menu.add_cascade(label="File",menu=fileMenu)
menu.add_command(label="Edit")
menu.add_command(label="View")
root.config(menu=menu)
root.mainloop()





    

    
