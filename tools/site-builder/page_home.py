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
        ("images/stock/hero-living.webp", "Living room with a deep green painted wall"),
        ("images/stock/hero-exterior.webp", "Modern house exterior painted in warm tones"),
        ("images/stock/hero-bedroom.webp", "Bedroom with a navy blue accent wall"),
    ]
    slide_html = "\n".join(
        f'      <div class="hero__slide{" is-active" if k == 0 else ""}"><img src="{src}" alt="{alt}"'
        f'{" fetchpriority=\"high\"" if k == 0 else " loading=\"lazy\""}></div>'
        for k, (src, alt) in enumerate(slides))
    dots = "".join(f'<button type="button" data-slide="{k}" aria-label="Slide {k + 1}"></button>' for k in range(len(slides)))

    brand_cards = [
        ("asian-paints.html", "images/brands/asian-paints.svg", "Asian Paints", "images/products/asian/tractor-emulsion.webp",
         "linear-gradient(135deg,#ffe6d9,#ffc7b6)", "Interior &amp; exterior emulsions, waterproofing, putty, primers and enamels."),
        ("birla-opus.html", "images/brands/birla-opus.svg", "Birla Opus", "images/products/birla/calista-neo-star-shine.webp",
         "linear-gradient(135deg,#efe9fa,#d9ccf2)", "Style and Calista exterior paints, putty and primers."),
        ("berger-paints.html", "images/brands/berger-paints.png", "Berger Paints", "images/products/berger/weathercoat-glow.webp",
         "linear-gradient(135deg,#e2edfb,#bcd3f3)", "WeatherCoat Glow, Walmasta, wall putty and primers."),
        ("forever-paints.html", "images/brands/forever-paints.png", "Forever Paints", "images/products/forever/forever-emulsion.webp",
         "linear-gradient(135deg,#fde6ea,#f7c3cc)", "Budget-friendly emulsions, primer and rustic putty."),
        ("acc-cement.html", "images/brands/acc.svg", "ACC Cement", "images/products/acc/acc-gold-water-shield.webp",
         "linear-gradient(135deg,#fff1c7,#f6c343)", "Gold Water Shield, Concrete Plus and Suraksha Power, with home delivery."),
    ]
    bc = "\n".join(f"""      <a class="brand-card reveal" href="{h}">
        <div class="brand-card__top" style="--c:{bg}"><img src="{prod}" alt="" loading="lazy"{' class="is-photo"' if 'berger' in prod else ''}></div>
        <div class="brand-card__body">
          <img class="brand-card__logo" src="{logo}" alt="{name}" loading="lazy">
          <p>{desc}</p>
          <span class="link-arrow">Explore {name} {i('right', '2')}</span>
        </div>
      </a>""" for h, logo, name, prod, bg, desc in brand_cards)

    strip = "\n".join(f'        <a href="{h}" aria-label="{n}"><img src="{img}" alt="{n}" loading="lazy"></a>' for h, img, n, _ in BRANDS)

    services = [
        ("roller", "Interior &amp; Exterior Painting", "Our own team of painters with 15+ years of experience paints your home neatly and on time."),
        ("estimate", "Site Visit &amp; Estimate", "Our contractor visits your site, checks the walls and gives you a clear estimate for paint and labour."),
        ("umbrella", "Waterproofing Solutions", "Terrace, bathroom, water tank and damp wall solutions with Asian Paints SmartCare and more."),
        ("palette", "Computerised Colour Mixing", "Any shade from the shade card, mixed exactly on ColorWorld and Corob tinting machines."),
        ("bricks", "Cement &amp; Steel Supply", "ACC cement and steel for building your new home, with home delivery of cement."),
        ("layers", "Putty, Primer &amp; Enamel", "Complete range of wall putty, primers, enamels and painting tools under one roof."),
    ]
    sv = "\n".join(f"""      <div class="service reveal">
        <div class="service__icon">{i(ic, '1.6')}</div>
        <h3>{t}</h3>
        <p>{d}</p>
      </div>""" for ic, t, d in services)

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
    <div>
      <div class="hero__badge"><b>SINCE 2000</b> Authorised dealer &middot; Passi Kandi, Dasuya</div>
      <h1>Rang Aapke,<br><span>Bharosa Hamara</span></h1>
      <p class="hero__lead">Paints, putty, waterproofing and cement for every home. Asian Paints, Birla Opus, Berger, Forever and ACC, all under one roof, with our own team of expert painters.</p>
      <div class="hero__actions">
        <a class="btn" href="#brands">Explore Brands {i('right', '2.2')}</a>
        <a class="btn btn--ghost-white" href="shades.html">Explore Shades</a>
      </div>
      <div class="hero__stat">
        <div class="hero__stat-box"><strong>5000+</strong><small>Shades</small></div>
        <p>Mixed exactly on our<br>computerised colour machines</p>
      </div>
    </div>
  </div>
  <div class="hero__dots">
    <button class="hero__arrow hero__arrow--prev" type="button" aria-label="Previous slide">{i('left', '2.2')}</button>
    {dots}
    <button class="hero__arrow hero__arrow--next" type="button" aria-label="Next slide">{i('right', '2.2')}</button>
  </div>
</section>

<!-- ============ DEALER STRIP ============ -->
<section class="brandstrip" aria-label="Authorised dealer of">
  <div class="container">
    <div class="brandstrip__label">Authorised Dealer<small>Genuine products, right price</small></div>
    <div class="brandstrip__logos">
{strip}
    </div>
  </div>
</section>

<!-- ============ ABOUT ============ -->
<section class="section" id="about">
  <div class="container">
    <div class="about">
      <div class="about__media reveal">
        <img src="images/stock/painters-team.webp" alt="Painters painting a bright red and blue wall" loading="lazy">
        <img class="about__small" src="images/stock/swatches.webp" alt="Colour shade card fan" loading="lazy">
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
          <a class="btn" href="#team">Meet Our Team</a>
          <a class="btn btn--outline" href="{tel('94171 23935')}">{i('phone')} Call Us</a>
        </div>
      </div>
    </div>
    <div class="stats">
      <div class="stat reveal"><strong data-count="25" data-suffix="+">25+</strong><span>Years of trust</span></div>
      <div class="stat reveal"><strong data-count="15" data-suffix="+">15+</strong><span>Years painter experience</span></div>
      <div class="stat reveal"><strong data-count="5">5</strong><span>Authorised brands</span></div>
      <div class="stat reveal"><strong data-count="5000" data-suffix="+">5000+</strong><span>Shades available</span></div>
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

<!-- ============ COLOUR MACHINES ============ -->
<section class="section section--soft" id="machines">
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
      <div class="split__media"><img src="images/stock/construction.webp" alt="House under construction" loading="lazy"></div>
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
