from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from exam.models import School
from exam.serializer.ExamSerializer import SchoolSerializer


class SchoolList(APIView):
    def get(self, request):
        print("..SchoolList......",request)
        school = School.objects.all()
        print("..SchoolList...22...",school)
        #serializer_class = SchoolSerializer
        serializer = SchoolSerializer(school, many=True)
        return Response({"school": serializer.data})

    def post(self, request):
        article = request.data.get('school')

        # Create an article from the above data
        serializer = SchoolSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "School '{}' updated successfully".format(article_saved.name)})

    def put(self, request, pk):
        saved_article = get_object_or_404(School.objects.all(), id=pk)
        data = request.data.get('school')
        serializer = SchoolSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(article_saved.name)})

    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(School.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)
