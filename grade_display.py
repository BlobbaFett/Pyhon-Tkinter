import tkinter


def display_grade():
    user = entry.get().upper()

    if user == 'O':
        label2.config(text='Outstanding')
    elif user == 'A':
        label2.config(text='Very Good')
    elif user == 'B':
        label2.config(text='Good')
    elif user == 'C':
        label2.config(text='Average')
    elif user == 'F':
        label2.config(text='Fail')
    else:
        label2.config(text='Invalid Grade')

master = tkinter.Tk()
master.geometry('400x400')
master.title('Grades Display GUI')

label1= tkinter.Label(master, text='Enter Grade (O, A, B, C, or F)')
label1.pack(pady=10)

entry = tkinter.Entry(master, width=10)
entry.pack()
button = tkinter.Button(master, text='Submint', command=display_grade)
button.pack(pady=10)
label2 = tkinter.Label(master, text='')
label2.pack()


master.mainloop()