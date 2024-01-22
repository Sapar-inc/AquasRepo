# def say_hello():
#     print('hello')
# def add_label():
#     label = tk.Label(win, text='new label')
#     label.pack()
# def Increase():
#     global counter
#     counter += 1
#     button_three['text'] = f'Новое значение {counter}'
#
# counter = 0
#
# import tkinter as tk
#
# win = tk.Tk()
#
# win.title('My Project APP')
# win.geometry('500x500+10+10')
#
# photo = tk.PhotoImage(file='main_icon.png')
# win.iconphoto(False, photo)
#
# win.config(bg='#5D910F')
#
# win.minsize(400,400)
# win.maxsize(800,800)
# win.resizable(True, True)
#
#
# #widget
# label_first = tk.Label(win,
#                        text='Hello',
#                        bg='#7DC019',
#                        fg='#fff',
#                        font=('Aerial', 20, 'bold'),
#                        padx=10,
#                        pady=10,
#                        width=100,
#                        height=2,
#                        anchor='center',
#                        relief=tk.RAISED,
#                        bd=5,
#                        justify=tk.CENTER
#                        )
# label_first.pack()
#
# button_test = tk.Button(win, text='click me!', command=say_hello)
# button_test.pack()
#
# button_second = tk.Button(win, text='add label!', command=add_label)
# button_second.pack()
#
# button_three = tk.Button(win, text=f'Счётчик: {counter}', command=Increase)
# button_three.pack()
#
# win.mainloop()



import tkinter as tk
# from splash_screen import show_splash
# from menu import menu_page
from menu import start

if __name__ == "__main__":
    start()