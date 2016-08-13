
var FolderView = Marionette.ItemView.extend({
    template: '#folder-template',
    tagName: 'li',

    ui: {
        'folderName': '.name',
        'edit': '.edit',
        'remove': '.remove',
        'editForm': '.edit-form',
        'folderOptions': '.options',
        'editFolderInput': '.edit-folder-input',
        'cancelEditForm': '.cancel-edit-folder',
        'editFolder': '.edit-folder',
    },

    events: {
        'click @ui.folderName': 'fetchFolder',
        'mouseover': 'toggleOptions',
        'mouseout': 'toggleOptions',
        'click @ui.remove': 'removeFolder',
        'click @ui.edit': 'openEditForm',
        'click @ui.cancelEditForm': 'cancelEditForm',
        'click @ui.editFolder': 'editFolder',
    },

    onRender: function() {
        this.ui.folderOptions.hide();
    },

    fetchFolder: function(event) {
        event.preventDefault();
        App.current_folder = this.model.get('id');
        App.vent.trigger('bookmarks:fetchFolder', this.model.get('id'));
    },

    toggleOptions: function(event) {
        if (this.ui.editForm.is(':visible') == false) {
            this.ui.folderOptions.toggle();
        }
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
    },

    openEditForm: function(event) {
        event.preventDefault();
        this.ui.editFolderInput.val(this.ui.folderName.text());
        this.ui.folderName.hide();
        this.ui.editForm.show();
        this.ui.folderOptions.hide();

    },

    cancelEditForm: function(event) {
        this.ui.folderName.show();
        this.ui.editForm.hide();
        this.ui.folderOptions.show();
    },

    editFolder: function(event) {
        this.model.set('name', this.ui.editFolderInput.val());
        this.ui.folderName.text(this.ui.editFolderInput.val());
        this.model.save();
        this.cancelEditForm();
    },
});


var FoldersView = Marionette.CompositeView.extend({
    template: '#folders-template',
    childView: FolderView,
    childViewContainer: '#folders-container',

    ui: {
        'showAll': '#show-all',
        'showNoFolder': '#show-no-folder',
        'toggleFolderForm': '#toggle-folder-form',
        'folderFormSection': '#folder-form-section',
        'folderInput': '#folder-input',
        'save': '#save-folder'
    },

    events: {
        'click @ui.showAll': 'showAll',
        'click @ui.showNoFolder': 'showNoFolder',
        'click @ui.toggleFolderForm': 'toggleFolderForm',
        'click @ui.save': 'save'
    },

    showAll: function(event) {
        event.preventDefault();
        App.vent.trigger('bookmarks:showAll');
    },

    showNoFolder: function(event) {
        event.preventDefault();
        App.vent.trigger('bookmarks:showNoFolder');
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
