/* All Script here it will extends to all the pages */

// Character remaining counter
$(document).ready(function () {
    var start = 0;
    var limit = 1000;

    $("#message").keyup(function(){ 
        start = this.value.length;
        if(start > limit){
            return false;
        }
        else if (start == limit){
            $("#remaining").html("Characters remaining: "+ (limit - start)).css('color', 'red');
            swal("Opsss !", "Character limit exceeded !", "info");
        }
        else if (start > 984){
            $("#remaining").html("Characters remaining: "+ (limit - start)).css('color', 'red');
        }
        else if (start < 1000){
            $("#remaining").html("Characters remaining: "+ (limit - start)).css('color', 'black');
        }
        else{
            $("#remaining").html("Characters remaining: "+ (limit - start)).css('color', 'black');
        }
    });
});

// Input mask (PHONE)
$(document).ready(function(){
    $(".phone").inputmask("(+237) 999-99-99-99",{"onincomplete": function(){
        swal("Opsss !", "Incomplete phone, Please review !", "success");
        $(".phone").val("");
        return false
    }})
})

// Get the TIME running at realtime
setInterval(function(){
    var date = new Date();
    $('#clock').html(
        (date.getHours < 10 ? '0' : '') + date.getHours() + ":" +
        (date.getMinutes < 10 ? '0' : '') + date.getMinutes() + ":" +
        (date.getSeconds < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);

// Update the page always at (0:00)
function autoRefresh(){
    var now = new Data(), then = new Data();
    then.setHours(hours, minutes, seconds, 0);
    if(then.getTime() < now.getTime()){
        then.setData(now.getDate() + 1);
    }
    var timeout = (then.getHours() - now.getTime());
    setTimeout(function(){
        window.location.reload(true);
    }, timeout);
}
autoRefresh(0,0,0)