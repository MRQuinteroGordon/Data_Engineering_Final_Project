from requests import post, get
import json
import pprint


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def extract_audio_features(token, track_id):
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    # print(url)
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

def extract_many_audio_features(token, track_ids):
    url = f"https://api.spotify.com/v1/audio-features?ids={track_ids}"
    # print(f"track ids are: {track_ids}")
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result["audio_features"] # <---- FIX THIS RIGHT HERE

    
