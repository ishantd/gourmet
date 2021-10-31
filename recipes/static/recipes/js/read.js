function get_search_data() {
    $.get("/recipes/read/?api=true", function (data, status) {
        console.log(data)
        var search_list = data.data;
        console.log(search_list)
        var search_this = new Bloodhound({
            datumTokenizer: Bloodhound.tokenizers.whitespace,
            queryTokenizer: Bloodhound.tokenizers.whitespace,
            local: search_list,
        });

        $("#autocomplete").typeahead({
            highlight: true,
        },
            {
                name: 'recipes',
                source: search_this,
                templates: {
                    header: '<h6 class="symbol-class">Recipes and Ingredients</h6>'
                }
        })
    });
}

$('#autocomplete').bind('typeahead:select', function (ev, symbol) {

    $.get(`/recipes/get-id/?string=${symbol}`, function (data) {
        var id = data.id;
        window.location = `/recipes/read/single/${id}/`;
    });
});




get_search_data();