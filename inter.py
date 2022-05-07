from  tkinter import *
from pyglet import *

count1=1
count2=1
count3=1
count4=1
root = Tk()
root.minsize(width=360,height=640)
root['bg']= '#fff2ea'


def click1():
    global c1,count1
    c1.destroy()
    count1+=1
    if count1%2==1:    
        c1=Button(root, image=img_c1,background='#fff2ea',border=0,command=click1)
        c1.place(anchor='center', relx=0.8,rely=0.15)
    else:
        c1=Button(root, image=img_c2,background='#fff2ea', border=0,command=click1)
        c1.place(anchor='center', relx=0.8,rely=0.15)
def click2():
    global c2, count2
    c2.destroy()
    count2+=1
    if count2%2==1:
        c2 = Button(root ,image= img_c1,background='#fff2ea',bd=1, border=0,command=click2)
        c2.place(anchor='center', relx=0.8,rely=0.35)
    else:
        c2 = Button(root ,image=img_c2 ,background='#fff2ea', border=0,command=click2)
        c2.place(anchor='center', relx=0.8,rely=0.35)
def click3():
    global c3 ,count3
    c3.destroy()
    count3+=1
    if count3%2==1:
        c3=Button(root, image=img_c1,background='#fff2ea',command=click3, border=0)
        c3.place(anchor='center', relx=0.8,rely=0.55)
    else:
        c3 = Button(root ,image=img_c2,background='#fff2ea',border=0,command=click3)
        c3.place(anchor='center', relx=0.8,rely=0.55)
def click4():
    global c4 ,count4
    c4.destroy()
    count4+=1
    if count4%2==1:
        c4=Button(root,background='#fff2ea' ,image=img_c1,command=click4, border=0)
        c4.place(anchor='center', relx=0.8,rely=0.75)
    else:
        c4 = Button(root ,image=img_c2 ,background='#fff2ea',border=0,command=click4)
        c4.place(anchor='center', relx=0.8,rely=0.75)

img_c1 = PhotoImage(file= 'stat_2.png')
img_c2=PhotoImage(file="stat_1.png")
img_menu= PhotoImage(file='menu.png')
menu = Button ( root, border=0,background='#fff2ea',image = img_menu)
save_me= Label(root, text="SAVE ME",background='#fff2ea',font=("Jura", 25))

text_1 = Label( root, text='Оповещения',background='#fff2ea',font=("Jura", 15))
text_2= Label( root, text='Персональные данные',background='#fff2ea',font=("Jura", 15))
text_3= Label( root, text='Геолокация',background='#fff2ea',font=("Jura", 15))
text_4_1= Label( root, text='Озвучивание  ',background='#fff2ea',font=("Jura", 15))
text_4_2=Label( root, text='порядка действий',background='#fff2ea',font=("Jura", 15))

c1 = Button(root ,image= img_c1,bd=1,background='#fff2ea', border=0,command=click1)
c2 = Button(root ,image= img_c1,bd=1,background='#fff2ea', border=0,command=click2)
c3 = Button(root ,image= img_c1,bd=1,background='#fff2ea',  border=0,command=click3)
c4= Button(root ,image= img_c1,bd=1,background='#fff2ea',  border=0,command=click4)


menu.place(relx=1,rely=0,anchor="ne")
c1.place(anchor='center', relx=0.8,rely=0.15)
c2.place(anchor='center', relx=0.8,rely=0.35)
c3.place(anchor='center', relx=0.8,rely=0.55)
c4.place (anchor='center', relx=0.8,rely=0.75)
text_1.place(anchor='center', relx=0.25,rely=0.15)
text_2.place(anchor='center', relx=0.3,rely=0.35)
text_3.place(anchor='center', relx=0.25,rely=0.55)
text_4_1.place(anchor='center', relx=0.25,rely=0.74)
text_4_2.place(anchor='center', relx=0.25,rely=0.78)
save_me.place(relx=0.49,rely=0.03,x=20,y=0,anchor="center")
root.mainloop()