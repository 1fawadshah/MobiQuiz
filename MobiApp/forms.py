from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions
from MobiApp.models import Degree, UserInformation, Course, Semester, AssignCoursesToFM, EnrollStudentToCourse, Quiz, \
    Question


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('username', required=True, css_class='input-xlarge'),
        Field('password', required=True, css_class='input_xlarge'),
        FormActions(
            Submit('login', 'Login!', css_class="btn-primary"),
        )
    )


class CreateUserForm(forms.Form):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    username = forms.CharField(max_length=16)
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )
    email = forms.EmailField()
    group = forms.ChoiceField(
        choices=(
            ('option_one', "Student"),
            ('option_two', "Faculty Member"),
            ('option_three', "Administrator"),
        ),
        widget = forms.RadioSelect,
        initial = 'option_one',
    )
    #degree = forms.ModelChoiceField(queryset=Degree.objects.all())
    #cell_no = forms.CharField()

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('first_name', required=True, css_class='input-xlarge'),
        Field('last_name', required=True, css_class='input-xlarge'),
        Field('username', required=True, css_class='input-xlarge'),
        Field('password', required=True, css_class='input-xlarge'),
        Field('email', required=True, css_class='input-xlarge'),
        'group',
        #'degree',
        #Field('cell_no', required=True, css_class='input-xlarge'),
        FormActions(
            Submit('create', 'Create!', css_class="btn-primary"),
        )
    )


class EditUserForm(forms.ModelForm):
    #group = forms.ChoiceField(
    #    choices=(
    #        ('option_one', "Student"),
    #        ('option_two', "Faculty Member"),
    #        ('option_three', "Administrator"),
    #    ),
    #    widget = forms.RadioSelect,
    #    initial = 'option_one',
    #)
    #degree = forms.ModelChoiceField(queryset=Degree.objects.all())
    #cell_no = forms.CharField()

    class Meta:
        model = UserInformation
        #exclude = ('user', 'username', 'email', 'password',)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('first_name', required=True, css_class='input-xlarge'),
        Field('last_name', required=True, css_class='input-xlarge'),
        Field('username', required=True, css_class='input-xlarge'),
        Field('password', required=True, css_class='input-xlarge'),
        Field('email', required=True, css_class='input-xlarge'),
        #'group',
        #'degree',
        #Field('cell_number', required=True, css_class='input-xlarge'),
        FormActions(
            Submit('update', 'Update!', css_class="btn-primary"),
        )
    )


################# LOCKED #################


class AddDegreeProgram(forms.Form):
    degree_code = forms.CharField(max_length=8, required=True)
    degree_name = forms.CharField(max_length=128, required=True)
    #courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple())

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('degree_code', required=True, css_class='input-xlarge'),
        Field('degree_name', required=True, css_class='input-xlarge'),
        FormActions(
            Submit('add', 'Add!', css_class="btn-primary"),
        )
    )


class EditDegreeProgram(forms.ModelForm):

    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Degree

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('degree_code', required=True, css_class='input-xlarge'),
        Field('degree_name', required=True, css_class='input-xlarge'),
        'courses',
        'is_active',
        FormActions(
            Submit('update', 'Update!', css_class="btn-primary"),
        )
    )


################# LOCKED #################

################# LOCKED #################


class AddCourse(forms.Form):
    course_code = forms.CharField(max_length=8)
    course_name = forms.CharField(max_length=128)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('course_code', required=True, css_class='input-xlarge'),
        Field('course_name', required=True, css_class='input-xlarge'),
        FormActions(
            Submit('add', 'Add!', css_class="btn-primary"),
        )
    )


class EditCourse(forms.ModelForm):
    #course_code = forms.CharField(max_length=8, initial=Course.objects.values_list('course_code', flat=True).get(pk=int()))
    #course_name = forms.CharField(max_length=128, initial=Course.objects.values_list('course_name', flat=True).get(pk=int()))
    #is_active = forms.BooleanField(initial=Course.objects.values_list('is_active', flat=True).get(pk=15))

    class Meta:
        model = Course

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('course_code', required=True, css_class='input-xlarge'),
        Field('course_name', required=True, css_class='input-xlarge'),
        'is_active',
        FormActions(
            Submit('update', 'Update!', css_class="btn-primary"),
        )
    )


################# LOCKED #################

################# LOCKED #################


class AddSemester(forms.Form):
    degree = forms.ModelChoiceField(queryset=Degree.objects.all())
    semester_no = forms.CharField(max_length=128)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        'degree',
        Field('semester_no', required=True, css_class='input-xlarge'),
        FormActions(
            Submit('add', 'Add!', css_class="btn-primary"),
        )
    )


class EditSemester(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Semester

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('degree', required=True, css_class='input-xlarge'),
        Field('semester_no', required=True, css_class='input-xlarge'),
        'courses',
        FormActions(
            Submit('update', 'Update!', css_class="btn-primary"),
        )
    )


################# LOCKED #################

################# LOCKED #################


class AssignCourseFaculty(forms.Form):
    user = forms.ModelChoiceField(queryset=UserInformation.objects.filter(groups__name='faculty_member'))

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        'user',
        FormActions(
            Submit('assign', 'Assign!', css_class="btn-primary"),
        )
    )


class AssignCourseFacultyChange(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=UserInformation.objects.filter(groups__name='faculty_member'))
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = AssignCoursesToFM

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        'user',
        'courses',
        FormActions(
            Submit('update', 'Update!', css_class="btn-primary"),
        )
    )


################# LOCKED #################


class EnrollStudent(forms.Form):
    user = forms.ModelChoiceField(queryset=UserInformation.objects.filter(groups__name='student'))

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        'user',
        FormActions(
            Submit('enroll', 'Enroll!', css_class="btn-primary"),
        )
    )


class EnrollStudentChange(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=UserInformation.objects.filter(groups__name='student'))
    course = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = EnrollStudentToCourse

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        'user',
        'course',
        FormActions(
            Submit('update', 'Update!', css_class="btn-primary"),
        )
    )


################# LOCKED #################

################# LOCKED #################


class CreateQuiz(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    quiz_no = forms.IntegerField(max_value=15, min_value=1)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        'course',
        Field('quiz_no', required=True, css_class='input-xlarge'),
        FormActions(
            Submit('create', 'Create!', css_class="btn-primary"),
        )
    )


class UpdateQuiz(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    quiz_no = forms.IntegerField(max_value=15, min_value=1)
    flag = forms.BooleanField

    class Meta:
        model = Quiz

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        'course',
        Field('quiz_no', required=True, css_class='input-xlarge'),
        'flag',
        FormActions(
            Submit('update', 'Update!', css_class="btn-primary"),
        )
    )


################# LOCKED #################

################# LOCKED #################


class CreateQuestion(forms.Form):
    quiz = forms.ModelChoiceField(queryset=Quiz.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    lecture = forms.IntegerField(max_value=50, min_value=1)
    question_no = forms.IntegerField(max_value=100, min_value=1)
    question_text = forms.CharField(max_length=500)
    option_1 = forms.CharField(max_length=500)
    option_2 = forms.CharField(max_length=500)
    option_3 = forms.CharField(max_length=500)
    option_4 = forms.CharField(max_length=500)
    option_correct = forms.IntegerField(max_value=4, min_value=1)
    question_type = forms.CharField(max_length=16)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        'quiz',
        'course',
        Field('lecture', required=True, css_class='input-xlarge'),
        Field('question_no', required=True, css_class='input-xlarge'),
        Field('question_text', required=True, css_class='input-xlarge'),
        Field('option_1', required=True, css_class='input-xlarge'),
        Field('option_2', required=True, css_class='input-xlarge'),
        Field('option_3', required=False, css_class='input-xlarge'),
        Field('option_4', required=False, css_class='input-xlarge'),
        Field('option_correct', required=True, css_class='input-xlarge'),
        Field('question_type', required=True, css_class='input-xlarge'),

        FormActions(
            Submit('create', 'Create!', css_class="btn-primary"),
        )
    )


class UpdateQuestion(forms.ModelForm):
    #course = forms.ModelChoiceField(queryset=Course.objects.all())
    #quiz_no = forms.IntegerField(max_value=15, min_value=1)
    #flag = forms.BooleanField

    class Meta:
        model = Question

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        'quiz',
        'course',
        Field('lecture', required=True, css_class='input-xlarge'),
        Field('question_no', required=True, css_class='input-xlarge'),
        Field('question_text', required=True, css_class='input-xlarge'),
        Field('option_1', required=True, css_class='input-xlarge'),
        Field('option_2', required=True, css_class='input-xlarge'),
        Field('option_3', required=False, css_class='input-xlarge'),
        Field('option_4', required=False, css_class='input-xlarge'),
        Field('option_correct', required=True, css_class='input-xlarge'),
        Field('question_type', required=True, css_class='input-xlarge'),
        FormActions(
            Submit('update', 'Update!', css_class="btn-primary"),
        )
    )