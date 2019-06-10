from tkinter import *
from tkinter import ttk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()
        self.text = None

    def init_window(self):

        self.text = self._text_panel(self.master)
        self._load_file_panel(self.master, self.text)
        self._search_panel(self.master)

    def _load_file_panel(self, parent, text):

        f = ttk.Frame(parent)
        f.pack(side=TOP)
        ttk.Label(text='File Name : ', width=13, anchor=W).pack(side = LEFT)
        fname = StringVar()
        e = ttk.Entry(width=40, textvariable=fname)
        e.pack(side=LEFT)
        btn = ttk.Button(text="Load file", command= lambda fn=fname:self._load_file(fn.get(),text))
        btn.pack(side=LEFT, padx=10, pady=5)

    def _load_file(self, fname, text):

        self.text = text

        self.text.delete('0.0', END)
        try:
            self.text.insert(END, open(fname).read())
        except IOError:
            self.bell()
            self.text.insert(END,'File '+ fname + 'not found.')
        return 'break'

    def _text_panel(self, parent):
        txtFrame = ttk.Frame(parent)
        txtFrame.pack(side=TOP, fill=BOTH, expand=Y)

        self.text = Text(txtFrame, height=20, setgrid=True, wrap=WORD,
                         undo=True, pady=2, padx=3)

        xscroll = ttk.Scrollbar(txtFrame, command=self.text.xview,
                                orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(txtFrame, command=self.text.yview,
                                orient=VERTICAL)

        self.text.configure(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        self.text.tag_configure('search', background='yellow')

        self.text.grid(row=0, column=0, sticky=NSEW)

        yscroll.grid(row=0, column=1, sticky=NSEW)
        txtFrame.rowconfigure(0, weight=1)
        txtFrame.columnconfigure(0, weight=1)

        return self.text

    def _search_panel(self, parent):
        f = ttk.Frame(parent)
        f.pack(side=TOP)

        ttk.Label(text="Searth string: ",width=13, anchor=W).pack(in_=f, side=LEFT)

        srchStr = StringVar()
        e = ttk.Entry(width=40, textvariable=srchStr)
        e.pack(in_=f, side=LEFT)

        btn = ttk.Button(text='Highhlight', command=lambda ss=srchStr: self._search_text(ss.get()))
        btn.pack(in_=f, side=LEFT, padx=10, pady=5)

        e.bind('<Return>', lambda evt, btn=btn: btn.invoke())

    def _search_text(self, srchString):
        self.text.tag_remove('searth',0.0, END)

        if not srchString:
            return 'break'

        cur = 1.0
        length = IntVar()
        while True:
            cur = self.text.search(srchString, cur, END, count=length)
            if not cur:
                return 'break'

            matchEnd = '{0}+{1}c'.format(cur, length.get())
            print(matchEnd)

            self.text.tag_add('search', cur, matchEnd)
            cur = self.text.index(matchEnd)

root = Tk()
root.geometry("1000x1000")
app = Window(root)
root.mainloop()