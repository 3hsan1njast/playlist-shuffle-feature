import random

def shuffle(playlist: list):
    clone = playlist
    while (len(clone) != 0):
        track = random.choice(clone)
        print(f'♫ Now playing ♫ --> "{track}"')
        clone.remove(track)
    
    print("--- Your playlist has ended ---")


# Feel free to add your own playlist (:
my_playlist = [
    "Baraye To",
    "No Role Modelz",
    "Save Your Tears", 
    "Pray For Me", 
    "a lot", 
    "I KNOW?", 
    "Ordinary Life", 
    "Secrets"
]

shuffle(my_playlist)
