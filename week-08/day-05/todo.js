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

readTasks();
// deleteItems();

function readTasks () {
   xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
   xhr.send();
   xhr.onreadystatechange = ready;
}

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
      trash.src = 'trash-icon.png';
      trash.className = 'wastebin';
      trash.dataset.idd = e[1];
      if (e[0]) {
         check.className = 'checkbox fa fa-check fa-2x';
         check.dataset.idd = e[1];
      } else {
         check.className = 'checkbox';
         check.dataset.idd = e[1];
      };
      box.appendChild(taskRow);
      items = document.querySelectorAll('.items');
      items[items.length - 1].appendChild(task);
      items[items.length - 1].appendChild(trash);
      items[items.length - 1].appendChild(check);
   })
   deleteItems();
}

button.addEventListener('click', function() {
   newTask = inputText.value;
   console.log(newTask);
   inputText.value = '';
})




function deleteItems() {
   var trashes = document.querySelectorAll('.wastebin');
   trashes.forEach(function (e) {
      e.addEventListener('click', function() {
         console.log(e.dataset.idd);
         xhr.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/'+e.dataset.idd);
         xhr.send();
         xhr.onreadystatechange = console.log;
      })
   })
   checkItems();
}

function checkItems() {
   var trashes = document.querySelectorAll('.checkbox');
   trashes.forEach(function (e) {
      e.addEventListener('click', function() {
         console.log(e.dataset.idd);
         xhr.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/'+e.dataset.idd);
         xhr.send({'text': 'eeeeee', 'completed': true});
         xhr.onreadystatechange = console.log;
      })
   })
}
