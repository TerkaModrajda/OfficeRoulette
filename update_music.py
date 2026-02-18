import json

# Database of music data (CCA3 -> {artists: [], instrument: str/None})
music_data = {
    # Europe
    "ALB": {"artists": ["Bebe Rexha (původ)", "Era Istrefi", "Vaçe Zela"], "instrument": "Çifteli"},
    "AND": {"artists": ["Persefone", "Marta Roure"], "instrument": None},
    "AUT": {"artists": ["Mozart", "Strauss", "Falco", "Conchita Wurst"], "instrument": "Citha (Zither)"},
    "BEL": {"artists": ["Stromae", "Gotye", "Technotronic", "Jacques Brel"], "instrument": "Adolphe Sax (Saxofon)"},
    "BGR": {"artists": ["Le Mystère des Voix Bulgares", "Azis", "Kristian Kostov"], "instrument": "Gaida (dudy)"},
    "BIH": {"artists": ["Dino Merlin", "Goran Bregović", "Dubioza Kolektiv"], "instrument": "Saz"},
    "BLR": {"artists": ["Molchat Doma", "Naviband", "Pesnyary"], "instrument": "Cymbaly"},
    "CHE": {"artists": ["DJ BoBo", "Tina Turner (občanka)", "Yello"], "instrument": "Alpský roh (Alphorn)"},
    "CYP": {"artists": ["Anna Vissi", "Eleni Foureira"], "instrument": "Laouto"},
    "CZE": {"artists": ["Antonín Dvořák", "Bedřich Smetana", "Karel Gott", "Kabát"], "instrument": "Cimbál"},
    "DEU": {"artists": ["Beethoven", "Bach", "Rammstein", "Kraftwerk", "Nena"], "instrument": "Waldzither"},
    "DNK": {"artists": ["MØ", "Lukas Graham", "Aqua", "Volbeat"], "instrument": None}, # Často housle, ale ne unikátní
    "ESP": {"artists": ["Enrique Iglesias", "Rosalía", "Paco de Lucía", "Gipsy Kings"], "instrument": "Kastaniety"},
    "EST": {"artists": ["Arvo Pärt", "Kerli", "Ewert and The Two Dragons"], "instrument": "Kannel"},
    "FIN": {"artists": ["Sibelius", "Nightwish", "The Rasmus", "Darude"], "instrument": "Kantele"},
    "FRA": {"artists": ["Daft Punk", "Édith Piaf", "Stromae", "David Guetta", "Gojira"], "instrument": "Akordeon"},
    "GBR": {"artists": ["The Beatles", "Queen", "Adele", "Ed Sheeran", "Pink Floyd"], "instrument": "Dudy (Bagpipes - Skotsko)"},
    "GRC": {"artists": ["Vangelis", "Demis Roussos", "Nana Mouskouri"], "instrument": "Bouzouki"},
    "HRV": {"artists": ["2Cellos", "Oliver Dragojević", "Severina"], "instrument": "Tamburica"},
    "HUN": {"artists": ["Franz Liszt", "Omega (Gyöngyhajú lány)"], "instrument": "Cimbalom (maďarský)"},
    "IRL": {"artists": ["U2", "Enya", "The Cranberries", "Hozier", "The Dubliners"], "instrument": "Irská harfa"},
    "ISL": {"artists": ["Björk", "Sigur Rós", "Of Monsters and Men", "Kaleo"], "instrument": "Langspil"},
    "ITA": {"artists": ["Vivaldi", "Pavarotti", "Måneskin", "Andrea Bocelli", "Eros Ramazzotti"], "instrument": "Mandolína"},
    "LIE": {"artists": ["Al Walser"], "instrument": None},
    "LTU": {"artists": ["The Roop", "Dynoro"], "instrument": "Kanklės"},
    "LUX": {"artists": ["Bolero (skladba Maurice Ravel - matka z Baskicka, ale vliv)", "Jürgen Melzer"], "instrument": None}, # Tady je to těžké
    "LVA": {"artists": ["Brainstorm", "Aminata"], "instrument": "Kokle"},
    "MCO": {"artists": ["Léo Ferré (narozen)"], "instrument": None},
    "MDA": {"artists": ["O-Zone (Dragostea Din Tei)", "SunStroke Project"], "instrument": "Nai"},
    "MKD": {"artists": ["Toše Proeski", "Esma Redžepova"], "instrument": "Tapan"},
    "MLT": {"artists": ["Joseph Calleja", "Ira Losco"], "instrument": "Żaqq (dudy)"},
    "MNE": {"artists": ["Rambo Amadeus", "Sergej Ćetković"], "instrument": "Gusle"},
    "NLD": {"artists": ["Tiësto", "Martin Garrix", "Armin van Buuren", "André Rieu"], "instrument": "Flašinet (Draaiorgel)"},
    "NOR": {"artists": ["A-ha", "Kygo", "Alan Walker", "Edvard Grieg", "Aurora"], "instrument": "Hardangerské housle"},
    "POL": {"artists": ["Chopin", "Vader", "Behemoth", "Czesław Niemen"], "instrument": None},
    "PRT": {"artists": ["Amália Rodrigues", "Salvador Sobral", "Mariza"], "instrument": "Portugalská kytara"},
    "ROU": {"artists": ["Inna", "Enescu", "Gheorghe Zamfir"], "instrument": "Panova flétna"},
    "RUS": {"artists": ["Tchaikovsky", "Rachmaninoff", "t.A.T.u.", "Little Big"], "instrument": "Balalaika"},
    "SMR": {"artists": ["Valentina Monetta"], "instrument": None},
    "SRB": {"artists": ["Marija Šerifović", "Goran Bregović"], "instrument": "Frula"},
    "SVK": {"artists": ["Elán", "Miroslav Žbirka", "Horkýže Slíže", "Kontrafakt"], "instrument": "Fujara"},
    "SVN": {"artists": ["Slavko Avsenik (Oberkrainer)", "Laibach"], "instrument": "Harmonika"},
    "SWE": {"artists": ["ABBA", "Avicii", "Roxette", "Europe", "Zara Larsson"], "instrument": "Nyckelharpa"},
    "TUR": {"artists": ["Tarkan ("], "instrument": "Saz (Baglama)"},
    "UKR": {"artists": ["Ruslana", "Kalush Orchestra", "Okean Elzy", "Verka Serduchka"], "instrument": "Bandura"},
    "VAT": {"artists": ["Papežský sbor"], "instrument": "Varhany"},
    "XKX": {"artists": ["Rita Ora (původ)", "Dua Lipa (původ)"], "instrument": "Çifteli"},

    # North America
    "ATG": {"artists": ["Burning Flames"], "instrument": "Steel Pan"},
    "BHS": {"artists": ["Baha Men (Who Let the Dogs Out)"], "instrument": "Goombay drum"},
    "BLZ": {"artists": ["Andy Palacio"], "instrument": "Garifuna drums"},
    "BRB": {"artists": ["Rihanna", "Grandmaster Flash"], "instrument": "Steel Pan"},
    "CAN": {"artists": ["Céline Dion", "Drake", "Justin Bieber", "The Weeknd", "Bryan Adams"], "instrument": "Fiddle (housle)"},
    "CRI": {"artists": ["Debi Nova"], "instrument": "Marimba"},
    "CUB": {"artists": ["Buena Vista Social Club", "Celia Cruz", "Camila Cabello"], "instrument": "Tres (kytara)"},
    "DMA": {"artists": ["Nasio Fontaine"], "instrument": None},
    "DOM": {"artists": ["Juan Luis Guerra", "Romeo Santos", "Aventura"], "instrument": "Güira"},
    "GRD": {"artists": ["Mighty Sparrow"], "instrument": None},
    "GTM": {"artists": ["Ricardo Arjona"], "instrument": "Marimba"},
    "HND": {"artists": ["Guillermo Anderson"], "instrument": "Marimba"},
    "HTI": {"artists": ["Wyclef Jean", "Sweet Micky"], "instrument": "Rada drums"},
    "JAM": {"artists": ["Bob Marley", "Sean Paul", "Shaggy", "Jimmy Cliff"], "instrument": "Steel Pan / Reggae drums"},
    "KNA": {"artists": ["Joan Armatrading"], "instrument": None},
    "LCA": {"artists": ["Teddyson John"], "instrument": None},
    "MEX": {"artists": ["Carlos Santana", "Mariachi Vargas", "Selena", "Thalía"], "instrument": "Guitarrón (velká kytara)"},
    "NIC": {"artists": ["Rubén Darío (básník/písně)"], "instrument": "Marimba"},
    "PAN": {"artists": ["Rubén Blades"], "instrument": "Mejoranera"},
    "SLV": {"artists": ["Álvaro Torres"], "instrument": "Marimba"},
    "TTO": {"artists": ["Nicki Minaj", "Billy Ocean"], "instrument": "Steel Pan (ocelový buben)"},
    "USA": {"artists": ["Michael Jackson", "Elvis Presley", "Beyoncé", "Taylor Swift", "Eminem"], "instrument": "Banjo"},
    "VCT": {"artists": ["Kevin Lyttle"], "instrument": None},

    # South America
    "ARG": {"artists": ["Astor Piazzolla", "Soda Stereo", "Mercedes Sosa"], "instrument": "Bandoneón (tango harmonika)"},
    "BOL": {"artists": ["Los Kjarkas (Lambada originál)"], "instrument": "Charango (kytara z pásovce)"},
    "BRA": {"artists": ["Anitta", "Sepultura", "Antônio Carlos Jobim", "Caetano Veloso"], "instrument": "Berimbau"},
    "CHL": {"artists": ["Pablo Neruda (poezie v hudbě)", "Mon Laferte"], "instrument": "Kultrun"},
    "COL": {"artists": ["Shakira", "J Balvin", "Maluma", "Juanes", "Carlos Vives"], "instrument": "Caja Vallenata"},
    "ECU": {"artists": ["Julio Jaramillo"], "instrument": "Rondador (flétna)"},
    "GUY": {"artists": ["Eddy Grant"], "instrument": None},
    "PER": {"artists": ["Yma Sumac", "Susana Baca"], "instrument": "Cajón", "songs": ["El Cóndor Pasa"]},
    "PRY": {"artists": ["Agustín Barrios"], "instrument": "Paraguayská harfa"},
    "SUR": {"artists": ["Kenny B"], "instrument": "Kaseko drums"},
    "URY": {"artists": ["Jorge Drexler", "Natalia Oreiro"], "instrument": "Candombe drums"},
    "VEN": {"artists": ["Simón Díaz", "Oscar D'León"], "instrument": "Cuatro (malá kytara)"},

    # Asia
    "AFG": {"artists": ["Ahmad Zahir"], "instrument": "Rubab"},
    "ARE": {"artists": ["Ahlam", "Hussain Al Jassmi"], "instrument": "Oud"},
    "ARM": {"artists": ["System of a Down", "Charles Aznavour (původ)", "Aram Khachaturian"], "instrument": "Duduk"},
    "AZE": {"artists": ["Uzeyir Hajibeyov"], "instrument": "Tar"},
    "BGD": {"artists": ["Runa Laila"], "instrument": "Ektara"},
    "BHR": {"artists": ["Ali Bahar"], "instrument": None},
    "BRN": {"artists": ["Wu Chun"], "instrument": None},
    "BTN": {"artists": ["Misty Terrace"], "instrument": "Dranyen"},
    "CHN": {"artists": ["Lang Lang", "Teresa Teng", "Jackson Wang"], "instrument": "Guzheng (citera)"},
    "GEO": {"artists": ["Trio Mandili", "Khatia Buniatishvili"], "instrument": "Panduri"},
    "HKG": {"artists": ["Jackie Chan", "G.E.M."], "instrument": None},
    "IDN": {"artists": ["Rich Brian", "Anggun"], "instrument": "Gamelan (orchestr)"},
    "IND": {"artists": ["Ravi Shankar", "A.R. Rahman", "Freddie Mercury (původ)", "Punjabi MC"], "instrument": "Sitar"},
    "IRN": {"artists": ["Googoosh", "Ramin Djawadi (skladatel GoT)"], "instrument": "Santur"},
    "IRQ": {"artists": ["Kazem Al Saher"], "instrument": "Oud"},
    "ISR": {"artists": ["Netta", "Gene Simmons (původ)", "Ofra Haza"], "instrument": "Shofar"},
    "JPN": {"artists": ["AKB48", "Babymetal", "Joe Hisaishi", "Ryuichi Sakamoto"], "instrument": "Koto / Shamisen"},
    "KAZ": {"artists": ["Dimash Kudaibergen"], "instrument": "Dombra"},
    "KGZ": {"artists": ["Ordo Sakhna"], "instrument": "Komuz"},
    "KHM": {"artists": ["Sinn Sisamouth"], "instrument": "Khim"},
    "KOR": {"artists": ["BTS", "BLACKPINK", "PSY", "EXO"], "instrument": "Gayageum"},
    "KWT": {"artists": ["Nawal El Kuwaitia"], "instrument": "Mirwas"},
    "LAO": {"artists": ["Alexandra Bounxouei"], "instrument": "Khene (ústní varhany)"},
    "LBN": {"artists": ["Fairuz", "Mika (původ)", "Shakira (původ)"], "instrument": "Oud"},
    "LKA": {"artists": ["M.I.A. (původ)"], "instrument": "Thammattama"},
    "MNG": {"artists": ["The Hu", "Batzorig Vaanchig"], "instrument": "Morin Khuur (koňské housle)"},
    "MYS": {"artists": ["Yuna", "Siti Nurhaliza"], "instrument": "Sape"},
    "NPL": {"artists": ["Ani Choying Drolma"], "instrument": "Sarangi"},
    "OMN": {"artists": ["Salah Al-Zadjali"], "instrument": "Oud"},
    "PAK": {"artists": ["Nusrat Fateh Ali Khan", "Atif Aslam"], "instrument": "Harmonium"},
    "PHL": {"artists": ["Bruno Mars (původ)", "Lea Salonga", "Olivia Rodrigo (původ)"], "instrument": "Kulintang"},
    "PRK": {"artists": ["Moranbong Band"], "instrument": None},
    "PSE": {"artists": ["Mohammed Assaf"], "instrument": "Oud"},
    "QAT": {"artists": ["Fahad Al Kubaisi"], "instrument": None},
    "SAU": {"artists": ["Mohammed Abdu"], "instrument": "Oud"},
    "SGP": {"artists": ["JJ Lin", "Vanessa-Mae"], "instrument": None},
    "SYR": {"artists": ["Assala Nasri", "Omar Souleyman"], "instrument": "Qanun"},
    "THA": {"artists": ["LISA (Blackpink)", "Tata Young"], "instrument": "Ranat Ek (xylofon)"},
    "TJK": {"artists": ["Shabnam Surayo"], "instrument": "Rubab"},
    "TKM": {"artists": ["Gunesh Ensemble"], "instrument": "Dutar"},
    "TWN": {"artists": ["Jay Chou", "Teresa Teng"], "instrument": "Pipa"},
    "UZB": {"artists": ["Sevara Nazarkhan"], "instrument": "Doira"},
    "VNM": {"artists": ["Son Tung M-TP"], "instrument": "Dan Bau (monochord)"},
    "YEM": {"artists": ["Ofra Haza (původ)"], "instrument": None},

    # Africa
    "AGO": {"artists": ["Bonga", "Anselmo Ralph"], "instrument": "Kissange"},
    "BDI": {"artists": ["Khadja Nin"], "instrument": "Ingoma drums"},
    "BEN": {"artists": ["Angélique Kidjo (Grammy winner)"], "instrument": "Gangan"},
    "BFA": {"artists": ["Victor Démé"], "instrument": "Balafon"},
    "BWA": {"artists": ["Vee Mampeezy"], "instrument": "Segaba"},
    "CAF": {"artists": ["Laetitia Zonzambé"], "instrument": "Sanza"},
    "CIV": {"artists": ["Alpha Blondy", "Magic System"], "instrument": "Djembe"},
    "CMR": {"artists": ["Manu Dibango", "Richard Bona"], "instrument": "Balafon"},
    "COD": {"artists": ["Fally Ipupa", "Papa Wemba", "Maître Gims"], "instrument": "Likembe"},
    "COG": {"artists": ["Koffi Olomide"], "instrument": "Ngoma"},
    "CPV": {"artists": ["Cesária Évora"], "instrument": "Cavaquinho"},
    "DJI": {"artists": ["Nima Djama"], "instrument": "Tanbura"},
    "DZA": {"artists": ["Cheb Khaled (Aïcha)", "Rachid Taha", "DJ Snake (původ)"], "instrument": "Mandole"},
    "EGY": {"artists": ["Umm Kulthum", "Amr Diab", "Dalida"], "instrument": "Oud / Qanun"},
    "ERI": {"artists": ["Helen Meles"], "instrument": "Krar"},
    "ETH": {"artists": ["Teddy Afro", "Mulatu Astatke", "Gigi"], "instrument": "Masenqo"},
    "GAB": {"artists": ["Patience Dabany"], "instrument": "Moungongo"},
    "GHA": {"artists": ["Sarkodie", "Osibisa"], "instrument": "Talking Drum"},
    "GIN": {"artists": ["Mory Kanté (Yeke Yeke)"], "instrument": "Kora"},
    "GMB": {"artists": ["Sona Jobarteh"], "instrument": "Kora"},
    "GNB": {"artists": ["Justino Delgado"], "instrument": None},
    "KEN": {"artists": ["Sauti Sol", "Ayub Ogada"], "instrument": "Nyatiti"},
    "LBR": {"artists": ["Kobazzie"], "instrument": None},
    "LBY": {"artists": ["Ahmed Fakroun"], "instrument": "Zukra"},
    "LSO": {"artists": ["Famole"], "instrument": "Lesiba"},
    "MAR": {"artists": ["Saad Lamjarred", "French Montana (původ)", "Loreen (původ)"], "instrument": "Oud / Guimbri"},
    "MDG": {"artists": ["Erick Manana"], "instrument": "Valiha (bambusová citera)"},
    "MLI": {"artists": ["Salif Keita", "Tinariwen", "Amadou & Mariam"], "instrument": "Kora"},
    "MOZ": {"artists": ["Mariza (původ)"], "instrument": "Timbila"},
    "MRT": {"artists": ["Noura Mint Seymali"], "instrument": "Ardin"},
    "MUS": {"artists": ["Alain Ramanisum"], "instrument": "Ravanne"},
    "MWI": {"artists": ["The Black Missionaries"], "instrument": "Mbira"},
    "NAM": {"artists": ["Elemotho"], "instrument": None},
    "NER": {"artists": ["Bombino"], "instrument": "Tuareg Guitar"},
    "NGA": {"artists": ["Burna Boy", "Wizkid", "Fela Kuti", "Sade", "Davido"], "instrument": "Talking Drum / Udu"},
    "RWA": {"artists": ["The Ben"], "instrument": "Inanga"},
    "SDN": {"artists": ["Emmanuel Jal"], "instrument": "Tambour"},
    "SEN": {"artists": ["Youssou N'Dour (7 Seconds)", "Akon", "Ismaël Lô"], "instrument": "Kora / Sabar"},
    "SLE": {"artists": ["Bunn A Badd"], "instrument": None},
    "SOM": {"artists": ["K'naan (Wavin' Flag)"], "instrument": "Kaban (Oud)"},
    "SSD": {"artists": ["Emmanuel Jal"], "instrument": None},
    "STP": {"artists": ["Kalú Mendes"], "instrument": None},
    "SWZ": {"artists": ["Sands"], "instrument": "Makhoyane"},
    "SYC": {"artists": ["Jean-Marc Volcy"], "instrument": None},
    "TCD": {"artists": ["H'Sao"], "instrument": None},
    "TGO": {"artists": ["Bella Bellow"], "instrument": None},
    "TUN": {"artists": ["Emel Mathlouthi"], "instrument": "Oud"},
    "TZA": {"artists": ["Diamond Platnumz"], "instrument": "Zezeru"},
    "UGA": {"artists": ["Eddy Kenzo"], "instrument": "Adungu"},
    "ZAF": {"artists": ["Die Antwoord", "Miriam Makeba", "Master KG (Jerusalema)", "Seether"], "instrument": "Vuvuzela / Marimba"},
    "ZMB": {"artists": ["Mampi"], "instrument": "Silimba"},
    "ZWE": {"artists": ["Oliver Mtukudzi"], "instrument": "Mbira (kalimba)"},

    # Oceania
    "AUS": {"artists": ["AC/DC", "Sia", "Kylie Minogue", "Tame Impala", "Nick Cave"], "instrument": "Didgeridoo"},
    "FJI": {"artists": ["Rosiloa"], "instrument": "Lali drums"},
    "FSM": {"artists": ["SDA"], "instrument": None},
    "KIR": {"artists": ["Te Vaka (částečně)"], "instrument": None},
    "MHL": {"artists": ["Yastamon"], "instrument": None},
    "NRU": {"artists": ["Baron Waqa (bývalý prezident a skladatel)"], "instrument": None},
    "NZL": {"artists": ["Lorde", "Crowded House", "Peter Jackson (režisér, ale kultura)"], "instrument": "Pūtātara (lastura)"},
    "PLW": {"artists": ["Kendall Titus"], "instrument": None},
    "PNG": {"artists": ["O-Shen", "George Telek"], "instrument": "Kundu drum"},
    "SLB": {"artists": ["Sharzy"], "instrument": "Panpipes"},
    "TON": {"artists": ["Soane"], "instrument": "Nafa"},
    "TUV": {"artists": ["Te Vaka"], "instrument": None},
    "VUT": {"artists": ["Vanessa Quai"], "instrument": "Slit drum"},
    "WSM": {"artists": ["Te Vaka (Moana soundtrack)"], "instrument": "Pate (log drum)"},
}

def update_music():
    try:
        with open('countries.json', 'r', encoding='utf-8') as f:
            countries = json.load(f)
        
        updated_count = 0
        
        for country in countries:
            cca3 = country.get('cca3')
            
            if cca3 in music_data:
                data = music_data[cca3]
                
                if 'culture' not in country:
                    country['culture'] = {}
                
                # Update Artists
                # Join simple list to string if frontend expects generic string,
                # BUT logic above shows 'artists' expects array in frontend: 
                # "(country.culture.artists) ? country.culture.artists : [musicVibe..."
                country['culture']['artists'] = data['artists']
                
                # Update Instrument
                # Only if not None
                if data['instrument']:
                    country['culture']['instrument'] = data['instrument']
                else:
                    # Explicitly remove or set to null if none exists, per user request
                    # to not show generic instruments for countries without specific ones.
                    country['culture']['instrument'] = None
                
                updated_count += 1

        with open('countries.json', 'w', encoding='utf-8') as f:
            json.dump(countries, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully updated specific music for {updated_count} countries.")

    except Exception as e:
        print(f"Error updating music: {e}")

if __name__ == "__main__":
    update_music()
