import requests
import json
from datetime import date

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "MrBeast"
maxResults = 50


def get_playlist_id():

    try:

        # URL to get uploads playlist ID using
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        #print(json.dumps(data, indent=4))

        channel_items = data['items'][0]

        channel_playlistId = channel_items['contentDetails']['relatedPlaylists']['uploads']

        print(channel_playlistId)

        return channel_playlistId

    except requests.exceptions.RequestException as e:
        raise e



def get_video_ids(playlistId):

    video_ids = []

    pageToken = None

    base_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=ContentDetails&maxResults={maxResults}&playlistId={playlistId}&key={API_KEY}"

    try:

        while True:

            url = base_url

            if pageToken:
                url += f"&pageToken={pageToken}"
                

            response = requests.get(url)

            response.raise_for_status()

            data = response.json()

            #print(json.dumps(data, indent=4))

            for item in data.get('items', []):
                video_id = item['contentDetails']['videoId']
                video_ids.append(video_id)

            pageToken = data.get('nextPageToken')

            if not pageToken:
                break

        print(video_id)

        return video_ids
    
    except requests.exceptions.RequestException as e:
        raise e



"https://youtube.googleapis.com/youtube/v3/videos?part=ContentDetails&part=snippet&part=statistics&id=0e3GPea1Tyg&key={API_KEY}"

def extract_video_data(video_ids):

    extracted_data = []

    def batch_list(video_id_list, batch_size):
        for video_id in range(0, len(video_id_list), batch_size):
            yield video_id_list[video_id:video_id + batch_size]

    try:
        for batch in batch_list(video_ids, maxResults):
            video_ids_str = ",".join(batch)

            url = f"https://youtube.googleapis.com/youtube/v3/videos?part=ContentDetails&part=snippet&part=statistics&id={video_ids_str}&key={API_KEY}"

            response = requests.get(url)

            response.raise_for_status()

            data = response.json()

            for item in data.get('items', []):
                video_id = item['id']
                snipet = item['snippet']
                contentDetails = item['contentDetails']
                statistics = item['statistics']

                video_data = {
                    "video_id": video_id,
                    "title": snipet.get("title"),
                    "publishedAt": snipet.get("publishedAt"),
                    "duration": contentDetails.get("duration"),
                    "viewCount": statistics.get("viewCount"),
                    "likeCount": statistics.get("likeCount"),
                    "commentCount": statistics.get("commentCount")
                }

                extracted_data.append(video_data)

            return extracted_data


    except requests.exceptions.RequestException as e:
        raise e
    

def save_to_json(extracted_data):
    file_path = f"./data/YT_data_{date.today()}.json"

    with open(file_path, 'w', encoding="utf-8") as json_outfile:
        json.dump(extracted_data, json_outfile, indent=4, ensure_ascii=False)



if __name__ == "__main__":
    playlistId = get_playlist_id()
    vidoe_ids = get_video_ids(playlistId)
    video_data = extract_video_data(vidoe_ids)
    save_to_json(video_data)
