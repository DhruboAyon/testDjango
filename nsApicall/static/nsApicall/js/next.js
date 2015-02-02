var api = "";
var guid = "";

$( document ).ready(function() {
    api = $("#api").val();
    guid = $("#guid").val();
});


app = angular.module("SingleView",[]);

app.factory('TestService', function($http){
    return {
        getRequest: function(url,payload) {
            return $http.get(url,payload);
        }
    };
});

app.controller("SingleViewController",[ 'TestService','$scope', function(TestService,$scope){
    $scope.image_url = "";
    $scope.description = "";
    $scope.searchData = "";

    angular.element(document).ready(function () {
	var url = "../results/"+api+"/"+guid
	TestService.getRequest(url,{}).success(handleSuccess);
    });

    var handleSuccess = function(data){
	if( api === "article"){
	    $scope.image_url = data.article.thumbnail.link;
	    $scope.description = data.article.description;
	}else if( api === "topic"){
	    $scope.image_url = data.topic.image_url;
	    $scope.description = data.topic.description;	    
	}
	    
    }
}]);
