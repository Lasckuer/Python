from tkinter import *


root = Tk()
root.title('Calculator')
root.geometry('400x400')

label = Label(root, text='Calculator')
label.pack(pady=20)

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
        text.insert(END, '=')
  

text = Text(root, width=30, height=5)
text.pack(pady=10)
text.insert('1.0', 'Enter numbers here')

button1 = Button(root, text='1', command=lambda: on_button_click('1'))
button1.pack(pady=5)
button2 = Button(root, text='2', command=lambda: on_button_click('2'))
button2.pack(pady=5)
button3 = Button(root, text='3', command=lambda: on_button_click('3'))
button3.pack(pady=5)
button4 = Button(root, text='4', command=lambda: on_button_click('4'))
button4.pack(pady=5)
button5 = Button(root, text='5', command=lambda: on_button_click('5'))
button5.pack(pady=5)
button6 = Button(root, text='6', command=lambda: on_button_click('6'))
button6.pack(pady=5)
button7 = Button(root, text='7', command=lambda: on_button_click('7'))
button7.pack(pady=5)
button8 = Button(root, text='8', command=lambda: on_button_click('8'))
button8.pack(pady=5)
button9 = Button(root, text='9', command=lambda: on_button_click('9'))
button9.pack(pady=5)
button0 = Button(root, text='0', command=lambda: on_button_click('0'))
button0.pack(pady=5)
button_clear = Button(root, text='C', command=lambda: on_button_click('C'))
button_clear.pack(pady=5)
button_plus = Button(root, text='+', command=lambda: on_button_click('Plus'))
button_plus.pack(pady=5)
button_minus = Button(root, text='-', command=lambda: on_button_click('Minus'))
button_minus.pack(pady=5)
button_multiply = Button(root, text='*', command=lambda: on_button_click('Multiply'))
button_multiply.pack(pady=5)
button_divide = Button(root, text='/', command=lambda: on_button_click('Divide'))
button_divide.pack(pady=5)
button_equal = Button(root, text='=', command=lambda: on_button_click('Equal'))
button_equal.pack(pady=5)


def exit_app():
    root.destroy()

button_exit = Button(root, text='Exit', command=exit_app)
button_exit.pack(pady=10)

root.mainloop()
