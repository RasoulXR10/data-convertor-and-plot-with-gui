from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename
from PIL import Image, ImageTk
import matplotlib.pyplot
import matplotlib
matplotlib.use('TkAgg')

root = tk.Tk()
root.geometry("900x600")
root.title('Convertor and Plot')
# root.iconbitmap()

# # # All Frames & Labels # # #


sf_frame = tk.Frame(root, bg='#80b3ff', bd=5)
sf_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.06, anchor="n")

label1 = tk.Label(sf_frame, text="Selected File:", font=('Courier', 12))
label1.place(relx=0, relwidth=0.15, relheight=1)

filename_label = tk.Label(
    sf_frame, text="", anchor='w', justify="left", font=('Courier New', 15))
filename_label.place(relx=0.16, relwidth=0.45, relheight=1)

label2 = tk.Label(root, text="Selected Data",
                  font=('Courier', 12), bg='#f2f2f2')
label2.place(relx=0.055, rely=0.18, relwidth=0.17, relheight=0.05)

label3 = tk.Label(root, text="Converted Data",
                  font=('Courier', 12), bg='#f2f2f2')
label3.place(relx=0.405, rely=0.18, relwidth=0.17, relheight=0.05)

# table frames #
table1_frame = tk.Frame(root, bg='#80b3ff', bd=5)
table1_frame.place(relx=0.05, rely=0.25, relwidth=0.18,
                   relheight=0.6, anchor="nw")

table2_frame = tk.Frame(root, bg='#80b3ff', bd=5)
table2_frame.place(relx=0.4, rely=0.25, relwidth=0.18,
                   relheight=0.6, anchor="nw")


# plot frames #

plot1_frame = tk.Frame(root, bg='#80b3ff', bd=5)
plot1_frame.place(relx=0.6, rely=0.15, relwidth=0.35,
                  relheight=0.38, anchor='nw')

plot2_frame = tk.Frame(root, bg='#80b3ff', bd=5)
plot2_frame.place(relx=0.6, rely=0.58, relwidth=0.35,
                  relheight=0.38, anchor='nw')


# # # All Functions # # #

class ReadFile:
    def __init__(self):
        pass

    def choose_file(self):
        file = tk.filedialog.askopenfile(mode='r',
                                              initialdir="/", title="Select A File", filetypes=(('Text files', '*.txt'),))
        self.content = file.readlines()
        return file

    def create_result(self, file):
        self.res = []
        mylist = [line.rstrip('\n') for line in self.content]
        for element in mylist[1:]:
            self.res.append(element)
        self.result = [tuple(map(int, sub.split())) for sub in self.res]
        return (self.result)

    # convert function #

    def convert_eq(self, result):

        x = [i[0] for i in result]
        y = [i[1] for i in result]
        new_x = [j + 10 for j in x]
        new_y = [k + 20 for k in y]
        convert_result = list(zip(new_x, new_y))
        return convert_result


read_file = ReadFile()

result = []


def selected_file():
    global result
    file = read_file.choose_file()
    filename_label.configure(text=file.name)
    res = read_file.create_result(file)
    result = res


def insert_data():
    Table(table1_frame, result)


def convert_data():
    Table(table2_frame, read_file.convert_eq(result))


# plot #


def plot_selected_data():
    Plot(plot1_frame, result)


def plot_converted_data():
    Plot(plot2_frame, read_file.convert_eq(result))


# # # All Buttons # # #
choose_button = tk.Button(sf_frame, text="Choose TXT File",
                          font=('Courier', 12), command=selected_file)
choose_button.place(relx=0.65, relwidth=0.15, relheight=1)


insert_button = tk.Button(sf_frame, text="Insert File",
                          font=('Courier', 12), command=insert_data)
insert_button.place(relx=0.85, relwidth=0.15, relheight=1)


convert_table_button = tk.Button(root, text="Convert With Eq",
                                 font=('Courier', 12), command=convert_data)
convert_table_button.place(relx=0.24, rely=0.4, relwidth=0.15, relheight=0.05)


plot_selected_data_button = tk.Button(
    root, text="Plot Selected Data", font=('Courier', 12), command=plot_selected_data)
plot_selected_data_button.place(
    relx=0.054, rely=0.87, relwidth=0.17, relheight=0.05)

plot_converted_data_button = tk.Button(
    root, text="Plot Converted Data", font=('Courier', 12), command=plot_converted_data)
plot_converted_data_button.place(
    relx=0.404, rely=0.87, relwidth=0.17, relheight=0.05)

# tabels #


class Table:

    def __init__(self, table_frames, result):
        # code for creating table
        total_rows = len(result)
        total_columns = len(result[0])
        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(table_frames, width=7, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, result[i][j])

# plot #


class Plot:

    def __init__(self, plot_frames, data):

        self.x = []
        self.y = []
        self.plot_frames = plot_frames
        self.plot_data = data

        for element in self.plot_data:
            self.x.append(element[0])
        for element in self.plot_data:
            self.y.append(element[1])

        self.fig = Figure(figsize=(6, 6))
        self.a = self.fig.add_subplot(111)
        self.a.plot(self.x, self.y)

        canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frames)
        canvas.get_tk_widget().pack()
        canvas.draw()


root.mainloop()
