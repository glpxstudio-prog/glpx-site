"""Spanish pages under /es/, each paired with its English page through hreflang.

One page per real Spanish search, not a copy of every English page:
  es/                                         <-> index.html
  es/fotografia-de-marca-orlando/             <-> branding.html
  es/fotos-profesionales-orlando/             <-> headshots.html
  es/fotografo-musica-artistas-orlando/       <-> editorial.html
  es/fotografia-eventos-corporativos-orlando/ <-> corporate-event-photography-orlando.html

Runs at the end of areas.py. It also adds the hreflang tags and an "Español" link to the
English pages of each pair, and the Spanish URLs to the sitemap, so a full rebuild keeps
everything in step. Edit the Spanish text here, then run .venv/bin/python areas.py."""
import re
import build, finish
from build import page, frame, sheet, faq, reviews_section, ROOT
from blog import REL

SITE = "https://www.glpxstudio.com/"
BOOKING = "book.html"

# Spanish path -> English file it translates
PAIRS = {
    "es/": "index.html",
    "es/fotografia-de-marca-orlando/": "branding.html",
    "es/fotos-profesionales-orlando/": "headshots.html",
    "es/fotografo-musica-artistas-orlando/": "editorial.html",
    "es/fotografia-eventos-corporativos-orlando/": "corporate-event-photography-orlando.html",
}

NAV_ES = [
    ("es/", "Inicio"),
    ("es/fotografia-de-marca-orlando/", "Marca"),
    ("es/fotos-profesionales-orlando/", "Headshots"),
    ("es/fotografo-musica-artistas-orlando/", "Artistas"),
    ("es/fotografia-eventos-corporativos-orlando/", "Eventos"),
    ("portfolio.html", "Portafolio"),
    ("contact.html", "Contacto"),
]

RELATED = [
    ("es/fotografia-de-marca-orlando/", "Fotografía de marca personal"),
    ("es/fotos-profesionales-orlando/", "Fotos profesionales y headshots"),
    ("es/fotografo-musica-artistas-orlando/", "Fotógrafo para artistas"),
    ("es/fotografia-eventos-corporativos-orlando/", "Eventos corporativos"),
]


def en_url(f):
    return SITE + ("" if f == "index.html" else f)


def hreflang_tags(es_path):
    en = en_url(PAIRS[es_path])
    return (f'<link rel="alternate" hreflang="en" href="{en}">\n'
            f'<link rel="alternate" hreflang="es" href="{SITE}{es_path}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{en}">\n')


def header_es(current):
    en = PAIRS[current]
    links = "\n".join(f'      <a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV_ES)
    menu = "\n".join(f'          <a href="{h}">{t}</a>' for h, t in NAV_ES)
    return f'''<header class="site-head">
  <div class="wrap">
    <a class="logo" href="es/" aria-label="GLPX Studio, inicio"><img src="assets/img/logo-white.svg" alt="GLPX Studio"></a>
    <nav class="nav" aria-label="Principal">
{links}
      <a href="{en}" lang="en" hreflang="en">English</a>
      <details class="menu">
        <summary>Menú +</summary>
        <div class="menu-panel">
{menu}
          <a href="{en}" lang="en" hreflang="en">English</a>
        </div>
      </details>
      <a class="btn btn--red" href="{BOOKING}">Reservar</a>
    </nav>
  </div>
</header>'''


FOOTER_ES = f'''<footer class="site-foot">
  <div class="wrap">
    <div><img src="assets/img/logo-white.svg" alt="GLPX Studio"></div>
    <div>
      <h4>Explora</h4>
      <ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV_ES + [("blog/", "Blog"), ("index.html", "English")])}</ul>
    </div>
    <div>
      <h4>Contacto</h4>
      <ul><li><a href="tel:+14075347581">Llama al (407) 534-7581</a></li><li><a href="sms:+14075347581">Escribe al (407) 534-7581</a></li><li><a href="mailto:glpxstudio@gmail.com">glpxstudio@gmail.com</a></li><li><a href="https://www.instagram.com/glpxstudio/" target="_blank" rel="noopener">Instagram @glpxstudio</a></li><li>Orlando, FL</li></ul>
    </div>
    <p class="fine">© 2026 GLPX Studio · Fotografía de marca, retratos profesionales, editorial y video en Orlando, FL · <a href="terms-and-conditions/index.html">Términos</a> · <a href="privacy-policy/index.html">Privacidad</a></p>
  </div>
</footer>'''


def closer_es(title_html, sub=""):
    return f'''  <section class="closer">
    <div class="wrap">
      <p class="eyebrow">Siguiente paso</p>
      <h2>{title_html}</h2>
      {f"<p class='lede'>{sub}</p>" if sub else ""}
      <div><a class="btn btn--solid" href="{BOOKING}">Agenda una llamada gratis</a></div>
      <div class="contact-lines"><a href="tel:+14075347581">Llama al (407) 534-7581</a><a href="sms:+14075347581">Escríbeme</a><a href="mailto:glpxstudio@gmail.com">glpxstudio@gmail.com</a><a href="https://www.instagram.com/glpxstudio/" target="_blank" rel="noopener">@glpxstudio</a></div>
    </div>
  </section>'''


def reviews_es(keys, heading):
    # Client quotes stay in the words they were written in; only the frame is translated.
    return (reviews_section(keys, heading)
            .replace("Google reviews · 5.0", "Reseñas en Google · 5.0")
            .replace("Read all reviews on Google →", "Lee todas las reseñas en Google →")
            .replace('aria-label="5 out of 5 stars"', 'aria-label="5 de 5 estrellas"'))


def related(current):
    """Links to the other Spanish pages, so none is left without internal links."""
    rows = "".join(f'<a href="{h}">{t}</a>' for h, t in RELATED if h != current)
    return (f'  <section class="section cream">\n    <div class="wrap"><p class="eyebrow">También en español</p>'
            f'<div class="tags">{rows}<a href="blog/foto-perfil-linkedin/">Guía: foto de perfil para LinkedIn</a>'
            f'<a href="blog/fotos-para-realtors-orlando/">Guía: fotos para realtors</a></div></div>\n  </section>\n\n')


def write_es(path, title, desc, body, extra_head=""):
    tmp = ROOT / "_tmp_es.html"
    page(tmp.name, title, desc, body, finish.LD + extra_head + hreflang_tags(path))
    html = tmp.read_text()
    html = html.replace('<html lang="en">', '<html lang="es">', 1)
    html = re.sub(r'<header class="site-head">.*?</header>', lambda m: header_es(path), html, count=1, flags=re.S)
    html = re.sub(r'<footer class="site-foot">.*?</footer>', lambda m: FOOTER_ES, html, count=1, flags=re.S)
    tmp.write_text(html)
    url = SITE + path
    finish.finish(tmp, url)
    html = tmp.read_text()
    tmp.unlink()
    # Spanish wording for the pieces finish.py adds to every page
    html = (html.replace("Text Me</a>", "Escríbeme</a>")
                .replace('<span class="pick-note">The pick</span>', '<span class="pick-note">La elegida</span>')
                .replace("Request a Consultation</a>", "Agenda una consulta</a>")
                .replace("Hi%20Gerson!%20I%27m%20interested%20in%20a%20GLPX%20Studio%20session.",
                         "%C2%A1Hola%20Gerson!%20Me%20interesa%20una%20sesi%C3%B3n%20con%20GLPX%20Studio.")
                .replace('aria-label="Text GLPX Studio at (407) 534-7581"', 'aria-label="Escribe a GLPX Studio al (407) 534-7581"')
                .replace('aria-label="Contact GLPX Studio"', 'aria-label="Contacta a GLPX Studio"')
                .replace('content="GLPX Studio, Orlando branding and headshot photography"',
                         'content="GLPX Studio, fotografía de marca y retratos profesionales en Orlando"')
                .replace('<meta property="og:type" content="website">',
                         '<meta property="og:type" content="website">\n<meta property="og:locale" content="es_US">'))
    depth = path.rstrip("/").count("/") + 1
    html = REL.sub(lambda m: m.group(1) + "../" * depth, html)
    html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', html)
    dest = ROOT / path / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html)


def service_ld(name, desc, path):
    import json
    return '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "Service", "name": name, "description": desc,
        "inLanguage": "es", "url": SITE + path, "areaServed": "Orlando, FL",
        "provider": {"@type": "ProfessionalService", "name": "GLPX Studio", "url": SITE, "telephone": "+1-407-534-7581"},
    }, ensure_ascii=False) + "</script>\n"


def faq_ld(items):
    import json
    return '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage", "inLanguage": "es",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
                       for q, a in items],
    }, ensure_ascii=False) + "</script>\n"


# ================================================================== INICIO  es/
home_frames = [
    frame("br-pinkcoat.jpg", "Mujer sonriente con abrigo rosado y una tableta frente a un fondo magenta", "Marca", "01",
          href="es/fotografia-de-marca-orlando/", pick=True),
    frame("ed-alexrose.jpg", "Alex Rose con chaqueta roja y boina sobre fondo negro", "Música", "04", href="es/fotografo-musica-artistas-orlando/"),
    frame("hs-03.jpg", "Mujer con vestido lavanda y brazos cruzados en estudio", "Retrato", "07", href="es/fotos-profesionales-orlando/"),
    frame("ev-lcda-04.jpg", "Panel de conferencia corporativa en un hotel de Orlando", "Evento", "10", href="es/fotografia-eventos-corporativos-orlando/"),
    frame("br-steps.jpg", "Mujer de traje negro bajando unas escaleras en el centro de Orlando", "Marca", "13", href="es/fotografia-de-marca-orlando/"),
    frame("hs-tesoro.jpg", "Abogada con blazer negro sobre fondo gris oscuro", "Retrato", "16", href="es/fotos-profesionales-orlando/"),
]
home_faq = [
    ("¿Las sesiones son en español?", "Sí. Toda la sesión puede ser en español: la llamada de planificación, la dirección durante las fotos y la entrega. También trabajo en inglés, así que los equipos bilingües se sienten cómodos."),
    ("¿Cuánto cuesta una sesión?", "Cada sesión se cotiza según lo que necesitas: cuántas personas, cuántos looks, el lugar y cuántas fotos editadas. Agenda una llamada gratis y te envío la cotización en menos de 24 horas."),
    ("¿Dónde son las sesiones?", "En un estudio rentado en Orlando o en exteriores: tu oficina, tu negocio o una calle del centro. También cubro Winter Park, Lake Nona, Kissimmee, Dr. Phillips y el resto de la Florida Central."),
    ("¿Cómo reservo la fecha?", "Con un depósito del 50 %. El resto se paga el día de la sesión."),
]
home = f'''  <section class="page-hero page-hero--red">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Fotógrafo en Orlando, FL · En español</p>
        <h1>Fotos que hablan <em>por tu marca.</em></h1>
        <p class="lede">Soy Gerson, fotógrafo en Orlando con más de 8 años de experiencia. Hago fotografía de marca personal, fotos profesionales, portadas para artistas y eventos corporativos, con toda la sesión en español si lo prefieres.</p>
        <div class="hero-actions">
          <a class="btn btn--solid" href="{BOOKING}">Agenda una llamada gratis</a>
          <a class="btn btn--ghost" href="#servicios">Ver servicios</a>
        </div>
      </div>
      <figure class="print">
        <img src="assets/img/br-director.jpg" alt="Mujer sonriente con traje color crema sentada en una silla de director">
        <figcaption><span>Marca personal · Estudio</span><span>Fr. 01</span></figcaption>
      </figure>
    </div>
  </section>

  <div class="credits"><div class="wrap">
    <span><b>8+</b> años de experiencia</span><span><b>200+</b> clientes</span><span>Portadas · <b>Alex Rose</b> · <b>Anuel AA</b></span><span>Sesiones en <b>español</b> e inglés</span>
  </div></div>

  <section class="section" id="servicios">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Servicios</p>
        <h2>Cuatro formas de trabajar juntos.</h2>
        <p>Todas empiezan con una llamada gratis para planear las fotos antes de sacar la cámara.</p>
      </div>
      <div class="steps" style="grid-template-columns: repeat(auto-fit, minmax(220px, 1fr))">
        <div class="step"><h3><a href="es/fotografia-de-marca-orlando/">Fotografía de marca personal</a></h3><p>Una sesión planeada con outfits, lugares y lista de tomas para tu web, LinkedIn e Instagram.</p></div>
        <div class="step"><h3><a href="es/fotos-profesionales-orlando/">Fotos profesionales y headshots</a></h3><p>Retratos limpios y actuales para LinkedIn, tu empresa o tu perfil de actor. Te dirijo en cada pose.</p></div>
        <div class="step"><h3><a href="es/fotografo-musica-artistas-orlando/">Artistas y música</a></h3><p>Portadas de álbum, fotos de prensa y contenido para tu lanzamiento, con dirección creativa.</p></div>
        <div class="step"><h3><a href="es/fotografia-eventos-corporativos-orlando/">Eventos corporativos</a></h3><p>Conferencias, fiestas de empresa y lanzamientos, cubiertos en español y en inglés.</p></div>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Trabajo reciente</p><h2>Algunas fotos de sesiones recientes.</h2></div>
      {sheet(home_frames, ["GLPX STUDIO", "ORLANDO", "▸ EN ESPAÑOL"], "sheet--3")}
      <p style="margin-top:24px"><a class="btn btn--ghost" href="portfolio.html">Ver el portafolio completo</a></p>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Por qué en español</p>
        <h2>Es más fácil relajarte cuando te dirigen en tu idioma.</h2>
      </div>
      <div>
        <p>La mayoría de las personas me dice que odia salir en fotos. Por eso dirijo toda la sesión: dónde pararte, qué hacer con las manos, hacia dónde mirar. Cuando esas indicaciones llegan en tu idioma, la tensión se va más rápido y se nota en las fotos.</p>
        <p>Trabajo con dueños de negocio, realtors, abogados, médicos, artistas y equipos completos en Orlando. Muchos atienden clientes en los dos idiomas, y sus fotos tienen que funcionar en los dos mercados.</p>
        <div><a class="btn btn--red" href="about.html">Conoce más sobre mí (en inglés)</a></div>
      </div>
    </div>
  </section>

{reviews_es(["johan", "grace", "charlyn"], "Lo que dicen los clientes.")}
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Preguntas frecuentes</p><h2>Antes de reservar.</h2></div>
      {faq(home_faq)}
    </div>
  </section>

{related("es/")}{closer_es("Planeemos <em>tu</em> sesión.")}'''
write_es("es/", "Fotógrafo en Orlando que habla español · GLPX Studio",
         "Fotógrafo en Orlando con sesiones en español: fotografía de marca personal, fotos profesionales, portadas para artistas y eventos corporativos.",
         home, faq_ld(home_faq))

# ================================================================== MARCA PERSONAL
br_frames = [
    frame("br-pinkcoat.jpg", "Mujer sonriente con abrigo rosado y una tableta frente a un fondo magenta", "Estudio", "02", pick=True),
    frame("br-steps.jpg", "Mujer de traje negro bajando escaleras en el centro con un bolso de cuero", "Exteriores", "05"),
    frame("br-bw-woman.jpg", "Retrato en blanco y negro de una mujer con blazer amplio y guantes", "Estudio", "08"),
    frame("br-blacksuit.jpg", "Hombre sonriente de traje negro con las manos juntas", "Estudio", "11"),
    frame("br-bw-man.jpg", "Retrato en blanco y negro de un hombre con camisa blanca apoyado en una pared", "Estudio", "14"),
    frame("br-street.jpg", "Mujer con abrigo negro caminando por una calle con flores", "Exteriores", "17"),
]
br_faq = [
    ("¿Qué es la fotografía de marca personal?", "Es una sesión planeada para mostrar quién eres y cómo trabajas: retratos, fotos trabajando y detalles de tu negocio. A diferencia de un headshot, te da variedad para tu web, redes sociales, LinkedIn y materiales de prensa."),
    ("¿Dónde hacemos la sesión?", "En un estudio rentado en Orlando o en exteriores: tu oficina, una propiedad que estás vendiendo, una calle del centro o donde realmente pasa tu trabajo. Lo decidimos en la llamada."),
    ("¿Qué debo llevar?", "Un outfit por cada look de tu paquete: dos en Starter y cuatro en Signature. Los colores sólidos se ven mejor. Trae lo que usas en tu trabajo, como tu laptop, herramientas o productos."),
    ("¿Cuándo recibo mis fotos?", "Starter Branding se entrega en dos semanas y Signature Branding en tres. Los archivos llegan en alta resolución, listos para imprimir."),
    ("¿Puedo agregar maquillaje y peinado?", "Sí. Maquillaje, peinado y dirección creativa se pueden agregar a cualquier sesión y se incluyen en tu cotización."),
    ("¿Cómo reservo la fecha?", "Con un depósito del 50 %. El resto se paga el día de la sesión."),
]
marca = f'''  <section class="page-hero page-hero--red">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Fotografía de marca personal · Orlando, FL</p>
        <h1>Fotos de marca <em>con un plan.</em></h1>
        <p class="lede">Una sola sesión planeada que cubre tu web, LinkedIn, Instagram y kit de prensa. Decidimos las tomas antes de sacar la cámara, así cada foto tiene un propósito. Toda la sesión puede ser en español.</p>
        <div class="hero-actions">
          <a class="btn btn--solid" href="{BOOKING}">Agenda una llamada gratis</a>
          <a class="btn btn--ghost" href="#paquetes">Ver paquetes</a>
        </div>
      </div>
      <figure class="print">
        <img src="assets/img/br-director.jpg" alt="Mujer sonriente con traje color crema sentada en una silla de director">
        <figcaption><span>Marca personal · Estudio</span><span>Fr. 01</span></figcaption>
      </figure>
    </div>
  </section>

  <div class="credits"><div class="wrap">
    <span>Para <b>emprendedores</b></span><span><b>Realtors</b> y brokers</span><span><b>Abogados</b> y consultores</span><span>Coaches y <b>pequeños negocios</b></span>
  </div></div>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Lo que te llevas</p>
        <h2>Cada formato que tu marca necesita, planeado desde antes.</h2>
        <p>Cada plataforma pide una forma distinta. Fotografiamos pensando en todas, para que no termines recortando un retrato vertical para el banner de tu web.</p>
      </div>
      <div class="crops">
        <div class="crop"><div class="crop-box" style="aspect-ratio:4/5"><img src="assets/img/br-director.jpg" alt="" style="object-position:50% 30%"><span>4:5</span></div><h3>Feed de Instagram</h3><p>Retratos y fotos trabajando, del tamaño justo para tu perfil.</p></div>
        <div class="crop"><div class="crop-box" style="aspect-ratio:9/16"><img src="assets/img/br-director.jpg" alt="" style="object-position:40% 50%"><span>9:16</span></div><h3>Stories y Reels</h3><p>Fotos verticales con espacio para poner texto encima.</p></div>
        <div class="crop"><div class="crop-box" style="aspect-ratio:16/9"><img src="assets/img/br-director.jpg" alt="" style="position:absolute;width:130%;height:auto;max-width:none;left:-24%;top:-16%"><span>16:9</span></div><h3>Banners para tu web</h3><p>Tomas amplias con espacio libre para tu titular.</p></div>
        <div class="crop"><div class="crop-box" style="aspect-ratio:1/1"><img src="assets/img/br-director.jpg" alt="" style="position:absolute;width:300%;height:auto;max-width:none;left:-95%;top:-26%"><span>1:1</span></div><h3>LinkedIn y prensa</h3><p>Un headshot limpio para perfiles, biografías y artículos.</p></div>
      </div>
      <p class="terms">Una sola foto de la sesión, recortada de cuatro maneras.</p>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Sesiones de marca</p>
        <h2>En el estudio y donde realmente trabajas.</h2>
      </div>
      {sheet(br_frames, ["GLPX STUDIO", "MARCA PERSONAL", "▸ ORLANDO"], "sheet--3")}
    </div>
  </section>

  <section class="section cream" id="paquetes">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Paquetes</p>
        <h2>Sesión, estudio y edición en un solo paquete.</h2>
      </div>
      <div class="price-row">
        <article class="price">
          <span class="tag">El más popular</span>
          <h3>Starter Branding</h3>
          <ul><li>Sesión de 2 horas</li><li>2 outfits</li><li>10 fotos editadas</li><li>Archivos en alta resolución, listos para imprimir</li><li>Entrega en 2 semanas</li></ul>
        </article>
        <article class="price price--feature">
          <span class="tag">Mejor valor</span>
          <h3>Signature Branding</h3>
          <ul><li>Sesión de 3 horas</li><li>4 outfits</li><li>15 fotos editadas</li><li>Archivos en alta resolución, listos para imprimir</li><li>Entrega en 3 semanas</li></ul>
        </article>
      </div>
      <p class="terms">Cada sesión se cotiza según lo que necesitas. <a href="{BOOKING}" style="color:var(--red)">Pide tu cotización</a> · Maquillaje y peinado, fotos detrás de cámaras y reels se pueden agregar · Un depósito del 50 % reserva tu fecha</p>
    </div>
  </section>

{reviews_es(["grace", "johan", "charlyn"], "Clientes sobre su sesión de marca.")}
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Preguntas frecuentes</p><h2>Antes de reservar.</h2></div>
      {faq(br_faq)}
    </div>
  </section>

{related("es/fotografia-de-marca-orlando/")}{closer_es("Planeemos tu sesión de <em>marca</em>.")}'''
marca_desc = "Fotografía de marca personal en Orlando para emprendedores, realtors y abogados. Una sesión planeada para tu web, LinkedIn e Instagram, en español."
write_es("es/fotografia-de-marca-orlando/", "Fotografía de marca personal en Orlando · GLPX Studio", marca_desc, marca,
         service_ld("Fotografía de marca personal en Orlando", marca_desc, "es/fotografia-de-marca-orlando/") + faq_ld(br_faq))

# ================================================================== FOTOS PROFESIONALES
hs_frames = [
    frame("hs-01.jpg", "Hombre con lentes, traje azul marino y corbata a rayas", "Gris", "01"),
    frame("hs-17.jpg", "Mujer sonriente con blusa de lunares", "Gris lavanda", "04"),
    frame("hs-03.jpg", "Mujer con vestido lavanda y brazos cruzados", "Gris claro", "07", pick=True),
    frame("hs-yamil.jpg", "Joven con suéter gris claro y brazos cruzados", "Gris", "10"),
    frame("hs-green.jpg", "Mujer sonriente con blazer verde", "Gris lavanda", "13"),
    frame("hs-redtop.jpg", "Mujer sonriente de cabello rizado con blusa roja", "Gris lavanda", "16"),
    frame("hs-16.jpg", "Joven con blazer azul marino y camisa blanca", "Gris", "19"),
    frame("hs-19.jpg", "Mujer sonriente con lentes y blusa a rayas naranja", "Gris lavanda", "22"),
    frame("hs-10.jpg", "Barbero con polo blanco de su marca", "Gris", "25"),
]
hs_faq = [
    ("¿Qué es un headshot?", "Es una foto profesional de los hombros hacia arriba, con buena luz y un fondo limpio. Se usa en LinkedIn, en la web de tu empresa, en tarjetas de presentación y en perfiles de actor."),
    ("¿Cuánto dura una sesión de fotos profesionales?", "Una sesión individual suele tomar menos de una hora. Si quieres varios looks o fondos, o si es un equipo completo, lo planeamos en la llamada."),
    ("¿Qué ropa me pongo?", "Colores sólidos en lugar de estampados, un blazer o saco que te quede bien y una segunda opción de ropa para variar. Evita logos y estampados llamativos."),
    ("¿Hacen fotos para equipos y empresas?", "Sí. Puedo montar el estudio en tu oficina para que todo el equipo tenga fotos con la misma luz y el mismo fondo. Pregunta por las sesiones grupales."),
    ("¿Las fotos se ven retocadas de más?", "No. El retoque es natural: limpio y profesional, pero sigues pareciendo tú. Eso es especialmente importante para actores, porque el casting necesita ver a la persona real."),
    ("¿Cuánto cuestan las fotos profesionales?", "El precio depende de cuántas personas y cuántos looks necesitas. Cuéntame en una llamada rápida y te envío la cotización en menos de 24 horas."),
]
fotos = f'''  <section class="page-hero page-hero--ink">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Fotos profesionales y headshots · Orlando, FL</p>
        <h1>Fotos que se parecen a ti <em>en tu mejor día.</em></h1>
        <p class="lede">Headshots en Orlando para LinkedIn, empresas, abogados, médicos, realtors y actores. Te dirijo en cada pose, en español, así que no necesitas saber posar.</p>
        <div class="hero-actions">
          <a class="btn btn--red" href="{BOOKING}">Reserva tu sesión</a>
          <a class="btn btn--ghost" href="#galeria">Ver fotos</a>
        </div>
      </div>
      <figure class="print">
        <img src="assets/img/hs-tesoro.jpg" alt="Abogada con blazer negro sobre fondo gris oscuro" style="object-position:50% 30%">
        <figcaption><span>Headshot · Tesoro Law</span><span>Fr. 01</span></figcaption>
      </figure>
    </div>
  </section>

  <section class="section dark" id="galeria">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Headshots recientes</p>
        <h2>La misma luz. Personas distintas. Nadie se ve tieso.</h2>
      </div>
      {sheet(hs_frames, ["GLPX STUDIO", "FOTOS PROFESIONALES", "▸ ORLANDO"], "sheet--3")}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Cómo es la sesión</p><h2>Rápida, guiada y lista.</h2></div>
      <div class="steps">
        <div class="step"><h3>Elige el fondo</h3><p>Gris, gris oscuro, gris azulado o blanco, según tu industria y tu web.</p></div>
        <div class="step"><h3>Luz para tu cara</h3><p>Ajusto la luz para ti, incluyendo lentes, tono de piel y el ángulo que mejor te queda.</p></div>
        <div class="step"><h3>Dirección</h3><p>Te guío en la postura y la expresión hasta lograr la versión que la gente reconoce.</p></div>
        <div class="step"><h3>Retoque</h3><p>Tus fotos favoritas se retocan para verse pulidas sin dejar de parecer tú.</p></div>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Para cada uso</p>
        <h2>Una foto, muchos lugares.</h2>
        <p>Tu headshot es lo primero que ve un reclutador, un cliente o un director de casting. Lo usas en LinkedIn, en la web de tu empresa, en tu firma de correo y en tus perfiles. Por eso tiene que verse actual y parecerse a la persona que llega a la reunión.</p>
        <p>Para actores, podemos hacer un look comercial y uno teatral en la misma sesión.</p>
        <div><a class="btn btn--red" href="blog/foto-perfil-linkedin/">Guía: foto de perfil para LinkedIn</a></div>
      </div>
      <div>
        <ul class="ticks">
          <li><span>LinkedIn y perfiles</span><span>Sí</span></li>
          <li><span>Web de tu empresa</span><span>Sí</span></li>
          <li><span>Equipos completos</span><span>En tu oficina</span></li>
          <li><span>Actores</span><span>Comercial y teatral</span></li>
          <li><span>Sesión</span><span>Español e inglés</span></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Qué ponerte</p>
        <h2>Lo simple funciona.</h2>
        <ul class="ticks">
          <li><span>Colores sólidos en vez de estampados</span><span>Sí</span></li>
          <li><span>Un blazer o saco que te quede bien</span><span>Sí</span></li>
          <li><span>Una segunda blusa o camisa</span><span>Tráela</span></li>
          <li><span>Logos y estampados llamativos</span><span>Evítalos</span></li>
          <li><span>Maquillaje y peinado</span><span>Opcional</span></li>
        </ul>
      </div>
      <div>
        <p class="eyebrow">Precio</p>
        <h2>Pide tu cotización.</h2>
        <p>El precio depende de cuántas personas y cuántos looks necesitas. Cuéntame en una llamada rápida y te envío la cotización en menos de 24 horas. ¿Necesitas más que un headshot? Mira la <a href="es/fotografia-de-marca-orlando/">fotografía de marca personal</a>.</p>
        <div><a class="btn btn--red" href="{BOOKING}">Pide tu cotización</a></div>
      </div>
    </div>
  </section>

{reviews_es(["ashana", "melany"], "Clientes sobre sus fotos.")}
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Preguntas frecuentes</p><h2>Lo que más me preguntan.</h2></div>
      {faq(hs_faq)}
    </div>
  </section>

{related("es/fotos-profesionales-orlando/")}{closer_es("Retira la foto <em>recortada</em> de las vacaciones.")}'''
fotos_desc = "Fotos profesionales y headshots en Orlando para LinkedIn, empresas, abogados, realtors y actores. Sesión guiada en español, con retoque natural."
write_es("es/fotos-profesionales-orlando/", "Fotos profesionales y headshots en Orlando · GLPX Studio", fotos_desc, fotos,
         service_ld("Fotos profesionales y headshots en Orlando", fotos_desc, "es/fotos-profesionales-orlando/") + faq_ld(hs_faq))

# ================================================================== ARTISTAS Y MÚSICA
ed_frames = [
    frame("ed-greensuit.jpg", "Artista con traje verde cruzado apoyado en una pared de madera", "Música", "01"),
    frame("ed-08.jpg", "Artista con lentes de sol frente a una pared de bocinas", "Música", "04", pick=True),
    frame("ed-12.jpg", "Retrato de belleza con accesorios de perlas sobre fondo rosado", "Belleza", "07"),
    frame("ed-hero.jpg", "Mujer con rosas rojas frente a un fondo rojo intenso", "Belleza", "10"),
    frame("ed-09.jpg", "Artista con lentes de sol y cadena de oro sobre fondo gris", "Música", "13"),
    frame("ed-navy.jpg", "Modelo rubia con chaqueta azul marino y guantes largos de cuero", "Moda", "16"),
    frame("ed-10.jpg", "Artista con camiseta amarilla y gorra verde frente a un fondo verde", "Música", "19"),
    frame("ed-07.jpg", "Modelo con traje amplio color salvia frente a un degradado morado", "Moda", "22"),
    frame("ed-01.jpg", "Retrato de belleza con joyas plateadas en la cara", "Belleza", "25"),
]
ed_faq = [
    ("¿Hacen portadas de álbum y sencillos?", "Sí. He hecho portadas para Alex Rose (El Nuevo Rockstar y Oversized) y Anuel AA (Las Leyendas Nunca Mueren). Planeamos la idea, el vestuario y el set para que la foto funcione en Spotify, Apple Music y en redes."),
    ("¿Qué incluye una sesión para artistas?", "Tú eliges el tiempo: medio día (hasta 5 horas y 3 cambios de set) o día completo (hasta 10 horas y cambios ilimitados). Las fotos editadas se agregan por imagen, así que solo pagas por las que vas a usar."),
    ("¿También hacen video para el lanzamiento?", "Sí. Puedes agregar fotos detrás de cámaras, un reel de 30 a 60 segundos o un paquete de contenido con 2 reels y 15 fotos detrás de cámaras."),
    ("¿Hay dirección creativa?", "Sí, tanta como quieras. Se puede agregar dirección creativa, maquillaje y peinado a cualquier producción."),
    ("¿Con cuánto tiempo debo reservar?", "Lo ideal es planear la sesión varias semanas antes de tu fecha de lanzamiento, para tener tiempo de editar y preparar el contenido. Mándame la fecha y lo armamos desde ahí."),
]
artistas = f'''  <section class="page-hero page-hero--black">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Artistas · Música · Editorial · Orlando, FL</p>
        <h1>Portadas, prensa y <em>todo lo que va en medio.</em></h1>
        <p class="lede">Fotógrafo para artistas en Orlando: portadas de álbum, fotos de prensa, contenido para lanzamientos y editoriales de belleza y moda. Producciones de medio día o día completo, con dirección creativa en español.</p>
        <div class="hero-actions">
          <a class="btn btn--red" href="{BOOKING}">Planea tu producción</a>
          <a class="btn btn--ghost" href="#tarifas">Ver tarifas</a>
        </div>
      </div>
      <figure class="print">
        <img src="assets/img/ed-alexrose.jpg" alt="Alex Rose con chaqueta roja y boina sobre fondo negro">
        <figcaption><span>Alex Rose · Música</span><span>Fr. 01</span></figcaption>
      </figure>
    </div>
  </section>

  <div class="credits"><div class="wrap">
    <span>Portadas · <b>Alex Rose</b></span><span>Portadas · <b>Anuel AA</b></span><span><b>8+</b> años en set</span><span>Sets en <b>español</b> e inglés</span>
  </div></div>

  <section class="section dark">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Trabajo editorial</p>
        <h2>Color, actitud y una razón para cada foto.</h2>
      </div>
      {sheet(ed_frames, ["GLPX STUDIO", "ARTISTAS", "▸ ORLANDO"], "sheet--3")}
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Para tu lanzamiento</p>
        <h2>Una sesión, todo el contenido del lanzamiento.</h2>
      </div>
      <div>
        <p>Un lanzamiento necesita más que la portada: fotos de prensa, contenido vertical para Reels y TikTok, y material para anunciar la fecha. Lo planeamos todo en una sola producción, para que llegues al día del estreno con contenido listo para varias semanas.</p>
        <p>Trabajo con artistas de música urbana, pop y regional, y con productores y sellos independientes en la Florida Central.</p>
        <div><a class="btn btn--red" href="blog/contenido-lanzamiento-musical/">Guía: contenido para un lanzamiento musical</a></div>
      </div>
    </div>
  </section>

  <section class="section cream" id="tarifas">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Tarifas por sesión</p>
        <h2>Reservas el tiempo. Eliges las fotos editadas.</h2>
        <p>La tarifa cubre la fotografía. Las fotos editadas se agregan por imagen, así solo pagas por retocar las que vas a usar. Cada sesión se cotiza después de una llamada gratis.</p>
      </div>
      <div class="price-row">
        <article class="price">
          <h3>Medio día</h3>
          <ul><li>Hasta 5 horas en set</li><li>Hasta 3 cambios de set o locación</li><li>Marca, editorial y sesiones personales</li></ul>
        </article>
        <article class="price price--feature">
          <span class="tag">Máximo contenido</span>
          <h3>Día completo</h3>
          <ul><li>Hasta 10 horas</li><li>Cambios de locación ilimitados</li><li>Traslado incluido hasta 1 hora de Orlando</li><li>Campañas, portadas y producciones completas</li></ul>
        </article>
      </div>
      <div class="price-group" style="margin-top:56px">
        <p class="eyebrow">Completa la producción</p>
        <div class="addons">
          <div><span>Dirección creativa</span><b>Opcional</b></div>
          <div><span>Maquillaje</span><b>Opcional</b></div>
          <div><span>Peinado</span><b>Opcional</b></div>
          <div><span>Fotos detrás de cámaras · 10 fotos</span><b>Opcional</b></div>
          <div><span>Reel · 30–60 seg</span><b>Opcional</b></div>
          <div><span>Paquete de contenido · 2 reels + 15 fotos</span><b>Opcional</b></div>
        </div>
        <p class="terms">Un depósito del 50 % reserva tu fecha · el resto se paga el día de la sesión</p>
      </div>
    </div>
  </section>

{reviews_es(["gabriel", "charlyn"], "Creativos sobre trabajar con GLPX.")}
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Preguntas frecuentes</p><h2>Antes de tu producción.</h2></div>
      {faq(ed_faq)}
    </div>
  </section>

{related("es/fotografo-musica-artistas-orlando/")}{closer_es("¿Tienes un lanzamiento <em>en camino?</em>", "Mándame la fecha y la idea. Armamos la sesión alrededor de eso.")}'''
art_desc = "Fotógrafo para artistas en Orlando: portadas de álbum, fotos de prensa y contenido para lanzamientos. Créditos con Alex Rose y Anuel AA, en español."
write_es("es/fotografo-musica-artistas-orlando/", "Fotógrafo para artistas y portadas en Orlando · GLPX Studio", art_desc, artistas,
         service_ld("Fotografía para artistas y portadas de álbum en Orlando", art_desc, "es/fotografo-musica-artistas-orlando/") + faq_ld(ed_faq))

# ================================================================== EVENTOS CORPORATIVOS
ev_frames = [
    frame("ev-lcda-04.jpg", "Panel de conferencia corporativa en un salón de hotel en Orlando", "Conferencia", "01", pick=True),
    frame("ev-lcda-05.jpg", "Asistentes conversando durante una conferencia", "Networking", "04"),
    frame("ev-lcda-07.jpg", "Orador en el escenario de una conferencia", "Escenario", "07"),
    frame("ev-lcda-09.jpg", "Público atento durante una presentación", "Público", "10"),
    frame("ev-lcda-14.jpg", "Detalle de un evento corporativo", "Detalles", "13"),
    frame("ev-h10.jpg", "Momento espontáneo durante un evento de empresa", "Espontáneas", "16"),
]
ev_faq = [
    ("¿Qué tipo de eventos cubren?", "Conferencias, convenciones, fiestas de fin de año, lanzamientos de producto, días de equipo y activaciones de marca, desde salones de hotel hasta el Orange County Convention Center."),
    ("¿Cubren eventos en español?", "Sí. Trabajo en español y en inglés, lo que ayuda con equipos bilingües, invitados internacionales y organizaciones latinas."),
    ("¿Pueden tomar headshots durante el evento?", "Sí. Un set sencillo de headshots en tu evento permite que asistentes o empleados se lleven una foto profesional entre sesiones."),
    ("¿Cuánto tiempo de cobertura necesito?", "Medio día cubre hasta 5 horas: oradores, público, detalles y fotos espontáneas. Día completo cubre hasta 10 horas, varios salones o locaciones, e incluye traslado hasta 1 hora de Orlando."),
    ("¿Hacen video del evento?", "Sí. Puedes agregar un video resumen del evento a cualquier cobertura."),
    ("¿Cómo reservo la fecha?", "Con un depósito del 50 %. Planeamos la cobertura según el programa del evento para no perder los momentos clave."),
]
eventos = f'''  <section class="page-hero page-hero--ink">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Fotografía de eventos corporativos · Orlando, FL</p>
        <h1>Tu evento, <em>bien contado.</em></h1>
        <p class="lede">Fotógrafo bilingüe para conferencias, fiestas de empresa, lanzamientos y días de equipo en Orlando. Sé moverme en el salón sin estorbar y planeo la cobertura según el programa del evento.</p>
        <div class="hero-actions">
          <a class="btn btn--red" href="{BOOKING}">Agenda una llamada gratis</a>
          <a class="btn btn--ghost" href="#cobertura">Ver cobertura</a>
        </div>
      </div>
      <figure class="print">
        <img src="assets/img/ev-lcda-01.jpg" alt="Conferencia corporativa en un hotel de Orlando">
        <figcaption><span>Eventos corporativos · Orlando</span><span>Fr. 01</span></figcaption>
      </figure>
    </div>
  </section>

  <div class="credits"><div class="wrap">
    <span><b>Conferencias</b> y convenciones</span><span>Fiestas de <b>fin de año</b></span><span><b>Lanzamientos</b> y activaciones</span><span>Cobertura en <b>español</b> e inglés</span>
  </div></div>

  <section class="section dark">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Trabajo reciente</p>
        <h2>Oradores, público, detalles y los momentos entre sesiones.</h2>
      </div>
      {sheet(ev_frames, ["GLPX STUDIO", "EVENTOS", "▸ ORLANDO"], "sheet--3")}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Cómo trabajo</p><h2>Cobertura planeada, no improvisada.</h2></div>
      <div class="steps">
        <div class="step"><h3>Revisamos el programa</h3><p>Antes del evento repasamos la agenda, los oradores y las fotos que no pueden faltar.</p></div>
        <div class="step"><h3>Cubro el salón</h3><p>Escenario, público, networking, patrocinadores y detalles, sin interrumpir.</p></div>
        <div class="step"><h3>Headshots en el evento</h3><p>Opcional: un set de headshots para asistentes o empleados entre sesiones.</p></div>
        <div class="step"><h3>Entrega</h3><p>Una galería privada con las fotos editadas, lista para prensa, redes y el informe del evento.</p></div>
      </div>
    </div>
  </section>

  <section class="section cream" id="cobertura">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Cobertura</p>
        <h2>Una cotización hecha para tu evento.</h2>
      </div>
      <div class="price-row">
        <article class="price">
          <h3>Medio día</h3>
          <ul><li>Hasta 5 horas de cobertura</li><li>Oradores, público, detalles y fotos espontáneas</li><li>Fotos editadas por imagen</li></ul>
        </article>
        <article class="price price--feature">
          <span class="tag">Evento completo</span>
          <h3>Día completo</h3>
          <ul><li>Hasta 10 horas de cobertura</li><li>Varios salones o locaciones</li><li>Traslado incluido hasta 1 hora de Orlando</li></ul>
        </article>
      </div>
      <p class="terms">Agrega headshots en el evento o un video resumen · Cobertura en español e inglés · Un depósito del 50 % reserva tu fecha</p>
    </div>
  </section>

{reviews_es(["charlyn", "gabriel"], "Lo que dicen los clientes.")}
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Preguntas frecuentes</p><h2>Eventos corporativos en Orlando.</h2></div>
      {faq(ev_faq)}
    </div>
  </section>

{related("es/fotografia-eventos-corporativos-orlando/")}{closer_es("Cuéntame de tu <em>evento</em>.", "Mándame la fecha, el lugar y el programa. Te envío una cotización en menos de 24 horas.")}'''
ev_desc = "Fotógrafo bilingüe para eventos corporativos en Orlando: conferencias, fiestas de empresa y lanzamientos. Cobertura en español e inglés."
write_es("es/fotografia-eventos-corporativos-orlando/", "Fotografía de eventos corporativos en Orlando · GLPX Studio", ev_desc, eventos,
         service_ld("Fotografía de eventos corporativos en Orlando", ev_desc, "es/fotografia-eventos-corporativos-orlando/") + faq_ld(ev_faq))


# ================================================================== English side of each pair
def link_english(path_es, f):
    p = ROOT / f
    html = p.read_text()
    if 'hreflang="es"' not in html:
        html = html.replace("</head>", hreflang_tags(path_es) + "</head>", 1)
    if 'class="lang-es"' not in html:
        a = f'<a class="lang-es" href="{path_es}" lang="es" hreflang="es">Español</a>'
        html = html.replace('      <details class="menu">', f"      {a}\n      <details class=\"menu\">", 1)
        html = html.replace('        </div>\n      </details>', f"          {a}\n        </div>\n      </details>", 1)
    p.write_text(html)


for path_es, f in PAIRS.items():
    link_english(path_es, f)

# ------------------------------------------------------------------ sitemap
sm = (ROOT / "sitemap.xml").read_text()
add = "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in PAIRS if f"{SITE}{u}<" not in sm)
(ROOT / "sitemap.xml").write_text(sm.replace("</urlset>", add + "</urlset>"))
print("spanish pages:", len(PAIRS))
