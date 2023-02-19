from .models import Post
import django_filters

class Filter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['category']