"""Homepage concept v2 (editorial / brick + black). Writes index-v2.html."""
import build
from build import header, FOOTER, BOOK, ROOT

FONTS = ("https://fonts.googleapis.com/css2?family=Libre+Caslon+Condensed:ital,wght@0,400;0,700;1,400"
         "&family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&family=Archivo:wdth,wght@125,700&display=swap")

work = [("br-pinkcoat", "Branding", "branding.html"), ("ed-alexrose", "Alex Rose · Music", "editorial.html"),
        ("hs-17", "Headshots", "headshots.html"), ("br-steps", "Branding · On location", "branding.html"),
        ("ed-lily", "Beauty", "editorial.html"), ("br-lagom", "Branding · Med spa", "branding.html"),
        ("hs-yamil", "Headshots", "headshots.html"), ("ed-greensuit", "Music", "editorial.html")]
work_html = "\n".join(
    f'<a href="{h}"><div class="prt"><img src="assets/img/{i}.jpg" alt="{l} photo by GLPX Studio"></div><span class="kicker">{l}</span></a>'
    for i, l, h in work)

services = [
    ("01", "Branding", "br-director", "A planned shoot built around how you sell. Outfits, locations and a shot list for your website, LinkedIn and Instagram, all done in one session.", "Investment · custom quote", "branding.html"),
    ("02", "Headshots", "hs-tesoro", "A clean, current headshot that looks like you on a good day. Guided posing and retouching for actors, professionals and whole teams.", "Investment · custom quote", "headshots.html"),
    ("03", "Editorial &amp; Music", "ed-greensuit", "Album covers, press kits, beauty and fashion stories. Half day and full day productions with as much creative direction as you want.", "Investment · custom quote", "editorial.html"),
    ("04", "Corporate Events", "ev-a04", "Conferences, launches and company parties covered in English and Spanish, with on site team headshots if you need them.", "Investment · custom quote", "corporate-event-photography-orlando.html"),
]
svc_html = "\n".join(f'''    <div class="v2-svc">
      <div class="v2-svc-img"><img src="assets/img/{img}.jpg" alt="{name} photo by GLPX Studio"></div>
      <div class="v2-svc-txt">
        <span class="kicker">Service {n}</span>
        <h3 class="wide">{name}</h3>
        <p>{txt}</p>
        <span class="kicker inv">{inv}</span>
        <div class="actions"><a class="pill pill--act" href="{BOOK}" target="_blank" rel="noopener">Book this service</a><a class="pill" href="{href}">See the work</a></div>
      </div>
    </div>''' for n, name, img, txt, inv, href in services)

marq = " · ".join(["Refuse to be forgettable", "Branding", "Headshots", "Editorial", "Orlando, FL"]) + " · "

body = f'''  <section class="hero hero--photo v2-trio-hero v2-dark-hero">
    <div class="v2-dark-photo" aria-hidden="true"><img src="assets/img/br-steps.jpg" alt=""></div>
    <div class="wrap">
      <div class="hero-copy">
        <p class="kicker">Branding &amp; headshot photography · Orlando, FL</p>
        <h1 class="tall">Refuse to be <em>(forgettable).</em></h1>
        <p class="lede">Portraits for founders, realtors, artists and executives who need their photos to do some of the selling. Studio sessions in Orlando, or on location wherever your work happens.</p>
        <div class="hero-actions">
          <a class="pill pill--act" href="{BOOK}" target="_blank" rel="noopener">Book a free strategy call</a>
          <a class="pill" href="#work">See the work</a>
        </div>
      </div>
    </div>
  </section>

  <div class="v2-credits"><div class="wrap">
    <span><b>8+</b> years behind the camera</span><span><b>200+</b> clients photographed</span>
    <span>Album credits · <b>Alex Rose</b> · <b>Anuel AA</b></span><span>Sessions in <b>English &amp; Español</b></span>
  </div></div>

  <section class="v2-intro">
    <div class="wrap">
      <div class="v2-collage">
        <div class="block"><img src="assets/img/br-bw-woman.jpg" alt=""></div>
        <div class="prt"><img src="assets/img/br-bw-man.jpg" alt="Black and white branding portrait of a man in a white shirt"></div>
        <div class="prt"><img src="assets/img/ed-12.jpg" alt="Beauty portrait with pearl hair accessories on pink"></div>
      </div>
      <div class="v2-intro-copy">
        <p class="kicker" style="color:var(--dust)">GLPX, in short</p>
        <h2 class="tall">I photograph people who refuse to be <em>(forgettable)</em> and want photos that do some of the selling.</h2>
        <p>Founders, realtors, attorneys, artists and executives across Orlando. Studio sessions in Orlando, or on location wherever your work happens. I direct the whole time, so you never have to guess what to do.</p>
        <div><a class="pill" href="about.html">Get to know me</a></div>
      </div>
    </div>
  </section>

  <div class="v2-marquee" aria-hidden="true"><div><span>{marq * 3}</span><span>{marq * 3}</span></div></div>

  <section class="v2-sec" id="work">
    <div class="wrap">
      <h2 class="tall v2-title">(Selected) Work</h2>
      <p class="v2-sub">A few frames from recent branding, headshot and editorial sessions.</p>
      <div class="v2-work">
{work_html}
      </div>
      <div class="v2-work-foot"><a class="pill" href="branding.html">View the full portfolio</a></div>
    </div>
  </section>

  <section class="v2-sec v2-reviews" id="reviews">
    <div class="wrap">
      <h2 class="tall v2-title">(Kind) Words</h2>
      <p class="v2-sub v2-score"><b>5.0</b> <span class="stars">★★★★★</span> from 17 Google reviews</p>
      <div class="v2-rev-grid">
<figure class="v2-rev"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><blockquote>“He took the time to understand my brand, my vision, and the message I wanted to communicate through my photos. He doesn’t just take pictures. He helps bring your brand to life through powerful visual storytelling.”</blockquote><figcaption><b>Johan Fitch</b><span>CutsbyJohan</span></figcaption></figure>
<figure class="v2-rev"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><blockquote>“I needed a branding photo shoot for my real estate business, he offered valuable guidance and secured an excellent studio for us. He is very professional and very attentive to every detail.”</blockquote><figcaption><b>Grace N</b><span>Real estate</span></figcaption></figure>
<figure class="v2-rev"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><blockquote>“GLPX Studio is hands down the best photographer in Orlando. Their eye for detail, lighting, and storytelling is on another level.”</blockquote><figcaption><b>Charlyn Castro-Rojas</b><span>Branding client</span></figcaption></figure>
<figure class="v2-rev"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><blockquote>“From editorial shoots to outdoor concepts and creative direction, their versatility and eye for detail are unmatched.”</blockquote><figcaption><b>Gabriel Bravo</b><span>Creative partner since 2020</span></figcaption></figure>
<figure class="v2-rev"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><blockquote>“My headshots came out so beautiful and I’m so excited to book here again. Gerson was extremely professional and gave clear directions to capture the perfect shots.”</blockquote><figcaption><b>Ashana G</b><span>Headshots</span></figcaption></figure>
<figure class="v2-rev"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><blockquote>“I absolutely love my professional headshots. Gerson was punctual, professional and knows how the get the best shots. I highly recommend!”</blockquote><figcaption><b>Melany Stewart</b><span>Headshots</span></figcaption></figure>
      </div>
      <div class="v2-work-foot"><a class="pill" href="https://www.google.com/search?q=GLPX+Studio+Orlando#lrd=0xae321d709281f5d:0xc845892b9d5b52b4,1,,,," target="_blank" rel="noopener">Read all reviews on Google</a></div>
    </div>
  </section>

  <section class="v2-svc-head">
    <div class="wrap">
      <h2 class="tall v2-title">(Our) Services</h2>
      <p class="v2-sub" style="color:#FFF1EA">Four ways to work together. Every one starts with a free call.</p>
    </div>
  </section>
  <section>
{svc_html}
  </section>

  <section class="v2-sec v2-inv" id="pricing">
    <div class="wrap">
      <h2 class="tall v2-title">(The) Packages</h2>
      <p class="v2-sub">Every shoot is quoted to fit what you need. Here's what each option includes.</p>
      <div class="v2-inv-grid">
        <article><span class="kicker tag">Most popular</span><h3 class="kicker">Starter Branding</h3><ul><li>2-hour shoot · 2 outfits</li><li>10 edited images</li><li>Delivered in 2 weeks</li></ul></article>
        <article><span class="kicker tag">Best value</span><h3 class="kicker">Signature Branding</h3><ul><li>3-hour shoot · 4 outfits</li><li>15 edited images</li><li>Delivered in 3 weeks</li></ul></article>
        <article><span class="kicker tag">Photography only</span><h3 class="kicker">Half Day</h3><ul><li>Up to 5 hours on set</li><li>Up to 3 set changes</li><li>Edits added per image</li></ul></article>
        <article><span class="kicker tag">Max output</span><h3 class="kicker">Full Day</h3><ul><li>Up to 10 hours</li><li>Unlimited locations</li><li>Travel within 1 hour</li></ul></article>
      </div>
      <p class="v2-inv-note">Not sure which fits? <a href="{BOOK}" target="_blank" rel="noopener">Request a quote</a> · Hair &amp; makeup, BTS stills and reels can be added · 50% deposit secures your date</p>
    </div>
  </section>

  <section class="v2-sec">
    <div class="wrap">
      <h2 class="tall v2-title">(The) Process</h2>
      <div class="v2-proc">
        <div class="v2-proc-prints">
          <div class="prt"><img src="assets/img/ab-bts-camera.jpg" alt="Gerson checking a frame on a tethered camera"></div>
          <div class="prt"><img src="assets/img/br-blacksuit.jpg" alt="Branding portrait of a man in a black suit"></div>
        </div>
        <ol class="v2-steps">
          <li><b>01</b><div><h3>Strategy call</h3><p>A free call about where the photos will live and who needs to see them. No brief needed, just tell me what you're working on.</p></div></li>
          <li><b>02</b><div><h3>Plan the shoot</h3><p>Outfits, locations and a shot list. A 50% deposit locks your date.</p></div></li>
          <li><b>03</b><div><h3>Shoot day</h3><p>A studio session in Orlando or on location. I direct the whole time, so you're never guessing.</p></div></li>
          <li><b>04</b><div><h3>Delivery</h3><p>Edited, print ready images in two to three weeks, sized for web and print.</p></div></li>
        </ol>
      </div>
    </div>
  </section>

  <section class="v2-sec v2-vals">
    <img src="assets/img/ab-bts-steps.jpg" alt="">
    <div class="wrap">
      <h2 class="tall v2-title">(The things) I come back to</h2>
      <div class="v2-vals-list">
        <div><h3 class="wide">Plan before we shoot</h3><p>Every frame gets a job before the camera comes out: a banner, a profile, a post.</p></div>
        <div><h3 class="wide">Direct the whole time</h3><p>Most people hate having their photo taken. My job is to make it easy and keep you talking.</p></div>
        <div><h3 class="wide">Look like you</h3><p>Polished, never plastic. People should recognize you when they meet you in person.</p></div>
      </div>
    </div>
  </section>

  <section class="v2-about">
    <div class="wrap">
      <div class="prt"><img src="assets/img/gerson.jpg" alt="Gerson Lopez holding a camera on his shoulder, smiling"></div>
      <div class="v2-about-copy">
        <p class="kicker" style="color:#FFF1EA">Behind the camera</p>
        <h2 class="tall">Hi, I'm (Gerson).</h2>
        <p>More than eight years photographing people, from album covers for Alex Rose and Anuel AA to headshots for realtors on a lunch break. Based in Thornton Park, shooting across Orlando in English or Spanish.</p>
        <div><a class="pill" href="about.html">More about me</a></div>
      </div>
    </div>
  </section>

  <section class="v2-close">
    <img src="assets/img/br-director.jpg" alt="">
    <div class="wrap">
      <p class="kicker">Next step</p>
      <h2 class="tall">Start with a (free) call</h2>
      <p style="color:#E3D7CB;max-width:44ch">Tell me what you're working on and where the photos need to show up. I'll take it from there.</p>
      <a class="pill pill--act" href="{BOOK}" target="_blank" rel="noopener">Book a free strategy call</a>
      <div class="lines"><a href="tel:+14075347581">Call (407) 534-7581</a><a href="sms:+14075347581">Text me</a><a href="mailto:glpxstudio@gmail.com">glpxstudio@gmail.com</a><a href="https://www.instagram.com/glpxstudio/" target="_blank" rel="noopener">@glpxstudio</a></div>
    </div>
  </section>'''

head = header("index.html").replace("assets/img/logo-black.png", "assets/img/logo-cream.png")
html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>GLPX Studio · Orlando Branding &amp; Headshot Photography</title>
<meta name="description" content="Branding, headshot, editorial and corporate event photography in Orlando. Custom quotes for every shoot.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/v2.css">
</head>
<body class="v2">

{head}

<main>
{body}
</main>

{FOOTER}

</body>
</html>
'''
(ROOT / "index.html").write_text(html)
(ROOT / "index-v2.html").write_text(html)
print("v2 built")
