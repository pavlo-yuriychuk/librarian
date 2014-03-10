'use strict';

angular.module('librarianApp')
  .factory('Books', ['$resource', function ($resource) {
    var booksResource = $resource(Settings.API.ENTITIES.URL + "/books/:id");

    // Public API here
    return {
      getInstance: function () {
        return booksResource;
      }
    };
  }]);
