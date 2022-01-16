import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread("C:/Users/Nikhi/Downloads/10yr old white oak.png")
imgplot = plt.imshow(img)
#lum_img = img[:, :, 0]
#plt.imshow(lum_img, cmap="hot")

from PIL import Image

img = Image.open('C:/Users/Nikhi/Downloads/10yr old white oak.png')
imgWidth, imgHeight = img.size
img = img.convert("RGBA")
imgdata = img.getdata()

x_pos = 0
y_pos = 1
w_pos = 0

for item in imgdata:
    if (x_pos) == imgWidth:
        x_pos = 1
        y_pos += 1
    else:
        x_pos += 1

    if (y_pos) == 450:
        if (item[0] <= 200):
            if (item[1] <= 200):
                if (item[2]<= 200):
                    if (item[3] == 255):
                        print(x_pos, item[0], item[1], item[2], item[3], "not white")
                        w_pos += 1
        else:
            if (item[2] == 255):
                print(x_pos,item[2], "white")
            else:
                
                print(x_pos, item[0], item[1], item[2], item[3])
         
print()
print("Picture pixel Width and Height",imgWidth,imgHeight)
print("Picture Width", 10, "feet")
print("Picture Brown Pixels Size", w_pos)
print("Tree Root Width (DBH)", round(w_pos / x_pos * 10 * 12), "inches")
print("Tree Growth Factor", 5)
print("Tree Age approximately", round(w_pos / x_pos * 10 * 12 * 5), "years")
