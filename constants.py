# Pokemon stats

HP = "HP"
ATTACK = "Attack"
DEFENSE = "Defense"
SPATTACK = "SpAttack"
SPDEFENSE = "SpDefense"
SPEED = "Speed"

PHYSICAL = "physical"
SPECIAL = "special"

# Command
DO_ATTACK = "attack"
DO_ATTACK_SELECTION = "selected_attack"

# Attack categories
PHYSICAL = "physical"
SPECIAL = "special"
NATURES = [
    "Hardy",
    "Lonely",
    "Brave",
    "Adamant",
    "Naughty",
    "Bold",
    "Docile",
    "Relaxed",
    "Impish",
    "Lax",
    "Timid",
    "Hasty",
    "Serious",
    "Jolly",
    "Naive",
    "Modest",
    "Mild",
    "Quiet",
    "Bashful",
    "Rash",
    "Calm",
    "Gentle",
    "Sassy",
    "Careful",
    "Quirky"
]

NATURE_MATRIX = [
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},
    {HP: 1, ATTACK: 1.1, DEFENSE: 0.9, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},
    {HP: 1,}
]