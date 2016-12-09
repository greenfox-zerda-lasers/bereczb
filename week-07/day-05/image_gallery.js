'use strict';

var urlToDisplay
var currentPos
var mainPic = document.querySelector('.mainpic');
var buttonL = document.querySelector('.left');
var buttonR = document.querySelector('.right');
var button = document.querySelectorAll('.index-buttons button');


function changeImageDirect(index) {
      currentPos = readCurrent();
   delCurrent(currentPos);
   writeCurrent(index);
   urlToDisplay = "url('" + (index + 1) + ".jpg')";
   mainPic.style.backgroundImage = urlToDisplay;
}

function changeImageSteps(index) {
   currentPos = readCurrent();
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
   button[index].classList.remove('current');
}

function writeCurrent(index) {
   button[index].classList.add('current');
}

buttonL.addEventListener('click', function(){changeImageSteps('L')});
buttonR.addEventListener('click', function(){changeImageSteps('R')});
button.forEach(function(e) {
   e.addEventListener('click', function(){changeImageDirect(parseInt(this.dataset.imageId))});
});
