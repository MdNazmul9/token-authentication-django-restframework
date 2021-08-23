from rest_framework import generics
from .serializers import PostSerializer
from  .models import Post
from rest_framework.response import Response


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class PostView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # permission_classes = [IsAdminUser]

#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)

class PostCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class=PostSerializer
   