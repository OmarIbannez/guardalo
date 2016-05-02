$(document).ready(function() {

    $('#import-bookmarks-form').on('submit', function(event) {
        event.preventDefault();
        var self = this;
        var url = window.config.bookmarkImportUrl;
        var file = $('#bookmarks-file')[0].files[0];
        var formData = new FormData();
        formData.append('file', file);
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                var response = JSON.parse(xhr.response);
                Materialize.toast(response.message, 4000);
                $('.file-path-wrapper .file-path').text('');
                $('.file-path-wrapper .file-path').val('');
                $('#bookmarks-file').val('');
            }
        }
        xhr.open('POST', url, true);
        xhr.setRequestHeader('X-CSRFToken', window.config.csrf_token);
        xhr.send(formData);
    });

});
