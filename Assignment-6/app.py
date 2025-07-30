from tkinter import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(textspace.get()))
            textspace.delete(0, END)
            textspace.insert(END, result)
        except Exception as ep:
            textspace.delete(0, END)
            textspace.insert(END, "error")
    elif text =="CLEAR":
        textspace.delete(0, END)
    else:
        textspace.insert(END, text)

window = Tk()
window.geometry("300x420")
window.title("Calculator")

topfame = Frame(
    window,
    width=300,
    height=50,
    background='#123'

)
topfame.pack(side=TOP)

bottomFrame = Frame(
    window,
    width=300,
    height=350,
    background='#345'

)
bottomFrame.pack(side=BOTTOM)

textspace = Entry(
    topfame,
    width=30,
    borderwidth=5,
    font=('Arial 15'),
    justify=RIGHT
)
textspace.pack(fill=Y, expand=True)

# Buttons
custom_width=5
custom_height=2

clearBtn = Button(
    bottomFrame,
    text="CLEAR",
    height=custom_height,
    width=10,
    font=("Arial 15"),
    borderwidth=5
)
clearBtn.grid(row=0, columnspan=3, sticky='nsew')
clearBtn.bind('<Button-1>', click)

addBtn = Button(
    bottomFrame,
    text='+',
    width=custom_width,
    height=custom_height,
    borderwidth=5,
    font=("Arial 15"),
)
addBtn.grid(row=0, column=3)
addBtn.bind('<Button-1>', click)

# Row --> 1
btn1 = Button(
    bottomFrame,
    text="1",
    font=("Arial 15"),
    width=custom_width,
    height=custom_height,
    borderwidth=5

)
btn1.grid(row=1, column=0)
btn1.bind('<Button-1>', click)

btn2 = Button(
    bottomFrame,
    text="2",
    font=("Arial 15"),
    width=custom_width,
    height=custom_height,
    borderwidth=5

)
btn2.grid(row=1, column=1)
btn2.bind('<Button-1>', click)

btn3 = Button(
    bottomFrame,
    text="3",
    font=("Arial 15"),
    width=custom_width,
    height=custom_height,
    borderwidth=5

)
btn3.grid(row=1, column=2)
btn3.bind('<Button-1>', click)

subBtn = Button(
    bottomFrame,
    text="-",
    height=custom_height,
    width=custom_width,
    font=("Arial 15"),
    borderwidth=5
)
subBtn.grid(row=1, column=3)
subBtn.bind('<Button-1>', click)

btn4 = Button(
    bottomFrame,
    text="4",
    font=("Arial 15"),
    width=custom_width,
    height=custom_height,
    borderwidth=5

)
btn4.grid(row=2, column=0)
btn4.bind('<Button-1>', click)

btn5 = Button(
    bottomFrame,
    text="5",
    font=("Arial 15"),
    width=custom_width,
    height=custom_height,
    borderwidth=5

)
btn5.grid(row=2, column=1)
btn5.bind('<Button-1>', click)

btn6 = Button(
    bottomFrame,
    text="6",
    font=("Arial 15"),
    width=custom_width,
    height=custom_height,
    borderwidth=5

)
btn6.grid(row=2, column=2)
btn6.bind('<Button-1>', click)

mulBtn = Button(
    bottomFrame,
    text="*",
    font=("Arial 15"),
    width=custom_width,
    height=custom_height,
    borderwidth=5
)
mulBtn.grid(row=2, column=3)
mulBtn.bind('<Button-1>', click)

# Row --> 3
btn7 = Button(
    bottomFrame,
    text="7",
    font=("Arial 15"),
    width=custom_width,
    height=custom_height,
    borderwidth=5

)
btn7.grid(row=3, column=0)
btn7.bind('<Button-1>', click)

btn8 = Button(
    bottomFrame,
    text="8",
    font=("Arial 15"),
    width=custom_width,
    height=custom_height,
    borderwidth=5

)
btn8.grid(row=3, column=1)
btn8.bind('<Button-1>', click)

btn9 = Button(
    bottomFrame,
    text="9",
    font=("Arial 15"),
    width=custom_width,
    height=custom_height,
    borderwidth=5

)
btn9.grid(row=3, column=2)
btn9.bind('<Button-1>', click)

divBtn = Button(
    bottomFrame,
    text='/',
    font=("Arial 15"),
    width=custom_width,
    height=custom_height,
    borderwidth=5
)
divBtn.grid(row=3, column=3)
divBtn.bind('<Button-1>', click)

# row --> 4
eqBtn = Button(
    bottomFrame,
    text="=",
    font=("Arial 15"),
    height=custom_height,
    borderwidth=5

)
eqBtn.grid(row=4, columnspan=4, sticky='nsew')
eqBtn.bind('<Button-1>', click)

window.mainloop()