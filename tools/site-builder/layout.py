"""Shared page layout: <head>, top bar, header, footer."""
from urllib.parse import quote
from icons import i, LOGO_MARK

SHOP = "Rana Paint &amp; Cement Store"
WA_NUM = "919417123935"
MAPS = ("https://www.google.com/maps/place/RANA+PAINT+HARDWARE+%26+CEMENT+STORE/@31.8291775,75.7380735,1011m/"
        "data=!3m2!1e3!4b1!4m6!3m5!1s0x391b0b5024be199f:0x976d251ef4bd5a5e!8m2!3d31.829173!4d75.7406484!16s%2Fg%2F11vdnwc_x_")
INSTA = "https://www.instagram.com/dwon13/"
EMAIL = "dalerrana123@gmail.com"

BRANDS = [
    ("asian-paints.html", "images/brands/asian-paints.svg", "Asian Paints", "Emulsions, waterproofing, putty, primers &amp; enamels"),
    ("birla-opus.html", "images/brands/birla-opus.svg", "Birla Opus", "Style &amp; Calista exterior paints, putty, primers"),
    ("berger-paints.html", "images/brands/berger-paints.png", "Berger Paints", "WeatherCoat, Walmasta, putty &amp; primers"),
    ("forever-paints.html", "images/brands/forever-paints.png", "Forever Paints", "Emulsions, primer &amp; rustic putty"),
    ("acc-cement.html", "images/brands/acc.svg", "ACC Cement", "Gold Water Shield, Concrete Plus, Suraksha Power"),
]


def wa(text):
    return f"https://wa.me/{WA_NUM}?text={quote(text)}"


def tel(num):
    return f"tel:+91{num.replace(' ', '')}"


def head(title, desc, extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#d2161e">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="images/stock/hero-living.webp">
<link rel="icon" href="images/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800&amp;family=Barlow:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v=4">
{extra}</head>"""


def topbar():
    return f"""<div class="topbar">
  <div class="container">
    <div class="topbar__info">
      <a href="{tel('94171 23935')}">{i('phone')} +91 94171 23935</a>
      <a class="hide-sm" href="mailto:{EMAIL}">{i('mail')} {EMAIL}</a>
      <a class="hide-sm" href="{MAPS}" target="_blank" rel="noopener">{i('pin')} Passi Kandi, Dasuya (Punjab)</a>
    </div>
    <div class="topbar__social">
      <a href="{wa('Namaste Rana Paints!')}" target="_blank" rel="noopener" aria-label="WhatsApp">{i('wa')}</a>
      <a href="{INSTA}" target="_blank" rel="noopener" aria-label="Instagram">{i('instagram')}</a>
      <a href="mailto:{EMAIL}" aria-label="Email">{i('mail')}</a>
      <a href="{MAPS}" target="_blank" rel="noopener" aria-label="Google Maps">{i('pin')}</a>
    </div>
  </div>
</div>"""


def logo(cls=""):
    return (f'<a class="logo {cls}" href="index.html" aria-label="Rana Paints home">{LOGO_MARK}'
            '<span class="logo__text"><span class="logo__name">RANA <b>PAINTS</b></span>'
            '<span class="logo__tag">Paint &amp; Cement Store</span></span></a>')


def header(active=""):
    def cur(key):
        return ' aria-current="page"' if key == active else ""

    brand_active = active in {b[0] for b in BRANDS}
    drop = "\n".join(
        f'          <a href="{href}"{cur(href)}><span class="dropdown__logo"><img src="{img}" alt=""></span>'
        f'<span><strong>{name}</strong><small>{sub}</small></span></a>'
        for href, img, name, sub in BRANDS)
    return f"""<header class="header">
  <div class="container header__inner">
    {logo()}
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul class="nav__list">
        <li><a class="nav__link" href="index.html"{cur('index.html')}>Home</a></li>
        <li class="nav__item--drop">
          <button class="nav__link" type="button" aria-expanded="false" aria-controls="brands-menu"{' aria-current="page"' if brand_active else ''}>Brands {i('chev', '2.4')}</button>
          <div class="dropdown" id="brands-menu">
{drop}
          </div>
        </li>
        <li><a class="nav__link" href="shades.html"{cur('shades.html')}>Shades</a></li>
        <li><a class="nav__link" href="index.html#services">Services</a></li>
        <li><a class="nav__link" href="index.html#team">About Us</a></li>
        <li><a class="nav__link" href="index.html#contact">Contact</a></li>
      </ul>
      <div class="nav__mobile-cta">
        <a class="btn" href="index.html#site-visit">{i('house')} Book a Site Visit</a>
        <a class="btn btn--outline" href="{tel('94171 23935')}">{i('phone')} Call 94171 23935</a>
        <a class="btn btn--wa" href="{wa('Namaste Rana Paints!')}" target="_blank" rel="noopener">{i('wa')} WhatsApp</a>
      </div>
    </nav>
    <div class="header__cta">
      <a class="btn btn--sm" href="index.html#site-visit">Book a Site Visit</a>
      <a class="callbox" href="{tel('94171 23935')}">
        <span class="callbox__icon">{i('phone')}</span>
        <span><small>Call now</small><strong>94171 23935</strong></span>
      </a>
    </div>
    <button class="nav-toggle" type="button" aria-label="Menu" aria-expanded="false" aria-controls="site-nav"><span></span></button>
  </div>
</header>"""


def footer():
    brand_links = "\n".join(f'          <li><a href="{h}">{n}</a></li>' for h, _, n, _ in BRANDS)
    return f"""<footer class="footer">
  <div class="container footer__grid">
    <div>
      {logo()}
      <p style="margin-top:18px">Serving homes in Passi Kandi, Dasuya and nearby villages since 2000. Authorised dealer of India's top paint brands and ACC cement, with our own team of expert painters.</p>
      <div class="footer__social">
        <a href="{wa('Namaste Rana Paints!')}" target="_blank" rel="noopener" aria-label="WhatsApp">{i('wa')}</a>
        <a href="{INSTA}" target="_blank" rel="noopener" aria-label="Instagram">{i('instagram')}</a>
        <a href="mailto:{EMAIL}" aria-label="Email">{i('mail')}</a>
        <a href="{MAPS}" target="_blank" rel="noopener" aria-label="Google Maps">{i('pin')}</a>
      </div>
    </div>
    <div>
      <h4>Our Brands</h4>
      <ul class="footer__links">
{brand_links}
      </ul>
    </div>
    <div>
      <h4>Quick Links</h4>
      <ul class="footer__links">
        <li><a href="index.html">Home</a></li>
        <li><a href="shades.html">Shade Cards</a></li>
        <li><a href="index.html#services">Our Services</a></li>
        <li><a href="index.html#team">Meet the Team</a></li>
        <li><a href="index.html#site-visit">Book a Site Visit</a></li>
        <li><a href="index.html#contact">Contact Us</a></li>
      </ul>
    </div>
    <div>
      <h4>Get In Touch</h4>
      <ul class="footer__contact">
        <li>{i('pin')}<span>{SHOP}<br>Passi Kandi, Dasuya, Punjab</span></li>
        <li>{i('phone')}<span><a href="{tel('94171 23935')}">94171 23935</a>, <a href="{tel('98764 12125')}">98764 12125</a><br><a href="{tel('98769 63879')}">98769 63879</a></span></li>
        <li>{i('users')}<span>Contractor: <a href="{tel('99884 12088')}">99884 12088</a>, <a href="{tel('94178 88704')}">94178 88704</a></span></li>
        <li>{i('mail')}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
      </ul>
    </div>
  </div>
  <div class="footer__bottom">
    <div class="container">
      <span>&copy; <span data-year>2026</span> <b>{SHOP}</b>. All rights reserved.</span>
      <span>Authorised dealer: Asian Paints &middot; Birla Opus &middot; Berger Paints &middot; Forever Paints &middot; ACC Cement</span>
    </div>
  </div>
</footer>
<a class="fab-wa" href="{wa('Namaste Rana Paints! I have a question.')}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{i('wa')}</a>
<button class="to-top" type="button" aria-label="Back to top">{i('up', '2.4')}</button>"""


def page(title, desc, body, active="", body_class="", scripts="", extra_head=""):
    cls = f' class="{body_class}"' if body_class else ""
    return f"""{head(title, desc, extra_head)}
<body{cls}>
<a class="skip-link" href="#main">Skip to content</a>
{topbar()}
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="js/main.js?v=2"></script>
{scripts}</body>
</html>
"""
