from tkinter import *
root=Tk()
root.geometry('500x500')
root.title("Soul Soothers")
frame_Break=Frame(root,height=500,width=500,bg='gray')
frame_Break.pack(padx=140,pady=160,fill=BOTH,expand=1)
picture_break = PhotoImage(file="")
label=Label(frame_Break,image=picture_break)
label.place(x=0,y=0)

r1=Radiobutton(label,text="Phir Le Aaya Dil",font=('calibre',15))
r1.grid(row=1,column=0)
r2=Radiobutton(label,text="Iktara",font=('calibre',15))
r2.grid(row=2,column=0)
r3=Radiobutton(label,text="Raabta",font=('calibre',15))
r3.grid(row=3,column=0)
r4=Radiobutton(label,text="Kinare",font=('calibre',15))
r4.grid(row=4,column=0)
label_heading=Label(label,text="SoulSoothers",font=('calibre',20, 'bold',"underline"))
label_heading.grid(row=0,column=0)


root.mainloop()