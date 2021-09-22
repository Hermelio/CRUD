$(document).ready(function(){

$(".btn-novo").on("click", function(e){
  e.preventDefault();
  $(".caixa").show( 'slow' );
  var pos = $(".caixa").offset();
  $(document).scrollTop(pos.top);
})


$(".btn-cancelar").on('click', function(e){
  e.preventDefault();
  $(".caixa").hide( "slow" );
})

$(".btn-salvar").on("click", function(e){
  e.preventDefault();
  alertify.set('notifier','position', 'top-right');
  $(".caixa").hide( "slow" , function (){
    alertify.success("Cliente cadastrado com sucesso!");
  });
});





function validaCpf(cpf) {

	if (cpf.value.length !== 11 || cpf.value == '11111111111' || cpf.value == '22222222222' || cpf == '33333333333' ||
		cpf.value == '44444444444' || cpf.value == '55555555555' || cpf.value == '66666666666' ||
		cpf.value == '77777777777' || cpf.value == '88888888888' || cpf.value == '99999999999' ||
		cpf.value == '01234567890') {

		return false
	}

	resultado = 0;


	for (x = 0, contador = 10; contador >1; x++, contador--) {

		resultado += parseInt(cpf.value[x]) * contador;
	}


	digito_um = (resultado * 10) % 11


	resultado = 0;

	if (digito_um == parseInt(cpf.value[9])) {

	for (x = 0, contador=11; contador>1; x++,contador--) {
		resultado += parseInt(cpf.value[x]) * contador;
	}

	digito_dois = (resultado * 10) % 11;

	if (digito_dois == cpf.value[10]) {

		return true

	} else {

			return false
		}
	}


}


})
