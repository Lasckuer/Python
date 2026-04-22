from tkinter import *
from Logic import calculate_sum


root = Tk()
root.title('Calculator')
root.geometry('400x400')

label = Label(root, text='Calculator')
label.pack(pady=20)
label.place(x=100, y=20)

label = Label(root, width=30)
label.pack(pady=10)

def on_button_click(button_id):
    if button_id == '1':
        text.insert(END, '1')
    elif button_id == '2':
        text.insert(END, '2')
    elif button_id == '3':
        text.insert(END, '3')
    elif button_id == '4':
        text.insert(END, '4')
    elif button_id == '5':
        text.insert(END, '5')
    elif button_id == '6':
        text.insert(END, '6')
    elif button_id == '7':
        text.insert(END, '7')
    elif button_id == '8':
        text.insert(END, '8')
    elif button_id == '9':
        text.insert(END, '9')
    elif button_id == '0':
        text.insert(END, '0')
    elif button_id == 'C':
        text.delete('1.0', END)
    elif button_id == 'Plus':
        text.insert(END, '+')
    elif button_id == 'Minus':
        text.insert(END, '-')
    elif button_id == 'Multiply':
        text.insert(END, '*')
    elif button_id == 'Divide':
        text.insert(END, '/')
    elif button_id == 'Equal':
        expression = text.get("1.0", "end-1c")
        try:
            if '+' in expression:
                result = eval(expression)
                text.delete("1.0", "end")
                text.insert("1.0", str(result))
            elif '-' in expression:
                result = eval(expression)
                text.delete("1.0", "end")
                text.insert("1.0", str(result))
            elif '*' in expression:
                result = eval(expression)
                text.delete("1.0", "end")
                text.insert("1.0", str(result))
            elif '/' in expression:
                result = eval(expression)
                text.delete("1.0", "end")
                text.insert("1.0", str(result)) 
        except Exception as e:
            text.delete("1.0", "end")
            text.insert("1.0", "Ошибка")

text = Text(root, width=30, height=2)
text.pack(pady=10)
text.insert('1.0', '')
text.place(x=50, y=50)

button1 = Button(root, text='1', command=lambda: on_button_click('1'), width=2, height=1)
button1.pack(pady=5)
button1.place(x=50, y=150)
button2 = Button(root, text='2', command=lambda: on_button_click('2'), width=2, height=1)
button2.pack(pady=5)
button2.place(x=100,y=150)
button3 = Button(root, text='3', command=lambda: on_button_click('3'), width=2, height=1)
button3.pack(pady=5)
button3.place(x=150,y=150)
button4 = Button(root, text='4', command=lambda: on_button_click('4'), width=2, height=1)
button4.pack(pady=5)
button4.place(x=50,y=200)
button5 = Button(root, text='5', command=lambda: on_button_click('5'), width=2, height=1)
button5.pack(pady=5)
button5.place(x=100,y=200)
button6 = Button(root, text='6', command=lambda: on_button_click('6'), width=2, height=1)
button6.pack(pady=5)
button6.place(x=150,y=200)
button7 = Button(root, text='7', command=lambda: on_button_click('7'), width=2, height=1)
button7.pack(pady=5)
button7.place(x=50,y=250)
button8 = Button(root, text='8', command=lambda: on_button_click('8'), width=2, height=1)
button8.pack(pady=5)
button8.place(x=100,y=250)
button9 = Button(root, text='9', command=lambda: on_button_click('9'), width=2, height=1)
button9.pack(pady=5)
button9.place(x=150,y=250)
button0 = Button(root, text='0', command=lambda: on_button_click('0'), width=2, height=1)
button0.pack(pady=5)
button0.place(x=100,y=300)
button_clear = Button(root, text='C', command=lambda: on_button_click('C'), width=2, height=1)
button_clear.pack(pady=5)
button_clear.place(x=150,y=300)
button_plus = Button(root, text='+', command=lambda: on_button_click('Plus'), width=2, height=1)
button_plus.pack(pady=5)
button_plus.place(x=200,y=150)
button_minus = Button(root, text='-', command=lambda: on_button_click('Minus'), width=2, height=1)
button_minus.pack(pady=5)
button_minus.place(x=200,y=200)
button_multiply = Button(root, text='*', command=lambda: on_button_click('Multiply'), width=2, height=1)
button_multiply.pack(pady=5)
button_multiply.place(x=200,y=250)
button_divide = Button(root, text='/', command=lambda: on_button_click('Divide'), width=2, height=1)
button_divide.pack(pady=5)
button_divide.place(x=200,y=300)
button_equal = Button(root, text='=', command=lambda: on_button_click('Equal'), width=2, height=9)
button_equal.pack(pady=5)
button_equal.place(x=250,y=150)

def exit_app():
    root.destroy()

button_exit = Button(root, text='Exit', command=exit_app, width=2, height=1)
button_exit.pack(pady=5)
button_exit.place(x=50,y=300)

root.mainloop()
