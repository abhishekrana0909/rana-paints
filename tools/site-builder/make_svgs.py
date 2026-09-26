"""Draws the illustration images (SVG) for products that have no photo:
spray paint cans, wall stencils, cement colour bag, curtain pipe/brackets,
normal roller and Atul brush.  Run: python tools/site-builder/make_svgs.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "images" / "products"


def write(rel, svg):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(svg.strip() + "\n", encoding="utf-8")


# ---------------------------------------------------------------- spray cans
SPRAY = {
    "red": ("Red", "#d32f2f", "#8e1b1b", "gloss"),
    "black": ("Black", "#1d1d1f", "#000000", "gloss"),
    "white": ("White", "#f7f7f5", "#cfcfca", "gloss"),
    "matt-black": ("Matt Black", "#2b2b2d", "#1a1a1b", "matt"),
    "shyne-black": ("Shyne Black", "#111113", "#000000", "shine"),
    "green": ("Green", "#1e8e3e", "#0f5a24", "gloss"),
    "silver": ("Silver", "#c9ced6", "#7d848f", "metal"),
    "metallic": ("Metallic Gold", "#d4af37", "#8a6d12", "metal"),
}


def spray_svg(key, name, c1, c2, finish):
    hl = {"matt": 0.10, "gloss": 0.35, "shine": 0.6, "metal": 0.55}[finish]
    text = "#1d1d1f" if key in ("white", "silver", "metallic") else "#ffffff"
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 360" role="img" aria-label="{name} spray paint can">
  <defs>
    <linearGradient id="b" x1="0" x2="1">
      <stop offset="0" stop-color="{c2}"/><stop offset=".22" stop-color="{c1}"/>
      <stop offset=".38" stop-color="#ffffff" stop-opacity="{hl}"/><stop offset=".52" stop-color="{c1}"/>
      <stop offset="1" stop-color="{c2}"/>
    </linearGradient>
    <linearGradient id="m" x1="0" x2="1">
      <stop offset="0" stop-color="#8d939c"/><stop offset=".35" stop-color="#eef0f3"/><stop offset="1" stop-color="#7a808a"/>
    </linearGradient>
  </defs>
  <ellipse cx="120" cy="344" rx="70" ry="9" fill="#000" opacity=".12"/>
  <rect x="96" y="22" width="48" height="30" rx="8" fill="url(#b)"/>
  <rect x="110" y="10" width="20" height="16" rx="4" fill="#3a3a3c"/>
  <path d="M72 64c0-10 20-16 48-16s48 6 48 16v8H72z" fill="url(#m)"/>
  <rect x="68" y="70" width="104" height="262" rx="14" fill="url(#b)"/>
  <rect x="68" y="150" width="104" height="112" fill="#ffffff" opacity=".93"/>
  <rect x="68" y="150" width="104" height="10" fill="{c1}"/>
  <circle cx="120" cy="196" r="20" fill="{c1}" stroke="{c2}" stroke-width="3"/>
  <text x="120" y="236" text-anchor="middle" font-family="Arial, sans-serif" font-weight="700" font-size="13" fill="#1d1d1f">SPRAY PAINT</text>
  <text x="120" y="253" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="#555">400 ml</text>
  <text x="120" y="296" text-anchor="middle" font-family="Arial, sans-serif" font-weight="700" font-size="14" fill="{text}">{name.upper()}</text>
  <rect x="68" y="318" width="104" height="14" rx="4" fill="url(#m)"/>
</svg>"""


for key, (name, c1, c2, fin) in SPRAY.items():
    write(f"spray/spray-{key}.svg", spray_svg(key, name, c1, c2, fin))


# ---------------------------------------------------------------- stencils
def frame(bg, motif, inner, label):
    # 2 ft x 1.5 ft = 4:3 sheet
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" role="img" aria-label="{label} wall stencil design">
  <rect width="400" height="300" fill="{bg}"/>
  <g fill="{motif}" stroke="none">{inner}</g>
  <rect x="6" y="6" width="388" height="288" fill="none" stroke="#000" stroke-opacity=".12" stroke-width="2" stroke-dasharray="8 6"/>
</svg>"""


def tile(fn, cols, rows, w, h, ox=0, oy=0):
    out = []
    for r in range(rows):
        for c in range(cols):
            out.append(fn(ox + c * w, oy + r * h, r, c))
    return "".join(out)


def flower(x, y, s=1.0):
    petals = "".join(f'<ellipse cx="{x}" cy="{y - 14 * s}" rx="{7 * s}" ry="{13 * s}" transform="rotate({a} {x} {y})"/>' for a in range(0, 360, 60))
    return petals + f'<circle cx="{x}" cy="{y}" r="{5 * s}" fill-opacity=".6"/>'


STENCILS = {
    "floral-bloom": ("Floral Bloom", "#f3e3d3", "#b5523b",
                     tile(lambda x, y, r, c: flower(x + (40 if r % 2 else 0), y, 1.1), 5, 4, 80, 75, 40, 40)),
    "damask": ("Royal Damask", "#1f3b4d", "#d8c38f",
               tile(lambda x, y, r, c: f'<path d="M{x} {y-34}c10 10 22 18 22 34s-12 24-22 34c-10-10-22-18-22-34s12-24 22-34z" fill-opacity=".9"/><path d="M{x-30} {y}c8-6 16-6 22 0-6 6-14 6-22 0zM{x+8} {y}c6-6 14-6 22 0-8 6-16 6-22 0z"/><circle cx="{x}" cy="{y}" r="5" fill="#1f3b4d"/>', 5, 3, 90, 100, 30, 50)),
    "mandala": ("Mandala", "#f6efe3", "#7a3e8c",
                "".join(f'<ellipse cx="200" cy="{150 - rr}" rx="{rr * .22}" ry="{rr * .45}" transform="rotate({a} 200 150)" fill-opacity="{0.35 + rr / 400}"/>' for rr in (40, 80, 120) for a in range(0, 360, 30)) + '<circle cx="200" cy="150" r="18"/>'),
    "tropical-leaves": ("Tropical Leaves", "#e9f2ea", "#2e7d4f",
                        tile(lambda x, y, r, c: f'<path d="M{x} {y+40}C{x-40} {y+10} {x-20} {y-40} {x+10} {y-50}C{x+30} {y-10} {x+20} {y+20} {x} {y+40}z" transform="rotate({(r*3+c*5)%40-20} {x} {y})"/><path d="M{x} {y+40}L{x+8} {y-44}" stroke="#e9f2ea" stroke-width="2"/>', 5, 3, 85, 100, 30, 55)),
    "moroccan-trellis": ("Moroccan Quatrefoil", "#fbf4ea", "#c96a2b",
                         tile(lambda x, y, r, c: f'<circle cx="{x-11}" cy="{y}" r="13"/><circle cx="{x+11}" cy="{y}" r="13"/><circle cx="{x}" cy="{y-11}" r="13"/><circle cx="{x}" cy="{y+11}" r="13"/><circle cx="{x}" cy="{y}" r="9" fill="#fbf4ea"/>', 7, 5, 60, 64, 20, 22)),
    "birds-branch": ("Birds on Branch", "#eef3f6", "#34495e",
                     '<path d="M0 210C80 190 150 150 240 160s120-20 160-40" fill="none" stroke="#34495e" stroke-width="7" stroke-linecap="round"/>'
                     + "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="5" transform="rotate(-30 {x} {y})" fill="#5d7d63"/>' for x, y in [(60, 195), (110, 178), (180, 160), (270, 158), (330, 142), (370, 125)])
                     + "".join(f'<path d="M{x} {y}c10-22 40-22 44 0 10-2 16 2 20 8-8 0-14 2-18 6 0 14-20 24-40 16l-12 10 2-16c-6-6-4-16 4-24z"/>' for x, y in [(120, 130), (250, 120)])),
    "paisley": ("Paisley", "#fff1e6", "#a8324a",
                tile(lambda x, y, r, c: f'<path d="M{x} {y+30}c-30 0-40-40-10-58 20-12 42 6 36 26-4 12-18 14-22 6 12 2 14-14 2-16-18-2-24 26-6 34" fill="none" stroke="#a8324a" stroke-width="5" stroke-linecap="round"/><circle cx="{x+2}" cy="{y}" r="5"/>', 5, 3, 80, 100, 40, 50)),
    "geometric-diamonds": ("Geometric Diamonds", "#e8eef5", "#27496d",
                           tile(lambda x, y, r, c: f'<path d="M{x} {y-24}l24 24-24 24-24-24z" fill-opacity="{0.5 if (r+c)%2 else 0.95}"/>', 9, 7, 48, 48, 8, 16)),
    "bubbles": ("Bubble Circles", "#f4f9fb", "#1f8fb3",
                "".join(f'<circle cx="{x}" cy="{y}" r="{rr}" fill-opacity="{op}"/>' for x, y, rr, op in [(50, 60, 30, .8), (120, 40, 16, .5), (170, 110, 44, .9), (260, 60, 22, .6), (330, 110, 36, .85), (80, 170, 20, .55), (140, 230, 38, .8), (230, 200, 26, .6), (300, 240, 30, .9), (370, 200, 16, .5), (40, 260, 14, .5), (215, 280, 12, .4)])),
    "lotus": ("Lotus", "#fdf2f5", "#c2185b",
              tile(lambda x, y, r, c: "".join(f'<path d="M{x} {y+20}C{x-18+d} {y} {x-10+d} {y-28} {x+d*.4} {y-40}C{x+10+d} {y-28} {x+18+d} {y} {x} {y+20}z" fill-opacity=".85"/>' for d in (-16, 0, 16)) + f'<path d="M{x-30} {y+24}h60" stroke="#c2185b" stroke-width="4" stroke-linecap="round"/>', 4, 3, 100, 100, 50, 55)),
    "butterflies": ("Butterflies", "#f2f7ee", "#6a4c93",
                    tile(lambda x, y, r, c: f'<g transform="rotate({(r*25+c*15)%50-25} {x} {y})"><path d="M{x} {y}c-6-24-34-30-34-8 0 14 18 16 34 8zM{x} {y}c6-24 34-30 34-8 0 14-18 16-34 8zM{x} {y}c-4 16-24 22-24 8 0-8 12-10 24-8zM{x} {y}c4 16 24 22 24 8 0-8-12-10-24-8z"/><rect x="{x-2}" y="{y-14}" width="4" height="26" rx="2"/></g>', 5, 3, 80, 95, 40, 55)),
    "bamboo": ("Bamboo", "#f1f6e9", "#3f7d3a",
               "".join(f'<rect x="{x}" y="0" width="16" height="300" rx="6"/>' + "".join(f'<rect x="{x - 3}" y="{j}" width="22" height="5" rx="2" fill="#f1f6e9"/>' for j in range(40 + (i * 23) % 50, 300, 90))
                       + f'<path d="M{x + 16} {80 + i * 17}c30-14 46-8 60 4-20 6-40 6-60-4z"/><path d="M{x} {170 + i * 11}c-30-12-46-4-58 8 20 4 40 2 58-8z"/>'
                       for i, x in enumerate((40, 130, 220, 310)))),
}

for key, (label, bg, motif, inner) in STENCILS.items():
    write(f"stencils/{key}.svg", frame(bg, motif, inner, label))


# ---------------------------------------------------------------- cement colour bag
CEMENT_COLOURS = [("White", "#f5f5f2"), ("Mid Cream", "#efe0bb"), ("Apple Green", "#9ccc65"), ("Bone White", "#efe7d4"),
                  ("Dove Gray", "#a7a8aa"), ("Dark Gray", "#5b5d60"), ("Bright Pink", "#ec407a"), ("Sky Blue", "#7ec8e3"),
                  ("Light Green", "#b5e3a1"), ("Dark Pink", "#c2185b")]
dots = "".join(f'<circle cx="{92 + (k % 5) * 34}" cy="{232 + (k // 5) * 34}" r="13" fill="{c}" stroke="#00000022" stroke-width="2"/>' for k, (_, c) in enumerate(CEMENT_COLOURS))
write("misc/cement-colour-bag.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 380" role="img" aria-label="Cement colour 20 kg bag">
  <ellipse cx="180" cy="362" rx="130" ry="10" fill="#000" opacity=".12"/>
  <path d="M58 40q122-22 244 0l12 300q-134 26-268 0z" fill="#fbfaf7" stroke="#d9d4c8" stroke-width="3"/>
  <path d="M58 40q122-22 244 0l2 34q-124-20-248 0z" fill="#d2161e"/>
  <path d="M46 340q134 26 268 0l-2-30q-132 22-264 0z" fill="#d2161e"/>
  <text x="180" y="112" text-anchor="middle" font-family="Arial Narrow, Arial, sans-serif" font-weight="700" font-size="30" fill="#16161b">CEMENT COLOUR</text>
  <text x="180" y="140" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#676773">Powder colour for cement &amp; floors</text>
  <rect x="120" y="156" width="120" height="36" rx="18" fill="#16161b"/>
  <text x="180" y="181" text-anchor="middle" font-family="Arial, sans-serif" font-weight="700" font-size="18" fill="#fff">20 kg</text>
  {dots}
</svg>""")


# ---------------------------------------------------------------- curtain pipe + brackets
STEEL = '<linearGradient id="s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4f6f8"/><stop offset=".45" stop-color="#b9c0c8"/><stop offset=".55" stop-color="#8e969f"/><stop offset="1" stop-color="#dfe3e8"/></linearGradient>'
write("curtain/curtain-pipe.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 300" role="img" aria-label="Steel curtain pipe">
  <defs>{STEEL}<linearGradient id="v" x1="0" x2="1"><stop offset="0" stop-color="#9aa2ab"/><stop offset=".4" stop-color="#f1f3f5"/><stop offset="1" stop-color="#8b939c"/></linearGradient></defs>
  <g transform="rotate(-18 210 150)">
    <rect x="40" y="138" width="340" height="24" rx="12" fill="url(#s)"/>
    <rect x="16" y="126" width="34" height="48" rx="8" fill="url(#v)"/>
    <rect x="370" y="126" width="34" height="48" rx="8" fill="url(#v)"/>
    <rect x="140" y="132" width="16" height="36" rx="4" fill="#6b737c"/>
    <rect x="264" y="132" width="16" height="36" rx="4" fill="#6b737c"/>
  </g>
  <text x="210" y="272" text-anchor="middle" font-family="Arial, sans-serif" font-weight="700" font-size="20" fill="#33333d">12 ft  ·  15 ft</text>
</svg>""")


def bracket(depth, label):
    d = depth
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 320" role="img" aria-label="{label} steel curtain bracket">
  <defs>{STEEL}</defs>
  <path d="M60 {300} h{d} a14 14 0 0 0 14-14 V110 a50 50 0 1 1 100 0 v14 h-18 v-14 a32 32 0 1 0-64 0 V286 a32 32 0 0 1-32 32 H60z"
        fill="#c3c9d0" stroke="#7d858e" stroke-width="3" stroke-linejoin="round" transform="translate({-(d - 60) / 2} -10)"/>
  <circle cx="{175 - (d - 60) / 2}" cy="102" r="7" fill="#5f6770"/>
  <circle cx="{80 - (d - 60) / 2}" cy="{280}" r="4" fill="#5f6770"/><circle cx="{80 + d * .6 - (d - 60) / 2}" cy="{280}" r="4" fill="#5f6770"/>
  <text x="130" y="30" text-anchor="middle" font-family="Arial, sans-serif" font-weight="700" font-size="18" fill="#33333d">{label}</text>
</svg>"""


write("curtain/bracket-small.svg", bracket(60, "Small"))
write("curtain/bracket-big.svg", bracket(100, "Big"))


# ---------------------------------------------------------------- normal roller & Atul brush
write("tools/normal-roller.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" role="img" aria-label="Paint roller">
  <defs><linearGradient id="r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".6" stop-color="#f1ece2"/><stop offset="1" stop-color="#d9d2c4"/></linearGradient></defs>
  <ellipse cx="160" cy="300" rx="110" ry="9" fill="#000" opacity=".1"/>
  <rect x="40" y="40" width="220" height="70" rx="30" fill="url(#r)" stroke="#d6cfc2" stroke-width="2"/>
  <path d="M60 58h180M60 75h180M60 92h180" stroke="#e7e0d3" stroke-width="3"/>
  <rect x="40" y="40" width="46" height="70" rx="22" fill="#e8742a" opacity=".85"/>
  <path d="M260 75h22v70H160v48" fill="none" stroke="#a9b0b8" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="146" y="186" width="28" height="104" rx="12" fill="#d2161e"/>
  <rect x="152" y="196" width="6" height="84" rx="3" fill="#fff" opacity=".35"/>
</svg>""")

write("tools/atul-brush.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" role="img" aria-label="Paint brush">
  <defs><linearGradient id="f" x1="0" x2="1"><stop offset="0" stop-color="#9aa2ab"/><stop offset=".45" stop-color="#f1f3f5"/><stop offset="1" stop-color="#8b939c"/></linearGradient>
  <linearGradient id="h" x1="0" x2="1"><stop offset="0" stop-color="#1c3f9e"/><stop offset=".5" stop-color="#3d6be0"/><stop offset="1" stop-color="#1c3f9e"/></linearGradient></defs>
  <g transform="rotate(-35 160 160)">
    <path d="M110 30h100v70H110z" fill="#e9d29a"/>
    <path d="M110 30h100" stroke="#cdb577" stroke-width="3"/>
    <path d="M122 30v70M136 30v70M150 30v70M164 30v70M178 30v70M192 30v70" stroke="#d8bf82" stroke-width="2"/>
    <rect x="104" y="100" width="112" height="46" rx="6" fill="url(#f)"/>
    <path d="M104 118h112" stroke="#7d858e" stroke-width="2"/>
    <path d="M128 146h64l-10 40c-2 10-4 60-6 96a16 16 0 0 1-32 0c-2-36-4-86-6-96z" fill="url(#h)"/>
    <circle cx="160" cy="266" r="6" fill="#0f2466"/>
  </g>
</svg>""")

# ---------------------------------------------------------------- texture putty bag
write("misc/texture-putty-bag.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 380" role="img" aria-label="Texture putty 25 kg bag">
  <ellipse cx="180" cy="362" rx="130" ry="10" fill="#000" opacity=".12"/>
  <path d="M58 40q122-22 244 0l12 300q-134 26-268 0z" fill="#fbfaf7" stroke="#d9d4c8" stroke-width="3"/>
  <path d="M58 40q122-22 244 0l2 34q-124-20-248 0z" fill="#5b3fa0"/>
  <path d="M46 340q134 26 268 0l-2-30q-132 22-264 0z" fill="#5b3fa0"/>
  <g fill="#e6dfd2"><circle cx="110" cy="240" r="6"/><circle cx="140" cy="262" r="4"/><circle cx="175" cy="236" r="7"/><circle cx="210" cy="258" r="5"/><circle cx="246" cy="238" r="6"/><circle cx="128" cy="286" r="5"/><circle cx="196" cy="290" r="6"/><circle cx="232" cy="284" r="4"/></g>
  <text x="180" y="116" text-anchor="middle" font-family="Arial Narrow, Arial, sans-serif" font-weight="700" font-size="30" fill="#16161b">TEXTURE PUTTY</text>
  <text x="180" y="142" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#676773">For textured wall finishes</text>
  <rect x="120" y="158" width="120" height="36" rx="18" fill="#16161b"/>
  <text x="180" y="183" text-anchor="middle" font-family="Arial, sans-serif" font-weight="700" font-size="18" fill="#fff">25 kg</text>
</svg>""")

print("SVG illustrations written to", ROOT)
