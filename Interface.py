import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("900x600")
root.title('Convertor and Plot')
# root.iconbitmap()

# # # select file frame # # #
sf_frame = tk.Frame(root, bg='#80b3ff', bd=5)
sf_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.06, anchor="n")

label1 = tk.Label(sf_frame, text="Selected File:", font=('Courier', 12))
label1.place(relx=0, relwidth=0.15, relheight=1)

filename_label = tk.Label(
    sf_frame, text="", anchor='w', justify="left", font=('Courier New', 15))
filename_label.place(relx=0.16, relwidth=0.45, relheight=1)


def choose_file():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select A File", filetypes=(('Text files', '*.txt'),))

    filename_label.configure(text=filename)


choose_button = tk.Button(sf_frame, text="Choose TXT File",
                          font=('Courier', 12), command=choose_file)
choose_button.place(relx=0.65, relwidth=0.15, relheight=1)


insert_button = tk.Button(sf_frame, text="Insert File",
                          font=('Courier', 12))
insert_button.place(relx=0.85, relwidth=0.15, relheight=1)

# # # tables frame # # #

# # # plot frame # # #

root.mainloop()
