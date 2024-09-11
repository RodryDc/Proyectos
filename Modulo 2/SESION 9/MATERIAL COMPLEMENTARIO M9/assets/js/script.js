var tareas = [
    { tarea: "Pintar la fachada de la casa" },
    { tarea: "Comprar comida para el perro" },
    { tarea: "Pagar la tarjeta de crédito" },
];

// Función para renderizar las tareas en la tabla
function renderizarTareas() {
    const cuerpoTabla = document.getElementById("cuerpo-tabla");
    cuerpoTabla.innerHTML = ""; // Limpiar la tabla antes de renderizar

    tareas.forEach((item, index) => {
        const nuevaFila = document.createElement("tr");
        git;
        // Crear la celda de la tarea
        const tareaCelda = document.createElement("td");
        tareaCelda.textContent = item.tarea;
        nuevaFila.appendChild(tareaCelda);

        // Crear la celda del botón "Finalizar"
        const accionCelda = document.createElement("td");
        const finalizarBoton = document.createElement("button");
        finalizarBoton.textContent = "Finalizar";
        finalizarBoton.classList.add("btn", "btn-danger");

        // Agregar el evento de clic al botón "Finalizar"
        finalizarBoton.addEventListener("click", function () {
            tareas.splice(index, 1); // Eliminar la tarea del array
            renderizarTareas(); // Volver a renderizar la lista
        });

        accionCelda.appendChild(finalizarBoton);
        nuevaFila.appendChild(accionCelda);

        // Agregar la nueva fila a la tabla
        cuerpoTabla.appendChild(nuevaFila);
    });
}

// Renderizar las tareas iniciales al cargar la página
renderizarTareas();

// Evento para mostrar/ocultar el formulario de agregar tarea
document.querySelector(".btn-success").addEventListener("click", function () {
    const formulario = document.getElementById("formulario");
    if (
        formulario.style.display === "none" ||
        formulario.style.display === ""
    ) {
        formulario.style.display = "block";
    } else {
        formulario.style.display = "none";
    }
});

// Agregar nueva tarea al hacer clic en "Agregar"
document.querySelector(".btn-primary").addEventListener("click", function () {
    const tareaInput = document.getElementById("nuevaTarea");
    const tareaTexto = tareaInput.value.trim();

    if (tareaTexto !== "") {
        // Agregar la nueva tarea al array de tareas
        tareas.push({ tarea: tareaTexto });

        // Volver a renderizar la lista de tareas
        renderizarTareas();

        // Limpiar el input
        tareaInput.value = "";

        // Ocultar el formulario nuevamente después de agregar la tarea
        document.getElementById("formulario").style.display = "none";
    }
});
