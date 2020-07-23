from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def mainFunction():
    videoFiles = ['mp4','avi','flv']
    filesInDir = os.listdir()
    OnlyFile = [x for x in filesInDir if os.path.isfile(x)]
    VideoFilesFromDir = [x for x in OnlyFile if x.split('.')[1] in videoFiles]
    xmap = {}
    print("Number of video present are ",str(len(VideoFilesFromDir)))
    answer = int(input("\n Press \n 1 : Add All \n 2 : Select files : "))
    if answer==2:
        for i in range(len(VideoFilesFromDir)):
            xmap[i] = VideoFilesFromDir[i]
            print(str(i),"--->",VideoFilesFromDir[i])
        print("Enter the values sperated by , like 1,2,3.....")
        answerlist = [int(x) for x in input("Enter here :: ").split(',')]
        sendingList = [VideoFilesFromDir[x] for x in answerlist]
        print(sendingList)
        rendeRingFiles(sendingList)
    elif answer ==1:
        rendeRingFiles(VideoFilesFromDir)


def rendeRingFiles(listt:list):
    print("Enter the Resolution of video \n 1:480p \n 2:720p \n 3:1080p \n 4:Custom Resolution")
    resolution = int(input("Enter here: "))
    a=0
    b=0
    if(resolution == 1):
        a=720
        b=480
    elif resolution ==2:
        a=1280
        b=720
    elif resolution ==3:
        a=1920
        b=1080
    elif resolution ==4:
        a=int(input("Enter Weidth"))
        b = int(input("Enter height"))
    videoClipslist =[vidoClipMaker(x,a,b) for x in listt]
    finalVideoName = input("Enter your video name ::::")
    print("Video will be in .mp4")
    dirToSave = input("Enter directory to save file :: ")
    concatenate_videoclips(videoClipslist).write_videofile(dirToSave+"\\"+finalVideoName+".mp4")


def vidoClipMaker(videoClipName,a,b):
    return VideoFileClip(videoClipName).resize((a,b))



if __name__=="__main__":

    while(True):
        directory = input("Enter the directory in which videos are presenrt \n")
        try:
            os.chdir(directory)
            #mainFunction()
            break
        except:
            print("Directory Not valid please try again")

    mainFunction()