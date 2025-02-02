from tkinter import *

window = Tk()
window.geometry('550x540')
window.title('Calculator')
window.config(background='black')
affichage = ''
old_affichage = 0
result = 0

def btn1():
    global affichage
    global result
    global old_affichage
    sign = (old_affichage[-1])
    result = eval(f"{old_affichage.replace(old_affichage[-1],'')} {old_affichage[-1]} {affichage[len(old_affichage):]}") 
    label.config(text=result)
    
def btn2():
    global affichage
    affichage += '+'
    global old_affichage
    old_affichage = affichage
    label.config(text=affichage)
def btn3():
    global affichage
    affichage += '-'
    global old_affichage
    old_affichage = affichage
    label.config(text=affichage)
def btn4():
    global affichage
    affichage += '/'
    global old_affichage
    old_affichage = affichage
    label.config(text=affichage)
def btn5():
    global affichage
    affichage += '*'
    global old_affichage
    old_affichage = affichage
    label.config(text=affichage)
def btn6():
    global affichage
    affichage =''
    label.config(text=affichage)
def btn7():
    global affichage
    affichage += '0'
    label.config(text=affichage)
def btn8():
    global affichage
    affichage += '1'
    label.config(text=affichage)
def btn9():
    global affichage
    affichage += '2'
    label.config(text=affichage)
def btn10():
    global affichage
    affichage += '3'
    label.config(text=affichage)
def btn11():
    global affichage
    affichage += '4'
    label.config(text=affichage)
def btn12():
    global affichage
    affichage += '5'
    label.config(text=affichage)
def btn13():
    global affichage
    affichage += '6'
    label.config(text=affichage)
def btn14():
    global affichage
    affichage += '7'
    label.config(text=affichage)
def btn15():
    global affichage
    affichage += '8'
    label.config(text=affichage)
def btn16():
    global affichage
    affichage += '9'
    label.config(text=affichage)

def btn17():
    global affichage
    affichage = affichage.replace(affichage[-1],'')
    label.config(text=affichage)


equal = Button(window,
               text='=',
               bg='#ff9717',
               fg='white',
               width=7,
               height=2,
               command = btn1)
plus = Button(window,
               text='+',
               bg='#ff9717',
               fg='white',width=10,height=2,command = btn2)
minus = Button(window,
               text='-',
               bg='#ff9717',
               fg='white',width=10,height=2,command = btn3)
divide = Button(window,
               text='/',
               bg='#ff9717',
               fg='white',width=7,height=2,command = btn4)
multiply = Button(window,
               text='x',
               bg='#ff9717',
               fg='white',width=10,height=2,command = btn5)
clear = Button(window,
               text='C',
               bg='#ff9717',
               fg='white',width=7,height=2,command = btn6)
delete = Button(window,
               text='del',
               bg='#ff9717',
               fg='white',width=7,height=2,command = btn17)
zero = Button(window,
               text='0',
               bg='#3b3b3b',
               fg='white',width=7,height=2,command = btn7)
one = Button(window,
               text='1',
               bg='#3b3b3b',
               fg='white',width=10,height=2,command = btn8)
two = Button(window,
               text='2',
               bg='#3b3b3b',
               fg='white',width=10,height=2,command = btn9)
three = Button(window,
               text='3',
               bg='#3b3b3b',
               fg='white',width=10,height=2,command = btn10)
four = Button(window,
               text='4',
               bg='#3b3b3b',
               fg='white',width=10,height=2,command = btn11)
five = Button(window,
               text='5',
               bg='#3b3b3b',
               fg='white',width=10,height=2,command = btn12)
six = Button(window,
               text='6',
               bg='#3b3b3b',
               fg='white',width=10,height=2,command = btn13)
seven = Button(window,
               text='7',
               bg='#3b3b3b',
               fg='white',width=10,height=2,command = btn14)
eight = Button(window,
               text='8',
               bg='#3b3b3b',
               fg='white',width=10,height=2,command = btn15)
nine = Button(window,
               text='9',
               bg='#3b3b3b',
               fg='white',width=10,height=2,command = btn16)

seven.place(x=50, y=140)
eight.place(x=180, y=140)
nine.place(x=305, y=140)
multiply.place(x=430, y=140)
four.place(x=50, y=240)
five.place(x=180, y=240)
six.place(x=305, y=240)
minus.place(x=430, y=240)
one.place(x=50, y=340)
two.place(x=180, y=340)
three.place(x=305, y=340)
plus.place(x=430, y=340)
clear.place(x=50, y=430)
zero.place(x=150, y=430)
equal.place(x=250, y=430)
divide.place(x=350, y=430)
delete.place(x=450, y= 430)


label = Label(window,width=70,height=4,anchor='w')
label.place(y=20,x=30)



window.mainloop()





