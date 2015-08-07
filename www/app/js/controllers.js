(function (window, angular, undefined) {
  "use strict";

  function MainController($scope) {

  }

  function HomeController($scope) {

  }

  angular.module("app")
    .controller("MainController", ["$scope", MainController])
    .controller("HomeController", ["$scope", HomeController]);

})(window, window.angular);