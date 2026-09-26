"""Product data for every brand page + card renderer."""
from layout import wa
from icons import i

AP = "https://www.asianpaints.com"
BG = "https://www.bergerpaints.com/products"
BO = "https://www.birlaopus.com/paint-products"


def P(slug, name, desc, chips, url, tier=None, cat="", tags="", cover=False):
    return dict(slug=slug, name=name, desc=desc, chips=chips, url=url, tier=tier, cat=cat, tags=tags, cover=cover)


# ---------------- Asian Paints ----------------
ASIAN = {
    "interior_luxury": [
        P("tractor-emulsion", "Tractor Emulsion", "Smooth finish with superior washability and no shade fading.",
          ["4-year warranty", "Washable", "Smooth matt"], AP + "/paint-products/interior-wall-paints/plain-finishes/tractor-emulsion.html", "luxury", "Interior Emulsion"),
        P("apcolite-premium-emulsion", "Apcolite Premium Emulsion", "Stain Guard technology keeps walls clean; easy to wash.",
          ["5-year warranty", "Stain Guard", "Washable"], AP + "/paint-products/interior-wall-paints/plain-finishes/apcolite-premium-emulsion.html", "luxury", "Interior Emulsion"),
        P("apcolite-shyne", "Apcolite Shyne", "Rich sheen finish with excellent washability for a premium look.",
          ["Sheen finish", "Washable", "Premium look"], AP + "/paint-products/interior-wall-paints/plain-finishes/apcolite-advanced-shyne-premium-emulsion.html", "luxury", "Interior Emulsion"),
    ],
    "interior_economy": [
        P("tractor-uno", "Tractor Uno Distemper", "Affordable acrylic distemper for a fresh, clean look on a budget.",
          ["Budget friendly", "Acrylic distemper", "2L to 20L"], AP + "/paint-products/interior-wall-paints/plain-finishes/tractor-uno.html", "economy", "Distemper"),
        P("neo-bharat-interior", "Neo Bharat Latex (Interior)", "High coverage and a smooth finish in 1000+ shades.",
          ["High coverage", "1000+ shades", "Smooth finish"], AP + "/paint-products/interior-wall-paints/plain-finishes/neobharat-latex-interior-paint.html", "economy", "Interior Paint"),
        P("tractor-sparc", "Tractor Sparc", "1.5x more coverage than distemper with better whiteness.",
          ["2-year warranty", "1.5x coverage", "Better whiteness"], AP + "/paint-products/interior-wall-paints/plain-finishes/tractor-sparc.html", "economy", "Interior Emulsion"),
    ],
    "exterior_luxury": [
        P("apex-shyne", "Apex Shyne Dust Proof", "High-sheen exterior finish that resists dust and algae.",
          ["6-year warranty", "Dust proof", "Anti-algal"], AP + "/paint-products/exterior-wall-paints/apex-shyne.html", "luxury", "Exterior Emulsion"),
        P("apex-dustproof", "Apex Dust Proof Emulsion", "Dust-proof technology with high washability for outside walls.",
          ["6-year warranty", "Dust proof", "Washable"], AP + "/paint-products/exterior-wall-paints/apex-dustproof-emulsion.html", "luxury", "Exterior Emulsion"),
    ],
    "exterior_economy": [
        P("neo-bharat-exterior", "Neo Bharat Latex (Exterior)", "Durable, weather-resistant exterior paint in 1000+ shades.",
          ["Weather resistant", "1000+ shades", "Budget friendly"], AP + "/paint-products/exterior-wall-paints/neobharat-latex-exterior-paint.html", "economy", "Exterior Paint"),
        P("ace-sparc", "Ace Sparc", "Value-for-money exterior emulsion with vibrant shades.",
          ["2-year warranty", "Vibrant shades", "Value for money"], AP + "/paint-products/exterior-wall-paints/ace-sparc.html", "economy", "Exterior Emulsion"),
        P("ace-shyne", "Ace Shyne", "High-sheen finish with water resistance for outside walls.",
          ["4-year warranty", "High sheen", "Water resistant"], AP + "/paint-products/exterior-wall-paints/ace-shyne.html", "economy", "Exterior Emulsion"),
        P("ace-power-plus", "Ace Power+", "Anti-fade technology and weather guard with a stylish matt finish.",
          ["4-year warranty", "Anti-fade", "Matt finish"], AP + "/paint-products/exterior-wall-paints/ace-power-plus.html", "economy", "Exterior Emulsion"),
    ],
    "waterproofing": [
        P("smartcare-damp-proof", "SmartCare Damp Proof", "Two-coat protection for terraces and exterior walls against seepage and damp patches.",
          ["10-year warranty", "Heat reduction", "Terrace"], AP + "/waterproofing-products/smartcare-damp-proof.html", None, "Waterproofing", "terrace exterior"),
        P("hydroloc-xtreme", "SmartCare Hydroloc Xtreme", "Advanced waterproofing membrane for roofs, tanks and wet areas.",
          ["5-year warranty", "Membrane", "Roof &amp; tanks"], AP + "/waterproofing-products/hydroloc-xtreme.html", None, "Waterproofing", "terrace bathrooms"),
        P("damp-block-2k", "SmartCare Damp Block 2K", "Two-component waterproof coating for interior and exterior walls.",
          ["3-year warranty", "2-component", "Walls &amp; bathrooms"], AP + "/waterproofing-products/smartcare-damp-block-2k.html", None, "Waterproofing", "interior exterior bathrooms"),
        P("damp-sheath-exterior", "SmartCare Damp Sheath Exterior", "Waterproof base coat for exterior plaster, applied before paint.",
          ["5-year warranty", "Exterior walls", "Under paint"], AP + "/waterproofing-products/damp-sheath-exterior.html", None, "Waterproofing", "exterior"),
        P("damp-sheath-interior", "SmartCare Damp Sheath Interior", "Anti-damp coating that stops dampness on interior walls.",
          ["3-year warranty", "Anti-damp", "Interior walls"], AP + "/waterproofing-products/smartcare-damp-sheath-interior.html", None, "Waterproofing", "interior"),
        P("crack-seal", "SmartCare Crack Seal", "Fills fine cracks on walls and stops water seepage.",
          ["Fine cracks", "Stops seepage", "Easy to apply"], AP + "/waterproofing-products/smartcare-crack-seal.html", None, "Cracks &amp; Joints", "cracks exterior"),
        P("repair-polymer", "SmartCare Repair Polymer", "Bonding agent to repair floors, chajjas, beams and slabs.",
          ["Bonding agent", "Repairs", "Concrete"], AP + "/waterproofing-products/smartcare-repair-polymer.html", None, "Cracks &amp; Joints", "cracks terrace"),
        P("tile-adhesive", "SmartCare Tile Adhesive", "High-bond adhesive for ceramic, vitrified and glass tiles.",
          ["High bond", "Vitrified tiles", "Floors &amp; walls"], AP + "/waterproofing-products/smartcare-tile-adhesive.html", None, "Tiling", "tiling bathrooms"),
    ],
    "putty": [
        P("acrylic-wall-putty", "TruCare Acrylic Wall Putty", "Ready-to-use acrylic putty with a strong grip for a long-lasting finish.",
          ["Ready to use", "Strong grip", "Interior"], AP + "/paint-products/interior-wall-paints/plain-finishes/acrylic-wall-putty.html", None, "Wall Putty"),
        P("trucare-putty", "TruCare Powder Acrylic Putty", "Gives a marble-like, ultra-smooth base for glossy topcoats.",
          ["Ultra smooth", "Powder", "Interior &amp; exterior"], AP + "/products/undercoats/trucare-powder-acrylic-putty.html", None, "Wall Putty"),
        P("waterproofing-putty", "SmartCare Waterproofing Putty", "Smooth base for damp-prone walls with water and efflorescence resistance.",
          ["Water resistant", "Anti-efflorescence", "1 kg to 40 kg"], AP + "/waterproofing-products/smartcare-waterproofing-putty.html", None, "Wall Putty"),
    ],
    "primer_interior": [
        P("trucare-interior-primer", "TruCare Interior Wall Primer", "Strong adhesion of the paint film on interior walls.",
          ["Strong adhesion", "Interior", "Smooth base"], AP + "/products/undercoats/trucare-interior-wall-primer-solvent-thinnable.html", None, "Interior Primer"),
        P("sparc-interior-primer", "Sparc Interior Primer", "Excellent whiteness and a smooth surface for your topcoat.",
          ["Whiteness", "Adhesion", "Economical"], AP + "/products/undercoats/sparc-interior-primer.html", None, "Interior Primer"),
    ],
    "primer_exterior": [
        P("trucare-exterior-primer", "TruCare Exterior Wall Primer Advanced", "Balance of whiteness, adhesion and topcoat finish for outside walls.",
          ["Advanced", "Adhesion", "Exterior"], AP + "/products/undercoats/trucare-exterior-wall-primer-advanced.html", None, "Exterior Primer"),
        P("sparc-exterior-primer", "Sparc Exterior Primer", "Smooth, white base with strong adhesion for long-lasting exteriors.",
          ["Whiteness", "Strong adhesion", "Economical"], AP + "/products/undercoats/sparc-exterior-primer.html", None, "Exterior Primer"),
    ],
    "enamel": [
        P("apcolite-gloss-enamel", "Apcolite Premium Gloss Enamel", "Lustrous, durable gloss finish for doors, windows and grills.",
          ["High gloss", "Wood &amp; metal", "Premium"], AP + "/enamel-paints/apcolite-premium-gloss-enamel.html", None, "Enamel"),
        P("apcolite-satin-enamel", "Apcolite Premium Satin Enamel", "Soft sheen enamel for a rich, elegant look on wood and metal.",
          ["Soft sheen", "Wood &amp; metal", "Premium"], AP + "/enamel-paints/apcolite-premium-satin-enamel.html", None, "Enamel"),
        P("tractor-enamel", "Tractor Enamel", "Long-lasting glossy finish for metal and wood at a great price.",
          ["Glossy", "Long lasting", "Economical"], AP + "/enamel-paints/tractor-enamel.html", None, "Enamel"),
        P("tractor-sparc-enamel", "Tractor Sparc Enamel", "Affordable high-sheen enamel for homes and small projects.",
          ["High sheen", "Affordable", "Wood &amp; metal"], AP + "/enamel-paints/tractor-sparc-enamel.html", None, "Enamel"),
    ],
}

# ---------------- Berger Paints ----------------
BERGER = [
    P("walmasta-lite", "Walmasta Lite", "The most economical exterior emulsion from Berger, with anti-algal and anti-fungal protection.",
      ["Most economical", "Anti-algal", "Exterior"], BG + "/exterior-wall-coatings/walmasta-lite", "economy", "Exterior Emulsion", "exterior", True),
    P("walmasta", "Walmasta", "Anti-fungal exterior emulsion with an excellent matt finish.",
      ["4-year warranty", "Matt finish", "Anti-fungal"], BG + "/exterior-wall-coatings/walmasta", "economy", "Exterior Emulsion", "exterior", True),
    P("weathercoat-glow", "WeatherCoat Glow", "100% acrylic outdoor paint with a rich sheen and stay-clean formula for Indian weather.",
      ["7-year warranty", "Rich sheen", "Stay clean"], BG + "/exterior-wall-coatings/weathercoat-glow", "economy", "Exterior Emulsion", "exterior", True),
    P("bison-wall-putty", "Bison Wall Putty", "Cement-based putty for interior and exterior walls: a smooth, even base before painting.",
      ["Cement based", "Interior &amp; exterior", "Smooth base"], BG + "/putty-and-cement-paint/bison-wall-putty", None, "Wall Putty", "putty", True),
    P("happy-wall-putty", "Happy Walls Acrylic Putty", "Butter-smooth acrylic putty with excellent filling and levelling.",
      ["Easy to apply", "Alkali resistant", "Acrylic"], BG + "/putty-and-cement-paint/happy-wall-acrylic-putty", None, "Wall Putty", "putty", True),
    P("bp-white-primer", "BP White Primer", "Premium white primer that makes colours look brighter, with chalking resistance.",
      ["Interior", "Easy to brush", "Green Pro"], BG + "/primers/bp-white-primer", None, "Interior Primer", "primer", True),
    P("bp-cement-primer-wt", "BP Cement Primer (WT)", "Acrylic, anti-alkali cement primer for strong adhesion and a flawless base.",
      ["Interior &amp; exterior", "Anti-alkali", "Water thinnable"], BG + "/primers/bp-cement-primer-wt", None, "Cement Primer", "primer", True),
    P("bp-exterior-primer", "BP Exterior Cement Primer", "Durable exterior primer for long-lasting protection and brighter topcoats.",
      ["Exterior", "Durable", "Green Pro"], BG + "/primers/bp-exterior-cement-primer", None, "Exterior Primer", "primer", True),
    P("walmasta-primer", "Walmasta Exterior &amp; Interior Primer", "Easy to apply with great coverage and whiteness; resists chalking.",
      ["Interior &amp; exterior", "Great coverage", "Green certified"], BG + "/primers/walmasta-exterior-interior-primer", None, "Primer", "primer", True),
]

# ---------------- Birla Opus ----------------
BIRLA = {
    "exterior": [
        P("style-power-bright", "Style Power Bright", "Peel-proof protection with a bright, long-lasting finish for exterior walls.",
          ["Peel protection", "High coverage", "Low odour"], BO + "/exterior-wall-paint/style-power-bright", "economy", "Exterior Emulsion"),
        P("style-power-fit", "Style Power Fit", "Bright emulsion that hides hairline cracks and resists fading.",
          ["Crack hiding", "Fade resistant", "Anti-chalking"], BO + "/exterior-wall-paint/style-power-fit", "economy", "Exterior Emulsion"),
        P("calista-neo-star-shine", "Calista Neo Star Shine", "Premium sheen finish that is algae-proof and dust-resistant.",
          ["Algae proof", "Dust resistant", "Sheen finish"], BO + "/exterior-wall-paint/calista-neo-star-shine", "luxury", "Premium Emulsion"),
    ],
    "putty": [
        P("one-pro-smooth-putty", "One Pro Smooth Putty", "Acrylic wall putty for a smooth, even surface and a flawless paint finish.",
          ["Acrylic", "Smooth finish", "Interior"], BO + "/interior-wall-paint/one-pro-smooth-putty", None, "Wall Putty"),
    ],
    "primer_interior": [
        P("style-pro-hide-primer", "Style Pro Hide Primer", "Primer and topcoat in one, with low odour and excellent coverage.",
          ["2-in-1", "Low odour", "Coverage"], BO + "/interior-wall-paint/style-pro-hide-primer", None, "Interior Primer"),
        P("calista-pro-white-primer", "Calista Pro White Primer", "Smooth white base with excellent adhesion for interior walls.",
          ["Premium", "Adhesion", "Water thinnable"], BO + "/interior-wall-paint/calista-pro-white-primer", None, "Interior Primer"),
    ],
    "primer_exterior": [
        P("style-perfect-start-primer", "Style Perfect Start Primer", "Peel-proof exterior primer that brightens walls and gives a smooth base.",
          ["Peel proof", "Brightness", "Exterior"], BO + "/exterior-wall-paint/style-perfect-start-primer", None, "Exterior Primer"),
        P("calista-perfect-choice-primer", "Calista Perfect Choice Primer", "Premium water-thinnable exterior primer for Calista and One topcoats.",
          ["Premium", "Water thinnable", "Exterior"], BO + "/exterior-wall-paint", None, "Exterior Primer"),
    ],
}

# ---------------- Forever ----------------
FOREVER = [
    P("forever-emulsion", "Forever Emulsions", "Interior and exterior emulsions in a wide range of shades, at a pocket-friendly price.",
      ["Interior &amp; exterior", "Washable", "Many shades"], "https://paintsforever.net/", None, "Emulsion"),
    P("forever-primer", "Forever Primer", "Interior and exterior wall primers for strong adhesion and a smooth base.",
      ["Interior &amp; exterior", "Adhesion", "Smooth base"], "https://paintsforever.net/", None, "Primer"),
    P("forever-putty", "Forever Rustic Putty", "Wall putty that fills uneven surfaces and gives a smooth finish before paint.",
      ["Fills gaps", "Smooth finish", "Walls"], "https://paintsforever.net/", None, "Putty"),
]

BRAND_LABEL = {"asian": "Asian Paints", "berger": "Berger Paints", "birla": "Birla Opus", "forever": "Forever Paints"}


def card(p, brand):
    img = f"images/products/{brand}/{p['slug']}.webp"
    tier = ""
    if p["tier"] == "luxury":
        tier = f'<span class="tier tier--luxury">Luxury</span>'
    elif p["tier"] == "economy":
        tier = '<span class="tier tier--economy">Economy</span>'
    chips = "".join(f"<li>{c}</li>" for c in p["chips"])
    tags = f' data-tags="{p["tags"]}"' if p["tags"] else ""
    name_plain = p["name"].replace("&amp;", "&")
    msg = f"Namaste Rana Paints! Please share price and details of {name_plain} ({BRAND_LABEL[brand]})."
    cover = " product__img--cover" if p["cover"] else ""
    return f"""<article class="product"{tags}>
  {tier}
  <div class="product__img{cover}"><img src="{img}" alt="{p['name']} by {BRAND_LABEL[brand]}" loading="lazy" width="600" height="600"></div>
  <div class="product__body">
    <span class="product__cat">{p['cat']}</span>
    <h3>{p['name']}</h3>
    <p>{p['desc']}</p>
    <ul class="chips">{chips}</ul>
    <div class="product__actions">
      <a class="btn btn--sm btn--wa" href="{wa(msg)}" target="_blank" rel="noopener">{i('wa')} Enquire</a>
      <a class="link-arrow" href="{p['url']}" target="_blank" rel="noopener">Details {i('ext', '2')}</a>
    </div>
  </div>
</article>"""


def grid(items, brand, gid=""):
    idattr = f' id="{gid}"' if gid else ""
    return f'<div class="products"{idattr}>\n' + "\n".join(card(p, brand) for p in items) + "\n</div>"
