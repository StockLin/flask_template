$("#btn-exec").click(function() {
    var url = "http://localhost:5000/shares-return/add";
    var x = $('#calc-x').val();
    var y = $('#calc-y').val();
    var z = {"x":x, "y":y}


    $.ajax({
        url: url,
        data: JSON.stringify(z),
        type: "POST",
        dataType: "json",
        contentType: "application/json;charset=utf-8",
        success: function(response){
            $("#status").text(response["status"])
            $("#result").text(response["data"])
        },
        error: function(xhr, ajaxOptions, thrownError){
            console.log(xhr.status);
            console.log(thrownError);
            alert("計算失敗");
        }
    });

});