from layout import page, wa
from icons import i
from page_brands import shadecard_tiles

BIRLA_INT = "https://www.birlaopus.com/content/dam/grasimsbirlaopusconsumerwebsite/in/en/products-module/pip/interior-colour-guide/interior-colour-guide.pdf"
BIRLA_EXT = "https://www.birlaopus.com/content/dam/grasimsbirlaopusconsumerwebsite/in/en/products-module/pip/exterior-colour-guide/exterior-colour-book.pdf"


def build():
    tabs = [
        ("asian", "images/brands/asian-paints.svg", "Asian Paints"),
        ("berger", "images/brands/berger-paints.png", "Berger Paints"),
        ("birla", "images/brands/birla-opus.svg", "Birla Opus"),
    ]
    btns = "".join(
        f'<button type="button" role="tab" id="tab-{k}" aria-controls="panel-{k}" data-hash="{k}" class="{"is-active" if n == 0 else ""}"><img src="{logo}" alt="">{name}</button>'
        for n, (k, logo, name) in enumerate(tabs))
    note = (f'<p class="note">{i("info")}<span>Colours on a phone or computer screen look a little different from real paint. '
            'Please confirm the final shade on the printed shade card at our shop before buying.</span></p>')
    stripes = "".join(f'<span style="background:{c}"></span>' for c in ["#d2161e", "#f2b33d", "#6fa8dc", "#7a9e56", "#8e5ea2"])

    body = f"""
<section class="phero">
  <div class="phero__stripes" aria-hidden="true">{stripes}</div>
  <div class="container">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span>Shades</nav>
    <h1>Shade Cards &amp; Colours</h1>
    <p>Find your colour: open the Asian Paints shade cards, or browse 3,800+ Berger and Birla Opus shades by name and code. Tell us the shade code and we mix it on our computerised machine.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="brandtabs" role="tablist" aria-label="Choose brand" data-tabs data-hash>{btns}</div>

    <div class="tabpanel" role="tabpanel" id="panel-asian" aria-labelledby="tab-asian">
      <div class="section-head">
        <span class="eyebrow" style="--accent:#e0312f">Asian Paints</span>
        <h2>Asian Paints shade cards</h2>
        <p>Tap a card to open it. You can also download the PDF to your phone.</p>
      </div>
      <div class="shadecards">
{shadecard_tiles()}
      </div>
      {note}
    </div>

    <div class="tabpanel" role="tabpanel" id="panel-berger" aria-labelledby="tab-berger" hidden>
      <div class="section-head">
        <span class="eyebrow" style="--accent:#0b4ea2">Berger Paints</span>
        <h2>Berger colour catalogue</h2>
        <p>Search by shade name or code, or pick a colour family. Tap a shade to see it on a wall.</p>
      </div>
      <div class="swatch-app page-berger" data-brand="berger"></div>
      {note}
    </div>

    <div class="tabpanel" role="tabpanel" id="panel-birla" aria-labelledby="tab-birla" hidden>
      <div class="section-head">
        <span class="eyebrow" style="--accent:#5b3fa0">Birla Opus</span>
        <h2>Birla Opus colour catalogue</h2>
        <p>Search by shade name or code, or pick a colour family. Want the full printed guide? <a class="link-arrow" style="--accent:#5b3fa0" href="{BIRLA_INT}" target="_blank" rel="noopener">Interior guide (PDF)</a> &middot; <a class="link-arrow" style="--accent:#5b3fa0" href="{BIRLA_EXT}" target="_blank" rel="noopener">Exterior guide (PDF)</a></p>
      </div>
      <div class="swatch-app page-birla" data-brand="birla"></div>
      {note}
    </div>
  </div>
</section>

<section class="section section--soft section--tight">
  <div class="container">
    <div class="cta">
      <div>
        <h2>Found your shade?</h2>
        <p>Send us the shade name or code on WhatsApp. We'll tell you the price for your pack size and keep it ready.</p>
      </div>
      <div class="cta__actions">
        <a class="btn btn--wa" href="{wa('Namaste Rana Paints! I have chosen a shade: ')}" target="_blank" rel="noopener">{i('wa')} Send Shade Code</a>
      </div>
    </div>
  </div>
</section>
"""
    scripts = ('<script src="js/data/berger-shades.js"></script>\n'
               '<script src="js/data/birla-shades.js"></script>\n'
               '<script src="js/shades.js?v=3"></script>\n')
    return page("Shade Cards: Asian Paints, Berger, Birla Opus | Rana Paints",
                "Asian Paints shade cards (Tractor, Ace & Apex, Apcolite) and 3,800+ Berger and Birla Opus shades with names and codes. Rana Paints, Dasuya.",
                body, active="shades.html", scripts=scripts)
