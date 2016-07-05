from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from posts.models import Post
from posts.serializers import CommentModelSerializer


class PostCommentListAPIView(ListAPIView):
    serializer_class = CommentModelSerializer

    def get_queryset(self):
        post = Post.objects.get(hash_id=self.kwargs.get('slug'))
        queryset = post.comment_set.all()
        return queryset

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(hash_id=self.kwargs.get('slug'))
        comment = post.comment_set.create(
                user=self.request.user,
                content=request.POST.get('content')
        )

        return Response(
                status=status.HTTP_201_CREATED,
                data={
                    'username': request.user.username,
                    'content': comment.content,
                }
        )
