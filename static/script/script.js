var sbmtBtn = document.getElementById('btn');
var agefrom = document.getElementById('age-from');
var ageto = document.getElementById('age-to');
var category = document.getElementById('category-input');
var keyword = document.getElementById('keyword-input');
var sub = document.querySelector('.subject');
var tip = document.querySelector('.tip');

function checkCount(obj, event){
    if(obj.value && event.keyCode == 32){
        alert("한 분야만 입력 가능합니다");
        return false;
    }
};

function checkSpace(event){
    if(event.keyCode == 32){
        keyword.value = keyword.value + ", ";
    }
};

sbmtBtn.addEventListener('click',function(e){
    e.preventDefault();

    if(agefrom.value > ageto.value){
        alert("연령을 재확인해주세요");
        agefrom.focus();
        return false;
    }
    if(!ageto.value){
        alert("빈칸을 채워주세요");
        ageto.focus();
        return false;
    } else if(!category.value){
        alert("빈칸을 채워주세요");
        category.focus();
        return false;
    } else if(!keyword.value){
        alert("빈칸을 채워주세요");
        keyword.focus()
        return false;
    }
    var url="http://127.0.0.1:5000/result";
    location.href=url;
});

sub.addEventListener('mousemove',function(event){
      var x = event.clientX;
      var y = event.clientY;
      tip.style.left = x+10;
      tip.style.top = y-20;
      tip.setAttribute('class', 'tip on');
  });

  /*.mouseleave(function(){
      $(".tip").removeClass("on");
  });*/