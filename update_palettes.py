
import json

# Define palettes and music updates for countries
# Note: The countries.json file now contains ALL countries of the world (generated via update_all_countries.py).
# This script is used to manually override/customize the palette and music for specific countries.
# If a country is not listed here, it will use the default data from countries.json (which might be generic).

country_data = {
    # Original 20 countries
    "CZE": {
        "palette": ["#E3DAC9", "#722F37", "#2D5A27"],  # Pivo, Víno, Les
        "music": "Bedřich Smetana - Vltava, Karel Gott, Kabát" 
    },
    "JPN": {
        "palette": ["#FFB7C5", "#F4F1EA", "#8B4513"],  # Sakura, Papír, Dřevo
        "music": "Joe Hisaishi (Ghibli), AKB48 (J-Pop), Wagakki Band"
    },
    "USA": {
        "palette": ["#B22234", "#3C3B6E", "#FFFFFF"],  # Stars & Stripes (Deep)
        "music": "Michael Jackson, Elvis Presley, Taylor Swift"
    },
    "MEX": {
        "palette": ["#FF00BF", "#00CCA3", "#FF6F00"],  # Mexican Pink, Turquoise, Marigold
        "music": "Mariachi Vargas, Selena, Luis Miguel"
    },
    "ITA": {
        "palette": ["#009246", "#F1F2F1", "#CE2B37"],  # Tricolore (Vibrant) + Terracotta
        "music": "Luciano Pavarotti, Andrea Bocelli, Måneskin"
    },
    "FRA": {
        "palette": ["#0055A4", "#EF4135", "#F5F5DC"],  # Tricolore + Cream/Beige
        "music": "Édith Piaf - La Vie en rose, Daft Punk, Stromae"
    },
    "ESP": {
        "palette": ["#AA151B", "#F1BF00", "#800020"],  # Red, Yellow, Sangria
        "music": "Gipsy Kings, Rosalía, Enrique Iglesias"
    },
    "THA": {
        "palette": ["#FFD700", "#800080", "#007B5E"],  # Gold, Royal Purple, Jungle Green
        "music": "Carabao (Thai Rock), Tata Young"
    },
    "IND": {
        "palette": ["#FF9933", "#138808", "#FF00CC"],  # Saffron, Green, Rani Pink
        "music": "A.R. Rahman (Jai Ho), Ravi Shankar, Punjabi MC"
    },
    "BRA": {
        "palette": ["#009C3B", "#FFDF00", "#002776"],  # Green, Yellow, Blue
        "music": "Antônio Carlos Jobim (Girl from Ipanema), Anitta, Sepultura"
    },
    "GRC": {
        "palette": ["#0D5EAF", "#FFFFFF", "#B5C7D3"],  # Aegean Blue, White, Stone
        "music": "Mikis Theodorakis (Zorba), Nana Mouskouri"
    },
    "AUS": {
        "palette": ["#FFCC00", "#00843D", "#C65C3B"],  # Green & Gold + Outback Red
        "music": "AC/DC, Kylie Minogue, Tame Impala"
    },
    "KEN": {
        "palette": ["#000000", "#922529", "#008C51"],  # Masai Red, Green, Black
        "music": "Sauti Sol, Fadhili William (Malaika)"
    },
    "MAR": {
        "palette": ["#C1272D", "#006233", "#D4AF37"],  # Red walls, Green tiles, Gold
        "music": "Saad Lamjarred, Nass El Ghiwane"
    },
    "DEU": {
        "palette": ["#DD0000", "#FFCE00", "#000000"],  # Black, Red, Gold
        "music": "Rammstein, Nena (99 Luftballons), Scorpions"
    },
    "VNM": {
        "palette": ["#DA251D", "#FFFF00", "#008080"],  # Flag Red n Yellow + Teal Water
        "music": "Sơn Tùng M-TP, Hoàng Thùy Linh"
    },
    "ARG": {
        "palette": ["#74ACDF", "#F6B40E", "#333333"],  # Sky Blue, Sun, Asphalt/Tango
        "music": "Astor Piazzolla (Libertango), Carlos Gardel, Soda Stereo"
    },
    "KOR": {
        "palette": ["#CD2E3A", "#0047A0", "#000000"],  # Taegeukgi Colors (Red/Blue/Black)
        "music": "BTS, BLACKPINK, PSY (Gangnam Style)"
    },
    "SWE": {
        "palette": ["#FECC00", "#006AA7", "#F0E68C"],  # Blue, Yellow, Light Wood
        "music": "ABBA (Dancing Queen), Avicii, Roxette"
    },
    "EGY": {
        "palette": ["#C59235", "#000000", "#0066CC"],  # Sand, Ancient Black, Nile Blue
        "music": "Amr Diab, Umm Kulthum"
    },
    
    # New 20 countries
    "GBR": {
        "palette": ["#012169", "#C8102E", "#FFFFFF"],  # Union Jack
        "music": "The Beatles, Queen, Adele"
    },
    "CAN": {
        "palette": ["#FF0000", "#FFFFFF", "#2F4F4F"],  # Maple Red, Snow, Pine Green
        "music": "Céline Dion, Justin Bieber, The Weeknd"
    },
    "CHN": {
        "palette": ["#DE2910", "#FFDE00", "#BC002D"],  # China Red, Emperor Yellow, Lacquer
        "music": "Teresa Teng, Jay Chou, Lang Lang"
    },
    "TUR": {
        "palette": ["#E30A17", "#FFFFFF", "#40E0D0"],  # Turkish Red, White, Turquoise
        "music": "Tarkan (Kiss Kiss), Sezen Aksu"
    },
    "NLD": {
        "palette": ["#FF9B00", "#21468B", "#AE1C28"],  # Orange, Delft Blue, Red
        "music": "Martin Garrix, Shocking Blue (Venus), André Rieu"
    },
    "ZAF": {
        "palette": ["#007749", "#FFB612", "#DE3831"],  # Flag Green, Gold, Red
        "music": "Miriam Makeba (Pata Pata), Die Antwoord, Master KG (Jerusalema)"
    },
    "COL": {
        "palette": ["#FCD116", "#003893", "#CE1126"],  # Tricolor
        "music": "Shakira, J Balvin, Carlos Vives"
    },
    "CHE": {
        "palette": ["#FF0000", "#FFFFFF", "#A52A2A"],  # Swiss Red, Snow, Alpine Wood
        "music": "DJ BoBo, Yello (Oh Yeah), Mani Matter"
    },
    "SAU": {
        "palette": ["#006C35", "#FFFFFF", "#D2B48C"],  # Saudi Green, White, Desert Sand
        "music": "Mohammed Abdu, Rashed Al-Majed"
    },
    "NZL": {
        "palette": ["#000000", "#FFFFFF", "#009933"],  # All Blacks, Silver Fern, Green
        "music": "Lorde, Crowded House, Katchafire"
    },
    "PER": {
        "palette": ["#D91023", "#FFFFFF", "#FFD700"],  # Peru Red, White, Inca Gold
        "music": "Yma Sumac, Susana Baca"
    },
    "IDN": {
        "palette": ["#FF0000", "#FFFFFF", "#009900"],  # Red, White, Tropical Green
        "music": "Anggun, Rich Brian, Rhoma Irama"
    },
    "IRL": {
        "palette": ["#169B62", "#FFFFFF", "#FF883E"],  # Flag Green, White, Orange
        "music": "U2, The Dubliners, Enya"
    },
    "POL": {
        "palette": ["#DC143C", "#FFFFFF", "#BABABA"],  # Crimson, White, Silver
        "music": "Fryderyk Chopin, sanah, Dawid Podsiadło"
    },
    "SGP": {
        "palette": ["#EF3340", "#FFFFFF", "#028482"],  # Red, White, Orchid Purple/Green
        "music": "JJ Lin, Stefanie Sun"
    },
    "AUT": {
        "palette": ["#ED2939", "#FFFFFF", "#BDB76B"],  # Red, White, Imperial Gold
        "music": "Falco (Rock Me Amadeus), Wolfgang Amadeus Mozart"
    },
    "BEL": {
        "palette": ["#000000", "#FDDA24", "#EF3340"],  # Black, Yellow, Red
        "music": "Stromae (Papaoutai), Technotronic"
    },
    "NOR": {
        "palette": ["#BA0C2F", "#00205B", "#FFFFFF"],  # Red, Blue, White + Snow
        "music": "A-ha (Take On Me), Kygo, Aurora"
    },
    "CHL": {
        "palette": ["#DA291C", "#FFFFFF", "#0039A6"],  # Red, White, Blue
        "music": "Los Jaivas, La Ley, Mon Laferte"
    },
    "PRT": {
        "palette": ["#046A38", "#DA291C", "#FFD700"],  # Green, Red, Gold
        "music": "Amália Rodrigues (Fado), Salvador Sobral"
    }
}

# --- Další země (Odemkněte a doplňte dle potřeby) ---
# Zde jsou předpřipravené šablony pro všechny ostatní země.
# Pokud chcete upravit paletu nebo hudbu pro konkrétní zemi, odkomentujte ji a vyplňte.

# country_data.update({
#     "AFG": {  # 🇦🇫 Afghánistán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Afghánistán"
#     },
#     "ALB": {  # 🇦🇱 Albánie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Albánie"
#     },
#     "DZA": {  # 🇩🇿 Alžírsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Alžírsko"
#     },
#     "ASM": {  # 🇦🇸 Americká Samoa
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Americká Samoa"
#     },
#     "VIR": {  # 🇻🇮 Americké Panenské ostrovy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Americké Panenské ostrovy"
#     },
#     "AND": {  # 🇦🇩 Andorra
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Andorra"
#     },
#     "AGO": {  # 🇦🇴 Angola
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Angola"
#     },
#     "AIA": {  # 🇦🇮 Anguilla
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Anguilla"
#     },
#     "ATG": {  # 🇦🇬 Antigua a Barbuda
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Antigua a Barbuda"
#     },
#     "ARE": {  # 🇦🇪 Arabské emiráty
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Arabské emiráty"
#     },
#     "ARM": {  # 🇦🇲 Arménie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Arménie"
#     },
#     "ABW": {  # 🇦🇼 Aruba
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Aruba"
#     },
#     "BHS": {  # 🇧🇸 Bahamy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Bahamy"
#     },
#     "BHR": {  # 🇧🇭 Bahrajn
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Bahrajn"
#     },
#     "BGD": {  # 🇧🇩 Bangladéš
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Bangladéš"
#     },
#     "BRB": {  # 🇧🇧 Barbados
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Barbados"
#     },
#     "BLZ": {  # 🇧🇿 Belize
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Belize"
#     },
#     "BEN": {  # 🇧🇯 Benin
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Benin"
#     },
#     "BMU": {  # 🇧🇲 Bermudy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Bermudy"
#     },
#     "BTN": {  # 🇧🇹 Bhútán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Bhútán"
#     },
#     "BOL": {  # 🇧🇴 Bolívie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Bolívie"
#     },
#     "BIH": {  # 🇧🇦 Bosna a Hercegovina
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Bosna a Hercegovina"
#     },
#     "BWA": {  # 🇧🇼 Botswana
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Botswana"
#     },
#     "VGB": {  # 🇻🇬 Britské Panenské ostrovy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Britské Panenské ostrovy"
#     },
#     "IOT": {  # 🇮🇴 Britské indickooceánské území
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Britské indickooceánské území"
#     },
#     "BRN": {  # 🇧🇳 Brunej
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Brunej"
#     },
#     "BGR": {  # 🇧🇬 Bulharsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Bulharsko"
#     },
#     "BFA": {  # 🇧🇫 Burkina Faso
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Burkina Faso"
#     },
#     "BDI": {  # 🇧🇮 Burundi
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Burundi"
#     },
#     "BLR": {  # 🇧🇾 Bělorusko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Bělorusko"
#     },
#     "HRV": {  # 🇭🇷 Chorvatsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Chorvatsko"
#     },
#     "COK": {  # 🇨🇰 Cookovy ostrovy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Cookovy ostrovy"
#     },
#     "CUW": {  # 🇨🇼 Curaçao
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Curaçao"
#     },
#     "COD": {  # 🇨🇩 DR Kongo
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro DR Kongo"
#     },
#     "DMA": {  # 🇩🇲 Dominika
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Dominika"
#     },
#     "DOM": {  # 🇩🇴 Dominikánská republika
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Dominikánská republika"
#     },
#     "DNK": {  # 🇩🇰 Dánsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Dánsko"
#     },
#     "DJI": {  # 🇩🇯 Džibutsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Džibutsko"
#     },
#     "ECU": {  # 🇪🇨 Ekvádor
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Ekvádor"
#     },
#     "ERI": {  # 🇪🇷 Eritrea
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Eritrea"
#     },
#     "EST": {  # 🇪🇪 Estonsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Estonsko"
#     },
#     "ETH": {  # 🇪🇹 Etiopie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Etiopie"
#     },
#     "FRO": {  # 🇫🇴 Faerské ostrovy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Faerské ostrovy"
#     },
#     "FLK": {  # 🇫🇰 Falklandy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Falklandy"
#     },
#     "FJI": {  # 🇫🇯 Fidži
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Fidži"
#     },
#     "PHL": {  # 🇵🇭 Filipíny
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Filipíny"
#     },
#     "FIN": {  # 🇫🇮 Finsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Finsko"
#     },
#     "GUF": {  # 🇬🇫 Francouzská Guyana
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Francouzská Guyana"
#     },
#     "PYF": {  # 🇵🇫 Francouzská Polynésie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Francouzská Polynésie"
#     },
#     "GAB": {  # 🇬🇦 Gabon
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Gabon"
#     },
#     "GMB": {  # 🇬🇲 Gambie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Gambie"
#     },
#     "GHA": {  # 🇬🇭 Ghana
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Ghana"
#     },
#     "GIB": {  # 🇬🇮 Gibraltar
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Gibraltar"
#     },
#     "GRD": {  # 🇬🇩 Grenada
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Grenada"
#     },
#     "GEO": {  # 🇬🇪 Gruzie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Gruzie"
#     },
#     "GRL": {  # 🇬🇱 Grónsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Grónsko"
#     },
#     "GLP": {  # 🇬🇵 Guadeloupe
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Guadeloupe"
#     },
#     "GUM": {  # 🇬🇺 Guam
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Guam"
#     },
#     "GTM": {  # 🇬🇹 Guatemala
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Guatemala"
#     },
#     "GGY": {  # 🇬🇬 Guernsey
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Guernsey"
#     },
#     "GIN": {  # 🇬🇳 Guinea
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Guinea"
#     },
#     "GNB": {  # 🇬🇼 Guinea-Bissau
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Guinea-Bissau"
#     },
#     "GUY": {  # 🇬🇾 Guyana
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Guyana"
#     },
#     "HTI": {  # 🇭🇹 Haiti
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Haiti"
#     },
#     "HND": {  # 🇭🇳 Honduras
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Honduras"
#     },
#     "HKG": {  # 🇭🇰 Hongkong
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Hongkong"
#     },
#     "IRQ": {  # 🇮🇶 Irák
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Irák"
#     },
#     "ISL": {  # 🇮🇸 Island
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Island"
#     },
#     "ISR": {  # 🇮🇱 Izrael
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Izrael"
#     },
#     "JAM": {  # 🇯🇲 Jamajka
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Jamajka"
#     },
#     "YEM": {  # 🇾🇪 Jemen
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Jemen"
#     },
#     "JEY": {  # 🇯🇪 Jersey
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Jersey"
#     },
#     "SSD": {  # 🇸🇸 Jižní Súdán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Jižní Súdán"
#     },
#     "JOR": {  # 🇯🇴 Jordánsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Jordánsko"
#     },
#     "CYM": {  # 🇰🇾 Kajmanské ostrovy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kajmanské ostrovy"
#     },
#     "KHM": {  # 🇰🇭 Kambodža
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kambodža"
#     },
#     "CMR": {  # 🇨🇲 Kamerun
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kamerun"
#     },
#     "CPV": {  # 🇨🇻 Kapverdy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kapverdy"
#     },
#     "BES": {  # 🇧🇶 Karibské Nizozemsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Karibské Nizozemsko"
#     },
#     "QAT": {  # 🇶🇦 Katar
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Katar"
#     },
#     "KAZ": {  # 🇰🇿 Kazachstán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kazachstán"
#     },
#     "KIR": {  # 🇰🇮 Kiribati
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kiribati"
#     },
#     "CCK": {  # 🇨🇨 Kokosové ostrovy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kokosové ostrovy"
#     },
#     "COM": {  # 🇰🇲 Komory
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Komory"
#     },
#     "COG": {  # 🇨🇬 Kongo
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kongo"
#     },
#     "UNK": {  # 🇽🇰 Kosovo
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kosovo"
#     },
#     "CRI": {  # 🇨🇷 Kostarika
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kostarika"
#     },
#     "CUB": {  # 🇨🇺 Kuba
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kuba"
#     },
#     "KWT": {  # 🇰🇼 Kuvajt
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kuvajt"
#     },
#     "CYP": {  # 🇨🇾 Kypr
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kypr"
#     },
#     "KGZ": {  # 🇰🇬 Kyrgyzstán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Kyrgyzstán"
#     },
#     "LAO": {  # 🇱🇦 Laos
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Laos"
#     },
#     "LSO": {  # 🇱🇸 Lesotho
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Lesotho"
#     },
#     "LBN": {  # 🇱🇧 Libanon
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Libanon"
#     },
#     "LBY": {  # 🇱🇾 Libye
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Libye"
#     },
#     "LBR": {  # 🇱🇷 Libérie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Libérie"
#     },
#     "LIE": {  # 🇱🇮 Lichtenštejnsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Lichtenštejnsko"
#     },
#     "LTU": {  # 🇱🇹 Litva
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Litva"
#     },
#     "LVA": {  # 🇱🇻 Lotyšsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Lotyšsko"
#     },
#     "LUX": {  # 🇱🇺 Lucembursko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Lucembursko"
#     },
#     "MAC": {  # 🇲🇴 Macao
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Macao"
#     },
#     "MDG": {  # 🇲🇬 Madagaskar
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Madagaskar"
#     },
#     "MYS": {  # 🇲🇾 Malajsie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Malajsie"
#     },
#     "MWI": {  # 🇲🇼 Malawi
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Malawi"
#     },
#     "MDV": {  # 🇲🇻 Maledivy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Maledivy"
#     },
#     "MLI": {  # 🇲🇱 Mali
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Mali"
#     },
#     "MLT": {  # 🇲🇹 Malta
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Malta"
#     },
#     "MHL": {  # 🇲🇭 Marshallovy ostrovy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Marshallovy ostrovy"
#     },
#     "MTQ": {  # 🇲🇶 Martinik
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Martinik"
#     },
#     "MUS": {  # 🇲🇺 Mauricius
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Mauricius"
#     },
#     "MRT": {  # 🇲🇷 Mauritánie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Mauritánie"
#     },
#     "MYT": {  # 🇾🇹 Mayotte
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Mayotte"
#     },
#     "HUN": {  # 🇭🇺 Maďarsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Maďarsko"
#     },
#     "UMI": {  # 🇺🇲 Menší odlehlé ostrovy USA
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Menší odlehlé ostrovy USA"
#     },
#     "FSM": {  # 🇫🇲 Mikronésie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Mikronésie"
#     },
#     "MDA": {  # 🇲🇩 Moldavsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Moldavsko"
#     },
#     "MCO": {  # 🇲🇨 Monako
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Monako"
#     },
#     "MNG": {  # 🇲🇳 Mongolsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Mongolsko"
#     },
#     "MSR": {  # 🇲🇸 Montserrat
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Montserrat"
#     },
#     "MOZ": {  # 🇲🇿 Mosambik
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Mosambik"
#     },
#     "MMR": {  # 🇲🇲 Myanmar
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Myanmar"
#     },
#     "NAM": {  # 🇳🇦 Namibie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Namibie"
#     },
#     "NRU": {  # 🇳🇷 Nauru
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Nauru"
#     },
#     "NPL": {  # 🇳🇵 Nepál
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Nepál"
#     },
#     "NER": {  # 🇳🇪 Niger
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Niger"
#     },
#     "NGA": {  # 🇳🇬 Nigérie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Nigérie"
#     },
#     "NIC": {  # 🇳🇮 Nikaragua
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Nikaragua"
#     },
#     "NIU": {  # 🇳🇺 Niue
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Niue"
#     },
#     "NFK": {  # 🇳🇫 Norfolk
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Norfolk"
#     },
#     "NCL": {  # 🇳🇨 Nová Kaledonie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Nová Kaledonie"
#     },
#     "OMN": {  # 🇴🇲 Omán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Omán"
#     },
#     "IMN": {  # 🇮🇲 Ostrov Man
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Ostrov Man"
#     },
#     "PLW": {  # 🇵🇼 Palau
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Palau"
#     },
#     "PSE": {  # 🇵🇸 Palestina
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Palestina"
#     },
#     "PAN": {  # 🇵🇦 Panama
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Panama"
#     },
#     "PNG": {  # 🇵🇬 Papua-Nová Guinea
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Papua-Nová Guinea"
#     },
#     "PRY": {  # 🇵🇾 Paraguay
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Paraguay"
#     },
#     "PCN": {  # 🇵🇳 Pitcairnovy ostrovy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Pitcairnovy ostrovy"
#     },
#     "CIV": {  # 🇨🇮 Pobřeží slonoviny
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Pobřeží slonoviny"
#     },
#     "PRI": {  # 🇵🇷 Portoriko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Portoriko"
#     },
#     "PAK": {  # 🇵🇰 Pákistán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Pákistán"
#     },
#     "GNQ": {  # 🇬🇶 Rovníková Guinea
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Rovníková Guinea"
#     },
#     "ROU": {  # 🇷🇴 Rumunsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Rumunsko"
#     },
#     "RUS": {  # 🇷🇺 Rusko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Rusko"
#     },
#     "RWA": {  # 🇷🇼 Rwanda
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Rwanda"
#     },
#     "REU": {  # 🇷🇪 Réunion
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Réunion"
#     },
#     "SPM": {  # 🇵🇲 Saint-Pierre a Miquelon
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Saint-Pierre a Miquelon"
#     },
#     "SLV": {  # 🇸🇻 Salvador
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Salvador"
#     },
#     "WSM": {  # 🇼🇸 Samoa
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Samoa"
#     },
#     "SMR": {  # 🇸🇲 San Marino
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro San Marino"
#     },
#     "SEN": {  # 🇸🇳 Senegal
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Senegal"
#     },
#     "PRK": {  # 🇰🇵 Severní Korea
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Severní Korea"
#     },
#     "MKD": {  # 🇲🇰 Severní Makedonie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Severní Makedonie"
#     },
#     "MNP": {  # 🇲🇵 Severní Mariany
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Severní Mariany"
#     },
#     "SYC": {  # 🇸🇨 Seychely
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Seychely"
#     },
#     "SLE": {  # 🇸🇱 Sierra Leone
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Sierra Leone"
#     },
#     "SVK": {  # 🇸🇰 Slovensko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Slovensko"
#     },
#     "SVN": {  # 🇸🇮 Slovinsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Slovinsko"
#     },
#     "SOM": {  # 🇸🇴 Somálsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Somálsko"
#     },
#     "SRB": {  # 🇷🇸 Srbsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Srbsko"
#     },
#     "LKA": {  # 🇱🇰 Srí Lanka
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Srí Lanka"
#     },
#     "CAF": {  # 🇨🇫 Středoafrická republika
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Středoafrická republika"
#     },
#     "SUR": {  # 🇸🇷 Surinam
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Surinam"
#     },
#     "SHN": {  # 🇸🇭 Svatá Helena, Ascension a Tristan da Cunha
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Svatá Helena, Ascension a Tristan da Cunha"
#     },
#     "LCA": {  # 🇱🇨 Svatá Lucie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Svatá Lucie"
#     },
#     "BLM": {  # 🇧🇱 Svatý Bartoloměj
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Svatý Bartoloměj"
#     },
#     "KNA": {  # 🇰🇳 Svatý Kryštof a Nevis
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Svatý Kryštof a Nevis"
#     },
#     "MAF": {  # 🇲🇫 Svatý Martin (Francie)
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Svatý Martin (Francie)"
#     },
#     "SXM": {  # 🇸🇽 Svatý Martin (Nizozemsko)
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Svatý Martin (Nizozemsko)"
#     },
#     "STP": {  # 🇸🇹 Svatý Tomáš a Princův ostrov
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Svatý Tomáš a Princův ostrov"
#     },
#     "VCT": {  # 🇻🇨 Svatý Vincenc a Grenadiny
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Svatý Vincenc a Grenadiny"
#     },
#     "SWZ": {  # 🇸🇿 Svazijsko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Svazijsko"
#     },
#     "SDN": {  # 🇸🇩 Súdán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Súdán"
#     },
#     "SYR": {  # 🇸🇾 Sýrie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Sýrie"
#     },
#     "TZA": {  # 🇹🇿 Tanzanie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Tanzanie"
#     },
#     "TWN": {  # 🇹🇼 Tchaj-wan
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Tchaj-wan"
#     },
#     "TGO": {  # 🇹🇬 Togo
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Togo"
#     },
#     "TKL": {  # 🇹🇰 Tokelau
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Tokelau"
#     },
#     "TON": {  # 🇹🇴 Tonga
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Tonga"
#     },
#     "TTO": {  # 🇹🇹 Trinidad a Tobago
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Trinidad a Tobago"
#     },
#     "TUN": {  # 🇹🇳 Tunisko
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Tunisko"
#     },
#     "TKM": {  # 🇹🇲 Turkmenistán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Turkmenistán"
#     },
#     "TCA": {  # 🇹🇨 Turks a Caicos
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Turks a Caicos"
#     },
#     "TUV": {  # 🇹🇻 Tuvalu
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Tuvalu"
#     },
#     "TJK": {  # 🇹🇯 Tádžikistán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Tádžikistán"
#     },
#     "UGA": {  # 🇺🇬 Uganda
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Uganda"
#     },
#     "UKR": {  # 🇺🇦 Ukrajina
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Ukrajina"
#     },
#     "URY": {  # 🇺🇾 Uruguay
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Uruguay"
#     },
#     "UZB": {  # 🇺🇿 Uzbekistán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Uzbekistán"
#     },
#     "VUT": {  # 🇻🇺 Vanuatu
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Vanuatu"
#     },
#     "VAT": {  # 🇻🇦 Vatikán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Vatikán"
#     },
#     "VEN": {  # 🇻🇪 Venezuela
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Venezuela"
#     },
#     "CXR": {  # 🇨🇽 Vánoční ostrov
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Vánoční ostrov"
#     },
#     "TLS": {  # 🇹🇱 Východní Timor
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Východní Timor"
#     },
#     "WLF": {  # 🇼🇫 Wallis a Futuna
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Wallis a Futuna"
#     },
#     "ZMB": {  # 🇿🇲 Zambie
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Zambie"
#     },
#     "ZWE": {  # 🇿🇼 Zimbabwe
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Zimbabwe"
#     },
#     "ESH": {  # 🇪🇭 Západní Sahara
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Západní Sahara"
#     },
#     "AZE": {  # 🇦🇿 Ázerbájdžán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Ázerbájdžán"
#     },
#     "ALA": {  # 🇦🇽 Ålandy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Ålandy"
#     },
#     "IRN": {  # 🇮🇷 Írán
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Írán"
#     },
#     "TCD": {  # 🇹🇩 Čad
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Čad"
#     },
#     "MNE": {  # 🇲🇪 Černá Hora
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Černá Hora"
#     },
#     "SLB": {  # 🇸🇧 Šalamounovy ostrovy
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Šalamounovy ostrovy"
#     },
#     "SJM": {  # 🇸🇯 Špicberky a Jan Mayen
#         "palette": ["#CCCCCC", "#CCCCCC", "#CCCCCC"],  # TODO: Doplňte barvy
#         "music": "Typická hudba pro Špicberky a Jan Mayen"
#     },
# })


try:
    with open('countries.json', 'r', encoding='utf-8') as f:
        countries = json.load(f)

    for country in countries:
        code = country.get('cca3')
        if code in country_data:
            # Update Palette
            country['culture']['palette'] = country_data[code]['palette']
            
            # Update Music (Overwrite with more specific examples if generic)
            # Or append? Let's overwrite for consistency with "Specific Famous Music"
            # But maybe keep the genre if it's descriptive?
            # The prompt says "jeste... u kazde zeme bych chtela nejakou jejich znamou hudbu".
            # The current data has genre descriptions. I will REPLACE it with the Artist/Song string 
            # to be more specific as requested, OR append it.
            # "Lidová hudba... nebo český pop/rock" -> "Lidová hudba... (např. Smetana, Dvořák). Známé hity: Karel Gott..."
            # Actually, simply replacing might be cleaner for the "Music" tag in the UI.
            # Let's use the new string which contains specific artists.
            country['culture']['music'] = country_data[code]['music']

    with open('countries.json', 'w', encoding='utf-8') as f:
        json.dump(countries, f, ensure_ascii=False, indent=2)
        
    print("Successfully updated countries.json with palette and music.")

except Exception as e:
    print(f"Error: {e}")

