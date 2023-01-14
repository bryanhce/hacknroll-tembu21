import tkinter as tk
from tkinter import messagebox
import json

class Textbox:

    def __init__(self):
        self.root = tk.Tk()

        #adjust size of the popup window
        self.root.geometry("350x330")
        self.root.title("tembu21")

        #make window draw over all others
        self.root.attributes('-topmost', True)

        #heading
        self.label = tk.Label(self.root, text="Time to Memorise!", font=('Arial bold', 18), fg="black")
        self.label.pack(padx=10, pady=10)

        #question label
        self.labelQues = tk.Label(self.root, text="Question", font=('Arial', 12), fg="black")
        self.labelQues.place(x=18, y=50)

        #frame for textbox question
        border_colour_ques = tk.Frame(self.root, background="black", borderwidth=1)
        border_colour_ques.pack(padx=20, pady=20)

        #frame for textbox answer
        border_colour_ans = tk.Frame(self.root, background="black", borderwidth=1)
        border_colour_ans.pack(padx=20, pady=20)

        #textbox for question
        self.textbox_ques = tk.Text(border_colour_ques, height=3, font=("Arial", 16), bg="gray")
        self.textbox_ques.bind("<KeyPress>", self.kb_enter_shortcut)
        self.textbox_ques.pack(padx=1, pady=1)

        #answer label
        self.labelAns = tk.Label(self.root, text="Answer", font=('Arial', 12), fg="black")
        self.labelAns.place(x=18, y=153)

        #textbox for answer
        self.textbox_ans = tk.Text(border_colour_ans, height=3, font=("Arial", 16), bg="gray")
        self.textbox_ans.bind("<KeyPress>", self.kb_enter_shortcut)
        self.textbox_ans.pack(padx=1, pady=1)

        #button
        self.button = tk.Button(self.root, text="Save", font=("Arial", 18), command=self.memorise_text)
        self.button.pack(padx=10, pady=5)

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

        #run events
        self.root.mainloop()

    def memorise_text(self):
        #parsing data
        ques = self.textbox_ques.get('1.0', tk.END).replace("\n", "").replace("\s", "")
        if ques == "":
            messagebox.showerror(title="No proper value", message="You did not enter a question.")
            return 

        ans = self.textbox_ans.get('1.0', tk.END).replace("\n", "").replace("\s", "")
        if ans == "":
            messagebox.showerror(title="No proper value", message="You did not enter an answer.")
            return

        #clear the texts in ui
        self.textbox_ans.delete("1.0",tk.END)
        self.textbox_ques.delete("1.0",tk.END)

        #saving to memory
        new_obj = {self.count: [ques, ans]}
        self.count += 1
        self.write_to_memory(new_obj)

    def kb_enter_shortcut(self, event):
        if event.keysym == "Return":
            self.memorise_text()

    def write_to_memory(self, new_obj):
        f = open("database.json", "w")
        self.database_dict.update(new_obj)
        json.dump(self.database_dict, f)
        f.close()

Textbox()