import requests
import time
import os
from pypresence import Presence
from dotenv import load_dotenv

load_dotenv()

discord_client_id = os.environ['DISCORD_CLIENT_ID']
spotify_user_token = os.environ['SPOTIFY_USER_TOKEN']

RPC = Presence(discord_client_id)
RPC.connect()

baseUrl = "https://api.spotify.com/v1/"
routes = {
    "player": "me/player/currently-playing",
    "queue": "me/player/queue",
}


def getPlayingState(token):
    headers = {
        "Authorization": "Bearer " + token
    }
    res = requests.get(url=baseUrl+routes["queue"], headers=headers)
    if (res.status_code != 200):
        print('Failed connect to the Spotify API. Is the user token still valid?')
        return False
    currentlyPlaying = res.json()['currently_playing']
    if 'show' in currentlyPlaying:
        episode_name = currentlyPlaying['name']
        episode_url = currentlyPlaying['external_urls']['spotify']
        episode_image = currentlyPlaying['images'][1]['url']
        show_name = currentlyPlaying['show']['name']
        show_publisher = currentlyPlaying['show']['publisher']

        return {"state": show_publisher, "details": episode_name, "large_image": episode_image, "large_text": show_name, "url": episode_url}
    return False


while True:
    currentState = getPlayingState(spotify_user_token)
    if (currentState != False):
        RPC.update(state=currentState['state'], details=currentState['details'],
                   large_image=currentState['large_image'], large_text=currentState['large_text'], buttons=[{"label": "Play on Spotify", "url": currentState['url']}])
        print(f'Updated Discord Presence ({currentState["details"]})')
    else:
        RPC.clear()
    time.sleep(15)
