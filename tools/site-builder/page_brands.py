import json
from pathlib import Path
from layout import page, wa, tel
from icons import i
from products import ASIAN, BERGER, BIRLA, FOREVER, grid

ASIAN_CARDS = json.load(open(Path(__file__).with_name("asian_shade_pages.json")))
CARD_META = {
    "tractor-emulsion": ("Tractor Emulsion", "Tractor range of finishes: 2000+ shades, matt and shyne", True),
    "ace-apex": ("Ace &amp; Apex Exterior", "Ace Anti-Fade and Apex Dust Proof exterior shades", False),
    "apcolite": ("Apcolite Emulsions", "Apcolite premium emulsion shade card", False),
}


def shadecard_tiles():
    out = []
    for key, (title, sub, strip) in CARD_META.items():
        pages = [f"images/shades/{p}" for p in ASIAN_CARDS[key]]
        out.append(f"""      <button class="shadecard reveal" type="button" data-viewer="{key}" data-title="Asian Paints {title.replace('&amp;', '&')}" data-pdf="shade-cards/asian-{key}.pdf" data-pages='{json.dumps(pages)}'{' data-strip="1"' if strip else ''}>
        <span class="shadecard__cover"><img src="images/shades/{key}-cover.webp" alt="" loading="lazy"></span>
        <span class="shadecard__body">
          <h3>{title}</h3>
          <p>{sub}</p>
          <span class="shadecard__meta">View shade card <span>{len(pages)} pages</span></span>
        </span>
      </button>""")
    return "\n".join(out)


def band(icon, title, text, btn_label, btn_href, ext=False):
    tgt = ' target="_blank" rel="noopener"' if ext else ""
    return f"""<div class="band reveal">
  <div class="band__icon">{i(icon, '1.6')}</div>
  <div><h3>{title}</h3><p>{text}</p></div>
  <a class="btn" href="{btn_href}"{tgt}>{btn_label}</a>
</div>"""


def crumbs(name, dark=False):
    return f'<nav class="crumbs{" crumbs--dark" if dark else ""}" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="index.html#brands">Brands</a><span>/</span>{name}</nav>'


# =====================================================================
def asian():
    cats = [
        ("#interior", "sofa", "Interior<br>walls"), ("#exterior", "sun", "Exterior<br>walls"),
        ("#waterproofing", "umbrella", "Water-<br>proofing"), ("#putty", "layers", "Wall<br>putty"),
        ("#primers", "bucket", "Primers &amp;<br>undercoats"), ("#enamels", "brush", "Enamel<br>paints"),
    ]
    catgrid = "\n".join(f'        <a href="{h}">{i(ic, "1.3")}{t}</a>' for h, ic, t in cats)
    wp_filters = [("all", "All products"), ("terrace", "Terrace &amp; Tanks"), ("bathrooms", "Bathrooms"),
                  ("cracks", "Cracks &amp; Joints"), ("interior", "Interior"), ("exterior", "Exteriors"), ("tiling", "Tiling")]
    wpf = "".join(f'<button type="button" data-filter="{k}" class="{"is-active" if k == "all" else ""}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>' for k, v in wp_filters)

    body = f"""
<section class="bhero">
  <img src="images/stock/hero-living.webp" alt="" fetchpriority="high">
  <div class="container bhero__inner">
    <div>
      {crumbs('Asian Paints')}
      <img class="bhero__logo" src="images/brands/asian-paints-white.svg" alt="Asian Paints" width="190" height="40">
      <h1>Asian Paints</h1>
      <p>Authorised Asian Paints dealer in Dasuya. Interior and exterior emulsions in <strong>luxury and economy</strong> ranges, SmartCare waterproofing, putty, primers and enamels, with shades mixed on the Asian Paints <strong>ColorWorld</strong> machine.</p>
      <div class="bhero__actions">
        <a class="btn" href="#shades">View Shade Cards</a>
        <a class="btn btn--wa" href="{wa('Namaste Rana Paints! I want to know about Asian Paints products and prices.')}" target="_blank" rel="noopener">{i('wa')} Enquire</a>
      </div>
    </div>
    <aside class="catcard" style="--page-hero-title:#e0312f">
      <h2 class="catcard__title">Transform<br>your space</h2>
      <nav class="catcard__grid" aria-label="Asian Paints categories">
{catgrid}
      </nav>
    </aside>
  </div>
</section>

<nav class="subnav" aria-label="Asian Paints sections">
  <div class="container"><div class="subnav__list">
    <a href="#interior">Interior Walls</a><a href="#exterior">Exterior Walls</a><a href="#waterproofing">Waterproofing</a><a href="#putty">Wall Putty</a><a href="#primers">Primers</a><a href="#enamels">Enamels</a><a href="#shades">Shade Cards</a>
  </div></div>
</nav>

<section class="section" id="interior">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">For Interior Walls</span>
      <h2>Interior wall paints</h2>
      <p>From budget-friendly distemper to premium washable emulsions for your living room, bedroom and kitchen.</p>
    </div>
    <div class="pgroup">
      <div class="pgroup__head"><span class="tier tier--luxury">Luxury</span><h3>Premium finish, long life</h3></div>
      {grid(ASIAN['interior_luxury'], 'asian')}
    </div>
    <div class="pgroup">
      <div class="pgroup__head"><span class="tier tier--economy">Economy</span><h3>Great value for money</h3></div>
      {grid(ASIAN['interior_economy'], 'asian')}
    </div>
  </div>
</section>

<section class="section section--soft" id="exterior">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">For Exterior Walls</span>
      <h2>Exterior wall paints</h2>
      <p>Weather-proof paints that fight rain, sun, dust and algae, so your home looks new for years.</p>
    </div>
    <div class="pgroup">
      <div class="pgroup__head"><span class="tier tier--luxury">Luxury</span><h3>Apex: dust proof, up to 6 years</h3></div>
      {grid(ASIAN['exterior_luxury'], 'asian')}
    </div>
    <div class="pgroup">
      <div class="pgroup__head"><span class="tier tier--economy">Economy</span><h3>Ace &amp; Neo Bharat: strong and affordable</h3></div>
      {grid(ASIAN['exterior_economy'], 'asian')}
    </div>
  </div>
</section>

<section class="section" id="waterproofing">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Waterproofing</span>
      <h2>SmartCare waterproofing</h2>
      <p>Leaking roof, damp walls, bathroom seepage or cracks? Choose the problem area to see the right product.</p>
    </div>
    <div class="filters" data-filters="wp-grid" role="group" aria-label="Filter waterproofing products">{wpf}</div>
    {grid(ASIAN['waterproofing'], 'asian', 'wp-grid')}
  </div>
</section>

<section class="section section--soft" id="putty">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Wall Putty</span>
      <h2>Smooth walls start with putty</h2>
      <p>Fill pores and small dents for a smooth, even wall before primer and paint.</p>
    </div>
    {grid(ASIAN['putty'], 'asian')}
  </div>
</section>

<section class="section" id="primers">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Primers &amp; Undercoats</span>
      <h2>Interior &amp; exterior primers</h2>
      <p>Primer helps paint stick better, cover more and last longer.</p>
    </div>
    <div class="pgroup">
      <div class="pgroup__head"><span class="tier tier--pro">Interior</span><h3>Interior wall primers</h3></div>
      {grid(ASIAN['primer_interior'], 'asian')}
    </div>
    <div class="pgroup">
      <div class="pgroup__head"><span class="tier tier--pro">Exterior</span><h3>Exterior wall primers</h3></div>
      {grid(ASIAN['primer_exterior'], 'asian')}
    </div>
  </div>
</section>

<section class="section section--soft" id="enamels">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Enamel Paints</span>
      <h2>Enamels for doors, windows &amp; grills</h2>
      <p>Glossy and satin enamels for wood and metal surfaces.</p>
    </div>
    {grid(ASIAN['enamel'], 'asian')}
  </div>
</section>

<section class="section" id="shades">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Shade Cards</span>
      <h2>Asian Paints shade cards</h2>
      <p>Open a shade card, pick your colour and tell us the shade code. We mix it on the ColorWorld machine at the shop.</p>
    </div>
    <div class="shadecards">
{shadecard_tiles()}
    </div>
    <div style="margin-top:40px">
      {band('machine', 'Asian Paints ColorWorld at our shop', 'Computerised tinting machine: your chosen shade, mixed exactly in minutes.', 'All Shades', 'shades.html')}
    </div>
  </div>
</section>
"""
    return page("Asian Paints Dealer in Dasuya | Rana Paints",
                "Asian Paints authorised dealer in Passi Kandi, Dasuya: Tractor, Apcolite, Ace, Apex, Neo Bharat, SmartCare waterproofing, putty, primers, enamels and shade cards.",
                body, active="asian-paints.html", body_class="page-asian")


# =====================================================================
def berger():
    ext = [p for p in BERGER if p["tags"] == "exterior"]
    putty = [p for p in BERGER if p["tags"] == "putty"]
    primer = [p for p in BERGER if p["tags"] == "primer"]
    body = f"""
<section class="pbanner pbanner--berger">
  <div class="container pbanner__inner">
    <div>
      {crumbs('Berger Paints')}
      <img class="bhero__logo bhero__logo--chip" src="images/brands/berger-paints.png" alt="Berger Paints" width="92" height="64">
      <h1>Outdoor paints that stand up to Punjab's weather</h1>
      <p>Authorised Berger Paints dealer. Economy exterior emulsions, Bison and Happy Walls putty, and primers, with shades mixed on the Berger ColorWorld machine.</p>
      <div class="bhero__actions">
        <a class="btn btn--white" href="#products">View Products</a>
        <a class="btn btn--wa" href="{wa('Namaste Rana Paints! I want to know about Berger Paints products and prices.')}" target="_blank" rel="noopener">{i('wa')} Enquire</a>
      </div>
    </div>
    <div class="pbanner__packs" aria-hidden="true">
      <img class="p1" src="images/products/berger/walmasta-lite.webp" alt="" style="border-radius:16px">
      <img class="p2" src="images/products/berger/weathercoat-glow.webp" alt="" style="border-radius:16px">
      <img class="p3" src="images/products/berger/walmasta.webp" alt="" style="border-radius:16px">
    </div>
  </div>
</section>

<section class="section" id="products">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">Berger Products</span>
      <h2>Products we stock</h2>
      <p>Choose a category below.</p>
    </div>
    <div class="filters filters--center" data-filters="bg-grid" role="group" aria-label="Filter Berger products">
      <button type="button" data-filter="all" class="is-active" aria-pressed="true">All Products</button><button type="button" data-filter="exterior" aria-pressed="false">Exterior Emulsions</button><button type="button" data-filter="putty" aria-pressed="false">Wall Putty</button><button type="button" data-filter="primer" aria-pressed="false">Primers</button>
    </div>
    {grid(ext + putty + primer, 'berger', 'bg-grid')}
  </div>
</section>

<section class="section section--soft" id="shades">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Berger Shades</span>
      <h2>1500+ Berger shades to choose from</h2>
      <p>Browse the full Berger colour catalogue with shade names and codes, then ask us for your favourite.</p>
    </div>
    <div class="mini-swatches" aria-hidden="true">{''.join(f'<span style="background:{c}"></span>' for c in ['#F5EDEA','#ECDFC8','#E29F88','#7A3640','#835342','#BEA793','#6CA5A0','#788598','#F8DAD1','#F5CCDC','#FADBD8','#F8F6EB'])}</div>
    <div class="hero__actions" style="margin-bottom:36px"><a class="btn" href="shades.html#berger">Explore Berger Shades {i('right', '2.2')}</a></div>
    {band('machine', 'Berger ColorWorld at our shop', 'Pick any Berger shade and we tint it on our computerised machine.', 'Ask for a Shade', wa('Namaste Rana Paints! I want a Berger shade mixed.'), True)}
  </div>
</section>
"""
    return page("Berger Paints Dealer in Dasuya | Rana Paints",
                "Berger Paints authorised dealer in Passi Kandi, Dasuya: Walmasta Lite, Walmasta, WeatherCoat Glow, Bison and Happy Walls putty, BP primers and 1500+ shades.",
                body, active="berger-paints.html", body_class="page-berger")


# =====================================================================
def birla():
    tabs = [
        ("exteriors", "Exteriors", "Exterior Wall Paint",
         "Exterior paints by Birla Opus, made to protect your home from sun, rain and dust. We stock the Style range for great value and Calista Neo Star Shine for a premium sheen finish.",
         grid(BIRLA['exterior'], 'birla')),
        ("putty", "Wall Putty", "Wall Putty",
         "An even, smooth wall is the base of a good paint job. One Pro Smooth acrylic putty fills pores and dents before primer.",
         grid(BIRLA['putty'], 'birla')),
        ("primers", "Primers", "Interior &amp; Exterior Primers",
         "The right primer makes paint stick better, cover more and last longer. Choose interior or exterior below.",
         f"""<div class="pgroup"><div class="pgroup__head"><span class="tier tier--pro">Interior</span><h3>Interior primers</h3></div>{grid(BIRLA['primer_interior'], 'birla')}</div>
<div class="pgroup"><div class="pgroup__head"><span class="tier tier--pro">Exterior</span><h3>Exterior primers</h3></div>{grid(BIRLA['primer_exterior'], 'birla')}</div>"""),
        ("shades", "Shades", "2300+ Birla Opus Shades",
         "Browse the Birla Opus colour catalogue by colour family, with shade names and codes, then ask us to mix it on our Corob machine.",
         f"""<div class="mini-swatches" aria-hidden="true">{''.join(f'<span style="background:{c}"></span>' for c in ['#F0E1CC','#705348','#BF8982','#8D4867','#CC839F','#803B46','#D6C9A3','#5C7BBD','#5967AD','#C5C9C6','#9C9389','#E0CEBD'])}</div>
<div class="hero__actions" style="justify-content:center;margin-bottom:36px">
  <a class="btn" href="shades.html#birla">Explore Birla Opus Shades {i('right', '2.2')}</a>
  <a class="btn btn--outline" href="https://www.birlaopus.com/content/dam/grasimsbirlaopusconsumerwebsite/in/en/products-module/pip/exterior-colour-guide/exterior-colour-book.pdf" target="_blank" rel="noopener">Exterior Colour Guide (PDF)</a>
</div>"""),
    ]
    tabbtns = "".join(f'<button type="button" role="tab" id="tab-{k}" aria-controls="panel-{k}" data-hash="{k}" class="{"is-active" if n == 0 else ""}">{label}</button>'
                      for n, (k, label, *_rest) in enumerate(tabs))
    panels = "\n".join(f"""<div class="tabpanel" role="tabpanel" id="panel-{k}" aria-labelledby="tab-{k}">
  <div class="tabpanel__head"><h2>{title}</h2><p>{desc}</p></div>
  {content}
</div>""" for k, _label, title, desc, content in tabs)

    body = f"""
<section class="pbanner pbanner--birla">
  <div class="container pbanner__inner">
    <div>
      {crumbs('Birla Opus', True)}
      <img class="bhero__logo" src="images/brands/birla-opus.svg" alt="Birla Opus" style="height:56px">
      <h1>Landmark homes with an exquisite range of exterior emulsions.</h1>
      <div class="hero__actions" style="margin-top:22px">
        <a class="btn" href="#range">View Range</a>
        <a class="btn btn--wa" href="{wa('Namaste Rana Paints! I want to know about Birla Opus products and prices.')}" target="_blank" rel="noopener">{i('wa')} Enquire</a>
      </div>
    </div>
    <div class="pbanner__packs" aria-hidden="true">
      <img class="p1" src="images/products/birla/style-power-bright.webp" alt="">
      <img class="p2" src="images/products/birla/calista-neo-star-shine.webp" alt="">
      <img class="p3" src="images/products/birla/style-power-fit.webp" alt="">
    </div>
  </div>
</section>

<section class="section" id="range" style="padding-top:0">
  <div class="container">
    <div class="otabs" role="tablist" aria-label="Birla Opus categories" data-tabs data-hash>{tabbtns}</div>
{panels}
  </div>
</section>

<section class="section section--soft section--tight">
  <div class="container">
    {band('machine', 'Birla Opus Corob machine at our shop', 'Your Birla Opus shade tinted accurately on the Corob machine.', 'Ask for a Shade', wa('Namaste Rana Paints! I want a Birla Opus shade mixed.'), True)}
  </div>
</section>
"""
    return page("Birla Opus Dealer in Dasuya | Rana Paints",
                "Birla Opus paints in Passi Kandi, Dasuya: Style Power Bright, Style Power Fit, Calista Neo Star Shine, One Pro Smooth Putty, primers and 2300+ shades.",
                body, active="birla-opus.html", body_class="page-birla")


# =====================================================================
def forever():
    body = f"""
<section class="pbanner pbanner--forever">
  <div class="container pbanner__inner">
    <div>
      {crumbs('Forever Paints')}
      <img class="bhero__logo bhero__logo--chip" src="images/brands/forever-paints.png" alt="Forever Paints" style="height:60px">
      <h1>Good paint at a pocket-friendly price</h1>
      <p>Forever Paints emulsions, primer and rustic putty: a smart choice when you want a fresh look within budget.</p>
      <div class="bhero__actions">
        <a class="btn btn--white" href="#products">View Products</a>
        <a class="btn btn--wa" href="{wa('Namaste Rana Paints! I want to know about Forever Paints products and prices.')}" target="_blank" rel="noopener">{i('wa')} Enquire</a>
      </div>
    </div>
    <div class="pbanner__packs" aria-hidden="true">
      <img class="p1" src="images/products/forever/forever-primer.webp" alt="">
      <img class="p2" src="images/products/forever/forever-emulsion.webp" alt="">
      <img class="p3" src="images/products/forever/forever-putty.webp" alt="">
    </div>
  </div>
</section>

<section class="section" id="products">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">Forever Paints</span>
      <h2>What we stock</h2>
      <p>Ask us for the shade and pack size you need.</p>
    </div>
    <div style="max-width:960px;margin:0 auto">{grid(FOREVER, 'forever')}</div>
  </div>
</section>
"""
    return page("Forever Paints in Dasuya | Rana Paints",
                "Forever Paints emulsions, primer and rustic putty at Rana Paint & Cement Store, Passi Kandi, Dasuya.",
                body, active="forever-paints.html", body_class="page-forever")


# =====================================================================
def acc():
    items = [
        ("acc-gold-water-shield", "ACC Gold Water Shield Cement",
         "Keep your home looking new with ACC Gold Water Shield, India's first cement with a unique water-resistant formula that protects your home from moisture and the damage it causes.",
         ["Water-repellent formula", "Less water absorption through concrete pores", "Ideal for roofs, bathrooms and damp-prone areas"],
         "https://www.acchelp.in/all-products/cement/acc-gold-water-shield"),
        ("acc-concrete-plus", "ACC Concrete Plus Cement",
         "Safeguard the strength of your home with ACC Concrete Plus Xtra Strong. Made from high-quality clinker with special performance additives for extra strength.",
         ["Xtra strong", "Great for roof slabs and structural work", "Superior bonding"],
         "https://www.acchelp.in/all-products/cement/acc-concrete-plus-cement"),
        ("acc-suraksha-power", "ACC Suraksha Power Cement",
         "A premium cement with unique strength multipliers that keep increasing the strength of your home over time.",
         ["Strength multipliers", "Dense, workable concrete", "Protects steel from corrosion"],
         "https://www.acchelp.in/all-products/cement/acc-suraksha-power-cement"),
    ]
    panels = []
    for n, (slug, name, desc, pts, url) in enumerate(items):
        msg = f"Namaste Rana Paints! Please share the rate of {name} with home delivery."
        panels.append(f"""<div class="feature-panel{' feature-panel--rev' if n % 2 else ''} reveal">
  <div>
    <div class="feature-panel__kicker">Featured Product</div>
    <h2>{name}</h2>
    <p>{desc}</p>
    <ul>{''.join(f'<li>{p}</li>' for p in pts)}</ul>
    <div class="feature-panel__actions">
      <a class="btn btn--white" href="{wa(msg)}" target="_blank" rel="noopener">{i('wa')} Ask Rate</a>
      <a class="btn btn--ghost-white" href="{url}" target="_blank" rel="noopener">View Details</a>
    </div>
  </div>
  <div class="feature-panel__media"><img src="images/products/acc/{slug}.webp" alt="{name} bag" loading="lazy"></div>
</div>""")
    body = f"""
<section class="acc-hero">
  <div class="container pbanner__inner" style="position:relative;z-index:2">
    <div>
      {crumbs('ACC Cement')}
      <img class="acc-logo" src="images/brands/acc.svg" alt="ACC" width="160" height="56">
      <h1>Strong homes start with ACC cement</h1>
      <p>Authorised ACC cement dealer in Passi Kandi, Dasuya. Three trusted ACC cements, steel for your construction, and <strong>home delivery of cement</strong> to your site.</p>
      <div class="bhero__actions">
        <a class="btn btn--white" href="#products">Our Cement Range</a>
        <a class="btn btn--wa" href="{wa('Namaste Rana Paints! I need ACC cement rates with home delivery.')}" target="_blank" rel="noopener">{i('wa')} Ask Rates</a>
      </div>
    </div>
    <div class="acc-hero__bags" aria-hidden="true">
      <img src="images/products/acc/acc-concrete-plus.webp" alt="">
      <img src="images/products/acc/acc-gold-water-shield.webp" alt="">
      <img src="images/products/acc/acc-suraksha-power.webp" alt="">
    </div>
  </div>
</section>

<section class="section" id="products">
  <div class="container">
    <div class="delivery reveal" style="margin-bottom:56px">
      <div class="delivery__icon">{i('truck', '1.5')}</div>
      <div><h3>Cement home delivery</h3><p>Order ACC cement from Rana Paints and we deliver it to your home or construction site. Call or WhatsApp us with the number of bags.</p></div>
      <a class="btn" href="{tel('94171 23935')}">{i('phone')} Order Now</a>
    </div>
{chr(10).join(panels)}
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="split reveal">
      <div class="split__media"><img src="images/stock/steel.webp" alt="Steel reinforcement bars at a construction site" loading="lazy"></div>
      <div class="split__body">
        <span class="eyebrow">Steel Supply</span>
        <h2>Steel for your construction</h2>
        <p>Building a new house? Along with cement, we also arrange steel for your construction. Tell us your requirement and get a combined rate for cement and steel.</p>
        <div class="hero__actions" style="margin-top:8px">
          <a class="btn btn--wa" href="{wa('Namaste Rana Paints! I need cement and steel for construction. Please share rates.')}" target="_blank" rel="noopener">{i('wa')} Get Combined Rate</a>
          <a class="btn btn--outline" href="{tel('94171 23935')}">{i('phone')} Call Us</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""
    return page("ACC Cement Dealer in Dasuya | Rana Paints",
                "ACC Gold Water Shield, ACC Concrete Plus and ACC Suraksha Power cement in Passi Kandi, Dasuya, with home delivery. Steel supply for construction.",
                body, active="acc-cement.html", body_class="page-acc")
