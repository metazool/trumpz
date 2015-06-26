angular.module('trumpz.services', [])

.factory('Cards', function($resource) {

   return { 

     all: function() { 
        return $resource('http://localhost:5000/deck/') 
     },
     one: function(cardId) { 
        console.log('http://localhost:5000/card/'+cardId);
        return $resource('http://localhost:5000/card/'+cardId) 
     }
   };

});
