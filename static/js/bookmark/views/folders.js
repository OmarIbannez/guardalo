
var FolderView = Marionette.ItemView.extend({
    template: '#folder-template',
    tagName: 'li',

    ui: {
        'name': '.name',
        'edit': '.edit',
        'remove': '.remove'
    },

    events: {
        'click @ui.name': 'fetchFolder',
        'mouseover': 'toggleOptions',
        'mouseout': 'toggleOptions',
        'click @ui.remove': 'removeFolder',
    },

    fetchFolder: function(event) {
        event.preventDefault();
        App.current_folder = this.model.get('id');
        App.vent.trigger('bookmarks:fetchFolder', this.model.get('id'));
    },

    toggleOptions: function(event) {
        this.ui.edit.toggle();
        this.ui.remove.toggle();
    },

    removeFolder: function(event) {
        event.preventDefault();
        var confirmRemove = confirm('Do you want to continue?');
        if (confirmRemove == true) {
            if (App.current_folder == this.model.get('id')) {
                App.vent.trigger('bookmarks:showAll');
            }
            this.model.destroy();
        }
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
        folder.save(null, {
            success: function () {
                App.vent.trigger('bookmark:addNewFolder', folder);
            }
        });
        this.collection.add(folder);
        this.ui.folderInput.val('');
        this.toggleFolderForm();
    }
});
