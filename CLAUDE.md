# Rana Paints website

Static website for "Rana Paint & Cement Store", Passi Kandi, Dasuya (Punjab). Owner: Daler Singh Rana & Son (son = Abhishek Rana, who is the user). Authorised dealer of Asian Paints, Birla Opus, Berger Paints, Forever Paints and ACC Cement. Theme: white + red.

- Live: https://abhishekrana0909.github.io/rana-paints/ (GitHub Pages, `main` branch, root). Repo: https://github.com/abhishekrana0909/rana-paints (public).
- The `.html` files are GENERATED. Edit `tools/site-builder/*.py` (products in `products.py`, header/footer/phone numbers in `layout.py`), then run `python tools/site-builder/build.py`. Hand edits to `.html` get overwritten.
- `css/style.css`, `js/main.js`, `js/shades.js` are edited directly. After changing CSS/JS, bump the `?v=` number in `layout.py` (or `page_shades.py` for shades.js) so browsers load the new file.
- Preview: `python -m http.server 5500`, then open http://localhost:5500.
- Deploy: commit and `git push` to `origin main`. Pages updates in 1-2 minutes.
- Product photos come from the brand websites (dealer use); room/painter photos from Unsplash. Berger/Birla shade data (`js/data/`) was scraped from their colour catalogues.
- `reference/` and `rana-paints-details.md` (gitignored) hold the owner's original photos and the full list of details the user gave.

The user is learning Python and talks in Hinglish. Explain steps simply in Hinglish. When they are giving requirements, they like to send all details first and say "START" before anything is built.
