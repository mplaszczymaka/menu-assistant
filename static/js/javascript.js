// $('button').click(function() {
//     if ($('.basket').attr('display') == 'none') {
//         $('.basket').attr('display', 'block');
//     } else {
//         $('.basket').attr('display', 'none');
//     }
// });

// $('button').click(function() {
//     if ($('.basket').hide()) {
//         $('.basket').show();
//     } else {
//         $('.basket').hide();
//     }
// });

$(".basket-btn").click(function(){
    $(".basket").toggle();
  });