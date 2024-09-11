var cliente1 = {
    nombre: "Patricia Torres",
    contraseña: "ptorres",
    saldo: 1000500,
};
var cliente2 = {
    nombre: "Juan Perez",
    contraseña: "jperez",
    saldo: 100000,
};
var cliente3 = {
    nombre: "Maria Lopez",
    contraseña: "mlopez",
    saldo: 30000,
};

function ingresar() {
    var id = prompt("Ingrese su nombre:");
    var clave = prompt("Ingrese su contraseña:");

    if (id == cliente1.nombre && clave == cliente1.contraseña) {
        alert("Bienvenid@ " + cliente1.nombre);
        var auxcliente = cliente1;
        menu(auxcliente);
    } else if (id == cliente2.nombre && clave == cliente2.contraseña) {
        alert("Bienvenid@ " + cliente2.nombre);
        var auxcliente = cliente2;
        menu(auxcliente);
    } else if (id == cliente3.nombre && clave == cliente3.contraseña) {
        alert("Bienvenid@ " + cliente3.nombre);
        var auxcliente = cliente3;
        menu(auxcliente);
    } else {
        alert("Credenciales incorrectas");
        ingresar();
    }
}

function menu(auxcliente) {
    var opcion = prompt(
        "Seleccione que desea hacer:\n1. Ver saldo\n2. Realizar giro\n3. Realizar depósito\n4. Salir"
    );
    while (opcion != "4") {
        switch (opcion) {
            case "1":
                alert(
                    "El saldo de " +
                        auxcliente.nombre +
                        " es: " +
                        auxcliente.saldo
                );
                break;
            case "2":
                var monto = parseInt(
                    prompt(
                        "Su saldo actual es: " +
                            auxcliente.saldo +
                            "\nIngrese el monto que desea girar"
                    )
                );
                if (auxcliente.saldo >= monto) {
                    auxcliente.saldo -= monto;
                    alert(
                        "Giro realizado. Su nuevo saldo es: " + auxcliente.saldo
                    );
                } else {
                    alert("Saldo insuficiente");
                }
                break;
            case "3":
                var monto = parseInt(
                    prompt(
                        "Su saldo actual es: " +
                            auxcliente.saldo +
                            "\nIngrese el monto que desea depositar"
                    )
                );
                auxcliente.saldo += monto;
                alert(
                    "Depósito realizado. Su nuevo saldo es: " + auxcliente.saldo
                );
                break;
            case "4":
                alert("Gracias por usar el cajero automatico");
                break;
            default:
                alert("Opcion no valida");
        }
        opcion = prompt(
            "Seleccione que desea hacer:\n1. Ver saldo\n2. Realizar giro\n3. Realizar depósito\n4. Salir"
        );
    }
}

ingresar();
