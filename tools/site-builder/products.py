"""Product data for every page + the product card (with Add to cart).

Har product ke liye:  P(slug, name, desc, chips, url, ...)
  sizes = size ki list (dropdown banta hai)
  opts  = aur dropdowns, jaise [("Colour", [...])]
  fixed = fixed cheez jo cart mein jaati hai, jaise {"Size": "400 ml"}
  img   = photo ka rasta (na do toh images/products/<brand>/<slug>.webp)
  imgs  = option ke hisaab se photo badle, jaise {"12": "images/...webp"}
"""
import json
from html import escape
from layout import wa
from icons import i

AP = "https://www.asianpaints.com"
BG = "https://www.bergerpaints.com/products"
BO = "https://www.birlaopus.com/paint-products"

# ---- standard pack sizes (owner ne bataye) ----
EMUL = ["1 L", "4 L", "10 L", "20 L"]          # emulsions, wall primers, waterproofing liquids
DIST = ["1 kg", "5 kg", "10 kg", "20 kg"]      # distempers
ENAM = ["500 ml", "1 L", "4 L"]                # enamels + wood/metal primers
POWDER_PUTTY = ["20 kg", "40 kg"]
PASTE_PUTTY = ["1 kg", "5 kg", "20 kg"]
FIXIT = ["1 L", "5 L", "10 L", "20 L"]
ROLLER = ["2 inch", "4 inch", "9 inch"]
BRUSH = ["1 inch", "2 inch", "3 inch", "4 inch"]


def P(slug, name, desc, chips, url, tier=None, cat="", tags="", cover=False,
      sizes=None, opts=None, fixed=None, img=None, imgs=None):
    return dict(slug=slug, name=name, desc=desc, chips=chips, url=url, tier=tier, cat=cat, tags=tags,
                cover=cover, sizes=sizes, opts=opts or [], fixed=fixed or {}, img=img, imgs=imgs or {})


# ================================================================ Asian Paints
ASIAN = {
    "interior_luxury": [
        P("tractor-emulsion", "Tractor Emulsion", "Smooth finish with superior washability and no shade fading.",
          ["4-year warranty", "Washable", "Smooth matt"], AP + "/paint-products/interior-wall-paints/plain-finishes/tractor-emulsion.html", "luxury", "Interior Emulsion", sizes=EMUL),
        P("apcolite-premium-emulsion", "Apcolite Premium Emulsion", "Stain Guard technology keeps walls clean; easy to wash.",
          ["5-year warranty", "Stain Guard", "Washable"], AP + "/paint-products/interior-wall-paints/plain-finishes/apcolite-premium-emulsion.html", "luxury", "Interior Emulsion", sizes=EMUL),
        P("apcolite-shyne", "Apcolite Shyne", "Rich sheen finish with excellent washability for a premium look.",
          ["Sheen finish", "Washable", "Premium look"], AP + "/paint-products/interior-wall-paints/plain-finishes/apcolite-advanced-shyne-premium-emulsion.html", "luxury", "Interior Emulsion", sizes=EMUL),
    ],
    "interior_economy": [
        P("tractor-uno", "Tractor Uno Distemper", "Affordable acrylic distemper for a fresh, clean look on a budget.",
          ["Budget friendly", "Acrylic distemper", "Matt finish"], AP + "/paint-products/interior-wall-paints/plain-finishes/tractor-uno.html", "economy", "Distemper", sizes=DIST),
        P("neo-bharat-interior", "Neo Bharat Latex (Interior)", "High coverage and a smooth finish in 1000+ shades.",
          ["High coverage", "1000+ shades", "Smooth finish"], AP + "/paint-products/interior-wall-paints/plain-finishes/neobharat-latex-interior-paint.html", "economy", "Interior Paint", sizes=EMUL),
        P("tractor-sparc", "Tractor Sparc", "1.5x more coverage than distemper with better whiteness.",
          ["2-year warranty", "1.5x coverage", "Better whiteness"], AP + "/paint-products/interior-wall-paints/plain-finishes/tractor-sparc.html", "economy", "Interior Emulsion", sizes=EMUL),
    ],
    "exterior_luxury": [
        P("apex-shyne", "Apex Shyne Dust Proof", "High-sheen exterior finish that resists dust and algae.",
          ["6-year warranty", "Dust proof", "Anti-algal"], AP + "/paint-products/exterior-wall-paints/apex-shyne.html", "luxury", "Exterior Emulsion", sizes=EMUL),
        P("apex-dustproof", "Apex Dust Proof Emulsion", "Dust-proof technology with high washability for outside walls.",
          ["6-year warranty", "Dust proof", "Washable"], AP + "/paint-products/exterior-wall-paints/apex-dustproof-emulsion.html", "luxury", "Exterior Emulsion", sizes=EMUL),
    ],
    "exterior_economy": [
        P("neo-bharat-exterior", "Neo Bharat Latex (Exterior)", "Durable, weather-resistant exterior paint in 1000+ shades.",
          ["Weather resistant", "1000+ shades", "Budget friendly"], AP + "/paint-products/exterior-wall-paints/neobharat-latex-exterior-paint.html", "economy", "Exterior Paint", sizes=EMUL),
        P("ace-sparc", "Ace Sparc", "Value-for-money exterior emulsion with vibrant shades.",
          ["2-year warranty", "Vibrant shades", "Value for money"], AP + "/paint-products/exterior-wall-paints/ace-sparc.html", "economy", "Exterior Emulsion", sizes=EMUL),
        P("ace-shyne", "Ace Shyne", "High-sheen finish with water resistance for outside walls.",
          ["4-year warranty", "High sheen", "Water resistant"], AP + "/paint-products/exterior-wall-paints/ace-shyne.html", "economy", "Exterior Emulsion", sizes=EMUL),
        P("ace-power-plus", "Ace Power+", "Anti-fade technology and weather guard with a stylish matt finish.",
          ["4-year warranty", "Anti-fade", "Matt finish"], AP + "/paint-products/exterior-wall-paints/ace-power-plus.html", "economy", "Exterior Emulsion", sizes=EMUL),
    ],
    "waterproofing": [
        P("smartcare-damp-proof", "SmartCare Damp Proof", "Two-coat protection for terraces and exterior walls against seepage and damp patches.",
          ["10-year warranty", "Heat reduction", "Terrace"], AP + "/waterproofing-products/smartcare-damp-proof.html", None, "Waterproofing", "terrace exterior", sizes=EMUL),
        P("hydroloc-xtreme", "SmartCare Hydroloc Xtreme", "Advanced waterproofing membrane for roofs, tanks and wet areas.",
          ["5-year warranty", "Membrane", "Roof &amp; tanks"], AP + "/waterproofing-products/hydroloc-xtreme.html", None, "Waterproofing", "terrace bathrooms", sizes=EMUL),
        P("damp-block-2k", "SmartCare Damp Block 2K", "Two-component waterproof coating for interior and exterior walls.",
          ["3-year warranty", "2-component", "Walls &amp; bathrooms"], AP + "/waterproofing-products/smartcare-damp-block-2k.html", None, "Waterproofing", "interior exterior bathrooms", sizes=["3 L", "15 L"]),
        P("damp-sheath-exterior", "SmartCare Damp Sheath Exterior", "Waterproof base coat for exterior plaster, applied before paint.",
          ["5-year warranty", "Exterior walls", "Under paint"], AP + "/waterproofing-products/damp-sheath-exterior.html", None, "Waterproofing", "exterior", sizes=EMUL),
        P("damp-sheath-interior", "SmartCare Damp Sheath Interior", "Anti-damp coating that stops dampness on interior walls.",
          ["3-year warranty", "Anti-damp", "Interior walls"], AP + "/waterproofing-products/smartcare-damp-sheath-interior.html", None, "Waterproofing", "interior", sizes=EMUL),
        P("crack-seal", "SmartCare Crack Seal", "Fills fine cracks on walls and stops water seepage.",
          ["Fine cracks", "Stops seepage", "Easy to apply"], AP + "/waterproofing-products/smartcare-crack-seal.html", None, "Cracks &amp; Joints", "cracks exterior", sizes=["1 kg", "5 kg"]),
        P("repair-polymer", "SmartCare Repair Polymer", "Bonding agent to repair floors, chajjas, beams and slabs.",
          ["Bonding agent", "Repairs", "Concrete"], AP + "/waterproofing-products/smartcare-repair-polymer.html", None, "Cracks &amp; Joints", "cracks terrace", sizes=EMUL),
        P("tile-adhesive", "SmartCare Tile Adhesive", "High-bond adhesive for ceramic, vitrified and glass tiles.",
          ["High bond", "Vitrified tiles", "Floors &amp; walls"], AP + "/waterproofing-products/smartcare-tile-adhesive.html", None, "Tiling", "tiling bathrooms", sizes=["20 kg"]),
    ],
    "putty": [
        P("acrylic-wall-putty", "TruCare Acrylic Wall Putty", "Ready-to-use acrylic putty with a strong grip for a long-lasting finish.",
          ["Ready to use", "Strong grip", "Interior"], AP + "/paint-products/interior-wall-paints/plain-finishes/acrylic-wall-putty.html", None, "Wall Putty", sizes=PASTE_PUTTY),
        P("trucare-putty", "TruCare Powder Acrylic Putty", "Gives a marble-like, ultra-smooth base for glossy topcoats.",
          ["Ultra smooth", "Powder", "Interior &amp; exterior"], AP + "/products/undercoats/trucare-powder-acrylic-putty.html", None, "Wall Putty", sizes=POWDER_PUTTY),
        P("waterproofing-putty", "SmartCare Waterproofing Putty", "Smooth base for damp-prone walls with water and efflorescence resistance.",
          ["Water resistant", "Anti-efflorescence", "Damp walls"], AP + "/waterproofing-products/smartcare-waterproofing-putty.html", None, "Wall Putty", sizes=["1 kg", "20 kg", "40 kg"]),
    ],
    "primer_interior": [
        P("trucare-interior-primer", "TruCare Interior Wall Primer", "Strong adhesion of the paint film on interior walls.",
          ["Strong adhesion", "Interior", "Smooth base"], AP + "/products/undercoats/trucare-interior-wall-primer-solvent-thinnable.html", None, "Interior Primer", sizes=EMUL),
        P("sparc-interior-primer", "Sparc Interior Primer", "Excellent whiteness and a smooth surface for your topcoat.",
          ["Whiteness", "Adhesion", "Economical"], AP + "/products/undercoats/sparc-interior-primer.html", None, "Interior Primer", sizes=EMUL),
    ],
    "primer_exterior": [
        P("trucare-exterior-primer", "TruCare Exterior Wall Primer Advanced", "Balance of whiteness, adhesion and topcoat finish for outside walls.",
          ["Advanced", "Adhesion", "Exterior"], AP + "/products/undercoats/trucare-exterior-wall-primer-advanced.html", None, "Exterior Primer", sizes=EMUL),
        P("sparc-exterior-primer", "Sparc Exterior Primer", "Smooth, white base with strong adhesion for long-lasting exteriors.",
          ["Whiteness", "Strong adhesion", "Economical"], AP + "/products/undercoats/sparc-exterior-primer.html", None, "Exterior Primer", sizes=EMUL),
    ],
    "enamel": [
        P("apcolite-gloss-enamel", "Apcolite Premium Gloss Enamel", "Lustrous, durable gloss finish for doors, windows and grills.",
          ["High gloss", "Wood &amp; metal", "Premium"], AP + "/enamel-paints/apcolite-premium-gloss-enamel.html", None, "Enamel", sizes=ENAM),
        P("apcolite-satin-enamel", "Apcolite Premium Satin Enamel", "Soft sheen enamel for a rich, elegant look on wood and metal.",
          ["Soft sheen", "Wood &amp; metal", "Premium"], AP + "/enamel-paints/apcolite-premium-satin-enamel.html", None, "Enamel", sizes=ENAM),
        P("tractor-enamel", "Tractor Enamel", "Long-lasting glossy finish for metal and wood at a great price.",
          ["Glossy", "Long lasting", "Economical"], AP + "/enamel-paints/tractor-enamel.html", None, "Enamel", sizes=ENAM),
        P("tractor-sparc-enamel", "Tractor Sparc Enamel", "Affordable high-sheen enamel for homes and small projects.",
          ["High sheen", "Affordable", "Wood &amp; metal"], AP + "/enamel-paints/tractor-sparc-enamel.html", None, "Enamel", sizes=ENAM),
    ],
    "enamel_primer": [
        P("wood-primer", "TruCare Wood Primer", "Seals new wood and helps enamel stick well for a smooth finish.",
          ["For wood", "Good sealing", "Before enamel"], AP + "/products/undercoats/wood-primer.html", None, "Wood Primer", sizes=ENAM),
        P("red-oxide-metal-primer", "TruCare Red Oxide Metal Primer", "Rust protection for iron and steel gates, grills and windows before enamel.",
          ["For metal", "Rust protection", "Before enamel"], AP + "/enamel-paints/trucare-red-oxide-metal-primer.html", None, "Metal Primer", sizes=ENAM),
    ],
}

# ================================================================ Berger Paints
BERGER = [
    P("walmasta-lite", "Walmasta Lite", "The most economical exterior emulsion from Berger, with anti-algal and anti-fungal protection.",
      ["Most economical", "Anti-algal", "Exterior"], BG + "/exterior-wall-coatings/walmasta-lite", "economy", "Exterior Emulsion", "exterior", True, sizes=EMUL),
    P("walmasta", "Walmasta", "Anti-fungal exterior emulsion with an excellent matt finish.",
      ["4-year warranty", "Matt finish", "Anti-fungal"], BG + "/exterior-wall-coatings/walmasta", "economy", "Exterior Emulsion", "exterior", True, sizes=EMUL),
    P("weathercoat-glow", "WeatherCoat Glow", "100% acrylic outdoor paint with a rich sheen and stay-clean formula for Indian weather.",
      ["7-year warranty", "Rich sheen", "Stay clean"], BG + "/exterior-wall-coatings/weathercoat-glow", "economy", "Exterior Emulsion", "exterior", True, sizes=EMUL),
    P("bison-wall-putty", "Bison Wall Putty", "Cement-based putty for interior and exterior walls: a smooth, even base before painting.",
      ["Cement based", "Interior &amp; exterior", "Smooth base"], BG + "/putty-and-cement-paint/bison-wall-putty", None, "Wall Putty", "putty", True, sizes=POWDER_PUTTY),
    P("happy-wall-putty", "Happy Walls Acrylic Putty", "Butter-smooth acrylic putty with excellent filling and levelling.",
      ["Easy to apply", "Alkali resistant", "Acrylic"], BG + "/putty-and-cement-paint/happy-wall-acrylic-putty", None, "Wall Putty", "putty", True, sizes=PASTE_PUTTY),
    P("bp-white-primer", "BP White Primer", "Premium white primer that makes colours look brighter, with chalking resistance.",
      ["Interior", "Easy to brush", "Green Pro"], BG + "/primers/bp-white-primer", None, "Interior Primer", "primer", True, sizes=EMUL),
    P("bp-cement-primer-wt", "BP Cement Primer (WT)", "Acrylic, anti-alkali cement primer for strong adhesion and a flawless base.",
      ["Interior &amp; exterior", "Anti-alkali", "Water thinnable"], BG + "/primers/bp-cement-primer-wt", None, "Cement Primer", "primer", True, sizes=EMUL),
    P("bp-exterior-primer", "BP Exterior Cement Primer", "Durable exterior primer for long-lasting protection and brighter topcoats.",
      ["Exterior", "Durable", "Green Pro"], BG + "/primers/bp-exterior-cement-primer", None, "Exterior Primer", "primer", True, sizes=EMUL),
    P("walmasta-primer", "Walmasta Exterior &amp; Interior Primer", "Easy to apply with great coverage and whiteness; resists chalking.",
      ["Interior &amp; exterior", "Great coverage", "Green certified"], BG + "/primers/walmasta-exterior-interior-primer", None, "Primer", "primer", True, sizes=EMUL),
]

# ================================================================ Birla Opus (+ Birla White putty)
BW = "https://www.birlawhite.com/en/products/wall-putty"
WNR_IMG = "images/products/birla/wall-n-roof-10.webp"
BIRLA = {
    "exterior": [
        P("style-power-bright", "Style Power Bright", "Peel-proof protection with a bright, long-lasting finish for exterior walls.",
          ["Peel protection", "High coverage", "Low odour"], BO + "/exterior-wall-paint/style-power-bright", "economy", "Exterior Emulsion", sizes=EMUL),
        P("style-power-bright-shine", "Style Power Bright Shine", "The Power Bright range with a high-sheen finish that keeps outside walls looking fresh.",
          ["High sheen", "Peel protection", "Exterior"], BO + "/exterior-wall-paint/style-power-bright-shine", "economy", "Exterior Emulsion", sizes=EMUL),
        P("style-power-fit", "Style Power Fit", "Bright emulsion that hides hairline cracks and resists fading.",
          ["Crack hiding", "Fade resistant", "Anti-chalking"], BO + "/exterior-wall-paint/style-power-fit", "economy", "Exterior Emulsion", sizes=EMUL),
        P("calista-neo-star-shine", "Calista Neo Star Shine", "Premium sheen finish that is algae-proof and dust-resistant.",
          ["Algae proof", "Dust resistant", "Sheen finish"], BO + "/exterior-wall-paint/calista-neo-star-shine", "luxury", "Premium Emulsion", sizes=EMUL),
    ],
    "interior": [
        P("style-color-fresh", "Style Color Fresh", "Budget interior emulsion that freshens up walls with bright, even colour.",
          ["Economy", "Smooth finish", "Interior"], "https://www.birlaopus.com/products/interiors/style-color-fresh", "economy", "Interior Emulsion", sizes=EMUL),
        P("style-color-smart", "Style Color Smart", "Washable, mildew-proof interior emulsion with a smooth matt finish.",
          ["Washable", "Mildew proof", "Matt"], BO + "/interior-wall-paint/style-color-smart", "economy", "Interior Emulsion", sizes=EMUL),
        P("style-color-smart-shine", "Style Color Smart Shine", "Sheen finish with very good washability and anti-fungal protection, in 1800+ shades.",
          ["4-year warranty", "Sheen finish", "Anti-fungal"], BO + "/interior-wall-paint/style-color-smart-shine", "economy", "Interior Emulsion", sizes=EMUL),
        P("style-super-bright", "Style Super Bright Distemper", "Affordable distemper with good whiteness for a quick, clean refresh.",
          ["Distemper", "Budget friendly", "Bright white"], BO + "/interior-wall-paint/style-super-bright", "economy", "Distemper", sizes=DIST),
    ],
    "waterproofing": [
        P("wall-n-roof", "Alldry Wall n Roof", "All-in-one waterproofing coating for roofs and outside walls. The number (3, 4, 7, 10, 12) is the grade: a higher number gives longer protection.",
          ["Roof &amp; walls", "Heat reduction", "Water pressure resistant"], BO + "/waterproofing/alldry-wall-n-roof-10", None, "Waterproofing",
          opts=[("Grade", ["3", "4", "7", "10", "12"])], sizes=EMUL, img=WNR_IMG, imgs={"12": "images/products/birla/wall-n-roof-12.webp"}),
    ],
    "putty": [
        P("one-pro-smooth-putty", "One Pro Smooth Putty", "Acrylic wall putty for a smooth, even surface and a flawless paint finish.",
          ["Acrylic", "Smooth finish", "Interior"], BO + "/interior-wall-paint/one-pro-smooth-putty", None, "Wall Putty", sizes=PASTE_PUTTY),
        P("wallcare-putty", "Birla White WallCare Putty", "White cement-based putty with extra polymers for a smooth, bright and water-resistant base.",
          ["White cement", "Water resistant", "Normal"], BW + "/wallcare-putty", None, "Birla White Putty", sizes=POWDER_PUTTY, img="images/products/birla-white/wallcare-putty.webp"),
        P("wallseal-putty", "Birla White WallSeal Putty", "Waterproof putty for exterior and damp-prone walls, so paint lasts longer.",
          ["Waterproof", "Exterior", "Damp walls"], BW + "/wallseal-waterproof-putty", None, "Birla White Putty", sizes=POWDER_PUTTY, img="images/products/birla-white/wallseal-putty.webp"),
        P("texture-putty", "Birla Texture Putty", "Texture putty for designer textured wall finishes.",
          ["Texture finish", "25 kg bag", "Walls"], "https://www.birlaopus.com/", None, "Texture Putty", fixed={"Size": "25 kg bag"}, img="images/products/misc/texture-putty-bag.svg"),
    ],
    "primer_interior": [
        P("style-pro-hide-primer", "Style Pro Hide Primer", "Primer and topcoat in one, with low odour and excellent coverage.",
          ["2-in-1", "Low odour", "Coverage"], BO + "/interior-wall-paint/style-pro-hide-primer", None, "Interior Primer", sizes=EMUL),
        P("calista-pro-white-primer", "Calista Pro White Primer", "Smooth white base with excellent adhesion for interior walls.",
          ["Premium", "Adhesion", "Water thinnable"], BO + "/interior-wall-paint/calista-pro-white-primer", None, "Interior Primer", sizes=EMUL),
    ],
    "primer_exterior": [
        P("style-perfect-start-primer", "Style Perfect Start Primer", "Peel-proof exterior primer that brightens walls and gives a smooth base.",
          ["Peel proof", "Brightness", "Exterior"], BO + "/exterior-wall-paint/style-perfect-start-primer", None, "Exterior Primer", sizes=EMUL),
        P("calista-perfect-choice-primer", "Calista Perfect Choice Primer", "Premium water-thinnable exterior primer for Calista and One topcoats.",
          ["Premium", "Water thinnable", "Exterior"], BO + "/exterior-wall-paint", None, "Exterior Primer", sizes=EMUL),
    ],
}

# ================================================================ Forever
FOREVER = [
    P("forever-emulsion", "Forever Emulsions", "Interior and exterior emulsions in a wide range of shades, at a pocket-friendly price.",
      ["Interior &amp; exterior", "Washable", "Many shades"], "https://paintsforever.net/", None, "Emulsion", sizes=EMUL),
    P("forever-primer", "Forever Primer", "Interior and exterior wall primers for strong adhesion and a smooth base.",
      ["Interior &amp; exterior", "Adhesion", "Smooth base"], "https://paintsforever.net/", None, "Primer", sizes=EMUL),
    P("forever-putty", "Forever Rustic Putty", "Wall putty that fills uneven surfaces and gives a smooth finish before paint.",
      ["Fills gaps", "Smooth finish", "Walls"], "https://paintsforever.net/", None, "Putty", sizes=POWDER_PUTTY),
]

# ================================================================ ACC page extras
DRFIXIT = [
    P("drfixit-101-lw", "Dr. Fixit 101 Pidiproof LW+", "Integral liquid waterproofing compound. Mix it into cement concrete and plaster for roofs, tanks, basements and walls.",
      ["Mix with cement", "Roof &amp; tanks", "Blue pack"], "https://www.drfixit.co.in/products/dr-fixit-pidiproof-lw/detail", None, "Dr. Fixit Waterproofing",
      sizes=FIXIT, img="images/products/drfixit/drfixit-101-lw.webp"),
    P("drfixit-301-urp", "Dr. Fixit 301 Pidicrete URP", "SBR latex bonding agent for crack repair, joining old and new concrete, and waterproof repairs.",
      ["Crack repair", "Bonding agent", "Orange pack"], "https://www.drfixit.co.in/", None, "Dr. Fixit Waterproofing",
      sizes=FIXIT, img="images/products/drfixit/drfixit-301-urp.webp"),
]
CEMENT_COLOURS = [("White", "#f5f5f2"), ("Mid Cream", "#efe0bb"), ("Apple Green", "#9ccc65"), ("Bone White", "#efe7d4"),
                  ("Dove Gray", "#a7a8aa"), ("Dark Gray", "#5b5d60"), ("Bright Pink", "#ec407a"), ("Sky Blue", "#7ec8e3"),
                  ("Light Green", "#b5e3a1"), ("Dark Pink", "#c2185b")]
CEMENT_COLOUR = P("cement-colour", "Cement Colour (Powder)", "Powder colour to mix with cement for floors, walls and outside plaster. Comes in a 20 kg bag.",
                  ["20 kg bag", "10 colours", "Mix with cement"], "", None, "Cement Colour",
                  opts=[("Colour", [c for c, _ in CEMENT_COLOURS])], fixed={"Size": "20 kg bag"}, img="images/products/misc/cement-colour-bag.svg")

# ================================================================ Tools & more (tools.html)
T = "images/products/tools/"
TOOLS = {
    "rollers": [
        P("asian-roller-800", "Asian Paints TruCare Roller 800", "Economy interior felt roller for a smooth finish, even on uneven walls.",
          ["Interior", "Felt roller", "Asian Paints"], AP + "/products/tools/listing/roller-800-1057hn74122.html", None, "Roller", sizes=ROLLER, img=T + "asian-roller-800.webp"),
        P("asian-roller-800-exterior", "Asian Paints TruCare Roller 800 Exterior", "Felt roller made for exterior walls and rough surfaces.",
          ["Exterior", "Felt roller", "Asian Paints"], AP + "/products/tools/listing.html", None, "Roller", sizes=ROLLER, img=T + "asian-roller-800-exterior.webp"),
        P("normal-roller", "Paint Roller (ColorCraft / Blue Apple)", "Good quality everyday paint roller with a comfortable handle.",
          ["Everyday use", "Interior &amp; exterior", "Value"], "", None, "Roller", opts=[("Brand", ["ColorCraft", "Blue Apple"])], sizes=ROLLER, img=T + "normal-roller.svg"),
    ],
    "brushes": [
        P("asian-brush", "Asian Paints TruCare Brush", "Brush for water-based and solvent paints with good edge cutting. No. 710 is the 4 inch brush.",
          ["Asian Paints", "Interior &amp; exterior", "Sharp edges"], AP + "/products/tools/listing/ap-trucare-brush-710-1057ai54122.html", None, "Paint Brush",
          sizes=["1 inch", "2 inch", "3 inch", "4 inch (No. 710)"], img=T + "asian-brush-710.webp",
          imgs={"1 inch": T + "asian-brush-10.webp", "2 inch": T + "asian-brush-20.webp", "3 inch": T + "asian-brush-30.webp"}),
        P("aman-brush", "Aman Paint Brush", "&ldquo;Painter's best friend&rdquo;: strong bristles and a steel ferrule for smooth, even strokes.",
          ["Aman", "Strong bristles", "Long life"], "", None, "Paint Brush", sizes=BRUSH, img=T + "aman-brush.webp"),
        P("atul-brush", "Atul Paint Brush", "High quality paint brush for walls, doors and grills.",
          ["Atul", "Everyday use", "Value"], "", None, "Paint Brush", sizes=["2 inch", "3 inch", "4 inch"], img=T + "atul-brush.svg"),
    ],
    "scrapers": [
        P("putty-scraper", "Putty Scraper (Wooden Handle)", "Steel putty blade (patti) with a wooden handle for applying and levelling wall putty.",
          ["Steel blade", "Wooden handle", "For putty"], "", None, "Putty Scraper", sizes=["4 inch", "7 inch", "10 inch"], img=T + "putty-scrapers.webp"),
    ],
}
SPRAY = [("red", "Red"), ("black", "Black"), ("white", "White"), ("matt-black", "Matt Black"),
         ("shyne-black", "Shyne Black"), ("green", "Green"), ("silver", "Silver"), ("metallic", "Metallic")]
TOOLS["spray"] = [
    P(f"cube-spray-{k}", f"CUBE Spray Paint: {n}", "Quick-dry aerosol paint for metal, wood, bikes, grills and craft work.",
      ["CUBE", "400 ml", "Quick dry"], "", None, "Spray Paint", fixed={"Colour": n, "Size": "400 ml"}, img=f"images/products/spray/spray-{k}.svg")
    for k, n in SPRAY]
TOOLS["turpentine"] = [
    P("kayson-turpentine", "Kayson Vaspa Turpentine Oil", "Good quality turpentine oil for thinning enamel paints and cleaning brushes.",
      ["For enamel paints", "Kayson", "Good quality"], "", None, "Turpentine Oil", sizes=["500 ml", "750 ml", "1 L", "3 L", "5 L"], img="images/products/misc/kayson-turpentine.webp"),
]
C = "images/products/curtain/"
TOOLS["curtain"] = [
    P("curtain-pipe", "Steel Curtain Pipe", "Strong steel curtain pipe (rod) for windows and doors.",
      ["Steel", "Rust free", "Window &amp; door"], "", None, "Curtain Pipe", sizes=["12 ft", "15 ft"], img=C + "curtain-pipe.svg"),
    P("curtain-bracket", "Steel Curtain Bracket", "Simple steel bracket to fix the curtain pipe on the wall.",
      ["Steel", "Small &amp; big", "Easy to fix"], "", None, "Bracket", sizes=["Small", "Big"], img=C + "bracket-small.svg", imgs={"Big": C + "bracket-big.svg"}),
] + [
    P(f"finial-{k}", f"Curtain Finial: {n}", "Decorative end cap (finial) for the curtain pipe.",
      ["Steel", "Design " + str(k), "Pair"], "", None, "Finial", fixed={"Design": n}, img=f"{C}finial-{k}.webp")
    for k, n in [(1, "Silver Moon"), (2, "Copper Stripe"), (3, "Black Moon"), (4, "Silver Stripe")]
]
STENCILS = [("floral-bloom", "Floral Bloom"), ("damask", "Royal Damask"), ("mandala", "Mandala"), ("tropical-leaves", "Tropical Leaves"),
            ("moroccan-trellis", "Moroccan Quatrefoil"), ("birds-branch", "Birds on Branch"), ("paisley", "Paisley"),
            ("geometric-diamonds", "Geometric Diamonds"), ("bubbles", "Bubble Circles"), ("lotus", "Lotus"),
            ("butterflies", "Butterflies"), ("bamboo", "Bamboo")]
TOOLS["stencils"] = [
    P(f"stencil-{k}", f"Wall Stencil: {n}", "Reusable wall stencil to print a design on your wall with paint.",
      ["2 ft &times; 1.5 ft", "Reusable", "Any colour"], "", None, "Wall Stencil", fixed={"Design": n, "Size": "2 ft x 1.5 ft"},
      img=f"images/products/stencils/{k}.svg", cover=True)
    for k, n in STENCILS]

BRAND_LABEL = {"asian": "Asian Paints", "berger": "Berger Paints", "birla": "Birla Opus", "forever": "Forever Paints",
               "birla-white": "Birla White", "drfixit": "Dr. Fixit", "acc": "ACC", "tools": "", "misc": ""}


def _plain(s):
    return s.replace("&amp;", "&").replace("&ldquo;", "\"").replace("&rdquo;", "\"").replace("&times;", "x")


def card(p, brand):
    img = p["img"] or f"images/products/{brand}/{p['slug']}.webp"
    blabel = BRAND_LABEL.get(brand, "")
    if brand == "birla" and p["img"] and "birla-white" in p["img"]:
        blabel = "Birla White"
    tier = ""
    if p["tier"] == "luxury":
        tier = '<span class="tier tier--luxury">Luxury</span>'
    elif p["tier"] == "economy":
        tier = '<span class="tier tier--economy">Economy</span>'
    chips = "".join(f"<li>{c}</li>" for c in p["chips"])
    tags = f' data-tags="{p["tags"]}"' if p["tags"] else ""
    name_plain = _plain(p["name"])
    full = f"{name_plain} ({blabel})" if blabel else name_plain
    msg = f"Namaste Rana Paints! Please share price and details of {full}."
    cover = " product__img--cover" if p["cover"] else ""

    # ---- buy box: dropdowns + qty + add to cart ----
    selects = []
    all_opts = list(p["opts"]) + ([("Size", p["sizes"])] if p["sizes"] else [])
    for label, values in all_opts:
        options = "".join(
            f'<option value="{escape(v)}"{f" data-img={chr(34)}{p["imgs"][v]}{chr(34)}" if v in p["imgs"] else ""}>{escape(v)}</option>'
            for v in values)
        selects.append(f'<label class="buy__field"><span>{label}</span><select data-opt="{label}">{options}</select></label>')
    fixed = "".join(f'<span class="buy__fixed">{escape(k)}: <b>{escape(v)}</b></span>' for k, v in p["fixed"].items()
                    if not (k == "Colour" and p["slug"].startswith("cube-")) and not k == "Design")
    data = (f' data-pid="{brand}-{p["slug"]}" data-name="{escape(name_plain)}" data-brand="{escape(blabel)}"'
            f' data-img="{img}" data-fixed="{escape(json.dumps(p["fixed"]))}"')
    details = (f'<a class="link-arrow" href="{p["url"]}" target="_blank" rel="noopener">Details {i("ext", "2")}</a>'
               if p["url"] else "")
    return f"""<article class="product"{tags}{data}>
  {tier}
  <div class="product__img{cover}"><img src="{img}" alt="{p['name']}{' by ' + blabel if blabel else ''}" loading="lazy" width="600" height="600"></div>
  <div class="product__body">
    <span class="product__cat">{p['cat']}</span>
    <h3>{p['name']}</h3>
    <p>{p['desc']}</p>
    <ul class="chips">{chips}</ul>
    <div class="buy">
      {''.join(selects)}{fixed}
      <div class="buy__row">
        <div class="qty"><button type="button" data-step="-1" aria-label="Less">&minus;</button><input type="number" min="1" max="999" value="1" inputmode="numeric" aria-label="Quantity"><button type="button" data-step="1" aria-label="More">+</button></div>
        <button class="btn btn--sm btn--cart" type="button" data-add>{i('cart', '2')} Add</button>
      </div>
    </div>
    <div class="product__links">
      <a class="link-wa" href="{wa(msg)}" target="_blank" rel="noopener">{i('wa')} Ask on WhatsApp</a>
      {details}
    </div>
  </div>
</article>"""


def grid(items, brand, gid=""):
    idattr = f' id="{gid}"' if gid else ""
    return f'<div class="products"{idattr}>\n' + "\n".join(card(p, brand) for p in items) + "\n</div>"
