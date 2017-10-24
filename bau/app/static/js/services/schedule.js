
app.factory('ScheduleService' , function($http){

	var service = {
		get_todays_shift : function(){
			return $http.get('/shift')
			.then(
				function(response){
					return response.data
			}, 
				function(error){
					console.log(error);
			})
		}
	}

	return service

})
