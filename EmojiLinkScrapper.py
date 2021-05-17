import requests
import re
from bs4 import BeautifulSoup
import json
import pickle

# All the links that will be used to scrape the site
CategoriesLinks = ["people", "nature", "food-drink", "activity", "travel-places", "objects", "symbols", "flags"]
EmojiLinks = []
#loops though every link in 
for category in CategoriesLinks:
    #url which will go through each diffrent catehgory
    Url = "https://emojipedia.org/{}".format(category)
    print(Url)
    #renders the page documnet
    page = requests.get(Url).content
    soup = BeautifulSoup(page, 'lxml')
    #finds the emoji list of the page
    EmojiList = soup.find(class_="emoji-list")
    #gets all the links with in emoiji-list
    for li in EmojiList.find_all("li"):
         #gets the links with in the li element
         SubStringLink = li.a.get("href")
         #creates the new url
         #ex: NewUrl= https://emojipedia.org/people/ + briefcase/
         NewUrl = Url + SubStringLink
         #adds the list data
         EmojiLinks.append(NewUrl)
         

#only uncoment when you are ready to save the data to a json file
# with open('EmoijLinks.data', 'wb') as filehandle:
#     # store the data as binary data stream
#     pickle.dump(EmojiLinks, filehandle)