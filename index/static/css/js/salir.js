function salir() {
    // Realiza una solicitud AJAX para notificar al servidor sobre la acción de salida
    $.ajax({
        url: '{% url "salir" %}',  // Ajusta la URL según la configuración de tus URLs en Django
        type: 'GET',  // O 'POST' dependiendo de cómo manejes las solicitudes en tu vista
        success: function (data) {
            // La solicitud fue exitosa, puedes redirigir o realizar otras acciones según sea necesario
            window.location.href = 'control_soporte';  // Redirige al inicio después de salir
        },
        error: function (xhr, status, error) {
            console.error('Error al intentar salir:', error);
            // Manejar el error según tus necesidades
        }
    });
}
