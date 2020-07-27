from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from exam.models import Student
from exam.serializer.StudentSerializer import StudentSerializer
from exam.views.exam import sendinblue_emailSend


class StudentAPI(APIView):
    def get(self, request):
        print("..StudentAPI......",request)
        student = Student.objects.all()
        print("..StudentAPI...22...",student)
        serializer = StudentSerializer(student, many=True)
        return Response({"student": serializer.data})

    def post(self, request):
        print( "...StudentAPI post....333..", request)
        students = request.data.get('student')
        objects = list(request.data.get('student'))

        print(objects, "...StudentAPI post......", students)
        # Create an article from the above data
        try:
            for stud in objects:
                try:
                    #print(stud['is_approved'] ,"...StudentAPI post..333....", stud['id'])
                    saved_article = get_object_or_404(Student.objects.all(), id=stud['id'])
                    #print("...StudentAPI post..5555....", saved_article)
                    serializer = StudentSerializer(instance=saved_article, data=stud, partial=True)
                    #print("...StudentAPI post..44444....", serializer)
                    if serializer.is_valid(raise_exception=True):
                        article_saved = serializer.save()
                        #print("...StudentAPI email....", stud['status'])
                        #print("...StudentAPI email.ggg...", saved_article.user.first_name)

                        if stud['status'] == 1:
                            htmlMessage = ("<html><head></head><body><p>Hello, %s</p>We are delighted to inform you that your  registration  for the November 2020 catechism examination is approved!  <br> Your registration number is %s.  Please use the registration number as your username to log into to the examination portal. <br><br> Regards, <br> Centralized Exam Panel Director  <br> ------------------------------------------------------- <br>Powered by Team MAVA</p></body></html>" %(saved_article.user.first_name,saved_article.user.username ))
                        else:
                            htmlMessage = ("<html><head></head><body><p>Hello, %s</p>We are sorry, your  registration  for the November 2020 catechism examination is rejected. <br> Please contact your local catechism  department for  further information  and to resolve the issues.<br>We regret the inconvenience caused. <br><br> Regards, <br> Centralized Exam Panel Director  <br> ------------------------------------------------------- <br>Powered by Team MAVA</p></body></html>" %(saved_article.user.first_name))
                        print("...StudentAPI email....", htmlMessage)
                        data = { "sender":{  
                            "name":"Mava Partners",
                            "email":"mava.partnersin@gmail.com"},
                            "to":[  
                            {  
                                "email":"mava.partnersin@gmail.com",
                                "name":"Mava Partners"
                            },
                            {  
                                "email":saved_article.user.email,
                                "name":saved_article.user.first_name
                            }
                            ],
                            "subject":"Malankara Syrian Orthodox Sunday School Association of North America",
                            "htmlContent":htmlMessage
                        }
                        sendinblue_emailSend(data)
                except self.model.DoesNotExist:
                    print('........student not exist.......')
            return Response({"success": "Student '{}' updated successfully".format(objects.count)})
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_article = get_object_or_404(Student.objects.all(), id=pk)
        data = request.data.get('student')
        serializer = StudentSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(article_saved.user.username)})

    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(Student.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)
