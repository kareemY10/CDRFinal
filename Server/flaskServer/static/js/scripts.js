
$(document).ready(function(){

$('form[name=signup_form').submit(function (e){
    var $form=$(this);
    var data=$form.serialize();
    e.preventDefault();
    $('#loader').show();
    $('#signupform').hide();



    $.ajax({

        url:"/users/signup",
        type:"POST",
        data: data,
        dataType:"json",
        success:function(resp){
            console.log(resp);

        },
        error:function(resp){
            console.log(resp)
        }


    }



    )

});
});


