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
                var CommentLi = $('<li>').text(comment.content);
                $('.comment-list').append(CommentLi);
            });
        },
        error: function(data) {},
    });

    var commentBox = $('.comment-content').find('input[name="content"]');
    
    $('.comment-content').submit(function() {
        var content = $(commentBox).val();
        $(commentBox).val('');
        var newCommentLi = $('<li>').text(content);
        $('.comment-list').append(newCommentLi);
        return false;
    });
};

$(document).ready(main)
