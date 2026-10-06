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

EXTRA.update({
    "windermere": dict(
        plan="Windermere sessions usually lean elevated and calm. Many clients shoot at their own home or a listing they represent, then add a few waterfront portraits on the Butler Chain of Lakes for a relaxed luxury feel.",
        light="The hour before sunset on the water is the best light in Windermere. Indoors, we bring lighting so a home or office looks bright and warm.",
        logistics="Home and listing sessions are scheduled with you ahead of time. Historic downtown Windermere is small and walkable, with easy parking near Main Street.",
        svc=dict(
            branding="Windermere branding suits luxury realtors, executives and private practices who need images that feel as polished as the homes and clients they work with.",
            headshots="Windermere headshots can be shot at your home or office, or in a studio in Orlando if you want a classic backdrop.",
            editorial="Waterfront docks, open lawns and elegant interiors give Windermere editorial shoots a quiet, high end look.",
            events="Windermere events at private estates and clubs call for discreet coverage that captures guests without getting in the way.",
        )),
    "thornton-park": dict(
        plan="Thornton Park is where I'm based, so sessions here are easy to plan. We walk the brick streets under the oaks, step into a cafe for lifestyle shots, and finish by Lake Eola if you want a skyline in the frame.",
        light="The oak canopy keeps light soft for most of the day. Lake Eola is a short walk away for golden hour.",
        logistics="Street parking is tight on weekends, so weekday mornings are the easiest. Everything is within a short walk, so outfit changes stay quick.",
        svc=dict(
            branding="Thornton Park branding suits creatives, small business owners and coaches who want a local, lived in feel.",
            headshots="Thornton Park headshots can be shot outdoors under the oaks for a soft look, or in a studio in Orlando a few minutes away.",
            editorial="Brick, shade and sidewalk cafes give Thornton Park editorial shoots an easy, cinematic city feel.",
            events="Thornton Park and nearby downtown restaurants and lofts work well for smaller company gatherings with relaxed, candid coverage.",
        )),
    "lake-eola": dict(
        plan="A Lake Eola session puts Orlando in the frame. We usually start at the fountain early, move around the lakeside loop for variety, and use the amphitheater and the downtown skyline for full length portraits.",
        light="Early morning is the best time, with soft light and fewer people. Golden hour works beautifully too, with the skyline glowing behind you.",
        logistics="The park is busiest on weekends and evenings. We meet near a downtown garage and walk the loop, so you can keep spare outfits close.",
        svc=dict(
            branding="Lake Eola branding is perfect for founders, realtors and artists who want their photos to say Orlando at a glance.",
            headshots="Lake Eola headshots give you an outdoor option with soft skyline in the background, great for LinkedIn and speaker bios.",
            editorial="The fountain, swan boats and amphitheater give Lake Eola editorial shoots an iconic, recognizable setting.",
            events="Downtown hotels and venues around Lake Eola host company events, with outdoor group photos by the lake if you want them.",
        )),
    "winter-garden": dict(
        plan="Winter Garden sessions feel local and real. We usually shoot inside your shop, cafe or studio space first, then step out to Plant Street for storefront and walking shots.",
        light="Morning light on Plant Street is soft and even. The downtown pavilion and the West Orange Trail offer shade on bright afternoons.",
        logistics="Plant Street has public parking nearby, and weekday mornings avoid the weekend crowds and farmers market traffic.",
        svc=dict(
            branding="Winter Garden branding suits boutique and cafe owners, makers and realtors who want photos that feel like their community.",
            headshots="Winter Garden headshots can be shot on site at your business or in a studio in Orlando for a classic look.",
            editorial="Historic storefronts and brick along Plant Street give Winter Garden editorial shoots a warm, small town character.",
            events="Winter Garden event halls, breweries and restaurants host company gatherings that call for candid, relaxed coverage.",
        )),
    "altamonte-springs": dict(
        plan="Altamonte Springs clients often need a mix of polished and practical: team headshots on site at the office, plus a few bright outdoor portraits around Cranes Roost Park.",
        light="The boardwalk at Cranes Roost looks best in the morning or late afternoon. Indoors, we bring lighting for consistent results.",
        logistics="Uptown Altamonte has easy parking. On site team sessions run on a simple schedule so nobody loses much of the workday.",
        svc=dict(
            branding="Altamonte Springs branding suits medical practices, insurance and finance pros who need trustworthy images for a website and social media.",
            headshots="Altamonte Springs team headshots are shot on site with a consistent backdrop, so every bio on your website matches.",
            editorial="The lake, boardwalk and modern buildings around Cranes Roost give editorial shoots bright, clean backdrops.",
            events="Hotel conference rooms and event space around Uptown and Cranes Roost host company events with coverage of speakers and guests.",
        )),
    "sanford": dict(
        plan="Sanford has real character, so we use it. Sessions often start inside your restaurant, brewery or shop, then move to First Street murals and the riverwalk on Lake Monroe for open, bright portraits.",
        light="The riverwalk is beautiful at sunset. First Street's brick and storefronts photograph well in morning shade.",
        logistics="Downtown Sanford is walkable with street parking. We plan around your business hours so customers aren't interrupted.",
        svc=dict(
            branding="Sanford branding suits restaurant and brewery owners, makers and artists who want images with personality.",
            headshots="Sanford headshots can be shot at your business or in a studio in Orlando, with an outdoor option on the riverwalk.",
            editorial="Murals, brick and Lake Monroe views give Sanford editorial shoots a creative, textured feel.",
            events="Historic downtown venues and breweries in Sanford host company events that suit candid, story driven coverage.",
        )),
    "oviedo": dict(
        plan="Oviedo sessions are usually fresh and modern. Clients near UCF often want a clean headshot plus a few lifestyle frames around Center Lake Park or Oviedo on the Park.",
        light="Center Lake Park looks best in the morning or late afternoon, with water and open sky behind you.",
        logistics="Parking at Oviedo on the Park is easy, and the park, paths and amphitheater are all close together.",
        svc=dict(
            branding="Oviedo branding suits founders, coaches and local business owners who want a modern, approachable look.",
            headshots="Oviedo headshots are popular with UCF grads, researchers and young professionals updating LinkedIn.",
            editorial="The amphitheater and lakeside paths at Center Lake Park give Oviedo editorial shoots open, modern backdrops.",
            events="Oviedo community venues and nearby hotels host smaller company events with relaxed coverage.",
        )),
    "celebration": dict(
        plan="Celebration makes polished photos easy. Market Street storefronts work for lifestyle branding, and the lakefront and tree lined streets give you calm, timeless portraits.",
        light="Mornings by the lakefront are soft and quiet. Market Street has shade from the buildings most of the day.",
        logistics="The town center is compact and walkable, with public parking close to Market Street.",
        svc=dict(
            branding="Celebration branding suits realtors, wellness pros and family run businesses who want a clean, bright look.",
            headshots="Celebration headshots can be shot outdoors in town or in a studio in Orlando for a classic backdrop.",
            editorial="Classic architecture and the lakefront give Celebration editorial shoots a timeless, storybook feel.",
            events="Celebration and the nearby resort area host company events at hotels and venues, with coverage planned around your schedule.",
        )),
})
