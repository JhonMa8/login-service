document.addEventListener("DOMContentLoaded", function () {
    const role = localStorage.getItem("role");
    const roleSpan = document.getElementById("userRole");

    if (!role) {
        roleSpan.textContent = "Desconocido";
        alert("No se detectó el rol. Redirigiendo al login.");
        window.location.href = "index.html";
        return;
    }

    roleSpan.textContent = role;

    switch (role) {
        case "admin":
            document.getElementById("menuAdmin").style.display = "block";
            break;
        case "jefe":
            document.getElementById("menuJefe").style.display = "block";
            break;
        case "tecnico":
            document.getElementById("menuTecnico").style.display = "block";
            break;
        case "botanico":
            document.getElementById("menuBotanico").style.display = "block";
            break;
        default:
            roleSpan.textContent = "Rol no reconocido. Contacta al administrador.";
            break;
    }
});
