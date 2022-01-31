import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import requests
import pandas as pd
import csv
import json


API_KEY = "2b10jIwQGcnhgz5KCnXiXUvO"
api_endpoint = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"

image_path_1 = "C:/Users/Owner/OneDrive/Desktop/eCybermission/Test Images/Tree 1 (Northern Red Oak)/oakbark.jpg"
image_data_1 = open(image_path_1, 'rb')

image_path_2 = "C:/Users/Owner/OneDrive/Desktop/eCybermission/Test Images/Tree 1 (Northern Red Oak)/oakleaf.jpg"
image_data_2 = open(image_path_2, 'rb')

data = {
	'organs': ['bark', 'leaf']
}

imgfiles = [
	('images', image_data_1),
	('images', image_data_2)
]

response = requests.post(url=api_endpoint, files=imgfiles, data=data)

json_result = json.loads(response.text)

treename = json_result["results"][0]["species"]["commonNames"][0]

#file1 = open("treegrowthfactors.csv")
#csvreader = csv.reader(file1)
treegrowth = pd.read_csv('treegrowthfactors.csv', header=None, index_col=0, squeeze=True).to_dict()

    
    
#file2 = open("treelifespans.csv")
#csvreader = csv.reader(file2)
treespan = pd.read_csv('treelifespans.csv', header=None, index_col=0, squeeze=True).to_dict()


img = mpimg.imread("C:/Users/Owner/OneDrive/Pictures/Saved Pictures/tree.jpg")
imgplot = plt.imshow(img)
#lum_img = img[:, :, 0]
#plt.imshow(lum_img, cmap="hot")


img = Image.open("C:/Users/Owner/OneDrive/Pictures/Saved Pictures/tree.jpg")
imgWidth, imgHeight = img.size
img = img.convert("RGBA")
imgdata = img.getdata()

x_pos = 0
y_pos = 1
w_pos = 0

for item in imgdata:
    #print(x_pos, y_pos, w_pos)
    if (x_pos) == imgWidth:
        x_pos = 1
        y_pos += 1
    else:
        x_pos += 1

    if (y_pos) == 200:
        if (item[0] < 255):
            if (item[1] < 255):
#                if (50 <= item[2] <= 80):
#                    if (item[3] == 255):
                        print(x_pos,item[0],item[1],item[2],item[3], "Not White")
                        w_pos += 1
        else:
            if (item[0] == 255):
                print(x_pos,item[2], "White")
            else:
                print(x_pos, item[0], item[1], item[2], item[3])
    elif y_pos > 200:
        break
        
width = 10
         
print()
print("Picture Width:", imgWidth, "pixels")
print("Picture Height:", imgHeight, "pixels")
print("Picture Width:", width, "feet")
print("Trunk Pixels:", w_pos, "pixels")
trunkwidth = round(w_pos / imgWidth * width * 12)
print("Trunk Width:", trunkwidth, "inches")

print('\n'"Tree Name:", treename)
if treename in treegrowth:
    growth = treegrowth[treename]
    print("Growth Factor:", growth)
else:
    print("This tree is not in our database")
    
if treename in treespan:
    span = treespan[treename]
    print("Lifespan:", span, "years")
else:
    print("This tree is not in our database")
        
print('\n''\n'"Tree Aproximate Age:", int(trunkwidth * growth), "years")
