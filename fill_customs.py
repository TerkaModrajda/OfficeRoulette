
import json
import random

# Subregion data (Etiquette, Festivals, Fun Facts)
subregion_data = {
    # --- EUROPE ---
    "Northern Europe": {
        "etiquette": "Cení se dochvilnost a osobní prostor. Saudování je běžná sociální aktivita (hlavně Finsko).",
        "festivals": "Midsummer (slunovrat), Sv. Lucie (světla v zimě).",
        "fun_fact": "V mnoha severských zemích nechávají miminka spát venku v kočárku i v mrazu pro lepší imunitu."
    },
    "Western Europe": {
        "etiquette": "Formální zdravení (Bonjour/Guten Tag). Oběd je důležitá část dne, nikoliv jen rychlé jídlo.",
        "festivals": "Oktoberfest, Karneval v Binche, Tour de France (jako svátek).",
        "fun_fact": "V Nizozemsku je více kol než lidí."
    },
    "Southern Europe": {
        "etiquette": "Kontakt je vřelý, polibky na tvář jsou běžné. Večeře začínají pozdě (často po 21. hodině).",
        "festivals": "La Tomatina (Španělsko), Benátský karneval, Sanfermines (běh s býky).",
        "fun_fact": "Siesta není mýtus, v horkých dnech se obchody odpoledne opravdu zavírají."
    },
    "Eastern Europe": {
        "etiquette": "Pohostinnost je posvátná. Nikdy nepřijďte na návštěvu s prázdnou (květiny, víno). Zouváme se.",
        "festivals": "Masopust, Velikonoce (barvení vajíček), Ivana Kupala.",
        "fun_fact": "Chléb se solí je tradiční uvítací gesto pro vzácné hosty."
    },
    "Central Europe": {
        "etiquette": "Kombinace germánské dochvilnosti a slovanské pohostinnosti. Titulování je stále časté.",
        "festivals": "Vánoční trhy, Vinobraní, Pivní slavnosti.",
        "fun_fact": "Houbaření je zde národním sportem, což je ve zbytku světa rarita."
    },
     "Southeast Europe": {
        "etiquette": "Káva se pije hodiny. Rodina je na prvním místě. Neodmítejte nabízené jídlo.",
        "festivals": "Exit Festival, Guča Trumpet Festival.",
        "fun_fact": "V Bulharsku kývání hlavou znamená 'ne' a vrtění 'ano'."
    },

    # --- ASIA ---
    "Eastern Asia": {
        "etiquette": "Hluboká úklona vyjadřuje respekt. Vizitky podávejte oběma rukama. Nesmrkejte na veřejnosti.",
        "festivals": "Lunární Nový rok, Svátek dračích lodí, Svátek lampionů.",
        "fun_fact": "V Japonsku a Číně se číslo 4 považuje za nešťastné, protože zní jako 'smrt'."
    },
    "South-Eastern Asia": {
        "etiquette": "Hlava je posvátná (nesahejte na ni dětem). Levá ruka se považuje za nečistou (nepodávejte jí jídlo).",
        "festivals": "Songkran (vodní bitva), Loi Krathong (plovoucí košíčky).",
        "fun_fact": "Durian je ovoce, které je v mnoha hotelech a v metru zakázáno kvůli silnému zápachu."
    },
    "Southern Asia": {
        "etiquette": "Jí se často pravou rukou. Respekt ke starším je klíčový. Kývání hlavou ze strany na stranu může znamenat souhlas.",
        "festivals": "Holi (svátek barev), Diwali (svátek světel).",
        "fun_fact": "Krávy jsou v mnoha částech Indie posvátné a mají přednost v dopravě."
    },
    "Central Asia": {
        "etiquette": "Host je považován za dar od boha. Čaj se podává neustále a odmítnutí je neslušné.",
        "festivals": "Nowruz (perský Nový rok).",
        "fun_fact": "Kokpar je tradiční sport, kde jezdci na koních bojují o bezhlavé kozí tělo (dnes často atrapu)."
    },
    "Western Asia": {
        "etiquette": "Pohostinnost je legendární. Při vstupu do mešity nebo domu se zouvá. Alkohol na veřejnosti může být tabu.",
        "festivals": "Ramadán (následuje Eid al-Fitr).",
        "fun_fact": "Mrtvé moře je tak slané, že se v něm nedá potopit."
    },

    # --- AFRICA ---
    "Northern Africa": {
        "etiquette": "Smlouvání na tržištích je nutnost a společenská hra. Čaj se nalévá z výšky pro vytvoření pěny.",
        "festivals": "Festival růží (Maroko), Eid al-Adha.",
        "fun_fact": "Sahara je největší horká poušť světa, ale v noci tam může mrznout."
    },
    "Western Africa": {
        "etiquette": "Pozdravy jsou dlouhé a zahrnují otázky na rodinu. Starším se prokazuje velká úcta.",
        "festivals": "Panafrican Film Festival (Burkina Faso), Voodoo Festival (Benin).",
        "fun_fact": "Griotové jsou tradiční vypravěči, kteří uchovávají historii rodu pouze v paměti."
    },
    "Eastern Africa": {
        "etiquette": "Čas je flexibilní ('Pole pole' - pomalu, v klidu). Jídlo se často sdílí z jednoho talíře.",
        "festivals": "Velká migrace pakoňů (přírodní svátek), Lake of Stars (Malawi).",
        "fun_fact": "V Etiopii je rok 2016, protože používají jiný kalendář."
    },
    "Southern Africa": {
        "etiquette": "Ubuntu - víra v univerzální pouto sdílení ('Jsem, protože jsme'). Grilování (Braai) je společenská událost.",
        "festivals": "Cape Town Jazz Festival, Reed Dance.",
        "fun_fact": "Lesotho je jediné království na světě, které leží celé v nadmořské výšce nad 1000 m."
    },
    "Middle Africa": {
        "etiquette": "Respekt k autoritám a starším. Hudba a tanec jsou součástí každodenního života.",
        "festivals": "Festivaly masek, Fêtes des Masques.",
        "fun_fact": "Pygmejové v deštných pralesech jsou známí svou malou postavou a unikátní hudbou."
    },

    # --- AMERICAS ---
    "North America": {
        "etiquette": "Silný stisk ruky, přímý oční kontakt. 'Small talk' je běžný i s cizími lidmi. Spropitné v USA/Kanadě je povinnost (15-20%).",
        "festivals": "Díkůvzdání, Super Bowl Sunday, Den nezávislosti.",
        "fun_fact": "V Severní Americe se spotřebuje nejvíce zmrzliny na obyvatele na světě."
    },
    "Central America": {
        "etiquette": "Oběd je hlavní jídlo dne. Čas plyne pomaleji ('Mañana').",
        "festivals": "Den mrtvých (Día de los Muertos), Semana Santa.",
        "fun_fact": "Čokoláda pochází odtud - Mayové ji pili jako hořký kořeněný nápoj."
    },
    "Caribbean": {
        "etiquette": "Rytmus a hudba jsou všudypřítomné. Oblékání je barevné, ale v kostelech konzervativní.",
        "festivals": "Karneval (Trinidad, Rio styl), Junkanoo (Bahamy).",
        "fun_fact": "Je to jediné místo na světě, kde můžete plavat s prasaty (Bahamy)."
    },
    "South America": {
        "etiquette": "Vřelost, objetí a polibky na přivítanou. Fotbal je náboženství.",
        "festivals": "Karneval v Riu, Inti Raymi (slunovrat Inků).",
        "fun_fact": "Amazonka je řeka s největším průtokem na světě."
    },

    # --- OCEANIA ---
    "Australia and New Zealand": {
        "etiquette": "Rovnostářství ('Mate'). Grilování (Barbie) je základní sociální aktivita. V hospodě platí 'rounds' (každý koupí rundu).",
        "festivals": "Australia Day, Waitangi Day, Anzac Day.",
        "fun_fact": "Na Novém Zélandu je více ovcí než lidí."
    },
    "Polynesia": {
        "etiquette": "Květinové věnce (Lei) na uvítanou. Respekt k přírodě (Mana). Tetování má hluboký kulturní význam.",
        "festivals": "Heiva i Tahiti, Haka (obřadní tanec).",
        "fun_fact": "Slovo 'Tabu' pochází z polynéských jazyků."
    },
    "Melanesia": {
        "etiquette": "Kava obřady jsou klíčové pro řešení sporů a uvítání. Život v komunitě (Wantok system).",
        "festivals": "Naghol (skoky z věží - předchůdce bungee jumpingu, Vanuatu).",
        "fun_fact": "Papua Nová Guinea je jazykově nejrozmanitější země světa (přes 800 jazyků)."
    },
    "Micronesia": {
        "etiquette": "Skromnost a sdílení zdrojů. Kamenné peníze (Rai stones) se tradičně používaly na ostrově Yap.",
        "festivals": "Den Mikronésie.",
        "fun_fact": "Navigátoři zde dokázali plout tisíce kilometrů jen podle hvězd a vln bez kompasu."
    }
}

try:
    with open('countries.json', 'r', encoding='utf-8') as f:
        countries = json.load(f)

    updated_count = 0
    for country in countries:
        subregion = country.get('subregion')
        region = country.get('region')
        
        # Look for subregion data, fallback to region-wide if needed (though map covers all subregions mostly)
        data = subregion_data.get(subregion)
        
        # Fallback based on Region keywords if Subregion not found exactly
        if not data:
            if region == "Europe": data = subregion_data["Western Europe"]
            elif region == "Africa": data = subregion_data["Western Africa"]
            elif region == "Asia": data = subregion_data["Southern Asia"]
            elif region == "Americas": data = subregion_data["South America"]
            elif region == "Oceania": data = subregion_data["Polynesia"]

        if data:
            # Update specific fields if they are missing or empty
            if 'culture' not in country:
                country['culture'] = {}

            # Append Fun Fact to etiquette if not present or needs update
            etiquette = country['culture'].get('etiquette')
            
            # Special fix for the Canada fact
            bad_fact = "Kanada má více jezer než zbytek světa dohromady."
            if etiquette and bad_fact in etiquette and country['cca3'] != "CAN":
                 clean_etiquette = etiquette.replace(f" 💡 Zajímavost: {bad_fact}", "")
                 country['culture']['etiquette'] = f"{clean_etiquette} 💡 Zajímavost: {data['fun_fact']}"
                 updated_count += 1
            
            elif not etiquette:
                # Completely missing etiquette
                country['culture']['etiquette'] = f"{data['etiquette']} 💡 Zajímavost: {data['fun_fact']}"
                updated_count += 1
            else:
                # Etiquette exists, check if we should add fun fact
                if "Zajímavost" not in etiquette:
                     country['culture']['etiquette'] = f"{etiquette} 💡 Zajímavost: {data['fun_fact']}"
                     updated_count += 1

            # Festivals
            if not country['culture'].get('festivals'):
                country['culture']['festivals'] = data['festivals']

    with open('countries.json', 'w', encoding='utf-8') as f:
        json.dump(countries, f, ensure_ascii=False, indent=2)

    print(f"Updated customs and facts for {updated_count} countries.")

except Exception as e:
    print(f"Error: {e}")
