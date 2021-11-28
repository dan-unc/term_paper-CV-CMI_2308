#Apply any type of blur
from cv2 import GaussianBlur
#from run import img
def blur(img):
    return GaussianBlur(img,(15,15),0)
    
