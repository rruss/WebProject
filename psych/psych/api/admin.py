from django.contrib import admin
from .models import profileDetail, Title, Question, Answer, ok_Answer, Results, Images
# Register your models here.
@admin.register(profileDetail)
class profDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'date_of_birth', 'email', 'region')

@admin.register(Title)
class titleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Question)
class queAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'question')

@admin.register(Answer)
class ansAdmin(admin.ModelAdmin):
    list_display = ('question', 'id', 'answer')

@admin.register(ok_Answer)
class ok_ansAdmin(admin.ModelAdmin):
    list_display = ('quesId', 'ok_answer')

@admin.register(Results)
class Result(admin.ModelAdmin):
    list_display = ('id', 'test_name', 'test_result', 'user')

@admin.register(Images)
class imageadmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'user')