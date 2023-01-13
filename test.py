import tkinter as tk
import time
import random
from PIL import Image
import math
import datetime


class pet():
  
    def __init__(self, x, y):
        # create a window
        self.window = tk.Tk()
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.curr_dir_y = "Down"
        self.curr_dir_x = "Right"

        # finding attributes of placeholder image
        self.imageLink = 'graphics/Pvu.gif'
        self.image = Image.open(self.imageLink)
        self.frame = self.image.n_frames
        self.width = self.image.width
        self.height = self.image.height
        

        # placeholder image
        # change: switch frame rates 
        self.walking_right = [tk.PhotoImage(file=self.imageLink, format='gif -index %i' % (i), master=self.window) for i in range(self.frame)]
        self.frame_index = 0
        self.img = self.walking_right[self.frame_index]

        # finding attributes of new image
        self.new_imageLink = 'graphics/Pvu.gif'
        self.new_image = Image.open(self.new_imageLink)
        self.new_frame = self.new_image.n_frames

        # new image
        self.new_img = [tk.PhotoImage(file=self.new_imageLink, format='gif -index %i' % (i), master=self.window) for i in range(self.new_frame)][0]

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
        self.x = x
        self.y = y
        self.window.geometry('{width}x{height}+{x}+{y}'.format(width=str(self.width), height=str(self.height), x=str(self.x), y=str(self.y)))
        # add the image to our label
        self.label.configure(image=self.img)


        #onclick functions
        def on_click_duplicate():
          self.window.attributes('-alpha', 0.0)
          pet(random.randint(0, self.screen_width), random.randint(0, self.screen_height))
          # self.window.after(10000, self.window.attributes("-alpha", 1.0))
          # self.label.configure(image=self.new_img)

        def on_click_disappear():
          self.window.attributes('-alpha', 0.0)
          # self.window.after(10000, self.window.attributes("-alpha", 1.0))
          # self.label.configure(image=self.new_img)

        self.label.bind("<Button-1>", lambda e,:on_click_duplicate())
        self.label.bind("<Double-Button-1>", lambda e,:on_click_disappear())

        # give window to geometry manager (so it will appear)
        self.label.pack()

        #to loop through gif array
        self.gif_arr = [ "graphics/xw.gif", "graphics/DEv.gif", "graphics/idle.gif", \
          "graphics/idle_to_sleep.gif", "graphics/Pvu.gif", "graphics/walking_negative.gif"]
        self.gif_counter = 0

        # run self.update() after 0ms when mainloop starts
        self.window.after(0, self.update)
        self.window.after(10000, self.change_gif)
        self.window.after(1000, self.bring_gif_back)
        self.window.mainloop()

    def update(self):

        def bounce_x(num, dir):
          if (dir == "Right"):
            if (num + 1 >= self.screen_width - self.width):
              dir = "Left"
            return (num + 1, dir)
          else:
            if (num - 1 <= 0):
              dir = "Right"
            return (num - 1, dir)

        new_x, new_dir = bounce_x(self.x, self.curr_dir_x)
        self.curr_dir_x = new_dir
        self.x = new_x

        def bounce_y(num, dir):
          if (dir == "Down"):
            if (num + 1 >= self.screen_height - self.height):
              dir = "Up"
            return (num + 1, dir)
          else:
            if (num - 1 <= 0):
              dir = "Down"
            return (num - 1, dir)
        
        new_y, new_dir = bounce_y(self.y, self.curr_dir_y)
        self.curr_dir_y = new_dir
        self.y = new_y

        # advance frame if 50ms have passed
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.frame_index = (self.frame_index + 1) % self.frame
            self.img = self.walking_right[self.frame_index]

        # create the window
        self.window.geometry('{width}x{height}+{x}+{y}'.format(width=str(self.width), height=str(self.height), x=str(self.x), y=str(self.y)))
        # add the image to our label
        self.label.configure(image=self.img)
        # give window to geometry manager (so it will appear)
        self.label.pack()

        # call update after 20ms
        self.window.after(10, self.update)

    def change_gif(self):
        self.imageLink = self.gif_arr[self.gif_counter]
        self.gif_counter = (self.gif_counter + 1) % (len(self.gif_arr) - 1)
        self.image = Image.open(self.imageLink)
        self.frame = self.image.n_frames
        self.width = self.image.width
        self.height = self.image.height
        self.walking_right = [tk.PhotoImage(file=self.imageLink, format='gif -index %i' % (i), master=self.window) for i in range(self.frame)]
        self.image = self.walking_right[0]
        self.label.configure(image=self.image)
        self.label.pack()
        self.window.after(10000, self.change_gif)

    def bring_gif_back(self):
      self.window.attributes('-alpha', 1.0)
      self.window.after(10000, self.bring_gif_back)

if __name__ == "__main__":
  pet(0, 0)