'use strict';

// create a function that when called alerts "I'm delayed" after 1 second

function callAlert(){
   window.alert('I\'am delayed');
}

setTimeout(callAlert, 1000);
