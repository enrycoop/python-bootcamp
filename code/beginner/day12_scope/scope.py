# SCOPE

# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"Enemies outside function: {enemies}")

# Local scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(portion_strength)


# Global Scope
# player_health = 10
#
# def drink_potion():
#     player_health = 2 # le modifiche non escono dallo scope
#     print(player_health)
#
# drink_potion()
# print(player_health)

# There is no Block Scope

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]

# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy) # posso accedervi perché è nello stesso scope

# Modifying Global Scope
# enemies = 1

# def increase_enemies():
#     global enemies # pratica scoraggiata
#     enemies += 2
#     print(f"Enemies inside function: {enemies}")

# increase_enemies()
# print(f"Enemies outside function: {enemies}")

# Global Constants

PI = 3.14159 # è solo una convenzione ma per le globali costanti si usa il maiuscolo