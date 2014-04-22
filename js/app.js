'use strict';

/* App Module */

var frtApp = angular.module('frtApp', [
  'ngRoute'
  ,'frtControllers'
  //,'frtFilters'
]);

frtApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/main', {
        templateUrl: 'partials/main.html',
        controller: 'indexCtrl'
      }).
      when('/input_1', {
        templateUrl: 'partials/input_1.html',
        controller: 'input_1_Ctrl'
      }).
      
      otherwise({
        redirectTo: '/main'
      });
  }]);