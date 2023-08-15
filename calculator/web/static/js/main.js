$(document).ready(function() {
    // Load operations from the API
    $.get("/api/calculator/operations/", function(data) {
        console.log(data);
        $('#available-operations').text(data.available_operations.join(", "));
    });

    // Calculate button listener
    $("#calculateBtn").click(function() {
        // Clear previous errors
        $(".error").text('');

        // Clear previous result
        $("#result").text('');

        const expression = $('#expression').val();
        $.post("/api/calculator/calculate/", {
            expression: expression
        }, function(data) {
            $('#result').text(data.result);
            $('#error').text('');
        }).fail(function(error) {
            const errors = error.responseJSON;
            $('#error').text(errors.error);
            $('#result').text('-');
        });
    });
});
