
var Bookmark = Backbone.Model.extend({
    urlRoot: window.config.bookmarksApi
});

var Folder = Backbone.Model.extend({
    urlRoot: window.config.foldersApi
});
