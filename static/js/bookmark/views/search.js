
var SearchView = Marionette.ItemView.extend({
    template: '#search-template',
    className: 'col s12 m12 l9',

    ui: {
        searchInput: '#search-input',
    },

    events: {
        'keyup @ui.searchInput': 'searchBookmarks',
    },

    searchBookmarks: function(event) {
        event.preventDefault();
        var search = this.ui.searchInput.val();
        if (search.length < 30) {
            App.vent.trigger('bookmarks:searchBookmarks', search);
        } else if (search.length == 0) {
            App.vent.trigger('bookmarks:showAll');
        }
    },

});
