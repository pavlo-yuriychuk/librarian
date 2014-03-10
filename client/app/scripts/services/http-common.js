'use strict';

angular.module('librarianApp')
  .service('HttpCommon', ['$http', function HttpCommon($http) {

    this.init = function () {
      $http.defaults.headers["ContentType"] = "application/json";
    };

    this.setAuthorizationToken = function (value) {
      $http.defaults.headers["X-Auth-Token"] = value.id;
    };

    this.unsetAuthorizationToken = function (value) {
      delete $http.defaults.headers["X-Auth-Token"];
    };
  }]);
