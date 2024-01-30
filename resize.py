import cv2
import os
datasets = ""
yourPath = './training_data/XM-220_NG/'
allFileList = os.listdir(yourPath)
for file in allFileList:
    print(file)
    img = cv2.imread("./training_data/XM-220_NG/"+file)
    resize_img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)
    cv2.imwrite('./training_data/XM-220_NG/'+file, resize_img)
    cv2.waitKey(0)
