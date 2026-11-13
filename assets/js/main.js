// Mobile menu, testimonial slider and footer year.
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    // Fit the open mobile menu between the header and the fixed bottom action bar,
    // so it scrolls on its own and its last item is never hidden.
    var actionBar = document.querySelector('.action-bar');
    var fitMenu = function () {
      if (!nav.classList.contains('is-open')) return;
      var bar = actionBar && getComputedStyle(actionBar).display !== 'none' ? actionBar.offsetHeight : 0;
      nav.style.maxHeight = (window.innerHeight - bar - nav.getBoundingClientRect().top) + 'px';
    };
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (open) { fitMenu(); } else { nav.style.maxHeight = ''; }
    });
    window.addEventListener('resize', fitMenu);
    window.addEventListener('scroll', fitMenu, { passive: true });

    // Mobile: tap the arrow to expand About / Services sub-pages.
    Array.prototype.forEach.call(nav.querySelectorAll('.sub-toggle'), function (btn) {
      btn.addEventListener('click', function () {
        var item = btn.parentNode;
        var open = item.classList.toggle('is-open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        btn.setAttribute('aria-label', btn.getAttribute('aria-label').replace(open ? 'Show' : 'Hide', open ? 'Hide' : 'Show'));
      });
    });
  }

  var reviews = Array.prototype.slice.call(document.querySelectorAll('.review'));
  if (reviews.length) {
    var current = 0;
    var timer;
    var show = function (i) {
      reviews[current].classList.remove('is-active');
      current = (i + reviews.length) % reviews.length;
      reviews[current].classList.add('is-active');
    };
    var restart = function () {
      clearInterval(timer);
      if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        timer = setInterval(function () { show(current + 1); }, 7000);
      }
    };
    document.querySelector('[data-review="prev"]').addEventListener('click', function () { show(current - 1); restart(); });
    document.querySelector('[data-review="next"]').addEventListener('click', function () { show(current + 1); restart(); });
    restart();
  }

  // Hero background video: pause/play button, and stay still for reduced-motion users.
  var video = document.querySelector('.hero__video');
  var vToggle = document.querySelector('.hero__toggle');
  if (video && vToggle) {
    var setPaused = function (paused) {
      if (paused) { video.pause(); } else { var p = video.play(); if (p && p.catch) p.catch(function () {}); }
      vToggle.classList.toggle('is-paused', paused);
      vToggle.setAttribute('aria-label', paused ? 'Play background video' : 'Pause background video');
    };
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) setPaused(true);
    vToggle.addEventListener('click', function () { setPaused(!video.paused); });
  }

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
