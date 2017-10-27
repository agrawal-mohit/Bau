 app.config( function ( $stateProvider, $urlRouterProvider ) {
   $urlRouterProvider.otherwise('/');

    $stateProvider
        
        // STATES AND VIEWS ========================================
        .state('home', {
            url: '/',
            templateUrl: 'static/views/home.html',
            controller : 'HomeCtrl'
        })

});

