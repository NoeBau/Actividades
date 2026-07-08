function mostrarPassword(){
    const input = document.getElementById("password");

    if(input.type === "password"){
        input.type = "text";
    }else{
        input.type = "password";
    }
}

function iniciarSesion(){
    alert("Inicio de sesión en desarrollo");
}