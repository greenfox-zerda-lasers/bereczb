'use strict';

var Playlists = (function () {
	var root = document.querySelector('#playlists');
	var listNode = root.querySelector('ul');
	var createButton = root.querySelector('button');

	var playlists = [];
	var ajax = new Ajax();

	function render(){
		playlists.forEach(function(playlist){
			var li = _createPlaylistItem(playlist.name, playlist.id);
			listNode.appendChild(li);
		});
	}

	function create(name,id){
		var li = _createPlaylistItem(name,id);
		listNode.appendChild(li);
	}

	function _createPlaylistItem(name, id) {
		var li = document.createElement('li');
		li.innerHTML = name;
		li.addEventListener('click', function(){
			console.log(id);
			// TODO: Render tracks
			Tracks.load(id);
		});
		return li;
	}

	return {
		init: function(){
			ajax.getPlaylists(function(res){
				playlists = res;
				render();
			});

			createButton.addEventListener('click',function(){
				var input = prompt('Enter playlist name');
				ajax.createPlaylists( input, function(rsp){
					console.log(rsp)
					create(input, rsp.id);
				});
			});
		},

		getPlaylists: function(){
			return playlists;
		}
	}
})();
