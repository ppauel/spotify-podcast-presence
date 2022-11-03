# Spotify Podcast Discord Presence
A Python script allowing you to display the podcast you're currently listening to in your Discord profile.

![Example](https://i.imgur.com/80hSwPG.png)

## Installation

### Clone the repository
```sh
git clone https://github.com/ppauel/spotify-podcast-presence
```
- Navigate into the newly created folder

### Install the required pip modules.
```sh
pip3 install python-dotenv
pip3 install pypresence
```
> **pypresence** is developed by qwertyquerty (https://github.com/qwertyquerty/pypresence)

### Create your .env file
- Create a new file called "**.env**" and copy the contents from "**.env.example**"

### Create a Discord Application
- Visit https://discord.com/developers/applications and click "**New Application**"
- Select a name for your application (e.g. "Spotify Podcast", it will be visible in your Discord profile)
- Copy the Application ID (aka Clint ID) in your "**.env**" file

### Get a Spotify user token
- Visit https://developer.spotify.com/console/get-queue/ and click "**Get Token**"
- Tick the "**user-read-playback-state**" scope displayed on top
- Click "**Request Token**" and copy it in your "**.env**" file

### Run the script
```sh
python3 app.py
```

- **Done!** Once you start listening to a Spotify Podcast, it shows up as your Discord activity.


## Updating your Spotify user token (work in progress)
Your Spotify token created earlier will expire after some time. Once it is expired, the python log will show a notice. Currently, you have to request a new token from the Spotify website and update your "**.env**" file. Since this is not very user friendly, I'm working on a solution to automatically refresh the token.

## License
MIT
