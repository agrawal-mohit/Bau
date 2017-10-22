 app.config( function ( $stateProvider, $urlRouterProvider ) {
   $urlRouterProvider.otherwise('/');

    $stateProvider
        
        // STATES AND VIEWS ========================================
        .state('home', {
            url: '/',
            templateUrl: 'static/views/home.html',
            controller : 'HomeCtrl'
            // resolve: {
            //     investment_profile : ['UserService', function(UserService) {
            //         return UserService.get_user_profile('investment');
            //     }]
            // }     
        })
        .state('schedule', {
            url: '/',
            templateUrl: 'static/views/schedule.html',
            controller : 'ScheduleCtrl'
        })
        .state('register', {
            url: '/',
            templateUrl: 'static/views/register.html',
            controller : 'RegisterCtrl'
        })


});

