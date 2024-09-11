var opcion = prompt(
    "¡Hola! Soy Eva, tu asistente virtual del Servicio al Cliente de Mentel. Estoy aquí para ayudarte en lo que necesides.\nEscribe el número de la opción que buscas: \n1.- Boletas y Pagos \n2.- Señal y llamadas \n3.- Oferta comercial  \n4.- Otras consultas"
);

//FUNCIONES

switch (opcion) {
    case "1":
        var opcion1 = prompt(
            "Seleccione una opción: \n 1.- Ver Boleta \n 2.- Pagar cuenta"
        );
        if (opcion1 == "1") {
            alert("Haga click aquí para decargar su boleta");
        } else if (opcion1 == "2") {
            alert("Usted está siendo transferido. Espere por favor...");
        }
        break;
    case "2":
        var opcion2 = prompt(
            "Seleccione una opción: \n 1.- Problemas con la señal \n 2.- Problemas con las llamadas"
        );
        if (opcion2 == "1" || opcion2 == "2") {
            var solicitud = prompt("A continuación escriba su solicitud:");
            alert(
                "Estimado usuario, su solicitud: '" +
                    solicitud +
                    "' Ha sido enviada con exito. Pronto será contactado por uno de nuestros ejecutivos"
            );
        }
        break;
    case "3":
        var opcion3 = prompt(
            "¡Mentel tiene una oferta comercial acorde a tus necesidades! \n Para conocer más información y ser asesorado personalmente por un ejecutivo escribe 'SI' y un ejecutivo te llamará. De lo contratio ingrese 'NO'"
        );
        if (opcion3 == "SI") {
            alert("El ejecutivo contactará con usted");
        } else if (opcion3 == "NO") {
            alert("Gracias por preferir nuestros servicios");
        }
        break;
    case "4":
        var consulta = prompt("A continuación escriba su consulta:");
        alert(
            "Estimado usuario, su consulta: '" +
                consulta +
                "' Ha sido ingresada con exito. Pronto será contactado por uno de nuestros ejecutivos"
        );
        break;
    default:
        alert(
            "La opción ingresada no es válida. Gracias por preferir nuestros servicios"
        );
        break;
}
