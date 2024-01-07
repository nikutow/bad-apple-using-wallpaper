import time
import os
import ctypes

def play():
    totalFrames = len(os.listdir(f"{os.getcwd()}\\frames"))
    currentFrame = 1

    
    while True:
        if currentFrame != totalFrames:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{os.getcwd()}/frames/frame{currentFrame}.jpg", 0)
            time.sleep(0.2)  #this works the best for me you can change it to whatever you like
            currentFrame += 1
       
        else:
            print("Video played!")
            os.system("pause")

        print(currentFrame)

if __name__ == "__main__":
    play()
