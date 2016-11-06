$(window).load(function(){
    $(".photo_gallery").click(function(){
        $("#myModal").css("display","block");
        var img_src = $(this).attr('src');
          $("#img01").attr("src",img_src);
      });
});
