from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MobiQuiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'MobiApp.views.index', name='index'),
    url(r'^logout/$', 'MobiApp.views.logout_user', name='logout'),

    url(r'^student/$', 'MobiApp.views.student', name='student'),
    url(r'^faculty_member/$', 'MobiApp.views.faculty_member', name='faculty_member'),
    url(r'^administrator/$', 'MobiApp.views.administrator', name='administrator'),

    url(r'^administrator/user_management/$', 'MobiApp.views.ad_user_management', name='ad_user_management'),
    url(r'^administrator/create_user/$', 'MobiApp.views.ad_create_user', name='ad_create_user'),
    url(r'^administrator/edit_user/(?P<u_id>\d+)/$', 'MobiApp.views.ad_edit_user', name='ad_edit_user'),

    url(r'^administrator/degree_program_management/$', 'MobiApp.views.ad_degree_program_management',
        name='ad_degree_program_management'),
    url(r'^administrator/add_degree_program/$', 'MobiApp.views.ad_add_degree_program', name='ad_add_degree_program'),
    url(r'^administrator/edit_degree_program/(?P<deg_id>\d+)/$', 'MobiApp.views.ad_edit_degree_program',
        name='ad_edit_degree_program'),
    url(r'^administrator/edit_degree_program/(?P<deg_id>\d+)/delete/$', 'MobiApp.views.ad_del_degree_program',
        name='ad_del_degree_program'),

    url(r'^administrator/course_management/$', 'MobiApp.views.ad_course_management', name='ad_course_management'),
    url(r'^administrator/add_course/$', 'MobiApp.views.ad_add_course', name='ad_add_course'),
    url(r'^administrator/edit_course/(?P<cou_id>\d+)/$', 'MobiApp.views.ad_edit_course', name='ad_edit_course'),
    url(r'^administrator/edit_course/(?P<cou_id>\d+)/delete/$', 'MobiApp.views.ad_del_course', name='ad_del_course'),

    url(r'^administrator/semester/$', 'MobiApp.views.ad_semester', name='ad_semester'),
    url(r'^administrator/add_semester/$', 'MobiApp.views.ad_add_semester', name='ad_add_semester'),
    url(r'^administrator/edit_semester/(?P<sem_id>\d+)/$', 'MobiApp.views.ad_edit_semester', name='ad_edit_semester'),
    url(r'^administrator/edit_semester/(?P<sem_id>\d+)/delete/$', 'MobiApp.views.ad_del_semester',
        name='ad_del_semester'),

    url(r'^administrator/assign_course_faculty/$', 'MobiApp.views.ad_assign_course_faculty',
        name='ad_assign_course_faculty'),
    url(r'^administrator/assign/$', 'MobiApp.views.ad_new_assign', name='ad_new_assign'),
    url(r'^administrator/update_assign/(?P<acf_id>\d+)/$', 'MobiApp.views.ad_update_assign', name='ad_update_assig'),
    url(r'^administrator/update_assign/(?P<acf_id>\d+)/delete/$', 'MobiApp.views.ad_del_assign', name='ad_del_assign'),

    url(r'^administrator/enroll_student_semester/$', 'MobiApp.views.ad_enroll_student', name='ad_enroll_student'),
    url(r'^administrator/enroll/$', 'MobiApp.views.ad_new_enroll', name='ad_new_enroll'),
    url(r'^administrator/update_enroll/(?P<esc_id>\d+)/$', 'MobiApp.views.ad_update_enroll', name='ad_update_enroll'),
    url(r'^administrator/update_enroll/(?P<esc_id>\d+)/delete/$', 'MobiApp.views.ad_del_enroll', name='ad_del_enroll'),



    url(r'^faculty_member/quiz/$', 'MobiApp.views.fm_quiz', name='fm_quiz'),
    url(r'^faculty_member/create_quiz/$', 'MobiApp.views.fm_create_quiz', name='fm_create_quiz'),
    url(r'^faculty_member/update_quiz/(?P<quiz_id>\d+)/$', 'MobiApp.views.fm_update_quiz', name='fm_update_quiz'),
    url(r'^faculty_member/update_quiz/(?P<quiz_id>\d+)/delete/$', 'MobiApp.views.fm_del_quiz', name='fm_del_quiz'),

    url(r'^faculty_member/question/$', 'MobiApp.views.fm_question', name='fm_question'),
    url(r'^faculty_member/create_question/$', 'MobiApp.views.fm_create_question', name='fm_create_question'),
    url(r'^faculty_member/update_question/(?P<ques_id>\d+)/$', 'MobiApp.views.fm_update_question',
        name='fm_update_question'),
    url(r'^faculty_member/update_question/(?P<ques_id>\d+)/delete/$', 'MobiApp.views.fm_del_question',
        name='fm_del_question'),

    url(r'^faculty_member/view_answers/$', 'MobiApp.views.fm_view_answers', name='fm_view_answers'),

    url(r'^faculty_member/check_quiz/$', 'MobiApp.views.fm_check_quiz', name='fm_check_quiz'),
    url(r'^faculty_member/check_quiz/(?P<quiz_ins>\d+)/$', 'MobiApp.views.fm_check_quiz_instance',
        name='fm_check_quiz_instance'),

    url(r'^faculty_member/results/$', 'MobiApp.views.fm_result', name='fm_result'),
    url(r'^faculty_member/results/(?P<quiz_id>\d+)/$', 'MobiApp.views.fm_result_quiz', name='fm_result_quiz'),



    url(r'^student/start_quiz/$', 'MobiApp.views.st_start_quiz', name='st_start_quiz'),
    url(r'^student/quiz_results/$', 'MobiApp.views.st_quiz_result', name='st_quiz_result'),
    url(r'^student/grade_book/$', 'MobiApp.views.st_grade_book', name='st_grade_book'),
)