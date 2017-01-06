'use strict';

var tracks = [];
var tracklist = document.querySelector('.tracklist');
var track;
var currentSource = document.querySelector('.currentSource');
var current = document.querySelector('.currentTrack');
var artist = document.querySelector('.artist');
var alltracks = document.querySelector('.alltracks');
var favorites = document.querySelector('.favorites');
var tracksToRender = tracks;

var xhr = new XMLHttpRequest();
var rawData;

function renderTracks(tracksToRender) {
   tracksToRender.forEach(function(e) {
      track = document.createElement('li');
      track.innerHTML = e[2] + ' (' + e[1] + ')';
      track.dataset.idd = e[0];
      tracklist.appendChild(track)
      track.addEventListener('click', function(){
         currentSource.src = e[3];
         current.innerHTML = e[1];
         artist.innerHTML = e[2];
      });
   });
};

alltracks.addEventListener('click', function () {
   tracksToRender.forEach(function(e) {
      tracklist.removeChild(tracklist.firstChild);
   });
   tracksToRender = tracks;
   renderTracks(tracksToRender);
});

favorites.addEventListener('click', function () {
   tracksToRender.forEach(function(e) {
      tracklist.removeChild(tracklist.firstChild);
   });
   tracksToRender = [];
   tracks.forEach(function(e){
      if (e[4] === 1){
         tracksToRender.push(e);
      };
   });
   renderTracks(tracksToRender);
});

// ajax
xhr.open('GET', 'http://localhost:3000/tracks');
xhr.send();
xhr.onreadystatechange = ready;

function ready(rsp) {
   if ( xhr.readyState === XMLHttpRequest.DONE ) {
      rawData = JSON.parse(xhr.response).reverse();
      rawData.forEach(function(e){
         tracks.push([e.id, e.artist, e.track, e.path, e.playlist_id]);
      });
      console.log(tracks);
      currentSource.src = tracks[0][3];
      current.innerHTML = tracks[0][1];
      artist.innerHTML = tracks[0][2];
      renderTracks(tracksToRender);
      }
}
