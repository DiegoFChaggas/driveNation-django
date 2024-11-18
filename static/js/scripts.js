/*Slide home*/
let count = 1;
document.getElementById("radio1").checked = true;

setInterval(function () {
  nextImage();
}, 4000);

function nextImage() {
  count++;
  if (count > 2) {
    count = 1;
  }

  document.getElementById("radio" + count).checked = true;
}
/*Fim Slide Home*/ 