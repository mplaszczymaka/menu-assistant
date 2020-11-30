// (".basket-btn").click(function(){
//     $(".basket").toggle();
//   });

function openSimilar() {
    var el = document.getElementById('similar');
    if (el.style.display == 'block') {
        el.style.display = 'none';
    } else {
        el.style.display = 'block';
    }
}