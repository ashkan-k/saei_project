app.controller('myCtrl', function ($scope, $http) {
    $scope.window = window;
    $scope.intervalId = 0;
    $scope.counter = 0;
    $scope.loginUser = {};

    $scope.init = function () {
        countDown();
    }

    // Counter here
    function clearTimer() {
        clearInterval($scope.intervalId);
    }

    function countDown() {
        // Set the date we're counting down to
        date = new Date();
        date.setMinutes(date.getMinutes() + {{ object.time }})
        var countDownDate = date.getTime();

// Update the count down every 1 second
        var x = setInterval(function () {

            // Get today's date and time
            var now = new Date().getTime();

            // Find the distance between now and the count down date
            var distance = countDownDate - now;

            // Time calculations for days, hours, minutes and seconds
            var days = Math.floor(distance / (1000 * 60 * 60 * 24));
            var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Display the result in the element with id="demo"
            document.getElementById("timer").innerHTML = hours + "	&#160;ساعت \t&#160;\t&#160;"
                + minutes + "	&#160;دقیقه \t&#160;\t&#160; " + seconds + "	&#160;ثانیه \t&#160;\t&#160; ";

            if (seconds == 10) {
                $.toast({
                    heading: 'هشدار',
                    text: 'زمان آزمون رو به اتمام است!',
                    position: 'bottom-left',
                    bgColor: '#e6294b',
                    loaderBg: "rgb(13, 146, 108)",
                    loader: true,
                    hideAfter: 3000,
                    stack: 3
                });
            }

            // If the count down is finished, write some text
            if (distance < 0) {
                clearInterval(x);
                window.location.href = '{% url "quizzes-list" %}'
            }
        }, 1000);
    }

    $scope.reset = reset;

    function reset() {
        $scope.counter = 0;
        $scope.toggleVerifyMode();
        $scope.loginCode = '';
        $scope.updateCaptcha();
    }
});

// $("#header-menu").click(function () {
//     $("#tg-navigation").toggleClass("in");
// });