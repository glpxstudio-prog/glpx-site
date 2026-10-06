"""Book a Call page (calendar embedded) and the post-booking thank-you page.
Runs from areas.py before finish.py."""
from build import page, faq, BOOK, ROOT

CAL_ID = BOOK.rstrip("/").split("/")[-1]
GUIDE = "assets/guide/GLPX-Studio-Client-Guide.pdf"

embed = f'''<div class="cal-wrap">
        <iframe src="{BOOK}" title="Book a free strategy call with GLPX Studio" id="{CAL_ID}_booking" scrolling="no"></iframe>
        <p class="cal-fallback">Calendar not loading? <a href="{BOOK}" target="_blank" rel="noopener noreferrer">Open it in a new tab</a> or text <a href="sms:+14075347581">(407) 534-7581</a>.</p>
      </div>
      <script src="https://link.msgsend.com/js/form_embed.js" defer></script>'''

book = f'''  <section class="page-hero post-hero book-hero">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Free strategy call</p>
        <h1>Let's plan your <em>shoot.</em></h1>
        <p class="lede">Pick a time that works for you. We'll talk through what you need, where the photos will live, and I will send a custom quote within 24 hours of the call. English o español.</p>
      </div>
    </div>
  </section>

  <section class="section book-sec">
    <div class="wrap book-grid">
      {embed}
      <aside class="book-side">
        <p class="eyebrow">What happens next</p>
        <ol class="prep">
          <li>You get a confirmation by email and text, plus the GLPX client guide so you know exactly how a shoot works.</li>
          <li>On the call we cover goals, looks, locations and timing. No prep needed.</li>
          <li>You receive a custom quote within 24 hours.</li>
          <li>A 50% deposit locks in your date.</li>
        </ol>
        <div class="book-alt">
          <p class="eyebrow">Rather talk now?</p>
          <a class="btn btn--ghost" href="tel:+14075347581">Call (407) 534-7581</a>
          <a class="btn btn--ghost" href="sms:+14075347581">Text me</a>
          <a class="btn btn--ghost" href="https://www.instagram.com/glpxstudio/" target="_blank" rel="noopener">DM @glpxstudio</a>
        </div>
      </aside>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Before you book</p><h2>Quick answers.</h2></div>
      {faq([
        ("Is the call really free?", "Yes. It's a short call to understand what you need. There's no obligation to book a shoot."),
        ("What should I have ready?", "Nothing formal. It helps to know where the photos will be used (website, LinkedIn, an album, a press kit) and any dates you're working toward."),
        ("Can we talk in Spanish?", "Sí. Calls and sessions run in English or Spanish, whichever you prefer."),
        ("I need a team or event quote.", "Book the call and mention how many people or the event date. I'll put together a quote for the whole group."),
      ])}
    </div>
  </section>'''
page("book.html", "Book a Free Strategy Call · GLPX Studio Orlando",
     "Book a free strategy call with GLPX Studio for branding, headshot, editorial or event photography in Orlando. Pick a time on the calendar.", book)

booked = f'''  <section class="page-hero post-hero">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">You're booked</p>
        <h1>Talk soon. <em>Here's your guide.</em></h1>
        <p class="lede">Your call is on the calendar and a confirmation is on its way to your email and phone. While you wait, take a look at the GLPX client guide. It walks you through how a shoot works from first call to final gallery.</p>
        <div class="hero-actions">
          <a class="btn btn--red" href="{GUIDE}" target="_blank" rel="noopener" download>Download the client guide (PDF)</a>
          <a class="btn btn--ghost" href="index.html#work">See recent work</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Need to change your time?</p>
        <h2>No problem.</h2>
        <p>Use the reschedule link in your confirmation email, or text <a href="sms:+14075347581">(407) 534-7581</a> and I'll move it for you.</p>
      </div>
      <div>
        <p class="eyebrow">Get a head start</p>
        <h2>Three things to think about.</h2>
        <ul class="ticks">
          <li><span>Where the photos will be used</span><span>Website · LinkedIn · IG</span></li>
          <li><span>Any dates you're working toward</span><span>Launch · listing · release</span></li>
          <li><span>Two or three images you love</span><span>Screenshots are fine</span></li>
        </ul>
      </div>
    </div>
  </section>'''
page("booked.html", "You're Booked · GLPX Studio", "Your strategy call with GLPX Studio is booked. Download the client guide.", booked,
     '<meta name="robots" content="noindex">\n')
print("book pages built")
