from rest_framework import generics
from .models import Skill, Project, Certification, BlogPost
from .serializers import SkillSerializer, ProjectSerializer, CertificationSerializer, BlogPostSerializer

class SkillListAPIView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CertificationListAPIView(generics.ListAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class BlogPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer