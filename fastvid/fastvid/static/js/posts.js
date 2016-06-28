var main = function() {
    var postSlug = $('#comment-section').data('post-slug');
    var commentAPIURL = '/api/posts/' + postSlug + '/comments/';    
    alert(commentAPIURL);

    $.ajax({
        url: commentAPIURL,
        type: 'GET',
        success: function(data) {
            var commentCount = data.length;
            $('.comment-count').html(commentCount);

            data.forEach(function(comment) {
                var newCommentLi = $('<li>').text(comment.content);
                $('.comment-list').append(newCommentLi);
            });
        },
        error: function(data) {},
    })
};

$(document).ready(main)
