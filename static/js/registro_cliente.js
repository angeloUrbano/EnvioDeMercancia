 // Obtener el campo de entrada, botón y contenedor de checkbox
 const inputMostrar = document.getElementById('input-mostrar');
 const botonMostrar = document.getElementById('boton-mostrar');
 const checkboxContenedor = document.getElementById('checkbox-contenedor');

 // Agregar listener de evento al botón
 botonMostrar.addEventListener('click', () => {
   // Mostrar el contenedor de checkbox si el campo de entrada no está vacío
   if (inputMostrar.value !== '') {
     checkboxContenedor.style.display = 'block';
   } else {
     alert('Por favor, ingrese un valor en el campo de entrada');
   }
 });

 // Obtener las casillas de verificación y contenedores de formularios
 const formulario1Casilla = document.getElementById('formulario1-casilla');
 const formulario2Casilla = document.getElementById('formulario2-casilla');
 const formulario1Contenedor = document.getElementById('formulario1-contenedor');
 const formulario2Contenedor = document.getElementById('formulario2-contenedor');

 // Agregar listeners de eventos a las casillas de verificación
 formulario1Casilla.addEventListener('change', () => {
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

   // If all inputs are valid, submit the form
   formulario1.submit();
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

   // If the input is valid, submit the form
   formulario2.submit();
 }