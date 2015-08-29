
$(document).ready(function () {
    $("#id_valor2").focusout(function(){
        var valor1 = $("#id_valor1");
        var valor2 = $(this);
        if(valor1.val() != "" && valor2.val() != ""){
            $.ajax({
                type: 'POST',
                url: 'soma',
                data: {
                    valor1: valor1.val(),
                    valor2: valor2.val(),
                },
                success: function(data){
                    $("#id_resultado").val(data.resultado)
                }
            });
        }
    });
})

