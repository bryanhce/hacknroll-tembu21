from multiprocessing import Process

# after which, whenever they are away from their computer for too long (tracked by face tracker), answerbox will be prompted 
# regarding one of the questions/ans given by user
# if answers correctly, nothing
# else, call pet() from gif.py. for each wrong answer, another pet() called
from textbox import *
from facetracker import *
from gif import *


if __name__=='__main__':
  # when application launch, launch textbok for user to fill in list of things they want to remember
  p1 = Process(target = Textbox)
  p1.start()

  # # face tracker launches
  face_tracker = FaceTracker(start_time=time.time())
  p2 = Process(target = face_tracker.start)
  p2.start()
    

