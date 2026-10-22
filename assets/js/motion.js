(() => {
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (!Element.prototype.animate) return;

  const active = new Set();
  const revealed = new WeakSet();
  let observer;

  const animate = (element, frames, options) => {
    const animation = element.animate(frames, options);
    active.add(animation);
    const cleanup = () => active.delete(animation);
    animation.finished.then(cleanup, cleanup);
  };

  const configure = () => {
    observer?.disconnect();
    if (preference.matches) {
      active.forEach(animation => animation.cancel());
      return;
    }
    if (!('IntersectionObserver' in window)) return;
    observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        observer.unobserve(entry.target);
        revealed.add(entry.target);
        animate(entry.target, [
          { opacity: .8, transform: 'translateY(10px)' },
          { opacity: 1, transform: 'translateY(0)' },
        ], { duration: 440, easing: 'cubic-bezier(.16, 1, .3, 1)' });
      });
    }, { threshold: .08, rootMargin: '0px 0px -20px 0px' });

    document.querySelectorAll([
      '.home-work > .work-entry', '.home-practice', '.home-notes', '.home-contact',
      '.portfolio-grid > article', '.journal-entry', '.journal-article > h2',
      '.site-interior .w > h2',
    ].join(',')).forEach(element => {
      if (!revealed.has(element)) observer.observe(element);
    });
  };

  document.addEventListener('click', event => {
    if (preference.matches || !(event.target instanceof Element)) return;
    const control = event.target.closest('a, button');
    if (!control) return;
    // Native links, downloads, focus, and modifier-click behavior remain intact.
    animate(control, [{ opacity: .65 }, { opacity: 1 }], {
      duration: 180, easing: 'ease-out',
    });
  });
  preference.addEventListener('change', configure);
  configure();
})();
