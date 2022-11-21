      $('button').click(function(event) {
        var class_name = event.target.className.split(" ");

        if (class_name[1] == 'add-to-cart') {
            console.log(class_name[1]);
            var _vm =$(this);
            var _productName = this.id
            $.ajax({
              url:'/add-to-cart',
              data:{
                'name': _productName
              },
              dataype:'json',
              beforeSend:function(){
                _vm.attr('disabled',true);
              },
              success:function(res){
                console.log(res);
                $(".cart-list").text(res.totalitems);
                _vm.attr('disabled',false);
              }
          });
        } else if (class_name[1] == 'delete-item') {
                var _productName = $(this).attr('data-item');
                var _vm =$(this);
            $.ajax({
              url:'/delete-from-cart',
              data:{
                'name': _productName
              },
              dataype:'json',
              beforeSend:function(){
                _vm.attr('disabled',true);
              },
              success:function(res){
                console.log(res);
                $(".cart-list").text(res.totalitems);
                _vm.attr('disabled',false);
                $("#cartList").html(res.data);
              }
          });
        } else if (class_name[1] == 'pay-button') {
            var _vm =$(this);
           $.ajax({
                  url:'/pay-from-cart',
                  dataype:'json',
                  beforeSend:function(){
                    _vm.attr('disabled',true);
                  },
                  success:function(res){
                    console.log(res);
                    $(".cart-list").text(res.totalitems);
                    _vm.attr('disabled',false);
                    $("#cartList").html(res.data);
                  }
              });
        } else if (class_name[0] == 'screen-reader') {
            let msg = new SpeechSynthesisUtterance();
            let voices = speechSynthesis.getVoices();
            msg.voice = voices[0];
            let tags = document.querySelectorAll('h1, h2, h3, h4, h5, p, span, button, input, td, tr, a');
            tags.forEach( (tag) => {
                tag.addEventListener('click', (e) => {
                    msg.text = e.target.innerText;
                    tag.style.backgroundColor = "yellow";
                    speechSynthesis.speak(msg);

                    let interval = setInterval(() => {
                        if(!speechSynthesis.speaking) {
                            tag.style.removeProperty('background-color');
                            clearInterval(interval);
                        }
                    }, 100);
                });
            });
        }});