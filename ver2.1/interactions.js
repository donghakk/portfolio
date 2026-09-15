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
  // Native lazy loading starts far below the viewport. A live LP can take
  // focus during startup, pulling the parent page away from the introduction.
  // Start each embed only when its frame is actually visible to the reader.
  const frames = [...document.querySelectorAll('.lp-frame[data-src]')];
  function loadFrame(frame) {
    frame.loading = 'eager';
    frame.src = frame.dataset.src;
    frame.removeAttribute('data-src');
  }
  if ('IntersectionObserver' in window) {
    const embeds = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        embeds.unobserve(entry.target);
        loadFrame(entry.target);
      }
    }, { rootMargin: '0px', threshold: 0.01 });
    frames.forEach(frame => embeds.observe(frame));
  } else {
    // Preserve the same visibility condition on older browsers.
    function loadVisibleFrames() {
      for (const frame of frames) {
        const box = frame.getBoundingClientRect();
        if (frame.dataset.src && box.top < innerHeight && box.bottom > 0) loadFrame(frame);
      }
      if (frames.every(frame => !frame.dataset.src)) {
        window.removeEventListener('scroll', loadVisibleFrames);
        window.removeEventListener('resize', loadVisibleFrames);
      }
    }
    window.addEventListener('scroll', loadVisibleFrames, { passive: true });
    window.addEventListener('resize', loadVisibleFrames, { passive: true });
    loadVisibleFrames();
  }
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.add('entered');
        observer.unobserve(entry.target);
      }
    }, { threshold: 0.12 });
    document.querySelectorAll('.case-heading, .index>div>a, .gallery, .lp-embeds').forEach(el => observer.observe(el));
  }
})();
