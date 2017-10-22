
app.directive('starRating', function () {
    return {
        restrict: 'A',
        template: '<tr class="rating">' +
            '<td ng-repeat="star in stars" ng-class="star">' +
            '\u2605' +
            '</td>' +
            '</tr>',
        scope: {
            ratingValue: '=',
            max: '='
        },
        link: function (scope, elem, attrs) {
            scope.stars = [];
            for (var i = 0; i < scope.max; i++) {
                scope.stars.push({
                    filled: i < scope.ratingValue
                });
            }
        }
    }
});


