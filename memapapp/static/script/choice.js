var index=0;

// reference lines 5-15, https://www.jianshu.com/p/f84b76b67e86
//change images
function ChangeImg() {
		index++;
		var a=document.getElementsByClassName("imgtop");
		if(index>=a.length) index=0;
		for(var i=0;i<a.length;i++){
			a[i].style.display='none';
		}
		a[index].style.display='block';
	}
// set interval to change images
setInterval(ChangeImg,2000);

// text filter
document.getElementById("tb4").onclick=function(){
	var area = document.querySelectorAll(".area")
	for(var i = 0;i < area.length;i++){
		area[i].style.color = '#ccc'
	}
	var bd4 = document.querySelectorAll(".TB4")
	for(var i = 0;i < bd4.length;i++){
		bd4[i].style.color = '#f00'
	}
}

document.getElementById("tb3").onclick=function(){
	var area = document.querySelectorAll(".area")
	for(var i = 0;i < area.length;i++){
		area[i].style.color = '#ccc'
	}
	var bd3 = document.querySelectorAll(".TB3")
	for(var i = 0;i < bd3.length;i++){
		bd3[i].style.color = '#f00'
	}
}

document.getElementById("gro").onclick=function(){
	var area = document.querySelectorAll(".area")
	for(var i = 0;i < area.length;i++){
			area[i].style.color = '#ccc'
		}
		var gro = document.querySelectorAll(".GRO")
		for(var i = 0;i < gro.length;i++){
			gro[i].style.color = '#f00'
		}
	}

document.getElementById("lib").onclick=function(){
	var area = document.querySelectorAll(".area")
	for(var i = 0;i < area.length;i++){
		area[i].style.color = '#ccc'
	}
	var lib = document.querySelectorAll(".LIB")
	for(var i = 0;i < lib.length;i++){
		lib[i].style.color = '#f00'
	}
}

// image filter
document.getElementById("imgtb4").onclick=function(){
	var area = document.querySelectorAll(".area")
	for(var i = 0;i < area.length;i++){
		area[i].style.color = '#ccc'
	}
	var bd4 = document.querySelectorAll(".TB4")
	for(var i = 0;i < bd4.length;i++){
		bd4[i].style.color = '#f00'
	}
}

document.getElementById("imgtb3").onclick=function(){
	var area = document.querySelectorAll(".area")
	for(var i = 0;i < area.length;i++){
		area[i].style.color = '#ccc'
	}
	var bd3 = document.querySelectorAll(".TB3")
	for(var i = 0;i < bd3.length;i++){
		bd3[i].style.color = '#f00'
	}
}

document.getElementById("imggro").onclick=function(){
	var area = document.querySelectorAll(".area")
	for(var i = 0;i < area.length;i++){
		area[i].style.color = '#ccc'
	}
	var gro = document.querySelectorAll(".GRO")
	for(var i = 0;i < gro.length;i++){
		gro[i].style.color = '#f00'
	}
}

document.getElementById("imglib").onclick=function(){
	var area = document.querySelectorAll(".area")
	for(var i = 0;i < area.length;i++){
		area[i].style.color = '#ccc'
	}
	var lib = document.querySelectorAll(".LIB")
	for(var i = 0;i < lib.length;i++){
		lib[i].style.color = '#f00'
	}
}