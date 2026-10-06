"""Two service pages aimed at high-intent searches found in Search Console / keyword research:
  commercial-photography-orlando.html   ("commercial photography near me / Orlando")
  corporate-headshots-orlando.html      ("corporate headshots", "LinkedIn headshots", team headshots)
Runs from areas.py after book.py and before finish.py. Adds both to the sitemap and cross-links them."""
import re
from build import page, frame, sheet, faq, closer, reviews_section, BOOK, ROOT

SITE = "https://www.glpxstudio.com/"

# ------------------------------------------------------------------ COMMERCIAL
cm_frames = [
    frame("br-laptop.jpg", "Professional in black holding a laptop against a grey studio backdrop", "Studio", "01"),
    frame("br-jersey.jpg", "Man in a red football jersey and cap seated on a folding chair", "Campaign", "04", pick=True),
    frame("br-suit.jpg", "Woman in a black suit with arms crossed standing at a desk", "Studio", "07"),
    frame("br-green.jpg", "Woman in a green sweater in front of a green panel", "Studio", "10"),
    frame("br-fringe.jpg", "Man in a black and white fringe sweater against a deep blue backdrop", "Campaign", "13"),
    frame("br-lightblue.jpg", "Woman in a light blue dress against a soft blue backdrop", "Studio", "16"),
    frame("br-night.jpg", "Woman in a black coat on a lit downtown Orlando street at night", "On location", "19"),
    frame("br-bluelight.jpg", "Man in sunglasses and a graphic jacket under saturated blue light", "Campaign", "22"),
    frame("br-sofa.jpg", "Man seated on a leather sofa next to a plant in a white brick space", "Lifestyle", "25"),
]

commercial = f'''  <section class="page-hero page-hero--ink">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Commercial photography · Orlando, FL</p>
        <h1>Commercial photos that <em>sell the work.</em></h1>
        <p class="lede">Campaign, website and ad images for Orlando businesses. People first: your team, your customers and your brand in action, planned around exactly where every image will run.</p>
        <div class="hero-actions">
          <a class="btn btn--red" href="{BOOK}" target="_blank" rel="noopener">Book a free strategy call</a>
          <a class="btn btn--ghost" href="#work">See commercial work</a>
        </div>
      </div>
      <figure class="print">
        <img src="assets/img/yellow-suit.jpg" alt="Stylist in a butter yellow suit holding shears against a cream backdrop">
        <figcaption><span>Commercial · Studio</span><span>Fr. 01</span></figcaption>
      </figure>
    </div>
  </section>

  <div class="credits"><div class="wrap">
    <span>Built for <b>local brands</b></span><span><b>Salons</b> &amp; barbershops</span><span><b>Clinics</b> &amp; practices</span><span>Startups &amp; <b>agencies</b></span>
  </div></div>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">What commercial shoots cover</p>
        <h2>Images with a job to do.</h2>
        <p>Commercial photography is any image your business uses to sell. Before the shoot we list every place the photos will live, so you get the right shapes, the right people and the right message in each frame.</p>
      </div>
      <div class="steps">
        <div class="step"><h3>Website &amp; landing pages</h3><p>Hero banners with room for a headline, about page portraits and service photos that show what you actually do.</p></div>
        <div class="step"><h3>Ads &amp; social campaigns</h3><p>Vertical and square frames for Meta, Google and Instagram, shot as a set so your campaign looks consistent.</p></div>
        <div class="step"><h3>Your team at work</h3><p>Real people doing the real job. Behind the chair, at the desk, with a client. The photos that build trust fastest.</p></div>
        <div class="step"><h3>Launches &amp; announcements</h3><p>New location, new hire, new offer. Fresh images for the press release, the post and the email.</p></div>
      </div>
    </div>
  </section>

  <section class="section dark" id="work">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Commercial work</p>
        <h2>Studio sets, city streets and real workplaces.</h2>
      </div>
      {sheet(cm_frames, ["GLPX STUDIO", "COMMERCIAL", "▸ ORLANDO"], "sheet--3")}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">How a commercial shoot runs</p><h2>Planned like a campaign.</h2></div>
      <div class="steps">
        <div class="step"><h3>Strategy call</h3><p>We talk goals, audience and where the images will run. You get a custom quote within 24 hours.</p></div>
        <div class="step"><h3>Shot list</h3><p>Every frame is planned in advance: who is in it, what they are doing, and which crop it needs.</p></div>
        <div class="step"><h3>Shoot day</h3><p>A studio session in Orlando, on location at your business, or both. I direct the people so nobody looks staged.</p></div>
        <div class="step"><h3>Delivery</h3><p>Edited, high resolution files sorted by use, ready for your website, ads and social.</p></div>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap cs-bts">
      <img src="assets/img/ab-bts-set.jpg" alt="Gerson setting up lights and camera on a commercial photo set">
      <div>
        <p class="eyebrow" style="color: var(--red)">Behind the scenes</p>
        <h3>Small crew. Big output.</h3>
        <p>Lighting, direction and a clear shot list mean more usable images per hour. Need more hands? Hair, makeup and creative direction can be added to any production.</p>
      </div>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Productions</p>
        <h2>Half day or full day.</h2>
        <ul class="ticks">
          <li><span>Half Day</span><span>Up to 5 hours · 3 set changes</span></li>
          <li><span>Full Day</span><span>Up to 10 hours · unlimited locations</span></li>
          <li><span>Travel</span><span>Within 1 hour of Orlando included on full days</span></li>
          <li><span>Add-ons</span><span>Creative direction · hair &amp; makeup</span></li>
          <li><span>Sets</span><span>English &amp; Español</span></li>
        </ul>
      </div>
      <div>
        <p class="eyebrow">Pricing</p>
        <h2>Quoted per project.</h2>
        <p>Every commercial shoot is different, so every quote is custom. Tell me what you need on a free call and I will send a quote within 24 hours. A 50% deposit secures your date.</p>
        <div><a class="btn btn--red" href="{BOOK}" target="_blank" rel="noopener">Get a quote</a></div>
      </div>
    </div>
  </section>

{reviews_section(["grace", "johan", "charlyn"], "Businesses on working with GLPX.")}
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Questions</p><h2>Before you book.</h2></div>
      {faq([
        ("What is the difference between commercial and branding photography?", "Branding photography is usually about one person and their personal brand. Commercial photography is for the business itself: your team, your service, your customers and your campaigns. Many shoots mix both. See <a href='branding.html'>branding photography</a> for personal brand shoots."),
        ("Where do we shoot?", "A studio session in Orlando, on location at your business, or a mix of both. We decide on the strategy call based on what the images need to show."),
        ("Can you photograph my team and customers?", "Yes. People are the focus of my commercial work. I direct everyone in the frame so the photos feel natural, not staged. For a matching set of team portraits, see <a href='corporate-headshots-orlando.html'>team headshots</a>."),
        ("Do you shoot interiors, real estate or product only images?", "No. My commercial work is people first. If you need interiors or real estate, I am happy to point you to someone who specializes in it."),
        ("Do you work in Spanish?", "Yes. Every shoot can run in English or Spanish, which helps with bilingual teams and customers."),
      ])}
    </div>
  </section>

{closer("Let's plan your <em>campaign.</em>", "Tell me where the photos will run. We'll build the shoot around it.")}'''

page("commercial-photography-orlando.html", "Commercial Photographer in Orlando, FL · GLPX Studio",
     "Commercial photography in Orlando for local brands, salons, clinics and startups. Website, ad and campaign images of your team and business, in studio or on location. Custom quotes.",
     commercial)

# ------------------------------------------------------------------ CORPORATE / TEAM / LINKEDIN HEADSHOTS
team_frames = [
    frame("jestic-adrian.jpg", "Barber in a black Jestic polo against a charcoal backdrop", "Team", "01"),
    frame("jestic-ericko.jpg", "Barber with a beard in a black Jestic polo", "Team", "02"),
    frame("jestic-jesus.jpg", "Smiling barber with a full beard in a grey Jestic polo", "Team", "03", pick=True),
    frame("jestic-luisito.jpg", "Barber in a black Jestic polo looking into the lens", "Team", "04"),
    frame("jestic-regal.jpg", "Barber in clear glasses and a black Jestic polo", "Team", "05"),
    frame("jestic-rene.jpg", "Barber in a black Jestic polo with a short beard", "Team", "06"),
]
corp_frames = [
    frame("headshot-3.jpg", "Executive in glasses, navy suit and gold striped tie", "Corporate", "01"),
    frame("headshot-2.jpg", "Smiling doctor in a white coat with arms crossed", "Medical", "04"),
    frame("hs-hero.jpg", "Smiling professional in a navy suit and white shirt", "LinkedIn", "07", pick=True),
    frame("hs-07.jpg", "Man in a navy check suit with a pocket square", "Corporate", "10"),
    frame("hs-14.jpg", "Smiling woman in a black and white tweed jacket", "LinkedIn", "13"),
    frame("hs-12.jpg", "Man in a navy suit standing with hands together", "Corporate", "16"),
]

corporate = f'''  <section class="page-hero page-hero--black">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Corporate &amp; LinkedIn headshots · Orlando, FL</p>
        <h1>Team headshots that <em>match.</em></h1>
        <p class="lede">One consistent look for your whole team, photographed at your office or in an Orlando studio. Same light, same backdrop, same crop, so your website and LinkedIn look like one company.</p>
        <div class="hero-actions">
          <a class="btn btn--red" href="{BOOK}" target="_blank" rel="noopener">Get a team quote</a>
          <a class="btn btn--ghost" href="#team">See a team set</a>
        </div>
      </div>
      <figure class="print">
        <img src="assets/img/headshot-1.jpg" alt="Executive in a navy suit and burgundy tie with hands together" style="object-position:50% 25%">
        <figcaption><span>Corporate headshot</span><span>Fr. 01</span></figcaption>
      </figure>
    </div>
  </section>

  <div class="credits"><div class="wrap">
    <span>Law &amp; <b>finance</b></span><span><b>Medical</b> practices</span><span>Real estate <b>teams</b></span><span>Salons &amp; <b>barbershops</b></span>
  </div></div>

  <section class="section dark" id="team">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">One crew, one look</p>
        <h2>A full team, shot to match.</h2>
        <p>The Jestic barbershop team, photographed with the same backdrop, light and framing. Add a new hire next year and their photo will still match.</p>
      </div>
      {sheet(team_frames, ["GLPX STUDIO", "TEAM HEADSHOTS", "▸ ORLANDO"], "sheet--3")}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">How an on-site day runs</p><h2>Set up in a corner. Back to work fast.</h2></div>
      <div class="steps">
        <div class="step"><h3>We plan the look</h3><p>Backdrop color, crop and wardrobe notes, matched to your brand and your website.</p></div>
        <div class="step"><h3>I bring the studio</h3><p>Lights and backdrop fit in a conference room or open office corner. Your team never leaves the building.</p></div>
        <div class="step"><h3>A few minutes each</h3><p>Everyone gets guided posing and coaching, so nobody ends up with their stiff camera face.</p></div>
        <div class="step"><h3>Retouched &amp; delivered</h3><p>Each person picks a favorite. Files come retouched and cropped for LinkedIn, your website and badges.</p></div>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap cs-bts">
      <img src="assets/img/jestic-atwork.jpg" alt="Jestic barber cutting a client's hair in the shop">
      <div>
        <p class="eyebrow" style="color: var(--red)">Same visit, more content</p>
        <h3>Headshots plus the team at work.</h3>
        <p>While the setup is there, we can also capture your team doing the job. Those shots feed your website, Google profile and social for months. See <a href="commercial-photography-orlando.html" style="color:var(--red)">commercial photography</a>.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Individual LinkedIn &amp; corporate headshots</p>
        <h2>Just you? Same polish.</h2>
        <p>New role, new firm or a profile photo that is overdue. Book a solo session in an Orlando studio and leave with a headshot that works on LinkedIn, your bio and your next speaking slide.</p>
      </div>
      {sheet(corp_frames, ["GLPX STUDIO", "CORPORATE", "▸ ORLANDO"], "sheet--3")}
    </div>
  </section>

  <section class="section cream">
    <div class="wrap split">
      <div>
        <p class="eyebrow">What you get</p>
        <h2>Ready for every profile.</h2>
        <ul class="ticks">
          <li><span>Backdrop</span><span>Matched to your brand</span></li>
          <li><span>Coaching</span><span>For every person</span></li>
          <li><span>Retouching</span><span>Natural, true to you</span></li>
          <li><span>Crops</span><span>LinkedIn · website · badge</span></li>
          <li><span>New hires</span><span>Matched later</span></li>
          <li><span>Sessions</span><span>English &amp; Español</span></li>
        </ul>
      </div>
      <div>
        <p class="eyebrow">Pricing</p>
        <h2>Quoted by team size.</h2>
        <p>Team pricing depends on how many people, how many looks and whether we shoot on site or in a studio. Tell me on a quick call and I will send a quote within 24 hours.</p>
        <div><a class="btn btn--red" href="{BOOK}" target="_blank" rel="noopener">Get a team quote</a></div>
      </div>
    </div>
  </section>

{reviews_section(["ashana", "melany"], "Clients on their headshots.")}
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Questions</p><h2>Before you book.</h2></div>
      {faq([
        ("Can you come to our office?", "Yes. I bring lights and a backdrop and set up in a conference room or a quiet corner. It usually needs less space than people expect."),
        ("How long does each person take?", "Just a few minutes in front of the camera. We schedule people in short slots so nobody loses half a day of work."),
        ("What if someone misses the shoot or we hire later?", "We can photograph them later with the same backdrop, light and crop, so every headshot on your site still matches."),
        ("What should everyone wear?", "Solid colors and a jacket or blazer that fits. I will send a short wardrobe guide to share with the team before the shoot. More tips in <a href='blog/what-to-wear-for-headshots-orlando/index.html'>what to wear for headshots</a>."),
        ("Do you also do individual headshots?", "Yes. Solo corporate and LinkedIn headshots are shot in an Orlando studio. See <a href='headshots.html'>headshot photography</a> for actors and professionals."),
      ])}
    </div>
  </section>

{closer("Make the <em>whole team</em> look good.", "Headshots for 2 people or 50. Quoted within 24 hours.")}'''

page("corporate-headshots-orlando.html", "Corporate &amp; Team Headshots in Orlando, FL · GLPX Studio",
     "Corporate, team and LinkedIn headshots in Orlando. On-site at your office or in a studio, with one consistent look for the whole team. Custom quotes within 24 hours.",
     corporate)

# ------------------------------------------------------------------ VIDEO
IG = "https://www.instagram.com/glpxstudio/"
video = f'''  <section class="page-hero page-hero--red">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Video · Orlando, FL</p>
        <h1>Video that <em>keeps up.</em></h1>
        <p class="lede">Phone-shot social content, brand videos and event videography for Orlando businesses. Shot on its own or alongside your photos, in English or Spanish.</p>
        <div class="hero-actions">
          <a class="btn btn--solid" href="{BOOK}" target="_blank" rel="noopener">Book a free strategy call</a>
          <a class="btn btn--ghost" href="{IG}" target="_blank" rel="noopener">See video on Instagram</a>
        </div>
      </div>
      <figure class="print">
        <img src="assets/img/ab-bts-team.jpg" alt="Black and white behind the scenes shot of Gerson and artists on set">
        <figcaption><span>On set · Video</span><span>Fr. 01</span></figcaption>
      </figure>
    </div>
  </section>

  <div class="credits"><div class="wrap">
    <span><b>Reels</b> &amp; TikToks</span><span><b>Brand</b> videos</span><span><b>Event</b> recaps</span><span>English &amp; <b>Español</b></span>
  </div></div>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">What I film</p>
        <h2>Three kinds of video. One goal: get you seen.</h2>
      </div>
      <div class="steps">
        <div class="step"><h3>Social content</h3><p>Reels, TikToks and Stories shot on phone for a native, organic look. Vertical, edited and ready to post, so your feed stays active without you filming yourself.</p></div>
        <div class="step"><h3>Brand &amp; business videos</h3><p>Your about us video, service explainers, founder story and client testimonials. The videos that live on your website and close the sale.</p></div>
        <div class="step"><h3>Event videography</h3><p>Conference and company event recaps, speaker clips and highlight reels you can post the same week.</p></div>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Photo + video</p>
        <h2>One shoot. Both covered.</h2>
        <p>Most businesses need photos and video from the same day. Book them together and you get matching visuals for your website, ads and social, with one plan, one crew and one schedule.</p>
        <div><a class="btn btn--red" href="{BOOK}" target="_blank" rel="noopener">Plan a photo + video shoot</a></div>
      </div>
      <div>
        <ul class="ticks">
          <li><span>Social content</span><span>Shot on phone · vertical</span></li>
          <li><span>Brand &amp; event video</span><span>Professional camera gear</span></li>
          <li><span>Photos</span><span>Same day, same look</span></li>
          <li><span>Formats</span><span>9:16 · 1:1 · 16:9</span></li>
          <li><span>Language</span><span>English &amp; Español</span></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">How a video shoot runs</p><h2>Hooks first. Camera second.</h2></div>
      <div class="steps">
        <div class="step"><h3>Strategy call</h3><p>We talk goals, platforms and where the videos will run. You get a custom quote within 24 hours.</p></div>
        <div class="step"><h3>Plan the content</h3><p>Hooks, talking points and a shot list, so nothing on shoot day is improvised.</p></div>
        <div class="step"><h3>Shoot day</h3><p>On location at your business, at your event or in an Orlando studio. I direct you on camera, so you don't need to be a natural.</p></div>
        <div class="step"><h3>Edit &amp; deliver</h3><p>Edited videos sized for each platform, ready to post or hand to your team.</p></div>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap cs-bts">
      <img src="assets/img/bts.jpg" alt="Lighting setup on set before a shoot">
      <div>
        <p class="eyebrow" style="color: var(--red)">Latest work</p>
        <h3>The newest videos live on Instagram.</h3>
        <p>Reels and behind-the-scenes clips from recent shoots are posted on <a href="{IG}" target="_blank" rel="noopener" style="color:var(--red)">@glpxstudio</a>. Ask on your call and I will share examples that match your industry.</p>
      </div>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Pricing</p>
        <h2>Quoted per project.</h2>
        <p>Video depends on how many pieces you need, how long the shoot runs and how much editing goes into each one. Tell me on a free call and I will send a quote within 24 hours. A 50% deposit secures your date.</p>
        <div><a class="btn btn--red" href="{BOOK}" target="_blank" rel="noopener">Get a quote</a></div>
      </div>
      <div>
        <p class="eyebrow">Pairs well with</p>
        <h2>Photos for the same campaign.</h2>
        <p>Add <a href="branding.html">branding photos</a>, <a href="commercial-photography-orlando.html">commercial photos</a> or <a href="corporate-headshots-orlando.html">team headshots</a> to the same day.</p>
      </div>
    </div>
  </section>

{reviews_section(["johan", "gabriel"], "Clients on working with GLPX.")}
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Questions</p><h2>Before you book.</h2></div>
      {faq([
        ("Why shoot social content on a phone?", "Phone video looks native on Reels and TikTok, which usually means more views than polished ads. Brand and event videos are filmed with professional camera gear when the job calls for it."),
        ("Do I need to be good on camera?", "No. I give you the lines, the hooks and direction between takes. Most people loosen up after the first few minutes."),
        ("Can you film our event and take photos too?", "Yes. Event coverage can include photos, a recap video and short clips for social. See <a href='corporate-event-photography-orlando.html'>corporate event photography</a>."),
        ("Do you post the videos for us?", "I deliver edited videos ready to post. Posting and account management stay with you or your team."),
        ("Do you film in Spanish?", "Yes. Content can be filmed in English, Spanish or both, which helps when your customers are bilingual."),
      ])}
    </div>
  </section>

{closer("Let's get you <em>on camera.</em>", "Social content, brand videos and event coverage across Orlando.")}'''

page("videography-orlando.html", "Videographer in Orlando, FL · Social, Brand &amp; Event Video · GLPX Studio",
     "Orlando videographer for social media content, brand and business videos, and event recaps. Phone-shot Reels and TikToks, plus photo and video on the same day. Custom quotes.",
     video)

# ------------------------------------------------------------------ cross-links from existing pages
NEW = ["commercial-photography-orlando.html", "corporate-headshots-orlando.html", "videography-orlando.html"]

cm = ROOT / "commercial-photography-orlando.html"
t = cm.read_text()
t = t.replace('<details><summary>Do you work in Spanish?</summary>',
              '<details><summary>Do you shoot video too?</summary><p>Yes. Social content, brand videos and event recaps can be filmed on the same day as your photos. See <a href="videography-orlando.html">video</a>.</p></details><details><summary>Do you work in Spanish?</summary>', 1)
cm.write_text(t)

hs = ROOT / "headshots.html"
t = hs.read_text()
t = t.replace("<p>Teams and offices are welcome. Ask about group sessions.</p>",
              '<p>Teams and offices are welcome. See <a href="corporate-headshots-orlando.html" style="color:var(--red)">team &amp; corporate headshots</a>.</p>', 1)
hs.write_text(t)

br = ROOT / "branding.html"
t = br.read_text()
if "Do you shoot for businesses" not in t:
    t = t.replace('<details><summary>How do I lock in a date?</summary>',
                  '<details><summary>Do you shoot for businesses, not just personal brands?</summary><p>Yes. For team, campaign and website images for your business, see <a href="commercial-photography-orlando.html">commercial photography</a>.</p></details><details><summary>How do I lock in a date?</summary>', 1)
br.write_text(t)

# ------------------------------------------------------------------ sitemap
sm = (ROOT / "sitemap.xml").read_text()
add = "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in NEW if f"{SITE}{u}<" not in sm)
(ROOT / "sitemap.xml").write_text(sm.replace("</urlset>", add + "</urlset>"))
print("service pages:", ", ".join(NEW))
