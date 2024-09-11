// Arrays o arreglos

let miArreglo = ["Pedro","Juan","Diego"];

console.log("Mi arreglo tiene "+ miArreglo.length +" elementos")

console.log("El segundo elemento de mi arreglo es: "+ miArreglo[1])

miArreglo.push("Ignacio")

console.log(miArreglo)

miArreglo.pop()

console.log(miArreglo)


//Objetos
let miAuto = {
    color:"rojo",
    marca:"nissan",
    modelo:"versa"
}

console.log(miAuto.marca)

miAuto.año = 2020

console.log(miAuto)


let arregloNumeros = []

//condición inicial; condición final; incremento
for(let i = 0; i < 10; i++){
    console.log(i);
    arregloNumeros.push(i);
}

console.log(arregloNumeros)

//iterador en iterable
for(posicion in miArreglo){
    console.log(posicion);
    console.log(miArreglo[posicion]);
}

for(atributo in miAuto){
    console.log(atributo)
    console.log(miAuto[atributo])
}

for (element in miAuto) {
    console.log(`${element}: ${miAuto[element]}`);
    console.log(element+" : "+miAuto[element]);
}

function miFuncion(num1,num2){
    return num1+num2
}

