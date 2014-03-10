'use strict';

describe('Service: HttpCommon', function () {

  // load the service's module
  beforeEach(module('librarianApp'));

  // instantiate service
  var HttpCommon;
  beforeEach(inject(function (_HttpCommon_) {
    HttpCommon = _HttpCommon_;
  }));

  it('should do something', function () {
    expect(!!HttpCommon).toBe(true);
  });

});
