from constants import *
from models import *

# Primero tenemos que definir los stats y los pokemon

pokemon1 = Pokemon("Bulbasaur", 100, "grass", "poison")
pokemon2 = Pokemon("Charmander", 100, "fire", None)

# Stats
pokemon1.stats = {
    HP: 45,
    ATTACK: 49,
    DEFENSE: 49,
    SPATTACK: 65,
    SPDEFENSE: 65,
    SPEED: 45
}

pokemon2.stats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}

# Attacks
pokemon1.attacks = [Attack("scratch", "normal", PHYSICAL, 10, 10, 100)]
pokemon2.attacks = [Attack("scratch", "normal", PHYSICAL, 10, 10, 100)]

# Start battle
battle = Battle(pokemon1, pokemon2)

def ask_command(pokemon):
    command = None
    while not command:
        # DO ATTACK -> attack 0
        tmp_command = input("What should "+pokemon.name+" do?").split(" ")
        if len(tmp_command) == 2:
            try:
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1])
                    command = Command({DO_ATTACK: int(tmp_command[1])})
                except Exception:
                    pass
    return command 


while not battle.is_finished():
    # First ask for command
    command1 = ask_command(pokemon1)
    command2 = ask_command(pokemon2)

    turn = Turn()
    turn.command1 = command1
    turn.command2 = command2

    