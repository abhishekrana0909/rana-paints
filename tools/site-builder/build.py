"""Generate the static Rana Paints website into the project folder."""
from pathlib import Path
import page_home, page_brands, page_shades, page_tools
from icons import FAVICON

OUT = Path(__file__).resolve().parents[2]  # the project folder

pages = {
    "index.html": page_home.build(),
    "asian-paints.html": page_brands.asian(),
    "berger-paints.html": page_brands.berger(),
    "birla-opus.html": page_brands.birla(),
    "forever-paints.html": page_brands.forever(),
    "acc-cement.html": page_brands.acc(),
    "shades.html": page_shades.build(),
    "tools.html": page_tools.build(),
}
for name, html in pages.items():
    (OUT / name).write_text(html, encoding="utf-8")
    print(f"{name:22} {len(html):>7} bytes")
(OUT / "images" / "favicon.svg").write_text(FAVICON, encoding="utf-8")
