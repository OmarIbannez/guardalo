

// Config App area in the page
App.addRegions({
    bookmarks_area: '#bookmarks-area',
    folders_area: '#folders-area'
});

// Initialize application
App.addInitializer(function(options) {
    /* Bookmarks */
    App.bookmarks = new Bookmarks();
    App.bookmarks.fetch({
        error: function(model, error, options) {
            Materialize.toast(error.responseJSON.detail, 4000);
        },
    });

    /* Folders */
    App.current_folder = null;
    App.folders = new Folders();
    App.folders.fetch({
        success: function() {
            App.folders_area.show(new FoldersView({collection: App.folders}));
            App.bookmarks_area.show(new BookmarksView({collection: App.bookmarks}));
        },
        error: function(model, error, options) {
            Materialize.toast(error.responseJSON.detail, 4000);
        },
    });


});

// Start Marionette application
App.start();
