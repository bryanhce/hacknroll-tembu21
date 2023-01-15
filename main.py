from multiprocessing import Process
import ray
# ray.init()

# after which, whenever they are away from their computer for too long (tracked by face tracker), answerbox will be prompted 
# regarding one of the questions/ans given by user
# if answers correctly, nothing
# else, call pet() from gif.py. for each wrong answer, another pet() called
from textbox import *
from facetracker import *
from gif import *

# @ray.remote
# def func1():
#   Textbox()

# @ray.remote
# def func2():
#   face_tracker = FaceTracker(start_time=time.time())
#   face_tracker.start()


if __name__=='__main__':
  # when application launch, launch textbok for user to fill in list of things they want to remember
  p1 = Process(target = Textbox)
  p1.start()

  # # face tracker launches
  face_tracker = FaceTracker(start_time=time.time())
  p2 = Process(target = face_tracker.start)
  p2.start()
  # ray.get([func1.remote(), func2.remote()])
    

