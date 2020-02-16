from imutils.video import VideoStream
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import os
import numpy as np
import smtplib
import argparse
import datetime
import imutils
import time
import cv2
import pyautogui

path = os.getcwd()
relative_path = path + '\screenshot.png'

email_user = 'noreplygameseeai@gmail.com'
email_send = input("Enter the email you want to receive the alert on: ")

while "@" not in email_send and '.com' not in email_send:
    print("Invalid input! Please re-enter correct email address")
    email_send = input("Enter the email you want to receive the alert on: ")

subject = 'Security Alert'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = """Hello, 
We recently detected a suspicious person/movement near your registered device. If you are not near your device, please make sure you device is safe secure.
Confidential Transmissions:
This message is intended only for the use of the individual to whom it is addressed, and may contain information that is privileged and confidential.  If the reader of 
this message is not the intended recipient, you are hereby notified that any dissemination, distribution, or copying of this communication is strictly prohibited. If you have received 
this communication in error, please notify the sender immediately by reply email and confirm you have permanently delete the original transmission, including attachments, without making a copy."""
msg.attach(MIMEText(body, 'plain'))

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=720, help="minimum area size")
args = vars(ap.parse_args())

# if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
	vs = VideoStream(src = 0).start()
	time.sleep(2.0)
	
# otherwise, we are reading from a video file
else:
	vs = cv2.VideoCapture(args["video"])

# initialize the first frame in the video stream
firstFrame = None

# loop over the frames of the video
while True:
	# grab the current frame and detect
	frame = vs.read()
	frame = frame if args.get("video", None) is None else frame[1]
	text = "NULL Activity - Safe"

	# if the frame could not be grabbed, then we have reached the end of the video
	if frame is None:
		break

	# resize the frame, convert it to grayscale, and blur it
	frame = imutils.resize(frame, width=720)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue

	# compute the absolute difference between the current frame and first frame
	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 140, 255, cv2.THRESH_BINARY)[1]

	# dilate the thresholded image to fill in holes, then find contours on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	# loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < args["min_area"]:
			continue

		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Detected - Unsafe"

		if text == "Detected - Unsafe":
			myScreenshot = pyautogui.screenshot()
			
			myScreenshot.save(relative_path)

			filename = 'screenshot.png'

			attachment = open(filename, 'rb') # Reading by bits

			part = MIMEBase('application', 'octet-stream') # Allowing you to upload the attachemnt and then sending and then closing
			part.set_payload((attachment).read())
			encoders.encode_base64(part)
			part.add_header('Content-Disposition', 'attachment; filename= '+filename)

			msg.attach(part)

			text = msg.as_string()
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.starttls()
			server.login(email_user, "fufhd&fudfhd*")

			server.sendmail(email_user, email_send, text)
			server.quit()			
			
	# Text
	cv2.putText(frame, "Gamsee Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	# User control
	cv2.imshow("GamseeAI", frame)
	ctrlAbort = cv2.waitKey(1) & 0xFF
	if ctrlAbort == ord("a"):
		break


# cleanup the camera and close any open windows
vs.stop() if args.get("video", None) is None else vs.release()
cv2.destroyAllWindows()