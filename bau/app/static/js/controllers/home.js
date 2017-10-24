app.controller('HomeCtrl', function($scope, ScheduleService) {

	
   $scope.show_shift = function() {
      ScheduleService.get_todays_shift()
      .then(function(shift){
         $scope.todays_shift = shift
      })
   }
   
})

