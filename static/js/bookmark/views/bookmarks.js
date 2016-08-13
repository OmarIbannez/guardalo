
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

    initialize: function(options) {
        this.listenTo(App.vent, 'bookmark:addNewFolder', this.addNewFolder);
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
    },

    addNewFolder: function(folder) {
        $folder = $('<option>', {
            value: folder.get('id'),
            text : folder.get('name'),
        });
        this.ui.bookmarkFolder.append($folder);
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
        this.listenTo(App.vent, 'bookmarks:searchBookmarks', this.searchBookmarks);
    },

    fetchFolder: function(folder) {
        this.collection.fetchFolder(folder);
    },

    showAll: function() {
        this.collection.fetch({reset:true});
    },

    searchBookmarks: function(search) {
        this.collection.fetchSearch(search);
    }

});
