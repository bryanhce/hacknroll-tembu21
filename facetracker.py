import cv2
import numpy as np
import time
from answerbox import *
from gif import *
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

detector_params = cv2.SimpleBlobDetector_Params()
detector_params.filterByArea = True
detector_params.maxArea = 1500
detector = cv2.SimpleBlobDetector_create(detector_params)

class FaceTracker():
  start_time = None
  time_away = None


  def __init__(self, start_time):
    self.time_away = 0
    self.start_time = start_time

  def detect_faces(self, img, classifier):
      gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      coords = classifier.detectMultiScale(gray_frame)
      frame = None
      if len(coords) > 1:
        biggest = (0, 0, 0, 0)
        for i in coords:
            if i[3] > biggest[3]:
                biggest = i
        biggest = np.array([i], np.int32)
      elif len(coords) == 1:
        biggest = coords
      else:
        return None
      for (x, y, w, h) in biggest:
          frame = img[y:y + h, x:x + w]
      return frame

  # def detect_eyes(img, classifier):
  #     gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  #     eyes = classifier.detectMultiScale(gray_frame, 1.3, 5) # detect eyes
  #     width = np.size(img, 1) # get face frame width
  #     height = np.size(img, 0) # get face frame height
  #     left_eye = None
  #     right_eye = None
  #     for (x, y, w, h) in eyes:
  #         if y > height / 2:
  #             pass
  #         eyecenter = x + w / 2  # get the eye center
  #         if eyecenter < width * 0.5:
  #             left_eye = img[y:y + h, x:x + w]
  #         else:
  #             right_eye = img[y:y + h, x:x + w]
  #     return left_eye, right_eye

  def blob_process(self, img, detector):
      gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      _, img = cv2.threshold(gray_frame, 90, 255, cv2.THRESH_BINARY)
      img = cv2.erode(img, None, iterations=2) #1
      img = cv2.dilate(img, None, iterations=4) #2
      img = cv2.medianBlur(img, 5) #3
      keypoints = detector.detect(img)
      return keypoints

  def cut_eyebrows(self, img):
      height, width = img.shape[:2]
      eyebrow_h = int(height / 4)
      img = img[eyebrow_h:height, 0:width]  # cut eyebrows out (15 px)
      return img

  # if face_frame is not None:
  #     eyes = detect_eyes(face_frame, eye_cascade)
  #     for eye in eyes:
  #         if eye is not None:
  #             eye = cut_eyebrows(eye)
  #             keypoints = blob_process(eye, detector)
  #             eye = cv2.drawKeypoints(eye, keypoints, eye, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

  def start(self):
      cap = cv2.VideoCapture(0)
      while True:
          _, frame = cap.read()
          face_frame = self.detect_faces(frame, face_cascade)
          if (face_frame) is not None:
            self.time_away = 0
            self.start_time = time.time()
          else:
            self.time_away = time.time() - self.start_time
            if (self.time_away > 5):
              print("here")
              Answerbox()
            
          if cv2.waitKey(1) & 0xFF == ord('q'):
              break
      cap.release()
      cv2.destroyAllWindows()