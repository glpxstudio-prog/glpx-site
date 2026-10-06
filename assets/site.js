// GLPX Studio — gallery lightbox. Click any photo in a contact sheet to view it large.
(function () {
  var frames = Array.prototype.slice.call(document.querySelectorAll('.sheet .frame'));
  if (!frames.length) return;
  var catNames = { 'branding.html': 'Branding', 'headshots.html': 'Headshots', 'editorial.html': 'Editorial & Music' };
  var lb = document.createElement('div');
  lb.className = 'lb'; lb.hidden = true;
  lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', 'Photo viewer');
  lb.innerHTML = '<div class="lb-stage"><button class="lb-close" type="button">Close ✕</button>' +
    '<button class="lb-btn lb-prev" type="button" aria-label="Previous photo">‹</button>' +
    '<img alt=""><button class="lb-btn lb-next" type="button" aria-label="Next photo">›</button></div>' +
    '<div class="lb-bar"><span class="lb-cap"></span><span class="lb-count"></span><a class="lb-link" hidden></a></div>';
  document.body.appendChild(lb);
  var img = lb.querySelector('img'), cap = lb.querySelector('.lb-cap'), count = lb.querySelector('.lb-count'), link = lb.querySelector('.lb-link');
  var i = 0, lastFocus = null;

  function show(n) {
    i = (n + frames.length) % frames.length;
    var f = frames[i], src = f.querySelector('img');
    img.src = src.getAttribute('src'); img.alt = src.alt;
    var label = f.querySelector('figcaption span'), num = f.querySelector('figcaption b');
    cap.innerHTML = (label ? label.textContent : '') + (num ? ' &nbsp;<b>' + num.textContent + '</b>' : '');
    count.textContent = (i + 1) + ' / ' + frames.length;
    var href = f.getAttribute('href');
    if (href && catNames[href]) { link.href = href; link.textContent = 'See more ' + catNames[href] + ' →'; link.hidden = false; }
    else { link.hidden = true; }
  }
  function open(n) { lastFocus = document.activeElement; show(n); lb.hidden = false; document.body.style.overflow = 'hidden'; lb.querySelector('.lb-close').focus(); }
  function close() { lb.hidden = true; document.body.style.overflow = ''; if (lastFocus) lastFocus.focus(); }

  frames.forEach(function (f, n) {
    if (f.tagName !== 'A') { f.tabIndex = 0; f.setAttribute('role', 'button'); }
    f.addEventListener('click', function (e) { e.preventDefault(); open(n); });
    f.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(n); } });
  });
  lb.querySelector('.lb-prev').addEventListener('click', function () { show(i - 1); });
  lb.querySelector('.lb-next').addEventListener('click', function () { show(i + 1); });
  lb.querySelector('.lb-close').addEventListener('click', close);
  lb.addEventListener('click', function (e) { if (e.target === lb || e.target.classList.contains('lb-stage')) close(); });
  document.addEventListener('keydown', function (e) {
    if (lb.hidden) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') show(i - 1);
    else if (e.key === 'ArrowRight') show(i + 1);
  });
  var x0 = null;
  lb.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener('touchend', function (e) {
    if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 50) show(dx < 0 ? i + 1 : i - 1); x0 = null;
  });
})();

/* Phones: show the first 6 photos of long galleries, with a button to see the rest */
(function () {
  if (!window.matchMedia('(max-width: 760px)').matches) return;
  document.querySelectorAll('.sheet').forEach(function (sheet) {
    var frames = sheet.querySelectorAll('.frame');
    if (frames.length <= 8) return;
    sheet.classList.add('is-collapsed');
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'btn btn--ghost sheet-more';
    btn.textContent = 'See all ' + frames.length + ' photos';
    btn.addEventListener('click', function () { sheet.classList.remove('is-collapsed'); btn.remove(); });
    sheet.insertAdjacentElement('afterend', btn);
  });
})();
