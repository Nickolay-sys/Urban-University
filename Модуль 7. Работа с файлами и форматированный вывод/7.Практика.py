import tkinter

window = tkinter.Tk()
window.title('Проводник')
window.geometry('500x500')
window.configure(bg='gold')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл', height=5 ,width=20, background='silver')
text.grid(column=1,row=1)
button_select = tkinter.Button(window, width=20, height=3, text='Выберите файл')
button_select.grid(column=1, row=2)
window.mainloop()