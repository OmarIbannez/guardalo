var Bookmarks = Backbone.Collection.extend({
    model: Bookmark,
    url: window.config.bookmarksApi,

    fetchFolder: function(folder) {
        var result = this.fetch({
            data: {
                folder: folder,
            },
            reset: true
        });
        return result;
    }

});

var Folders = Backbone.Collection.extend({
    model: Folder,
    url: window.config.foldersApi
});
