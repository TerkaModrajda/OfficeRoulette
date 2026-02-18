import json
import random

# Load countries
with open('countries.json', 'r', encoding='utf-8') as f:
    countries = json.load(f)

# Regional Drink Defaults (Mix of Cocktails & Specifics)
regional_drinks = {
    "Europe": {
        "alko": [
            {"name": "Aperol Spritz", "desc": "3 díly Prosecca, 2 díly Aperolu, 1 díl sody, led a pomeranč.", "type": "alko"},
            {"name": "Gin & Tonic (Evropský styl)", "desc": "Prémiový gin, řemeslný tonic, rozmarýn a jalovec.", "type": "alko"},
            {"name": "Hugo Spritz", "desc": "Prosecco, bezový sirup, máta, limetka a soda.", "type": "alko"}
        ],
        "nealko": {"name": "Domácí limonáda", "desc": "Sezónní ovoce (jahody/okurka), máta, soda.", "type": "nealko"}
    },
    "Asia": {
        "alko": [
            {"name": "Sake Bomb", "desc": "Shot sake vhozený do sklenice japonského piva.", "type": "alko"},
            {"name": "Singapore Sling", "desc": "Gin, třešňový likér, Cointreau, benediktinka, ananas a limetka.", "type": "alko"},
            {"name": "Lychee Martini", "desc": "Vodka, liči sirup/šťáva, vermut.", "type": "alko"}
        ],
        "nealko": {"name": "Mango Lassi", "desc": "Hustý jogurtový nápoj s mangem a kardamomem.", "type": "nealko"}
    },
    "Africa": {
        "alko": [
            {"name": "Dawa", "desc": "Vodka, med, limetka a drcený led (keňská klasika).", "type": "alko"},
            {"name": "Amarula on Ice", "desc": "Smetanový likér z ovoce marula na ledu.", "type": "alko"},
            {"name": "Chapman", "desc": "Rum/Gin, Angostura bitters, Fanta, Sprite a okurka.", "type": "alko"}
        ],
        "nealko": {"name": "Bissap", "desc": "Ibiškový čaj s mátou a vanilkou, podávaný ledově vychlazený.", "type": "nealko"}
    },
    "Americas": { # Latin America focus
        "alko": [
            {"name": "Mojito", "desc": "Bílý rum, čerstvá máta, limetka, cukr a soda.", "type": "alko"},
            {"name": "Margarita", "desc": "Tequila, Cointreau, limetková šťáva, sůl na okraji.", "type": "alko"},
            {"name": "Caipirinha", "desc": "Cachaça, drcená limetka a cukr.", "type": "alko"}
        ],
        "nealko": {"name": "Agua Fresca", "desc": "Mixované ovoce (meloun/ananas) s vodou a limetkou.", "type": "nealko"}
    },
    "Oceania": {
        "alko": [
            {"name": "Espresso Martini", "desc": "Vodka, kávový likér a espresso (australský hit).", "type": "alko"},
            {"name": "Pavlova Punch", "desc": "Šumivé víno s jahodami a kiwi sirupem.", "type": "alko"},
            {"name": "Lemon Lime & Bitters (Alko verze)", "desc": "Vodka, citronová limonáda, limetka a Angostura.", "type": "alko"}
        ],
        "nealko": {"name": "Lemon Lime & Bitters", "desc": "Limonáda, limetkový kordial a kapka Angostury (nealko ikona).", "type": "nealko"}
    }
}

# Override for North America specifically
north_america_drinks = {
    "alko": [
        {"name": "Old Fashioned", "desc": "Bourbon/Rye whiskey, cukr, Angostura bitters, pomerančová kůra.", "type": "alko"},
        {"name": "Cosmopolitan", "desc": "Vodka, Cointreau, brusinkový džus, limetka.", "type": "alko"},
        {"name": "Manhattan", "desc": "Whisky, sladký vermut, bitters, třešeň.", "type": "alko"}
    ],
    "nealko": {"name": "Arnold Palmer", "desc": "Půl na půl ledový čaj a citronáda.", "type": "nealko"}
}

# Specific Overrides for problematic/generic countries
specific_overrides = {
    "IOT": { # British Indian Ocean Territory
        "drinks": [
            {"name": "Gin & Tonic (Navy Strength)", "desc": "Silný gin, kvalitní tonic a plátek citronu (tradiční námořnický).", "type": "alko"},
            {"name": "Pimm's Cup", "desc": "Pimm's No. 1, limonáda, okurka, jahody, máta - britská klasika v tropech.", "type": "alko"},
            {"name": "Dark 'n' Stormy", "desc": "Tmavý rum a zázvorové pivo (oblíbené na základnách).", "type": "alko"},
            {"name": "Iced Earl Grey", "desc": "Černý čaj s bergamotem na ledu s citronem.", "type": "nealko"}
        ]
    },
    "CZE": {
        "drinks": [
            {"name": "Beton", "desc": "Becherovka s tonicem a citronem.", "type": "alko"},
            {"name": "Bavorák (Fernet Citrus & Tonic)", "desc": "Fernet Citrus, tonic, led.", "type": "alko"},
            {"name": "Tuzemák s Colou", "desc": "Tradiční český 'rum' s kolou a citronem.", "type": "alko"},
            {"name": "Kofola", "desc": "Točená bylinná limonáda s plátkem citronu.", "type": "nealko"}
        ]
    }
}

dry_countries = ["AFG", "IRN", "SAU", "KWT", "SOM", "MRT", "LBY", "YEM", "SDN"]

def get_drinks_for_country(country):
    code = country.get('cca3', '')
    region = country.get('region', 'Europe')
    subregion = country.get('subregion', '')
    
    # 1. Check Specific Override
    if code in specific_overrides:
        return specific_overrides[code]['drinks']
    
    # 2. Start with Region Defaults
    if region == "Americas" and "North" in subregion:
        base = north_america_drinks
    else:
        base = regional_drinks.get(region, regional_drinks['Europe'])

    # 3. Handle Dry Countries
    if code in dry_countries:
        # Create 4 nealko drinks based on existing or generic
        existing = country.get('gastronomy', {}).get('drinks', [])
        default_nealko = [
            {"name": "Mátový čaj", "desc": "Čerstvý čaj s hromadou cukru.", "type": "nealko"},
            {"name": "Čerstvá ovocná šťáva", "desc": "Granátové jablko nebo pomeranč.", "type": "nealko"},
            {"name": "Jogurtový nápoj (Ayran/Lassi)", "desc": "Osvěžující slaný jogurt.", "type": "nealko"},
            {"name": "Kořeněná káva", "desc": "Silná káva s kardamomem.", "type": "nealko"}
        ]
        # Merge existing into default to ensure 4
        final_list = existing + [d for d in default_nealko if d['name'] not in [e['name'] for e in existing]]
        return final_list[:4] # Return top 4
        
    # 4. Standard Case: Merge existing specific data with defaults to get 3 alko + 1 nealko
    current_drinks = country.get('gastronomy', {}).get('drinks', [])
    
    # Analyze current drinks (ensure they are dicts)
    current_alko = [d for d in current_drinks if isinstance(d, dict) and d.get('type') == 'alko']
    current_nealko = [d for d in current_drinks if isinstance(d, dict) and d.get('type') == 'nealko']
    
    final_alko_list = current_alko[:]
    
    # Fill Alko (Need 3)
    defaults_alko = base['alko']
    for d in defaults_alko:
        if len(final_alko_list) >= 3:
            break
        # Check for duplicates by name
        if not any(existing['name'] == d['name'] for existing in final_alko_list):
            final_alko_list.append(d)
    
    final_nealko_list = current_nealko[:]
    
    # Fill Nealko (Need 1)
    if len(final_nealko_list) == 0:
        if isinstance(base['nealko'], list):
             final_nealko_list.append(base['nealko'][0])
        else:
             final_nealko_list.append(base['nealko'])
        
    # Combine
    final_combined = final_alko_list + final_nealko_list
    
    return final_combined[:4] # Return exact 4 items

# Process all countries lists
print("Updating drinks...")
count = 0
for c in countries:
    if 'gastronomy' not in c:
        c['gastronomy'] = {}
    
    # Logic to update
    c['gastronomy']['drinks'] = get_drinks_for_country(c)
    count += 1

# Save back
with open('countries.json', 'w', encoding='utf-8') as f:
    json.dump(countries, f, indent=4, ensure_ascii=False)

print(f"Updated drinks for {count} countries.")
