from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def all_students(request):
    if request.method == 'GET':
        all_students = Student.objects.all()
        serialized_students = StudentSerializer(all_students, many=True)
        return Response(serialized_students.data)
    else:
        student_data = StudentSerializer(data=request.data)
        if student_data.is_valid():
            student_data.save()
            return Response('Thank you for signing up')
        return Response(student_data.errors)
    

@api_view(['GET', 'PUT', 'DELETE'])
def single_student_view(request, id):
    if request.method == 'GET':
        single_student = Student.objects.get(id=id)
        serialized_student = StudentSerializer(single_student)
        return Response(serialized_student.data)
    elif request.method =='PUT':
        single_student = Student.objects.get(id = id)
        serialized_student = StudentSerializer(single_student, data=request.data, partial=True)
        if serialized_student.is_valid():
            serialized_student.save()
            return Response('You have successfully updated this data')
        return Response('Something went wrong')
    else:
        single_student = Student.objects.get(id=id)
        single_student.delete()
        return Response('You have successfully deleted your account')
