// Set the date we're counting down to
var endDate = new Date("May 15, 2023 09:30:00").getTime();
var startDate = new Date("September 5, 2022 09:30:00").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();
    
  // Find the distance between now and the count down date
  var distance = endDate - now;
  var exp = now - startDate;

  // Time calculations for days, hours, minutes and seconds
  // var lastDays = Math.floor(distance / (1000 * 60 * 60 * 24));
  var expDays = Math.floor(exp / (1000 * 60 * 60 * 24));
  var percent = Math.round((expDays / 247)*100);

  // document.getElementById("leftDay").innerHTML = lastDays + "일";
  document.getElementById("dday").innerHTML = "완전작전 "+ expDays + "일째";
  document.getElementById("percent").innerHTML = percent + "%";
  document.getElementById("per").value = percent;
 
  // If the count down is over, write some text 
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("dday").innerHTML = "EXPIRED";
  }
}, 1000);
