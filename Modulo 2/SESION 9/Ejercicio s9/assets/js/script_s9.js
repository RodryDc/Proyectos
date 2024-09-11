/*document.addEventListener("DOMContentLoaded", function () {
    const text1 = document.getElementById("text1");
    const text2 = document.getElementById("text2");
    const caja2 = document.getElementById("caja2");
    const img = caja2.querySelector("img");
    const caja3 = document.getElementById("caja3");

    text1.addEventListener("mouseover", function () {
        text2.style.display = "block";
    });

    text1.addEventListener("mouseout", function () {
        text2.style.display = "none";
    });

    caja2.addEventListener("click", function () {
        img.classList.toggle("large");
    });

    caja3.addEventListener("dblclick", function () {
        caja3.classList.toggle("large-text");
    });
});
*/

function mostrarmensaje() {
    document.getElementById("text2").style.display = "block";
}
function ocultarmensaje() {
    document.getElementById("text2").style.display = "none";
}

function aumentarimagen() {
    document.getElementById("img").style.width = "100%";
}

function disminuirimagen() {
    document.getElementById("img").style.width = "20%";
}

function aumentartexto() {
    document.getElementById("caja3").style.fontSize = "2em";
}
