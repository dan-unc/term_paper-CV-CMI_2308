from run import cv2,plt

def rgb_histogram(image):
    h_list=[]
    for j, nir in enumerate(['b', 'g', 'r']):
        hist = cv2.calcHist([image], [j], None, [256], [0, 256])
        h_list.append(hist)
        plt.plot(hist,color=nir)

rgb_histogram(cv2.imread('data/output/crop2.png'))
plt.show()
#h_list.reshape(-1)
   
