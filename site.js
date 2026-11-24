// Ara's website: two small jobs.
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
