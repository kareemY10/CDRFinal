
$(document).ready(function(){

    const btns=document.querySelectorAll('.openMail');
    btns.forEach(btn => {
        btn.addEventListener('click', function handleClick(event) {
          console.log('box clicked', event);
          $('form[name=hide').submit(function (e){

            e.preventDefault();
            


        });


          
      
        });
      });
});


