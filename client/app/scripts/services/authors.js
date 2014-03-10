'use strict';

angular.module('librarianApp')
  .factory('Authors', ['$resource', 'Settings', function ($resource, Settings) {

    var authorResource = $resource(Settings.API.ENTITIES.URL + "/authors/:id");

    // Public API here
    return {
      getInstance: function () {
        return authorResource;
      }
    };
  }]);
