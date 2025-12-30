angular.module('linuxDash').directive('keyValueList', ['server', function (server) {
  return {
    scope: {
      heading: '@',
      info: '@',
      moduleName: '@',
    },
    templateUrl: 'src/js/core/features/key-value-list/key-value-list.html',
    link: function(scope, element) {

      scope.getData = function() {
        delete scope.tableRows

        server.get(scope.moduleName, function(serverResponseData) {
          scope.tableRows = serverResponseData
          scope.lastGet = new Date().getTime()

          if (Object.keys(serverResponseData).length === 0) {
            scope.emptyResult = true
          }

          scope.$applyAsync()
        })
      }

      scope.getData()
    }
  }
}])
