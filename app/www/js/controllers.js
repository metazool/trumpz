angular.module('trumpz.controllers', [])

.controller('DashCtrl', function($scope, $state, Cards) {
  $scope.card = Cards.random().query();
  $scope.searchterm = '';
  console.log($scope.card);
  $scope.search = function() {
	
	console.log($scope.searchterm);
	var searchterm = $scope.searchterm.charAt(0).toUpperCase() + $scope.searchterm.slice(1);
	
	$state.go('tab.search',{text:searchterm});
  }
})

.controller('CardsCtrl', function($scope, $resource, Cards) {
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //
  //$scope.$on('$ionicView.enter', function(e) {
//	$scope.cards = Cards.all().query()
//  });
  $scope.cards = Cards.all().query()
})

.controller('CardDetailCtrl', function($scope, $stateParams, Cards) {
  $scope.card = Cards.one($stateParams.cardId).get();
  //.get( function(data) {
//
  //	console.log(data);
   //});

})

.controller('CardSearchCtrl', function($scope, $stateParams, Cards) {
  $scope.card = Cards.search($stateParams.text).get();
  //.get( function(data) {
//
  //    console.log(data);
   //});

})

.controller('AccountCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };
});
