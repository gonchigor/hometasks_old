from django.urls import path
from dimensionsapp.views import AuthorDetailView, SerieDetailView, JenreDetailView, PublishingHouseDetailView, \
     FormatBookDetailView, BindingDetailView, AgeRestrictionDetailView, SerieListView, AuthorListView, \
     JenreListView, PublishingHouseListView, FormatBookListView, BindingListView, AgeRestrictionListView, \
     MenuView, SerieCreateView, AuthorCreateView, JenreCreateView, PublishingHouseCreateView, \
     FormatBookCreateView, BindingCreateView, AgeRestrictionCreateView
from django.views.generic import TemplateView
from goodsapp.views import BookDetailView, BookListView

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

    path('serie/create/', SerieCreateView.as_view(), name='serie_create'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('jenre/create/', JenreCreateView.as_view(), name='jenre_create'),
    path('publishing/create/', PublishingHouseCreateView.as_view(), name='publishing_house_create'),
    path('format/create/', FormatBookCreateView.as_view(), name='format_book_create'),
    path('binding/create/', BindingCreateView.as_view(), name='binding_create'),
    path('agerestriction/create/', AgeRestrictionCreateView.as_view(), name='age_restriction_create'),

    path('book/', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('', MenuView.as_view())
]
