from tkinter import * 

win = Tk()
win.geometry('300x500')

e_input = StringVar(win, value='')

e = Entry(win, width=15, font=('Ariel', 20), textvariable=e_input)
e.grid(column=0, row=0)


def num_enter(num):
    e.insert(END, num)
    return

def num_clear():
    e.delete(0, END)

def num_equal():
    divide = []
    multiply = []
    subratct = []
    add = []
    
    
    num = e.get()
    num_list = list(num)
    
    for char in range(len(num_list)):
        var1 = char - 1
        var2 = char + 1
        if(num_list[char] == '/'):
            output = (int(num_list[var1])) / (int(num_list[var2]))
            num_clear()
            num_enter(output)
        elif(num_list[char] == '*'):
            output = (int(num_list[var1])) * (int(num_list[var2]))
            num_clear()
            num_enter(output)
        elif(num_list[char] == '-'):
            if(num_list[0] == "-"):
                output = int(num_list[var2])
                output = -output
                output = output - (int(num_list[var2]))
                num_clear()
                num_enter(output)
            else:
                output = (int(num_list[var1])) - (int(num_list[var2]))
                num_clear()
                num_enter(output)
        elif(num_list[char] == '+'):
            output = (int(num_list[var1])) + (int(num_list[var2]))
            num_clear()
            num_enter(output)
    
    
    
    '''
    for char in range(len(num_list)):
        if(num_list[char] != "/"):
            equal_num += int(num_list[char])
      
        elif(num_list[char] != "*"):
            equal_num += int(num_list[char])
        
        elif(num_list[char] != "-"):
            equal_num += int(num_list[char])
            
        elif(num_list[char] != "+"):
            equal_num += int(num_list[char])
    '''


#First Row
seven = Button(win,text="7", width=9, height=3, padx=0.25, command=lambda:num_enter(7))
seven.grid(column=0, row=1, sticky="NW")

eight = Button(win,text="8", width=9, height=3, padx=0.25, command=lambda:num_enter(8))
eight.grid(column=0, row=1, sticky="N")

nine = Button(win,text="9", width=9, height=3, padx=0.25, command=lambda:num_enter(9))
nine.grid(column=0, row=1, sticky="NE")

#Second Row
four = Button(win,text="4", width=9, height=3, padx=0.25, command=lambda:num_enter(4))
four.grid(column=0, row=2, sticky="NW")

five = Button(win,text="5", width=9, height=3, padx=0.25, command=lambda:num_enter(5))
five.grid(column=0, row=2, sticky="N")

six = Button(win,text="6", width=9, height=3, padx=0.25, command=lambda:num_enter(6))
six.grid(column=0, row=2, sticky="NE")


#Third Row
two = Button(win,text="2", width=9, height=3, padx=0.25, command=lambda:num_enter(2))
two.grid(column=0, row=3, sticky="NW")

three = Button(win,text="3", width=9, height=3, padx=0.25, command=lambda:num_enter(3))
three.grid(column=0, row=3, sticky="N")

divide = Button(win,text="/", width=9, height=1, padx=0.25, command=lambda:num_enter("/"))
divide.grid(column=0, row=3, sticky="NE")

multiply = Button(win,text="*", width=9, height=1, padx=0.25, command=lambda:num_enter("*"))
multiply.grid(column=0, row=3, sticky="SE")

#Fourth Row
zero = Button(win,text="0", width=9, height=3, padx=0.25, command=lambda:num_enter(0))
zero.grid(column=0, row=4, sticky="NW")

one = Button(win,text="1", width=9, height=3, padx=0.25, command=lambda:num_enter(1))
one.grid(column=0, row=4, sticky="N")

subtract = Button(win,text="-", width=9, height=1, padx=0.25, command=lambda:num_enter("-"))
subtract.grid(column=0, row=4, sticky="NE")

add = Button(win,text="+", width=9, height=1, padx=0.25, command=lambda:num_enter("+"))
add.grid(column=0, row=4, sticky="SE")


#Fifth Row
clear = Button(win,text="AC", width=20, height=3, padx=0.25, command=lambda:num_clear())
clear.grid(column=0, row=5, sticky="NW")

enter = Button(win,text="=", width=9, height=3, padx=0.25, command=lambda:num_equal())
enter.grid(column=0, row=5, sticky="NE")







win.mainloop()