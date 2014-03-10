'use strict';

angular.module('librarianApp')
  .constant('Settings', {
      API: {
        AUTHORIZATION: {
          URL: "http://localhost:5000"
        },
        ENTITIES: {
          URL: "http://localhost:5000"
        }
      }
    });
