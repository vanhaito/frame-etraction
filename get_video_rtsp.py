from threading import Thread
import cv2
import time

class RTSPVideoWriterObject(object):
    def __init__(self, src=0):
        # Create a VideoCapture object
        self.capture = cv2.VideoCapture(src)

        # Default resolutions of the frame are obtained (system dependent)
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4)) 

        # Set up codec and output video settings
        self.codec = cv2.VideoWriter_fourcc('M','J','P','G')
        self.output_video = cv2.VideoWriter('./data/videos/output2.avi', self.codec, 30, (self.frame_width, self.frame_height))

        # Start the thread to read frames from the video stream
        self.pre_time = time.time()
        self.now = 0
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
                self.now = time.time()

    def show_frame(self):
        # Display frames in main program
        if self.status:
            cv2.imshow('frame', self.frame)

        # Press Q on keyboard to stop recording
        key = cv2.waitKey(1)
        length_of_vid = self.now - self.pre_time
        if key == ord('q') or length_of_vid > 2700:
            print("Stop streaming!")
            self.capture.release()
            self.output_video.release()
            cv2.destroyAllWindows()
            exit(1)

    def save_frame(self):
        # Save obtained frame into video output file
        self.output_video.write(self.frame)

if __name__ == '__main__':
    rtsp_stream_link = 'rtsp://admin:hd2018vt@@27.67.55.46:554/profile2/media.smp'
    video_stream_widget = RTSPVideoWriterObject(rtsp_stream_link)
    while True:
        try:
            video_stream_widget.show_frame()
            video_stream_widget.save_frame()
        except AttributeError:
            pass
