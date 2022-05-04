window.addEventListener("DOMContentLoaded", (event) => {
  registerModal();
});

function registerModal() {
  var elems = document.getElementById("add-course");
  var instances = M.Modal.init(elems);
  document
    .getElementById("add-course-card")
    .addEventListener("click", function () {
      instances.open();
    });
}
