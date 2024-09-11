$(document).ready(function(){

    $("h1").click(function(){

        $(this).css({
            "background-color":"red"
        })

    })

    $("h1").dblclick(function(){

        $("h1").css({
            "background-color":"brown"
        })

    })

    $("p").hover(function(){
        let atribId = $(this).attr("id");

        if(atribId==null || atribId==""){
            $(this).resize()
        }
        
    })

    $("#Enviar").click(function(){
        let nombre = $("#campo-nombre").val()
        let correo = $("#campo-correo").val()

        $("#p-nombre").text(nombre)
        $("#p-correo").text(correo)

        $("#campo-nombre").val("")
        $("#campo-correo").val("")
    })
})



