import os
import subprocess

# It takes in a video file and extracts frames from it at a specified frame rate.
class FFMPEGFrames:
    def __init__(self, output):
        """
        The function __init__() is a special function in Python classes. It is run as soon as an object
        of a class is instantiated. The method __init__() is similar to constructors in C++ and Java
        
        :param output: The output file to write the results to
        """
        self.output = output

    def extract_frames(self, input, fps):
        """
        It takes in a video file, extracts frames from it at a specified frame rate, and saves them in a
        specified directory
        
        :param input: The path to the video file
        :param fps: The number of frames per second you want to extract from the video
        """
        output = input.split('/')[-1].split('.')[0]
        query = "ffmpeg -i " + input + " -vf fps=" + str(fps) + " " + self.output + "/{}_%d.jpg".format(output)
        response = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE).stdout.read()
        s = str(response).encode('utf-8')
