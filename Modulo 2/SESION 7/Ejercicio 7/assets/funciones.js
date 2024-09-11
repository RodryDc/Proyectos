var num1 = parseInt(prompt("Ingresa el primer numero: "));
var num2 = parseInt(prompt("Ingresa el segundo numero: "));

if (num1 > num2) {
    alert("El primer número " + num1 + " es mayor que el " + num2 + "");
} else if (num1 < num2) {
    alert("El segundo número " + num2 + " es mayor que el " + num1 + "");
} else {
    alert("Los números " + num1 + " y " + num2 + " son iguales");
}
