import json

# Dictionary of specific traditional/historical clothing by CCA3 code
clothing_map = {
    # Europe
    "ALB": "Xhubleta (tradiční sukně), Qeleshe (bílá plstěná čepice)",
    "AND": "Retalls (tradiční katalánský kroj), Barretina (červená čepice)",
    "AUT": "Dirndl (ženy), Lederhosen (kožené kalhoty, muži)",
    "BEL": "Krajkové doplňky (Bruggy), Smock (halena)",
    "BGR": "Sukman (šatová sukně), Kalpak (kožešinová čepice)",
    "BIH": "Dimije (široké kalhoty), Jelek (vyšívaná vesta)",
    "BLR": "Vyšívaná košile (Vyshyvanka), slaměný klobouk",
    "CHE": "Kroj s edelweiss (alpská tráva), sýrařská halena (Kühermutz)",
    "CYP": "Vraka (černé pytlovité kalhoty), vyšívaná vesta",
    "CZE": "Moravský kroj, Modrotisková košile/šaty",
    "DEU": "Dirndl, Lederhosen, Trachtenjanker (vlněné sako)",
    "DNK": "Pletený svetr (Lusekofte styl), námořnické prvky",
    "ESP": "Flamenco šaty (traje de flamenca), Sombrero cordobés",
    "EST": "Pruhované sukně (každá farnost má svou barvu), vlněné svetry",
    "FIN": "Tradiční kroj (Kansallispuku), sobí kůže (Sámové)",
    "FRA": "Baret, pruhované triko (Marinière), šátek",
    "GBR": "Tweedové sako, Buřinka (Bowler hat), Kilt (Skotsko)",
    "GRC": "Foustanella (skládaná suknice), střevíce Tsarouhi s bambulí",
    "HRV": "Kravata (původ v Chorvatsku), šestinský deštník (červený)",
    "HUN": "Vyšívaná zástěra, husarský kabátek (Dolman)",
    "IRL": "Aran svetr (tlustý vlněný), Leine (lněná tunika)",
    "ISL": "Lopapeysa (svetr s kruhovým vzorem), vlněné doplňky",
    "ITA": "Benátská maska, módní šala, Coppola (lidová bekovka)",
    "LIE": "Tracht (kroj s černou čelenkou pro ženy)",
    "LTU": "Lněná tunika, tkaný pás (Juosta), jantarové šperky",
    "LUX": "Modrý pracovní plášť, krajkové čepce",
    "LVA": "Ziemelmeita (koruna), pruhovaná a kostkovaná vlněná šála (Villaine)",
    "MCO": "Tradiční kroj (Monégasque costume), bílé a červené prvky",
    "MDA": "Vyšívaná lněná košile (ie), vesta z ovčí kůže (bondiță)",
    "MKD": "Červeno-černě vyšívaný kroj, vesta s mincemi",
    "MLT": "Għonnella (černý hedvábný plášť s kapucí - historické)",
    "MNE": "Džamadan (červená vesta se zlatou výšivkou), kroj (nošnje)",
    "NLD": "Dřeváky (Klompen), bílý čepec (Volendam styl)",
    "NOR": "Bunad (národní kroj s výšivkami a stříbrem)",
    "POL": "Krakovský kroj (květinová sukně, vesta s pavími pery)",
    "PRT": "Oblek Fado (černý plášť), pestrý šátek z Viana do Castelo",
    "ROU": "Ie (vyšívaná blůza - dědictví UNESCO), zástěra (Fota)",
    "RUS": "Sarafan (šatová sukně), Kokošník (čelenka), Rubáška",
    "SMR": "Ceremoniální uniformy, středověké kostýmy",
    "SRB": "Šajkača (vojenská čepice), Jelek (sametová vesta)",
    "SVK": "Kroj (Detva - krátká košile), valaška, krpce",
    "SVN": "Gorenjska noša (alpský kroj), karafiát v klopě",
    "SWE": "Sverigedräkten (modro-žlutý kroj), věneček z květin (Midsommar)",
    "TUR": "Fez (historické), Kaftan, Shalvar (široké kalhoty)",
    "UKR": "Vyshyvanka (vyšívaná košile), Vinok (květinový věnec)",
    "VAT": "Švýcarská garda (historická uniforma), duchovní oděv",
    "XKX": "Plis (bílá čepice), tradiční albánský kroj",

    # Asia
    "AFG": "Perahan Tunban (volná košile a kalhoty), Pakol (čepice)",
    "ARE": "Kandura (bílá tunika), Ghutra (šátek na hlavě)",
    "ARM": "Taraz (historický oděv), stříbrný pás, čelenka",
    "AZE": "Arkhalig (dlouhý kabát), papakha (kožešinová čepice)",
    "BGD": "Sárí (ženy), Lungi/Panjabi (muži)",
    "BHR": "Thobe (dlouhá košile), Shemagh (šátek)",
    "BRN": "Baju Kurung (tradiční malajský oděv), Songkok (čepice)",
    "BTN": "Gho (mužské roucho), Kira (ženské zavinovací šaty)",
    "CHN": "Qipao (šaty s límečkem), Hanfu (historický oděv), Mao oblek",
    "GEO": "Chokha (kabát s nábojovými pásy), papakha",
    "HKG": "Moderní business styl, historicky Cheongsam",
    "IDN": "Batikovaná košile (Batik - UNESCO), Sarong",
    "IND": "Sárí, Kurta, Turban (Sikhové), Sherwani",
    "IRN": "Chador (ženy), perské vzory, termeh (brokát)",
    "IRQ": "Dishdasha (tunika), Keffiyeh (šátek)",
    "ISR": "Kippah (jarmulka), Tallit (modlitební šál), sandály",
    "JPN": "Kimono, Yukata (letní verze), Geta (dřeváky)",
    "KAZ": "Chapan (kabát), Saukele (vysoký klobouk pro nevěsty)",
    "KGZ": "Kalpak (vysoký bílý plstěný klobouk), plášť",
    "KHM": "Krama (tradiční šachovnicový šátek), Sampot",
    "KOR": "Hanbok (tradiční oděv s pestrými barvami a stuhou)",
    "KWT": "Dishdasha, Gutra a Igal (černá obruč na šátku)",
    "LAO": "Sinh (hedvábná sukně), Salong (kalhoty)",
    "LBN": "Sherwal (pytlovité kalhoty), Tantour (vysoký klobouk - hist.)",
    "LKA": "Sárí (Kandyan styl), Sarong",
    "MAC": "Portugalsko-čínský mix, Cheongsam",
    "MDV": "Libaas (šaty se zlatou výšivkou), Mundu",
    "MMR": "Longyi (zavinovací sukně pro muže i ženy)",
    "MNG": "Deel (dlouhý plášť s pásem), kožešinová čepice",
    "MYS": "Baju Melayu (košile), Baju Kurung, Songket (tkanina)",
    "NPL": "Daura-Suruwal (mužský oděv), Topi (čepice), Gunyo Cholo",
    "OMN": "Dishdasha (často barevná), Khanjar (dýka za pasem), Kuma (čepička)",
    "PAK": "Shalwar Kameez (dlouhá košile a kalhoty), vesta",
    "PHL": "Barong Tagalog (vyšívaná košile z ananasového vlákna)",
    "PRK": "Choson-ot (Hanbok), uniformní styl",
    "PSE": "Keffiyeh (černobílý šátek)",
    "QAT": "Thobe (bílá tunika, naškrobená), Ghutra",
    "SAU": "Thobe, Shemagh (červenobílý šátek), Abaya",
    "SGP": "Peranakan Kebaya (vyšívaná blůza), moderní fusion",
    "SYR": "Shirwal, Abaya, šátky s damaškovým vzorem",
    "THA": "Chut Thai (hedvábné roucha), Sabai (šál přes rameno)",
    "TJK": "Chapan, Tubeteika (čepička)",
    "TKM": "Telpek (velká ovčí čepice), červené šaty",
    "TWN": "Qipao, tradiční oděvy domorodých kmenů (Ami)",
    "UZB": "Ikat (vzorovaná látka Atlas), Doppa (hranatá čepička)",
    "VNM": "Ao Dai (dlouhá tunika s rozparky a kalhotami), Nón Lá (kuželový klobouk)",
    "YEM": "Thobe, Jambiya (dýka), Ma'awaz (suknice)",

    # Americas
    "ARG": "Pončo, bombachas (jezdecké kalhoty), baret (Gaucho styl)",
    "ATG": "Madras (pestrá kostkovaná látka), tradiční karibský styl",
    "BHS": "Androsia (batikovaná látka), slaměný klobouk",
    "BLZ": "Mestizo huipil (vyšívaná halena), květinové vzory",
    "BOL": "Buřinka (Cholas), Pollera (nařasená sukně), Aguayo (šátek)",
    "BRA": "Havaianas, karnevalové masky, fotbalový dres (seleção)",
    "BRB": "Barva akvamarínu a žluté, formální koloniální styl",
    "CAN": "Flanelová košile (Lumberjack), vlněná čepice (Toque), parka",
    "CHL": "Pončo (Chamanto), Huaso klobouk (široký, plochý)",
    "COL": "Sombrero Vueltiao (černobílý klobouk), Ruana (pončo)",
    "CRI": "Bílá rolnická košile, červený šátek, květ ve vlasech",
    "CUB": "Guayabera (košile se 4 kapsami), slaměný klobouk",
    "DOM": "Barvy vlajky, lehké lněné oblečení, merengue šaty",
    "ECU": "Panama klobouk (pochází odtud!), vlněné pončo",
    "GRD": "Oblečení s motivem muškátového oříšku, batika",
    "GTM": "Huipil (tkaná blůza s mayskými vzory), Corte (sukně)",
    "GUY": "Madras, košile a la Shirt-jac",
    "HND": "Lencas kroj (zářivé barvy), bílo-červené šaty",
    "HTI": "Karabela (džínové šaty), šátky na hlavu",
    "JAM": "Rasta barvy (zelená, žlutá, červená), háčkovaná čepice (Tam)",
    "KNA": "Národní kroj inspirovaný africkým a evropským stylem",
    "LCA": "Madras (Wob Dwiyet), kreolský kroj",
    "MEX": "Sombrero, Pončo, China Poblana (vyšívané šaty), Mariachi oblek",
    "NIC": "Huipil, bílé kalhoty, slaměný klobouk, šátek",
    "PAN": "Pollera (bohatě zdobené šaty), Sombrero Pintao",
    "PER": "Chullo (ušanka z lamy), Pončo, barevné textilie",
    "PRY": "Ao Po'i (vyšívaná košile), Ñandutí (krajka)",
    "SLV": "Bílé bavlněné šaty s barevným lemováním, šátek",
    "SUR": "Koto (tradiční sukně a šátek Angisa - vzkazy v uvázání)",
    "TTO": "Karnevalový kostým (peří, flitry), červená a černá",
    "URY": "Gaucho styl, baret, pončo, šátek kolem krku",
    "USA": "Džíny (Denim), kovbojské boty, baseballová čepice, univerzitní mikina",
    "VCT": "Batikované látky, pestré barvy",
    "VEN": "Liqui liqui (bílý oblek se stojáčkem), alpargatas (sandály)",
    
    # Africa
    "AGO": "Samakaka (látka s geometrickými vzory), bubu",
    "BDI": "Imvutano (tóga přes jedno rameno)",
    "BEN": "Bomba (tunika), krajkové látky, Gele (šátek)",
    "BFA": "Faso Dan Fani (pruhovaná bavlněná látka)",
    "BWA": "Leteisi (německý potisk - modrotisk), kůže, hnědá a modrá",
    "CAF": "Pagne (zavinovací sukně), pestré bavlněné látky",
    "CIV": "Kente, Kita (tradiční látka), Boubou",
    "CMR": "Kaba (šaty), Toghu (vyšívaný černý samet)",
    "COD": "Liputa (barevné látky se vzkazy), oblek Abacost",
    "COG": "Sapeurs (švihácký dandy styl), barevné obleky",
    "COM": "Shiromani (šátek/závoj), Kofia (čepička)",
    "CPV": "Pano de terra (tkaná látka), jednoduché bavlněné oděvy",
    "DJI": "Macawiis (sarong), Dirac (lehké šaty)",
    "DZA": "Karakou (vyšívaný kabátek), Burnous (vlněný plášť)",
    "EGY": "Galabeya (dlouhá volná tunika), Fez, zlaté šperky",
    "ERI": "Zuria (bílé šaty se zlatou výšivkou)",
    "ETH": "Habesha kemis (bílé šaty s barevným lemem), Netela (šál)",
    "GAB": "Tradiční masky (pro dekor), rafie, látka s potiskem",
    "GHA": "Kente (pestrobarevná tkaná látka), korálky, Fugu",
    "GIN": "Lepi (indigo látka), Boubou",
    "GMB": "Grand Boubou, Kaftan, špičaté kožené pantofle",
    "GNB": "Pente (tkaná látka), tradiční kroj",
    "GNQ": "Abalá (šaty), přírodní materiály a španělský vliv",
    "KEN": "Masajská shuka (červený károvaný pléd), korálkové šperky",
    "LBR": "Venkovský styl, košile ve stylu Vai, pestré šátky",
    "LBY": "Jerd (bílý vlněný plášť), tagiyah (čepička)",
    "LSO": "Mokorotlo (basothský slaměný klobouk), vlněná deka",
    "MAR": "Djellaba (plášť s kapucí), Babouche (pantofle), Kaftan",
    "MDG": "Lamba (tradiční pruh látky nošený přes rameno)",
    "MLI": "Bògòlanfini (látka barvená blátem), Boubou",
    "MOZ": "Capulana (barevná potištěná látka nošená jako sukně)",
    "MRT": "Daraa (modrá volná tunika), Melehfa (závoj)",
    "MUS": "Sárí (indický vliv), Sega šaty (široké sukně)",
    "MWI": "Chitenje (zavinovací sukně), košile s potiskem",
    "NAM": "Herero šaty (viktoriánský styl s 'kravím' čepcem)",
    "NER": "Tuaregský turban (Tagelmust - indigo), kožené amulety",
    "NGA": "Agbada (velké roucho), Gele (vázaný šátek), Ankara",
    "RWA": "Mushanana (šaty na jedno rameno), čelenka",
    "SDN": "Jalabiya (bílá tunika), Tobe (dámský závoj)",
    "SEN": "Boubou (bohatý, naškrobený oděv), špičaté boty",
    "SLE": "Ronko (tradiční košile), gara (batika)",
    "SOM": "Macawiis (sarong), Koofiyad (čepička), Dirac",
    "SSD": "Lau (tradiční oděv), korálkové korzety",
    "STP": "Pestré šátky, jednoduchý ostrovní styl",
    "SWZ": "Emahiya (zavinovací látka), štít a kopí (symbolicky)",
    "SYC": "Slaměný klobouk (Kazak), květinové vzory, pareo",
    "TCD": "Jalabiya, turban, světlé látky do pouště",
    "TGO": "Pagne (voskovaný potisk), korálky",
    "TUN": "Chéchia (červená čepice), Jebba (tunika)",
    "TZA": "Kanga (látka s příslovím), Kitenge",
    "UGA": "Gomesi (šaty se špičatými rameny a šerpou), Kanzu",
    "ZAF": "Shweshwe (potištěná látka), Madiba shirt, Ndebele korálky",
    "ZMB": "Chitenge outfit, moderní africký print",
    "ZWE": "Oděv s potiskem ptáka Zimbabwe, barevné šátky",

    # Oceania
    "AUS": "Akubra (klobouk), Cork hat, plážový styl, Blundstones",
    "FJI": "Sulu (zavinovací sukně pro muže i ženy), květinový vzor",
    "FSM": "Lava-lava (sukně), věnce z květin (Mwaramwar)",
    "KIR": "Te Tibuta (blůza), rohože z pandánu",
    "MHL": "Amimono (ruční práce), Jaki-ed (rohož-oděv)",
    "NRU": "Letní šaty, ostrovní motivy, květiny",
    "NZL": "Maori: Plášť z peří (Korowai), Jadeit (Pounamu), All Blacks dres",
    "PLW": "Barevné košile, tropický styl",
    "PNG": "Bilum (tkaná taška/čepice), nátěry na tělo, peří",
    "SLB": "Lava-lava, přírodní ozdoby z mušlí",
    "TON": "Ta'ovala (rohož kolem pasu), Tupenu",
    "TUV": "Fou (květinový věnec), barevné sukně",
    "VUT": "Ostrovní šaty (Mother Hubbard dress), barvy",
    "WSM": "Lava-lava, Puletasi (tradiční šaty), tetování (symbolicky)",
}

def update_clothing():
    try:
        with open('countries.json', 'r', encoding='utf-8') as f:
            countries = json.load(f)
        
        updated_count = 0
        
        for country in countries:
            cca3 = country.get('cca3')
            
            # Check if we have specific data for this country
            if cca3 in clothing_map:
                # Update clothing
                if 'culture' not in country:
                    country['culture'] = {}
                
                # We overwrite specific value
                country['culture']['clothing'] = clothing_map[cca3]
                updated_count += 1
            else:
                # Fallbacks for regions if specific country is missing but region exists
                # (This part handles smaller islands or unlisted countries)
                region = country.get('region')
                subregion = country.get('subregion')
                
                # Basic Fallbacks
                fallback = ""
                if region == "Europe":
                    fallback = "Místní kroj, slavnostní vesty, barvy vlajky"
                elif region == "Asia":
                    fallback = "Hedvábí, tradiční tunika, sarong nebo kaftan"
                elif region == "Africa":
                    fallback = "Pestré látky (Pagne/Kanga), šátky na hlavu"
                elif region == "Oceania":
                    fallback = "Květinové věnce, sukně z trávy/látky, pareo"
                elif region == "Americas" and subregion == "Caribbean":
                    fallback = "Madras (kostkovaná látka), slaměný klobouk, světlé barvy"
                elif region == "Americas" and subregion == "South America":
                    fallback = "Pončo, vlna z lamy, pestré tkané vzory"
                elif region == "Americas": # North/Central
                    fallback = "Džíny, kožené doplňky, domorodé vzory"
                
                if fallback and ('culture' not in country or 'clothing' not in country['culture'] or "Smart casual" in country['culture']['clothing']):
                     if 'culture' not in country: country['culture'] = {}
                     country['culture']['clothing'] = fallback
                     updated_count += 1

        with open('countries.json', 'w', encoding='utf-8') as f:
            json.dump(countries, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully updated specific clothing for {updated_count} countries.")

    except Exception as e:
        print(f"Error updating clothing: {e}")

if __name__ == "__main__":
    update_clothing()
