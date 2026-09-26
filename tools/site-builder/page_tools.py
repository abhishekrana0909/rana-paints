from layout import page, wa
from icons import i
from products import TOOLS, grid

SECTIONS = [
    ("rollers", "Paint Rollers", "Rollers", "Asian Paints TruCare rollers and everyday rollers in 2, 4 and 9 inch sizes.", "roller"),
    ("brushes", "Paint Brushes", "Brushes", "Asian Paints, Aman and Atul paint brushes from 1 to 4 inch.", "brush"),
    ("scrapers", "Putty Scrapers", "Scrapers", "Steel putty patti with a wooden handle in 4, 7 and 10 inch.", "layers"),
    ("spray", "Spray Paints", "Spray Paints", "CUBE aerosol spray paint, 400 ml, in 8 colours for bikes, grills, doors and craft work.", "drop"),
    ("turpentine", "Turpentine Oil", "Turpentine", "Kayson Vaspa turpentine oil for thinning enamel paints and cleaning brushes.", "bucket"),
    ("curtain", "Curtain Fittings", "Curtain", "Steel curtain pipes (12 ft and 15 ft), brackets and finials.", "door"),
    ("stencils", "Wall Stencils", "Stencils", "Reusable wall stencils (2 ft &times; 1.5 ft) to print designs on your wall with any paint colour.", "palette"),
]


def build():
    subnav = "".join(f'<a href="#{k}">{short}</a>' for k, _t, short, _d, _ic in SECTIONS)
    tiles = "".join(f'<a href="#{k}">{i(ic, "1.4")}{short}</a>' for k, _t, short, _d, ic in SECTIONS)
    sections = []
    for n, (k, title, _short, desc, _ic) in enumerate(SECTIONS):
        soft = " section--soft" if n % 2 else ""
        sections.append(f"""<section class="section{soft}" id="{k}">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{_short}</span>
      <h2>{title}</h2>
      <p>{desc}</p>
    </div>
    {grid(TOOLS[k], 'tools')}
  </div>
</section>""")

    body = f"""
<section class="phero">
  <div class="container">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span>Tools &amp; More</nav>
    <h1>Tools, Spray Paints &amp; More</h1>
    <p>Everything else you need for the job: rollers, brushes, putty scrapers, spray paints, turpentine oil, curtain fittings and wall stencils. Add what you need to the cart and send the list on WhatsApp.</p>
    <nav class="tool-tiles" aria-label="Jump to a category">{tiles}</nav>
  </div>
</section>

<nav class="subnav" aria-label="Tools sections">
  <div class="container"><div class="subnav__list">{subnav}</div></div>
</nav>

{chr(10).join(sections)}

<section class="section section--tight">
  <div class="container">
    <div class="cta">
      <div>
        <h2>Can't find something?</h2>
        <p>We keep many more hardware and painting items at the shop. Send us a message and we'll tell you.</p>
      </div>
      <div class="cta__actions">
        <a class="btn btn--wa" href="{wa('Namaste Rana Paints! Do you have this item: ')}" target="_blank" rel="noopener">{i('wa')} Ask on WhatsApp</a>
      </div>
    </div>
  </div>
</section>
"""
    return page("Tools, Spray Paints, Curtain Fittings & Stencils | Rana Paints",
                "Paint rollers, brushes, putty scrapers, CUBE spray paints, Kayson turpentine oil, curtain pipes, brackets, finials and wall stencils at Rana Paints, Dasuya.",
                body, active="tools.html")
