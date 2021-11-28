#Segment image and give bounding box
from run import img,cv2,plt

stack=[]
im1=img.copy()
#img=cv2.GaussianBlur(img,(15,15),0)
from threshhold import threshold
cnts=threshold(img)
if len(cnts)==2:
        cnts=cnts[0]
else:
        cnts=cnts[1]
for cn in cnts:
        x,y,w,h=cv2.boundingRect(cn)
        #stack.append(im1[y-10:y+h+10,x-10:x+w+10])
        cv2.rectangle(im1,(x,y),(x+w,y+h),(36,255,12),2)
im=cv2.resize(im1,(500,500))
plt.imshow(im)
plt.show()