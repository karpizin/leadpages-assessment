from services.api_client import *
#from services.api_client import post_animals_in_batches
from utils.transformations import * 


def main():
    # Step 1: Fetch all animals
    animals = fetch_all_animals()


    print(f"analyzing animals for friends... ")
    for a in animals: 
        if a.get('friends'):
            print(f"animal with friends: {a}")
    
    # Step 2: Transform animals
    print(f"doing transformations ")
    transformed_animals = [transform_animal(animal) for animal in animals]
    
    # Step 3: Post animals in batches
    print(f"starting to post batches ")
    post_animals_in_batches(transformed_animals)
    print(f"uploading finished ")


if __name__ == "__main__":
    main()