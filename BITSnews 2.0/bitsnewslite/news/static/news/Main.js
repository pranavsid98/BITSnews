$(document).ready(function(){
  function ticker() {
      $('#ticker1 li:first').slideUp(function() {
          $(this).appendTo($('#ticker1')).slideDown();
      });
  }

  setInterval(function(){ ticker(); }, 3000);
});
