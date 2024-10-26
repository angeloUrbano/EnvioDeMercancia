
// Obtener el campo de entrada, botón y contenedor de checkbox
const inputMostrar = document.getElementById('input-mostrar');
const botonMostrar = document.getElementById('boton-mostrar');
const checkboxContenedor = document.getElementById('checkbox-contenedor');

// Obtener las casillas de verificación y contenedores de formularios
const formulario1Casilla = document.getElementById('formulario1-casilla');
const formulario2Casilla = document.getElementById('formulario2-casilla');
const formulario1Contenedor = document.getElementById('formulario1-contenedor');
const formulario2Contenedor = document.getElementById('formulario2-contenedor');

// Agregar listeners de eventos a las casillas de verificación
formulario1Casilla.addEventListener('change', () => {
 if (formulario2Casilla.checked) {
   formulario2Casilla.checked = false;
   formulario2Contenedor.style.display = 'none';
   cedula.value= inputMostrar.value
   cedula.disabled = true
   

 }
 if (formulario1Casilla.checked) {
   formulario1Contenedor.style.display = 'block';
   cedula.value= inputMostrar.value
   cedula.disabled = true
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


