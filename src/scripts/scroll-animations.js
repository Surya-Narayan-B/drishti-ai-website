document.addEventListener('astro:page-load', () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1, // Trigger when 10% of the element is visible
  });

  const elementsToAnimate = document.querySelectorAll('.scroll-animate');
  elementsToAnimate.forEach((el) => observer.observe(el));
});