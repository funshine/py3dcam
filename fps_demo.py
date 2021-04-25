# import the necessary packages
from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=200,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args())
position = (10,40)
fps_str = "Time: , FPS: "

# grab a pointer to the video stream and initialize the FPS counter
print("[INFO] sampling frames from camera...")
print("[INFO] press Ctrl+C to exit...")
stream = cv2.VideoCapture(0)
try:
	while True:
		fps = FPS().start()
		# loop over some frames
		while fps._numFrames < args["num_frames"]:
			# grab the frame from the stream
			(grabbed, frame) = stream.read()
			# resize it to have a maximum width of 400 pixels
			# frame = imutils.resize(frame, width=400)

			# check to see if the frame should be displayed to our screen
			if args["display"] > 0:
				cv2.putText(frame, fps_str, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 250, 255), 3)
				cv2.imshow("Frame", frame)
				key = cv2.waitKey(1) & 0xFF

			# update the FPS counter
			fps.update()

		# stop the timer and display FPS information
		fps.stop()
		if not args["display"] > 0:
			# print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
			print("[INFO] elasped time: {:.2f}, approx. FPS: {:.2f}".format(fps.elapsed(), fps.fps()))
		fps_str = "Time: {:.2f}, FPS: {:.2f}".format(fps.elapsed(), fps.fps())

except KeyboardInterrupt:
	# do a bit of cleanup
	stream.release()
	cv2.destroyAllWindows()

# do a bit of cleanup
stream.release()
cv2.destroyAllWindows()



# Seems NOT Correct!!

# created a *threaded* video stream, allow the camera sensor to warmup,
# and start the FPS counter
# print("[INFO] sampling THREADED frames from webcam...")
# vs = WebcamVideoStream(src=0).start()
# fps = FPS().start()

# # loop over some frames...this time using the threaded stream
# while fps._numFrames < args["num_frames"]:
# 	# grab the frame from the threaded video stream and resize it
# 	# to have a maximum width of 400 pixels
# 	frame = vs.read()
# 	frame = imutils.resize(frame, width=400)

# 	# check to see if the frame should be displayed to our screen
# 	if args["display"] > 0:
# 		cv2.imshow("Frame", frame)
# 		key = cv2.waitKey(1) & 0xFF

# 	# update the FPS counter
# 	fps.update()

# # stop the timer and display FPS information
# fps.stop()
# print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
# print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# # do a bit of cleanup
# cv2.destroyAllWindows()
# vs.stop()