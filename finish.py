"""Final pass over every built page: structured data, social previews, lazy images.
Runs automatically at the end of areas.py (python3 areas.py rebuilds everything)."""
import json, re, pathlib

ROOT = pathlib.Path(__file__).parent
SITE = "https://www.glpxstudio.com/"
VERSION = "20261005h"
SKIP = {"index-v1.html", "index-v2.html", "artifact-index.html"}

BUSINESS = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "additionalType": "https://schema.org/Photographer",
    "name": "GLPX Studio",
    "url": SITE,
    "logo": SITE + "assets/img/logo-black.png",
    "image": SITE + "assets/img/br-director.jpg",
    "description": "Branding, headshot, editorial and corporate event photography in Orlando, FL. Sessions in English and Spanish.",
    "telephone": "+1-407-534-7581",
    "email": "glpxstudio@gmail.com",
    "address": {"@type": "PostalAddress", "addressLocality": "Orlando", "addressRegion": "FL", "addressCountry": "US"},
    "areaServed": ["Orlando", "Winter Park", "Lake Nona", "Downtown Orlando", "Baldwin Park", "Dr. Phillips", "Windermere",
                   "Thornton Park", "Kissimmee", "Winter Garden", "Altamonte Springs", "Lake Mary", "Sanford", "Oviedo", "Celebration"],
    "knowsLanguage": ["en", "es"],
    "sameAs": ["https://www.instagram.com/glpxstudio/"],
}
LD = '<script type="application/ld+json">' + json.dumps(BUSINESS, ensure_ascii=False) + "</script>\n"

# Mobile sticky bar (phones only): Text Me + Request a Consultation.
# Links are root-absolute so they work from blog/ and other folder pages too.
CTA_SKIP = {"book.html", "booked.html", "404.html"}
CTA_BAR = """<!-- glpx-cta-bar -->
<style>
#glpx-cta{display:none}
@media (max-width:767px){
#glpx-cta{display:flex;gap:10px;position:fixed;left:0;right:0;bottom:0;z-index:9999;padding:10px 12px calc(10px + env(safe-area-inset-bottom));background:rgba(16,13,12,.96);border-top:1px solid #2A2421;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);transition:transform .25s ease}
#glpx-cta.is-hidden{transform:translateY(110%)}
#glpx-cta a{display:flex;align-items:center;justify-content:center;gap:8px;min-height:48px;border-radius:999px;font:700 clamp(9.5px,2.85vw,11px)/1 "Archivo","Helvetica Neue",Arial,sans-serif;font-stretch:125%;letter-spacing:.06em;text-transform:uppercase;text-align:center;white-space:nowrap;text-decoration:none;color:#fff;padding:0 12px;-webkit-tap-highlight-color:transparent;transition:transform .15s ease,opacity .15s ease}
#glpx-cta a:active{transform:scale(.97);opacity:.85}
#glpx-cta .cta-text{flex:0 0 auto;padding:0 14px;border:1px solid #B9AA9C;background:transparent}
#glpx-cta .cta-book{flex:1;min-width:0;border:1px solid #E53935;background:#E53935}
#glpx-cta svg{width:16px;height:16px;flex-shrink:0}
@media (max-width:350px){#glpx-cta svg{display:none}}
body{padding-bottom:calc(70px + env(safe-area-inset-bottom))}
}
</style>
<nav id="glpx-cta" aria-label="Contact GLPX Studio">
<a class="cta-text" href="sms:+14075347581?&amp;body=Hi%20Gerson!%20I%27m%20interested%20in%20a%20GLPX%20Studio%20session." aria-label="Text GLPX Studio at (407) 534-7581"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>Text Me</a>
<a class="cta-book" href="/book.html">Request a Consultation</a>
</nav>
<script>
(function(){var b=document.getElementById('glpx-cta');if(!b)return;var last=window.pageYOffset,t=false;
window.addEventListener('scroll',function(){if(t)return;t=true;requestAnimationFrame(function(){var y=window.pageYOffset,end=(window.innerHeight+y)>=document.body.scrollHeight-80;
if(y>last+8&&y>200&&!end)b.classList.add('is-hidden');else if(y<last-8||end)b.classList.remove('is-hidden');last=y;t=false;});},{passive:true});})();
</script>
<!-- /glpx-cta-bar -->
"""


def add_cta_bar(html, name):
    """Insert the mobile CTA bar before </body> once (safe to run repeatedly)."""
    if name in CTA_SKIP or "<!-- glpx-cta-bar -->" in html or "</body>" not in html:
        return html
    i = html.rfind("</body>")
    return html[:i] + CTA_BAR + html[i:]


def finish(path, url=None):
    html = path.read_text()
    name = path.name
    url = url or SITE + ("" if name == "index.html" else name)
    head_add = ""
    if "application/ld+json" not in html:
        head_add += LD
    if 'rel="canonical"' not in html:
        head_add += f'<link rel="canonical" href="{url}">\n'
    if "og:image" not in html:
        main = html.split("<main>", 1)[-1]
        m = re.search(r'<img src="(assets/img/(?!logo)[^"]+)"', main.split("<footer", 1)[0])
        img = SITE + (m.group(1) if m else "assets/img/og-home.jpg")
        if name == "index.html" and url == SITE:
            img = SITE + "assets/img/og-home.jpg"  # 1200x630 share card
            head_add += '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
        head_add += f'<meta property="og:image:alt" content="GLPX Studio, Orlando branding and headshot photography">\n'
        title = re.search(r"<title>(.*?)</title>", html, re.S).group(1)
        desc_m = re.search(r'<meta name="description" content="([^"]*)"', html)
        if 'property="og:title"' not in html:
            head_add += f'<meta property="og:title" content="{title}">\n'
            if desc_m:
                head_add += f'<meta property="og:description" content="{desc_m.group(1)}">\n'
        head_add += (f'<meta property="og:type" content="website">\n<meta property="og:url" content="{url}">\n'
                     f'<meta property="og:image" content="{img}">\n<meta property="og:site_name" content="GLPX Studio">\n'
                     f'<meta name="twitter:card" content="summary_large_image">\n')
    if 'rel="icon"' not in html:
        head_add += '<link rel="icon" href="assets/img/favicon.png">\n<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">\n'
    if head_add:
        html = html.replace("</head>", head_add + "</head>", 1)

    # Every booking button opens our own Book a Call page (calendar embedded there)
    html = re.sub(r'href="https://api\.leadconnectorhq\.com/widget/booking/[\w]+" target="_blank" rel="noopener"', 'href="book.html"', html)

    # Cache-bust stylesheets/scripts so phones load fixes right away (bump VERSION after style changes)
    html = re.sub(r'(assets/(?:style|v2|inner)\.css|assets/site\.js)(\?v=[\w.]+)?"', lambda m: m.group(1) + "?v=" + VERSION + '"', html)

    # Lazy-load every photo after the first two on the page (those are above the fold).
    before, sep, after = html.partition("<main>")
    if sep:
        count = 0
        def lazy(m):
            nonlocal count
            count += 1
            tag = m.group(0)
            if count <= 2 or "loading=" in tag:
                return tag
            return tag.replace("<img ", '<img loading="lazy" decoding="async" ', 1)
        after = re.sub(r"<img [^>]*>", lazy, after)
        html = before + sep + after
    html = add_cta_bar(html, name)
    path.write_text(html)


for p in sorted(ROOT.glob("*.html")):
    if p.name not in SKIP:
        finish(p)
print("finished pages")
