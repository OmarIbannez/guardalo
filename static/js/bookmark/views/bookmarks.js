
var BookmarkView = Marionette.ItemView.extend({
    template: '#bookmark-template',
    className: 'col',

    ui: {
        openMenu: '.open-menu',
        removeBookmark: '.remove-bookmark',
        bookmarkFolder: '.bookmark-folder',
        folderName: '.folder-name'
    },

    events: {
        'click @ui.openMenu': 'openMenu',
        'click @ui.removeBookmark': 'removeBookmark',
        'change @ui.bookmarkFolder': 'updateBookmarkFolder'
    },

    templateHelpers: function () {
        return {
            folders: App.folders.toJSON()
        };
    },

    openMenu: function(event) {
        event.preventDefault();
    },

    removeBookmark: function(event) {
        event.preventDefault();
        this.model.destroy();
    },

    updateBookmarkFolder: function() {
        folder = this.ui.bookmarkFolder.find('option:selected').val();
        folder_name = this.ui.bookmarkFolder.find('option:selected').text();
        this.model.set({'folder': folder});
        this.model.save();
        this.ui.folderName.text(folder_name);
    }
});


var BookmarksView = Marionette.CompositeView.extend({
    template: '#bookmarks-template',
    childView: BookmarkView,
    childViewContainer: '#bookmarks-container',
    className: 'col s12 m12 l9',

    initialize: function(options) {
        this.listenTo(App.vent, 'bookmarks:fetchFolder', this.fetchFolder);
        this.listenTo(App.vent, 'bookmarks:showAll', this.showAll);
    },

    fetchFolder: function(folder) {
        this.collection.fetchFolder(folder);
    },

    showAll: function() {
        this.collection.fetch({reset:true});
    }

});
