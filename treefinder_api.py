import requests
import pandas as pd
import csv
import json
from pprint import pprint


API_KEY = "2b10jIwQGcnhgz5KCnXiXUvO"	# Your API_KEY here
api_endpoint = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"

image_path_1 = "C:/Users/Owner/Downloads/oakbark.jpg"
image_data_1 = open(image_path_1, 'rb')

image_path_2 = "C:/Users/Owner/Downloads/oakleaf.jpg"
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

pprint(response.status_code)
#pprint(json_result)
#pprint(response.text)
treename = json_result["results"][0]["species"]["commonNames"][0]
pprint("Tree Name: " + treename)

file1 = open("treegrowthfactors.csv")
csvreader = csv.reader(file1)
treegrowth = pd.read_csv('treegrowthfactors.csv', header=None, index_col=0, squeeze=True).to_dict()
if treename in treegrowth:
    growth = treegrowth[treename]
    pprint("Growth Factor: " + str(growth))
else:
    pprint("This tree is not in our database")
    
    
file2 = open("treelifespans.csv")
csvreader = csv.reader(file2)
treespan = pd.read_csv('treelifespans.csv', header=None, index_col=0, squeeze=True).to_dict()
if treename in treespan:
    span = treespan[treename]
    pprint("Lifespan: " + str(span) + " years")
else:
        pprint("This tree is not in our database")
    

#https://docs.python-requests.org/en/master/api/
#https://stackoverflow.com/questions/4359495/what-is-exactly-a-file-like-object-in-python
#https://www.w3schools.com/python/ref_requests_post.asp