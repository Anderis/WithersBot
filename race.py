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
        'description': '```ansi\n[2;34mDragonborn resemble draconic humanoids. They are a proud race that values clan and skills above all else. Once enslaved by dragons, they strive to be self-sufficient, not wanting to be beholden to anyone, not even the gods. Dragonborn can have scales in a variety of colours, and may or may not have a tail.[0m[2;31m[0m\n```',
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Dragonborn.png',
        'color': 0x6495ED     
        },
    'drow': {
        'title': 'DROW',
        'description': "```ansi\n[2;34mDrow are the dark elves of the Forgotten Realms. They dwell in the Underdark, large subterranean caverns beneath the surface.[0m[2;31m[0m\n```",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Drow.png',
        'color': 0x6495ED     
        },
    'dwarf': {
        'title': 'DWARF',
        'description': "```ansi\n[2;31m[2;35m[2;34m[2;35m[0m[2;34m[0m[2;35m[0m[2;31m[0m[2;31mAs durable and unyielding as their homes of stone, dwarves are some of the finest warriors, miners, and smiths of Faerûn.[0m[2;31m[0m\n```",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Dwarf.png',
        'color':  0xFF4040     
        },
    'elf': {
        'title': 'ELF',
        'description': "```ansi\n[2;34mWith an ethereal countenance and long lifespans, elves are at home with nature's power, flourishing in light and dark alike.[0m[2;31m[0m\n```",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Elf.png',
        'color': 0x6495ED     
        },
    'githyanki': {
        'title': 'GITHYANKI',
        'description': "```ansi\n[2;34mGithyanki are peerless warriors from the Astral Plane, known for their legendary silver blades and red dragon mounts. They seek the total destruction of Mind Flayers, whose ancient empire enslaved the Gith for millennia.\n\nAs time does not pass in their native Astral Plane, Githyanki are instead hatched from eggs all across realmspace in places called crèches. Crèches act as hatcheries, training grounds, and shelters outside of the Astral Plane.\n\nGithyanki are ruled by their lich queen Vlaakith and led in battle by her dragon-riding knights, the Kith'rak.[0m[2;31m[0m\n```",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Githyanki.png',
        'color': 0x6495ED     
        },
    'gnome': {
        'title': 'GNOME',
        'description': "```ansi\n[2;31m[2;35m[2;34m[2;35m[0m[2;34m[0m[2;35m[0m[2;31m[0m[2;31mmall, clever, and energetic, gnomes use their long lives to explore Faerûn's brightest corners and darkest depths.[0m[2;31m[0m\n```",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Gnome.png',
        'color':  0xFF4040     
        },
    'half-elf': {
        'title': 'HALF-ELF',
        'description': "```ansi\n[2;35mHalf-Elves inherit blessings from both their parents, but at the price of never quite fitting in. Curious, ambitious, and versatile, half-elves are welcome everywhere, but struggle without a community to call their own.[0m\n```",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Half-Elf.png',
        'color': 0x9370DB     
        },
    'half-orc': {
        'title': 'HALF-ORC',
        'description': "```ansi\n[2;35mHalf-Orcs exhibit a blend of orcish and human characteristics, and their appearance varies widely. Creatures of intense emotion, Half-Orcs are more inclined to act than contemplate - whether the rage burning their bodies compels them to fight, or the love filling their hearts inspires acts of incredible kindness.[0m\n```",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Half-Orc.png',
        'color': 0x9370DB    
        },
    'halfling': {
        'title': 'HALFLING',
        'description': "```ansi\n[2;31m[2;35m[2;34m[2;35m[0m[2;34m[0m[2;35m[0m[2;31m[0m[2;31mSmall yet capable, halflings prefer the comforts of home and hearth - but their natural luck and dexterity makes them fine adventurers.[0m[2;31m[0m\n```",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Halfling.png',
        'color':  0xFF4040     
        },
    'human': {
        'title': 'HUMAN',
        'description': "```ansi\n[2;31m[2;35m[2;34m[2;35m[0m[2;34m[0m[2;35m[0m[2;31m[0m[2;31mThe most common face to see in Faerûn, humans are known for their tenacity, creativity, and endless capacity for growth.[0m[2;31m[0m\n```",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Human.png',
        'color':  0xFF4040     
        },
    'tiefling': {
        'title': 'TIEFLING',
        'description': "```ansi\n[2;34mTouched by the Hells, Tieflings are resistant to fire and carry extraordinary Infernal powers.[0m[2;31m[0m\n```",
        'image_url': 'https://raw.githubusercontent.com/Anderis/WithersBot/main/images/races/Tiefling.png',
        'color': 0x6495ED  
        }
}

movement_speed = {
    'dragonborn': '9m / 30ft',
    'drow': '9m / 30ft',
    'dwarf': '7.5m / 25ft',
    'elf': '`SUBRACE DEPENDENT`',
    'githyanki': '9m / 30ft',
    'gnome': '7.5m / 25ft',
    'half-elf': '`SUBRACE DEPENDENT`',
    'half-orc': '9m / 30ft',
    'halfling': '7.5m / 25ft',
    'human': '9m / 30ft',
    'tiefling': '9m / 30ft'   
    }

racial_trait = {
    'dragonborn': '\n## <:Dragonborn:1168815084680773634> Breath Weapon <:Dragonborn:1168815084680773634>\n- `SUBRACE DEPENDENT`\n## <:Dragonborn:1168815084680773634> Draconic Ancestry <:Dragonborn:1168815084680773634>\n- `SUBRACE DEPENDENT`',
    'drow': '\n## <:feyancestry:1168809746640420915> **Fey Ancestry** <:feyancestry:1168809746640420915>\n- Cannot be put to **sleep** by magic\n- Advantage on **saving throws** against **charmed**\n## <:superiordarkvision:1168815878553477170> Superior Darkvision <:superiordarkvision:1168815878553477170>\n- Can see in the dark up to 24m\n## <:Drow:1168815047133368350> Drow Magic <:Drow:1168815047133368350>\n- **Level 1:** <:dancinglights:1168816351368978452> Dancing Lights **cantrip**\n- **Level 3:** <:faeriefire:1168816324022120448> Faerie Fire **spell**\n- **Level 5:** <:darkness:1168816338404376606> Darkness **spell**',
    'dwarf': '\n## <:dwarvenresilience:1169270630991007794> Dwarven Resilience <:dwarvenresilience:1169270630991007794>\n- Grants **advantage** on poison **saving throws**\n- Gain poison damage resistence\n## <:darkvision:1168809761857351701> Darkvision <:darkvision:1168809761857351701>\n- Can see in the dark up to 12m',
    'elf': '\n## <:feyancestry:1168809746640420915> **Fey Ancestry** <:feyancestry:1168809746640420915>\n- Cannot be put to **sleep** by magic\n- Advantage on **saving throws** against **charmed**\n## <:darkvision:1168809761857351701> Darkvision <:darkvision:1168809761857351701>\n- Can see in the dark up to 12m',
    'githyanki': '\n## <:astralknowledge:1169272239884083230> **Astral Knowledge** <:astralknowledge:1169272239884083230>\n- Gain **proficiency** in all Skills related to a chosen **Ability** until **Long Rest** `(Does not stack with current proficiencies)`\n## <:Githyanki:1168815041106157639> Githyanki Psionics <:Githyanki:1168815041106157639>\n- **Level 1:** <:magehand:1169272523410636850> Mage Hand **cantrip**\n- **Level 3:** <:enhancedleap:1169272546877771848> Enhanced Leap **spell**\n- **Level 5:** <:mistystep:1169272507849785387> Misty Step **spell**',
    'gnome': '\n## <:gnomecunning:1169280620845863033> Gnome Cunning <:gnomecunning:1169280620845863033>\n- Grants **advantage** on Intelligence, Wisdom, and Charisma **saving Throws**\n## <:darkvision:1168809761857351701> Darkvision <:darkvision:1168809761857351701>\n- Can see in the dark up to 12m',
    'half-elf': '\n## <:feyancestry:1168809746640420915> **Fey Ancestry** <:feyancestry:1168809746640420915>\n- Cannot be put to **sleep** by magic\n- Advantage on **saving throws** against **charmed**\n## <:darkvision:1168809761857351701> Darkvision <:darkvision:1168809761857351701>\n- Can see in the dark up to 12m',
    'half-orc': '\n## <:darkvision:1168809761857351701> Darkvision <:darkvision:1168809761857351701>\n- Can see in the dark up to 12m\n## <:savageattacks:1169283786912047104> Savage Attacks <:savageattacks:1169283786912047104>\n- Deal additional damage when you land a critical hit with a melee weapon attack\n## <:relentlessendurance:1169284764805644369> Relentless Endurance <:relentlessendurance:1169284764805644369>\n- if you hit 0 hitpoints you gain 1 hp instead of getting **downed** once per long rest',
    'halfling': '\n## <:halflingluck:1169286248666517566> Halfling Luck <:halflingluck:1169286248666517566>\n- When you roll a 1 on attack rolls, ability checks or saving throws, you will reroll\n## <:brave:1169287383582249071> Brave <:brave:1169287383582249071>\n- You have **advantage** on saving throws against being **frightened**',
    'human': '\n## <:human_versatility:1168535401640775830> **Human Versatility** <:human_versatility:1168535401640775830>\n- *Gain  **Proficiency** in one additional **Skill***\n- *Increased **Carrying Capacity** by 25%*',
    'tiefling': '\n## <:hellishresistance:1169289503303807086> Hellish Resistance <:hellishresistance:1169289503303807086>\n- you only take half damage from all fire type attacks\n## <:darkvision:1168809761857351701> Darkvision <:darkvision:1168809761857351701>\n- Can see in the dark up to 12m'   
}

def get_race_info(race_name):
    race_name = race_name.lower()  # Convert input to lowercase

    print(f"Searching for race_name: {race_name}")  # debugging
    for race, aliases in race_aliases.items():
        if race_name == race or race_name in aliases:
            return race_data.get(race, None)

    print("No match found for race_name")  # debugging
    return None

def get_movement_speed(race_name):
    race_name = race_name.lower()
    
    print(f"Searching for race movement speed:{race_name}") # debugging
    
    for race, aliases in race_aliases.items():
        if race_name == race or race_name in aliases:
            return movement_speed.get(race, None)
    
    print("No match found for movement speed") # debugging
    return None

def get_racial_trait(race_name):
    race_name = race_name.lower()
    
    print(f"Searching for racial feature: {race_name}")  # debugging
    
    for race, aliases in race_aliases.items():
        if race_name == race or race_name in aliases:
            return racial_trait.get(race, None)