CSS = """
@font-face{font-family:Fr;src:url(assets/fraunces-latin-900-normal.woff2);font-weight:900}
@font-face{font-family:Fr;src:url(assets/fraunces-latin-700-normal.woff2);font-weight:700}
@font-face{font-family:Fr;src:url(assets/fraunces-latin-900-italic.woff2);font-weight:900;font-style:italic}
@font-face{font-family:Fr;src:url(assets/fraunces-latin-700-italic.woff2);font-weight:700;font-style:italic}
@font-face{font-family:SG;src:url(assets/space-grotesk-latin-400-normal.woff2);font-weight:400}
@font-face{font-family:SG;src:url(assets/space-grotesk-latin-500-normal.woff2);font-weight:500}
@font-face{font-family:SG;src:url(assets/space-grotesk-latin-700-normal.woff2);font-weight:700}
@font-face{font-family:JB;src:url(assets/jetbrains-mono-latin-400-normal.woff2);font-weight:400}
@font-face{font-family:JB;src:url(assets/jetbrains-mono-latin-500-normal.woff2);font-weight:500}
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#170c26;--ink:#fff;--mute:#cbbde0;--pink:#ff4fa3;--pink2:#ff8cc6;--pinks:rgba(255,79,163,.18);--vio:#9b6bff;--lila:rgba(185,156,255,.2);--line:rgba(255,255,255,.14);--card:#24143a;--dk:#1f1230}
html,body{width:1080px;height:1350px;overflow:hidden;background:var(--bg)}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;color:var(--ink);font-family:SG;
 background:radial-gradient(700px 600px at 95% 0%,rgba(255,79,163,.30),transparent 70%),
            radial-gradient(800px 700px at 0% 100%,rgba(139,92,255,.32),transparent 70%),var(--bg)}
.s:before{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.10) 1.6px,transparent 1.6px);background-size:36px 36px;mask:linear-gradient(180deg,#000,transparent 40%);-webkit-mask:linear-gradient(180deg,#000 0%,transparent 35%)}
.top{position:absolute;top:52px;left:64px;right:64px;display:flex;align-items:center;justify-content:space-between;z-index:5}
.brand{font-weight:700;font-size:30px;letter-spacing:-.5px;display:flex;align-items:center;gap:14px}
.brand i{font-style:normal;color:var(--pink)}
.brand span{font-weight:500;color:#d9c8ff;font-size:24px;background:var(--lila);padding:6px 16px;border-radius:999px}
.count{font-family:JB;font-size:24px;padding:9px 20px;border-radius:999px;background:#fff;color:var(--bg)}
.tags{display:flex;gap:12px;align-items:center}
.tag{font-family:JB;font-size:22px;padding:8px 18px;border-radius:999px;border:2px solid var(--line);background:transparent}
.tag.d{background:#fff;color:var(--bg);border-color:#fff;font-family:SG;font-weight:700;letter-spacing:1.5px;font-size:20px}
h2{font-family:Fr;font-weight:900;font-size:84px;line-height:.98;letter-spacing:-2.5px}
h2 em{font-style:italic;color:var(--pink)}
.desc{font-size:34px;line-height:1.4;color:var(--mute)}
.desc b{color:var(--ink)}
.prompt{position:relative;background:var(--card);border:2.5px solid var(--ink);border-radius:28px;padding:50px 38px 30px;box-shadow:8px 8px 0 var(--pink)}
.prompt .lbl{position:absolute;top:-20px;left:30px;font-weight:700;font-size:21px;letter-spacing:2px;background:var(--pink);color:#fff;padding:8px 18px;border-radius:999px}
.prompt p{font-family:JB;font-size:27px;line-height:1.5}
.prompt .v{color:var(--pink);font-weight:500}
.foot{position:absolute;left:64px;right:64px;bottom:44px;display:flex;align-items:center;justify-content:space-between;font-family:JB;font-size:22px;color:var(--mute)}
.swipe{font-family:Fr;font-style:italic;font-weight:700;font-size:32px;color:var(--pink)}
.body{position:absolute;left:64px;right:64px;top:140px}
.g{position:relative;height:420px;margin-top:40px;transform:scale(1.1);transform-origin:center top;margin-bottom:42px}
.win{position:absolute;background:var(--card);border-radius:26px;border:2px solid var(--line);box-shadow:0 24px 50px rgba(0,0,0,.4);overflow:hidden}
.bar{height:44px;display:flex;align-items:center;gap:9px;padding:0 18px;border-bottom:2px solid var(--line);font-family:JB;font-size:18px;color:var(--mute)}
.bar i{width:13px;height:13px;border-radius:50%;background:#ffb3d1;display:block}
.bar i:nth-child(2){background:#cdb8ff}.bar i:nth-child(3){background:#ffd9a8}
.bar span{margin-left:10px}
.sticker{position:absolute;font-family:Fr;font-style:italic;font-weight:900;color:#fff;background:var(--pink);padding:12px 22px;border-radius:16px;box-shadow:0 12px 24px rgba(232,65,138,.35)}
.note{position:absolute;background:#fff4c9;padding:22px 26px;border-radius:6px;box-shadow:0 14px 28px rgba(80,30,110,.15);font-family:Fr;font-weight:700;font-style:italic;font-size:27px;line-height:1.45;color:var(--dk)}
"""

# ---------------------------------------------------------------------------
# Uso: python3 render.py contenido.json carpeta_salida
# Genera slide-1.png ... slide-N.png en 1080x1350.
# ---------------------------------------------------------------------------
import json, os, sys, shutil
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))

def page(inner, n, total, foot=True, light_brand=False):
    f = '<div class=foot><span>@mariamarin.ai · trucos de IA</span><span class=swipe>desliza →</span></div>' if foot else ''
    extra = '<style>.top .brand{color:#fff}</style>' if light_brand else ''
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style>{extra}</head><body><div class=s>
<div class=top><div class=brand><div>mariamarin<i>.ai</i></div><span>{SERIE}</span></div><div class=count>{n}/{total}</div></div>
{inner}{f}</div></body></html>"""

# Fotos de portada (plantilla/assets/portadas/) y su encuadre CSS "posición/tamaño".
# Para agregar una foto nueva: guárdala en esa carpeta y añade su encuadre aquí.
FOTOS = {
    "auto.png": "60% 8%/cover",
    "cocina.jpg": "50% 0%/cover",
    "luz-roja.jpg": "50% -200px/1080px auto",
    "lentes.jpg": "-280px 0/auto 1000px no-repeat",
}

def elegir_foto(json_path):
    """Rota las fotos: elige la que hace más tiempo no se usa (o nunca se ha usado),
    mirando publicados/*/contenido.json. Los carruseles sin 'foto' cuentan como auto.png."""
    repo = os.path.dirname(HERE)
    pub = os.path.join(repo, "publicados")
    yo = os.path.abspath(json_path)
    ultimo = {}
    for i, d in enumerate(sorted(os.listdir(pub)) if os.path.isdir(pub) else []):
        f = os.path.join(pub, d, "contenido.json")
        if os.path.isfile(f) and os.path.abspath(f) != yo:
            try:
                ultimo[json.load(open(f, encoding="utf-8"))["portada"].get("foto", "auto.png")] = i
            except Exception:
                pass
    disponibles = [f for f in FOTOS if os.path.isfile(os.path.join(HERE, "assets", "portadas", f))]
    return min(disponibles, key=lambda f: (ultimo.get(f, -1), list(FOTOS).index(f)))

def portada(c, total):
    return page(f"""
<div style="position:absolute;inset:0;background:url(assets/portadas/{c['foto']}) {FOTOS.get(c['foto'], 'center top/cover')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(23,12,38,.55) 0%,rgba(23,12,38,0) 16%,rgba(23,12,38,0) 44%,rgba(23,12,38,.85) 58%,#170c26 70%)"></div>
<div style="position:absolute;left:64px;top:140px" class=tags><div class="tag d">{c['hashtag']}</div></div>
<div class=sticker style="right:70px;top:430px;font-size:34px;transform:rotate(6deg)">{c.get('sticker','nivel pro ✦')}</div>
<div style="position:absolute;left:64px;right:64px;bottom:110px">
  <h1 style="font-family:Fr;font-weight:900;font-size:{c.get('titulo_px',108)}px;line-height:.95;letter-spacing:-3.5px">{c['titulo']}</h1>
  <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:30px">
    <p style="font-family:JB;font-size:27px;line-height:1.45;color:var(--mute);max-width:600px">{c['subtitulo']}</p>
    <div class=swipe style="font-size:40px;text-align:right;line-height:1.05">guárdalo<br>y desliza →</div>
  </div>
</div>
<div class=foot><span>@mariamarin.ai</span><span></span></div>""", 1, total, foot=False, light_brand=True)

def contenido(sl, n, total):
    return page(f"""<div class=body>
<div class=tags><div class=tag>/ {sl['num']}</div><div class="tag d">{sl['etiqueta']}</div></div>
<h2 style="margin-top:22px">{sl['titulo']}</h2>
<div class=g>{sl.get('grafico','')}</div>
<p class=desc style="margin-top:26px">{sl['texto']}</p>
<div class=prompt style="margin-top:44px"><div class=lbl>{sl.get('caja_titulo','PÍDELE ASÍ')}</div><p>{sl['caja_texto']}</p></div>
</div>""", n, total)

def cierre(c, total):
    colores = ["#eafaf0", "#efe8ff", "#ffe0ee", "#fff4c9", "#e9f1ff", "#ffe0ee"]
    items = c['items']
    cols = 2 if len(items) in (2, 4) else 3
    grid = "".join(f'<div style="background:{colores[i % len(colores)]};border:2px solid rgba(31,18,48,.08);border-radius:20px;padding:20px 22px;min-height:120px;color:var(--dk)"><div style="font-family:JB;font-size:19px;color:var(--pink)">{str(i+1).zfill(2)}</div><div style="font-family:Fr;font-weight:900;font-size:29px;line-height:1.1;margin-top:8px">{t}</div></div>' for i, t in enumerate(items))
    html = page(f"""<div class=body style="text-align:center">
<div class=tags style="justify-content:center"><div class=tag>/ {c.get('mini','gratis')}</div><div class="tag d">TE LO MANDO GRATIS</div></div>
<h2 style="font-size:110px;margin-top:26px">{c['titulo']}</h2>
<div style="margin-top:44px;background:var(--card);border:2px solid var(--line);border-radius:36px;padding:40px;box-shadow:0 24px 50px rgba(0,0,0,.35)">
 <div style="display:inline-block;background:linear-gradient(90deg,var(--pink),var(--vio));color:#fff;font-weight:700;font-size:50px;padding:24px 50px;border-radius:999px;box-shadow:0 14px 30px rgba(232,65,138,.35)">Comenta <span style="letter-spacing:1px">{c['palabra']}</span></div>
 <div style="font-family:Fr;font-style:italic;font-weight:700;font-size:36px;margin-top:24px">{c.get('promesa','y te llega directo a tu DM ✦')}</div>
</div>
<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:16px;margin-top:40px;text-align:left">{grid}</div>
<p style="margin-top:34px;font-size:28px;color:var(--mute)"><b style="color:var(--pink)">Guárdalo</b> y sígueme para más trucos de IA.</p>
</div>""", total, total, foot=False)
    return html.replace("</div></body>", '<div class=foot style="justify-content:center"><span>@mariamarin.ai · trucos de IA</span></div></div></body>')

def main(json_path, out_dir):
    global SERIE
    data = json.load(open(json_path, encoding="utf-8"))
    SERIE = data.get("serie", "trucos de IA")
    if not data["portada"].get("foto"):
        data["portada"]["foto"] = elegir_foto(json_path)
        json.dump(data, open(json_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("foto de portada:", data["portada"]["foto"])
    slides = data["slides"]
    total = len(slides) + 2
    pages = [portada(data["portada"], total)] + [contenido(s, i + 2, total) for i, s in enumerate(slides)] + [cierre(data["cierre"], total)]
    os.makedirs(out_dir, exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 1080, "height": 1350})
        for i, html in enumerate(pages, 1):
            fn = os.path.join(HERE, f"_tmp_slide{i}.html")
            open(fn, "w", encoding="utf-8").write(html)
            pg.goto("file://" + fn)
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(out_dir, f"slide-{i}.jpg"), type="jpeg", quality=92)
            os.remove(fn)
        br.close()
    print(f"{len(pages)} slides en {out_dir}")

SERIE = "trucos de IA"
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
