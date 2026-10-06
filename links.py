"""Link-in-bio page for Instagram at www.glpxstudio.com/links (same address the IG bio already uses).
Standalone mobile-first page in the site's red and black style. Runs from areas.py."""
from build import ROOT, FONTS

IG = "https://www.instagram.com/glpxstudio/"
REVIEWS = "https://www.google.com/search?q=GLPX+Studio+Orlando#lrd=0xae321d709281f5d:0xc845892b9d5b52b4,1,,,,"

main_btn = ("Book a free strategy call", "../book.html")
links = [
    ("See the work", "../portfolio.html", "All four services in one place"),
    ("Headshots", "../headshots.html", "Professionals, actors and teams"),
    ("Branding", "../branding.html", "Planned shoots for your brand"),
    ("Editorial &amp; Music", "../editorial.html", "Covers, press kits, beauty, fashion"),
    ("Corporate Events", "../corporate-event-photography-orlando.html", "English &amp; Español coverage"),
    ("Client Gallery", "https://gallery.glpxstudio.com", "Already shot with me? Your photos are here"),
    ("Journal", "../blog/index.html", "Guides: what to wear, where to shoot"),
    ("About Gerson", "../about.html", "8+ years behind the camera"),
    ("Google reviews · 5.0 ★", REVIEWS, "What clients say"),
]
rows = "\n".join(
    f'      <a class="lk" href="{h}"{" target=\"_blank\" rel=\"noopener\"" if h.startswith("http") else ""}><span><b>{t}</b><small>{s}</small></span><i>→</i></a>'
    for t, h, s in links)

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>GLPX Studio · Links</title>
<meta name="description" content="GLPX Studio links: book a free strategy call, see the work, client galleries and more. Branding, headshot and editorial photography in Orlando.">
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://www.glpxstudio.com/links/">
<meta property="og:title" content="GLPX Studio · Orlando Branding &amp; Headshot Photography">
<meta property="og:description" content="Book a free strategy call, see the work and find your client gallery.">
<meta property="og:image" content="https://www.glpxstudio.com/assets/img/og-home.jpg">
<meta property="og:url" content="https://www.glpxstudio.com/links/">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../assets/img/favicon.png">
<link rel="apple-touch-icon" href="../assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<style>
  :root {{ --red:#E53935; --night:#100D0C; --night2:#1B1715; --bone:#F3ECE3; --dust:#B9AA9C;
          --tall:"Libre Caslon Condensed", Georgia, serif; --wide:"Archivo", Arial, sans-serif; --body:"DM Sans", Arial, sans-serif; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: var(--night); color: var(--bone); font: 400 16px/1.5 var(--body); -webkit-font-smoothing: antialiased; min-height: 100vh; }}
  .hero {{ position: relative; height: 300px; overflow: hidden; }}
  .hero img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 30%; display: block; }}
  .hero::after {{ content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(16,13,12,.15) 0%, rgba(16,13,12,.35) 50%, var(--night) 100%); }}
  .wrap {{ max-width: 480px; margin: -110px auto 0; padding: 0 18px 40px; position: relative; z-index: 2; text-align: center; }}
  .logo {{ width: 110px; margin: 0 auto 14px; display: block; }}
  h1 {{ font: 400 2.6rem/.9 var(--tall); text-transform: uppercase; letter-spacing: -.005em; }}
  h1 em {{ color: var(--red); font-style: italic; }}
  .sub {{ margin: 12px auto 0; color: var(--dust); font-size: 15px; max-width: 34ch; }}
  .kick {{ margin-top: 14px; font: 700 10px/1.4 var(--wide); font-stretch: 125%; letter-spacing: .16em; text-transform: uppercase; color: var(--red); }}
  .cta {{ display: block; margin: 24px 0 12px; padding: 18px 20px; border-radius: 999px; background: var(--red); color: #fff; text-decoration: none;
          font: 700 13px/1 var(--wide); font-stretch: 125%; letter-spacing: .12em; text-transform: uppercase; box-shadow: 0 14px 30px -14px rgba(229,57,53,.7); }}
  .cta small {{ display: block; margin-top: 7px; font: 400 12px/1 var(--body); letter-spacing: 0; text-transform: none; opacity: .9; }}
  .quick {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-bottom: 18px; }}
  .quick a {{ padding: 12px 6px; border: 1px solid #3A322E; border-radius: 999px; color: var(--bone); text-decoration: none;
              font: 700 10px/1 var(--wide); font-stretch: 125%; letter-spacing: .12em; text-transform: uppercase; }}
  .quick a:active, .quick a:hover {{ border-color: var(--red); color: var(--red); }}
  .list {{ display: grid; gap: 10px; text-align: left; }}
  .lk {{ display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 15px 18px; background: var(--night2); border: 1px solid #2A2421;
         color: var(--bone); text-decoration: none; transition: border-color .2s, transform .2s; }}
  .lk:hover, .lk:active {{ border-color: var(--red); transform: translateY(-1px); }}
  .lk b {{ display: block; font: 400 1.35rem/1 var(--tall); text-transform: uppercase; }}
  .lk small {{ display: block; margin-top: 5px; color: var(--dust); font-size: 13px; }}
  .lk i {{ font-style: normal; color: var(--red); font-size: 18px; }}
  .site {{ display: inline-block; margin-top: 26px; color: var(--bone); text-decoration: none; border-bottom: 1px solid var(--red); padding-bottom: 3px;
           font: 700 11px/1 var(--wide); font-stretch: 125%; letter-spacing: .14em; text-transform: uppercase; }}
  .fine {{ margin-top: 22px; color: #6E625A; font: 700 9px/1.6 var(--wide); font-stretch: 125%; letter-spacing: .14em; text-transform: uppercase; }}
</style>
</head>
<body>
  <div class="hero"><img src="../assets/img/br-steps.jpg" alt="Branding portrait on the downtown Orlando steps by GLPX Studio"></div>
  <main class="wrap">
    <img class="logo" src="../assets/img/logo-cream.png" alt="GLPX Studio">
    <h1>Refuse to be <em>(forgettable).</em></h1>
    <p class="sub">Branding, headshot and editorial photography in Orlando, by Gerson Lopez.</p>
    <p class="kick">English · Español · 5.0 ★ on Google</p>

    <a class="cta" href="{main_btn[1]}">{main_btn[0]}<small>Pick a time · custom quote within 24 hours</small></a>
    <div class="quick">
      <a href="sms:+14075347581">Text</a>
      <a href="tel:+14075347581">Call</a>
      <a href="mailto:glpxstudio@gmail.com">Email</a>
    </div>

    <nav class="list" aria-label="Links">
{rows}
    </nav>

    <a class="site" href="../index.html">Visit glpxstudio.com</a>
    <p class="fine">© 2026 GLPX Studio · Orlando, FL</p>
  </main>
</body>
</html>
'''
d = ROOT / "links"
d.mkdir(exist_ok=True)
(d / "index.html").write_text(html)
print("links page built")
