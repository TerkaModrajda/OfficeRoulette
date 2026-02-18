
import json

# Vibe palettes (NOT flag colors, but atmospheric/cultural colors)
vibe_palettes = {
    # Europe
    "CZE": ["#8B0000", "#DAA520", "#2F4F4F"], # Czech Garnet, Beer Gold, Forest Green
    "SVK": ["#4682B4", "#228B22", "#FFFFFF"], # Tatras Blue, Forest, Sheep Breeze (White)
    "FRA": ["#800020", "#F5F5DC", "#708090"], # Bordeaux Red, Cream (Bagutte/Stone), Slate Grey (Paris roofs)
    "ITA": ["#CE2029", "#556B2F", "#F4C430"], # Tomato Red, Olive/Basil Green, Pasta Gold
    "ESP": ["#E2725B", "#FFD700", "#800000"], # Terracotta, Saffron/Sun, Sangria Red
    "GBR": ["#1D1E33", "#C8102E", "#777B7E"], # Royal Navy, Bus Red, London Fog Grey
    "DEU": ["#2F3131", "#D4AF37", "#006400"], # Asphalt/Industry, Beer/Gold, Black Forest Green
    "GRC": ["#0047AB", "#F8F8FF", "#808000"], # Aegean Blue, Whitewashed Walls, Olive Oil
    "SWE": ["#7B9095", "#800000", "#E0C9A5"], # Nordic Grey, Falu Red (Cottages), Light Wood
    "NOR": ["#003366", "#FFFFFF", "#2E8B57"], # Fjord Blue, Snow, Pine
    "IRL": ["#0F4C35", "#B8860B", "#A9A9A9"], # Emerald Green, Guinness Dark/Gold, Stone
    "POL": ["#DC143C", "#F0E68C", "#8B4513"], # Poppy Red, Wheat, Wood
    "PRT": ["#007FFF", "#FFD700", "#FFFFFF"], # Azulejo Blue, Sun, White Tiles (keeping it distinct from Greece) -> actually lets do Cork/Port Wine
            # Revision for PRT:
            # Port Wine, Cork, Azulejo
    "PRT": ["#722F37", "#D2B48C", "#0067A5"], 
    "AUT": ["#C41E3A", "#D4C4A8", "#2F4F4F"], # Imperial Red, Architecture Beige, Alpine Green
    "BEL": ["#704214", "#F5F5DC", "#36454F"], # Chocolate, Waffle dough, Urban Grey
    "CHE": ["#FF0000", "#FFFFFF", "#A9A9A9"], # Swiss Red, Snow, Mountain Grey (keeping it simple but clean)
    "RUS": ["#D4AF37", "#8B0000", "#FFFFFF"], # Orthodox Gold, Red Square, Snow
    "UKR": ["#FFD700", "#0057B7", "#000000"], # Wheat Field, Sky Blue, Soil (Black Earth) -> Actually prefer Sunflowers