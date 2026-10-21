"""Model casting page: models apply for GLPX test shoots (TFP). HighLevel form embedded.
Lives at /model-casting/ (no .html). Runs from areas.py after finish.py; also runs on its own: `python3 model.py`."""
import sys, re, pathlib

ROOT = pathlib.Path(__file__).parent
FORM_ID = "ZHLlLE5eO3pSZCRm0jCM"
FORM_URL = f"https://api.leadconnectorhq.com/widget/form/{FORM_ID}"
SLUG = "model-casting"
URL = f"https://www.glpxstudio.com/{SLUG}/"
TITLE = "Model Casting · Test Shoots in Orlando · GLPX Studio"
DESC = ("Models in Orlando: apply for GLPX Studio test shoots. Trade (TFP) sessions for beauty, editorial, "
        "fashion and commercial looks. Apply once in English or Spanish.")

STYLE = '''<style>
.mc-strip { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px; margin-top: clamp(24px, 4vw, 40px); }
.mc-strip img { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; display: block; }
.mc-es { opacity: .78; font-style: italic; }
.form-wrap { background: #fff; border: 1px solid #D8CCBF; padding: 8px; }
.form-wrap iframe { width: 100%; min-height: 2300px; border: 0; display: block; }
.mc-steps { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: clamp(20px, 3vw, 40px); }
.mc-steps h3 { margin: .2em 0 .4em; }
.mc-steps .num { font: 400 2.4rem/1 var(--tall); color: var(--act); }
@media (max-width: 760px) {
  .mc-strip { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .mc-steps { grid-template-columns: 1fr; text-align: center; }
  .form-wrap iframe { min-height: 2700px; }
}
</style>
'''

strip = "\n".join(
    f'          <img src="assets/img/{img}.jpg" alt="{alt}" loading="lazy">'
    for img, alt in [
        ("ed-lily", "Beauty portrait from a GLPX Studio test shoot"),
        ("ed-greensuit", "Editorial fashion portrait in a green suit"),
        ("ed-erica", "Editorial portrait by GLPX Studio"),
        ("ed-navy", "Studio fashion portrait in navy"),
    ])

body = f'''  <section class="page-hero post-hero">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Model casting · Orlando</p>
        <h1>Shoot with <em>GLPX.</em></h1>
        <p class="lede">Monthly test shoots for models who want images that actually book work. Clean, high-glamour, skin you can see. Apply once and we'll reach out when a month's concept fits you.</p>
        <p class="lede mc-es">Sesiones de prueba cada mes para modelos que quieren fotos que consiguen trabajo. Aplica una vez y te escribimos cuando el concepto del mes sea para ti.</p>
        <div class="hero-actions"><a class="btn btn--red" href="#apply">Apply now · Aplica</a><a class="btn btn--ghost" href="editorial.html">See the work</a></div>
      </div>
      <div class="mc-strip">
{strip}
      </div>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">How it works</p><h2>Three steps. No guesswork.</h2></div>
      <div class="mc-steps">
        <div><span class="num">01</span><h3>Apply</h3><p>Fill out the form with three recent photos. Phone photos are fine.</p></div>
        <div><span class="num">02</span><h3>Get matched</h3><p>Every month there's a new concept. When it fits your look, you get a text or email with the date, the look and the Orlando studio or location.</p></div>
        <div><span class="num">03</span><h3>Shoot</h3><p>Show up ready. Usage and hair and makeup details are confirmed before every shoot. You leave with edited images for your book.</p></div>
      </div>
    </div>
  </section>

  <section class="section" id="apply">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Apply · Aplica</p><h2>Join the casting list.</h2><p>Takes about three minutes. 18+ only.</p></div>
      <div class="form-wrap">
        <iframe src="{FORM_URL}" id="inline-{FORM_ID}" data-layout="{{'id':'INLINE'}}" data-trigger-type="alwaysShow" data-trigger-value="" data-activation-type="alwaysActivated" data-activation-value="" data-deactivation-type="neverDeactivate" data-deactivation-value="" data-form-name="Model Test Shoot Application" data-layout-iframe-id="inline-{FORM_ID}" data-form-id="{FORM_ID}" title="Model Test Shoot Application"></iframe>
        <p class="cal-fallback">Form not loading? <a href="{FORM_URL}" target="_blank" rel="noopener noreferrer">Open it in a new tab</a> or DM <a href="https://www.instagram.com/glpxstudio/" target="_blank" rel="noopener">@glpxstudio</a>.</p>
      </div>
      <script src="https://link.msgsend.com/js/form_embed.js" defer></script>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Before you apply</p><h2>Quick answers.</h2></div>
      <div class="faq"><details><summary>How often are the test shoots?</summary><p>Once a month. Your application stays on file, so you can be picked for any month's concept without applying again.</p></details><details><summary>Is it paid?</summary><p>Test shoots are a trade (TFP). No payment either way, and you receive edited images to use in your portfolio.</p></details><details><summary>Do I need experience?</summary><p>No. New faces, working models and agency-signed talent are all welcome. Tell us where you are on the form.</p></details><details><summary>Is hair and makeup provided?</summary><p>It depends on the shoot. You'll know before you confirm, along with the look and the location.</p></details><details><summary>Where are the shoots?</summary><p>In an Orlando studio or on location around the city, depending on the concept.</p></details><details><summary>¿Puedo aplicar en español?</summary><p>Sí. Todo el proceso puede ser en español. Elige tu idioma en el formulario.</p></details><details><summary>How old do I have to be?</summary><p>18 or older. No exceptions.</p></details></div>
    </div>
  </section>'''


def build():
    """Render into model-casting/index.html (clean URL, no .html), using booked.html as the shell
    so it carries the same header, footer and finish.py head tags. Run after finish.py."""
    shell = (ROOT / "booked.html").read_text()
    html = re.sub(r"<main>.*?</main>", lambda m: f"<main>\n{body}\n</main>", shell, flags=re.S)
    html = html.replace('<meta name="robots" content="noindex">\n', "")
    html = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", html)
    html = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*"', rf'\g<1>{DESC}"', html)
    html = re.sub(r'(<meta property="og:title" content=")[^"]*"', rf'\g<1>{TITLE}"', html)
    html = html.replace("https://www.glpxstudio.com/booked.html", URL)
    html = html.replace("</head>", STYLE + "</head>", 1)
    # page lives one folder down: point relative links and assets up a level
    html = re.sub(r'((?:href|src)=")(?!https?:|//|/|#|mailto:|tel:|sms:|\.\./|data:)', r"\g<1>../", html)
    out = ROOT / SLUG
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(html)
    sm_path = ROOT / "sitemap.xml"
    sm = sm_path.read_text().replace(f"  <url><loc>https://www.glpxstudio.com/{SLUG}.html</loc></url>\n", "")
    if URL not in sm:
        sm = sm.replace("</urlset>", f"  <url><loc>{URL}</loc></url>\n</urlset>")
    sm_path.write_text(sm)


build()
print("model casting page built")
