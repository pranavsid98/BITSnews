$("#toshow").hide();
$('#toshow1').hide();
$(window).load(function() {
		// Animate loader off screen
		$(".se-pre-con").fadeOut("slow");;
	});
// // $('body').click(function(evt){    
// //        if(evt.target.id == "toshow")
// //           return;
// //       if($(evt.target).closest('#toshow').length)
// //           return;
// //       if(evt.target.id == "map") {
// //       	$("#toshow").show();
// //       }
// //       else           
// //        $("#toshow").hide();

// // });

// // var reply_clicked = function (clicked_id) 
// // {
// // 	$('body').click(function(evt){    
// //        if(evt.target.id == "toshow1")
// //           return;
// //       if($(evt.target).closest('#toshow1').length)
// //           return;
// //       if(evt.target.id == clicked_id) {
// //       	$("#toshow1").show();
// //       	$(document).getElementById("event-zoom").src = $(document).getElementById(clicked_id).src;
// //       }
// //       else           
// //        $("#toshow1").hide();

// // });
// // };


var on_clicked = function  (id) {
	// body...
	var div = document.createElement("div");
	div.id = "temp";
	div.style.zIndex = "100";
	div.style.left = "0px";
	div.style.top = "0px";
	div.style.position = "fixed";
	div.style.width = "100%";
	div.style.textAlign = "center";
	div.style.verticalAlign = "middle";
	div.style.height = "100%";
	div.style.backgroundColor = "rgba(0, 0, 0, 0.8)";

	var img = document.createElement("img");
	img.src = document.getElementById(id).src;
	img.className = "image-temp";

	div.appendChild(img);
	div.onclick = function(){
		document.body.removeChild(this);
	};
	document.body.appendChild(div);

}

// $('#temp').click(function(){
// 	$('#temp').remove();
// });
