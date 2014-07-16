$(document).ready(function() {
    var query_name = $("#query-program-name").val();
    if (query_name != null) {
            $.get('/ca/program_search', {search_name: query_name}, function(data) {
                $("#program_suggestions").html(data);
            });
    }

    $("#query-program-name").keyup(function() {
        var query_name = $(this).val();
            $.get('/ca/program_search/', {search_name: query_name}, function(data) {
                $("#program_suggestions").html(data);
            });
    });

    $(".program-search-category").hide();

    $("#category-trigger").click(function() {
        // var this_field = $(this).attr("thefield")
        $(".program-search-category").show();

    });
});

