import sys
from tkinter import Tk, messagebox, ttk
import subprocess

info_text = 'Players are moved by pressing the keys:\n' \
            '\tw key and up arrow,\n\ta key and left arrow,\n\ts key and down arrow,\n\td key and right arrow.\n' \
            'Shooting is carried out by pressing the g key or the space bar.\n' \
            'The players have three lives (hearts).\n' \
            'Their task is to make sure that the enemy runs out of them, respectively.'


def start_game():
    root.withdraw()
    window = Tk()
    window.resizable(False, False)
    window.title('Levels')
    window.geometry(f'+{width}+{height}')

    def handle_close():
        window.destroy()
        root.deiconify()

    window.protocol("WM_DELETE_WINDOW", handle_close)

    define_style(window)

    def start_level(number):
        def func():
            window.destroy()

            process = subprocess.Popen([sys.executable, 'game.py', f'{number}'])

            def check_process():
                if process.poll() is None:
                    root.after(500, check_process)
                else:
                    root.deiconify()

            window.after(500, check_process)

        return func

    btn_1 = ttk.Button(window, text='1', command=start_level(1), style='W.TButton')
    btn_1.grid(column=0, row=0)

    btn_2 = ttk.Button(window, text='2', command=start_level(2), style='W.TButton')
    btn_2.grid(column=1, row=0)

    btn_3 = ttk.Button(window, text='3', command=start_level(3), style='W.TButton')
    btn_3.grid(column=2, row=0)

    btn_4 = ttk.Button(window, text='4', command=start_level(4), style='W.TButton')
    btn_4.grid(column=3, row=0)

    btn_5 = ttk.Button(window, text='5', command=start_level(5), style='W.TButton')
    btn_5.grid(column=4, row=0)

    btn_6 = ttk.Button(window, text='6', command=start_level(6), style='W.TButton')
    btn_6.grid(column=0, row=1)

    btn_7 = ttk.Button(window, text='7', command=start_level(7), style='W.TButton')
    btn_7.grid(column=1, row=1)

    btn_8 = ttk.Button(window, text='8', command=start_level(8), style='W.TButton')
    btn_8.grid(column=2, row=1)

    btn_9 = ttk.Button(window, text='9', command=start_level(9), style='W.TButton')
    btn_9.grid(column=3, row=1)

    btn_10 = ttk.Button(window, text='10', command=start_level(10), style='W.TButton')
    btn_10.grid(column=4, row=1)


def info_function():
    messagebox.showinfo('Info', info_text)


def define_style(window):
    style = ttk.Style(window)
    style.configure('W.TButton', font=('Rockwell', 17, 'bold',), foreground='black', borderwith='5')
    style.map('TButton', foreground=[('active', '!disabled', 'white')], background=[('active', 'black')])


root = Tk()
root.resizable(False, False)
root.title('Menu')
width, height = (root.winfo_screenwidth() - root.winfo_reqwidth()) // 2, \
                (root.winfo_screenheight() - root.winfo_reqheight()) // 2
root.geometry(f'+{width}+{height}')

define_style(root)

start_btn = ttk.Button(root, text='Start the game', command=start_game, style='W.TButton')
start_btn.grid(column=0, row=0)

roles_btn = ttk.Button(root, text='Info', command=info_function, style='W.TButton')
roles_btn.grid(column=0, row=1)

quit_btn = ttk.Button(root, text='Quit', command=root.destroy, style='W.TButton')
quit_btn.grid(column=0, row=2)

root.mainloop()
