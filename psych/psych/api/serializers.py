from rest_framework import serializers
from .models import Title, Question, Answer, ok_Answer, profileDetail, Results, Images
from django.contrib.auth.models import User
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ['image']

class UserImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'images')

class updateUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'age', 'password', 'email', 'is_superuser')

class UserSerializer(serializers.ModelSerializer):
    encoder = BCryptSHA256PasswordHasher()
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'age', 'password', 'email', 'is_superuser')

    def create(self, validated_data):
        # pop and encode password
        password = validated_data.pop('password')
        hashed_password = self.encoder.encode(password, salt=self.encoder.salt())

        # pop and assign group
        user = User.objects.create(**validated_data)
        user.set_password(password)

        user.save()

        return user

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Results
        fields = '__all__'

class okAnsQuesId(serializers.ModelSerializer):
    id =serializers.IntegerField(read_only=True)

    class Meta:
        model = Question
        fields = ['id']

class OK_AnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ok_Answer
        fields = ('id', 'ok_answer', 'quesId')

class OkAnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    okanswers = OK_AnswerSerializer(many=True)

    class Meta:
        model = Title
        fields = ('id', 'okanswers')

class ProfileDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = profileDetail
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer')

class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'question', 'answers')

class TitleSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'questions')

    def create(self, validated_data):
        questions = validated_data.pop('questions')
        title = Title.objects.create(**validated_data)
        arr = [Question(title=title, **q) for q in questions]
        Question.objects.bulk_create(arr)
        return title



class ResultSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Results
        fields = ('id', 'test_name', 'test_result')


class UserResultSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    results = ResultSerializer2(many=True)

    class Meta:
        model = User
        fields = ('id', 'results')