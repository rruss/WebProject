from django.http import JsonResponse, Http404
import json
from rest_framework import generics, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from ..models import profileDetail, Title, Answer, ok_Answer, Question, User, Results, Images
from ..serializers import UserImageSerializer, ProfileDetailSerializer,ResultSerializer,UserResultSerializer, OkAnswerSerializer, TitleSerializer, \
    TitleSerializer2, QuestionSerializer, UserSerializer, AnswerSerializer, updateUserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import admin

# def HomePage(request):
#     return render()

class userView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class user_detail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class user_detail_c(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class profile(generics.ListCreateAPIView):
    queryset = profileDetail.objects.all()
    serializer_class = ProfileDetailSerializer
    permission_classes = (IsAuthenticated, )

class profiledetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = profileDetail.objects.all()
    serializer_class = ProfileDetailSerializer
    permission_classes = (IsAuthenticated, )

class okanswer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = OkAnswerSerializer

class results(generics.ListCreateAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultSerializer

class updateUser(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = updateUserSerializer

@api_view(['GET', 'POST'])
def results_fbv(request):
    if request.method == 'GET':
        results = Results.objects.all()
        serializer = ResultSerializer(results, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class title(generics.ListAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAuthenticated, )

class title_c(APIView):
    def get(self, request):
        titles = Title.objects.all()
        serializer = TitleSerializer2(titles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TitleSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class user_reg(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET', 'POST'])
def user_reg_f(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class detailtitle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer2


class question(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # t = Question.objects.all()
    # serializer = QuestionSerializer(t, many=True)
    # if request.method == 'GET':
    #     return JsonResponse(serializer.data, safe=False)
    # return JsonResponse(serializer.errors)




class answer(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class userresult(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserResultSerializer