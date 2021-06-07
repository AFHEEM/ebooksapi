# from rest_framework import mixins
from rest_framework import generics
from ebooks.models import Ebook, Review
from ebooks.serializers import EbookSerializer, ReviewSerializer


class EbookListCreateAPIView(generics.ListCreateAPIView):
    """
    List Ebooks
    """
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    List Ebooks
    """
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    """
    Create a Review
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        """
        Override Review creation
        :param serializer:
        :return:
        """
        ebook_pk = self.kwargs.get('ebook_pk')
        ebook = generics.get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update and delete a review object
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# class EbookListCreateAPIView(mixins.ListModelMixin,
#                              mixins.CreateModelMixin,
#                              generics.GenericAPIView):
#     """
#     Display Ebooks as a list
#     """
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer
#
#     def get(self, request, *args, **kwargs):
#         """
#         Get all ebooks
#         :param request:
#         :return:
#         """
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         """
#         Get all ebooks
#         :param request:
#         :return:
#         """
#         return self.create(request, *args, **kwargs)