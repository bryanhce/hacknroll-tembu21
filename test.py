import tkinter as tk
import time
import random
from PIL import Image
import math
import datetime


class pet():
  
    def __init__(self):
        # create a window
        self.window = tk.Tk()

        # finding attributes of placeholder image
        self.imageLink = 'graphics/cat_idle.gif'
        self.image = Image.open(self.imageLink)
        self.frame = self.image.n_frames
        self.width = self.image.width
        self.height = self.image.height

        # placeholder image
        # change: switch frame rates 
        self.walking_right = [tk.PhotoImage(file=self.imageLink, format='gif -index %i' % (i)) for i in range(self.frame)]
        self.frame_index = 0
        self.img = self.walking_right[self.frame_index]

        # finding attributes of new image
        self.new_imageLink = 'graphics/cat_headpat.gif'
        self.new_image = Image.open(self.new_imageLink)
        self.new_frame = self.new_image.n_frames

        # new image
        self.new_img = [tk.PhotoImage(file=self.new_imageLink, format='gif -index %i' % (i)) for i in range(self.new_frame)][0]

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


        #onclick functions
        def on_click():
          self.label.configure(image=self.new_img)

        self.label.bind("<Button-1>", lambda e,:on_click())

        # give window to geometry manager (so it will appear)
        self.label.pack()

        #to loop through gif array
        self.gif_arr = ["graphics/test.gif", "graphics/sleep.gif", "graphics/idle_to_sleep.gif", "graphics/cat_idle.gif"]
        self.gif_counter = 0

        # run self.update() after 0ms when mainloop starts
        self.window.after(0, self.update)
        self.window.after(1000, self.change_gif)
        self.window.mainloop()

    def update(self):
        # move right by one pixel
        self.x += 1

        # def move(num):
        #   if (self.x < 600):
        #     return num + 1
        #   else:
        #     return num - 1
        # # move down by one pixel
        self.y += 1

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
        self.window.after(50, self.update)

    def change_gif(self):
        self.imageLink = self.gif_arr[self.gif_counter]
        self.gif_counter = (self.gif_counter + 1) % (len(self.gif_arr) - 1)
        print(len(self.gif_arr))
        self.image = Image.open(self.imageLink)
        self.frame = self.image.n_frames
        self.walking_right = [tk.PhotoImage(file=self.imageLink, format='gif -index %i' % (i)) for i in range(self.frame)]
        self.image = self.walking_right[0]
        self.label.configure(image=self.image)
        self.label.pack()
        self.window.after(1000, self.change_gif)

pet()