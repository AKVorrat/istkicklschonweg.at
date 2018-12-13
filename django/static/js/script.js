document.addEventListener("DOMContentLoaded", function() {
  var lazyBackgrounds = [].slice.call(document.querySelectorAll(".shareable-image"));

  if ("IntersectionObserver" in window) {
    let lazyBackgroundObserver = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.style.backgroundImage = `url('${entry.target.parentElement.getAttribute('href')}')`;
          console.log(entry.target)
          lazyBackgroundObserver.unobserve(entry.target);
        }
      });
    });

    lazyBackgrounds.forEach(function(lazyBackground) {
      lazyBackground.style.display = 'block';
      lazyBackgroundObserver.observe(lazyBackground);
    });
  }
});
