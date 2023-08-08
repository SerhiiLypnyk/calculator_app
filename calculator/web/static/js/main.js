$(document).ready(function() {
    // Load operations from the API
    $.get("/api/calculator/operations/", function(data) {
        const operationSelect = $("#operation");
        for (let operation of data) {
            operationSelect.append(new Option(operation, operation));
        }
    });

    // Calculate button listener
    $("#calculateBtn").click(function() {
        // Clear previous errors
        $(".error").text('');

        // Clear previous result
        $("#result").text('');

        const operand1 = $("#operand1").val();
        const operand2 = $("#operand2").val();
        const operation = $("#operation").val();

        $.post("/api/calculator/calculate/", {
            operand1: operand1,
            operand2: operand2,
            operation: operation
        }, function(data) {
            $("#result").text(data.result);
        }).fail(function(error) {
            const errors = error.responseJSON;
            if(errors.operand1) {
                $("#operand1-error").text(errors.operand1[0]);
            }
            if(errors.operand2) {
                $("#operand2-error").text(errors.operand2[0]);
            }
        });
    });
});
