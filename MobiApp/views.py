from django.shortcuts import render, redirect
from MobiApp.forms import LoginForm, CreateUserForm, EditUserForm, AddDegreeProgram, EditDegreeProgram, AddCourse,\
    EditCourse, AddSemester, EditSemester, AssignCourseFaculty, AssignCourseFacultyChange, EnrollStudent, \
    EnrollStudentChange, CreateQuiz, UpdateQuiz, CreateQuestion, UpdateQuestion
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from MobiApp.models import UserInformation, Degree, Course, Semester, AssignCoursesToFM, EnrollStudentToCourse, Quiz, \
    Question, QuestionAttempt, QuizAttempt, GradeBook, ResultQuiz


# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active and user.groups.filter(name='student').exists():
                login(request, user)
                return HttpResponseRedirect('/student/')
            if user.is_active and user.groups.filter(name='faculty_member').exists():
                login(request, user)
                return HttpResponseRedirect('/faculty_member/')
            if user.is_active and user.groups.filter(name='administrator').exists():
                login(request, user)
                return HttpResponseRedirect('/administrator/')
    return render(request, 'MobiApp/index.html', {'form': LoginForm()})


def not_in_student_group(user):
    if user:
        return user.groups.filter(name='student').exists()
    return False
@login_required()
@user_passes_test(not_in_student_group)
def student(request):
    if not request.user.is_authenticated():
        return redirect('/?next=%s' % request.path)
    return render(request, 'MobiApp/student_index.html', RequestContext(request))


def not_in_faculty_member_group(user):
    if user:
        return user.groups.filter(name='faculty_member').exists()
    return False
@login_required()
@user_passes_test(not_in_faculty_member_group)
def faculty_member(request):
    if not request.user.is_authenticated():
        return redirect('/?next=%s' % request.path)
    return render(request, 'MobiApp/faculty_member_index.html', RequestContext(request))


def not_in_administrator_group(user):
    if user:
        return user.groups.filter(name='administrator').exists()
    return False
@login_required()
@user_passes_test(not_in_administrator_group)
def administrator(request):
    if not request.user.is_authenticated():
        return redirect('/?next=%s' % request.path)
    return render(request, 'MobiApp/administrator_index.html', RequestContext(request))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_user_management(request):
    admin_users_list = UserInformation.objects.filter(groups__name='administrator')
    faculty_member_users_list = UserInformation.objects.filter(groups__name='faculty_member')
    student_users_list = UserInformation.objects.filter(groups__name='student')
    return render(request, 'MobiApp/user_management.html', {'admin_users_list': admin_users_list,
                                                            'faculty_member_users_list': faculty_member_users_list,
                                                            'student_users_list': student_users_list})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            group = request.POST['group']
            #degree = request.POST['degree']
            #cell_no = request.POST['cell_no']
            new_user = UserInformation.objects.create_user(username, email, password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            #new_user = UserInformation(cell_number=cell_no)
            new_user.save()

            if group == 'option_one':
                new_user.groups.add(3)
                #userinfo = UserInformation(username=new_user)
                #userinfo.degree = Degree.objects.get(pk=degree)
                #userinfo = UserInformation(username=new_user, degree=Degree.objects.get(pk=degree), cell_number=cell_no)
                #userinfo.save()
            if group == 'option_two':
                new_user.groups.add(2)
                #userinfo = UserInformation(user=new_user, cell_number=cell_no)
                #userinfo.save()
            if group == 'option_three':
                new_user.groups.add(1)
                #userinfo = UserInformation(user=new_user, cell_number=cell_no)
                #userinfo = UserInformation(stakeholder=Stakeholder.objects.get(pk=set_group), cell_number=cell_no)
                #userinfo.save()
            return HttpResponseRedirect('/administrator/user_management/')
    else:
        form = CreateUserForm()
    return render(request, 'MobiApp/create_user.html', {'form': form})


def ad_edit_user(request, u_id):
    current_user = UserInformation.objects.get(pk=int(u_id))
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/administrator/user_management/')
    else:
        form = EditUserForm(instance=current_user)
    return render(request, 'MobiApp/edit_user.html', {'form': form, 'u_id': u_id})


################# LOCKED #################


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_degree_program_management(request):
    degree_program_list = Degree.objects.all()
    return render(request, 'MobiApp/degree_program_management.html', {'degree_program_list': degree_program_list})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_add_degree_program(request):
    if request.method == 'POST':
        form = AddDegreeProgram(request.POST)
        if form.is_valid():
            degree_code = request.POST['degree_code']
            degree_name = request.POST['degree_name']
            add_degree = Degree(degree_code=degree_code, degree_name=degree_name)
            add_degree.save()
            return HttpResponseRedirect('/administrator/degree_program_management/')
    else:
        form = AddDegreeProgram()
    return render(request, 'MobiApp/add_degree_program.html', {'form': form})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_edit_degree_program(request, deg_id):
    select_degree = Degree.objects.get(pk=int(deg_id))
    if request.method == 'POST':
        form = EditDegreeProgram(request.POST, instance=select_degree)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/administrator/degree_program_management/')
    else:
        form = EditDegreeProgram(instance=select_degree)
    return render(request, 'MobiApp/edit_degree_program.html', {'form': form, 'deg_id': deg_id})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_del_degree_program(request, deg_id):
    select_degree = Degree.objects.get(pk=int(deg_id))
    select_degree.delete()
    return HttpResponseRedirect('/administrator/degree_program_management/')


################# LOCKED #################

################# LOCKED #################


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_course_management(request):
    course_list = Course.objects.all()
    return render(request, 'MobiApp/course_management.html', {'course_list': course_list})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_add_course(request):
    if request.method == 'POST':
        form = AddCourse(request.POST)
        if form.is_valid():
            course_code = request.POST['course_code']
            course_name = request.POST['course_name']
            add_course = Course(course_code=course_code, course_name=course_name)
            add_course.save()
            return HttpResponseRedirect('/administrator/course_management/')
    else:
        form = AddCourse()
    return render(request, 'MobiApp/add_course.html', {'form': form})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_edit_course(request, cou_id):
    select_course = Course.objects.get(pk=int(cou_id))
    if request.method == 'POST':
        form = EditCourse(request.POST, instance=select_course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/administrator/course_management/')
    else:
        form = EditCourse(instance=select_course)
    return render(request, 'MobiApp/edit_course.html', {'form': form, 'cou_id': cou_id})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_del_course(request, cou_id):
    select_course = Course.objects.get(pk=int(cou_id))
    select_course.delete()
    return HttpResponseRedirect('/administrator/course_management/')


################# LOCKED #################

################# LOCKED #################


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_semester(request):
    semester_list = Semester.objects.all()
    return render(request, 'MobiApp/semester.html', {'semester_list': semester_list})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_add_semester(request):
    if request.method == 'POST':
        form = AddSemester(request.POST)
        if form.is_valid():
            degree = request.POST['degree']
            semester_no = request.POST['semester_no']
            add_semester = Semester(degree=Degree.objects.get(pk=degree), semester_no=semester_no)
            add_semester.save()
            return HttpResponseRedirect('/administrator/semester/')
    else:
        form = AddSemester()
    return render(request, 'MobiApp/add_semester.html', {'form': form})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_edit_semester(request, sem_id):
    select_semester = Semester.objects.get(pk=int(sem_id))
    if request.method == 'POST':
        form = EditSemester(request.POST, instance=select_semester)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/administrator/semester/')
    else:
        form = EditSemester(instance=select_semester)
    return render(request, 'MobiApp/edit_semester.html', {'form': form, 'sem_id': sem_id})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_del_semester(request, sem_id):
    select_semester = Semester.objects.get(pk=int(sem_id))
    select_semester.delete()
    return HttpResponseRedirect('/administrator/semester/')


################# LOCKED #################

################# LOCKED #################


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_assign_course_faculty(request):
    assign_list = AssignCoursesToFM.objects.all()
    return render(request, 'MobiApp/assign_course_faculty.html', {'assign_list': assign_list})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_new_assign(request):
    if request.method == 'POST':
        form = AssignCourseFaculty(request.POST)
        if form.is_valid():
            user = request.POST['user']
            new_assign = AssignCoursesToFM(user=UserInformation.objects.get(pk=user))
            new_assign.save()
            return HttpResponseRedirect('/administrator/assign_course_faculty/')
    else:
        form = AssignCourseFaculty()
    return render(request, 'MobiApp/assign.html', {'form': form})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_update_assign(request, acf_id):
    select_assign = AssignCoursesToFM.objects.get(pk=int(acf_id))
    if request.method == 'POST':
        form = AssignCourseFacultyChange(request.POST, instance=select_assign)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/administrator/assign_course_faculty/')
    else:
        form = AssignCourseFacultyChange(instance=select_assign)
    return render(request, 'MobiApp/update_assign.html', {'form': form, 'acf_id': acf_id})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_del_assign(request, acf_id):
    select_assign = AssignCoursesToFM.objects.get(pk=int(acf_id))
    select_assign.delete()
    return HttpResponseRedirect('/administrator/assign_course_faculty/')


################# LOCKED #################

################# LOCKED #################


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_enroll_student(request):
    enroll_list = EnrollStudentToCourse.objects.all()
    return render(request, 'MobiApp/enroll_student_semester.html', {'enroll_list': enroll_list})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_new_enroll(request):
    if request.method == 'POST':
        form = EnrollStudent(request.POST)
        if form.is_valid():
            user = request.POST['user']
            new_enroll = EnrollStudentToCourse(user=UserInformation.objects.get(pk=user))
            new_enroll.save()
            return HttpResponseRedirect('/administrator/enroll_student_semester/')
    else:
        form = EnrollStudent()
    return render(request, 'MobiApp/enroll.html', {'form': form})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_update_enroll(request, esc_id):
    select_enroll = EnrollStudentToCourse.objects.get(pk=int(esc_id))
    if request.method == 'POST':
        form = EnrollStudentChange(request.POST, instance=select_enroll)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/administrator/enroll_student_semester/')
    else:
        form = EnrollStudentChange(instance=select_enroll)
    return render(request, 'MobiApp/update_enroll.html', {'form': form, 'esc_id': esc_id})


@login_required()
@user_passes_test(not_in_administrator_group)
def ad_del_enroll(request, esc_id):
    select_enroll = EnrollStudentToCourse.objects.get(pk=int(esc_id))
    select_enroll.delete()
    return HttpResponseRedirect('/administrator/enroll_student_semester/')


################# LOCKED #################

################# LOCKED #################


@login_required()
@user_passes_test(not_in_faculty_member_group)
def fm_quiz(request):
    quiz_list = Quiz.objects.all()
    return render(request, 'MobiApp/quiz.html', {'quiz_list': quiz_list})


@login_required()
@user_passes_test(not_in_faculty_member_group)
def fm_create_quiz(request):
    if request.method == 'POST':
        form = CreateQuiz(request.POST)
        if form.is_valid():
            course = request.POST['course']
            quiz_no = request.POST['quiz_no']
            add_quiz = Quiz(course=Course.objects.get(pk=course), quiz_no=quiz_no)
            add_quiz.save()
            return HttpResponseRedirect('/faculty_member/quiz/')
    else:
        form = CreateQuiz()
    return render(request, 'MobiApp/add_quiz.html', {'form': form})


@login_required()
@user_passes_test(not_in_faculty_member_group)
def fm_update_quiz(request, quiz_id):
    select_quiz = Quiz.objects.get(pk=int(quiz_id))
    if request.method == 'POST':
        form = UpdateQuiz(request.POST, instance=select_quiz)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/faculty_member/quiz/')
    else:
        form = UpdateQuiz(instance=select_quiz)
    return render(request, 'MobiApp/update_quiz.html', {'form': form, 'quiz_id': quiz_id})


@login_required()
@user_passes_test(not_in_faculty_member_group)
def fm_del_quiz(request, quiz_id):
    select_quiz = Quiz.objects.get(pk=int(quiz_id))
    select_quiz.delete()
    return HttpResponseRedirect('/faculty_member/quiz/')


################# LOCKED #################


@login_required()
@user_passes_test(not_in_faculty_member_group)
def fm_question(request):
    question_list = Question.objects.all()
    return render(request, 'MobiApp/question.html', {'question_list': question_list})


@login_required()
@user_passes_test(not_in_faculty_member_group)
def fm_create_question(request):
    if request.method == 'POST':
        form = CreateQuestion(request.POST)
        if form.is_valid():
            quiz = request.POST['quiz']
            course = request.POST['course']
            lecture = request.POST['lecture']
            question_no = request.POST['question_no']
            question_text = request.POST['question_text']
            option_1 = request.POST['option_1']
            option_2 = request.POST['option_2']
            option_3 = request.POST['option_3']
            option_4 = request.POST['option_4']
            option_correct = request.POST['option_correct']
            question_type = request.POST['question_type']
            add_question = Question(quiz=Quiz.objects.get(pk=quiz), course=Course.objects.get(pk=course),
                                    lecture=lecture, question_no=question_no, question_text=question_text,
                                    option_1=option_1, option_2=option_2, option_3=option_3, option_4=option_4,
                                    option_correct=option_correct, question_type=question_type)
            add_question.save()
            return HttpResponseRedirect('/faculty_member/question/')
    else:
        form = CreateQuestion()
    return render(request, 'MobiApp/add_question.html', {'form': form})


@login_required()
@user_passes_test(not_in_faculty_member_group)
def fm_update_question(request, ques_id):
    select_question = Question.objects.get(pk=int(ques_id))
    if request.method == 'POST':
        form = UpdateQuestion(request.POST, instance=select_question)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/faculty_member/question/')
    else:
        form = UpdateQuestion(instance=select_question)
    return render(request, 'MobiApp/update_question.html', {'form': form, 'ques_id': ques_id})


@login_required()
@user_passes_test(not_in_faculty_member_group)
def fm_del_question(request, ques_id):
    select_question = Question.objects.get(pk=int(ques_id))
    select_question.delete()
    return HttpResponseRedirect('/faculty_member/question/')


@login_required()
@user_passes_test(not_in_faculty_member_group)
def fm_view_answers(request):
    view_answers_list = QuestionAttempt.objects.all()
    return render(request, 'MobiApp/view_answers.html', {'view_answers_list': view_answers_list})


@login_required()
@user_passes_test(not_in_faculty_member_group)
def fm_check_quiz(request):
    list_quiz = Quiz.objects.all()
    return render(request, 'MobiApp/check_quiz.html', {'list_quiz': list_quiz})


@login_required()
@user_passes_test(not_in_faculty_member_group)
def fm_check_quiz_instance(request, quiz_ins):
    all_answers = QuestionAttempt.objects.filter(quiz=quiz_ins)
    return render(request, 'MobiApp/check_quiz_instance.html', {'all_answers': all_answers, 'quiz_ins': quiz_ins})


@login_required()
@user_passes_test(not_in_faculty_member_group)
def fm_result(request):
    result_list = QuizAttempt.objects.all()
    return render(request, 'MobiApp/result.html', {'result_list': result_list})


@login_required()
@user_passes_test(not_in_faculty_member_group)
def fm_result_quiz(request, quiz_id):
    result_quiz = QuestionAttempt.objects.filter(quiz=quiz_id).values('option_select', 'question')
    return render(request, 'MobiApp/result_quiz.html', {'result_quiz': result_quiz, 'quiz_id': quiz_id})


@login_required()
@user_passes_test(not_in_student_group)
def st_start_quiz(request):
    start_quiz = Quiz.objects.all()
    return render(request, 'MobiApp/start_quiz.html', {'start_quiz': start_quiz})


@login_required()
@user_passes_test(not_in_student_group)
def st_grade_book(request):
    grade_book = GradeBook.objects.all()
    return render(request, 'MobiApp/gradebook.html', {'grade_book': grade_book})


@login_required()
@user_passes_test(not_in_student_group)
def st_quiz_result(request):
    quiz_result = ResultQuiz.objects.all()
    return render(request, 'MobiApp/result_quiz_student.html', {'quiz_result': quiz_result})