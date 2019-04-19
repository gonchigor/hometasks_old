from django.urls import path
from dimensionsapp.views import AuthorDetailView, SerieDetailView, JenreDetailView, PublishingHouseDetailView, \
     FormatBookDetailView, BindingDetailView, AgeRestrictionDetailView, SerieListView, AuthorListView, \
     JenreListView, PublishingHouseListView, FormatBookListView, BindingListView, AgeRestrictionListView
from django.views.generic import TemplateView

urlpatterns = [
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('serie/<int:pk>/', SerieDetailView.as_view(), name='serie_detail'),
    path('jenre/<int:pk>/', JenreDetailView.as_view(), name='jenre_detail'),
    path('publishing/<int:pk>/', PublishingHouseDetailView.as_view(), name='publishing_house_detail'),
    path('format/<int:pk>/', FormatBookDetailView.as_view(), name='format_book_detail'),
    path('binding/<int:pk>/', BindingDetailView.as_view(), name='binding_detail'),
    path('agerestriction/<int:pk>/', AgeRestrictionDetailView.as_view(), name='age_restriction_detail'),
    path('author/', AuthorListView.as_view(), name='author_list'),
    path('serie/', SerieListView.as_view(), name='serie_list'),
    path('jenre/', JenreListView.as_view(), name='jenre_list'),
    path('publishing/', PublishingHouseListView.as_view(), name='publishing_house_list'),
    path('format/', FormatBookListView.as_view(), name='format_book_list'),
    path('binding/', BindingListView.as_view(), name='binding_list'),
    path('agerestriction/', AgeRestrictionListView.as_view(), name='age_restriction_list'),
]
