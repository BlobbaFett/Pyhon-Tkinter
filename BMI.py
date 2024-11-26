import tkinter

master = tkinter.Tk()
master.geometry('400x400')
master.title('BMI Calculator')

def display_BMI():
    hight = entry.get()
    weight = entry2.get()

    BMI = float(weight)/(float(hight))**2
    result.config(text=f'BMI = {BMI}')
    
    if BMI >= 30:
        result2.config(text='Obesity')
    elif BMI == 25: 
        result2.config(text='Overweight')
    elif BMI >= 24.99:
        result2.config(text='Pre-obesity')
    elif BMI >= 18.5:
        result2.config(text='Normal range')
    elif BMI <= 18.49: 
        result2.config(text='Underweight')

label1= tkinter.Label(master, text=('Enter your height in meters:'))
label1.pack(pady=10)
entry = tkinter.Entry(master, width=30)
entry.pack()

label1= tkinter.Label(master, text='Enter your weight in kilograms:')
label1.pack(pady=10)
entry2 = tkinter.Entry(master, width=30)
entry2.pack()

button = tkinter.Button(master, text='Calculate BMI', command=display_BMI)
button.pack(pady=10)
result = tkinter.Label(master, text='')
result.pack()

result2 = tkinter.Label(master, text='')
result2.pack()

master.mainloop()