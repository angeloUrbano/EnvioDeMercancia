<<<<<<< HEAD


function eliminate_elements() {
  const divContainer = document.getElementById('divcontainer');
  const contenedorRegisterMerchandise = document.getElementById('contenedorRegisterMerchandise');

  console.log("Se está intentando eliminar elementos");

  for (let i = divContainer.children.length - 1; i >= 0; i--) {
    if (divContainer.children[i] !== contenedorRegisterMerchandise) {
      divContainer.removeChild(divContainer.children[i]);
      console.log("Se está intentando eliminar elementos");
    }
  }
}


function save_merchandise(data  , urlSaveMerchandise){



  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
  const csrftoken = getCookie('csrftoken');




    Options={
      method: 'POST',
      headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'X-CSRFToken': csrftoken,
        'Content-Type': 'application/x-www-form-urlencoded' // Agrega este header
      },
      body:"prueba"
    }

    fetch(urlSaveMerchandise , Options)
    .then(
      response => response.json()
     ).then(
      alert("prueba")
     )

    

    .catch()

}

// Obtener el campo de entrada, botón y contenedor de checkbox
=======
 // Obtener el campo de entrada, botón y contenedor de checkbox
>>>>>>> main
 const inputMostrar = document.getElementById('input-mostrar');
 const botonMostrar = document.getElementById('boton-mostrar');
 const checkboxContenedor = document.getElementById('checkbox-contenedor');

<<<<<<< HEAD
=======
 // Agregar listener de evento al botón
 botonMostrar.addEventListener('click', () => {
   // Mostrar el contenedor de checkbox si el campo de entrada no está vacío
   if (inputMostrar.value !== '') {
     checkboxContenedor.style.display = 'block';
   } else {
     alert('Por favor, ingrese un valor en el campo de entrada');
   }
 });

>>>>>>> main
 // Obtener las casillas de verificación y contenedores de formularios
 const formulario1Casilla = document.getElementById('formulario1-casilla');
 const formulario2Casilla = document.getElementById('formulario2-casilla');
 const formulario1Contenedor = document.getElementById('formulario1-contenedor');
 const formulario2Contenedor = document.getElementById('formulario2-contenedor');

 // Agregar listeners de eventos a las casillas de verificación
 formulario1Casilla.addEventListener('change', () => {
<<<<<<< HEAD
  if (formulario2Casilla.checked) {
    formulario2Casilla.checked = false;
    formulario2Contenedor.style.display = 'none';
  }
  if (formulario1Casilla.checked) {
    formulario1Contenedor.style.display = 'block';
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
  } else {
    formulario2Contenedor.style.display = 'none';
  }
});
=======
   if (formulario1Casilla.checked) {
     formulario1Contenedor.style.display = 'block';
   } else {
     formulario1Contenedor.style.display = 'none';
   }
 });

 formulario2Casilla.addEventListener('change', () => {
   if (formulario2Casilla.checked) {
     formulario2Contenedor.style.display = 'block';
   } else {
     formulario2Contenedor.style.display = 'none';
   }
 });
>>>>>>> main

 // Obtener los botones de envío de los formularios
 const enviarFormulario1 = document.getElementById('enviar-formulario1');
 const enviarFormulario2 = document.getElementById('enviar-formulario2');

 // Agregar listeners de eventos a los botones de envío
 enviarFormulario1.addEventListener('click', validateFormulario1);
 enviarFormulario2.addEventListener('click', validateFormulario2);

 // Función para validar el Formulario 1
 function validateFormulario1(event) {
   event.preventDefault(); // Prevent the form from submitting
   const nombre = document.getElementById('nombre').value;
   const apellido = document.getElementById('Apellido').value;
   const cedula = document.getElementById('cedula').value;
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
     alert('Por favor, ingrese un nombre válido');
     return;
   }
   if (!apellidoRegex.test(apellido)) {
     alert('Por favor, ingrese un apellido válido');
     return;
   }
   if (!cedulaRegex.test(cedula)) {
     alert('Por favor, ingrese una cédula válida');
     return;
   }
   if (!correoRegex.test(correo)) {
     alert('Por favor, ingrese un correo electrónico válido');
     return;
   }
   if (!correoRegex.test(correo_axi)) {
     alert('Por favor, ingrese un correo electrónico auxiliar válido');
     return;
   }
   if (!telefonoRegex.test(telefono)) {
     alert('Por favor, ingrese un teléfono válido');
     return;
   }
   if (!telefonoRegex.test(telefono_axi)) {
     alert('Por favor, ingrese un teléfono auxiliar válido');
     return;
   }

<<<<<<< HEAD
  // Peticion guardado de los datos
   const formData = new FormData()
    formData.append("nombre", nombre)
    formData.append("apellido", apellido)
    formData.append("cedula", cedula)
    formData.append("correo", correo)
    formData.append("correo_axi", correo_axi)
    formData.append("telefono", telefono)
    formData.append("telefono_axi", telefono_axi)

 console.log(" entro en el formData u el bucle")
   console.log(formData)
   for (var pair of formData.entries()) {
    console.log(pair[0] + ': ' + pair[1]);
  }
   const opciones = {
    method: 'POST',
    headers: {
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': csrfToken,
    },
    body: formData
  };
  fetch(urlpararegistrarcliente, opciones)
  .then(response => response.json())
  .then(data => {
    console.log(data);
    //  datos del registro_cliente
    const registroCliente = data.datos;
    console.log(registroCliente);
    //  aciones con los datos
    alert("paso por aqui prueba de angelo")
    alert("Cliente registrado con éxito");
    eliminate_elements()
    const contenedorRegisterMerchandise = document.getElementById('contenedorRegisterMerchandise');
    contenedorRegisterMerchandise.removeAttribute('hidden');
    console.log("se eliminaron los elementos")

    let prueba_de_envio =0
    save_merchandise( prueba_de_envio  , urlSaveMerchandise)

  })
  .catch(error => console.error(error));
   
=======
   // If all inputs are valid, submit the form
   formulario1.submit();
>>>>>>> main
 }

 // Función para validar el Formulario 2
 function validateFormulario2(event) {
   event.preventDefault(); // Prevent the form from submitting
   const correo = document.getElementById('correo').value;

   // Validate the input using a regular expression
   const correoRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/; // Allow valid email addresses

   if (!correoRegex.test(correo)) {
     alert('Por favor, ingrese un correo electrónico válido');
     return;
   }

<<<<<<< HEAD
   // falta validacioness

   //  peticion ajax de formulario2 

   enviarFormulario2.submit();
=======
   // If the input is valid, submit the form
   formulario2.submit();
>>>>>>> main
 }