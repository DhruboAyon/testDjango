app = angular.module("MainApplication",[]);

app.factory('TestService', function($http){
    return {
        getRequest: function(url,payload) {
            return $http.get(url,payload);
        }
    };
});

app.controller("ArticlesController",[ '$filter','TestService','$scope', function($filter,TestService,$scope){
    $scope.searchList = [];

    var handleArticlesSuccess = function(data){
	$scope.searchList = data.article_set;
    }

    var handleTopicsSuccess = function(data){
	$scope.topicsSearchList = data.topic_set;
    }



    $scope.loadArticles = function(searchParam){
	//alert(searchParam);
	TestService.getRequest("articles/"+searchParam,{}).success(handleArticlesSuccess);
	TestService.getRequest("topics/"+searchParam,{}).success(handleTopicsSuccess);
    }

}]);
