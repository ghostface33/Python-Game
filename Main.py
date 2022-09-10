### NOTE: NOT ALL SYSTEMS ARE COMPLETED
import random,time
print('loading game\n')
#data
modes = {
  'easy': 2,
  'normal':1,
  'hard':0.5
}
stuff = {
  'bandages': 30,
  'first aid': 10,
  'bread': 15,
  'soda': 10
}
maps = [
  'swamp',
  'forest',
  'desert'
]
day = 0

# input data
choice = input("Select Gamemode:\n\n[1]: Easy\n[2]: Normal\n[3]: Hard\n\nInput: ")
choice = int(choice)
if choice == None or choice > 3:
  print("Didn't find gamemode, quitting..")
  exit()
gamemode = choice-1
gamemode = list(modes.items())[gamemode][0]
distance = random.randrange(20,100) * modes[gamemode]
print('Game difficulty set to: '+ gamemode)
time.sleep(1)
place = random.choice(maps)

# starting game now
print('Starting...\n\n')
time.sleep(1)
print('You are, for some reason, stuck in a ' + place + ' and need to find a way how to escape...')
time.sleep(1)
print('type help for commands')

while True:
  inp = input("> ")
  if inp == "distance":
    print("You are " + str(distance) + " miles away from freedom")
  elif inp == "help":
    print("Commands:\n\ndistance: shows how far you are away from completing the game.\nitems: shows all items you have in your inventory\nuse: uses an item you have in your inventory\nscavenge: searches nearby for items. (uses 1 day)\nwalk: walk toward freedom. (uses 1 day)")
  elif inp == "walk":
    dis = random.randrange(1,7)* modes[gamemode]
    day = day + 1
    print('day: ' + str(day))
    print('You managed to walk ' + str(dis) + " miles")
    distance = distance - dis
    if distance <= 0:
      print('You have sucessfully completed the game. (' + day + ' days)')
      exit()
