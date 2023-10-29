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
        'title': 'DRAGONBORN',
        'description': '*Dragonborn resemble draconic humanoids. They are a proud race that values clan and skills above all else. Once enslaved by dragons, they strive to be self-sufficient, not wanting to be beholden to anyone, not even the gods. Dragonborn can have scales in a variety of colours, and may or may not have a tail.*',
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Dragonborn.png',
        'color': 0xF77709 #Placeholder     
        },
    'drow': {
        'title': 'DROW',
        'description': "*Drow are the dark elves of the Forgotten Realms. They dwell in the Underdark, large subterranean caverns beneath the surface.*",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Drow.png',
        'color': 0xF77709 #Placeholder     
        },
    'dwarf': {
        'title': 'DWARF',
        'description': "*As durable and unyielding as their homes of stone, dwarves are some of the finest warriors, miners, and smiths of Faerûn.*",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Dwarf.png',
        'color': 0xF77709 #Placeholder     
        },
    'elf': {
        'title': 'ELF',
        'description': "*With an ethereal countenance and long lifespans, elves are at home with nature's power, flourishing in light and dark alike.*",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Elf.png',
        'color': 0xF77709 #Placeholder     
        },
    'githyanki': {
        'title': 'GITHYANKI',
        'description': "*Githyanki are peerless warriors from the Astral Plane, known for their legendary silver blades and red dragon mounts. They seek the total destruction of Mind Flayers, whose ancient empire enslaved the Gith for millennia.\n\nAs time does not pass in their native Astral Plane, Githyanki are instead hatched from eggs all across realmspace in places called crèches. Crèches act as hatcheries, training grounds, and shelters outside of the Astral Plane.\n\nGithyanki are ruled by their lich queen Vlaakith and led in battle by her dragon-riding knights, the Kith'rak.*",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Githyanki.png',
        'color': 0xF77709 #Placeholder     
        },
    'gnome': {
        'title': 'GNOME',
        'description': "*Small, clever, and energetic, gnomes use their long lives to explore Faerûn's brightest corners and darkest depths.*",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Gnome.png',
        'color': 0xF77709 #Placeholder     
        },
    'half-elf': {
        'title': 'HALF-ELF',
        'description': "*Half-Elves inherit blessings from both their parents, but at the price of never quite fitting in. Curious, ambitious, and versatile, half-elves are welcome everywhere, but struggle without a community to call their own.*",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Half-Elf.png',
        'color': 0xF77709 #Placeholder     
        },
    'half-orc': {
        'title': 'HALF-ORC',
        'description': "*Half-Orcs exhibit a blend of orcish and human characteristics, and their appearance varies widely. Creatures of intense emotion, Half-Orcs are more inclined to act than contemplate - whether the rage burning their bodies compels them to fight, or the love filling their hearts inspires acts of incredible kindness.*",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Half-Orc.png',
        'color': 0xF77709 #Placeholder     
        },
    'halfling': {
        'title': 'HALFLING',
        'description': "*Small yet capable, halflings prefer the comforts of home and hearth - but their natural luck and dexterity makes them fine adventurers.*",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Halfling.png',
        'color': 0xF77709 #Placeholder     
        },
    'human': {
        'title': 'HUMAN',
        'description': "*The most common face to see in Faerûn, humans are known for their tenacity, creativity, and endless capacity for growth.*",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Human.png',
        'color': 0xF77709 #Placeholder     
        },
    'tiefling': {
        'title': 'TIEFLING',
        'description': "*Touched by the Hells, Tieflings are resistant to fire and carry extraordinary Infernal powers.*",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Tiefling.png',
        'color': 0xF77709 #Placeholder     
        },
}

racial_trait = {
    
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
