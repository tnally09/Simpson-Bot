Simpson's Bot Version 1.0 06/22/2021

------SUMMARY-------

The Simpson's Bot is an automated Discord chat bot that interacts with the Frinkiac API to pull 
random episode frames and generate a "Simpsons meme." The bot can either automatically reply when
certain keywords or phrases are said in chat, or the /any command can be provided for a random
screenshot. The Simpson's Bot currently only supports seasons 1 through 10 and will not pull content 
from season 11 or beyond.

The bot is programmed in Python, using the Discord, requests, base64, and re modules. It uses client
events to interact with Discord and ping for messages. When the right conditions are met, it parses
a random page of the Frinkiac JSON API to pull the frame and the associated lines of quote content, 
which are converted to the "Simpson's font" and generated onto the image itself.

------INSTALL-------


This repository only contains source code and the bot is not currently hosted online anywhere. In 
order to install and use it on your own servers, you must either find a bot host, or run the code
locally whenever you plan to use it. From there, standard Discord bot procedures follow. The final
line of the program's code contains replaceable hashmarks for a user to input their own valid 
Discord bot token.


-----HOW TO USE-----

The bot will return user selected and curated images from a keyword library contained at the bottom of 
the source code, such as "potato" or "water."

The bot will also generate an image at any time if the user simply types /any

/help will bring up a short explanation of the bot and its functions.
