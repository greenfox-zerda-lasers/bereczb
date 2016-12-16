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

function readTasks () {
   taskList = [];
   inputText.value = '';
   xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
   xhr.send();
   xhr.onreadystatechange = ready;
}

function ready(rsp) {
   if ( xhr.readyState === XMLHttpRequest.DONE ) {
      rawData = JSON.parse(xhr.response).reverse();
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
      task.dataset.idd = e[1];
      trash.src = 'trash-icon.png';
      trash.className = 'wastebin';
      trash.dataset.idd = e[1];
      if (e[0]) {
         check.className = 'checkbox fa fa-check fa-2x';
         check.dataset.idd = e[1];
         task.classList.add('checked');
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
   button.addEventListener('click', function() {
      newTask = inputText.value;
      console.log(newTask);
      xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos/');
      xhr.setRequestHeader('Content-Type', 'application/json')
      xhr.send(JSON.stringify({text: newTask}));
      xhr.onreadystatechange = endOfProcess;
   })
   var trashes = document.querySelectorAll('.wastebin');
   trashes.forEach(function (e) {
      e.addEventListener('click', function() {
         xhr.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/'+e.dataset.idd);
         xhr.send();
         xhr.onreadystatechange = endOfProcess;
      })
   })
   var checkboxes = document.querySelectorAll('.checkbox');
   checkboxes.forEach(function (e) {
      e.addEventListener('click', function() {
         xhr.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + e.dataset.idd);
         xhr.setRequestHeader('Content-Type', 'application/json')
         var  checkedTask;
         taskList.forEach(function (e) {
            console.log(e[1], ' ', this);
            if (e[1] === this) {
               console.log(e[2]);
               checkedTask = e[2];
            }
         }, parseInt(e.dataset.idd));
         console.log('checkedTask: ', checkedTask);
         if (e.classList.contains("fa")) {
            xhr.send(JSON.stringify({text: checkedTask, completed: false}));
         } else {
            xhr.send(JSON.stringify({text: checkedTask, completed: true}));
         }
         xhr.onreadystatechange = endOfProcess;
      })
   })
}

function endOfProcess(rsp) {
   if ( xhr.readyState === XMLHttpRequest.DONE ) {
      items = document.querySelectorAll('.items');
      box = document.querySelector('.box');
      items.forEach(function(e) {
         box.removeChild(e);
      });
      readTasks();
   }
}
