'use strict';

angular.module('librarianApp', ['ngResource', 'ngRoute'])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/login', {
        templateUrl: 'views/login.html',
        controller: 'LoginCtrl'
      })
      .when('/singup', {
        templateUrl: 'views/singup.html',
        controller: 'SingupCtrl'
      })
      .when('/query', {
        templateUrl: 'views/query.html',
        controller: 'QueryCtrl'
      })
      .when('/admin/:action', {
        templateUrl: 'views/admin.html',
        controller: 'AdminCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
    .run(['HttpCommon', 'Authorization', function (HttpCommon, Authorization) {
      HttpCommon.init();
      Authorization.init();
    }]);
