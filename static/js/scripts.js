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

/*Chatbot Blip*/
(function () {
  window.onload = function () {
      new BlipChat()
          .withAppKey('ZWF6eWNhcjE6YmJiYzg4ODktYjFhYS00OGJiLTk3N2UtNTc3MzM5Y2EyNDZi')
          .withButton({"color":"#0096fa","icon":""})
          .withCustomCommonUrl('https://ryan-melo-rlnqk.chat.blip.ai/')
          .build();
  }
})(); 