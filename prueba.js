var contador = 1;
var time;
var on = false;
var seconds = 0;


var startTime = function(){
seconds++;
time = setTimeout("startTime()",1000);
 if(seconds >= 10){
 on = false;
 clearTimeout(time);

 }

document.getElementById("segundos").value = seconds;
}


function cambiar()
{

  if(seconds >= 10){
    document.getElementById('contador').innerHTML = contador + 0;
  }else{
document.getElementById('contador').innerHTML = contador += 1;
  }

}
function nuevo()
{
  document.getElementById('contador').innerHTML = contador = 0;
  on = true;
  startTime();
   seconds = 0;
}
