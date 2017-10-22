app.directive('datetimepickerNeutralTimezone', function() {
    return {
      restrict: 'A',
      priority: 1,
      require: 'ngModel',
      link: function (scope, element, attrs, ctrl) {
        ctrl.$formatters.push(function (value) {
          var dt = new Date(Date.parse(value));
          dt = new Date(dt.getTime() + (60000 * dt.getTimezoneOffset()));
          return dt
        });

        /*ctrl.$parsers.push(function (value) {
          var dt = new Date(value.getTime() - (60000 * value.getTimezoneOffset()));
          return dt;
        });*/
      }
    };
});