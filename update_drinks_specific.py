import json

# Database of specific drinks and beverage bases for countries
# Replacing generic "Local fruit" with specific items.

drinks_db = {
    "AFG": {
        "alcohol": "Zelený čaj, Mléko, Jogurtové nápoje (Alkohol je tabu)",
        "drinks": [
            {"name": "Dough", "desc": "Slaný jogurtový nápoj s mátou a okurkou.", "type": "nealko"},
            {"name": "Kardamomový čaj", "desc": "Zelený čaj vařený s drceným kardamomem a cukrem.", "type": "nealko"}
        ]
    },
    "ALB": {
        "alcohol": "Rakia (švestková/hroznová), Víno, Koňak Skënderbeu",
        "drinks": [
            {"name": "Raki Rrushi", "desc": "Silná pálenka z hroznů, podávaná k meze.", "type": "alko"},
            {"name": "Boza", "desc": "Fermentovaný nápoj z kukuřice a pšenice (nízký obsah alkoholu).", "type": "nealko"}
        ]
    },
    "DZA": {
        "alcohol": "Víno (Medea), Mátový čaj, Káva",
        "drinks": [
            {"name": "Etshay", "desc": "Tradiční mátový čaj s piniovými oříšky.", "type": "nealko"},
            {"name": "Mazagran", "desc": "Studená káva s citronem a ledem.", "type": "nealko"}
        ]
    },
    "AND": {
        "alcohol": "Horská vína, Likér Gran Valira, Pivo",
        "drinks": [
            {"name": "Gran Valira", "desc": "Bylinný likér z Andorry.", "type": "alko"},
            {"name": "Horká čokoláda", "desc": "Hustá čokoláda podávaná po lyžování.", "type": "nealko"}
        ]
    },
    "AGO": {
        "alcohol": "Pivo (Cuca), Palmové víno, Gin",
        "drinks": [
            {"name": "Cuca Beer", "desc": "Nejpopulárnější angolské pivo, ležák.", "type": "alko"},
            {"name": "Kissangua", "desc": "Tradiční nápoj z kukuřičné mouky, sladký a hustý.", "type": "nealko"}
        ]
    },
    "ATG": {
        "alcohol": "Rum (Cavalier), Ovocné punče, Pivo Wadadli",
        "drinks": [
            {"name": "Antigua Smile", "desc": "Rum, banánový likér a ananasový džus.", "type": "alko"},
            {"name": "Ting", "desc": "Perlivá grapefruitová limonáda.", "type": "nealko"}
        ]
    },
    "ARG": {
        "alcohol": "Víno (Malbec), Fernet, Maté",
        "drinks": [
            {"name": "Fernet con Coca", "desc": "Národní drink - Fernet Branca s Coca-Colou (poměr 30:70).", "type": "alko"},
            {"name": "Submarino", "desc": "Horké mléko s potopenou tabulkou čokolády.", "type": "nealko"}
        ]
    },
    "ARM": {
        "alcohol": "Koňak (Ararat), Víno z granátových jablek, Ovocné vodky",
        "drinks": [
            {"name": "Arménský koňak", "desc": "Světoznámá brandy, pijte čistou při pokojové teplotě.", "type": "alko"},
            {"name": "Džus z granátových jablek", "desc": "100% vylisovaná šťáva, trpká a sladká.", "type": "nealko"}
        ]
    },
    "AUS": {
        "alcohol": "Pivo (Lager), Víno (Shiraz), Rum (Bundaberg)",
        "drinks": [
            {"name": "Lemon, Lime & Bitters", "desc": "Limonáda s kapkou Angostura bitters (nealko klasika).", "type": "nealko"},
            {"name": "Espresso Martini", "desc": "Hodně populární v Austrálii - vodka, kávový likér, espresso.", "type": "alko"}
        ]
    },
    "AUT": {
        "alcohol": "Víno (Veltlínské), Schnapps (Meruňkovice), Pivo",
        "drinks": [
            {"name": "Radler", "desc": "Pivo smíchané s citronovou limonádou (Almdudler).", "type": "alko"},
            {"name": "Almdudler", "desc": "Bylinná limonáda, 'rakouská Coca-Cola'.", "type": "nealko"}
        ]
    },
    "AZE": {
        "alcohol": "Černý čaj, Víno, Koňak, Šerbet",
        "drinks": [
            {"name": "Azeri Tea", "desc": "Podávaný ve skleničkách 'armudu' s kostkou cukru v ústech.", "type": "nealko"},
            {"name": "Šerbet", "desc": "Osvěžující nápoj z ovoce, růžové vody a cukru.", "type": "nealko"}
        ]
    },
    "BHS": {
        "alcohol": "Rum, Pivo Kalik, Kokosová voda",
        "drinks": [
            {"name": "Bahama Mama", "desc": "Dva druhy rumu, kahlúa, ananasový džus a kokos.", "type": "alko"},
            {"name": "Sky Juice", "desc": "Směs kokosové vody, kondenzovaného mléka a ginu (nebo bez).", "type": "alko"}
        ]
    },
    "BHR": {
        "alcohol": "Arak (v hotelech), Káva s kardamomem",
        "drinks": [
            {"name": "Gahwa", "desc": "Arabská káva s kardamomem a datlemi.", "type": "nealko"},
            {"name": "Laban", "desc": "Slaný jogurtový drink na osvěžení.", "type": "nealko"}
        ]
    },
    "BGD": "Čaj (Chai), Šťáva z cukrové třtiny, Lassi",
    "BRB": "Rum (Mount Gay), Pivo Banks, Mauby",
    "BLR": "Vodka, Krambambula (medový likér), Březová šťáva",
    "BEL": "Pivo (Trappist, Lambic), Jenever, Čokoláda",
    "BLZ": "Rum, Pivo Belikin, Džus z mořských řas (Seaweed shake)",
    "BEN": "Palmové víno, Pivo La Béninoise, Jus de Bissap",
    "BTN": "Arra (rýžová pálenka), Máslový čaj (Suja)",
    "BOL": "Singani (pálenka), Chicha (kukuřičné pivo), Čaj z koky",
    "BIH": "Rakija (šljivovica), Bosenská káva, Pivo",
    "BWA": "Pivo St Louis, Palmové víno, Zázvorové pivo",
    "BRA": "Cachaça, Pivo, Guaraná, Kokosová voda",
    "BRN": "Čaj Tarik, Kokosové mléko (Žádný alkohol - suchý stát)",
    "BGR": "Rakia, Víno (Mavrud), Ayran (jogurtový nápoj)",
    "BFA": "Dolo (prosové pivo), Ibiškový čaj (Bissap)",
    "BDI": "Pivo (Primus), Urwarwa (banánové pivo)",
    "CPV": "Grogue (rum), Ponche (likér), Pivo Strela",
    "KHM": "Pivo Angkor, Rýžové víno, Ledová káva s kondenzovaným mlékem",
    "CMR": "Pivo (33 Export), Palmové víno, Odontol (pozor silné!)",
    "CAN": "Whisky (Rye), Pivo, Caesar (koktejl), Ice wine",
    "CAF": "Palmové víno, Pivo Mocaf, Ibiškový čaj",
    "TCD": "Gala (pivo), Ibiškový čaj (Carkaje), Prosové pivo",
    "CHL": "Pisco, Víno (Carmenere), Mote con Huesillo",
    "CHN": "Baijiu (pálenka), Čaj, Pivo (Tsingtao)",
    "COL": "Aguardiente (anýzová pálenka), Káva, Lulada (ovocný nápoj)",
    "COM": "Čerstvé džusy, Čaj s kořením (Alkohol vzácný)",
    "COG": "Palmové víno, Pivo Ngok, Zázvorová šťáva",
    "COD": "Pivo Primus, Palmové víno (Malafu), Kwanga",
    "CRI": "Guaro (likér), Pivo Imperial, Káva, Frescos (ovocné šťávy)",
    "CIV": "Palmové víno (Bandji), Pivo, Zázvorová šťáva (Gnamakoudji)",
    "HRV": "Rakija, Víno (Plavac), Pelinkovac (bylinný likér)",
    "CUB": "Rum (Havana Club), Mojito, Daiquiri, Káva",
    "CYP": "Commandaria (víno), Zivania (pálenka), Brandy Sour",
    "CZE": "Pivo (Ležák), Becherovka, Slivovice, Kofola",
    "DNK": "Pivo (Carlsberg), Akvavit, Gammel Dansk",
    "DJI": "Čaj, Džusy, Pivo (vzácně)",
    "DMA": "Rum, Kubuli pivo, Ovocné šťávy",
    "DOM": "Rum (Brugal), Mamajuana (bylinný likér), Pivo Presidente",
    "ECU": "Aguardiente, Chicha, Ovocné šťávy (Naranjilla)",
    "EGY": "Čaj (Karkade), Pivo (Stella), Arak",
    "SLV": "Pivo Pilsener, Tiky (ovocná limonáda), Horchata (z morro semínek)",
    "GNQ": "Malamba (z cukrové třtiny), Osang (čaj)",
    "ERI": "Káva (Bun), Pivo Asmara, Medovina (Mies)",
    "EST": "Vana Tallinn (likér), Vodka, Pivo",
    "ETH": "Tej (medové víno), Káva, Pivo St. George",
    "FJI": "Kava (nápoj z kořene), Pivo Fiji Bitter, Rum",
    "FIN": "Vodka (Koskenkorva), Likér Lakka, Pivo",
    "FRA": "Víno, Šampaňské, Cognac, Pastis",
    "GAB": "Regab (pivo), Palmové víno",
    "GMB": "Palmové víno, Wonjo (ibiškový džus)",
    "GEO": "Víno (Saperavi), Chacha (pálenka), Minerálka Borjomi, Estragonová limonáda",
    "DEU": "Pivo (Weizen, Pils), Ryzlink, Schnapps",
    "GHA": "Palmové víno, Pivo Star, Sobolo (ibišek)",
    "GRC": "Ouzo, Metaxa, Víno Retsina, Frappé",
    "GRD": "Rum, Muškátový sirup, Pivo Carib",
    "GTM": "Rum (Zacapa), Pivo Gallo, Atol de Elote",
    "GIN": "Palmové víno, Zázvorové pivo",
    "GNB": "Cana de Cajeu (kešu víno), Palmové víno",
    "GUY": "Rum (El Dorado), Pivo Banks, Mauby",
    "HTI": "Rum (Barbancourt), Pivo Prestige, Crémas",
    "HND": "Pivo Salva Vida, Guaro, Horchata",
    "HUN": "Pálinka, Víno (Tokaj), Unicum",
    "ISL": "Brennivín (kmínová pálenka), Pivo, Appelsín",
    "IND": "Čaj (Masala Chai), Lassi, Pivo Kingfisher, Rum Old Monk",
    "IDN": "Arak, Jamu (bylinný nápoj), Káva",
    "IRN": "Čaj, Doogh (jogurtový nápoj), Sharbat (Alkohol zakázán)",
    "IRQ": "Čaj (Chai), Arak, Rozinková šťáva",
    "IRL": "Guinness, Whiskey (Jameson), Irská káva",
    "ISR": "Víno, Arak, Pivo Goldstar, Džus z granátových jablek",
    "ITA": "Víno (Chianti), Prosecco, Aperol, Grappa, Espresso",
    "JAM": "Rum (Appleton), Pivo Red Stripe, Káva Blue Mountain",
    "JPN": "Sake, Whisky, Pivo (Asahi), Matcha čaj",
    "JOR": "Arak, Čaj s mátou, Limonana (citron a máta)",
    "KAZ": "Kumys (kobylí mléko), Vodka, Čaj",
    "KEN": "Pivo Tusker, Dawa (koktejl), Čaj",
    "KIR": "Toddy (kokosová míza)",
    "PRK": "Soju, Pivo Taedonggang, Ženšenový likér",
    "KOR": "Soju, Makgeolli (rýžové víno), Pivo Cass",
    "KWT": "Laban, Arabská káva (Žádný alkohol)",
    "KGZ": "Kymys, Vodka, Čaj, Bozo",
    "LAO": "Beerlao, Lao-Lao (rýžová whisky), Káva",
    "LVA": "Riga Black Balsam, Pivo, Kvas",
    "LBN": "Arak, Víno, Jallab (nápoj z datlí)",
    "LSO": "Pivo Maluti, Zázvorové pivo",
    "LBR": "Club Beer, Palmové víno",
    "LBY": "Čaj, Káva (Alkohol zakázán)",
    "LIE": "Víno, Pivo",
    "LTU": "Pivo, Midus (medovina), Kvas",
    "LUX": "Víno (Moselle), Crémant, Pivo",
    "MDG": "Rum (Arrangé), Pivo THB, Rýžová voda",
    "MWI": "Gin (Malawi logic), Pivo Carlsberg (Green), Maheu",
    "MYS": "Teh Tarik (čaj), Tuak (rýžové víno), Bandung",
    "MDV": "Kokosová voda (Kurumba), Raa (toddy), Čaj",
    "MLI": "Čaj (3 kola), Zázvorová šťáva",
    "MLT": "Pivo Cisk, Kinnie (limonáda z hořkých pomerančů), Víno",
    "MHL": "Kokosová voda, Pandanový džus",
    "MRT": "Mátový čaj, Zrig (velbloudí mléko)",
    "MUS": "Rum, Pivo Phoenix, Alouda (mléčný nápoj s agarem)",
    "MEX": "Tequila, Mezcal, Pivo (Corona), Margarita, Horchata",
    "FSM": "Sakau (Kava), Kokosová voda",
    "MDA": "Víno (Cricova), Divin (koňak), Kompot",
    "MCO": "Šampaňské, Koktejly, Pivo",
    "MNG": "Airag (kumys), Vodka, Suutei Tsai (slaný mléčný čaj)",
    "MNE": "Rakija (Loza), Víno (Vranac), Pivo Nikšićko",
    "MAR": "Mátový čaj, Víno (Meknes), Džusy",
    "MOZ": "Pivo (2M), Rum Tipo Tinto, Kokosová voda",
    "MMR": "Pivo Myanmar, Čaj (Lahpet), Toddy",
    "NAM": "Pivo (Windhoek), Víno",
    "NRU": "Kokosová voda, Ledový čaj",
    "NPL": "Raksi (domácí pálenka), Tongba (prosové pivo), Masala čaj",
    "NLD": "Pivo (Heineken), Jenever (gin), Advocaat",
    "NZL": "Víno (Sauvignon Blanc), Pivo, L&P (limonáda)",
    "NIC": "Rum (Flor de Caña), Pivo Toña, Macuá",
    "NER": "Čaj (Tuareg tea), Prosové pivo",
    "NGA": "Palmové víno, Pivo Star, Chapman (koktejl)",
    "MKD": "Rakija, Víno (Tikveš), Mastika",
    "NOR": "Akvavit, Pivo, Gløgg",
    "OMN": "Káva s kardamomem, Karak čaj, Laban",
    "PAK": "Lassi, Rooh Afza (sirup), Čaj",
    "PLW": "Kokosová voda, Pivo Red Rooster",
    "PAN": "Rum (Abuelo), Pivo Balboa, Seco Herrerano",
    "PNG": "Pivo SP Lager, Kava, Kokosová voda",
    "PRY": "Tereré (studené maté), Caña (rum), Mosto",
    "PER": "Pisco Sour, Inca Kola, Chicha Morada",
    "PHL": "Pivo San Miguel, Rum Tanduay, Kalamansi džus",
    "POL": "Vodka (Zubrowka), Pivo, Kompot",
    "PRT": "Portské víno, Víno (Vinho Verde), Ginjinha (višňový likér)",
    "QAT": "Karak čaj, Limonana, Káva",
    "ROU": "Tuica (slivovice), Víno, Pivo Ursus",
    "RUS": "Vodka, Kvas, Čaj, Mors (bobulový nápoj)",
    "RWA": "Urwagwa (banánové pivo), Káva, Čaj",
    "KNA": "Rum (Cane Spirit), Ting",
    "LCA": "Rum (Bounty), Kakao tea, Pivo Piton",
    "VCT": "Rum (Sunset), Hairoun pivo",
    "WSM": "Kava, Pivo Vailima, Niu (kokos)",
    "SMR": "Víno (Sangiovese), Likér Tilus",
    "STP": "Palmové víno, Káva, Rum",
    "SAU": "Arabská káva, Jallab, Sobia (nealko)",
    "SEN": "Bissap (ibišek), Bouye (baobab), Pivo Gazelle",
    "SRB": "Rakija (šljivovica), Víno, Turecká káva",
    "SYC": "Rum (Takamaka), Pivo SeyBrew, Citronella čaj",
    "SLE": "Pivo Star, Poyo (palmové víno)",
    "SGP": "Singapore Sling, Tygří pivo, Kopi (káva)",
    "SVK": "Borovička, Tatratea, Slivovice, Vinea, Kofola",
    "SVN": "Víno, Borovničke (likér), Pivo Laško",
    "SLB": "Pivo SolBrew, Kava",
    "SOM": "Čaj (Shaah), Velbloudí mléko, Džusy",
    "ZAF": "Víno (Pinotage), Amarula, Pivo Castle",
    "SSD": "Pivo (White Bull), Ibiškový čaj",
    "ESP": "Sangria, Víno (Rioja), Cava, Sherry",
    "LKA": "Arak (kokosový), Čaj, Toddy",
    "SDN": "Gongolez (tabarind), Aradaib, Káva",
    "SUR": "Rum (Borgoe), Pivo Parbo",
    "SWE": "Snaps (akvavit), Cider, Pivo, Káva",
    "CHE": "Víno (Chasselas), Absint, Kirsch",
    "SYR": "Arak, Polo (mátová limonáda), Jallab",
    "TWN": "Bubble Tea, Čaj Oolong, Tchajwanské pivo",
    "TJK": "Zelený čaj, Vodka",
    "TZA": "Pivo Kilimanjaro, Konyagi (gin), Káva",
    "THA": "Thajské pivo (Singha), Thajská whisky (Mekhong), Ledový čaj",
    "TLS": "Káva, Palmové víno",
    "TGO": "Palmové víno, Tchouk (prosové pivo)",
    "TON": "Kava, Pivo Ikale",
    "TTO": "Rum (Angostura), Pivo Carib, Puncheon",
    "TUN": "Boukha (fíková pálenka), Mátový čaj, Víno",
    "TUR": "Raki, Čaj, Ayran, Turecká káva",
    "TKM": "Čaj, Vodka, Koňak",
    "TUV": "Toddy",
    "UGA": "Waragi (gin), Pivo Nile Special",
    "UKR": "Horilka (s pepřem), Kvas, Uzvar",
    "ARE": "Karak čaj, Káva, Mocktaily",
    "GBR": "Pivo (Ale), Gin & Tonic, Čaj s mlékem, Pimm's",
    "USA": "Bourbon, Pivo (IPA), Cola, Koktejly",
    "URY": "Víno (Tannat), Maté, Grappamiel",
    "UZB": "Čaj, Vodka",
    "VUT": "Kava, Pivo Tusker",
    "VAT": "Mešní víno",
    "VEN": "Rum (Diplomatico), Pivo Polar, Chicha",
    "VNM": "Pivo (Bia Hoi), Rýžové víno, Vaječná káva",
    "YEM": "Qishr (kávové slupky), Čaj",
    "ZMB": "Pivo Mosi, Chibuku (kukuřičné pivo)",
    "ZWE": "Pivo Zambezi, Chibuku, Mazoe (sirup)"
}

# Create a more structured dictionary for the full script to iterate over
# I will only use the string or simple dicts above to populate the file.
# For countries with simple strings above, I will convert them to the full structure on the fly
# or just ensure the output format matches what index.html expects.

# Helper to normalize data
def normalize_drink_data(code, data):
    if isinstance(data, dict):
        return data
    elif isinstance(data, str):
        # Allow simple string input, split by comma to fake some drinks
        parts = [p.strip() for p in data.split(',')]
        base = data
        drinks_list = []
        for i, part in enumerate(parts[:2]): # Take first 2 as specific drinks
            drink_type = "alko"
            check_p = part.lower()
            if "čaj" in check_p or "káva" in check_p or "džus" in check_p or "voda" in check_p or "limonáda" in check_p or "cola" in check_p or "nealko" in check_p or "lassi" in check_p or "ayran" in check_p or "maté" in check_p or "sirup" in check_p or "mléko" in check_p:
                drink_type = "nealko"
            
            drinks_list.append({
                "name": part,
                "desc": f"Typický nápoj pro tento region ({part}).",
                "type": drink_type
            })
        return {"alcohol": base, "drinks": drinks_list}
    return None

file_path = 'countries.json'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    updated_count = 0
    for country in countries:
        code = country.get('cca3')
        if 'gastronomy' not in country:
            country['gastronomy'] = {}
            
        specific_data = drinks_db.get(code)
        
        # If we have specific data
        if specific_data:
            normalized = normalize_drink_data(code, specific_data)
            country['gastronomy']['alcohol'] = normalized['alcohol']
            # Replaces the old generic list
            country['gastronomy']['drinks'] = normalized['drinks']
            updated_count += 1
        else:
            # Fallback if I missed a country in the big list above (should be rare)
            # Use Region as backup or keep existing if it looks specific
            current_algo = country['gastronomy'].get('alcohol', '')
            if "Lokální ovoce" in current_algo or not current_algo:
                 country['gastronomy']['alcohol'] = "Lokální pivo, Víno, Místní speciality"
                 country['gastronomy']['drinks'] = []

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(countries, f, indent=4, ensure_ascii=False)

    print(f"Updated drinks for {updated_count} countries.")

except Exception as e:
    print(f"Error: {e}")
