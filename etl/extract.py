import requests
def get_recall_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        response_data = response.json()
        return response_data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None