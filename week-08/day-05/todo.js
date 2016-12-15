'use strict';

var button = document.querySelector('.button');
var inputText = document.querySelector('input');
var items = document.querySelectorAll('.items');
var box = document.querySelector('.box');
var xhr = new XMLHttpRequest();
var taskList = [];
var task;
var trash;
var check;
var rawData;
var newTask;
var taskRow;

xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
xhr.send();
xhr.onreadystatechange = ready;

function ready(rsp) {
   if ( xhr.readyState === XMLHttpRequest.DONE ) {
      rawData = JSON.parse(xhr.response);
      console.log(JSON.parse(xhr.response));
      rawData.forEach(function(e){
         taskList.push([e.completed, e.id, e.text]);
      })
      console.log(taskList);
      displayTasks();
   }
}

function displayTasks() {
   taskList.forEach(function (e) {
      task = document.createElement('div');
      trash = document.createElement('img');
      check = document.createElement('i');
      taskRow = document.createElement('div');

      taskRow.className = 'items';
      task.innerHTML = e[2];
      task.className = 'itemtext';
      if (e[0]) {
         check.className = 'checkbox fa fa-check fa-2x';
      } else {
         check.className = 'checkbox';
      };
      trash.src = 'trash-icon.png';
      trash.className = 'wastebin';
      box.appendChild(taskRow);
      items = document.querySelectorAll('.items');
      items[items.length - 1].appendChild(task);
      items[items.length - 1].appendChild(trash);
      items[items.length - 1].appendChild(check);
   })
}

button.addEventListener('click', function() {
   newTask = inputText.value;
   console.log(newTask);
   inputText.value = '';
})
