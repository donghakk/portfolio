// Progressive enhancement: the complete portfolio stays visible without JS.
(() => {
  const links = [...document.querySelectorAll('.top nav a')];
  const targets = links.map(link => document.getElementById(link.hash.slice(1))).filter(Boolean);
  let queued = false;
  function updateNavigation() {
    const threshold = document.querySelector('.top').getBoundingClientRect().bottom + 60;
    let current = targets[0];
    for (const section of targets) {
      if (section.getBoundingClientRect().top <= threshold) current = section;
    }
    for (const link of links) {
      if (link.hash === `#${current.id}`) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    }
    queued = false;
  }
  function scheduleUpdate() {
    if (!queued) { queued = true; requestAnimationFrame(updateNavigation); }
  }
  window.addEventListener('scroll', scheduleUpdate, { passive: true });
  window.addEventListener('resize', scheduleUpdate, { passive: true });
  window.addEventListener('pageshow', scheduleUpdate);
  updateNavigation();
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.add('entered');
        observer.unobserve(entry.target);
      }
    }, { threshold: 0.12 });
    document.querySelectorAll('.case-heading, .index>div>a, .gallery, .lp-videos').forEach(el => observer.observe(el));
  }
})();
