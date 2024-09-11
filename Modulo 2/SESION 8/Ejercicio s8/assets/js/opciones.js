var opcion = prompt(
    "Vamos al grano. Elige una opción: \n 1. La primera? \n 2. La segunda? \n 3. La tercera? \n 4. La cuarta? \n 5. Salir"
);
while (opcion != "5") {
    switch (opcion) {
        case "1":
            alert("Elegiste la primera");
            break;
        case "2":
            alert("Elegiste la segunda");
            break;
        case "3":
            alert("Elegiste la tercera");
            break;
        case "4":
            alert("Elegiste la cuarta");
            break;
        case "5":
            alert("Hasta luego");
            break;
        default:
            alert("Opcion no valida");
    }
    opcion = prompt(
        "Vamos al grano. Elige una función: \n 1. Elijo la primera? \n 2. La segunda? \n 3. La tercera? \n 4. La cuarta? \n 5. Salir"
    );
}
