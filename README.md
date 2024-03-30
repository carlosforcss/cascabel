# Music bot
Since a lot of discord music bots are being blocked by youtube nowadays I've decided to write up a quick project that will allow anyone to host their own discord bot. This bot includes the following commands:

/help - displays all the available commands
/p <keywords> - finds the song on youtube and plays it in your current channel. Will resume playing the current song if it was paused\
/q - displays the current music queue\
/skip - skips the current song being played\
/clear - Stops the music and clears the queue\
/leave - Disconnected the bot from the voice channel\
/pause - pauses the current song being played or resumes if already paused\
/resume - resumes playing the current song
    
# Installation
To run the discord bot all you need is python 3.4 or above.\
Then run `pip install -r requirements.txt` to install all of the python dependencies.\
Please note that you will also need to have [ffmpeg](https://ffmpeg.org/download.html) installed and make sure that the path to the bin folder is in your environment variables. 

# Token
Remember that you need to have your token setup in your environment variables as well and it should be under TOKEN. On windows you can do this by running 
`EXPORT TOKEN=<you_token_here>`
