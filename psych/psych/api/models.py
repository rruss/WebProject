from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profileDetail(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender_choice = (
        ('M', 'Male'),
        ('FM', 'Female')
    )
    gender = models.CharField(default='Male', choices=gender_choice, max_length=6)
    date_of_birth = models.DateField()
    region_choice = (
        ('NS', 'Nur-Sultan'),
        ('AL', 'Almaty'),
        ('SH', 'Shymkent'),
        ('AKT', 'Aktau'),
        ('AK', 'Aktobe'),
        ('AT', 'Atyrau'),
        ('KR', 'Karaganda'),
        ('KT', 'Kokshetau'),
        ('KO', 'Kyzylorda'),
        ('OL', 'Oral'),
        ('OS', 'Oskemen'),
        ('PV', 'Pavlodar'),
        ('PT', 'Petropavl'),
        ('SM', 'Semey'),
        ('TZ', 'Taraz'),
        ('TR', 'Turkistan'),
        ('ZO', 'Zhanaozen'),
        ('ZK', 'Zhezkazgan')
    )
    region = models.CharField(default='Nur-Sultan', choices=region_choice, max_length=20)
    # count_of_tests = models.IntegerField()
    # result_of_tests = models.IntegerField()

    def __str__(self):
        return '{}: {}, {}, {}, {}' .format(self.id, self.full_name, self.email, self.date_of_birth, self.region)

    def to_json(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'date_of_birth': self.date_of_birth,
            'region': self.region
        }

class Title(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

class Question(models.Model):
    question = models.CharField(max_length=200)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return '{}: {}, {}'.format(self.id, self.question, self.title)

class ok_Answer(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, default=1, related_name='okanswers')
    quesId = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='quesId')
    ok_answer = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}, {}'.format(self.id, self.ok_answer, self.quesId)

class Answer(models.Model):
    answer = models.CharField(max_length=1000)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return '{}.{}: {}'.format(self.question, self.id, self.answer)

class Results(models.Model):
    test_name = models.CharField(max_length=100)
    test_result = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='results')

class Images(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return '{}: {} - {}'.format(self.id, self.image, self.user)