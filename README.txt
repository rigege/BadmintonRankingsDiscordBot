Badminton Rankings Discord Bot

TO USE ----------------------------
- this bot must be hosted locally for now
- download all the files into a folder
- creat an application in discord developer portal and set up the bot (read more: https://discord.com/developers/docs/getting-started)
- copy and paste the bot token into line 4 of badmintonRankingsBot.py
- insert the name of your guild in line 5 of badmintonRankingsBot.py
- run the badmintonRankingsBot.py file
= the bot is now ready to use

WHAT THIS IS -----------------------
- discord is a chat and voice call app, it is commonly used by gamers but also has many other communities
- in discord, a guild (commonly known as a server) consists of multiple text channels and voice call channels with multiple members, usually with something in common
- bots can be used in servers to perform and automate various tasks and add additional features
- this bot allows user to view badminton world rankings from directly inside a discord server with text commands
- its displays the players, their ranks, their countries, and their point counts

HOW IT WORKS -----------------------
- the bot is written in Python, utilizing discord.py library to communicate with the client
- a web scraping library, Beatiful Soup, is used to extract data from https://bwf.tournamentsoftware.com/
- comments are added in the code that explain specific choices and how parts work 