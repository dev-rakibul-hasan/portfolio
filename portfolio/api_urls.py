from django.urls import path
from . import api_views

urlpatterns = [
    path('skills/', api_views.SkillListAPIView.as_view(), name='api-skills'),
    path('projects/', api_views.ProjectListAPIView.as_view(), name='api-projects'),
    path('certifications/', api_views.CertificationListAPIView.as_view(), name='api-certifications'),
    path('blogposts/', api_views.BlogPostListAPIView.as_view(), name='api-blogposts'),
]