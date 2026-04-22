from tkinter import *
import Training.Calculator_logic as Calculator_logic


root = Tk()
root.title('Calculator')
root.geometry('400x400')

label = Label(root, text='Calculator')
label.pack(pady=20)

text = Label(root, width=30)
text.pack(pady=10)

def on_button_click(button_id):
    if button_id == '1':
        text.config(text='1')
    elif button_id == '2':
        text.config(text='2')
    elif button_id == '3':
        text.config(text='3')
    elif button_id == '4':
        text.config(text='4')
    elif button_id == '5':
        text.config(text='5')
    elif button_id == '6':
        text.config(text='6')
    elif button_id == '7':
        text.config(text='7')
    elif button_id == '8':
        text.config(text='8')
    elif button_id == '9':
        text.config(text='9')
    elif button_id == '0':
        text.config(text='0')

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

Calculator_logic.get_number()


def exit_app():
    root.destroy()

button_exit = Button(root, text='Exit', command=exit_app)
button_exit.pack(pady=10)

root.mainloop()
