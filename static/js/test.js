function startTime()
{
var today=new Date()
var h=today.getHours()
var m=today.getMinutes()
var s=today.getSeconds()

m=checkTime(m)
s=checkTime(s)
document.getElementById('txt').innerHTML=h+":"+m+":"+s
t=setTimeout('startTime()',500)
}

function checkTime(i){
    if (i<10){
        i = "0" + i
    }
    
    return i

}

$(document).ready(function(){
	$(".turn_off").click(function(){
		$("body").css("background-color","black");
		$("p").css("color","white");
		$("h2").css("color","white");
		$(".img").hide("slow");
	});
	$(".turn_on").click(function(){
		$(".img").show("slow");
	});
});