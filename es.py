"""Stand-alone Spanish section under /es/.

These pages are written for Spanish-speaking clients, not translated from the English pages,
and they are deliberately NOT connected to them: no hreflang, no language links either way.
The English pages are never touched by this script.

  es/                                         Inicio
  es/fotografia-de-marca-orlando/             Fotografía de marca personal
  es/fotos-profesionales-orlando/             Fotos profesionales y headshots
  es/fotografo-musica-artistas-orlando/       Artistas y portadas
  es/fotografia-eventos-corporativos-orlando/ Eventos corporativos

Runs at the end of areas.py and adds the pages to the sitemap.
Edit the Spanish text here, then run .venv/bin/python areas.py."""
import json, re
import build, finish
from build import page, frame, sheet, faq, reviews_section, ROOT
from blog import REL

SITE = "https://www.glpxstudio.com/"
BOOKING = "book.html"

NAV_ES = [
    ("es/", "Inicio"),
    ("es/fotografia-de-marca-orlando/", "Marca"),
    ("es/fotos-profesionales-orlando/", "Headshots"),
    ("es/fotografo-musica-artistas-orlando/", "Artistas"),
    ("es/fotografia-eventos-corporativos-orlando/", "Eventos"),
    ("portfolio.html", "Portafolio"),
]
PAGES = [h for h, _ in NAV_ES if h.startswith("es/")]
RELATED = [
    ("es/fotografia-de-marca-orlando/", "Fotografía de marca personal"),
    ("es/fotos-profesionales-orlando/", "Fotos profesionales y headshots"),
    ("es/fotografo-musica-artistas-orlando/", "Fotógrafo para artistas"),
    ("es/fotografia-eventos-corporativos-orlando/", "Eventos corporativos"),
]


def header_es(current):
    links = "\n".join(f'      <a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV_ES)
    menu = "\n".join(f'          <a href="{h}">{t}</a>' for h, t in NAV_ES)
    return f'''<header class="site-head">
  <div class="wrap">
    <a class="logo" href="es/" aria-label="GLPX Studio, inicio"><img src="assets/img/logo-white.svg" alt="GLPX Studio"></a>
    <nav class="nav" aria-label="Principal">
{links}
      <details class="menu">
        <summary>Menú +</summary>
        <div class="menu-panel">
{menu}
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
      <ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV_ES + [("blog/foto-perfil-linkedin/", "Guía: foto para LinkedIn"), ("blog/contenido-lanzamiento-musical/", "Guía: lanzamiento musical")])}</ul>
    </div>
    <div>
      <h4>Contacto</h4>
      <ul><li><a href="tel:+14075347581">Llama al (407) 534-7581</a></li><li><a href="sms:+14075347581">Escribe al (407) 534-7581</a></li><li><a href="mailto:glpxstudio@gmail.com">glpxstudio@gmail.com</a></li><li><a href="https://www.instagram.com/glpxstudio/" target="_blank" rel="noopener">Instagram @glpxstudio</a></li><li>Orlando, FL</li></ul>
    </div>
    <p class="fine">© 2026 GLPX Studio · Fotografía de marca, retratos profesionales, artistas y eventos en Orlando, FL · <a href="terms-and-conditions/index.html">Términos</a> · <a href="privacy-policy/index.html">Privacidad</a></p>
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
    # Client quotes stay in the words they were written in; only the frame is in Spanish.
    return (reviews_section(keys, heading)
            .replace("Google reviews · 5.0", "Reseñas en Google · 5.0")
            .replace("Read all reviews on Google →", "Lee todas las reseñas en Google →")
            .replace('aria-label="5 out of 5 stars"', 'aria-label="5 de 5 estrellas"'))


def related(current):
    rows = "".join(f'<a href="{h}">{t}</a>' for h, t in RELATED if h != current)
    return (f'  <section class="section cream">\n    <div class="wrap"><p class="eyebrow">Más servicios</p>'
            f'<div class="tags">{rows}<a href="blog/foto-perfil-linkedin/">Guía: foto de perfil para LinkedIn</a>'
            f'<a href="blog/fotos-para-realtors-orlando/">Guía: fotos para realtors</a></div></div>\n  </section>\n\n')


def write_es(path, title, desc, body, extra_head=""):
    tmp = ROOT / "_tmp_es.html"
    page(tmp.name, title, desc, body, finish.LD + extra_head)
    html = tmp.read_text()
    html = html.replace('<html lang="en">', '<html lang="es">', 1)
    html = re.sub(r'<header class="site-head">.*?</header>', lambda m: header_es(path), html, count=1, flags=re.S)
    html = re.sub(r'<footer class="site-foot">.*?</footer>', lambda m: FOOTER_ES, html, count=1, flags=re.S)
    tmp.write_text(html)
    url = SITE + path
    finish.finish(tmp, url)
    html = tmp.read_text()
    tmp.unlink()
    # Spanish wording for the pieces finish.py and frame() add to every page
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
    return '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "Service", "name": name, "description": desc,
        "inLanguage": "es", "url": SITE + path, "areaServed": "Orlando, FL",
        "provider": {"@type": "ProfessionalService", "name": "GLPX Studio", "url": SITE, "telephone": "+1-407-534-7581"},
    }, ensure_ascii=False) + "</script>\n"


def faq_ld(items):
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
    ("¿Toda la sesión es en español?", "Sí, de principio a fin: la llamada para planear, la dirección durante las fotos y la entrega. Si tu equipo o tus invitados hablan inglés, también lo manejo sin problema."),
    ("¿Cuánto cuesta?", "Depende de lo que necesites: cuántas personas, cuántos cambios de ropa, el lugar y cuántas fotos editadas. Agenda una llamada gratis y te mando la cotización en menos de 24 horas."),
    ("¿Dónde son las sesiones?", "En un estudio rentado en Orlando o en exteriores: tu oficina, tu negocio o una calle del centro. También voy a Kissimmee, Winter Park, Lake Nona, Dr. Phillips y el resto de la Florida Central."),
    ("¿Cómo aparto la fecha?", "Con un depósito del 50 %. El resto se paga el día de la sesión."),
]
home = f'''  <section class="page-hero page-hero--red">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Fotógrafo en Orlando, FL</p>
        <h1>Tu fotógrafo en Orlando, <em>en tu idioma.</em></h1>
        <p class="lede">Soy Gerson, fotógrafo latino en Orlando con más de 8 años de experiencia. Trabajo con dueños de negocio, profesionales, artistas y empresas que quieren fotos a la altura de lo que hacen, y toda la sesión puede ser en español.</p>
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
    <span><b>8+</b> años de experiencia</span><span><b>200+</b> clientes</span><span>Portadas · <b>Alex Rose</b> · <b>Anuel AA</b></span><span><b>5.0</b> en Google</span>
  </div></div>

  <section class="section" id="servicios">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Servicios</p>
        <h2>¿Qué necesitas?</h2>
        <p>Cada proyecto empieza con una llamada gratis. Me cuentas para qué son las fotos y armamos el plan juntos.</p>
      </div>
      <div class="steps" style="grid-template-columns: repeat(auto-fit, minmax(220px, 1fr))">
        <div class="step"><h3><a href="es/fotografia-de-marca-orlando/">Fotos para tu negocio</a></h3><p>Una sesión de marca personal con fotos para tu web, Instagram, Facebook y WhatsApp Business.</p></div>
        <div class="step"><h3><a href="es/fotos-profesionales-orlando/">Una foto profesional</a></h3><p>Headshots para LinkedIn, tu empresa, tus tarjetas de realtor o tu perfil de actor.</p></div>
        <div class="step"><h3><a href="es/fotografo-musica-artistas-orlando/">Tu próximo lanzamiento</a></h3><p>Portada, fotos de prensa y contenido para promocionar tu música.</p></div>
        <div class="step"><h3><a href="es/fotografia-eventos-corporativos-orlando/">Tu evento</a></h3><p>Conferencias, galas y fiestas de empresa, cubiertas en español y en inglés.</p></div>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Trabajo reciente</p><h2>Un poco de lo que hago.</h2></div>
      {sheet(home_frames, ["GLPX STUDIO", "ORLANDO", "▸ FLORIDA CENTRAL"], "sheet--3")}
      <p style="margin-top:24px"><a class="btn btn--ghost" href="portfolio.html">Ver el portafolio completo</a></p>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Con quién trabajo</p>
        <h2>Gente que atiende a la comunidad y quiere verse como se merece.</h2>
      </div>
      <div>
        <ul class="ticks">
          <li><span>Dueños de negocio latinos</span><span>Marca personal</span></li>
          <li><span>Realtors y agentes de seguros</span><span>Headshots y marca</span></li>
          <li><span>Abogados, médicos y consultores</span><span>Fotos profesionales</span></li>
          <li><span>Artistas y productores</span><span>Portadas y prensa</span></li>
          <li><span>Empresas y organizaciones</span><span>Equipos y eventos</span></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Cómo funciona</p><h2>Cuatro pasos, sin complicaciones.</h2></div>
      <div class="steps">
        <div class="step"><h3>1. Hablamos</h3><p>Una llamada gratis de unos minutos. Me cuentas qué necesitas y para cuándo.</p></div>
        <div class="step"><h3>2. Planeamos</h3><p>Te mando la cotización y armamos juntos el lugar, la ropa y las fotos que no pueden faltar.</p></div>
        <div class="step"><h3>3. La sesión</h3><p>Yo te dirijo todo el tiempo. No necesitas saber posar.</p></div>
        <div class="step"><h3>4. Tus fotos</h3><p>Las recibes en una galería privada, listas para usar donde las necesites.</p></div>
      </div>
    </div>
  </section>

{reviews_es(["johan", "grace", "charlyn"], "Lo que dicen los clientes.")}
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Preguntas frecuentes</p><h2>Lo que más me preguntan.</h2></div>
      {faq(home_faq)}
    </div>
  </section>

{related("es/")}{closer_es("Cuéntame qué <em>necesitas.</em>")}'''
write_es("es/", "Fotógrafo en Orlando que habla español · GLPX Studio",
         "Fotógrafo latino en Orlando con sesiones en español: fotos para tu negocio, fotos profesionales, portadas para artistas y eventos.",
         home, faq_ld(home_faq))

# ================================================================== MARCA PERSONAL
br_frames = [
    frame("br-pinkcoat.jpg", "Mujer sonriente con abrigo rosado y una tableta frente a un fondo magenta", "Estudio", "02", pick=True),
    frame("br-steps.jpg", "Mujer de traje negro bajando escaleras en el centro con un bolso de cuero", "Exteriores", "05"),
    frame("br-laptop.jpg", "Profesional vestida de negro con una laptop frente a un fondo gris", "Estudio", "08"),
    frame("br-blacksuit.jpg", "Hombre sonriente de traje negro con las manos juntas", "Estudio", "11"),
    frame("br-sofa.jpg", "Hombre sentado en un sofá de cuero junto a una planta", "Estilo de vida", "14"),
    frame("br-street.jpg", "Mujer con abrigo negro caminando por una calle con flores", "Exteriores", "17"),
]
br_faq = [
    ("¿Qué es una sesión de marca personal?", "Es una sesión planeada para mostrar quién eres y cómo trabajas: tu retrato principal, fotos atendiendo clientes o trabajando, y detalles de tu negocio. Te da variedad para publicar durante meses, no solo una foto de perfil."),
    ("¿Sirve para Facebook y WhatsApp Business?", "Sí. Planeamos fotos para cada lugar donde te encuentran tus clientes: tu web, Instagram, Facebook, tu perfil de WhatsApp Business, Google y tus anuncios."),
    ("¿Puedo hacer la sesión en mi negocio?", "Sí. Muchas sesiones son en el local del cliente: tu oficina, tu salón, tu restaurante o la propiedad que estás vendiendo. También puede ser en estudio, o una mezcla de los dos."),
    ("¿Qué me pongo?", "Un cambio de ropa por cada look de tu paquete: dos en Starter y cuatro en Signature. Los colores sólidos se ven mejor. Trae también lo que usas en tu trabajo: herramientas, productos, tu laptop."),
    ("¿Cuándo me entregan las fotos?", "Starter Branding se entrega en dos semanas y Signature Branding en tres, en alta resolución y listas para imprimir."),
    ("¿Cómo aparto la fecha?", "Con un depósito del 50 %. El resto se paga el día de la sesión. Maquillaje, peinado y dirección creativa se pueden agregar."),
]
marca = f'''  <section class="page-hero page-hero--red">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Fotografía de marca personal · Orlando, FL</p>
        <h1>Tu negocio merece <em>verse profesional.</em></h1>
        <p class="lede">Fotos de marca personal en Orlando para dueños de negocio, realtors, abogados y emprendedores. En una sola sesión salen las fotos para tu web, tus redes y tus anuncios, y la sesión es en español.</p>
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

  <section class="section">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Por qué importa</p>
        <h2>La gente compra a quien conoce.</h2>
      </div>
      <div>
        <p>Antes de llamarte, tus clientes te buscan en Google, en Instagram o en Facebook. Si lo que encuentran es una selfie o una foto de hace años, pasan a la siguiente opción. Una sesión de marca les muestra quién eres, cómo trabajas y por qué confiar en ti antes de la primera llamada.</p>
        <p>Muchos negocios en Orlando atienden en español y en inglés. Con una sola sesión tienes fotos que funcionan para los dos públicos, porque la foto no necesita traducción.</p>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Qué fotos salen</p><h2>Una sesión, meses de contenido.</h2></div>
      <div class="steps" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr))">
        <div class="step"><h3>Tu retrato principal</h3><p>Para tu web, Google y tu foto de perfil en todas partes.</p></div>
        <div class="step"><h3>Trabajando</h3><p>Atendiendo clientes, en tu escritorio, en el local. Fotos que cuentan qué haces.</p></div>
        <div class="step"><h3>Detalles</h3><p>Tus manos, tus herramientas, tus productos y tu espacio.</p></div>
        <div class="step"><h3>Con espacio para texto</h3><p>Tomas pensadas para anuncios, flyers y portadas de Facebook.</p></div>
        <div class="step"><h3>Vertical</h3><p>Fotos para Stories, Reels y tu estado de WhatsApp.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Sesiones recientes</p><h2>En estudio y en el lugar donde trabajas.</h2></div>
      {sheet(br_frames, ["GLPX STUDIO", "MARCA PERSONAL", "▸ ORLANDO"], "sheet--3")}
    </div>
  </section>

  <section class="section cream" id="paquetes">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Paquetes</p>
        <h2>Sesión, estudio y edición incluidos.</h2>
      </div>
      <div class="price-row">
        <article class="price">
          <span class="tag">El más popular</span>
          <h3>Starter Branding</h3>
          <ul><li>Sesión de 2 horas</li><li>2 cambios de ropa</li><li>10 fotos editadas</li><li>Alta resolución, listas para imprimir</li><li>Entrega en 2 semanas</li></ul>
        </article>
        <article class="price price--feature">
          <span class="tag">Mejor valor</span>
          <h3>Signature Branding</h3>
          <ul><li>Sesión de 3 horas</li><li>4 cambios de ropa</li><li>15 fotos editadas</li><li>Alta resolución, listas para imprimir</li><li>Entrega en 3 semanas</li></ul>
        </article>
      </div>
      <p class="terms">Cada sesión se cotiza según lo que necesitas. <a href="{BOOKING}" style="color:var(--red)">Pide tu cotización</a> · Maquillaje, peinado, fotos detrás de cámaras y reels se pueden agregar · Un depósito del 50 % aparta tu fecha</p>
    </div>
  </section>

{reviews_es(["grace", "johan", "charlyn"], "Clientes que ya hicieron su sesión.")}
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Preguntas frecuentes</p><h2>Antes de reservar.</h2></div>
      {faq(br_faq)}
    </div>
  </section>

{related("es/fotografia-de-marca-orlando/")}{closer_es("Hagamos que tu negocio <em>se vea</em> como es.")}'''
marca_desc = "Fotografía de marca personal en Orlando para dueños de negocio, realtors y emprendedores. Fotos para tu web, redes y anuncios, con sesión en español."
write_es("es/fotografia-de-marca-orlando/", "Fotografía de marca personal en Orlando · GLPX Studio", marca_desc, marca,
         service_ld("Fotografía de marca personal en Orlando", marca_desc, "es/fotografia-de-marca-orlando/") + faq_ld(br_faq))

# ================================================================== FOTOS PROFESIONALES
hs_frames = [
    frame("hs-01.jpg", "Hombre con lentes, traje azul marino y corbata a rayas", "Ejecutivo", "01"),
    frame("hs-17.jpg", "Mujer sonriente con blusa de lunares", "Profesional", "04"),
    frame("hs-03.jpg", "Mujer con vestido lavanda y brazos cruzados", "LinkedIn", "07", pick=True),
    frame("headshot-2.jpg", "Doctora sonriente con bata blanca y brazos cruzados", "Salud", "10"),
    frame("hs-green.jpg", "Mujer sonriente con blazer verde", "Profesional", "13"),
    frame("hs-redtop.jpg", "Mujer sonriente de cabello rizado con blusa roja", "Profesional", "16"),
    frame("hs-16.jpg", "Joven con blazer azul marino y camisa blanca", "LinkedIn", "19"),
    frame("jestic-jesus.jpg", "Barbero sonriente con barba y polo gris de su barbería", "Equipo", "22"),
    frame("hs-10.jpg", "Barbero con polo blanco de su marca", "Negocio", "25"),
]
hs_faq = [
    ("¿Qué es un headshot?", "Es una foto profesional de los hombros hacia arriba, con buena luz y un fondo limpio. Es la foto que usas en LinkedIn, en la web de tu empresa, en tu tarjeta de presentación y en tus perfiles."),
    ("No sé posar. ¿Es un problema?", "Para nada. Casi nadie sabe. Te digo exactamente cómo pararte, dónde poner las manos y hacia dónde mirar, y te enseño las fotos durante la sesión para que veas cómo van saliendo."),
    ("¿Cuánto dura la sesión?", "Una sesión individual suele tomar menos de una hora. Si quieres varios looks o fondos, o si es un equipo completo, lo planeamos en la llamada."),
    ("¿Qué ropa me pongo?", "Colores sólidos, un saco o blazer que te quede bien y una segunda opción para variar. Evita logos y estampados llamativos."),
    ("¿Van a la oficina para fotos de todo el equipo?", "Sí. Monto el estudio en tu oficina o negocio, y todo el equipo sale con la misma luz y el mismo fondo, sin que nadie pierda el día."),
    ("¿Cuánto cuesta?", "Depende de cuántas personas y cuántos looks necesitas. Cuéntame en una llamada rápida y te mando la cotización en menos de 24 horas."),
]
fotos = f'''  <section class="page-hero page-hero--ink">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Fotos profesionales y headshots · Orlando, FL</p>
        <h1>Una foto que <em>abre puertas.</em></h1>
        <p class="lede">Fotos profesionales en Orlando para LinkedIn, tu empresa, tu negocio o tu perfil de actor. Te dirijo en español en cada pose, así que no necesitas saber posar, y el retoque es natural: sigues siendo tú.</p>
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

  <section class="section">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Por qué importa</p>
        <h2>Tu foto llega antes que tú.</h2>
      </div>
      <div>
        <p>Un reclutador, un cliente nuevo o un director de casting ve tu foto antes de leer una sola palabra sobre ti. Una foto oscura, recortada de una fiesta o de hace diez años hace que duden. Una foto profesional dice que te tomas en serio tu trabajo.</p>
        <p>Si estás buscando trabajo, cambiando de carrera o empezando tu propio negocio en Orlando, es una de las mejoras más rápidas que puedes hacer.</p>
        <div><a class="btn btn--red" href="blog/foto-perfil-linkedin/">Guía: foto de perfil para LinkedIn</a></div>
      </div>
    </div>
  </section>

  <section class="section dark" id="galeria">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Fotos recientes</p>
        <h2>Profesionales de todo tipo. Nadie se ve tieso.</h2>
      </div>
      {sheet(hs_frames, ["GLPX STUDIO", "FOTOS PROFESIONALES", "▸ ORLANDO"], "sheet--3")}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Para cada profesión</p><h2>¿Para qué la necesitas?</h2></div>
      <div class="steps" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr))">
        <div class="step"><h3>LinkedIn y empleo</h3><p>Una foto clara y cercana para buscar trabajo o crecer en tu carrera.</p></div>
        <div class="step"><h3>Realtors y seguros</h3><p>Para tus tarjetas, letreros, anuncios y tu perfil en las plataformas.</p></div>
        <div class="step"><h3>Abogados y salud</h3><p>Fotos que transmiten confianza para tu web y tus directorios profesionales.</p></div>
        <div class="step"><h3>Actores</h3><p>Un look comercial y uno teatral, con retoque natural para casting.</p></div>
        <div class="step"><h3>Equipos completos</h3><p>Fotos iguales para toda la empresa, tomadas en tu oficina.</p></div>
      </div>
    </div>
  </section>

  <section class="section cream">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Qué ponerte</p>
        <h2>Lo simple funciona.</h2>
        <ul class="ticks">
          <li><span>Colores sólidos</span><span>Sí</span></li>
          <li><span>Saco o blazer que te quede bien</span><span>Sí</span></li>
          <li><span>Una segunda blusa o camisa</span><span>Tráela</span></li>
          <li><span>Logos y estampados llamativos</span><span>Evítalos</span></li>
          <li><span>Maquillaje y peinado</span><span>Opcional</span></li>
        </ul>
      </div>
      <div>
        <p class="eyebrow">Precio</p>
        <h2>Pide tu cotización.</h2>
        <p>El precio depende de cuántas personas y cuántos looks necesitas. Cuéntame en una llamada rápida y te mando la cotización en menos de 24 horas. ¿Necesitas más fotos para tu negocio? Mira la <a href="es/fotografia-de-marca-orlando/">sesión de marca personal</a>.</p>
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

{related("es/fotos-profesionales-orlando/")}{closer_es("Es hora de cambiar <em>esa foto.</em>")}'''
fotos_desc = "Fotos profesionales y headshots en Orlando para LinkedIn, empresas, realtors, abogados y actores. Te dirijo en español y el retoque es natural."
write_es("es/fotos-profesionales-orlando/", "Fotos profesionales y headshots en Orlando · GLPX Studio", fotos_desc, fotos,
         service_ld("Fotos profesionales y headshots en Orlando", fotos_desc, "es/fotos-profesionales-orlando/") + faq_ld(hs_faq))

# ================================================================== ARTISTAS Y MÚSICA
ed_frames = [
    frame("ed-greensuit.jpg", "Artista con traje verde cruzado apoyado en una pared de madera", "Música", "01"),
    frame("ed-08.jpg", "Artista con lentes de sol frente a una pared de bocinas", "Música", "04", pick=True),
    frame("ed-09.jpg", "Artista con lentes de sol y cadena de oro sobre fondo gris", "Música", "07"),
    frame("ed-hero.jpg", "Mujer con rosas rojas frente a un fondo rojo intenso", "Belleza", "10"),
    frame("ed-10.jpg", "Artista con camiseta amarilla y gorra verde frente a un fondo verde", "Música", "13"),
    frame("ed-navy.jpg", "Modelo rubia con chaqueta azul marino y guantes largos de cuero", "Moda", "16"),
    frame("ed-bw.jpg", "Retrato editorial en blanco y negro", "Editorial", "19"),
    frame("ed-07.jpg", "Modelo con traje amplio color salvia frente a un degradado morado", "Moda", "22"),
    frame("ed-12.jpg", "Retrato de belleza con accesorios de perlas sobre fondo rosado", "Belleza", "25"),
]
ed_faq = [
    ("¿Hacen portadas de álbum y sencillos?", "Sí. He hecho portadas para Alex Rose (El Nuevo Rockstar y Oversized) y Anuel AA (Las Leyendas Nunca Mueren). Planeamos la idea, el vestuario y el set para que la portada funcione en Spotify, Apple Music y redes."),
    ("¿Cuánto tiempo antes del lanzamiento hago la sesión?", "Lo ideal es varias semanas antes de la fecha, para tener la portada lista para el pre-save y contenido para anunciar el lanzamiento. Mándame la fecha y armamos el calendario desde ahí."),
    ("¿Qué incluye una sesión para artistas?", "Tú eliges el tiempo: medio día (hasta 5 horas y 3 cambios de set) o día completo (hasta 10 horas y cambios ilimitados). Las fotos editadas se agregan por imagen, así que solo pagas por las que vas a usar."),
    ("¿También hacen video?", "Sí. Puedes agregar fotos detrás de cámaras, un reel de 30 a 60 segundos o un paquete de contenido con 2 reels y 15 fotos detrás de cámaras."),
    ("¿Puedo traer mi equipo creativo?", "Claro. Puedes traer a tu estilista, maquillista o director creativo, o agregar los míos a la producción."),
]
artistas = f'''  <section class="page-hero page-hero--black">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Fotógrafo para artistas · Orlando, FL</p>
        <h1>Portadas que <em>suenan a tu música.</em></h1>
        <p class="lede">Fotógrafo para artistas en Orlando: portadas de álbum y sencillos, fotos de prensa y contenido para tu lanzamiento. Con créditos en portadas de Alex Rose y Anuel AA, y dirección creativa en español.</p>
        <div class="hero-actions">
          <a class="btn btn--red" href="{BOOKING}">Planea tu sesión</a>
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
    <span>Portada · <b>El Nuevo Rockstar</b></span><span>Portada · <b>Oversized</b></span><span>Portada · <b>Las Leyendas Nunca Mueren</b></span><span><b>8+</b> años en set</span>
  </div></div>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Tu lanzamiento</p>
        <h2>Una sola sesión para todo el lanzamiento.</h2>
        <p>Un lanzamiento necesita más que la portada. Lo planeamos completo para que no te quedes sin contenido a mitad de la promoción.</p>
      </div>
      <div class="steps">
        <div class="step"><h3>La portada</h3><p>La imagen del álbum o sencillo, pensada para verse bien en tamaño miniatura.</p></div>
        <div class="step"><h3>Fotos de prensa</h3><p>Para medios, playlists, flyers de shows y tu EPK.</p></div>
        <div class="step"><h3>Contenido vertical</h3><p>Fotos y reels para anunciar la fecha en Instagram y TikTok.</p></div>
        <div class="step"><h3>Detrás de cámaras</h3><p>El material que mantiene a tus fans pendientes después del estreno.</p></div>
      </div>
      <p style="margin-top:24px"><a class="btn btn--red" href="blog/contenido-lanzamiento-musical/">Guía: contenido para un lanzamiento musical</a></p>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Trabajo con artistas</p><h2>Color, actitud y una idea detrás de cada foto.</h2></div>
      {sheet(ed_frames, ["GLPX STUDIO", "ARTISTAS", "▸ ORLANDO"], "sheet--3")}
    </div>
  </section>

  <section class="section cream" id="tarifas">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Tarifas</p>
        <h2>Reservas el tiempo. Eliges las fotos.</h2>
        <p>La tarifa cubre la fotografía. Las fotos editadas se agregan por imagen, así solo pagas por las que vas a usar. Cada sesión se cotiza después de una llamada gratis.</p>
      </div>
      <div class="price-row">
        <article class="price">
          <h3>Medio día</h3>
          <ul><li>Hasta 5 horas en set</li><li>Hasta 3 cambios de set o locación</li><li>Portadas, sencillos y fotos de prensa</li></ul>
        </article>
        <article class="price price--feature">
          <span class="tag">Producción completa</span>
          <h3>Día completo</h3>
          <ul><li>Hasta 10 horas</li><li>Cambios de locación ilimitados</li><li>Traslado incluido hasta 1 hora de Orlando</li><li>Álbumes, campañas y producciones grandes</li></ul>
        </article>
      </div>
      <div class="price-group" style="margin-top:56px">
        <p class="eyebrow">Agrega a la producción</p>
        <div class="addons">
          <div><span>Dirección creativa</span><b>Opcional</b></div>
          <div><span>Maquillaje y peinado</span><b>Opcional</b></div>
          <div><span>Fotos detrás de cámaras · 10 fotos</span><b>Opcional</b></div>
          <div><span>Reel · 30–60 seg</span><b>Opcional</b></div>
          <div><span>Paquete de contenido · 2 reels + 15 fotos</span><b>Opcional</b></div>
        </div>
        <p class="terms">Un depósito del 50 % aparta tu fecha · el resto se paga el día de la sesión</p>
      </div>
    </div>
  </section>

{reviews_es(["gabriel", "charlyn"], "Creativos sobre trabajar con GLPX.")}
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Preguntas frecuentes</p><h2>Antes de tu sesión.</h2></div>
      {faq(ed_faq)}
    </div>
  </section>

{related("es/fotografo-musica-artistas-orlando/")}{closer_es("¿Ya tienes <em>fecha de lanzamiento?</em>", "Mándame la fecha y la idea. Armamos la sesión alrededor de eso.")}'''
art_desc = "Fotógrafo para artistas en Orlando: portadas de álbum, fotos de prensa y contenido para tu lanzamiento. Portadas para Alex Rose y Anuel AA."
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
    ("¿Qué tipo de eventos cubren?", "Conferencias, convenciones, galas, premiaciones, fiestas de fin de año, lanzamientos y eventos de organizaciones y cámaras de comercio, desde salones de hotel hasta el Orange County Convention Center."),
    ("¿Por qué un fotógrafo bilingüe?", "Porque en muchos eventos de Orlando se habla español e inglés. Puedo coordinar con los organizadores, dirigir fotos de grupo y hablar con invitados en el idioma que prefieran, sin intermediarios."),
    ("¿Pueden tomar headshots en el evento?", "Sí. Un set sencillo de headshots permite que asistentes o empleados se lleven una foto profesional entre sesiones. Es un buen detalle para patrocinadores y miembros."),
    ("¿Cuánto tiempo de cobertura necesito?", "Medio día cubre hasta 5 horas: oradores, público, detalles y fotos espontáneas. Día completo cubre hasta 10 horas, varios salones o locaciones, e incluye traslado hasta 1 hora de Orlando."),
    ("¿Hacen video del evento?", "Sí. Puedes agregar un video resumen del evento a cualquier cobertura."),
    ("¿Cómo aparto la fecha?", "Con un depósito del 50 %. Antes del evento revisamos el programa para no perder ningún momento clave."),
]
eventos = f'''  <section class="page-hero page-hero--ink">
    <div class="wrap">
      <div class="hero-copy">
        <p class="eyebrow">Fotografía de eventos corporativos · Orlando, FL</p>
        <h1>Tu evento, <em>en los dos idiomas.</em></h1>
        <p class="lede">Fotógrafo bilingüe para conferencias, galas y fiestas de empresa en Orlando. Coordino con tu equipo en español o en inglés, me muevo en el salón sin estorbar y cubro el programa completo.</p>
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

  <section class="section">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Para quién</p>
        <h2>Eventos donde la comunidad se reúne.</h2>
      </div>
      <div>
        <ul class="ticks">
          <li><span>Conferencias y convenciones</span><span>Hoteles y centros de convenciones</span></li>
          <li><span>Galas y premiaciones</span><span>Organizaciones y fundaciones</span></li>
          <li><span>Cámaras de comercio y networking</span><span>Grupos empresariales</span></li>
          <li><span>Fiestas de fin de año</span><span>Empresas y equipos</span></li>
          <li><span>Lanzamientos y activaciones</span><span>Marcas</span></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Trabajo reciente</p><h2>Oradores, público y los momentos entre sesiones.</h2></div>
      {sheet(ev_frames, ["GLPX STUDIO", "EVENTOS", "▸ ORLANDO"], "sheet--3")}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Qué te entrego</p><h2>Fotos para cada persona que las necesita.</h2></div>
      <div class="steps">
        <div class="step"><h3>Para tus redes</h3><p>Las mejores fotos del día, listas para publicar mientras el evento sigue en la conversación.</p></div>
        <div class="step"><h3>Para patrocinadores</h3><p>Fotos de sus logos, stands y participación, para mostrarles el valor de su apoyo.</p></div>
        <div class="step"><h3>Para prensa</h3><p>Oradores y momentos clave con calidad para medios y comunicados.</p></div>
        <div class="step"><h3>Para el próximo año</h3><p>Un archivo completo para promocionar la siguiente edición.</p></div>
      </div>
    </div>
  </section>

  <section class="section cream" id="cobertura">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Cobertura</p><h2>Una cotización hecha para tu evento.</h2></div>
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
      <p class="terms">Agrega headshots en el evento o un video resumen · Cobertura en español e inglés · Un depósito del 50 % aparta tu fecha</p>
    </div>
  </section>

{reviews_es(["charlyn", "gabriel"], "Lo que dicen los clientes.")}
  <section class="section">
    <div class="wrap">
      <div class="section-head"><p class="eyebrow">Preguntas frecuentes</p><h2>Eventos en Orlando.</h2></div>
      {faq(ev_faq)}
    </div>
  </section>

{related("es/fotografia-eventos-corporativos-orlando/")}{closer_es("Cuéntame de tu <em>evento.</em>", "Mándame la fecha, el lugar y el programa. Te envío una cotización en menos de 24 horas.")}'''
ev_desc = "Fotógrafo bilingüe para eventos corporativos en Orlando: conferencias, galas, fiestas de empresa y lanzamientos. Cobertura en español e inglés."
write_es("es/fotografia-eventos-corporativos-orlando/", "Fotografía de eventos corporativos en Orlando · GLPX Studio", ev_desc, eventos,
         service_ld("Fotografía de eventos corporativos en Orlando", ev_desc, "es/fotografia-eventos-corporativos-orlando/") + faq_ld(ev_faq))

# ------------------------------------------------------------------ sitemap
sm = (ROOT / "sitemap.xml").read_text()
add = "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in PAGES if f"{SITE}{u}<" not in sm)
(ROOT / "sitemap.xml").write_text(sm.replace("</urlset>", add + "</urlset>"))
print("spanish pages:", len(PAGES))
