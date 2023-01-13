import tkinter as tk
import time
import random
from PIL import Image
import math


class pet():
  
    def __init__(self):
        # create a window
        self.window = tk.Tk()

        # finding attributes of image
        self.imageLink = 'graphics/headpat.gif'
        self.image = Image.open(self.imageLink)
        self.frame = self.image.n_frames
        self.width = self.image.width
        self.height = self.image.height

        # placeholder image
        # change: switch frame rates 
        self.walking_right = [tk.PhotoImage(file=self.imageLink, format='gif -index %i' % (i)) for i in range(self.frame)]
        self.frame_index = 0
        self.img = self.walking_right[self.frame_index]

        # timestamp to check whether to advance frame
        self.timestamp = time.time()

        # set focushighlight to black when the window does not have focus
        self.window.config(highlightbackground='black')

        # make window frameless
        self.window.overrideredirect(True)

        # make window draw over all others
        self.window.attributes('-topmost', True)

        # turn black into transparency
        self.window.wm_attributes('-topmost', 'true')

        # create a label as a container for our image
        self.label = tk.Label(self.window, bd=0, bg='black')

        # create a window of size 128x128 pixels, at coordinates 0,0
        self.x = 0
        self.y = 0
        self.window.geometry('140x140+{x}+{y}'.format(x=str(self.x), y=str(self.y)))
        # add the image to our label
        self.label.configure(image=self.img)

        # give window to geometry manager (so it will appear)
        self.label.pack()

        # run self.update() after 0ms when mainloop starts
        self.window.after(0, self.update)
        self.window.mainloop()

    def update(self):
        # move right by one pixel
        self.x += 1

        def move(num):
          if (num < 500):
            return num + 1
          else:
            return num - 1
        # move down by one pixel
        self.y = move(self.y)

        # advance frame if 50ms have passed
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.frame_index = (self.frame_index + 1) % self.frame
            self.img = self.walking_right[self.frame_index]

        # create the window
        self.window.geometry('140x140+{x}+{y}'.format(x=str(self.x), y=str(self.y)))
        # add the image to our label
        self.label.configure(image=self.img)
        # give window to geometry manager (so it will appear)
        self.label.pack()

        # call update after 10ms
        self.window.after(10, self.update)

pet()