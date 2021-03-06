'use strict';

describe('Controller: SingupCtrl', function () {

  // load the controller's module
  beforeEach(module('librarianApp'));

  var SingupCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    SingupCtrl = $controller('SingupCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
