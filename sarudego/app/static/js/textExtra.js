var delay = 0;
var lines = $(".highLight div").length;
var line = 0;
$(".highLight div").each(function(){
   var count = $(this).text().length;
   var duration = count / 12;
   $(this).css({
    "-webkit-animation" : "typing " + duration + "s steps(" + count + ", end) forwards, blink 1s step-end 1s infinite",
    "-moz-animation" : "typing " + duration + "s steps(" + count + ", end) forwards, blink 1s step-end 1s infinite",
    "animation-delay" : delay + "s"});
   var that = $(this);
   setTimeout(function(){
       that.css('opacity', '1');
   },delay*1000);
   delay += duration;
   line += 1;
   if(line != lines)
   {
       setTimeout(function(){
           that.css('border-right', '0');
       },delay*1000);
   }
});

