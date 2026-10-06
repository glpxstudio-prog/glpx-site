"""Local service pages: one page per area x service, plus areas.html hub and sitemap.
Run:  python3 areas.py      (this also re-runs build.py first)"""
import re, pathlib
import build
from build import page, frame, sheet, faq, closer, reviews_section, BOOK, ROOT
from area_extra import EXTRA

SITE = "https://www.glpxstudio.com/"

# ------------------------------------------------------------------ AREAS
AREAS = [
    dict(slug="orlando", name="Orlando", kind="city",
         intro="Orlando is home base. Most sessions happen in a rented studio in the city or on location within a short drive, from the downtown towers to the brick streets around Lake Eola.",
         spots=[("Lake Eola Park", "The fountain, the skyline and the walking loop give you three looks in one lap."),
                ("Church Street", "Brick, old rail lines and warm storefronts for a city feel."),
                ("Mills 50", "Murals and color on almost every block, great for bold personal brands.")],
         who="founders, realtors, attorneys, artists and teams across the city",
         venue="Orlando hosts conferences of every size, from hotel ballrooms to the Orange County Convention Center."),
    dict(slug="downtown-orlando", name="Downtown Orlando", kind="neighborhood",
         intro="Downtown is where a lot of Orlando's offices, law firms and startups live. The mix of glass towers, brick and greenery makes it easy to shoot polished and personal in the same hour.",
         spots=[("Orange Avenue towers", "Clean glass and steel lines for corporate and legal clients."),
                ("Dr. Phillips Center plaza", "Open, modern architecture with great light late in the day."),
                ("Church Street", "Brick and character when you want something warmer.")],
         who="attorneys, finance pros, startup founders and downtown office teams",
         venue="Downtown has hotel ballrooms, rooftop venues and the Dr. Phillips Center for company events."),
    dict(slug="winter-park", name="Winter Park", kind="neighborhood",
         intro="Winter Park feels made for photos. Brick streets, big oaks and storefronts that have been there for decades give branding shoots an easy, upscale look.",
         spots=[("Park Avenue", "Boutiques, brick and shade for walking and working shots."),
                ("Central Park", "Open lawns and the rose garden for softer, natural light portraits."),
                ("Rollins College area", "Mediterranean style architecture with arches and texture.")],
         who="boutique owners, realtors, wellness pros and consultants",
         venue="Winter Park has boutique hotels like The Alfond Inn plus private event spaces off Park Avenue."),
    dict(slug="lake-nona", name="Lake Nona", kind="neighborhood",
         intro="Lake Nona is Orlando's medical and innovation hub. Clients here usually need sharp, modern images that match a clinic, a research lab or a growing startup.",
         spots=[("Lake Nona Town Center", "Modern architecture and public art for clean, current portraits."),
                ("Medical City", "Contemporary campus buildings that fit doctors and healthcare teams."),
                ("Lakefront paths", "Open water and sky for a calmer, natural backdrop.")],
         who="doctors, researchers, healthcare teams and tech founders",
         venue="Lake Nona has modern hotels and conference space, including the Lake Nona Wave Hotel."),
    dict(slug="baldwin-park", name="Baldwin Park", kind="neighborhood",
         intro="Baldwin Park mixes a walkable village center with lakefront parks. It works well for relaxed, approachable branding that still looks put together.",
         spots=[("Lake Baldwin", "Water, trees and open sky for natural light portraits."),
                ("Baldwin Park Village Center", "Shops and sidewalks along New Broad Street for lifestyle shots."),
                ("Tree lined residential streets", "Calm, clean backgrounds for coaches and realtors.")],
         who="realtors, coaches, wellness pros and local business owners",
         venue="Baldwin Park has community spaces and restaurants that host smaller company gatherings."),
    dict(slug="dr-phillips", name="Dr. Phillips", kind="neighborhood",
         intro="Dr. Phillips is known for Restaurant Row and its upscale neighborhoods. Restaurant owners, hospitality brands and executives here need images that look as good as the places they run.",
         spots=[("Restaurant Row on Sand Lake Road", "Dining rooms, bars and patios for hospitality branding."),
                ("Dr. Phillips Community Park", "Trees and open space for outdoor portraits."),
                ("Office parks along Sand Lake", "Clean exteriors for corporate headshots and team photos.")],
         who="restaurant owners, hospitality teams, executives and realtors",
         venue="The Dr. Phillips and Sand Lake area is close to many of Orlando's resort hotels and event spaces."),
    dict(slug="windermere", name="Windermere", kind="neighborhood",
         intro="Windermere sits on the Butler Chain of Lakes and is known for its luxury homes. It is a natural fit for high end realtors, executives and anyone whose brand needs to feel elevated.",
         spots=[("Butler Chain of Lakes", "Waterfront light and docks for relaxed luxury portraits."),
                ("Historic downtown Windermere", "Small town charm around Main Street and the town hall."),
                ("Client homes and listings", "Your own space, styled and shot as part of your brand.")],
         who="luxury realtors, executives, private practices and coaches",
         venue="Windermere events are often hosted at private estates, clubs and nearby resort venues."),
    dict(slug="thornton-park", name="Thornton Park", kind="neighborhood",
         intro="Thornton Park is where I'm based. Brick streets, an oak canopy and sidewalk cafes a few steps from Lake Eola make it one of my favorite places to shoot.",
         spots=[("Brick streets under the oaks", "Soft, shaded light most of the day."),
                ("Washington and Summerlin cafes", "Lifestyle shots with a local, lived in feel."),
                ("Lake Eola, a short walk away", "Add a skyline or fountain look without moving the car.")],
         who="creatives, small business owners, coaches and downtown professionals",
         venue="Thornton Park and the nearby downtown area have restaurants and lofts for smaller company events."),
    dict(slug="lake-eola", name="Lake Eola", kind="neighborhood",
         intro="Lake Eola Park is the most recognizable backdrop in Orlando. The fountain, the swan boats and the skyline say Orlando in one frame.",
         spots=[("The fountain", "The classic Orlando shot, best early morning or at golden hour."),
                ("Walt Disney Amphitheater", "Architecture and open space for full length portraits."),
                ("The lakeside loop", "Trees, water and skyline in every direction.")],
         who="founders, realtors, artists and anyone who wants Orlando in the frame",
         venue="The Lake Eola area is surrounded by downtown hotels and venues for company events."),
    dict(slug="kissimmee", name="Kissimmee", kind="city",
         intro="Kissimmee has a big tourism and hospitality economy and one of the area's largest Spanish speaking communities. Sessions run in English or Spanish, whatever you are more comfortable with.",
         spots=[("Lakefront Park", "Lake Toho at sunrise or sunset for warm, open portraits."),
                ("Historic downtown Broadway", "Older storefronts and character for local business branding."),
                ("Your business", "Restaurants, shops and offices shot where your customers meet you.")],
         who="hospitality brands, Latino entrepreneurs, realtors and local shops",
         venue="Kissimmee has large resort and convention venues, including Gaylord Palms."),
    dict(slug="winter-garden", name="Winter Garden", kind="city",
         intro="Winter Garden's historic downtown on Plant Street is full of independent shops, cafes and breweries. It is ideal for small business owners who want photos that feel local and real.",
         spots=[("Plant Street", "Historic storefronts and brick for a small town look."),
                ("West Orange Trail", "Green, shaded paths for natural light portraits."),
                ("The downtown pavilion", "Open structure and good shade on bright days.")],
         who="boutique and cafe owners, realtors, makers and coaches",
         venue="Winter Garden has event halls, breweries and restaurants that host company gatherings."),
    dict(slug="altamonte-springs", name="Altamonte Springs", kind="city",
         intro="Altamonte Springs is a business hub just north of Orlando with medical offices, corporate campuses and a lakeside park at its center.",
         spots=[("Cranes Roost Park", "The lake, the boardwalk and fountains for bright outdoor portraits."),
                ("Uptown Altamonte", "Modern buildings and walkways for corporate looks."),
                ("Your office", "Team headshots and working shots on site.")],
         who="medical practices, corporate teams, insurance and finance pros",
         venue="Altamonte Springs has hotel conference rooms and event space around Uptown and Cranes Roost."),
    dict(slug="lake-mary", name="Lake Mary", kind="city",
         intro="Lake Mary is home to many corporate offices along the I-4 corridor. Most clients here need consistent team headshots and professional branding for a company website.",
         spots=[("Colonial TownPark", "Polished storefronts and plazas for business portraits."),
                ("Corporate campuses", "Clean, modern exteriors and lobbies for team photos."),
                ("Lake Mary's parks and lakes", "Calm, natural backdrops for a softer look.")],
         who="corporate teams, HR and marketing departments, consultants and executives",
         venue="Lake Mary has corporate campuses, hotels and the Lake Mary Events Center for company events."),
    dict(slug="sanford", name="Sanford", kind="city",
         intro="Sanford's historic downtown and riverwalk on Lake Monroe give it real character. It is a great fit for makers, restaurants and creative brands.",
         spots=[("Historic First Street", "Brick, old storefronts and murals."),
                ("Sanford Riverwalk", "Lake Monroe views and wide open light."),
                ("Breweries and local shops", "Working shots inside your space.")],
         who="restaurant and brewery owners, makers, artists and local shops",
         venue="Sanford has historic downtown venues, breweries and event halls for company events."),
    dict(slug="oviedo", name="Oviedo", kind="city",
         intro="Oviedo sits right next to UCF and has a growing mix of young professionals, founders and family run businesses.",
         spots=[("Center Lake Park", "Water, paths and an amphitheater for outdoor portraits."),
                ("Oviedo on the Park", "Modern, walkable spaces for lifestyle branding."),
                ("Near UCF", "Great for grads, researchers and startup teams.")],
         who="UCF grads, founders, coaches and local business owners",
         venue="Oviedo has community venues and nearby hotels for smaller company events."),
    dict(slug="celebration", name="Celebration", kind="city",
         intro="Celebration's planned town center, lakefront and classic architecture make polished photos easy. It suits realtors, wellness pros and anyone who wants a clean, bright look.",
         spots=[("Market Street", "Town center storefronts and sidewalks for lifestyle branding."),
                ("The lakefront", "Water, fountains and open sky."),
                ("Tree lined streets", "Classic architecture for calm, timeless portraits.")],
         who="realtors, wellness pros, coaches and family run businesses",
         venue="Celebration and the nearby resort area have hotels and venues for company events."),
]

# ------------------------------------------------------------------ SERVICES
SERVICES = dict(
    branding=dict(
        file="branding-photography-{s}.html", title="Branding Photographer in {a}, FL", h1="Branding photos in <em>{a}.</em>",
        eyebrow="Branding photography", hero="page-hero--red", main="branding.html", label="Branding",
        lede="One planned shoot for your website, LinkedIn and Instagram, photographed in {a} or in an Orlando studio. We decide the shots first so every frame has a job.",
        pool=["br-pinkcoat", "br-steps", "br-bw-woman", "br-blacksuit", "br-bw-man", "br-street", "br-director", "br-lagom", "br-tennis", "br-lashes"],
        caption="Branding",
        pricing='''<div class="price-row">
          <article class="price"><span class="tag">Most popular</span><h3>Starter Branding</h3>
            <ul><li>2-hour shoot</li><li>2 outfits</li><li>10 edited images</li><li>Delivered in 2 weeks</li></ul></article>
          <article class="price price--feature"><span class="tag">Best value</span><h3>Signature Branding</h3>
            <ul><li>3-hour shoot</li><li>4 outfits</li><li>15 edited images</li><li>Delivered in 3 weeks</li></ul></article>
        </div>
        <p class="terms">Every shoot is quoted to fit what you need. <a href="{BOOK}" target="_blank" rel="noopener" style="color:var(--red)">Request a quote</a> · 50% deposit secures your date</p>''',
        faqs=[("What do I get from a branding shoot?", "Edited, print ready images planned for where you will actually use them: your website, LinkedIn, Instagram and press. Starter includes 10 images, Signature includes 15."),
              ("Can we shoot at my business?", "Yes. On location is often the best choice for branding because it shows your real space, team and customers.")]),
    headshots=dict(
        file="headshots-{s}.html", title="Headshot Photographer in {a}, FL", h1="Headshots in <em>{a}.</em>",
        eyebrow="Headshot photography", hero="page-hero--ink", main="headshots.html", label="Headshots",
        lede="Professional headshots for actors, professionals and teams in {a}. Guided posing, flattering light and retouching, in an Orlando studio or at your office.",
        pool=["hs-tesoro", "hs-17", "hs-03", "hs-yamil", "hs-18", "hs-green", "hs-redtop", "hs-16", "hs-19", "hs-navytop", "hs-10", "br-curlyman", "hs-01"],
        caption="Headshots",
        pricing='''<div class="split" style="gap:32px">
          <div><h3>Ask for a quote</h3><p>Headshot pricing depends on how many people and looks you need. Tell me on a quick call and I'll send a quote within 24 hours.</p>
          <div><a class="btn btn--red" href="{BOOK}" target="_blank" rel="noopener">Get a quote</a></div></div>
          <div><h3>Need more than a headshot?</h3><p>Starter Branding includes ten edited images across two outfits, so you get your headshot plus photos for your website and social media.</p></div>
        </div>''',
        faqs=[("Do you shoot actor headshots?", "Yes. Actor headshots get clean light and natural retouching so you look like yourself in the audition room. We can shoot a commercial and a theatrical look in one session."), ("Can you photograph our whole team on site?", "Yes. Team headshots can be done at your office so everyone gets a consistent look without leaving work."),
              ("What should I wear?", "Solid colors, a jacket or blazer that fits, and a second top for variety. Skip logos and loud prints.")]),
    editorial=dict(
        file="editorial-photography-{s}.html", title="Editorial & Music Photographer in {a}, FL", h1="Editorial & music photos in <em>{a}.</em>",
        eyebrow="Editorial · music · beauty", hero="page-hero--black", main="editorial.html", label="Editorial & Music",
        lede="Album covers, press photos, beauty and fashion stories for artists and brands in {a}. Album credits include Alex Rose and Anuel AA.",
        pool=["ed-alexrose", "ed-01", "ed-greensuit", "ed-08", "ed-12", "ed-hero", "ed-navy", "ed-09", "ed-11", "ed-10", "ed-18", "ed-05", "ed-19", "ed-07", "ed-15", "ed-lily"],
        caption="Editorial",
        pricing='''<div class="price-row">
          <article class="price"><h3>Half Day</h3><ul><li>Up to 5 hours on set</li><li>Up to 3 set or location changes</li><li>Edits added per image</li></ul></article>
          <article class="price price--feature"><span class="tag">Max output</span><h3>Full Day</h3><ul><li>Up to 10 hours</li><li>Unlimited location changes</li><li>Travel within 1 hour included</li></ul></article>
        </div>
        <p class="terms">Add creative direction, hair &amp; makeup, BTS stills or a reel · every production is quoted after a free call · 50% deposit secures your date</p>''',
        faqs=[("Do you shoot album covers and press photos?", "Yes. Album art, single covers, press kits and promo shoots are a big part of my work, including credits with Alex Rose and Anuel AA."),
              ("Can you help with the concept?", "Yes. Creative direction can be added to any production and covers mood, styling direction and the shot list.")]),
    events=dict(
        file="corporate-event-photography-{s}.html", title="Corporate Event Photographer in {a}, FL", h1="Corporate event photos in <em>{a}.</em>",
        eyebrow="Corporate event photography", hero="page-hero--cream", main="contact.html", label="Corporate Events",
        lede="Conferences, company parties, launches and team days in {a}, covered by a bilingual photographer who knows how to work a room without getting in the way.",
        pool=["ev-a04", "ev-h10", "ev-a12", "ev-h08", "ev-a16", "ev-h12", "ev-a05", "ev-h06", "ev-a03", "ev-h05", "ev-a10", "ev-a09"],
        heroes=["ev-a09", "ev-h10"],
        caption="Event coverage",
        pricing='''<div class="price-row">
          <article class="price"><h3>Half Day</h3><ul><li>Up to 5 hours of coverage</li><li>Speakers, crowd, details and candids</li><li>Edits added per image</li></ul></article>
          <article class="price price--feature"><span class="tag">Full event</span><h3>Full Day</h3><ul><li>Up to 10 hours of coverage</li><li>Multiple rooms or locations</li><li>Travel within 1 hour included</li></ul></article>
        </div>
        <p class="terms">Add on-site team headshots or BTS content · English &amp; Spanish coverage · 50% deposit secures your date</p>''',
        faqs=[("Can you take team headshots during the event?", "Yes. A simple headshot setup at your event lets attendees or staff get a professional photo between sessions."),
              ("Do you cover events in Spanish?", "Yes. I work in English and Spanish, which helps with bilingual teams and international guests.")]),
)
ORDER = ["branding", "headshots", "editorial", "events"]


def fname(svc, area):
    return SERVICES[svc]["file"].format(s=area["slug"])


def picks(pool, i, n):
    k = (i * 3) % len(pool)
    rot = pool[k:] + pool[:k]
    return rot[:n]


# Low-value combinations: still reachable, but Google is asked to skip them so stronger pages carry more weight
NOINDEX = {("events", "thornton-park"), ("events", "lake-eola"), ("editorial", "celebration"), ("editorial", "oviedo")}


def area_page(svc_key, area, i):
    S = SERVICES[svc_key]
    a = area["name"]
    if svc_key == "events":
        hero = S["heroes"][i % 2]
        gal = picks(S["pool"], i, 6)
    else:
        p = picks(S["pool"], i, 7)
        hero, gal = p[0], p[1:7]
    frames = [frame(f"{g}.jpg", f"{S['caption']} photo by GLPX Studio", S["caption"], f"{(n * 3 + 2):02d}") for n, g in enumerate(gal)]
    spots = "".join(f"<li><span>{n}</span><span>{d}</span></li>" for n, d in area["spots"])
    others = " · ".join(f'<a href="{fname(k, area)}">{SERVICES[k]["label"]} in {a}</a>' for k in ORDER if k != svc_key)
    nearby = "".join(f'<a href="{fname(svc_key, b)}">{b["name"]}</a>' for b in AREAS if b is not area)
    travel = (f"Yes. {a} is part of my regular area. On location sessions happen right in {a}, and studio sessions take place in Orlando."
              if area["kind"] != "city" or area["slug"] == "orlando" else
              f"Yes. I travel to {a} for on location sessions, and studio sessions take place in Orlando. Full Day sessions include travel within one hour.")
    where = (f"<p>{area['venue']}</p>" if svc_key == "events" else "")
    REV = {"branding": ["grace", "johan"], "headshots": ["ashana", "melany"], "editorial": ["gabriel", "charlyn"], "events": ["charlyn", "gabriel"]}
    X = EXTRA.get(area["slug"])
    svc_line = f"<p>{X['svc'][svc_key]}</p>" if X else ""
    local = ""
    if X:
        local = f'''  <section class="section cream">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Planning a session in {a}</p>
        <h2>How a {a} shoot comes together.</h2>
        <p>{X["plan"]}</p>
      </div>
      <div>
        <ul class="ticks spots">
          <li><span>Best light</span><span>{X["light"]}</span></li>
          <li><span>Getting around</span><span>{X["logistics"]}</span></li>
          <li><span>Studio or on location</span><span>Studio sessions take place in a rented studio in Orlando. On location shoots happen right in {a}.</span></li>
        </ul>
      </div>
    </div>
  </section>

'''
    body = f'''  <section class="page-hero {S["hero"]}">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">{S["eyebrow"]} · {a}, FL</p>
        <h1>{S["h1"].format(a=a)}</h1>
        <p class="lede">{S["lede"].format(a=a)}</p>
        <div class="hero-actions">
          <a class="btn {"btn--solid" if S["hero"] == "page-hero--red" else "btn--red"}" href="{BOOK}" target="_blank" rel="noopener">Book a free strategy call</a>
          <a class="btn btn--ghost" href="{S["main"]}">{"See all " + S["label"] if svc_key != "events" else "Contact"}</a>
        </div>
      </div>
      <figure class="print">
        <img src="assets/img/{hero}.jpg" alt="{S["caption"]} photo by GLPX Studio">
        <figcaption><span>{S["label"]} · {a}</span><span>Fr. 01</span></figcaption>
      </figure>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div>
        <p class="eyebrow">{S["label"]} in {a}</p>
        <h2>Why shoot in {a}?</h2>
        <p>{area["intro"]}</p>
        {svc_line}
        {where}
        <p>I usually work with {area["who"]} here.</p>
      </div>
      <div>
        <p class="eyebrow">Where we can shoot</p>
        <ul class="ticks spots">{spots}</ul>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Recent work</p><h2>{S["label"]} by GLPX Studio.</h2></div>
      {sheet(frames, ["GLPX STUDIO", S["label"].upper(), "▸ " + a.upper()], "sheet--3")}
    </div>
  </section>

{local}{reviews_section(REV[svc_key], "What clients say.")}
  <section class="section cream">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Pricing</p><h2>A quote built around your shoot.</h2></div>
      {S["pricing"].replace("{BOOK}", BOOK)}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Questions</p><h2>{S["label"]} in {a}, answered.</h2></div>
      {faq([(f"Do you shoot in {a}?", travel)] + S["faqs"])}
      <p class="area-links" style="margin-top:40px">Also in {a}: {others}</p>
      <div class="area-nearby"><p class="eyebrow" style="color:var(--mute)">{S["label"]} in other areas</p><div class="tags">{nearby}</div></div>
    </div>
  </section>

{closer(f"Let's plan your shoot in <em>{a}.</em>")}'''
    ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"GLPX Studio",'
          f'"url":"{SITE}{fname(svc_key, area)}","telephone":"+1-407-534-7581","email":"glpxstudio@gmail.com",'
          f'"areaServed":"{a}, FL","serviceType":"{S["label"]} photography",'
          '"address":{"@type":"PostalAddress","addressLocality":"Orlando","addressRegion":"FL","addressCountry":"US"}}</script>\n')
    desc = f'{S["label"]} photography in {a}, FL by GLPX Studio. {S["lede"].format(a=a).split(". ")[0]}. Book a free strategy call.'
    robots = '<meta name="robots" content="noindex, follow">\n' if (svc_key, area["slug"]) in NOINDEX else ""
    page(fname(svc_key, area), S["title"].format(a=a) + " · GLPX Studio", desc.replace('"', "'"), body, robots + ld)


for i, area in enumerate(AREAS):
    for k in ORDER:
        area_page(k, area, i)

# ------------------------------------------------------------------ HUB
rows = ""
for area in AREAS:
    links = "".join(f'<a href="{fname(k, area)}">{SERVICES[k]["label"]}</a>' for k in ORDER)
    rows += f'<div class="area-row"><h3>{area["name"]}</h3><div class="tags">{links}</div></div>\n'
hub = f'''  <section class="page-hero page-hero--red">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Areas we serve</p>
        <h1>Orlando and <em>the neighborhoods around it.</em></h1>
        <p class="lede">Studio sessions take place in Orlando. On location shoots happen across these neighborhoods and nearby cities. Pick your area and the type of photos you need.</p>
      </div>
      <figure class="print"><img src="assets/img/ab-bts-steps.jpg" alt="Gerson photographing a client on location in downtown Orlando"><figcaption><span>On location</span><span>Orlando</span></figcaption></figure>
    </div>
  </section>
  <section class="section">
    <div class="wrap area-list">
{rows}    </div>
  </section>
{closer("Don't see your area? <em>Ask.</em>", "If you are within an hour of Orlando, I can most likely come to you.")}'''
page("areas.html", "Areas We Serve · GLPX Studio", "GLPX Studio photographs branding, headshots, editorial and corporate events across Orlando, Winter Park, Lake Nona, Kissimmee, Lake Mary and more.", hub)

# ------------------------------------------------------------------ Link strip on main service pages
strip_for = {"branding.html": "branding", "headshots.html": "headshots", "editorial.html": "editorial"}
for f, k in strip_for.items():
    html = (ROOT / f).read_text()
    links = "".join(f'<a href="{fname(k, a)}">{a["name"]}</a>' for a in AREAS)
    strip = (f'  <section class="section" style="padding-block:48px">\n    <div class="wrap area-nearby"><p class="eyebrow" style="color:var(--red)">'
             f'{SERVICES[k]["label"]} by area</p><div class="tags">{links}</div><p style="margin-top:16px"><a href="areas.html">See all areas we serve →</a></p></div>\n  </section>\n\n')
    html = html.replace('  <section class="closer">', strip + '  <section class="closer">', 1)
    (ROOT / f).write_text(html)

# ------------------------------------------------------------------ sitemap + robots
urls = ["", "branding.html", "headshots.html", "editorial.html", "about.html", "contact.html", "areas.html", "book.html", "portfolio.html"]
urls += [fname(k, a) for a in AREAS for k in ORDER if (k, a["slug"]) not in NOINDEX]
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                                  "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
print("area pages:", len(AREAS) * len(ORDER))

import v2  # rebuild the live homepage last

# 404 page for GitHub Pages
page("404.html", "Page not found · GLPX Studio", "This page moved or doesn't exist.", f'''  <section class="page-hero">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Error 404</p>
        <h1>This frame <em>didn't make the cut.</em></h1>
        <p class="lede">The page you're looking for moved or doesn't exist. Start from the homepage or book a free call.</p>
        <div class="hero-actions"><a class="btn btn--red" href="index.html">Back to the homepage</a><a class="btn btn--ghost" href="{BOOK}" target="_blank" rel="noopener">Book a free call</a></div>
      </div>
    </div>
  </section>''', '<meta name="robots" content="noindex">\n')

import book  # Book a Call page + thank-you page
import services2  # commercial + corporate/team headshot pages
import finish  # structured data, social previews, lazy images
import blog  # journal posts, legal pages, redirects from old Pixpa addresses
import links  # Instagram link-in-bio page at /links
