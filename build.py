"""Builds the GLPX Studio static pages from shared header/footer.
Run: python3 build.py   (edit page bodies below, then rebuild)"""
import re, pathlib

ROOT = pathlib.Path(__file__).parent
BOOK = "https://api.leadconnectorhq.com/widget/booking/6PJmFlf8wO5cNephtWVJ"
# Client gallery home (Pixpa client galleries). Change this one line if you move to Pic-Time / Pixieset.
GALLERY = "https://gallery.glpxstudio.com"
FONTS = ("https://fonts.googleapis.com/css2?family=Libre+Caslon+Condensed:ital,wght@0,400;0,700;1,400"
         "&family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&family=Archivo:wdth,wght@125,700&display=swap")
NAV = [("portfolio.html", "Portfolio"), ("branding.html", "Branding"), ("headshots.html", "Headshots"),
       ("editorial.html", "Editorial"), ("about.html", "About"), ("contact.html", "Contact"), ("client-gallery.html", "Client Gallery")]
BOOK_PAGE = "book.html"


def header(current):
    links = "\n".join(
        f'      <a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in [("index.html", "Home")] + NAV)
    menu = "\n".join(f'          <a href="{h}">{t}</a>' for h, t in [("index.html", "Home")] + NAV)
    return f'''<header class="site-head">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="GLPX Studio home"><img src="assets/img/logo-black.png" alt="GLPX Studio"></a>
    <nav class="nav" aria-label="Main">
{links}
      <details class="menu">
        <summary>Menu +</summary>
        <div class="menu-panel">
{menu}
        </div>
      </details>
      <a class="btn btn--red" href="book.html">Book a call</a>
    </nav>
  </div>
</header>'''


FOOTER = f'''<footer class="site-foot">
  <div class="wrap">
    <div><img src="assets/img/logo-cream.png" alt="GLPX Studio"></div>
    <div>
      <h4>Explore</h4>
      <ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h, t in [("index.html", "Home")] + NAV + [("areas.html", "Areas we serve"), ("blog/index.html", "Journal")])}</ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul><li><a href="tel:+14075347581">Call (407) 534-7581</a></li><li><a href="sms:+14075347581">Text (407) 534-7581</a></li><li><a href="mailto:glpxstudio@gmail.com">glpxstudio@gmail.com</a></li><li><a href="https://www.instagram.com/glpxstudio/" target="_blank" rel="noopener">Instagram @glpxstudio</a></li><li>Orlando, FL</li></ul>
    </div>
    <p class="fine">© 2026 GLPX Studio · Branding, headshot &amp; editorial photography in Orlando, FL · <a href="terms-and-conditions/index.html">Terms</a> · <a href="privacy-policy/index.html">Privacy</a></p>
  </div>
</footer>'''


def closer(title_html, sub=""):
    return f'''  <section class="closer">
    <div class="wrap">
      <p class="eyebrow">Next step</p>
      <h2>{title_html}</h2>
      {f"<p class='lede'>{sub}</p>" if sub else ""}
      <div><a class="btn btn--solid" href="{BOOK}" target="_blank" rel="noopener">Book a free strategy call</a></div>
      <div class="contact-lines"><a href="tel:+14075347581">Call (407) 534-7581</a><a href="sms:+14075347581">Text me</a><a href="mailto:glpxstudio@gmail.com">glpxstudio@gmail.com</a><a href="https://www.instagram.com/glpxstudio/" target="_blank" rel="noopener">@glpxstudio</a></div>
    </div>
  </section>'''


def page(fname, title, desc, body, extra_head=""):
    old = fname == "index-v1.html"
    head = header(fname) if old else header(fname).replace("assets/img/logo-black.png", "assets/img/logo-cream.png")
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://www.glpxstudio.com/{'' if fname == 'index.html' else fname}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/style.css">
{"" if old else '<link rel="stylesheet" href="assets/v2.css">' + chr(10) + '<link rel="stylesheet" href="assets/inner.css">'}
{extra_head}</head>
<body{"" if old else ' class="v2 inner"'}>

{head}

<main>
{body}
</main>

{FOOTER}

<script src="assets/site.js" defer></script>
</body>
</html>
'''
    (ROOT / fname).write_text(html)


def frame(img, alt, label, num, href=None, cls="", pick=False):
    tag = "a" if href else "figure"
    href_attr = f' href="{href}"' if href else ""
    note = '<span class="pick-note">The pick</span>' if pick else ""
    svg = ('<svg class="pick" viewBox="0 0 120 120" preserveAspectRatio="none" aria-hidden="true"><path d="M60 4 C 98 2, 118 30, 116 62 C 114 98, 86 118, 56 116 C 22 114, 3 90, 5 58 C 7 26, 30 6, 66 8"/></svg>'
           if pick else "")
    return (f'<{tag} class="frame {cls}"{href_attr}><div class="frame-img"><img src="assets/img/{img}" alt="{alt}">{note}</div>'
            f'{svg}<figcaption><span>{label}</span><b>▸ {num}</b></figcaption></{tag}>')


def sheet(frames, rebate, cls=""):
    return (f'<div class="sheet {cls}">\n' + "\n".join(frames) +
            f'\n<div class="sheet-rebate">{"".join(f"<span>{r}</span>" for r in rebate)}</div>\n</div>')


REVIEW_URL = "https://www.google.com/search?q=GLPX+Studio+Orlando#lrd=0xae321d709281f5d:0xc845892b9d5b52b4,1,,,,"
REVIEWS = {
    "johan": ("He took the time to understand my brand, my vision, and the message I wanted to communicate through my photos. He doesn\u2019t just take pictures. He helps bring your brand to life through powerful visual storytelling.", "Johan Fitch", "CutsbyJohan"),
    "grace": ("I needed a branding photo shoot for my real estate business, he offered valuable guidance and secured an excellent studio for us. He is very professional and very attentive to every detail.", "Grace N", "Real estate"),
    "charlyn": ("GLPX Studio is hands down the best photographer in Orlando. Their eye for detail, lighting, and storytelling is on another level.", "Charlyn Castro-Rojas", "Branding client"),
    "gabriel": ("From editorial shoots to outdoor concepts and creative direction, their versatility and eye for detail are unmatched.", "Gabriel Bravo", "Creative partner since 2020"),
    "ashana": ("My headshots came out so beautiful and I\u2019m so excited to book here again. Gerson was extremely professional and gave clear directions to capture the perfect shots.", "Ashana G", "Headshots"),
    "melany": ("I absolutely love my professional headshots. Gerson was punctual, professional and knows how the get the best shots. I highly recommend!", "Melany Stewart", "Headshots"),
}


def reviews_section(keys, heading="What clients say."):
    cards = "".join(
        f'<figure class="v2-rev"><span class="stars" aria-label="5 out of 5 stars">\u2605\u2605\u2605\u2605\u2605</span>'
        f'<blockquote>\u201c{REVIEWS[k][0]}\u201d</blockquote><figcaption><b>{REVIEWS[k][1]}</b><span>{REVIEWS[k][2]}</span></figcaption></figure>'
        for k in keys)
    return f'''  <section class="section rev-sec">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Google reviews · 5.0 \u2605</p><h2>{heading}</h2></div>
      <div class="v2-rev-grid rev-{len(keys)}">{cards}</div>
      <p class="rev-more"><a href="{REVIEW_URL}" target="_blank" rel="noopener">Read all reviews on Google \u2192</a></p>
    </div>
  </section>
'''


def faq(items):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


# ---------------------------------------------------------------- HOME
home_src = (ROOT / "index-v1.html").read_text()  # old red homepage (backup); live homepage comes from v2.py
home_main = re.search(r"<main>(.*?)</main>", home_src, re.S).group(1).strip("\n")
if "<!-- built -->" not in home_main:
    cat_link = {"Editorial": "editorial.html", "Branding": "branding.html", "Headshots": "headshots.html"}
    def relink(m):
        block = m.group(0)
        lab = re.search(r"<figcaption><span>(\w+)</span>", block).group(1)
        return re.sub(r'href="[^"]*"', f'href="{cat_link[lab]}"', block, count=1)
    home_main = re.sub(r'<a class="frame[^"]*" href="[^"]*">.*?</a>', relink, home_main, flags=re.S)
    for name, href in [("Branding", "branding.html"), ("Headshots", "headshots.html"), ("Editorial &amp; Music", "editorial.html")]:
        home_main = home_main.replace(f"<div><h3>{name}</h3>", f'<div><h3><a href="{href}">{name}</a></h3>')
    home_main = home_main.replace("A free 15-minute call", "A free call")
    home_main = home_main.replace(
        '<div class="hoods">', '<div><a class="btn btn--solid" href="about.html">More about me</a></div>\n        <div class="hoods">', 1)
    home_main = "<!-- built -->\n" + home_main
ld = re.search(r'<script type="application/ld\+json">.*?</script>\n', home_src, re.S)
page("index-v1.html", "GLPX Studio · Orlando Branding &amp; Headshot Photography",
     "Branding, headshot and editorial photography in Orlando. Studio sessions and on-location shoots across Winter Park, Lake Nona, Downtown Orlando and beyond. Custom quotes for every shoot.",
     home_main, ld.group(0) if ld else "")

# ---------------------------------------------------------------- BRANDING
br_frames = [
    frame("br-pinkcoat.jpg", "Smiling woman in a pink coat holding a tablet against a magenta backdrop", "Studio", "02", pick=True),
    frame("br-steps.jpg", "Woman in a black suit walking down downtown steps with a leather tote", "On location", "05"),
    frame("br-bw-woman.jpg", "Black and white portrait of a woman in an oversized blazer and gloves on a stool", "Studio", "08"),
    frame("br-blacksuit.jpg", "Man in a black suit with hands clasped, smiling", "Studio", "11"),
    frame("br-bw-man.jpg", "Black and white portrait of a man in a white shirt leaning on a wall", "Studio", "14"),
    frame("br-street.jpg", "Woman in a black coat walking down a flower-lined street", "On location", "17"),
]
branding = f'''  <section class="page-hero page-hero--red">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Branding photography · Orlando, FL</p>
        <h1>Branding photos <em>with a plan.</em></h1>
        <p class="lede">One planned shoot that covers your website, LinkedIn, Instagram and press kit. We decide the shots before the camera comes out, so every frame has a job.</p>
        <div class="hero-actions">
          <a class="btn btn--solid" href="{BOOK}" target="_blank" rel="noopener">Book a free strategy call</a>
          <a class="btn btn--ghost" href="#packages">See packages</a>
        </div>
      </div>
      <figure class="print">
        <img src="assets/img/br-director.jpg" alt="Smiling woman in a cream suit seated on a director's chair">
        <figcaption><span>Branding · Studio</span><span>Fr. 01</span></figcaption>
      </figure>
    </div>
  </section>

  <div class="credits"><div class="wrap">
    <span>Built for <b>founders</b></span><span><b>Realtors</b> &amp; brokers</span><span><b>Lawyers</b> &amp; consultants</span><span>Coaches &amp; <b>small brands</b></span>
  </div></div>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">What you walk away with</p>
        <h2>Every crop your brand needs, planned in advance.</h2>
        <p>Each platform wants a different shape. We shoot with all of them in mind, so you aren't stuck cropping a vertical portrait into a website banner.</p>
      </div>
      <div class="crops">
        <div class="crop"><div class="crop-box" style="aspect-ratio:4/5"><img src="assets/img/br-director.jpg" alt="" style="object-position:50% 30%"><span>4:5</span></div><h3>Instagram feed</h3><p>Portraits and working shots sized for the grid.</p></div>
        <div class="crop"><div class="crop-box" style="aspect-ratio:9/16"><img src="assets/img/br-director.jpg" alt="" style="object-position:40% 50%"><span>9:16</span></div><h3>Stories &amp; Reels</h3><p>Vertical frames with room for text on top.</p></div>
        <div class="crop"><div class="crop-box" style="aspect-ratio:16/9"><img src="assets/img/br-director.jpg" alt="" style="position:absolute;width:130%;height:auto;max-width:none;left:-24%;top:-16%"><span>16:9</span></div><h3>Website banners</h3><p>Wide shots with open space for your headline.</p></div>
        <div class="crop"><div class="crop-box" style="aspect-ratio:1/1"><img src="assets/img/br-director.jpg" alt="" style="position:absolute;width:300%;height:auto;max-width:none;left:-95%;top:-26%"><span>1:1</span></div><h3>LinkedIn &amp; press</h3><p>A clean headshot for profiles, bios and features.</p></div>
      </div>
      <p class="terms">One frame from a single shoot, cropped four ways.</p>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Branding work</p>
        <h2>In the studio and out where the work happens.</h2>
      </div>
      {sheet(br_frames, ["GLPX STUDIO", "BRANDING", "▸ ORLANDO"], "sheet--3")}
    </div>
  </section>

  <section class="section cream" id="packages">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Packages</p>
        <h2>Shoot, studio and editing in one package.</h2>
      </div>
      <div class="price-row">
        <article class="price">
          <span class="tag">Most popular</span>
          <h3>Starter Branding</h3>
          <ul><li>2-hour shoot</li><li>2 outfits</li><li>10 edited images</li><li>Print-ready high-res files</li><li>Delivered in 2 weeks</li></ul>
        </article>
        <article class="price price--feature">
          <span class="tag">Best value</span>
          <h3>Signature Branding</h3>
          <ul><li>3-hour shoot</li><li>4 outfits</li><li>15 edited images</li><li>Print-ready high-res files</li><li>Delivered in 3 weeks</li></ul>
        </article>
      </div>
      <p class="terms">Every shoot is quoted to fit what you need. <a href="{BOOK}" target="_blank" rel="noopener" style="color:var(--red)">Request a quote</a> · Hair &amp; makeup, BTS stills and reels can be added to any shoot · 50% deposit secures your date</p>
    </div>
  </section>

{reviews_section(["grace", "johan", "charlyn"], "Clients on their branding shoots.")}
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Questions</p><h2>Before you book.</h2></div>
      {faq([
        ("Where do we shoot?", "Either a studio session in Orlando or on location: your office, your listing, a downtown street, wherever your work actually happens. We pick on the strategy call."),
        ("What should I bring?", "One outfit per look in your package: two for Starter, four for Signature. Solid colors photograph best. Bring anything you use in your work, like a laptop, tools or product."),
        ("How fast do I get my photos?", "Starter Branding is delivered in two weeks. Signature Branding is delivered in three weeks. Files come print-ready in high resolution."),
        ("Can I add hair and makeup?", "Yes. Hair, makeup and creative direction can be added to any shoot and are included in your quote."),
        ("How do I lock in a date?", "A 50% deposit secures your date. The balance is due the day of the session."),
      ])}
    </div>
  </section>

{closer("Let's plan your <em>brand</em> shoot.")}'''
page("branding.html", "Branding Photography in Orlando · GLPX Studio",
     "Personal branding photography in Orlando for founders, realtors, lawyers and coaches. Starter and Signature branding packages, quoted to fit your shoot. Studio and on-location.", branding)

# ---------------------------------------------------------------- HEADSHOTS
hs_frames = [
    frame("hs-01.jpg", "Man in glasses, navy suit and striped tie", "Grey", "01"),
    frame("hs-17.jpg", "Smiling woman in a polka dot blouse", "Lavender grey", "04"),
    frame("hs-03.jpg", "Woman in a lavender dress with arms crossed", "Light grey", "07", pick=True),
    frame("hs-yamil.jpg", "Young man in a light grey sweater with arms crossed", "Grey", "10"),
    frame("hs-18.jpg", "Smiling woman in a blue cardigan with arms crossed", "Lavender grey", "13"),
    frame("hs-green.jpg", "Smiling woman in a green blazer, headshot from the SHRM conference activation", "Lavender grey", "16"),
    frame("hs-redtop.jpg", "Smiling woman with long curly hair in a red blouse", "Lavender grey", "19"),
    frame("hs-16.jpg", "Young man in a navy blazer and white shirt", "Grey", "22"),
    frame("hs-19.jpg", "Smiling woman in glasses and an orange striped blouse", "Lavender grey", "25"),
    frame("hs-navytop.jpg", "Woman in a navy top with a white beaded necklace", "Grey", "28"),
    frame("hs-10.jpg", "Barber in a white branded polo", "Grey", "31"),
    frame("br-curlyman.jpg", "Man with curly hair in a grey tee against a grey backdrop", "Grey", "34"),
]
headshots = f'''  <section class="page-hero page-hero--ink">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Headshot photography · Orlando, FL</p>
        <h1>Headshots that look like you <em>on a good day.</em></h1>
        <p class="lede">For actors, lawyers, doctors, realtors, executives and whole teams. I coach you through every frame, so you don't need to know how to pose.</p>
        <div class="hero-actions">
          <a class="btn btn--red" href="{BOOK}" target="_blank" rel="noopener">Book your headshot</a>
          <a class="btn btn--ghost" href="#gallery">See headshots</a>
        </div>
      </div>
      <figure class="print">
        <img src="assets/img/hs-tesoro.jpg" alt="Attorney headshot in a black blazer on a charcoal backdrop" style="object-position:50% 30%">
        <figcaption><span>Headshot · Tesoro Law</span><span>Fr. 01</span></figcaption>
      </figure>
    </div>
  </section>

  <section class="section dark" id="gallery">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Recent headshots</p>
        <h2>Same light. Different people. Nobody looks stiff.</h2>
      </div>
      {sheet(hs_frames, ["GLPX STUDIO", "HEADSHOTS", "▸ ORLANDO"], "sheet--3")}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">How a headshot session runs</p><h2>Quick, guided and done.</h2></div>
      <div class="steps">
        <div class="step"><h3>Pick a backdrop</h3><p>Grey, charcoal, blue-grey or white, matched to your industry and your website.</p></div>
        <div class="step"><h3>Light for your face</h3><p>The lighting is adjusted for you, including glasses, skin tone and the angle that works best.</p></div>
        <div class="step"><h3>Coaching</h3><p>I talk you through posture and expression until we get the version people recognize.</p></div>
        <div class="step"><h3>Retouching</h3><p>Your favorite frames are retouched to look polished and still like you.</p></div>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap split">
      <div>
        <p class="eyebrow">For actors</p>
        <h2>Headshots casting directors can use.</h2>
        <p>Your headshot has one job: look exactly like the person who walks into the audition. I keep the light clean, the retouching natural and the focus on your eyes, so you get images that work for casting sites, agents and your website.</p>
        <p>We can shoot a commercial look and a theatrical look in the same session, and change backdrops and wardrobe to show your range.</p>
        <div><a class="btn btn--red" href="{BOOK}" target="_blank" rel="noopener">Book an actor headshot session</a></div>
      </div>
      <div>
        <ul class="ticks">
          <li><span>Commercial look</span><span>Warm · approachable</span></li>
          <li><span>Theatrical look</span><span>Moody · dramatic</span></li>
          <li><span>Retouching</span><span>Natural, true to you</span></li>
          <li><span>Framing</span><span>Ready for casting sites</span></li>
          <li><span>Sessions</span><span>English &amp; Español</span></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap split">
      <div>
        <p class="eyebrow">What to wear</p>
        <h2>Simple wins.</h2>
        <ul class="ticks">
          <li><span>Solid colors over busy patterns</span><span>Yes</span></li>
          <li><span>A jacket or blazer that fits</span><span>Yes</span></li>
          <li><span>A second top for variety</span><span>Bring it</span></li>
          <li><span>Logos and loud prints</span><span>Skip</span></li>
          <li><span>Hair and makeup</span><span>Add-on</span></li>
        </ul>
      </div>
      <div>
        <p class="eyebrow">Pricing</p>
        <h2>Ask for a quote.</h2>
        <p>Headshot pricing depends on how many people and looks you need. Tell me on a quick call and I'll send a quote within 24 hours. Need more than a headshot? Starter Branding includes ten edited images across two outfits.</p>
        <p>Teams and offices are welcome. Ask about group sessions.</p>
        <div><a class="btn btn--red" href="{BOOK}" target="_blank" rel="noopener">Get a quote</a></div>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap cs-bts">
      <img src="assets/img/ab-bts-light.jpg" alt="Gerson adjusting a large softbox before a headshot session">
      <div>
        <p class="eyebrow" style="color: var(--red)">Behind the scenes</p>
        <h3>One big light and a lot of talking.</h3>
        <p>The setup stays simple so the time goes to you. Most of the work is getting you out of your stiff camera face and into the one your clients actually know.</p>
      </div>
    </div>
  </section>

{reviews_section(["ashana", "melany"], "Clients on their headshots.")}
{closer("Retire the <em>cropped</em> vacation photo.")}'''
page("headshots.html", "Headshot Photography in Orlando · GLPX Studio",
     "Professional headshots in Orlando for actors, lawyers, doctors, realtors, executives and teams. Guided studio sessions with coaching and retouching.", headshots)

# ---------------------------------------------------------------- EDITORIAL
ed_frames = [
    frame("ed-01.jpg", "Beauty portrait with silver face jewels and a reflective surface", "Beauty", "01"),
    frame("ed-greensuit.jpg", "Artist in a green double-breasted suit leaning on a wood-paneled wall", "Music", "04"),
    frame("ed-08.jpg", "Artist in sunglasses posing in front of a wall of speakers", "Music", "07"),
    frame("ed-12.jpg", "Beauty portrait with pearl hair accessories on pink", "Beauty", "10", pick=True),
    frame("ed-hero.jpg", "Woman holding red roses against a deep red backdrop", "Beauty", "13"),
    frame("ed-navy.jpg", "Platinum blonde model in a navy jacket and long leather gloves", "Fashion", "16"),
    frame("ed-09.jpg", "Artist in sunglasses and a gold chain against grey", "Music", "19"),
    frame("ed-11.jpg", "Glam beauty portrait with soft curls on a warm backdrop", "Beauty", "22"),
    frame("ed-erica.jpg", "Model in a black gown reclining on a white studio floor", "Fashion", "25", cls="frame--wide"),
    frame("ed-10.jpg", "Artist in a yellow tee and green cap against a green backdrop", "Music", "28"),
    frame("ed-18.jpg", "Model in a black tank top with hand at his face", "Fashion", "31"),
    frame("ed-05.jpg", "Man in a plaid jacket and orange beanie seated on the floor", "Editorial", "34"),
    frame("ed-19.jpg", "Model on a stool with hands on her head against a concrete wall", "Editorial", "37"),
    frame("ed-07.jpg", "Model in an oversized sage suit against a purple gradient", "Fashion", "40"),
    frame("ed-15.jpg", "Woman in boxing gloves seated on a dark ring floor", "Editorial", "43"),
]
editorial = f'''  <section class="page-hero page-hero--black">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Editorial · Music · Beauty</p>
        <h1>Covers, campaigns and <em>the shots in between.</em></h1>
        <p class="lede">Album art, press kits, beauty and fashion stories. Half-day and full-day productions with as much creative direction as you want.</p>
        <div class="hero-actions">
          <a class="btn btn--red" href="{BOOK}" target="_blank" rel="noopener">Plan a production</a>
          <a class="btn btn--ghost" href="#rates">Session rates</a>
        </div>
      </div>
      <figure class="print">
        <img src="assets/img/ed-alexrose.jpg" alt="Alex Rose in a red sherpa jacket and beret against black">
        <figcaption><span>Alex Rose · Music</span><span>Fr. 01</span></figcaption>
      </figure>
    </div>
  </section>

  <div class="credits"><div class="wrap">
    <span>Album credits · <b>Alex Rose</b></span><span>Album credits · <b>Anuel AA</b></span><span><b>8+</b> years on set</span><span>Sets in English &amp; Español</span>
  </div></div>

  <section class="section dark">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Editorial work</p>
        <h2>Color, attitude and a reason for every frame.</h2>
      </div>
      {sheet(ed_frames, ["GLPX STUDIO", "EDITORIAL", "▸ ORLANDO"])}
    </div>
  </section>

  <section class="section cream" id="rates">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Session rates</p>
        <h2>Book the time. Choose your edits.</h2>
        <p>Session rates cover photography only. Edits are added per image, so you only pay to retouch the frames you'll use. Every session is quoted after a free call.</p>
      </div>
      <div class="price-row">
        <article class="price">
          <h3>Half Day</h3>
          <ul><li>Up to 5 hours on set</li><li>Up to 3 set or location changes</li><li>Branding, editorial, personal shoots</li></ul>
        </article>
        <article class="price price--feature">
          <span class="tag">Max output</span>
          <h3>Full Day</h3>
          <ul><li>Up to 10 hours</li><li>Unlimited location changes</li><li>Travel within 1 hour of Orlando included</li><li>Campaigns, album covers, full productions</li></ul>
        </article>
      </div>
      <div class="price-group" style="margin-top:56px">
        <p class="eyebrow">Build out the production</p>
        <div class="addons">
          <div><span>Creative direction</span><b>Add-on</b></div>
          <div><span>Makeup artist</span><b>Add-on</b></div>
          <div><span>Hair stylist</span><b>Add-on</b></div>
          <div><span>Hair &amp; makeup</span><b>Add-on</b></div>
          <div><span>BTS stills · 10 photos</span><b>Add-on</b></div>
          <div><span>Reel · 30–60 sec</span><b>Add-on</b></div>
          <div><span>Content bundle · 2 reels + 15 BTS</span><b>Add-on</b></div>
          <div><span>Full-day content creation</span><b>Quote</b></div>
        </div>
        <p class="terms">50% deposit secures your date · balance due the day of the session</p>
      </div>
    </div>
  </section>

{reviews_section(["gabriel", "charlyn"], "Creatives on working with GLPX.")}
{closer("Got a release <em>coming up?</em>", "Send the date and the mood. We'll build the shoot around it.")}'''
page("editorial.html", "Editorial &amp; Music Photography in Orlando · GLPX Studio",
     "Album covers, artist portraits, beauty and fashion editorials in Orlando. Half day and full day productions. Album credits with Alex Rose and Anuel AA.", editorial)

# ---------------------------------------------------------------- ABOUT
about = f'''  <section class="page-hero page-hero--cream">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">About GLPX Studio</p>
        <h1>Hi, I'm <em>Gerson.</em></h1>
        <p class="lede">Photographer and owner of GLPX Studio. I make branding, headshot and editorial photos for people who need to be remembered.</p>
      </div>
      <figure class="print">
        <img src="assets/img/gerson.jpg" alt="Gerson Lopez holding a camera on his shoulder, smiling">
        <figcaption><span>Gerson Lopez</span><span>Owner · Photographer</span></figcaption>
      </figure>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div>
        <p class="eyebrow">The short version</p>
        <h2>Eight years of putting people at ease in front of a lens.</h2>
      </div>
      <div>
        <p>I've been photographing people for more than eight years. That includes album covers for artists like Alex Rose and Anuel AA, as well as headshots for realtors squeezing a session into their lunch break.</p>
        <p>Most people tell me they hate having their picture taken. That's the part I enjoy. I direct the whole session, from where to stand to what to do with your hands, so you can stop thinking about the camera and just show up as yourself.</p>
        <p>I'm based in Thornton Park and shoot studio sessions in Orlando and on location across the city. Sessions run in English or Spanish.</p>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">On set</p><h2>What a GLPX shoot looks like from the other side.</h2></div>
      <div class="bts-row" style="grid-template-columns: 1.4fr 1fr">
        <img src="assets/img/ab-bts-steps.jpg" alt="Gerson photographing a client on downtown Orlando steps with an umbrella light">
        <img src="assets/img/ab-bts-camera.jpg" alt="Black and white photo of Gerson checking a shot on a tethered camera">
      </div>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap">
      <div class="stats">
        <div><b>8+</b><span>Years behind the camera</span></div>
        <div><b>200+</b><span>Clients photographed</span></div>
        <div><b>2</b><span>Languages on set · English &amp; Español</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">How I work</p><h2>Three things you can count on.</h2></div>
      <div class="steps" style="grid-template-columns: repeat(auto-fit, minmax(220px, 1fr))">
        <div class="step"><h3>A plan before the shoot</h3><p>We agree on the shot list, outfits and locations on a call, so shoot day is about you.</p></div>
        <div class="step"><h3>Direction the whole time</h3><p>You never have to guess what to do. I'll tell you, and show you as we go.</p></div>
        <div class="step"><h3>Photos you'll actually use</h3><p>Every image is planned for a real place: your site, your profile, your next post.</p></div>
      </div>
      <div class="hoods" style="margin-top:48px">
        <span>Thornton Park</span><span>Downtown Orlando</span><span>Lake Eola</span><span>Winter Park</span><span>Baldwin Park</span><span>Lake Nona</span><span>Dr. Phillips</span><span>Windermere</span>
      </div>
    </div>
  </section>

{closer("Let's make <em>something</em> together.")}'''
page("about.html", "About Gerson Lopez · GLPX Studio",
     "Gerson Lopez is an Orlando photographer with 8+ years behind the camera and album credits with Alex Rose and Anuel AA. Branding, headshots and editorial in English and Spanish.", about)

# ---------------------------------------------------------------- CONTACT
contact = f'''  <section class="page-hero page-hero--red">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Contact · Orlando, FL</p>
        <h1>Let's plan <em>your shoot.</em></h1>
        <p class="lede">The fastest way to start is a free strategy call. Pick a time that works and we'll talk through what you need.</p>
        <div class="hero-actions"><a class="btn btn--solid" href="{BOOK}" target="_blank" rel="noopener">Book a free strategy call</a></div>
        <dl class="contact-card">
          <div><dt>Call</dt><dd><a href="tel:+14075347581">(407) 534-7581</a></dd></div>
          <div><dt>Text</dt><dd><a href="sms:+14075347581">Send a text</a></dd></div>
          <div><dt>Email</dt><dd><a href="mailto:glpxstudio@gmail.com">glpxstudio@gmail.com</a></dd></div>
          <div><dt>Instagram</dt><dd><a href="https://www.instagram.com/glpxstudio/" target="_blank" rel="noopener">@glpxstudio</a></dd></div>
          <div><dt>Based in</dt><dd>Thornton Park, Orlando</dd></div>
        </dl>
      </div>
      <figure class="print">
        <img src="assets/img/ct-joy.jpg" alt="Smiling woman in a plum dress with arms open against a pink backdrop">
        <figcaption><span>Branding · Studio</span><span>Orlando</span></figcaption>
      </figure>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Before the call</p>
        <h2>Four things to think about.</h2>
        <p>None of these need perfect answers. They just help us get to a plan faster.</p>
      </div>
      <ol class="prep">
        <li><span>Where will the photos be used? Website, LinkedIn, Instagram, an album, a press kit?</span></li>
        <li><span>Is there a deadline, like a launch, a listing or a release date?</span></li>
        <li><span>Is it just you, or a team or group?</span></li>
        <li><span>Studio, on location, or both?</span></li>
      </ol>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Quick answers</p><h2>Booking details.</h2></div>
      {faq([
        ("How do I secure a date?", "A 50% deposit secures your date. The balance is due the day of the session."),
        ("Where are sessions held?", "Studio sessions take place in Orlando. On-location shoots can happen anywhere in the city, including Downtown, Winter Park, Lake Nona, Baldwin Park, Dr. Phillips and Windermere. Full Day sessions include travel within one hour."),
        ("¿Hablas español?", "Sí. Las sesiones pueden ser en español o en inglés."),
        ("What does it cost?", "Every shoot is quoted to fit what you need: how many people, looks, locations and images. Book a free strategy call and I'll send a quote within 24 hours."),
      ])}
    </div>
  </section>'''
page("contact.html", "Contact &amp; Booking · GLPX Studio",
     "Book a free strategy call with GLPX Studio in Orlando. Phone (407) 534-7581, email glpxstudio@gmail.com, Instagram @glpxstudio.", contact)

# ---------------------------------------------------------------- CLIENT GALLERY
gallery = f'''  <section class="page-hero page-hero--ink">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Client gallery</p>
        <h1>Your photos <em>are ready.</em></h1>
        <p class="lede">Every client gets a private, password protected gallery. Use the link and password from your "photos are ready" email or text to view, favorite and download your images.</p>
        <div class="hero-actions">
          <a class="btn btn--red" href="{GALLERY}" target="_blank" rel="noopener">Open client galleries</a>
          <a class="btn btn--ghost" href="contact.html">Need help?</a>
        </div>
      </div>
      <figure class="print">
        <img src="assets/img/ab-bts-camera.jpg" alt="Gerson reviewing a frame on a tethered camera">
        <figcaption><span>Behind the scenes</span><span>Fr. 01</span></figcaption>
      </figure>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">How your gallery works</p><h2>Three steps.</h2></div>
      <div class="steps" style="grid-template-columns: repeat(auto-fit, minmax(220px, 1fr))">
        <div class="step"><h3>Open your link</h3><p>Use the private link and password I sent you. It works on your phone or computer.</p></div>
        <div class="step"><h3>Heart your favorites</h3><p>Tap the heart on the images you love so I know which ones matter most to you.</p></div>
        <div class="step"><h3>Download &amp; share</h3><p>Download web and print sizes. Tag <a href="https://www.instagram.com/glpxstudio/" target="_blank" rel="noopener">@glpxstudio</a> when you post.</p></div>
      </div>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Questions</p><h2>Gallery help.</h2></div>
      {faq([
        ("I can't find my link or password.", "Check your email and texts for a message from GLPX Studio titled \u201cYour photos are ready.\u201d Still nothing? Call or text <a href='tel:+14075347581'>(407) 534-7581</a> and I'll resend it."),
        ("Can I get more edited images?", "Yes. Heart the extra images you want in your gallery and send me a message. I'll send a quote for the additional edits."),
        ("Can I order prints?", "Yes. Message me with the images you want and the sizes, and I'll send options."),
      ])}
    </div>
  </section>

{closer("Loved your <em>photos?</em>", "A quick Google review helps other people find GLPX Studio.")}'''
page("client-gallery.html", "Client Gallery · GLPX Studio", "Private client photo galleries for GLPX Studio clients.", gallery, '<meta name="robots" content="noindex">\n')

print("built")
