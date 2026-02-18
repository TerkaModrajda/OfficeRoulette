
import json

# Data for missing countries
new_data = {
    "SVK": {
        "culture": {
            "etiquette": "Podobné jako v ČR. Pohostinnost, borovička na uvítanou.",
            "festivals": "Vánoce (Kapustnica), Velikonoce (Šibačka), Vinobraní.",
            "decor": "Modrotisk, črpáky, výšivky s geometrickými vzory, dřevěnice.",
            "music": "Elán, Horkýže Slíže, Miro Žbirka, lidová hudba (fujara)",
            "palette": ["#4682B4", "#228B22", "#FFFFFF"], # Tatry modrá, Les, Ovčí rouno
            "clothing": "Kroje (Detva, Čičmany), valaška, klobouk.",
            "instrument": "Fujara",
            "artists": ["Miro Žbirka", "Elán", "Marika Gombitová", "Rytmus"]
        },
        "gastronomy": {
            "focus": "Brambory, ovčí sýr, zelí.",
            "dishes": [
                {"name": "Bryndzové halušky", "recipe": "Bramborové noky s ovčím sýrem a slaninou."},
                {"name": "Kapustnica", "recipe": "Zelná polévka s uzeným masem, klobásou a houbami."},
                {"name": "Lokše", "recipe": "Bramborové placky maštěné sádlem."}
            ],
            "alcohol": "Borovička, Tatratea, Slivovice",
            "drinks": [
                {"name": "Žinčica", "desc": "Nápoj z ovčího mléka (vedlejší produkt výroby sýra).", "type": "nealko"},
                {"name": "Kofola", "desc": "Tradiční bylinková cola.", "type": "nealko"}
            ]
        }
    },
    "HUN": {
        "culture": {
            "etiquette": "Ťukání pivem je historicky nevhodné (ale dnes už méně). Silná národní hrdost.",
            "festivals": "Busójárás (masopust v maskách), Sziget Festival, svátek sv. Štěpána.",
            "decor": "Výšivky (Kalocsa), červená paprika, keramika Zsolnay.",
            "music": "Franz Liszt, lidová cikánská hudba, Omega (Gyöngyhajú lány)",
            "palette": ["#477050", "#CE2939", "#FFFFFF"], # Paprika Red, Green, White
            "clothing": "Kroje s bohatou výšivkou, husarské uniformy.",
            "instrument": "Cymbal (Cimbál)",
            "artists": ["Franz Liszt", "Béla Bartók", "Omega"]
        },
        "gastronomy": {
            "focus": "Paprika, maso, guláš.",
            "dishes": [
                {"name": "Gulyás", "recipe": "Polévka/guláš s hovězím, paprikou a brambory."},
                {"name": "Lángos", "recipe": "Smažené kynuté těsto s česnekem, sýrem a smetanou."},
                {"name": "Hortobágyi palacsinta", "recipe": "Palačinka plněná masem, přelitá paprikovou omáčkou."}
            ],
            "alcohol": "Tokajské víno, Pálinka, Unicum",
            "drinks": [
                {"name": "Fröccs", "desc": "Vinný střik (víno se sodovkou).", "type": "alko"}
            ]
        }
    },
    "UKR": {
        "culture": {
            "etiquette": "Pohostinnost, úcta ke starším, zouvání bot. Přípitek je důležitý.",
            "festivals": "Vánoce (Kalada), Velikonoce (Pysanka - barvení vajíček), Ivana Kupala.",
            "decor": "Vyšívanka (tradiční košile), motivy slunečnic, pšenice, modro-žlutá.",
            "music": "Ruslana, Okean Elzy, Kalush Orchestra",
            "palette": ["#FFD700", "#0057B7", "#000000"], # Wheat, Sky Blue, Soil
            "clothing": "Vyšívanka, věneček s pentlemi (vinok).",
            "instrument": "Bandura",
            "artists": ["Taras Ševčenko (básník)", "Jamala", "Verka Serduchka"]
        },
        "gastronomy": {
            "focus": "Červená řepa, zelí, těsto, smetana.",
            "dishes": [
                {"name": "Boršč", "recipe": "Polévka z červené řepy, zelí, masa a smetany."},
                {"name": "Varenyky", "recipe": "Taštičky plněné brambory, tvarohem nebo višněmi."},
                {"name": "Holubci", "recipe": "Zelné závitky plněné mletým masem a rýží."}
            ],
            "alcohol": "Horilka (Vodka s medem a pepřem)",
            "drinks": [
                {"name": "Uzvar", "desc": "Kompot ze sušeného ovoce.", "type": "nealko"},
                {"name": "Kvas", "desc": "Fermentovaný nápoj z chleba.", "type": "nealko"}
            ]
        }
    },
    "HRV": {
        "culture": {
            "etiquette": "Káva je rituál na hodiny. 'Fjaka' (stav mysli, nicnedělání u moře).",
            "festivals": "Dubrovnické letní hry, Sinjska Alka (rytířské hry).",
            "decor": "Červeno-bílá šachovnice, levandule, kamenné domy, kravata (vynalezli ji).",
            "music": "Oliver Dragojevič, Severina, 2Cellos",
            "palette": ["#FF0000", "#FFFFFF", "#003399"], # Checkerboard Red/White, Adriatic Blue
            "clothing": "Kroje, kravata.",
            "instrument": "Tamburica",
            "artists": ["Oliver Dragojević", "Gibonni", "Maksim Mrvica"]
        },
        "gastronomy": {
            "focus": "Mořské plody, jehněčí, olivový olej.",
            "dishes": [
                {"name": "Čevabčiči", "recipe": "Grilované válečky z mletého masa."},
                {"name": "Pašticada", "recipe": "Dušené hovězí ve švestkové omáčce s gnocchi."},
                {"name": "Crni rižot", "recipe": "Rizoto se sépiovým inkoustem a mořskými plody."}
            ],
            "alcohol": "Rakija (Travarica), Pelinkovac, Vína (Plavac Mali)",
            "drinks": [
                {"name": "Gemist", "desc": "Bílé víno s minerálkou.", "type": "alko"}
            ]
        }
    },
    "SVN": {
        "culture": {
            "etiquette": "Láska k přírodě a sportu. Dochvilnost. Skromnost.",
            "festivals": "Kurentovanje (masopustní průvod v maskách).",
            "decor": "Srdce z perníku (Lects), lipové dřevo, draci (Ljubljana).",
            "music": "Avsenik Brothers (polka), Laibach, Joker Out",
            "palette": ["#FFFFFF", "#0033CC", "#FF0000"], # Triglav White, Blue, Red
            "clothing": "Alpský styl, kroj.",
            "instrument": "Harmonika",
            "artists": ["Slavko Avsenik", "Melania Trump (rodáčka)"]
        },
        "gastronomy": {
            "focus": "Klobásy, dezerty, víno.",
            "dishes": [
                {"name": "Kranjska klobasa", "recipe": "Tradiční uzenina s křenem a chlebem."},
                {"name": "Potica", "recipe": "Zavinutý kynutý koláč s ořechy/mákem."},
                {"name": "Prekmurska gibanica", "recipe": "Vrstvený koláč s mákem, tvarohem, ořechy a jablky."}
            ],
            "alcohol": "Víno, Borovničke",
            "drinks": [
                {"name": "Cockta", "desc": "Bylinková limonáda s šípkem.", "type": "nealko"}
            ]
        }
    },
     "BGR": {
        "culture": {
            "etiquette": "Kývání hlavou znamená 'ne' a vrtění 'ano'.",
            "festivals": "Rose Festival (Kazanlak), Kukeri (masky).",
            "decor": "Růže, Martenitsa (červeno-bílé nItky), pravoslavné ikony.",
            "music": "Lidové sbory (Le Mystère des Voix Bulgares), Azis",
            "palette": ["#00966E", "#D62612", "#FFFFFF"], # Green, Red, White
            "clothing": "Kroje s bohatou výšivkou.",
            "instrument": "Gajda (Dudy)",
            "artists": ["Christo (umělec)", "Nina Dobrev (herečka)"]
        },
        "gastronomy": {
            "focus": "Zelenina, jogurt, sýr.",
            "dishes": [
                {"name": "Šopska salát", "recipe": "Paprika, okurka, rajče, cibule a strouhaný sýr sirene."},
                {"name": "Banitsa", "recipe": "Listové těsto plněné sýrem a vejci."},
                {"name": "Tarator", "recipe": "Studená polévka z jogurtu, okurky a česneku."}
            ],
            "alcohol": "Rakia, Víno",
            "drinks": [
                {"name": "Ayran", "desc": "Slaný jogurtový nápoj.", "type": "nealko"}
            ]
        }
    },
      "ROU": {
        "culture": {
            "etiquette": "Pohostinnost. Respekt ke starším. Silná folklórní tradice.",
            "festivals": "Martisor (příchod jara), Velikonoce.",
            "decor": "Koberce, malovaná vajíčka, dřevo, Dracula motivy.",
            "music": "Gheorghe Zamfir (Panova flétna), Inna, O-Zone (Dragostea Din Tei)",
            "palette": ["#002B7F", "#FCD116", "#CE1126"], # Blue, Yellow, Red
            "clothing": "Ie (tradiční vyšívaná blůza).",
            "instrument": "Panova flétna (Nai)",
            "artists": ["Constantin Brancusi", "Enescu"]
        },
        "gastronomy": {
            "focus": "Maso, kukuřice, česnek.",
            "dishes": [
                {"name": "Sarmale", "recipe": "Zelné závitky s mletým masem a rýží, podávané s mamaligou."},
                {"name": "Mămăligă", "recipe": "Kukuřičná kaše (polenta), často se sýrem a smetanou."},
                {"name": "Mici", "recipe": "Grilované válečky z mletého masa bez střívka."}
            ],
            "alcohol": "Tuica (švestková pálenka), Víno",
            "drinks": [
                {"name": "Socată", "desc": "Limonáda z květů černého bezu.", "type": "nealko"}
            ]
        }
    }
}

try:
    with open('countries.json', 'r', encoding='utf-8') as f:
        countries = json.load(f)

    count = 0
    for country in countries:
        cca3 = country.get('cca3')
        if cca3 in new_data:
            print(f"Updating {cca3}...")
            # Update culture
            if 'culture' not in country:
                country['culture'] = {}
            country['culture'].update(new_data[cca3]['culture'])
            
            # Update gastronomy
            if 'gastronomy' not in country:
                country['gastronomy'] = {}
            country['gastronomy'].update(new_data[cca3]['gastronomy'])
            count += 1

    with open('countries.json', 'w', encoding='utf-8') as f:
        json.dump(countries, f, ensure_ascii=False, indent=2)

    print(f"Successfully updated {count} countries.")

except Exception as e:
    print(f"Error: {e}")
