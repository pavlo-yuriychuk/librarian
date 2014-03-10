'use strict';

angular.module('librarianApp')
  .service('Authorization', ['$http', 'Settings', 'HttpCommon', function Authorization($http, Settings, HttpCommon) {
    var baseUrl;

    this.init = function () {
      baseUrl = Settings.API.AUTHORIZATION.URL;
    };

    this.login = function (username, password) {
      return $http.post(baseUrl + "/login", {username: username, password: password}).then(function (result) {
        HttpCommon.setAuthorizationToken(result.data.token);
        return result.data;
      });
    };

    this.logout = function (token) {
      return $http.post(baseUrl + "/logout", {token: token}).then(function (result) {
        HttpCommon.unsetAuthorizationToken(token);
      });
    };

    this.signup = function (username, password) {
      return $http.post(baseUrl + "/signup", {username: username, password: password});
    };
  }]);
