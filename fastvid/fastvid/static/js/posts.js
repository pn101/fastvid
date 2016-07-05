var main = function() {
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var postSlug = $('#comment-section').data('post-slug');
    var commentAPIURL = '/api/posts/' + postSlug + '/comments/';    

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
    })

    var commentBox = $('.comment-content').find('input[name="content"]');
    
    $('.comment-content').submit(function() {
        var content = $(commentBox).val();
        var data = {
            content: content,
        }

        $.ajax({
            url: commentAPIURL,
            type: 'POST',
            data: data,
            success: function(data) {
                var commentContent = data.content;
                var commentUsername = data.username;

                // add comment
                var newCommentLi = $('<li>').text(content);
                $('.comment-list').append(newCommentLi);

                // update comment count
                var commentCount = $('.comment-count').html();
                var newCommentCount = Number(commentCount) + 1;
                $('.comment-count').html(String(newCommentCount));

                $(commentBox).val('');

            },
            error: function(data) {},
        })
        return false;
    });
};

$(document).ready(main)
