import requests
from tenacity import retry, stop_after_attempt, wait_random

BASE_URL = 'http://localhost:3123/animals/v1'


#@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=5, max=15))

@retry(stop=stop_after_attempt(5), wait=wait_random(5, 15))
def fetch_animals(page: int):
    response = requests.get(f"{BASE_URL}/animals", params={'page': page})
    response.raise_for_status()  # Handle HTTP errors
    return response.json()

def fetch_all_animals():
    animals = []
    page = 1
    while True:
        data = fetch_animals(page)
        animals.extend(data['items'])
        if  page >= data['total_pages']:
            break
        page += 1
        print(f"loading {page} page (of {data['total_pages']}) with animals")
    return animals


def post_animal_batch(animals_batch):
    print(f"committing next batch...")
    url = f"{BASE_URL}/home"
    response = requests.post(url, json=animals_batch)
    #print(f"json for batch = {animals_batch}")
    response.raise_for_status()  # Handle HTTP errors
    return response.json()

def post_animals_in_batches(animals, batch_size=100):
    for i in range(0, len(animals), batch_size):
        batch = animals[i:i+batch_size]
        post_animal_batch(batch)
        print(f"uploaded {i*batch_size} our of {len(animals)}")



 # {
 #   "id": 1,
 #   "name": "string",
 #   "born_at": "2024-10-03T07:01:32.675Z",
 
#   "friends": [
#      "string"
#    ]
#  }