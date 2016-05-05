
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

    ui: {
        'showAll': '#show-all',
        'toggleFolderForm': '#toggle-folder-form',
        'folderFormSection': '#folder-form-section',
        'folderInput': '#folder-input',
        'save': '#save-folder'
    },

    events: {
        'click @ui.showAll': 'showAll',
        'click @ui.toggleFolderForm': 'toggleFolderForm',
        'click @ui.save': 'save'
    },

    showAll: function(event) {
        event.preventDefault();
        App.vent.trigger('bookmarks:showAll');
    },

    toggleFolderForm: function() {
        this.ui.folderFormSection.toggle();
        return false;
    },

    save: function(event) {
        event.preventDefault();
        folderName = this.ui.folderInput.val();
        folder = new Folder({
            'name': folderName
        });
        folder.save();
        this.collection.add(folder);
        this.ui.folderInput.val('');
        this.toggleFolderForm();
    }
});
