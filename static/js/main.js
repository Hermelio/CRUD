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

})
