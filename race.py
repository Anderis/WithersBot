race_aliases = {
    'dragonborn': ['db', 'dragonb', 'dborn', 'dragon'],
    'drow': ['dr','dro'],
    'dwarf': ['dw', 'dwa', 'dwar'],
    'elf': ['e', 'el'],
    'githyanki': ['gi', 'gith', 'yanki', 'githy', 'githyank', 'gi'],
    'gnome': ['gn', 'gno', 'gnom'],
    'half-elf': ['h-elf', 'helf', 'half-e', 'halfe', 'he', 'h-e'],
    'half-orc': ['h-orc', 'horc', 'half-o','halfo', 'ho', 'h-o'],
    'halfling': ['half',  'hling', 'halfl'],
    'human': ['man', 'hu', 'hum', 'hman'],
    'tiefling': ['tief', 't', 'tling']
}


race_data = {
    'dragonborn': {
        'title': 'Dragonborn',
        'description': '',
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Dragonborn.png',
        'color': 0xF77709 #Placeholder     
        },
    'drow': {
        'title': 'Drow',
        'description': '',
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Drow.png',
        'color': 0xF77709 #Placeholder     
        },
    'dwarf': {
        'title': 'Dwarf',
        'description': '',
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Dwarf.png',
        'color': 0xF77709 #Placeholder     
        },
    'elf': {
        'title': 'Elf',
        'description': '',
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Elf.png',
        'color': 0xF77709 #Placeholder     
        },
    'githyanki': {
        'title': 'Githyanki',
        'description': '',
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Githyanki.png',
        'color': 0xF77709 #Placeholder     
        },
    'gnome': {
        'title': 'Gnome',
        'description': '',
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Gnome.png',
        'color': 0xF77709 #Placeholder     
        },
    'half-elf': {
        'title': 'Half-Elf',
        'description': '',
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Half-Elf.png',
        'color': 0xF77709 #Placeholder     
        },
    'half-orc': {
        'title': 'Half-Orc',
        'description': '',
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Half-Orc.png',
        'color': 0xF77709 #Placeholder     
        },
    'halfling': {
        'title': 'Halfling',
        'description': '',
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Halfling.png',
        'color': 0xF77709 #Placeholder     
        },
    'human': {
        'title': 'Human',
        'description': '',
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Human.png',
        'color': 0xF77709 #Placeholder     
        },
    'tiefling': {
        'title': 'Tiefling',
        'description': '',
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Tiefling.png',
        'color': 0xF77709 #Placeholder     
        },
}

def get_race_info(race_name):
    race_name = race_name.lower()  # Convert input to lowercase

    print(f"Searching for race_name: {race_name}")  # Add this line for debugging

    for race, aliases in race_aliases.items():
        if race_name == race:
            return race_data.get(race, None)
        elif race_name in aliases:
            return race_data.get(race, None)

    print("No match found for race_name")  # Add this line for debugging

    return None
