'use strict';

angular.module('librarianApp')
  .controller('QueryCtrl', ['$scope', '$routeParams', 'Books', 'Authors', function ($scope, $routeParams, Books, Authors) {
    $scope.entity = "books";

    $scope.init = function () {
      $scope.items = $scope.getEntityResourceByType($scope.entity).query();
    };

    $scope.getEntityResourceByType = function (value) {
      return {
        "books": Books.getInstance(),
        "authors": Authors.getInstance()
      }[value];
    };
  }]);
