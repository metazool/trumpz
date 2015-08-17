angular.module('trumpz.controllers', [])

.controller('DashCtrl', function($scope, Cards) {
  $scope.card = Cards.random().query();
  console.log($scope.card);
})

.controller('CardsCtrl', function($scope, $resource, Cards) {
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //
  //$scope.$on('$ionicView.enter', function(e) {
  //});
  $scope.cards = Cards.all().query()
})

.controller('CardDetailCtrl', function($scope, $stateParams, Cards) {
  $scope.card = Cards.one($stateParams.cardId).get();
  //.get( function(data) {
//
  //	console.log(data);
   //});

})

.controller('AccountCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };
});
