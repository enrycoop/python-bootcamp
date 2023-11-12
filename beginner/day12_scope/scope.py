# SCOPE

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

# Local scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()