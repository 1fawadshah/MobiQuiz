from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Course(models.Model):
    course_code = models.CharField(max_length=8, unique=True)
    course_name = models.CharField(max_length=128, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.course_code


class Degree(models.Model):
    degree_code = models.CharField(max_length=16, unique=True)
    degree_name = models.CharField(max_length=128, unique=True)
    courses = models.ManyToManyField(Course)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.degree_code


class Semester(models.Model):
    degree = models.ForeignKey(Degree)
    semester_no = models.SmallIntegerField(max_length=4)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return '%s %d' % (self.degree, self.semester_no)


class UserInformation(AbstractUser):
    degree = models.ForeignKey(Degree, null=True, blank=True)
    cell_number = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.username


class Quiz(models.Model):
    course = models.ForeignKey(Course)
    quiz_no = models.SmallIntegerField(max_length=4)
    flag = models.BooleanField(default=True)

    def __str__(self):
        return '%s %d' % (self.course, self.quiz_no)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    course = models.ForeignKey(Course)
    lecture = models.SmallIntegerField(max_length=4)
    question_no = models.SmallIntegerField(max_length=4)
    question_text = models.CharField(max_length=500)
    option_1 = models.CharField(max_length=500)
    option_2 = models.CharField(max_length=500)
    option_3 = models.CharField(max_length=500, null=True, blank=True)
    option_4 = models.CharField(max_length=500, null=True, blank=True)
    option_correct = models.SmallIntegerField(max_length=4)
    question_type = models.CharField(max_length=16)

    def __str__(self):
        return '%s %s %s' % (self.quiz, self.question_text, self.option_correct)


class QuestionAttempt(models.Model):
    question = models.ForeignKey(Question)
    quiz = models.ForeignKey(Quiz)
    userinformation = models.ForeignKey(UserInformation)
    option_select = models.SmallIntegerField(max_length=4)
    is_attempted = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s %d' % (self.userinformation, self.question, self.option_select)


class QuizAttempt(models.Model):
    quiz = models.ForeignKey(Quiz)
    userinformation = models.ForeignKey(UserInformation)
    course = models.ForeignKey(Course)
    is_attempted = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s %s' % (self.userinformation, self.quiz, str(self.is_attempted))


class ResultQuiz(models.Model):
    userinformation = models.ForeignKey(UserInformation)
    quiz = models.ForeignKey(Quiz)
    course = models.ForeignKey(Course)
    marks_obtained = models.SmallIntegerField(max_length=4)
    total_marks = models.SmallIntegerField(max_length=4)

    def __str__(self):
        return '%s %d' % (self.userinformation, self.marks_obtained)


class ResultCourse(models.Model):
    userinformation = models.ForeignKey(UserInformation)
    course = models.ForeignKey(Course)
    marks_obtained = models.SmallIntegerField(max_length=4)
    total_marks = models.SmallIntegerField(max_length=4)

    def __str__(self):
        return '%s %d' % (self.userinformation, self.marks_obtained)


class GradeBook(models.Model):
    userinformation = models.ForeignKey(UserInformation)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return '%s %s' % (self.userinformation, str(self.cgpa))


class AssignCoursesToFM(models.Model):
    user = models.ForeignKey(UserInformation)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return '%s' % self.user


class EnrollStudentToCourse(models.Model):
    user = models.ForeignKey(UserInformation)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return '%s %s' % (self.user, self.course)