// Ara's website: three small jobs.
// 1. Old links ended in #pl when both languages shared a page; send them to the Polish page.
(function () {
  if (location.hash === "#pl" && !location.pathname.startsWith("/pl")) {
    var p = location.pathname.replace(/\/index\.html$/, "/").replace(/\.html$/, "");
    location.replace("/pl" + (p === "/" ? "/" : p));
  }
})();

// 2. "What's in Ara": as each feature reaches the middle of the screen, the phone shows its screen.
document.addEventListener("DOMContentLoaded", function () {
  var walk = document.querySelector(".walk");
  if (!walk || !("IntersectionObserver" in window)) return;
  document.documentElement.classList.add("js");
  var steps = walk.querySelectorAll(".step");
  var shots = walk.querySelectorAll(".shot");
  var ticks = walk.querySelectorAll(".ticks i");
  var stack = walk.querySelector(".stack");
  function show(i) {
    walk.dataset.active = i;
    steps.forEach(function (s, k) { s.classList.toggle("is-active", k === i); });
    shots.forEach(function (s, k) { s.classList.toggle("on", k === i); });
    ticks.forEach(function (s, k) { s.classList.toggle("on", k === i); });
    if (stack && shots[i]) stack.style.setProperty("--glow", shots[i].style.getPropertyValue("--c"));
  }
  show(0);
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) show(+e.target.dataset.step); });
  }, { rootMargin: "-45% 0px -45% 0px" });
  steps.forEach(function (s) { io.observe(s); });
});

// 3. The theme switch: Light, Automatic (follows the device) or Dark, remembered on this device.
// The colours follow data-theme on <html> (style.css); the app screenshots are <picture>s whose
// dark version is chosen by the <source>'s media, so that is pointed at the choice too.
(function () {
  var root = document.documentElement;
  function saved() {
    try { var t = localStorage.getItem("ara-theme"); return t === "light" || t === "dark" ? t : "system"; }
    catch (e) { return "system"; }
  }
  function apply(choice) {
    if (choice === "system") root.removeAttribute("data-theme"); else root.setAttribute("data-theme", choice);
    var media = choice === "dark" ? "all" : choice === "light" ? "not all" : "(prefers-color-scheme: dark)";
    document.querySelectorAll("picture source[srcset*='-dark.']").forEach(function (s) { s.media = media; });
    document.querySelectorAll("[data-theme-choice]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.themeChoice === choice));
    });
  }
  document.addEventListener("DOMContentLoaded", function () {
    apply(saved());
    document.querySelectorAll("[data-theme-choice]").forEach(function (b) {
      b.addEventListener("click", function () {
        var choice = b.dataset.themeChoice;
        try { if (choice === "system") localStorage.removeItem("ara-theme"); else localStorage.setItem("ara-theme", choice); }
        catch (e) {}
        apply(choice);
      });
    });
  });
})();
