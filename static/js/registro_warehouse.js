// Obtener el campo de entrada, botón y contenedor de checkbox
const inputMostrar = document.getElementById('input-mostrar');
const botonMostrar = document.getElementById('boton-mostrar');
const checkboxContenedor = document.getElementById('checkbox-contenedor');

// Obtener las casillas de verificación y contenedores de formularios
const formulario1Casilla = document.getElementById('formulario1-casilla');
const formulario2Casilla = document.getElementById('formulario2-casilla');
const formulario1Contenedor = document.getElementById('formulario1-contenedor');
const formulario2Contenedor = document.getElementById('formulario2-contenedor');

// Función para actualizar la visibilidad de los formularios
function actualizarFormularios() {
    formulario1Contenedor.style.display = formulario1Casilla.checked ? 'block' : 'none';
    formulario2Contenedor.style.display = formulario2Casilla.checked ? 'block' : 'none';
}

// Evento para el botón de búsqueda
botonMostrar.addEventListener('click', () => {
    // Si no hay checkboxes seleccionados, ocultar los formularios
    if (!formulario1Casilla.checked && !formulario2Casilla.checked) {
        formulario1Contenedor.style.display = 'none';
        formulario2Contenedor.style.display = 'none';
        // alert('Por favor, seleccione al menos un formulario.');
        return;
    }

    // Si hay checkboxes seleccionados, mostrar los formularios
    actualizarFormularios();
});

// Agregar listeners de eventos a las casillas de verificación
formulario1Casilla.addEventListener('change', () => {
    if (formulario2Casilla.checked) {
        formulario2Casilla.checked = false;
        formulario2Contenedor.style.display = 'none';
    }
    if (formulario1Casilla.checked) {
        formulario1Contenedor.style.display = 'block';
        console.log("validación de formulario 1");
    } else {
        formulario1Contenedor.style.display = 'none';
    }
});

formulario2Casilla.addEventListener('change', () => {
    if (formulario1Casilla.checked) {
        formulario1Casilla.checked = false;
        formulario1Contenedor.style.display = 'none';
    }
    if (formulario2Casilla.checked) {
        formulario2Contenedor.style.display = 'block';
        console.log("validación de formulario 2");
    } else {
        formulario2Contenedor.style.display = 'none';
    }
});
 // Obtener los botones de envío de los formularios
 const enviarFormulario1 = document.getElementById('enviar-formulario1');
 const enviarFormulario2 = document.getElementById('enviar-formulario2');

  // Agregar listeners de eventos a los botones de envío
  enviarFormulario1.addEventListener('click', validateFormulario1);
  // enviarFormulario2.addEventListener('click', validateFormulario2);
 

  // Función para validar el Formulario 1
  function validateFormulario1(event) {
    event.preventDefault(); // Prevent the form from submitting
    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('Apellido').value;
    const correo = document.getElementById('correo').value;
    const correo_axi = document.getElementById('correo_axi').value;
    const telefono = document.getElementById('telefono').value;
    const telefono_axi = document.getElementById('telefono_axi').value;
  
   
    
    // Validate the inputs using regular expressions
    const nombreRegex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{2,}$/; // Allow letters, spaces, and accents
    const apellidoRegex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{2,}$/; // Allow letters, spaces, and accents
    const cedulaRegex = /^\d{7,10}$/; // Allow 7-10 digits
    const correoRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/; // Allow valid email addresses
    const telefonoRegex = /^\d{7,10}$/; // Allow 7-10 digits
  
    if (!nombreRegex.test(nombre)) {
      Swal.fire({
        title: 'Error',
        text: 'Por favor, ingrese un nombre válido',
        icon: 'error',
      });
      return;
    }
    if (!apellidoRegex.test(apellido)) {
      Swal.fire({
        title: 'Error',
        text: 'Por favor, ingrese un apellido válido',
        icon: 'error',
      });
      return;
    }
    // if (!cedulaRegex.test(cedula)) {
    //   console.log(cedula)
    //   Swal.fire({
    //     title: 'Error',
    //     text: 'Por favor, ingrese una cédula válida',
    //     icon: 'error',
    //   });
    //   return;
    // }
    if (!correoRegex.test(correo)) {
      Swal.fire({
        title: 'Error',
        text: 'Por favor, ingrese un correo electrónico válido',
        icon: 'error',
      });
      return;
    }
    if (!correoRegex.test(correo_axi)) {
      Swal.fire({
        title: 'Error',
        text: 'Por favor, ingrese un correo electrónico auxiliar válido',
        icon: 'error',
      });
      return;
    }
    if (!telefonoRegex.test(telefono)) {
      Swal.fire({
        title: 'Error',
        text: 'Por favor, ingrese un teléfono válido',
        icon: 'error',
      });
      return;
    }
    if (!telefonoRegex.test(telefono_axi)) {
      Swal.fire({
        title: 'Error',
        text: 'Por favor, ingrese un teléfono auxiliar válido',
        icon: 'error',
      });
      return;
    }
    const formElement = document.getElementById('formulario1');

// Crea un objeto FormData a partir del formulario
const formData = new FormData(formElement)
console.log(" existe el formData")
console.log(formData)
    const opciones = {
      method: 'POST',
      headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'X-CSRFToken': csrfToken,
      },
      body: formData
    };
    
    console.log("Entró en el formData y el bucle");
    console.log(formData);
    
    // Imprimir las entradas de formData
    for (var pair of formData.entries()) {
      console.log(pair[0] + ': ' + pair[1]);
    }
    
    // No vuelvas a declarar 'opciones', simplemente usa la ya creada
    fetch(urlpararegistrarcliente, opciones)
      .then(response => response.json())
      .then(data => {
        console.log(data);
        // datos del registro_cliente
        const registroCliente = data.datos;
        console.log(registroCliente);
        // acciones con los datos
        Swal.fire({
          title: 'Éxito',
          text: 'Cliente registrado con éxito',
          icon: 'success',
        });
      })
      .catch(error => console.error(error));
    }
