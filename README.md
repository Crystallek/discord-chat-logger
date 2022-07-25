[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Crystallek/discord-chat-logger.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Crystallek/discord-chat-logger/context:python)

**discord-chat-logger**

This is a real-time discord chat logger, where you can have all chats in one place and have them logged in the file for future use.

## 1.0.1 UPDATE
  - Group filtering (you can choose which groups will be logged)
  - Embed fix (before it crashed the app, not it says that embeds are not supported)

## What does it do?
  - It saves the data from the discord gateway to the file

## How to set it up?
  - Insert your token to the "token.txt" file, located in the data folder
  - If you want to, you can filter out groups you want to log in the "guildstolog.txt" file. Default to "all", which logs all the groups
  - Turn it on
  
## Used libraries
  - websocket
  - json
  - threading
  - time
  - requests
  - colorama
  - emoji
  - os
  - unidecode

## FAQ
 Q: Will this lock my account?
 
 A: It shouldn't. Only thing the program does, is it filters out messages from the discord gateway. Discord gateway won't lock you. Why i said it shouldn't? Because it uses one api endpoint to translate guild id to guild name (to make it look better). I have tried it on multiple unverified accounts and i haven't been locked out once, but i won't promise anything.
 
 Q: I'm getting error <random-error>. How do I fix it?
  
 A: This is mainly problem on Discord's end and its rate limits or you entered the wrong token (insert the token without an apostrophe, thanks). Just wait a minute and turn it on again. 
  
 Q: Guild ID filtering doesn't work!
  
 A: Again, have you removed the apostrophes?
 
### Working Versions

| Version | Working            |
| ------- | ------------------ |
|   1.0.1    | :white_check_mark: |
|   1.0.0    | :white_check_mark: |
 </h6>
 
 ## Contact us
> Join our [Discord](https://aimforum.ml/freesploitdis.html)
 
> [Email](mailto:support@aimforum.ml) us

## License

>You can check out the full license [here](https://github.com/AimSploit/discord-raid-tool/blob/main/LICENSE)

This project is licensed under the terms of the **GNU General Public License v3.0** license.
