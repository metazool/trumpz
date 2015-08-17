angular.module('trumpz.services', [])

.factory('Cards', function($resource) {
   
   return { 

     all: function() { 
        return $resource('http://trumpz.herokuapp.com/deck/');
     },
     one: function(cardId) { 
        console.log('http://trumpz.herokuapp.com/card/'+cardId);
        return $resource('http://trumpz.herokuapp.com/card/'+cardId) 
     },
     random: function() {
	return $resource('http://trumpz.herokuapp.com/random/');
     }
   };

});
