import glob
import os
import json
import sys
import numpy as np

import cv2
from PIL import Image
from pdf2image import convert_from_path



untreatable_formats = [".exr", ".icns", ".msp", "xbm", ".palm", ".xvthumbnails"]



#python image2image.py inputDirectory inputFileExtension outputFileExtension
argvs = sys.argv
#-->  argvs = ["image2image.py", "inputDirectory", "inputFileExtension", "outputFileExtension"]
print("argvs:", argvs)






#load config file
with open('config.json') as f:
    _dict = json.load(f)

input_outputFileFormatOpenCV = _dict["input-outputFileFormatOpenCV"]
input_outputFileFormatPillow = _dict["input-outputFileFormatPillow"]
outputFileFormatPillow = _dict["outputFileFormatPillow"]
print("input_outputFileFormatOpenCV:", input_outputFileFormatOpenCV)
print("input_outputFileFormatPillow:", input_outputFileFormatPillow)

#DB path
db_path = glob.glob(os.path.join(argvs[1] + "/*"))
print("db_path:\n", db_path)
img_paths_for_opencv = []
img_paths_for_pillow = []
for i in range(len(db_path)):
    if db_path[i][-len(argvs[2]):].lower() in input_outputFileFormatOpenCV and db_path[i][-len(argvs[2]):].lower() == argvs[2]:
        img_paths_for_opencv.append(db_path[i])
    elif db_path[i][-len(argvs[2]):].lower() in input_outputFileFormatPillow and db_path[i][-len(argvs[2]):].lower() == argvs[2]:
        img_paths_for_pillow.append(db_path[i])

print("img_paths_for_opencv:", img_paths_for_opencv)
print("img_paths_for_pillow:", img_paths_for_pillow)

pdf_img_paths = [path for path in db_path if ((".pdf" in path.lower()) and (argvs[2] == ".pdf"))]

if img_paths_for_opencv == [] and img_paths_for_pillow == [] and pdf_img_paths == []:
    print("confirm arguments.")
    sys.exit()

print("image list was made.")


if argvs[2] == argvs[3]:
    print("no need to convert.")
    sys.exit()


if not (argvs[3] in input_outputFileFormatOpenCV or argvs[3] in input_outputFileFormatPillow or argvs[3] in outputFileFormatPillow or argvs[3] == ".pdf"):
    print("sorry, we can't convert to the format.")
    sys.exit()

if not (argvs[2] in input_outputFileFormatOpenCV or argvs[2] in input_outputFileFormatPillow or argvs[2] == ".pdf"):
    print("sorry, we can't convert from the format.")
    sys.exit()

if argvs[2] in untreatable_formats or argvs[3] in untreatable_formats:
    print("sorry, we can't deal with that format at this time.")
    sys.exit()

if not os.path.exists("result"):
        os.makedirs("result")
os.chdir("result")



if argvs[2] in input_outputFileFormatOpenCV and argvs[3] in input_outputFileFormatOpenCV:
    for i in range(len(img_paths_for_opencv)):
        image = cv2.imread("../" + img_paths_for_opencv[i])
        cv2.imwrite('{0}{1}'.format(img_paths_for_opencv[i].split("/")[-1][:-len(argvs[2])], argvs[3]), image)
        print("{0}th picture was converted.".format(i + 1))

elif argvs[2] in input_outputFileFormatOpenCV:
    for i in range(len(img_paths_for_opencv)):
        image = cv2.imread("../" + img_paths_for_opencv[i])[:, :, ::-1]
        image = Image.fromarray(image)
        image.save('{0}{1}'.format(img_paths_for_opencv[i].split("/")[-1][:-len(argvs[2])], argvs[3]))
        print("{0}th picture was converted.".format(i + 1))


if argvs[2] in input_outputFileFormatPillow and (argvs[3] in input_outputFileFormatPillow or argvs[3] in outputFileFormatPillow):
    for i in range(len(img_paths_for_pillow)):
        image = Image.open("../" + img_paths_for_pillow[i])
        image.save('{0}{1}'.format(img_paths_for_pillow[i].split("/")[-1][:-len(argvs[2])], argvs[3]))
        print("{0}th picture was converted.".format(i + 1))

elif argvs[2] in input_outputFileFormatPillow:
    for i in range(len(img_paths_for_pillow)):
        image = Image.open("../" + img_paths_for_pillow[i])
        #image = np.asarray(image)[:, :, ::-1]
        image = np.asarray(image)
        cv2.imwrite('{0}{1}'.format(img_paths_for_pillow[i].split("/")[-1][:-len(argvs[2])], argvs[3]), image)
        print("{0}th picture was converted.".format(i + 1))

    


if argvs[2] == ".pdf":
    for i in range(len(pdf_img_paths)):
        image = convert_from_path("../" + pdf_img_paths[i])[0]
        if argvs[3] in input_outputFileFormatPillow or argvs[3] in outputFileFormatPillow:
            image.save('{0}{1}'.format(pdf_img_paths[i].split("/")[-1][:-len(argvs[2])], argvs[3]))
        else:
            image = np.asarray(image)[:, :, ::-1]
            cv2.imwrite('{0}{1}'.format(pdf_img_paths[i].split("/")[-1][:-len(argvs[2])], argvs[3]), image)
        
        print("{0}th picture was converted.".format(i + 1))



