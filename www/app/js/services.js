(function (window, angular, undefined) {
  "use strict";

  function apartmentsService($http, BASE_URL) {
    this.getApartments = function getApartments() {
      return $http.get(BASE_URL + "apartments/");
    };
  }

  angular.module("app")
    .service("apartmentsService", ["$http", "BASE_URL", apartmentsService]);

})(window, window.angular);