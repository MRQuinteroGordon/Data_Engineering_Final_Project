from requests import post, get
import json
import pprint



def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_track_id(token, artist_name, track_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q=track:'{track_name}'%20artist:'{artist_name}'&type=track&limit=1"
    query_url = url + query
    # query_url = f"https://api.spotify.com/v1/search?q=track:'{track_name}'%20artist:'{artist_name}'&type=track&limit=1"
    result = get(query_url, headers=headers)
    # json_result = json.loads(result.content)["tracks"]["items"][0]["id"]
    
    json_result = json.loads(result.content)
    # print(f"json result is: {json_result}")
    if 'error' in json_result:
        error = f"Error searching for track with name '{track_name}' by artist: {artist_name}.  API response is: {json_result}\n"
        with open('id_error_log.txt', 'a+') as file:
            file.write(error)
            # print(error)
        return 0    
    elif len(json_result) == 0:
        # print(f"No track with name '{track_name}' exists...")
        error = f"No track with name '{track_name}' by artist: {artist_name} found.  API response is: {json_result}\n"
        with open('id_error_log.txt', 'a+') as file:
            file.write(error)
        return 0
        # return None
    elif json_result['tracks'] == []:
        error = f"No track with name '{track_name}' by artist: {artist_name} found.  API response is: {json_result}\n"
        with open('id_error_log.txt', 'a+') as file:
            file.write(error)
        return 0
    elif json_result['tracks']['items'] == []:
        error = f"No track with name '{track_name}' by artist: {artist_name} found.  API response is: {json_result}\n"
        with open('id_error_log.txt', 'a+') as file:
            file.write(error)
        return 0
    else:
        track_id = json_result["tracks"]["items"][0]["id"]
        return track_id

def get_id(artist, track, token):
    track_id = search_for_track_id(token, artist, track)
    return track_id