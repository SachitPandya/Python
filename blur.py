import cv2
img_path=r"C:\Users\BAPS\Downloads\image.png"
img = cv2.imread(img_path)
if img is None:
    pass

img=cv2.resize(img,(128,128))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)                           # normalize brightness/contrast
print( cv2.Laplacian(gray, cv2.CV_64F).var())