import os
import cv2 as cv
import shutil
import time

folder_path = os.getcwd()

inputFolder = os.path.join(folder_path,'InputImages')
outputFolder = os.path.join(folder_path,'OutputImages')

try:
    shutil.rmtree(outputFolder)
    os.mkdir(outputFolder)
except:
    os.mkdir(outputFolder)

def rgb_to_grayscale(img_name):

    inputImage = os.path.join(inputFolder,img_name)

    img = cv.imread(inputImage)

    #convert to grayscale and store file
    gray_scale = cv.cvtColor(img,cv.COLOR_RGB2GRAY)

    outputFile = os.path.join(outputFolder,'processed_{}'.format(img_name)) 
    cv.imwrite(outputFile,gray_scale)

#start = time.time()
allImages = os.listdir(inputFolder)

if(len(allImages)<500):
    print('Not enough files in InputImages folder')
    exit(0)

for j in range(100,501,100):
    i = 0 

    start_bundle = time.time()
    for img in allImages:
        rgb_to_grayscale(img)

        if(i==j):
            break
        i+=1

    end_bundle = time.time()

    print(j,' ',end_bundle-start_bundle)

end = time.time()

#print(int(mthreads),' ', float(end - start))