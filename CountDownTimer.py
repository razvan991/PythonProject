import tkinter as tk
import datetime
import threading
from tkinter import messagebox
from playsound import playsound

class Countdown(tk.Frame):
    ##initializare
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left=0
        self._timer_on=False
    ##afisarea butoanelor+label+entry
    def show_widgets(self):
        self.label.pack()
        self.entry.pack()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
    ##creearea butoanelor , label si entry
    def create_widgets(self):
        self.label=tk.Label(self,text="Enter time in seconds...")
        self.entry=tk.Entry(self,justify="center")
        self.reset=tk.Button(self,text="Reset timer",command=self.reset_button)
        self.stop=tk.Button(self,text="Stop timer",command=self.stop_button)
        self.start=tk.Button(self,text="Start timer",command=self.start_button)
    ##functia pentru timer
    def countdown(self):
        self.label["text"]=self.convert_seconds_left_to_time()
        if self.seconds_left!=0:
            self.seconds_left-=1
            self._timer_on=self.after(1000,self.countdown)
        else:
            self._timer_on=False
            threading.Thread(target=playsound, args=('alarm.mp3',)).start()
            messagebox.showinfo("Time countdown", "Time's up")
    ##Butonul de reset
    def reset_button(self):
        self.seconds_left=0
        self.stop_timer()
        self._timer_on=False
        self.label["text"]="Enter time in seconds..."
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
    ##Butonul de stop
    def stop_button(self):
        self.seconds_left=int(self.entry.get())
        self.stop_timer()
    ##Butonul de start
    def start_button(self):
        self.seconds_left=int(self.entry.get())
        self.stop_timer()
        self.countdown()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()
    ##Stop timer
    def stop_timer(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on=False
    ##convertire secunde
    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)
if __name__=="__main__":
    root=tk.Tk()
    root.geometry("400x300")
    root.resizable(False,False)
    countdown=Countdown(root)
    countdown.pack()
    root.mainloop()