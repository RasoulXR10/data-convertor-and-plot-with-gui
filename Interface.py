from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename
from PIL import Image, ImageTk
import matplotlib.pyplot
import matplotlib
matplotlib.use('TkAgg')


# root.iconbitmap()

# # # All Frames & Labels # # #


class App:

    result = []
    root = None
    filename_label = None
    table1_frame = None
    table2_frame = None
    plot1_frame = None
    plot2_frame = None

    def __init__(self):
        self.read_file = ReadFile()
        self.root = tk.Tk()
        self.root.geometry("900x600")
        self.root.title('Convertor and Plot')
        self.sf_frame = tk.Frame(self.root, bg='#80b3ff', bd=5)
        self.sf_frame.place(relx=0.5, rely=0.05, relwidth=0.9,
                            relheight=0.06, anchor="n")

        self.label1 = tk.Label(self.sf_frame, text="Selected File:",
                               font=('Courier', 12))
        self.label1.place(relx=0, relwidth=0.15, relheight=1)

        self.filename_label = tk.Label(
            self.sf_frame, text="", anchor='w', justify="left", font=('Courier New', 15))
        self.filename_label.place(relx=0.16, relwidth=0.45, relheight=1)

        self.label2 = tk.Label(self.root, text="Selected Data",
                               font=('Courier', 12), bg='#f2f2f2')
        self.label2.place(relx=0.055, rely=0.18, relwidth=0.17, relheight=0.05)

        self.label3 = tk.Label(self.root, text="Converted Data",
                               font=('Courier', 12), bg='#f2f2f2')
        self.label3.place(relx=0.405, rely=0.18, relwidth=0.17, relheight=0.05)

        # table frames #
        self.table1_frame = tk.Frame(self.root, bg='#80b3ff', bd=5)
        self.table1_frame.place(relx=0.05, rely=0.25, relwidth=0.18,
                                relheight=0.6, anchor="nw")

        self.table2_frame = tk.Frame(self.root, bg='#80b3ff', bd=5)
        self.table2_frame.place(relx=0.4, rely=0.25, relwidth=0.18,
                                relheight=0.6, anchor="nw")

        # plot frames #
        self.plot1_frame = tk.Frame(self.root, bg='#80b3ff', bd=5)
        self.plot1_frame.place(relx=0.6, rely=0.15, relwidth=0.35,
                               relheight=0.38, anchor='nw')

        self.plot2_frame = tk.Frame(self.root, bg='#80b3ff', bd=5)
        self.plot2_frame.place(relx=0.6, rely=0.58, relwidth=0.35,
                               relheight=0.38, anchor='nw')

        # # # All Buttons # # #
        self.choose_button = tk.Button(self.sf_frame, text="Choose TXT File",
                                       font=('Courier', 12), command=self.selected_file)
        self.choose_button.place(relx=0.65, relwidth=0.15, relheight=1)

        self.insert_button = tk.Button(self.sf_frame, text="Insert File",
                                       font=('Courier', 12), command=self.insert_data)
        self.insert_button.place(relx=0.85, relwidth=0.15, relheight=1)

        self.convert_table_button = tk.Button(self.root, text="Convert With Eq",
                                              font=('Courier', 12), command=self.convert_data)
        self.convert_table_button.place(
            relx=0.24, rely=0.4, relwidth=0.15, relheight=0.05)

        self.plot_selected_data_button = tk.Button(
            self.root, text="Plot Selected Data", font=('Courier', 12), command=self.plot_selected_data)
        self.plot_selected_data_button.place(
            relx=0.054, rely=0.87, relwidth=0.17, relheight=0.05)

        self.plot_converted_data_button = tk.Button(
            self.root, text="Plot Converted Data", font=('Courier', 12), command=self.plot_converted_data)
        self.plot_converted_data_button.place(
            relx=0.404, rely=0.87, relwidth=0.17, relheight=0.05)

        self.root.mainloop()

    # # # All Functions # # #

    def selected_file(self):
        res = self.read_file.create_result(self)
        file = self.read_file.choose_file()
        self.filename_label.configure(text=file.name)
        self.result = self.read_file.create_result(file)

    def insert_data(self):
        Table(self.table1_frame, self.result)

    def convert_data(self):
        Table(self.table2_frame, self.read_file.convert_eq(self.result))

    # plot #

    def plot_selected_data(self):
        Plot(self.plot1_frame, self.result)

    def plot_converted_data(self):
        Plot(self.plot2_frame, self.read_file.convert_eq(self.result))

    # # # All Classes # # #

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


class ReadFile:

    content = str()

    def __init__(self):
        pass

    def choose_file(self):
        self.file = tk.filedialog.askopenfile(mode='r',
                                              initialdir="/", title="Select A File", filetypes=(('Text files', '*.txt'),))
        self.content = self.file.readlines()
        return self.file

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
