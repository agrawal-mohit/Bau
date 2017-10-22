app.directive('loader', ['$rootScope' , function ($rootScope) {
    return {
        restrict: 'EA',
        template: '<div class="loader centered"><img src="/static/images/loading.gif" alt="loading.gif"></img></div>',
        link: function (scope, element, attrs) {
            angular.element('.loader').hide();

         } //DOM manipulation
    }
}]);