import requests
import re
from bs4 import BeautifulSoup
import json
import pickle

EmojiDict = {}
#loads in the data
with open('EmoijLinks.data', 'rb') as filehandle:
    # read the data as binary data stream
    EmoijLinks = pickle.load(filehandle)

def getData(EmojiID, link):
    #gets the page
    page = requests.get(link).content
    soup = BeautifulSoup(page, "lxml")
    #gets the div where the emoji data is located
    div = soup.find('div', class_ = "content")
    #used to get the emoji
    emoji = div.h1.text.split()[0]
    #used to get the name of the emoji
    name = div.h1.text.split(None, 1)[1]
    #used to get the meaning of the emoji
    meaning = div.p.text
    EmojiDict[EmojiID] = {"emoji":emoji, "name": name, "meaning": meaning}
    print(EmojiID)
    

def getUpdatedLink(oldLink):
    #used regex to find the sublink of the catagory
    UpdatedEmojiLink = re.findall(r'(.*?)/', oldLink)
    #gets the last item of the subcatagory
    newUrl = "https://emojipedia.org/" + UpdatedEmojiLink[4]
    #returns the updated url for the emoji
    return newUrl

#goes through the emoji links data collected from EmojilinkScrapper.py
for EmojiID, link in enumerate(EmoijLinks):
    try:
        getData(EmojiID, link)
    except:
        #gets the new updated link for the url
        Newlink = getUpdatedLink(link)
        getData(EmojiID, Newlink)
        continue
    
#creates the data
with open('EmojiData.json', 'w') as fp:
    json.dump(EmojiDict, fp)