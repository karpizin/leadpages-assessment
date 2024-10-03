from datetime import datetime

def transform_animal(animal):
    # Split the friends string into a list
    if 'friends' in animal and isinstance(animal['friends'], str):
        animal['friends'] = animal['friends'].split(',')
    else: 
        animal['friends'] = []

    # Transform born_at field to ISO8601
    if animal.get('born_at'):
        animal['born_at'] = datetime.utcfromtimestamp(animal['born_at'] / 1000).isoformat() + 'Z'
    else: 
        animal['born_at'] = 0
        
    return animal