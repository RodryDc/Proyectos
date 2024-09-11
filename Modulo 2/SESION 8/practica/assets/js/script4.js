for (i = 0; i < 10; i++) {
    console.log(i);
}

console.log("hasta aca termina el for");

let x = 10;

while (x < 10) {
    console.log(x);
    x++;
}

console.log("hasta aca termina el primer while");

let y = 0;
do {
    console.log(y);
    y += 5;
} while (y < 30);

console.log("hasta aca termina el do while");

try {
    funcionInventada();
} catch (error) {
    console.log(error.message);
} finally {
    console.log("mensaje despues del try catch");
}

do {
    var num1 = parseInt(prompt("Ingresa un numero menor que 10: "));
    console.log(num1);
    num1++;
    console.log(num1);
} while (num1 < 10);

try {
    //instrucciones
    console.log("hola");
} catch (error) {
    //instrucciones
    console.log(error);
} finally {
    console.log("hasta aca termina el try catch");
}

try {
    let edad = parseInt(prompt("Ingresa tu edad: "));
    if (edad < 0) {
        throw new Error("La edad no puede ser negativa");
    }
    console.log("Tu edad es: " + edad);
} catch (error) {
    console.log(error.message);
} finally {
    console.log("hasta aca termina el try catch");
}
