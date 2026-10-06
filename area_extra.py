"""Extra, hand-written local content for the eight most important area pages.
Each area gets: a planning paragraph, best light, logistics, and one line per service
so the four service pages for the same area don't read alike."""

EXTRA = {
    "orlando": dict(
        plan="Most Orlando shoots start with one question: do you want the city in the frame or a clean studio look? Many clients do both. We start in a rented studio in Orlando for headshots and polished portraits, then spend the second half of the session outside where your work actually happens.",
        light="Early morning around Lake Eola and the last hour before sunset downtown. Midday sun is harsh, so studio time usually lands in the middle of the day.",
        logistics="Downtown garages on Central Boulevard and Pine Street make outfit changes easy. Weekday mornings are the quietest time for public spots.",
        svc=dict(
            branding="An Orlando branding session usually covers your website hero, a few LinkedIn options and a set of working shots, all from one planned shot list.",
            headshots="Orlando headshots are usually shot in a rented studio for consistent light, with an outdoor option if you want something warmer for social media.",
            editorial="For artists and creatives, Orlando's mix of murals in Mills 50, downtown architecture and studio sets gives an editorial shoot plenty of range in one day.",
            events="Orlando events range from hotel ballrooms to the Orange County Convention Center. Coverage is planned around your run of show so the key moments are never missed.",
        )),
    "winter-park": dict(
        plan="Winter Park works best when we lean into its character. Park Avenue for walking and working shots, Central Park for softer portraits, and a quiet side street for anything you want calm and simple.",
        light="Mornings on Park Avenue before the shops get busy, and late afternoon in Central Park when the oaks filter the light.",
        logistics="Street parking fills up on weekends, so weekday sessions are easier. The public garage near Park Avenue keeps outfits close by.",
        svc=dict(
            branding="Winter Park branding sessions suit boutique owners, realtors and wellness pros who want an upscale but approachable look, often with a coffee shop or storefront as a natural set.",
            headshots="For Winter Park headshots, we can shoot in a studio in Orlando or keep it outdoors under the oaks for a softer, more personal look.",
            editorial="Brick, arches around Rollins and shaded avenues give Winter Park editorial shoots a classic, magazine feel.",
            events="Winter Park company events are often hosted at boutique hotels and private spaces off Park Avenue, where discreet coverage matters.",
        )),
    "lake-nona": dict(
        plan="Lake Nona clients usually need images that feel current and credible. We plan around your workplace, whether that is a clinic, a lab or a startup office, and add a few outdoor frames around Town Center for variety.",
        light="Open, modern spaces here look best early in the day or in the soft hour before sunset. Glass buildings can reflect hard light at midday.",
        logistics="Town Center has easy parking. If we shoot inside a medical or research building, we confirm access and any privacy rules ahead of time.",
        svc=dict(
            branding="Lake Nona branding works well for doctors, founders and researchers who want a clean, modern look that matches their practice or company.",
            headshots="Lake Nona headshots are often for whole medical or tech teams, shot on a consistent backdrop so every bio on your website matches.",
            editorial="The architecture and public art around Lake Nona Town Center make a sharp, modern backdrop for editorial and fashion stories.",
            events="Lake Nona events range from medical conferences to company launches, with coverage that captures speakers, panels and networking.",
        )),
    "downtown-orlando": dict(
        plan="Downtown sessions move fast. Most clients want a polished office look plus a few frames with the city behind them, so we plan two or three nearby spots within a short walk.",
        light="Tall buildings create shade most of the day, which is great for portraits. The plaza around the Dr. Phillips Center gets beautiful light late in the afternoon.",
        logistics="We meet near a parking garage and walk between locations. If we shoot in your office, an early start avoids busy lobbies.",
        svc=dict(
            branding="Downtown branding sessions are ideal for attorneys, finance pros and founders who want to look established without looking stiff.",
            headshots="Downtown headshots often happen on site at your office, so a whole team can step out for a few minutes each.",
            editorial="Glass towers, brick on Church Street and the Dr. Phillips Center plaza give downtown editorial shoots a strong city feel.",
            events="Downtown events in hotel ballrooms, rooftops and the Dr. Phillips Center get coverage of speakers, guests and the details your team planned.",
        )),
    "dr-phillips": dict(
        plan="In Dr. Phillips, the business is usually the set. For restaurants and hospitality brands we plan around service hours, so we capture the dining room, the team and the food while it still looks like your place on a busy night.",
        light="Restaurants photograph best before opening, when we can control the light. Outdoor portraits work well in the shade of Dr. Phillips Community Park.",
        logistics="We schedule around your prep and service times. For offices along Sand Lake Road, an early session keeps the day moving.",
        svc=dict(
            branding="Dr. Phillips branding sessions suit restaurant owners, hospitality teams and executives who need images as polished as the places they run.",
            headshots="Dr. Phillips headshots are often for hospitality and office teams, shot on site so nobody has to leave work for long.",
            editorial="Upscale dining rooms and bars on Restaurant Row make striking sets for editorial and fashion work.",
            events="Dr. Phillips sits close to many resort hotels, so event coverage here often means conferences, galas and company dinners.",
        )),
    "baldwin-park": dict(
        plan="Baldwin Park suits a relaxed, approachable look. We usually pair a few frames around the Village Center with portraits by Lake Baldwin, so you get both a lifestyle feel and something calm and clean.",
        light="Late afternoon by Lake Baldwin is the best light of the day. Mornings work well for sidewalk and storefront shots.",
        logistics="Parking near the Village Center is straightforward, and the lake is a short drive or a longer walk away.",
        svc=dict(
            branding="Baldwin Park branding works well for realtors, coaches and wellness pros who want to feel friendly and trustworthy.",
            headshots="Baldwin Park headshots can be shot outdoors by the lake for a natural look, or in a studio in Orlando for a classic backdrop.",
            editorial="Lakefront light and clean village architecture give Baldwin Park editorial shoots a bright, easy feel.",
            events="Baldwin Park events are usually smaller gatherings at restaurants and community spaces, with relaxed, candid coverage.",
        )),
    "kissimmee": dict(
        plan="Kissimmee sessions often happen right at your business, whether that is a restaurant, a shop or an office, so customers see the real place. We add a few frames by Lake Toho for a warmer, open look. Sessions run in English or Spanish.",
        light="Sunrise and sunset at Lakefront Park are hard to beat. Inside your business, we bring lighting so the space looks its best at any time.",
        logistics="We plan around your opening hours so the shoot doesn't interrupt customers. Downtown Broadway has easy street parking.",
        svc=dict(
            branding="Kissimmee branding sessions suit Latino entrepreneurs, hospitality brands and local shops, in English or Spanish.",
            headshots="Kissimmee headshots are often for realtors and small teams, shot on site or in a studio in Orlando.",
            editorial="Lake Toho at golden hour and the older storefronts on Broadway give Kissimmee editorial shoots warmth and character.",
            events="Kissimmee is home to large resort and convention venues, and bilingual coverage helps when your guests speak Spanish.",
        )),
    "lake-mary": dict(
        plan="Lake Mary clients usually need consistency more than anything else. We set up one look for the whole team, often on site at your office, so every headshot on your website and LinkedIn matches.",
        light="Indoors we bring our own lighting for a consistent result. Outdoor portraits at Colonial TownPark look best in the morning or late afternoon.",
        logistics="On site team sessions run on a simple schedule, a few minutes per person, so nobody loses much of the workday.",
        svc=dict(
            branding="Lake Mary branding sessions suit consultants, executives and marketing teams who need a full set of images for a company website.",
            headshots="Lake Mary team headshots are shot on site with a consistent backdrop and lighting, so new hires can match the set later.",
            editorial="Colonial TownPark and the corporate campuses give Lake Mary editorial shoots clean, modern lines.",
            events="Lake Mary events at corporate campuses, hotels and the Lake Mary Events Center get coverage of speakers, awards and team moments.",
        )),
}
