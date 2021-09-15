from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

import groups.api_views
from events.views import GroupEventsView

urlpatterns = [
    path("", groups.api_views.GroupList.as_view(), name="groups-list"),
    path("new", groups.api_views.GroupCreate.as_view(), name="groups-create"),
    path(
        "<int:id>/",
        groups.api_views.GroupRetrieveUpdateDestroy.as_view(),
        name="groups-detail",
    ),
    path("tags/", groups.api_views.TagList.as_view(), name="tags-list"),
    path("tags/new", groups.api_views.TagCreate.as_view(), name="tags-create"),
    path(
        "tags/<int:id>/",
        groups.api_views.TagRetrieveUpdateDestroy.as_view(),
        name="tags-detail",
    ),
    path(
        "categories/", groups.api_views.CategoryList.as_view(), name="categories-list"
    ),
    path(
        "categories/new",
        groups.api_views.CategoryCreate.as_view(),
        name="categories-create",
    ),
    path(
        "categories/<int:id>/",
        groups.api_views.CategoryRetrieveUpdateDestroy.as_view(),
        name="categories-detail",
    ),
    path("members/", groups.api_views.MembersList.as_view(), name="members-list"),
    path(
        "memberships/",
        groups.api_views.MembershipList.as_view(),
        name="memberships-list",
    ),
    path(
        "memberships/new",
        groups.api_views.MembershipCreate.as_view(),
        name="memberships-create",
    ),
    path(
        "memberships/<int:id>/",
        groups.api_views.MembershipRetrieveUpdateDestroy.as_view(),
        name="memberships-detail",
    ),
    path("<int:group_id>/events/new", GroupEventsView.as_view(), name="group-events"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
