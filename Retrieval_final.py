import math
import operator
import numpy as np
import matplotlib.pyplot as plt
import cv2
import xlrd

loc = (r"C:\Users\HP\Desktop\CBIR\Project\CBIR-Using-MSD-master\CBIR-Using-MSD-master\test")
loc2 = (r"C:\Users\HP\Desktop\CBIR\Project\CBIR-Using-MSD-master\CBIR-Using-MSD-master\data_final.xls")
query=input("Enter name of image:")
loc1=loc+query+'.jpg'
wb = xlrd.open_workbook(loc2)
csv=72
counter=0
img_name=''
dist=0
threshold=.7
sheet = wb.sheet_by_index(0) 
std= np.zeros(csv)
img=np.zeros(csv)
entry=0
final_images=np.zeros(44)
for j in range(44):
    entry=entry+1
    for i in range(csv):
        sheet.cell_value(entry, i)
        if(query==sheet.cell_value(entry, i)):
            counter=1;
            for i in range(csv):
               std[i]=(sheet.cell_value(entry, i+1))
if(counter==0):
    print("Image not available")
#print(std)
entry=0

for j in range(44):
    entry=entry+1
    for i in range(csv):
               img[i]=(sheet.cell_value(entry, i+1))
               dist=(std[i]-img[i])**2+dist
               
    dist=math.sqrt(dist)
    print(dist)
    if(dist<=threshold):
                s=sheet.cell_value(entry, 0)
                print(s)
                out=cv2.imread(s)
                #cv2.namedWindow('image',out)
                #cv2.resizeWindow('image', 400,400)
                cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
                imS = cv2.resize(out, (960, 540))                    # Resize image
                cv2.imshow("output", imS)
                cv2.waitKey(0)   
    dist=0
