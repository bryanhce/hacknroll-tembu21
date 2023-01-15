import tkinter as tk
from tkinter import messagebox
import json
import random
import threading

from gif import *

class Answerbox:

    def __init__(self):
        self.r = tk.Tk()

        self.r.attributes('-alpha', 0.0)

        self.root = tk.Toplevel(self.r)

        #adjust size of the popup window
        self.root.geometry("350x330")
        self.root.title("tembu21")

        #make window draw over all others
        self.root.attributes('-topmost', True)

        #heading
        self.label = tk.Label(self.root, text="Time to Answer!", font=('Arial bold', 18), fg="black")
        self.label.pack(padx=10, pady=10)

        #database
        #create database if it doesn't exist
        f = open("database.json", "a+")
        f.close()
        
        self.database_dict = {}
        self.count = 0

        #if database exist, take prev data
        try:
            with open("database.json", "r", encoding="utf-8") as f:
                self.database_dict = json.load(f)
                self.count = len(self.database_dict)
                f.close()
        except json.decoder.JSONDecodeError:
            pass

        #question 
        self.number = random.randint(0, len(self.database_dict) - 1)
        self.questionText = self.database_dict.get(str(self.number), ["error, issue with database, restart application"])[0]
        self.answerText = self.database_dict.get(str(self.number), ["", "err"])[1]
        self.labelQues = tk.Label(self.root, text=self.questionText, \
            font=('Arial', 15), fg="black", wraplength=350)
        self.labelQues.place(x=18, y=50)

        #frame for textbox ans
        border_colour = tk.Frame(self.root, background="black", borderwidth=1)
        border_colour.pack(padx=20, pady=70)

        #textbox for ans
        self.textbox = tk.Text(border_colour, height=3, font=("Arial", 16), bg="gray")
        self.textbox.bind("<KeyPress>", self.kb_enter_shortcut)
        self.textbox.pack(padx=1, pady=1)

        #button
        self.button = tk.Button(self.root, text="Check", font=("Arial", 18), command=self.check_ans)
        self.button.pack(padx=10, pady=5)

        #run events
        self.root.mainloop()
        self.r.after(10000, self.r.destroy())

    def check_ans(self):
        answer = self.textbox.get('1.0', tk.END).replace("\n", "").lower().strip()
        if answer == "":
            messagebox.showerror(title="No proper value", message="You did not enter an answer.")
            # return False

        if answer == self.answerText:
            self.root.destroy()
            # return True
        else:
            messagebox.showerror(title="Wrong answer", message="Wrong answer, try again!")
            # return False
            pet(0, 0)



    def kb_enter_shortcut(self, event):
        if event.keysym == "Return":
            self.check_ans()

#for testing
# Answerbox()