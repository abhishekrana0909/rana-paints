from layout import page, wa, tel, MAPS, INSTA, EMAIL, BRANDS
from icons import i

JSONLD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HardwareStore",
  "name": "Rana Paint & Cement Store",
  "alternateName": "Rana Paints",
  "description": "Authorised dealer of Asian Paints, Birla Opus, Berger Paints, Forever Paints and ACC Cement in Passi Kandi, Dasuya, Punjab. Paints, putty, waterproofing, cement and steel, with our own team of painters.",
  "foundingDate": "2000",
  "telephone": "+91-9417123935",
  "email": "dalerrana123@gmail.com",
  "address": {"@type": "PostalAddress", "streetAddress": "Passi Kandi", "addressLocality": "Dasuya", "addressRegion": "Punjab", "addressCountry": "IN"},
  "geo": {"@type": "GeoCoordinates", "latitude": 31.829173, "longitude": 75.7406484},
  "founder": "Daler Singh Rana",
  "sameAs": ["https://www.instagram.com/dwon13/"]
}
</script>
"""


def build():
    slides = [
        ("images/stock/hero-living.webp", "Calm living room with soft beige walls"),
        ("images/stock/hero-bedroom.webp", "Warm wooden bedroom with sage green walls"),
        ("images/stock/hero-terracotta.webp", "Calm terracotta corridor with arches and plants"),
    ]
    slide_html = "\n".join(
        f'      <div class="hero__slide{" is-active" if k == 0 else ""}"><img src="{src}" alt="{alt}"'
        f'{" fetchpriority=\"high\"" if k == 0 else " loading=\"lazy\""}></div>'
        for k, (src, alt) in enumerate(slides))
    dots = "".join(f'<button type="button" data-slide="{k}" aria-label="Slide {k + 1}"></button>' for k in range(len(slides)))

    # (page, logo, naam, peeche wali photo, aage wali photo, brand ka rang, halka background, description)
    BC = "images/brandcards/"
    brand_cards = [
        ("asian-paints.html", "images/brands/asian-paints.svg", "Asian Paints", BC + "asian-a.webp", BC + "asian-b.webp",
         "#e0312f", "#f8e4d9", "Interior &amp; exterior emulsions, waterproofing, putty, primers and enamels."),
        ("birla-opus.html", "images/brands/birla-opus.svg", "Birla Opus", BC + "birla-a.webp", BC + "birla-b.webp",
         "#5b3fa0", "#efe8e1", "Style and Calista paints, Alldry waterproofing, putty and primers."),
        ("berger-paints.html", "images/brands/berger-paints.png", "Berger Paints", BC + "berger-a.webp", BC + "berger-b.webp",
         "#0b4ea2", "#ebe6de", "WeatherCoat Glow, Walmasta, wall putty and primers."),
        ("forever-paints.html", "images/brands/forever-paints.png", "Forever Paints", BC + "forever-a.webp", BC + "forever-b.webp",
         "#c8102e", "#f7e6de", "Budget-friendly emulsions, primer and rustic putty."),
        ("acc-cement.html", "images/brands/acc.svg", "ACC Cement", BC + "acc-a.webp", BC + "acc-b.webp",
         "#d71920", "#f7e9d0", "Gold Water Shield, Concrete Plus and Suraksha Power, with home delivery."),
    ]

    def brand_card(h, logo_html, desc, imgs_html, brand, bg, label):
        return f"""      <a class="brand-card reveal" href="{h}" style="--brand:{brand};--c:{bg}" aria-label="{label}">
        <div class="brand-card__in">
          <div class="brand-card__stage">
            <div class="brand-card__bg"></div>
            <span class="brand-card__ground"></span>
            <div class="brand-card__img">{imgs_html}</div>
          </div>
          <div class="brand-card__body">
            {logo_html}
            <p>{desc}</p>
            <span class="link-arrow">Explore {label} {i('right', '2')}</span>
          </div>
        </div>
      </a>"""

    bc = chr(10).join(
        brand_card(h, f'<img class="brand-card__logo" src="{logo}" alt="{name}" loading="lazy">', desc,
                   f'<img class="p-back" src="{ia}" alt="" loading="lazy"><img class="p-front" src="{ib}" alt="{name} products" loading="lazy">',
                   brand, bg, name)
        for h, logo, name, ia, ib, brand, bg, desc in brand_cards)
    tools_imgs = ('<img class="p-back" src="images/products/spray/spray-red.svg" alt="" loading="lazy">'
                  '<img class="p-mid" src="images/products/tools/atul-brush.svg" alt="" loading="lazy">'
                  '<img class="p-front" src="images/products/tools/normal-roller.svg" alt="Rollers, brushes and spray paints" loading="lazy">')
    bc += chr(10) + brand_card("tools.html", '<span class="brand-card__word">Tools &amp; More</span>',
                              "Rollers, brushes, putty scrapers, CUBE spray paints, turpentine, curtain fittings and wall stencils.",
                              tools_imgs, "#c8232b", "#f3e6d8", "Tools &amp; More")

    strip = "\n".join(f'        <a href="{h}" aria-label="{n}"><img src="{img}" alt="{n}" loading="lazy"></a>' for h, img, n, _ in BRANDS)

    services = [
        ("roller", "Interior &amp; Exterior Painting", "Our own team of painters with 15+ years of experience paints your home neatly and on time.",
         ["Own team of painters, 15+ years of experience", "Interior, exterior, enamel and texture work", "Neat finish, done on the promised date"],
         [("Book a site visit", "#site-visit", False), ("Ask on WhatsApp", wa("Namaste Rana Paints! I want to get my house painted."), True)]),
        ("estimate", "Site Visit &amp; Estimate", "Our contractor visits your site, checks the walls and gives you a clear estimate for paint and labour.",
         ["Contractor Manjit Rana visits your site", "Walls checked and measured properly", "Clear estimate for material and labour"],
         [("Call 99884 12088", tel("99884 12088"), False), ("Book online", "#site-visit", False)]),
        ("umbrella", "Waterproofing Solutions", "Terrace, bathroom, water tank and damp wall solutions with Asian Paints SmartCare and more.",
         ["Terrace, bathroom, tank and damp walls", "Asian Paints SmartCare and Birla Opus Alldry", "Dr. Fixit 101 and 301 with cement"],
         [("Asian waterproofing", "asian-paints.html#waterproofing", False), ("Dr. Fixit", "acc-cement.html#waterproofing", False)]),
        ("palette", "Computerised Colour Mixing", "Any shade from the shade card, mixed exactly on ColorWorld and Corob tinting machines.",
         ["Asian Paints ColorWorld and Berger ColorWorld", "Birla Opus Corob machine", "5000+ shades, exact colour every time"],
         [("Browse shades", "shades.html", False), ("Our machines", "#machines", False)]),
        ("bricks", "Cement &amp; Steel Supply", "ACC cement and steel for building your new home, with home delivery of cement.",
         ["ACC Gold Water Shield, Concrete Plus, Suraksha Power", "Steel for your construction", "Cement delivered to your site"],
         [("See ACC cement", "acc-cement.html", False), ("Ask rates", wa("Namaste Rana Paints! I need cement and steel rates."), True)]),
        ("layers", "Putty, Primer &amp; Enamel", "Complete range of wall putty, primers, enamels and painting tools under one roof.",
         ["Wall putty from Asian, Birla White and Berger", "Interior and exterior primers", "Enamels, rollers, brushes and spray paints"],
         [("Wall putty", "asian-paints.html#putty", False), ("Tools &amp; more", "tools.html", False)]),
    ]
    X_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'

    def book(n, ic, t, d, pts, acts):
        lis = "".join(f"<li>{x}</li>" for x in pts)
        btns = "".join(
            f'<a class="btn btn--sm{" btn--wa" if wa_btn else " btn--outline"}" href="{href}"{" target=\"_blank\" rel=\"noopener\"" if wa_btn else ""}>{lab}</a>'
            for lab, href, wa_btn in acts)
        return f"""      <div class="service book">
        <div class="book__page">
          <div class="book__inner">
            <div class="book__top"><span class="book__no">0{n}</span><h3>{t}</h3><button class="book__close" type="button" aria-label="Close {t}">{X_ICON}</button></div>
            <ul class="book__list">{lis}</ul>
            <div class="book__actions">{btns}</div>
          </div>
        </div>
        <div class="book__cover">
          <div class="book__front" role="button" tabindex="0" aria-expanded="false" aria-label="Open: {t}">
            <div class="service__icon">{i(ic, '1.6')}</div>
            <h3>{t}</h3>
            <p>{d}</p>
            <span class="book__hint">Open <span>{i('right', '2.2')}</span></span>
          </div>
          <div class="book__back" aria-hidden="true"><span>RANA</span><span>PAINTS</span></div>
        </div>
      </div>"""
    sv = chr(10).join(book(k + 1, *row) for k, row in enumerate(services))

    machines = [
        ("images/brands/asian-paints.svg", "Asian Paints ColorWorld", "Computerised tinting for Asian Paints emulsions and enamels. Pick a shade from the fan deck and we mix it right at the shop.",
         ["#e2553f", "#f2b33d", "#6fa8dc", "#7a9e56", "#8e5ea2", "#f4e1c6"]),
        ("images/brands/birla-opus.svg", "Birla Opus Corob", "Corob machine for Birla Opus shades: consistent colour from the first bucket to the last.",
         ["#5c7bbd", "#e05a4f", "#f0c24b", "#6aa27a", "#b08bc5", "#efe5d2"]),
        ("images/brands/berger-paints.png", "Berger ColorWorld", "Berger tinting machine for WeatherCoat, Walmasta and more. Exact shade, every time.",
         ["#7a3640", "#6ca5a0", "#bea793", "#e29f88", "#788598", "#f5edea"]),
    ]
    mc = "\n".join(f"""      <div class="machine reveal">
        <img class="machine__logo" src="{logo}" alt="" loading="lazy">
        <h3>{t}</h3>
        <p>{d}</p>
        <div class="machine__dots">{''.join(f'<span style="background:{c}"></span>' for c in cols)}</div>
      </div>""" for logo, t, d, cols in machines)

    team = [
        ("daler-singh-rana", "Daler Singh Rana", "Owner", "Running Rana Paints since 2000. Talk to him for paints, cement and the best rates.",
         [("phone", "94171 23935", tel("94171 23935")), ("wa", "WhatsApp 94171 23935", wa("Namaste Daler Singh ji!")), ("phone", "98764 12125", tel("98764 12125")), ("mail", EMAIL, "mailto:" + EMAIL)]),
        ("abhishek-rana", "Abhishek Rana", "Owner", "The &ldquo;Son&rdquo; in Daler Singh Rana &amp; Son. Helps you choose the right product and shade.",
         [("phone", "98769 63879", tel("98769 63879")), ("instagram", "@dwon13", INSTA)]),
        ("manjit-rana", "Manjit Rana", "Contractor", "Handles site visits, estimates and our team of painters with 15+ years of experience.",
         [("phone", "99884 12088", tel("99884 12088")), ("phone", "94178 88704", tel("94178 88704"))]),
    ]
    tm = "\n".join(f"""      <article class="member reveal">
        <div class="member__photo"><img src="images/team/{slug}.webp" alt="{name}, {role} at Rana Paints" loading="lazy" width="640" height="800"><span class="member__role">{role}</span></div>
        <div class="member__body">
          <h3>{name}</h3>
          <p>{bio}</p>
          <div class="member__contacts">
{chr(10).join(f'            <a href="{href}"{" target=\"_blank\" rel=\"noopener\"" if href.startswith("http") else ""}>{i(ic)} {label}</a>' for ic, label, href in contacts)}
          </div>
        </div>
      </article>""" for slug, name, role, bio, contacts in team)

    body = f"""
<!-- ============ HERO ============ -->
<section class="hero" aria-label="Welcome">
  <div class="hero__slides">
{slide_html}
  </div>
  <div class="container hero__inner">
    <div class="hero__text">
      <div class="hero__trust" data-rv="up">
        <span class="hero__faces"><img src="images/team/daler-singh-rana.webp" alt=""><img src="images/team/manjit-rana.webp" alt=""><img src="images/team/abhishek-rana.webp" alt=""></span>
        <span><strong>Since 2000</strong><small>Trusted by families across Dasuya</small></span>
      </div>
      <h1 data-rv="up">Sukoon Ke Rang,<br><span>Mazboot Neev</span></h1>
      <p class="hero__lead" data-rv="up">Paints, putty, waterproofing and cement for every home. Asian Paints, Birla Opus, Berger, Forever and ACC, all under one roof, with our own team of painters.</p>
      <div class="hero__actions" data-rv="up">
        <a class="btn btn--arrow" href="#brands">Explore Brands <span class="btn__arrow">{i('right', '2.2')}</span></a>
        <a class="btn btn--outline" href="shades.html">Explore Shades</a>
      </div>
      <ul class="hero__points" data-rv="up">
        <li><strong data-count="5000" data-suffix="+">5000+</strong><span>Shades</span></li>
        <li><strong data-count="25" data-suffix="+">25+</strong><span>Years of trust</span></li>
        <li><strong data-count="15" data-suffix="+">15+</strong><span>Years painter experience</span></li>
      </ul>
    </div>
    <div class="hero__visual" data-rv="right">
      <div class="hero__float" aria-hidden="true">
        <span class="hero__float-dots"><i style="background:#c8232b"></i><i style="background:#e8a15b"></i><i style="background:#8aa486"></i><i style="background:#d9c3a5"></i></span>
        <span><strong>Exact shade</strong><small>Computerised mixing</small></span>
      </div>
      <div class="hero__dots">
        <button class="hero__arrow hero__arrow--prev" type="button" aria-label="Previous slide">{i('left', '2.2')}</button>
        {dots}
        <button class="hero__arrow hero__arrow--next" type="button" aria-label="Next slide">{i('right', '2.2')}</button>
      </div>
    </div>
  </div>
</section>

<!-- ============ DEALER MARQUEE ============ -->
<section class="marquee" aria-label="Authorised dealer of">
  <p class="marquee__label">Authorised dealer of</p>
  <div class="marquee__track">
    <div class="marquee__row">
{strip}
    </div>
    <div class="marquee__row" aria-hidden="true">
{strip}
    </div>
  </div>
</section>

<!-- ============ ABOUT ============ -->
<section class="section" id="about">
  <div class="container">
    <div class="about">
      <div class="about__media reveal">
        <img src="images/stock/terracotta-wall.webp" alt="A warm terracotta painted wall with a green plant" loading="lazy">
        <img class="about__small" src="images/stock/swatches-warm.webp" alt="Warm earthy paint shade cards" loading="lazy">
        <div class="about__since"><span>Serving since</span><strong>2000</strong></div>
      </div>
      <div class="reveal">
        <span class="eyebrow">About Rana Paints</span>
        <h2>Dasuya's trusted paint &amp; cement store for 25+ years</h2>
        <p>Rana Paint &amp; Cement Store has been serving homes in Passi Kandi, Dasuya and nearby villages since 2000. Run by <strong>Daler Singh Rana &amp; Son</strong>, we are authorised dealers of India's top paint brands and ACC cement, so you always get genuine products at the right price.</p>
        <ul class="checklist">
          <li>{i('check', '3')}<span><strong>Our own team of painters</strong> with 15+ years of experience</span></li>
          <li>{i('check', '3')}<span><strong>Site visit and estimate</strong> for your paint work by our contractor</span></li>
          <li>{i('check', '3')}<span><strong>Computerised colour mixing</strong>: Asian ColorWorld, Birla Opus Corob, Berger ColorWorld</span></li>
          <li>{i('check', '3')}<span><strong>Cement &amp; steel supply</strong> for building your home, with home delivery of cement</span></li>
        </ul>
        <div class="hero__actions">
          <a class="btn btn--arrow" href="#team">Meet Our Team <span class="btn__arrow">{i('right', '2.2')}</span></a>
          <a class="btn btn--outline" href="{tel('94171 23935')}">{i('phone')} Call Us</a>
        </div>
      </div>
    </div>
    <div class="stats">
      <div class="stat reveal"><strong data-count="5">5</strong><span>Authorised brands</span></div>
      <div class="stat reveal"><strong data-count="3">3</strong><span>Colour mixing machines</span></div>
      <div class="stat reveal"><strong data-count="100" data-suffix="+">100+</strong><span>Products to order online</span></div>
      <div class="stat reveal"><strong data-count="12">12</strong><span>Wall stencil designs</span></div>
    </div>
  </div>
</section>

<!-- ============ BRANDS ============ -->
<section class="section section--soft" id="brands">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">Our Brands</span>
      <h2>Everything your home needs, from brands you trust</h2>
      <p>Pick a brand to see its products: interior and exterior paints, waterproofing, putty, primers and cement.</p>
    </div>
    <div class="brands-grid">
{bc}
    </div>
  </div>
</section>

<!-- ============ SERVICES ============ -->
<section class="section" id="services">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">What We Do</span>
      <h2>More than a paint shop</h2>
      <p>From choosing the shade to painting the last wall, and from cement for the foundation to waterproofing the roof: we handle it all.</p>
    </div>
    <div class="services">
{sv}
    </div>
  </div>
</section>

<!-- ============ HOW WE WORK ============ -->
<section class="section" id="how">
  <div class="container how">
    <div class="how__media" data-rv="left">
      <img src="images/stock/minimal-arch.webp" alt="Calm room with a soft beige arch" loading="lazy">
      <div class="how__note"><strong>Free advice</strong><span>Not sure which paint? Just ask us.</span></div>
    </div>
    <div>
      <div class="section-head">
        <span class="eyebrow">How we work</span>
        <h2>From the first shade to the last coat</h2>
      </div>
      <ol class="steps">
        <li><span class="steps__n">01</span><div><h3>Pick your shade &amp; product</h3><p>Browse shade cards and products here or at the shop. We help you choose the right paint for the room and budget.</p></div><a class="steps__go" href="shades.html" aria-label="See shades">{i('right', '2.2')}</a></li>
        <li><span class="steps__n">02</span><div><h3>Site visit &amp; estimate</h3><p>Our contractor checks your walls and tells you how much material and labour the job needs.</p></div><a class="steps__go" href="#site-visit" aria-label="Book a site visit">{i('right', '2.2')}</a></li>
        <li><span class="steps__n">03</span><div><h3>Exact colour, ready to go</h3><p>Your shade is mixed on our computerised machine. Cement is delivered to your site.</p></div><a class="steps__go" href="#machines" aria-label="Colour machines">{i('right', '2.2')}</a></li>
        <li><span class="steps__n">04</span><div><h3>Our painters do the rest</h3><p>A team with 15+ years of experience paints your home neatly and on time.</p></div><a class="steps__go" href="#team" aria-label="Meet the team">{i('right', '2.2')}</a></li>
      </ol>
    </div>
  </div>
</section>

<!-- ============ COLOUR MACHINES ============ -->
<section class="section section--soft" id="machines">
    <div class="machines__fx" aria-hidden="true"><i style="--x:6%;--s:14px;--c:#c8232b;--d:0s;--t:7.5s"></i><i style="--x:13%;--s:20px;--c:#e0a14f;--d:2.3s;--t:9.5s"></i><i style="--x:21%;--s:12px;--c:#8aa486;--d:4.1s;--t:8.2s"></i><i style="--x:29%;--s:24px;--c:#c9694a;--d:1.2s;--t:10.5s"></i><i style="--x:38%;--s:16px;--c:#d9c3a5;--d:5.6s;--t:7.8s"></i><i style="--x:46%;--s:18px;--c:#9b6b8e;--d:3.3s;--t:9.0s"></i><i style="--x:54%;--s:13px;--c:#6f93a8;--d:6.8s;--t:8.8s"></i><i style="--x:62%;--s:22px;--c:#c8232b;--d:0.7s;--t:10.0s"></i><i style="--x:70%;--s:15px;--c:#e0a14f;--d:4.9s;--t:7.2s"></i><i style="--x:78%;--s:19px;--c:#8aa486;--d:2.9s;--t:9.8s"></i><i style="--x:86%;--s:12px;--c:#c9694a;--d:6.1s;--t:8.4s"></i><i style="--x:93%;--s:21px;--c:#d9c3a5;--d:1.8s;--t:9.2s"></i></div>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Colour Mixing</span>
      <h2>Your exact shade, mixed in minutes</h2>
      <p>We have computerised colour mixing machines for all three paint companies, so the shade you pick on the card is the shade you get on your wall.</p>
    </div>
    <div class="machines">
{mc}
    </div>
  </div>
</section>

<!-- ============ CEMENT & STEEL ============ -->
<section class="section section--tight">
  <div class="container">
    <div class="split split--red reveal">
      <div class="split__media"><img src="images/stock/construction-sunset.webp" alt="House being built at sunset" loading="lazy"></div>
      <div class="split__body">
        <span class="eyebrow">Cement &amp; Steel</span>
        <h2>Building a new home? We supply cement &amp; steel too</h2>
        <p>Get ACC Gold Water Shield, ACC Concrete Plus and ACC Suraksha Power cement, plus steel for your construction, from the same trusted shop. <strong>We deliver cement to your site.</strong></p>
        <div class="hero__actions" style="margin-top:12px">
          <a class="btn btn--white" href="acc-cement.html">View ACC Cement</a>
          <a class="btn btn--ghost-white" href="{wa('Namaste Rana Paints! I need cement and steel rates with home delivery.')}" target="_blank" rel="noopener">{i('wa')} Ask Rates</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ TEAM ============ -->
<section class="section" id="team">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">Our Team</span>
      <h2>The people behind Rana Paints</h2>
      <p>Daler Singh Rana &amp; Son, with contractor Manjit Rana and a team of painters with 15+ years of experience.</p>
    </div>
    <div class="team">
{tm}
    </div>
  </div>
</section>

<!-- ============ SITE VISIT / QUOTE ============ -->
<section class="section quote" id="site-visit">
  <div class="container quote__inner">
    <div>
      <span class="eyebrow">Site Visit &amp; Estimate</span>
      <h2>Tell us about your work, we'll come and check</h2>
      <p class="quote__lead">Painting a room, the whole house, or fixing a leaking roof? Our contractor will visit your site, check the walls and give you a clear estimate for material and labour.</p>
      <div class="quote__contact">
        <img src="images/team/manjit-rana.webp" alt="Manjit Rana">
        <div>
          <strong>Manjit Rana</strong>
          <span style="display:block;margin-bottom:6px;color:#ffe3e4">Contractor, site visits</span>
          <a href="{tel('99884 12088')}">{i('phone')} 99884 12088</a>
          <a href="{tel('94178 88704')}">{i('phone')} 94178 88704</a>
        </div>
      </div>
    </div>
    <form class="form" data-wa-form>
      <h3>Book a site visit</h3>
      <label>Your name<input name="name" required autocomplete="name" placeholder="e.g. Gurpreet Singh"></label>
      <label>Phone number<input name="phone" type="tel" required autocomplete="tel" inputmode="tel" placeholder="98xxx xxxxx"></label>
      <label class="full">Village / City<input name="place" placeholder="e.g. Dasuya"></label>
      <label class="full">Type of work
        <select name="work">
          <option>Interior painting</option>
          <option>Exterior painting</option>
          <option>Full house painting</option>
          <option>Waterproofing (roof / bathroom / walls)</option>
          <option>Cement &amp; steel for construction</option>
          <option>Something else</option>
        </select>
      </label>
      <label class="full">Details (optional)<textarea name="message" placeholder="Number of rooms, approx. area, preferred date..."></textarea></label>
      <button class="btn btn--wa" type="submit">{i('wa')} Send on WhatsApp</button>
      <p class="form__note">This opens WhatsApp with your details filled in. Nothing is stored on this website.</p>
    </form>
  </div>
</section>

<!-- ============ FAQ ============ -->
<section class="section section--soft" id="faq">
  <div class="container faq">
    <div class="section-head">
      <span class="eyebrow">FAQ</span>
      <h2>Questions people ask us</h2>
      <p>Still have a question? Send us a message on WhatsApp, we usually reply the same day.</p>
      <a class="btn btn--arrow" href="{wa('Namaste Rana Paints! I have a question.')}" target="_blank" rel="noopener">Ask on WhatsApp <span class="btn__arrow">{i('right', '2.2')}</span></a>
    </div>
    <div class="faq__list">
      <details class="faq__item" open><summary>How do I order from the website?<span class="faq__icon" aria-hidden="true"></span></summary><div class="faq__a"><p>Choose the size and quantity on any product and press Add. Open the cart at the top, write your name and send the list on WhatsApp. We reply with the price and keep your order ready.</p></div></details>
      <details class="faq__item"><summary>Do you deliver cement to my site?<span class="faq__icon" aria-hidden="true"></span></summary><div class="faq__a"><p>Yes. We deliver ACC cement to your home or construction site. Tell us the number of bags and the location.</p></div></details>
      <details class="faq__item"><summary>Can you make any shade from the shade card?<span class="faq__icon" aria-hidden="true"></span></summary><div class="faq__a"><p>Yes. We have computerised colour mixing machines for Asian Paints (ColorWorld), Birla Opus (Corob) and Berger, so your shade comes out exactly right.</p></div></details>
      <details class="faq__item"><summary>Do you also paint the house?<span class="faq__icon" aria-hidden="true"></span></summary><div class="faq__a"><p>Yes. We have our own team of painters with 15+ years of experience. Our contractor Manjit Rana handles the work.</p></div></details>
      <details class="faq__item"><summary>Will someone come to check my walls first?<span class="faq__icon" aria-hidden="true"></span></summary><div class="faq__a"><p>Yes. Our contractor visits the site, checks the walls and gives you an estimate for paint and labour. Call 99884 12088 or 94178 88704.</p></div></details>
      <details class="faq__item"><summary>Which brands do you sell?<span class="faq__icon" aria-hidden="true"></span></summary><div class="faq__a"><p>We are authorised dealers of Asian Paints, Birla Opus, Berger Paints, Forever Paints and ACC Cement. We also keep Dr. Fixit, Birla White putty, tools, spray paints and curtain fittings.</p></div></details>
    </div>
  </div>
</section>

<!-- ============ CONTACT ============ -->
<section class="section" id="contact">
  <div class="container">
    <div class="cta reveal" style="margin-bottom:72px">
      <div>
        <h2>Planning to paint or build?</h2>
        <p>Call us or send a WhatsApp message. We'll help you pick the right product, shade and quantity.</p>
      </div>
      <div class="cta__actions">
        <a class="btn" href="{tel('94171 23935')}">{i('phone')} Call Now</a>
        <a class="btn btn--wa" href="{wa('Namaste Rana Paints!')}" target="_blank" rel="noopener">{i('wa')} WhatsApp</a>
      </div>
    </div>
    <div class="section-head">
      <span class="eyebrow">Visit Us</span>
      <h2>Find our shop</h2>
    </div>
    <div class="contact">
      <div class="contact__cards">
        <div class="contact-card">
          <span class="contact-card__icon">{i('pin')}</span>
          <div><h3>Address</h3><p>Rana Paint &amp; Cement Store<br>Passi Kandi, Dasuya, Punjab</p><a class="link-arrow" href="{MAPS}" target="_blank" rel="noopener">Get directions {i('ext', '2')}</a></div>
        </div>
        <div class="contact-card">
          <span class="contact-card__icon">{i('phone')}</span>
          <div><h3>Shop &amp; Owners</h3><p><a href="{tel('94171 23935')}">94171 23935</a> (WhatsApp)<br><a href="{tel('98764 12125')}">98764 12125</a> &middot; <a href="{tel('98769 63879')}">98769 63879</a></p></div>
        </div>
        <div class="contact-card">
          <span class="contact-card__icon">{i('users')}</span>
          <div><h3>Contractor (site visits)</h3><p>Manjit Rana<br><a href="{tel('99884 12088')}">99884 12088</a> &middot; <a href="{tel('94178 88704')}">94178 88704</a></p></div>
        </div>
        <div class="contact-card">
          <span class="contact-card__icon">{i('mail')}</span>
          <div><h3>Email &amp; Instagram</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="{INSTA}" target="_blank" rel="noopener">@dwon13</a></p></div>
        </div>
      </div>
      <div class="map">
        <iframe title="Rana Paint &amp; Cement Store on Google Maps" src="https://maps.google.com/maps?q=31.829173,75.7406484&amp;z=16&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      </div>
    </div>
  </div>
</section>
"""
    return page("Rana Paints | Paint & Cement Store, Passi Kandi, Dasuya",
                "Rana Paint & Cement Store, Passi Kandi, Dasuya (Punjab). Authorised dealer of Asian Paints, Birla Opus, Berger Paints, Forever Paints and ACC Cement since 2000. Own team of painters, site visit and estimate.",
                body, active="index.html", extra_head=JSONLD)
