(function (window, angular, undefined) {
  "use strict";

  function MainController($scope) {

  }

  function HomeController($scope) {

  }

  function ApartmentsController($scope, apartmentsService) {
    $scope.models = {
      apartments: [{
        building: {},
        apartment: {
          building: undefined,
          amenities: [],
          num_bedrooms: 0,
          num_bathrooms: 0,
          num_rooms: 0
        },
        amenity: {}
      }]
    };

    $scope.numApartments = function numApartments() {
      return _.size($scope.models.apartments);
    };

    $scope.range = function range(property) {
      var min = 0,
          max = 0;

      _.forEach($scope.models.apartments, function(apartment) {
        min = Math.min(min, apartment[property]);
        max = Math.max(max, apartment[property]);
      });

      return {min: min, max: max};
    };

    $scope.getApartments = function getApartments() {
      apartmentsService.getApartments().then(onLoadSuccess);

      function onLoadSuccess(response) {
        var apartments = response.data.apartment;

        _.forEach(apartments, function(apartment) {
          // Populate side-loaded building objects...
          apartment._building = _.findWhere(response.data.building, {id: apartment.building});

          // Populate side-loaded amenity objects...
          apartment._amenities = [];

          _.forEach(apartment.amenities, function(amenity) {
            apartment._amenities.push(_.findWhere(response.data.amenity, {id: amenity}));
          });
        });

        $scope.models.apartments = apartments;
      }
    };

    function init() {
      $scope.getApartments();
    }

    init();
  }

  angular.module("app")
    .controller("MainController", ["$scope", MainController])
    .controller("HomeController", ["$scope", HomeController])
    .controller("ApartmentsController", ["$scope", "apartmentsService", ApartmentsController]);

})(window, window.angular);