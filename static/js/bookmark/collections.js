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
    },

    fetchSearch: function(search) {
        var result = this.fetch({
            data: {
                search: search,
            },
            reset: true
        });
        return result;
    },

    fetchNoFolder: function(search) {
        var result = this.fetch({
            data: {
                no_folder: true,
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
