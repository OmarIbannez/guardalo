
var BookmarkView = Marionette.ItemView.extend({
    template: '#bookmark-template',
    className: 'col',

    ui: {
        openMenu: '.open-menu'
    },

    events: {
        'click @ui.openMenu': 'openMenu'
    },

    openMenu: function(event) {
        event.preventDefault();
    },

    templateHelpers: function () {
        return {
            folders: App.folders.toJSON()
        };
    },
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
