
import json

with open('countries.json', 'r') as f:
    countries = json.load(f)

incomplete_but_started = []
for c in countries:
    has_palette = c.get('culture', {}).get('palette') is not None
    has_gastronomy = c.get('gastronomy') and len(c['gastronomy']) > 0
    
    if has_palette and not has_gastronomy:
        incomplete_but_started.append(c['cca3'])

print("Countries with palette but no gastronomy:", incomplete_but_started)

empty_culture = [c['cca3'] for c in countries if not c.get('culture')]
print(f"Total empty culture: {len(empty_culture)}")
