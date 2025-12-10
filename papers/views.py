from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .models import Paper
from .serializers import PaperSerializer, LevelSerializer, SubjectSerializer
from .utils.filters import PaperFilter

# Home page route
@api_view(['GET'])
def index(request):
    # We should add the following functionalities in this route:
    # Done: Filter by Level: /api/papers/?level=MSCE
    # Done:Filter by Level & Subject: /api/papers/?level=MSCE&subject=Mathematics
    # Done:Search by Keyword: /api/papers/?search=English
    # We should implement pagination for large datasets(to be implemented later).

    paper_filter = PaperFilter(request.GET, queryset=Paper.objects.all())
    papers = paper_filter.qs
    serializer = PaperSerializer(papers, many=True)
    papers = serializer.data

    return Response({'papers': papers}, status=status.HTTP_200_OK)

# Read paper route
@api_view(['GET'])
def read_paper(request, paper_id):
    try:
        paper = Paper.objects.get(id=paper_id)
    except Paper.DoesNotExist:
        return Response({'error': 'Paper not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PaperSerializer(paper)
    return Response({'paper': serializer.data}, status=status.HTTP_200_OK)

# List all examination levels route
@api_view(['GET'])
def examination_levels(request):
    # Placeholder
    levels = []

    return Response({'examination_levels': levels}, status=status.HTTP_200_OK)

# List all subjects route
@api_view(['GET'])
def subjects(request):
    # Placeholder
    subjects = []

    return Response({'subjects': subjects}, status=status.HTTP_200_OK)

# List paper stats route
@api_view(['GET'])
def paper_stats(request):
    # Placeholder
    stats = {}

    return Response({'paper_stats': stats}, status=status.HTTP_200_OK)

# Download paper route
@login_required(login_url='users:login')
@api_view(['GET'])
def download_paper(request, paper_id):
    return Response({'message': 'Paper downloaded successfully!'}, status.HTTP_200_OK)

# Show downloaded papers
@login_required(login_url='users:login')
@api_view(['GET'])
def show_downloads(request):
    # Placeholder
    downloads = []

    return Response({'downloads': downloads}, status=status.HTTP_200_OK)