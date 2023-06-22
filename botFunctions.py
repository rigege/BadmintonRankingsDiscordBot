import requests
from bs4 import BeautifulSoup
from getFlags import getFlag
from discord import Embed, Colour

def singlesRank(URL, disc):                     # scrapes the web for data, and organizes it into a discord embed formatted for singles events and returns the embed
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(class_="ruler")

        data = results.find_all("tr")
        data.pop(0)
        data.pop(0)
        data.pop(len(data)-1)
        
        colour = {"Men's Singles":"#DF2027", "Women's Singles":"#ffee00"}              # dictionoary is used to get colour of embed based on men's or womne's discipline
        final = ""
        for entry in data:                      # loop to add all the data into a final string to add into the embed
                info = entry.find_all("td")
                                                # below a separate function is called that maps the country code to the appropriate flag (getFlag)
                string = info[0].text + " | " + getFlag(info[3].text) + " | " + info[10].text +" | " + info[7].text +"```" + info[4].find("a").text + "\n" + "```"
                final += string

        discipline = disc + " Rankings"
        date = soup.find(class_="rankingdate").text.strip("()")
        
        emb = Embed(colour=Colour.from_str(colour[disc]), title=discipline, url=URL, description=final)
        emb.set_footer(text="Week of " + date)
        
        return emb
        

def doublesRank(URL, disc):                     # scrapes the web for data, and organizes it into a discord embed formatted for doubles events and returns the embed                    
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(class_="ruler")

        data = results.find_all("tr")
        data.pop(0)
        data.pop(0)
        data.pop(len(data)-1)
        
        colour = {"Men's Doubles":"#0084ff", "Women's Doubles":"#00ff6a", "Mixed Doubles":"#de4cf5"}
        final = ""
        for entry in data:                      
                info = entry.find_all("td")
                
                players = info[4].find_all("a")
                string = info[0].text + " | " + getFlag(info[3].find("p").text) + " | " + info[10].text +" | " + info[7].text + "```" + players[0].text + "\n" + players[1].text + "\n" + "```"
                final += string
    
        discipline = disc + " Rankings"
        date = soup.find(class_="rankingdate").text.strip("()")
        
        emb = Embed(colour=Colour.from_str(colour[disc]), title=discipline, url=URL, description=final)
        emb.set_footer(text="Week of " + date)
        
        return emb

def getAdj(lookfor, embed):    # function to get the next or previous page of rankings, previous embed is passed so the data from the last page can be used to get the new page
        page = requests.get(embed.url)
        soup = BeautifulSoup(page.content, "html.parser")
        if (str(soup.find(class_ = lookfor)) != "None"):
                URL = "https://bwf.tournamentsoftware.com" + soup.find(class_ = lookfor)["href"]
        
                if ("single" in embed.title.lower()):   # checking the title to determine if is singles or doubles
                        edit = singlesRank(URL, embed.title.strip(" Rankings")+"s")
                else:
                        edit = doublesRank(URL, embed.title.strip(" Rankings")+"s")
                return edit
        else:
                return embed    # if no page can be found, then the original embed is returned again so there is no change to the displyed page