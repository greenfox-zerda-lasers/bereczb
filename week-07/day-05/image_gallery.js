'use strict';

var position = 1;
var urlToDisplay = "";
var currentPos = 1;
var mainPic = document.querySelector('.mainpic');
var buttonL = document.querySelector('.left');
var buttonR = document.querySelector('.right');
var button = document.querySelectorAll('.index-buttons button');


function changeImageDirect(index) {
   var currentPos = readCurrent();
   delCurrent(currentPos);
   writeCurrent(index);
   urlToDisplay = "url('" + (index + 1) + ".jpg')";
   mainPic.style.backgroundImage = urlToDisplay;
   console.log(urlToDisplay);

}

function changeImageSteps(index) {
   var currentPos = readCurrent();
   delCurrent(currentPos);
   if (index === 'R') {
      if (currentPos < 7) {
         urlToDisplay = "url('" + (currentPos + 2) + ".jpg')";
         mainPic.style.backgroundImage = urlToDisplay;
         writeCurrent(currentPos + 1);
      } else {
         urlToDisplay = "url('" + 1 + ".jpg')";
         mainPic.style.backgroundImage = urlToDisplay;
         writeCurrent(0);
      }
   } else {
      if (currentPos > 0) {
         urlToDisplay = "url('" + (currentPos) + ".jpg')";
         mainPic.style.backgroundImage = urlToDisplay;
         writeCurrent(currentPos - 1);
      } else {
         urlToDisplay = "url('" + 8 + ".jpg')";
         mainPic.style.backgroundImage = urlToDisplay;
         writeCurrent(7);
      }
   }
}

function readCurrent(){
   for (var i = 0; i < button.length; i++){
      if (button[i].classList.contains('current')) {
         return i;
      }
   }
}

function delCurrent(index) {
   console.log(index);
   button[index].classList.remove('current');
}

function writeCurrent(index) {
   button[index].classList.add('current');
}

function buttonClickObserver (index) {
   console.log(index);
}

buttonL.addEventListener('click', function(){changeImageSteps('L')});
buttonR.addEventListener('click', function(){changeImageSteps('R')});
button.forEach(function(e) {
   e.addEventListener('click', function(){buttonClickObserver(this.dataset.imageId)});
});

// button[0].addEventListener('click', function(){changeImageDirect(0)});
// button[1].addEventListener('click', function(){changeImageDirect(1)});
// button[2].addEventListener('click', function(){changeImageDirect(2)});
// button[3].addEventListener('click', function(){changeImageDirect(3)});
// button[4].addEventListener('click', function(){changeImageDirect(4)});
// button[5].addEventListener('click', function(){changeImageDirect(5)});
// button[6].addEventListener('click', function(){changeImageDirect(6)});
// button[7].addEventListener('click', function(){changeImageDirect(7)});


// Read
// var box = document.querySelector('.box')
// box.addEventListener('click',function (e) {
//    console.log(this.dataset.imageId)
// })
//
// // Write
// var x = document.createElement('div')
// x.dataset.test = 'hello'
// document.body.appendChild(x)
