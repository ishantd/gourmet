const search = instantsearch({
    indexName: 'recipes',
    searchClient: algoliasearch('9SNN6GI84R', 'f9f6b2690e3e8a75cdb6135fe9e539f1'),
});

instantsearch.widgets.searchBox({
    container: '#searchbox',
});

search.start();