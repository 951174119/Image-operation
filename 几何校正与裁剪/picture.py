
import cv2
import numpy as np
import cv2 as cv
from skimage.io import imsave
import glob
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif' ] =['simhei']
plt.rcParams['axes.unicode_minus'] =False
import os
def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    global point_list
    a = len(point_list)
    if (a < 3):
        if event == cv2.EVENT_LBUTTONDOWN:
            point_list.append([x, y])
            cv2.circle(img, (x, y), 3, (255, 0, 0), thickness=-1)

            # 添加文字
            cv2.putText(img, str(a + 1), (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (0, 255, 0), thickness=1)
            cv2.imshow("window 2", img)

str1 = 'in/'
str2 = 'out/'
img_list = glob.glob(str1 + '*.png')
img_list = img_list + glob.glob(str1 + '*.jpg')
img_list = img_list + glob.glob(str1 + '*.jpeg')
for i, img_path in enumerate(img_list):
    img0 = cv2.imread(img_path,1)
    img = img0.copy()
    print('%d----' % (i + 1), img_path)
    imgInput = cv.imread(img_path, 1)
    rows, cols, channels = imgInput.shape
    (filepath, tempfilename) = os.path.split(img_path)
    (Myfilename, extension) = os.path.splitext(tempfilename)
    point_list = list()
    cv2.namedWindow("window 2", flags=cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
    cv2.imshow("window 2", img)
    cv2.setMouseCallback("window 2", on_EVENT_LBUTTONDOWN)
    while(1):
        if cv2.waitKey(0):
            break
    cv2.destroyAllWindows()
    p1 = np.float32(point_list)
    p2 = np.float32([[50, 60], [150,60], [100,150]])
    M = cv.getAffineTransform(p1, p2)
    print(M)
    cols2, rows2 = 200,200
    imgOutput = cv.warpAffine(imgInput, M,(cols2, rows2),flags=cv.INTER_CUBIC ,)
    b, g, r = cv2.split(imgOutput)
    imgOutput = cv2.merge([r, g, b])
    plt.imshow(imgOutput)
    plt.show()
    cv.waitKey(0)
    imsave(str2 + Myfilename + '_out.jpeg', imgOutput)
    while(1):
        if cv2.waitKey(0):
            break
cv2.destroyAllWindows()


