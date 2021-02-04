import tkinter
from tkinter import ttk

main_win = tkinter.Tk()
main_win.title("USBポートをロックする")
main_win.geometry("200x40")


main_frm = ttk.Frame(main_win)
main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=1, pady=5)

app_btn1 = ttk.Button(main_frm, text="USBlock")
app_btn2 = ttk.Button(main_frm, text="USBlock解除")

app_btn1.grid(column=0, row=2)
app_btn2.grid(column=1, row=2)

main_win.columnconfigure(0, weight=1)
main_win.rowconfigure(0, weight=1)
main_frm.columnconfigure(1, weight=1)

def app():


main_win.mainloop()