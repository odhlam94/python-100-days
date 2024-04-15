import tkinter

window = tkinter.Tk()
window.title('Hello World')


#
def click():
    global label
    label['text'] = 'clicked button'


# Label
label = tkinter.Label(window, text='Hello World')
label.pack()

# Text box
txt_box = tkinter.Entry(window)
txt_box.pack()

# Button
button = tkinter.Button(window, text='Click Me', command=click)
button.pack()

window.mainloop()
