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
            swal("Opss !", "Character limit exceeded !", "info");
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