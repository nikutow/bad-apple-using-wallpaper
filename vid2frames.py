import os
import cv2

def createFrames(video):
    totalFrames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))


    success, image = video.read()
    for i in range(total_frames):
        cv2.imwrite(f"frames/frame{i+1}.jpg", image)
        success, image = video.read()
        print(f"\r{int((i+1))} frames complete", end="\r")

if __name__ == "__main__":
    createFrames()
