# Dictionary of SPECIFIC cultural drinks for Baltics & Eastern Europe
# Replacing generic "Vodka/Gin" with real local traditions

SPECIFIC_UPDATES = {
    # --- POBALTÍ ---
    "LTU": { # Litva
        "flavors": "Med, Bylinky (999), Kmín",
        "drinks": [
            {"name": "Midus (Medovina)", "desc": "Nejstarší litevský alkohol z medu, bylin a vody.", "type": "alko"},
            {"name": "999 (Trejos Devynerios)", "desc": "Bylinný likér z 27 bylin (9+9+9), pije se čistý nebo s džusem.", "type": "alko"},
            {"name": "Švyturys (Pivo)", "desc": "Tradiční litevský ležák, velmi populární.", "type": "alko"},
            {"name": "Gira (Kvass)", "desc": "Fermentovaný nápoj z tmavého žitného chleba.", "type": "nealko"}
        ]
    },
    "LVA": { # Lotyšsko
        "flavors": "Byliny (Balzám), Bříza, Brusinky",
        "drinks": [
            {"name": "Rīgas Melnais balzams", "desc": "Legendární hořký bylinný likér (45%), černý jako uhel.", "type": "alko"},
            {"name": "Black Balsam & Currant", "desc": "Horký nápoj z balzámu a rybízového džusu.", "type": "alko"},
            {"name": "Aldaris Pivo", "desc": "Místní světlý ležák.", "type": "alko"},
            {"name": "Březová šťáva", "desc": "Čerstvá míza z bříz (sbírá se na jaře).", "type": "nealko"}
        ]
    },
    "EST": { # Estonsko
        "flavors": "Jalovec, Rum (Vana Tallinn), Lesní plody",
        "drinks": [
            {"name": "Vana Tallinn", "desc": "Ikonický rumový likér s citrusy a vanilkou.", "type": "alko"},
            {"name": "Vana Tallinn Coffee", "desc": "Horká káva s likérem Vana Tallinn a šlehačkou.", "type": "alko"},
            {"name": "Saku Pivo", "desc": "Nejstarší estonský pivovar.", "type": "alko"},
            {"name": "Kama", "desc": "Nápoj z kysaného mléka a speciální moučné směsi (kama).", "type": "nealko"}
        ]
    },
    
    # --- SEVERSKÉ ZEMĚ (Doplnění specifik) ---
    "FIN": { # Finsko
        "flavors": "Lékořice (Salmiakki), Brusinky, Vodka",
        "drinks": [
            {"name": "Salmiakki Koskenkorva", "desc": "Vodka s příchutí slané lékořice (černá barva).", "type": "alko"},
            {"name": "Lonkero (Long Drink)", "desc": "Gin s grepovou limonádou (vynález pro OH 1952).", "type": "alko"},
            {"name": "Finlandia Vodka", "desc": "Čistá 'vodka' z ječmene a ledovcové vody.", "type": "alko"},
            {"name": "Glögi", "desc": "Finský svařák s mandlemi a rozinkami (často nealko).", "type": "nealko"}
        ]
    },
    "SWE": { # Švédsko
        "flavors": "Bezový květ, Káva, Punč",
        "drinks": [
            {"name": "Brännvin (Snaps)", "desc": "Kořeněná pálenka, pije se při jídle se zpěvem.", "type": "alko"},
            {"name": "Svensk Punsch", "desc": "Sladký likér z araku, pije se horký k hrachové polévce.", "type": "alko"},
            {"name": "Cider (Rekorderlig)", "desc": "Sladký švédský cider (jahoda-limetka).", "type": "alko"},
            {"name": "Julmust", "desc": "Kořeněná vánoční limonáda (pije se víc než Cola).", "type": "nealko"}
        ]
    },
    "DNK": { # Dánsko
        "flavors": "Kmín, Třešně, Pivo",
        "drinks": [
            {"name": "Akvavit", "desc": "Kmínová pálenka, podává se ledově vychlazená.", "type": "alko"},
            {"name": "Carlsberg/Tuborg", "desc": "Světlý ležák, národní ikona.", "type": "alko"},
            {"name": "Cherry Heering", "desc": "Třešňový likér (základ koktejlu Singapore Sling).", "type": "alko"},
            {"name": "Hyldeblomstsaft", "desc": "Šťáva z bezového květu.", "type": "nealko"}
        ]
    },

    # --- VÝCHODNÍ EVROPA (Upřesnění) ---
    "UKR": { # Ukrajina
        "flavors": "Med, Křen, Višně",
        "drinks": [
            {"name": "Horilka s percem", "desc": "Vodka s medem a chilli papričkou.", "type": "alko"},
            {"name": "Višňovka (Vyshniaka)", "desc": "Domácí likér z višní.", "type": "alko"},
            {"name": "Obolon", "desc": "Známé ukrajinské pivo.", "type": "alko"},
            {"name": "Uzvar", "desc": "Nápoj ze sušeného ovoce (hrušky, jablka, švestky).", "type": "nealko"}
        ]
    },
    "BLR": { # Bělorusko
        "flavors": "Bříza, Brusinky, Žito",
        "drinks": [
            {"name": "Krambambula", "desc": "Teplý nápoj z vodky/ginu, medu a koření.", "type": "alko"},
            {"name": "Zubrovka", "desc": "Vodka s bizoní trávou.", "type": "alko"},
            {"name": "Samogon", "desc": "Domácí pálenka (tradiční na venkově).", "type": "alko"},
            {"name": "Byaroza (Březová voda)", "desc": "Šťáva z břízy, velmi populární.", "type": "nealko"}
        ]
    },
     "MDA": { # Moldavsko
        "flavors": "Hroznové víno, Ořechy",
        "drinks": [
            {"name": "Moldavské víno (Fetească)", "desc": "Červené nebo bílé víno světové kvality.", "type": "alko"},
            {"name": "Divin", "desc": "Moldavské brandy (koňak).", "type": "alko"},
            {"name": "Izvar", "desc": "Svařené víno s medem a pepřem.", "type": "alko"},
            {"name": "Kompot z kdoulí", "desc": "Sladký ovocný vývar.", "type": "nealko"}
        ]
    },
    "ROU": { # Rumunsko
        "flavors": "Švestky (Tuica), Višně",
        "drinks": [
            {"name": "Țuică", "desc": "Silná švestková pálenka (50%+), pije se před jídlem.", "type": "alko"},
            {"name": "Pălincă", "desc": "Dvakrát destilovaná pálenka z ovoce.", "type": "alko"},
            {"name": "Visinată", "desc": "Višňový likér.", "type": "alko"},
            {"name": "Socată", "desc": "Fermentovaný nápoj z bezového květu a citronu.", "type": "nealko"}
        ]
    },
    "BGR": { # Bulharsko
        "flavors": "Hrozny, Anýz (Mastika), Růže",
        "drinks": [
            {"name": "Rakia", "desc": "Ovocná pálenka (hrozny, švestky), národní nápoj.", "type": "alko"},
            {"name": "Mastika", "desc": "Anýzový likér, pije se s mátovým likérem (Menta) jako 'Mrak'.", "type": "alko"},
            {"name": "Mavrud", "desc": "Starobylá odrůda červeného vína.", "type": "alko"},
            {"name": "Ayran", "desc": "Slaný jogurtový nápoj ředěný vodou.", "type": "nealko"}
        ]
    }
}

import json

with open("countries.json", "r", encoding="utf-8") as f:
    data = json.load(f)

count = 0
for country in data:
    cca3 = country.get("cca3")
    
    if cca3 in SPECIFIC_UPDATES:
        new_data = SPECIFIC_UPDATES[cca3]
        
        if "gastronomy" not in country:
            country["gastronomy"] = {}
        
        country["gastronomy"]["alcohol"] = new_data["flavors"]
        country["gastronomy"]["drinks"] = new_data["drinks"]
        count += 1
        print(f"Updating {cca3}: {new_data['drinks'][0]['name']}")

with open("countries.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"DONE: Updated distinct drinks for {count} countries (Baltics/North/East).")
