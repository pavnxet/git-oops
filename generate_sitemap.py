import json
from datetime import datetime

with open('gitoops/data/scenarios.json', 'r') as f:
    scenarios = json.load(f)

base_url = "https://gitoops.github.io"
today = datetime.now().strftime("%Y-%m-%d")

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{base_url}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>{base_url}/about.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
"""

for scenario in scenarios:
    sitemap_content += f"""  <url>
    <loc>{base_url}/scenario.html?id={scenario['id']}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""

sitemap_content += "</urlset>\n"

with open('gitoops/sitemap.xml', 'w') as f:
    f.write(sitemap_content)
