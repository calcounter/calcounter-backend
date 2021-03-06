from api.models import Meal, Profile
from api.serializers import MealSerializer, ProfileSerializer
from rest_framework import viewsets, permissions, renderers
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, detail_route
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination

#class SmallResultsSetPagination(PageNumberPagination):
 #   page_size = 10
  #  page_size_query_param = 'page_size'
   # max_page_size = 100

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]
    #pagination_class = SmallResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)

    def get_queryset(self):
        return self.request.user.profile.meals.all()


class ProfileView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


@api_view(('GET',))
def api_root(request, format=None):

    return Response({
        'profiles': reverse('profile-list', request=request, format=format),
        'meals': reverse('meal-list', request=request, format=format)
    })

