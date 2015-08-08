(function (window, angular, undefined) {
  "use strict";

  function MainController($scope) {

  }

  function HomeController($scope) {

  }

  function ApartmentsController($scope) {

  }

  angular.module("app")
    .controller("MainController", ["$scope", MainController])
    .controller("HomeController", ["$scope", HomeController])
    .controller("ApartmentsController", ["$scope", ApartmentsController]);

})(window, window.angular);