from django.contrib import admin
from MobiApp.models import *

# Register your models here.
admin.site.register(Degree)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(UserInformation)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuestionAttempt)
admin.site.register(QuizAttempt)
admin.site.register(ResultQuiz)
admin.site.register(ResultCourse)
admin.site.register(GradeBook)
admin.site.register(AssignCoursesToFM)
admin.site.register(EnrollStudentToCourse)