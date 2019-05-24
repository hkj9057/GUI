from tkinter import *
import time;

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

        self.start = 0.0
        self.elapsedtime = 0.0
        self.runing = 0.0
        self.timestr = StringVar()

    def init_window(self):
        self.master.title("GUI")

        self.pack(fill=BOTH, expand=1)

        timeButton = Button(self, text="Time", command = self.client_time)

        watchButton = Button(self, text="Stop Watch", command = self.client_watch)

        timeButton.place(x=0, y=0)
        watchButton.place(x=200, y=0)

    def client_time(self):

        clock = Label(root, font=('times', 50, 'bold'), bg='blue')
        clock.place(x=10,y=100)

        time_string = time.strftime('%H:%M:%S')

        clock.config(text=time_string)
        clock.after(200, self.client_time)

    def client_watch(self):
        watch = Label(root,textvariable=self.timestr)

        startButton = Button(self, text="Start", command=self.watch_start).pack(side=LEFT)
        stopButton = Button(self, text="Stop", command=self.watch_stop).pack(side=LEFT)
        resetButton = Button(self, text="Reset", command=self.watch_reset).pack(side=LEFT)
        quitButton = Button(self, text="quit", command=self.watch_quit).pack(side=LEFT)

        self.watch_time(self.elapsedtime)
        watch.place(x=10, y=100)


    def watch_start(self):
        if not self.runing:
            self.start = time.time() - self.elapsedtime
            self.watch_update()
            self.runing = 1

    def watch_time(self, time):
        min = int(time/60)
        sec = int(time - min*60)
        hsec = int((time - min*60 - sec)*100)
        self.timestr.set('%02d:%02d:%02d'%(min, sec, hsec))

    def watch_stop(self):
        if self.runing:
            self.after_cancel(self.timer)
            self.elapsedtime = time.time() - self.start
            self.watch_time(self.elapsedtime)
            self.runing = 0

    def watch_reset(self):
        self.start = time.time()
        self.elapsedtime = 0
        self.watch_time(self.elapsedtime)

    def watch_quit(self):
        quit()

    def watch_update(self):
        self.elapsedtime = time.time() - self.start
        self.watch_time(self.elapsedtime)
        self.timer = self.after(20, self.watch_update)

root = Tk()

root.geometry("400x300")

app = Window(root)

root.mainloop()