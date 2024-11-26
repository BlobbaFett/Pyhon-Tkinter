import tkinter

master = tkinter.Tk()
master.geometry('400x400')
master.title('Character Ocurrence Counter')

def display_ocurrences():
    user = entry.get().lower().replace(" ","")
    char_count = {}

    for char in user:
        current_count = char_count.get(char, 0)
        char_count[char] = current_count + 1
    result.config(text=str(char_count))

label1= tkinter.Label(master, text='Enter a Message:')
label1.pack(pady=10)

entry = tkinter.Entry(master, width=30)
entry.pack()
button = tkinter.Button(master, text='Count Ocurrences', command=display_ocurrences)
button.pack(pady=10)
result = tkinter.Label(master, text='')
result.pack()

master.mainloop()