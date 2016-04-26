
var FolderView = Marionette.ItemView.extend({
    template: '#folder-template',
    tagName: 'li',

    events: {
        'click': 'fetchFolder'
    },

    fetchFolder: function(event) {
        event.preventDefault();
        App.vent.trigger('bookmarks:fetchFolder', this.model.get('id'));
    }

});


var FoldersView = Marionette.CompositeView.extend({
    template: '#folders-template',
    childView: FolderView,
    childViewContainer: '#folders-container',
});
