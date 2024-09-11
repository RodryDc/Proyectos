$(document).ready(function() {
    $(".text-body-secondary").click(function() {
      var idBoton = $("#Rio").attr("id");
      $("#detalles" + idBoton).toggle();
    });


    $(".btn-close").click(function() {
        $(".detalles").show();
    });
  });