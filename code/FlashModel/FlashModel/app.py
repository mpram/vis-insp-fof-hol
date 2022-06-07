# import the necessary packages
from flashdetector.detect import DetectObj
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import imutils
import time
import cv2

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
outputFrame = None
lock = threading.Lock()

# initialize a flask object
app = Flask(__name__)

#vs = VideoStream(usePiCamera=1).start()
vs = VideoStream(src=0).start()
time.sleep(2.0)

@app.route("/")
def index():
	# return the rendered template
	return render_template("index.html")

def detect_motion(min_conf_threshold):
	# grab global references to the video stream, output frame, and
	# lock variables
	global vs, outputFrame, lock

	# initialize the motion detector and the total number of frames
	# read thus far

	md = DetectObj.DetectCount()

	# loop over frames from the video stream
	while True:
		# read the next frame from the video stream, resize it,
		# convert the frame to grayscale, and blur it
		frame = vs.read()

		motion = md.get_frame(frame,min_conf_threshold)

		# acquire the lock, set the output frame, and release the
		# lock
		with lock:
			outputFrame = motion.copy()


def generate():
	# grab global references to the output frame and lock variables
	global outputFrame, lock

	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop
			if outputFrame is None:
				continue

			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame)

			# ensure the frame was successfully encoded
			if not flag:
				continue

		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")




# check to see if this is the main thread of execution
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--threshold', help='Minimum confidence threshold for displaying detected objects',
	                    default=0.47)
	args = parser.parse_args()
	min_conf_threshold = float(args.threshold)

	# start a thread that will perform motion detection
	t = threading.Thread(target=detect_motion, args=(
		min_conf_threshold,))
	t.daemon = True
	t.start()

	# start the flask app
	app.run(host='0.0.0.0', port=8000, debug=True,
		threaded=True, use_reloader=False)

# release the video stream pointer
vs.stop()