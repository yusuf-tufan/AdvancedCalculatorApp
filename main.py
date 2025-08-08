from tkinter import *
from tkinter import messagebox

first_num=second_num=operator=None



def get_digit(digit):

    try:
        current=result_label['text']
        new=current + str(digit)
        result_label.config(text=new)
    except:
        print('error')

def clear():
    result_label.config(text='')

def clean():
    now_lbl=result_label.cget('text')
    if len(now_lbl)!=0:
        claan_character=now_lbl[:-1]
        result_label.config(text=claan_character)
def get_operator(op):
    global first_num,operator

    try:
        first_num= int(result_label['text'])
        operator=op
        result_label.config(text='')

    except:
        messagebox.showinfo(title='Error',message='Number First')

def get_result():
    global first_num,second_num,operator

    try:
        second_num=int(result_label['text'])
        if operator=='+':
            result_label.config(text=f"{first_num}+{second_num}\n={str(first_num + second_num)}")

        elif operator=='-':
            result_label.config(text=f"{first_num}-{second_num}\n={str(first_num + second_num)}")
        elif operator=='*':
            result_label.config(text=f"{first_num}x{second_num}\n={str(first_num + second_num)}")
        else:
            if second_num==0:
                result_label.config(text='Error')
            else:
                result_label.config(text=f"{first_num}/{second_num}\n={str(round(first_num / second_num,4))}")

    except:
        messagebox.showinfo(title='Error',message="- Number First\n- You can only calculate two numbers.\n- You cannot send more than one transaction.")


#window
window=Tk()
window.configure(background='black',padx=300)
window.resizable(False,False)
window.geometry("1000x400")

#result
result_label=Label(text='',bg='black',fg='white')
result_label.grid(row=0,column=1,columnspan=3000,pady=(50,20),sticky='w')
result_label.config(font=('verdana',30,'bold'))
"""
lbl_process=Label(text='',bg='black',fg='white',)
lbl_process.grid(row=0,column=10,columnspan=2000,pady=(50,25),sticky='w')
lbl_process.config(font=('verdana',30,'bold'))
"""
#numbers
btn1=Button(text='1',command=lambda :get_digit(1))
btn1.grid(row=1,column=1)
btn1.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))
btn2=Button(text='2',command=lambda :get_digit(2))
btn2.grid(row=1,column=2)
btn2.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))
btn3=Button(text='3',command=lambda :get_digit(3))
btn3.grid(row=1,column=3)
btn3.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))
btn4=Button(text='4',command=lambda :get_digit(4))
btn4.grid(row=2,column=1)
btn4.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))
btn5=Button(text='5',command=lambda :get_digit(5))
btn5.grid(row=2,column=2)
btn5.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))
btn6=Button(text='6',command=lambda :get_digit(6))
btn6.grid(row=2,column=3)
btn6.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))
btn7=Button(text='7',command=lambda :get_digit(7))
btn7.grid(row=3,column=1)
btn7.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))
btn8=Button(text='8',command=lambda :get_digit(8))
btn8.grid(row=3,column=2)
btn8.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))
btn9=Button(text='9',command=lambda :get_digit(9))
btn9.grid(row=3,column=3)
btn9.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))
btn0=Button(text='0',command=lambda :get_digit(0))
btn0.grid(row=4,column=2)
btn0.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))

#operators
btn_plus=Button(text='+',command=lambda :get_operator('+'))
btn_plus.grid(row=1,column=4)
btn_plus.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))
btn_minus=Button(text='-',command=lambda :get_operator('-'))
btn_minus.grid(row=2,column=4)
btn_minus.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))
btn_multiply=Button(text='x',command=lambda :get_operator('*'))
btn_multiply.grid(row=3,column=4)
btn_multiply.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))
btn_divide=Button(text='/',command=lambda :get_operator('/'))
btn_divide.grid(row=4,column=4)
btn_divide.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))

#clear
btn_clr=Button(text='C',command=clear)
btn_clr.grid(row=4,column=1)
btn_clr.config(width=4,height=1,bg='#ff4500',font=('Arial',15,'bold'))

#equals
btn_equal=Button(text='=',command=get_result)
btn_equal.grid(row=4,column=3)
btn_equal.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))

btn_clean=Button(text='⌫',command=clean)
btn_clean.grid(row=5,column=4)
btn_clean.config(width=4,height=1,bg='#5f9ea0',font=('Arial',15,'bold'))


window.mainloop()