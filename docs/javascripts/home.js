// Relógio UTC do hero da página inicial.
// Usa document$ do Material para funcionar com navigation.instant.
(function () {
  var timer = null;

  function doisDigitos(n) {
    return n < 10 ? "0" + n : "" + n;
  }

  function iniciar() {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }

    var hora = document.querySelector("[data-vb-utc]");
    var data = document.querySelector("[data-vb-data]");
    if (!hora) return;

    var meses = (document.documentElement.lang || "pt").indexOf("en") === 0
      ? ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
      : ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"];

    function atualizar() {
      var d = new Date();
      hora.textContent =
        doisDigitos(d.getUTCHours()) + ":" +
        doisDigitos(d.getUTCMinutes()) + ":" +
        doisDigitos(d.getUTCSeconds()) + "Z";
      if (data) {
        data.textContent = doisDigitos(d.getUTCDate()) + " " + meses[d.getUTCMonth()] + " " + d.getUTCFullYear();
      }
    }

    atualizar();
    timer = setInterval(atualizar, 1000);
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(iniciar);
  } else {
    document.addEventListener("DOMContentLoaded", iniciar);
  }
})();
