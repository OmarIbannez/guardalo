
var BookmarkView = Marionette.ItemView.extend({
    template: '#bookmark-template',
    className: 'col',
});


var BookmarksView = Marionette.CompositeView.extend({
    template: '#bookmarks-template',
    childView: BookmarkView,
    childViewContainer: '#bookmarks-container',
    className: 'col s12 m12 l9',

    initialize: function(options) {
        this.listenTo(App.vent, 'bookmarks:fetchFolder', this.fetchFolder);
    },

    fetchFolder: function(folder) {
        this.collection.fetchFolder(folder);
    }

});
