// Boton de Contacto
document.getElementById("contactar").addEventListener("click", function () {
    var formulario = document.getElementById("formulario");

    if (formulario.style.display === "none") {
        formulario.style.display = "block";
    } else {
        formulario.style.display = "none";
    }
});

// Boton de Copiar Email
document.getElementById("copiar").addEventListener("click", function () {
    navigator.clipboard.writeText("rdc.1985@gmail.com");
});

// Animar habilidades
var habilidades = document.querySelectorAll(".habilidad");

habilidades.forEach(function (habilidad) {
    habilidad.addEventListener("mouseenter", function () {
        habilidad.style.transform = "scale(1.1) translateY(-10px)";
    });

    habilidad.addEventListener("mouseleave", function () {
        habilidad.style.transform = "scale(1) translateY(0)";
    });
});

// Boton flotante
function irAlTop() {
    window.scrollTo({ top: 0, behavior: "smooth" });
}
