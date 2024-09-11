$(document).ready(function() {
    
    $('#text1').hover(
        function() { 
            $('#text2').show();
        },
        function() { 
            $('#text2').hide();
        }
    );

    
    $('#caja2').on('click', function() {
        $('#img').css('width', '100%'); 
    });

    $('#caja2').on('mouseleave', function() {
        $('#img').css('width', '20%'); 
    });

    
    $('#caja3').on('dblclick', function() {
        $(this).css('font-size', '2em'); 
    });
});
