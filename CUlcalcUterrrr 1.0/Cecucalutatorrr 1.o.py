import tkinter
from PIL import ImageTk, Image
from tkinter import messagebox
Chocolate_color="#8b4513"
Dark_chocolate_color="#552a0c"
oRAnGEEe="orange"
wHiTe="#FFFFFF"
Window=tkinter.Tk()
Window.title("Chocolatator 1.o")
Window.geometry("1100x670")
Window.configure(bg=Chocolate_color)
Answer_entry=tkinter.Entry(Window, width=17, font=("Rupee",30))
Answer_entry.grid(row=1, column=1,columnspan=3, pady=15, padx=15)

img=Image.open(r"img/Mike Wazowski.png").resize((150,500))
img_photo=ImageTk.PhotoImage(img)
img_label=tkinter.Label(image=img_photo)
img_label.grid(row=2, column=7, rowspan=3)
# img_label_2=tkinter.Label(image=img_photo)
# img_label_2.grid(row=3, column=7)
# img_label_3=tkinter.Label(image=img_photo)
# img_label_3.grid(row=4, column=7)

OPERATORS={"(":0,
           ")":0,
           "*":2,
           "×":2,
           "/":2,
           "÷":2,
           "+":1,
           "-":1
           }

def inetly(character):
    Answer_entry.insert(len(Answer_entry.get()), character)

def inetly_1():
    text=Answer_entry.get()
    Result_list = []
    temporary_str = ""
    for Character in text:
        if Character in OPERATORS.keys():
            if len(temporary_str) != 0:
                Result_list.append(temporary_str)
                temporary_str = ""
            Result_list.append(Character)
        if Character.isdigit():
            temporary_str = temporary_str + Character
    if len(temporary_str) != 0:
        Result_list.append(temporary_str)
    result=inelator(Result_list)
    messagebox.showinfo("Cecucalutatorrr 1.o", f"YoUr aNsWEr iS {result}")

def inelator(list_exp):
    Operators=[]
    Operands=[]
    for character in list_exp:
        if character.isdigit():
            Operands.append(character)
        else:
            if len(Operators)==0:
                Operators.append(character)
            elif character=="(":
                Operators.append(character)
                continue
            elif character==")":
                while Operators[-1]!="(":
                    n2=Operands.pop()
                    n1=Operands.pop()
                    Operator=Operators.pop()
                    result=spinning_monkeee(n1,n2,Operator)
                    Operands.append(result)
                Operators.pop()
                continue
            elif OPERATORS[character]>OPERATORS[Operators[-1]]:
               Operators.append(character)

            else:
                n2 = Operands.pop()
                n1 = Operands.pop()
                Operator = Operators.pop()
                result = spinning_monkeee(n1, n2, Operator)
                Operands.append(result)
                Operators.append(character)

    while len(Operators)!=0 and len(Operands)>=2:
        n2 = Operands.pop()
        n1 = Operands.pop()
        Operator = Operators.pop()
        result = spinning_monkeee(n1, n2, Operator)
        Operands.append(result)
    return Operands[0]

def spinning_monkeee(n1, n2, operator):
    n1=float(n1)
    n2=float(n2)
    if operator == "+":
        return n1 + n2
    if operator == "-":
        return n1 - n2
    if operator == "×":
        return n1 * n2
    if operator == "÷":
        return n1 / n2

button_1=tkinter.Button(background=Dark_chocolate_color, text="1", font=("MS Serif", 10), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("1"))
button_1.grid(row=2, column=1, padx=20, pady=20)
button_2=tkinter.Button(background=Dark_chocolate_color, text="2", font=("MS Serif", 10), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("2"))
button_2.grid(row=2, column=2, padx=20, pady=20)
button_3=tkinter.Button(background=Dark_chocolate_color, text="3", font=("MS Serif", 10), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("3"))
button_3.grid(row=2, column=3, padx=20, pady=20)
button_4=tkinter.Button(background=Dark_chocolate_color, text="4", font=("MS Serif", 10), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("4"))
button_4.grid(row=3, column=1, padx=20, pady=20)
button_5=tkinter.Button(background=Dark_chocolate_color, text="5", font=("MS Serif", 10), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("5"))
button_5.grid(row=3, column=2, padx=20, pady=20)
button_6=tkinter.Button(background=Dark_chocolate_color, text="6", font=("MS Serif", 10), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("6"))
button_6.grid(row=3, column=3, padx=20, pady=20)
button_7=tkinter.Button(background=Dark_chocolate_color, text="7", font=("MS Serif", 10), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("7"))
button_7.grid(row=4, column=1, padx=20, pady=20)
button_8=tkinter.Button(background=Dark_chocolate_color, text="8", font=("MS Serif", 10), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("8"))
button_8.grid(row=4, column=2, padx=20, pady=20)
button_9=tkinter.Button(background=Dark_chocolate_color, text="9", font=("MS Serif", 10), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("9"))
button_9.grid(row=4, column=3, padx=20, pady=20)
button_0=tkinter.Button(background=Dark_chocolate_color, text="0", font=("MS Serif", 10), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("0"))
button_0.grid(row=5, column=2, padx=20, pady=20)

button_addition=tkinter.Button(background=Dark_chocolate_color, text="+", font=("MS Serif", 13), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("+"))
button_addition.grid(row=2, column=5, padx=(150,40), pady=20)
button_subtraction=tkinter.Button(background=Dark_chocolate_color, text="-", font=("MS Serif", 13), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("-"))
button_subtraction.grid(row=2, column=6, padx=40, pady=20)
button_multiplication=tkinter.Button(background=Dark_chocolate_color, text="×", font=("MS Serif", 13), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("×"))
button_multiplication.grid(row=3, column=5, padx=(150,40), pady=20)
button_division=tkinter.Button(background=Dark_chocolate_color, text="÷", font=("MS Serif", 13), width=10, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly("÷"))
button_division.grid(row=3, column=6, padx=40, pady=20)
button_equal_sign=tkinter.Button(background=Dark_chocolate_color, text="=", font=("MS Serif", 13), width=30, height=5, activebackground=oRAnGEEe, fg=wHiTe, command=lambda:inetly_1())
button_equal_sign.grid(row=4, column=5, columnspan=2, padx=(150,40), pady=20)

Window.mainloop()