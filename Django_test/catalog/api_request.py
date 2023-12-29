import requests


URL = 'http://127.0.0.1:8000/api/category/?format=json'


def get_json_from_api(URL):
    try:
        req = requests.get(URL)
        if req.status_code == 200:
            print(f"Status: code {req.status_code}")
            for item in req.json():
                print(item)
        else:
            print(f"Error receiving data from the API. Status code: {req.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


json_data= get_json_from_api(URL)
