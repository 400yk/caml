$(document).ready(function() {

    var query_name = $("#query-program-name").val();
    if (query_name != null) {
        if (query_name != "") {
            $.get('/ca/program_search', {search_name: query_name}, function(data) {
                $("#program_suggestions").html(data);
            });
        } else {}
    }

    $("#query-program-name").keyup(function() {
        var query_name = $(this).val();
        if (query_name != "") {
            $.get('/ca/program_search/', {search_name: query_name}, function(data) {
                $("#program_suggestions").html(data);
            });
        } else {}
    });
});

