from tkinter import *
from matplotlib.figure import Figure
from heapq import nlargest
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

b = 0
a = {}

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")

        self.pack(fill=BOTH, expand=1)

        Button1 = Button(self, text="Button", command=self.client_from)
        Button2 = Button(self, text="Graph", command=self.show_graph)
        Button1.place(x=300, y=150)
        Button2.place(x=0, y=0)
        self.entry_box = Entry(self)
        self.entry_box.place(x =150, y=100)

    def client_from(self):
        print(self.entry_box.get())

        b = self.entry_box.get()
        b = b.split()
        print(b)

        for i in b:
            if(a.get(i) == None):
                a[i] = 1
            else:
                a[i] += 1

        print(a)
        self.entry_box.delete('0',END)

    def show_graph(self):
        #get의 key값을 넣어주고 오른쪾에는 초기값을 넣어준다.

        five_word = nlargest(5, a, key=a.get)
        t = Toplevel(self)
        counting = 0
        data = []
        ind = []
        for i in five_word:
            counting += 1
            ind.append(i)
            data.append(a.get(i))

        f = Figure(figsize=(5, 4), dpi=100)
        ax = f.add_subplot(111)

            # the x loactions for the groups
        width = .5
        rects1 = ax.bar(ind, data, width)
        canvas = FigureCanvasTkAgg(f, t)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

root = Tk()

root.geometry("400x300")

app = Window(root)

root.mainloop()