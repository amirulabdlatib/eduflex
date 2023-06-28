"""eduflex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views,Hod_Views,Staff_Views,Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    path('',views.index,name='index'),


    #login
    path('login/',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),



    #profile update
    path('Profile',views.PROFILE,name='profile'),
    path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),


    #HOD panel url
    path('Hod/Home',Hod_Views.HOME, name='hod_home'),
    path('Hod/Student/Add',Hod_Views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',Hod_Views.VIEW_STUDENT,name='view_student'),
    path('Hod/Student/Edit/<str:id>',Hod_Views.EDIT_STUDENT,name='edit_student'),
    path('Hod/Student/Update',Hod_Views.UPDATE_STUDENT,name='update_student'),
    path('Hod/Student/Delete/<str:admin>',Hod_Views.DELETE_STUDENT,name='delete_student'),



    path('Hod/Staff/Add',Hod_Views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/View',Hod_Views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>',Hod_Views.EDIT_STAFF,name='edit_staff'),
    path('Hod/Staff/Update',Hod_Views.UPDATE_STAFF,name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>',Hod_Views.DELETE_STAFF,name='delete_staff'),



    path('Hod/Course/Add',Hod_Views.ADD_COURSE,name='add_course'),
    path('Hod/Course/View',Hod_Views.VIEW_COURSE,name='view_course'),
    path('Hod/Course/Edit/<str:id>',Hod_Views.EDIT_COURSE,name='edit_course'),
    path('Hod/Course/Update',Hod_Views.UPDATE_COURSE,name='update_course'),
    path('Hod/Course/Delete/<str:id>',Hod_Views.DELETE_COURSE,name='delete_course'),



    path('Hod/Subject/Add',Hod_Views.ADD_SUBJECT,name='add_subject'),
    path('Hod/Subject/View',Hod_Views.VIEW_SUBJECT,name='view_subject'),
    path('Hod/Subject/Edit/<str:id>',Hod_Views.EDIT_SUBJECT,name='edit_subject'),
    path('Hod/Subject/Update',Hod_Views.UPDATE_SUBJECT,name='update_subject'),
    path('Hod/Subject/Delete/<str:id>',Hod_Views.DELETE_SUBJECT,name='delete_subject'),



    path('Hod/Session/Add',Hod_Views.ADD_SESSION,name='add_session'),
    path('Hod/Session/View',Hod_Views.VIEW_SESSION,name='view_session'),
    path('Hod/Session/Edit/<str:id>',Hod_Views.EDIT_SESSION,name='edit_session'),
    path('Hod/Session/Update',Hod_Views.UPDATE_SESSION,name='update_session'),
    path('Hod/Session/Delete/<str:id>',Hod_Views.DELETE_SESSION,name='delete_session'),



    path('Hod/Staff/send_notification',Hod_Views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('Hod/Staff/save_notification',Hod_Views.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),

    path('Hod/Student/send_notification',Hod_Views.STUDENT_SEND_NOTIFICATION,name='student_send_notification'),
    path('Hod/Student/save_notification',Hod_Views.SAVE_STUDENT_NOTIFICATION,name='save_student_notification'),



    path('Hod/Staff/Leave_View',Hod_Views.Staff_Leave_View,name='staff_leave_view'),
    path('Hod/Staff/approve_leave/<str:id>',Hod_Views.STAFF_APPROVE_LEAVE,name='staff_approve_leave'),
    path('Hod/Staff/disapprove_leave/<str:id>',Hod_Views.STAFF_DISAPPROVE_LEAVE,name='staff_disapprove_leave'),

    path('Hod/Student/Leave_view',Hod_Views.STUDENT_LEAVE_VIEW,name='student_leave_view'),
    path('Hod/Student/approve_leave/<str:id>',Hod_Views.STUDENT_APPROVE_LEAVE,name='student_approve_leave'),
    path('Hod/Student/disapprove_leave/<str:id>',Hod_Views.STUDENT_DISAPPROVE_LEAVE,name='student_disapprove_leave'),


    path('Hod/Staff/feedback',Hod_Views.STAFF_FEEDBACK,name='staff_feedback_reply'),
    path('Hod/Staff/feedback/save',Hod_Views.STAFF_FEEDBACK_SAVE,name='staff_feedback_reply_save'),
   
    path('Staff/Take_Attendance',Staff_Views.STAFF_TAKE_ATTENDANCE,name='staff_take_attendance'),
    path('Staff/Save_Attendance',Staff_Views.STAFF_SAVE_ATTENDANCE,name='staff_save_attendance'),
    path('Staff/View_Attendance',Staff_Views.STAFF_VIEW_ATTENDANCE,name='staff_view_attendance'),

    path('Staff/Add/Result',Staff_Views.STAFF_ADD_RESULT,name='staff_add_result'),
    path('Staff/Save/Result',Staff_Views.STAFF_SAVE_RESULT,name='staff_save_result'),
    path('Staff/View_Gradebook',Staff_Views.gradebook,name='staff_view_gradebook'),
    
    
    path('Hod/Student/feedback',Hod_Views.STUDENT_FEEDBACK,name='get_student_feedback'),
    path('Hod/Student/feedback/reply/save',Hod_Views.REPLY_STUDENT_FEEDBACK,name='reply_student_feedback'),

    path('Hod/View/Attendance',Hod_Views.VIEW_ATTENDANCE,name='view_attendance'),
    path('Student/View_Result/',Student_Views.VIEW_RESULT,name='view_result'),
    


    #Staff Urls
    path('Staff/Home',Staff_Views.HOME,name='staff_home'),

    path('Staff/Notification',Staff_Views.NOTIFICATIONS,name='notifications'),
    path('Staff/mark_as_done/<str:status>',Staff_Views.STAFF_NOTIFICATION_MARK_AS_DONE,name='staff_notification_mark_as_done'),

    path('Staff/Apply_leave',Staff_Views.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
    path('Staff/Apply_leave_save',Staff_Views.STAFF_APPLY_LEAVE_SAVE,name='staff_apply_leave_save'),

    path('Staff/Feedback',Staff_Views.STAFF_FEEDBACK,name='staff_feedback'),
    path('Staff/Feedback/Save',Staff_Views.STAFF_FEEDBACK_SAVE,name='staff_feedback_save'),

   
    path('Staff/Lesson/Add',Staff_Views.STAFF_ADD_LESSON,name='staff_add_lesson'),
    path('Staff/Lesson/View',Staff_Views.STAFF_VIEW_LESSON,name='staff_view_lesson'),
    path('Staff/Lesson/Delete/<int:id>',Staff_Views.delete_lesson,name='staff_delete_lesson'),
    path('Staff/Lesson/Edit/<int:sub_id>/<int:les_id>',Staff_Views.STAFF_EDIT_LESSON,name='staff_edit_lesson'),
    path('Staff/Lesson/Update',Staff_Views.STAFF_UPDATE_LESSON,name='staff_update_lesson'),
    path('Staff/Lesson/View_Assignments/<int:sub_id>/<int:les_id>',Staff_Views.STAFF_VIEW_ASSIGNMENTS,name='staff_view_assignment'),

    #Student Urls
    path('Student/Home',Student_Views.HOME,name='student_home'),
    path('Studennt/Course_Outline',Student_Views.COURSE_OUTLINE,name='course_outline'),

    path('Student/Notifications',Student_Views.STUDENT_NOTIFICATION,name='student_notification'),
    path('Student/mark_as_done/<str:status>',Student_Views.STUDENT_NOTIFICATION_MARK_AS_DONE,name='student_notification_mark_as_done'),
    path('Student/feedback',Student_Views.STUDENT_FEEDBACK,name='student_feedback'),
    path('Student/feedback/save',Student_Views.STUDENT_FEEDBACK_SAVE,name='student_feedback_save'),


    path('Student/apply_for_leave',Student_Views.STUDENT_LEAVE,name='student_leave'),
    path('Student/Leave_save',Student_Views.STUDENT_LEAVE_SAVE,name='student_leave_save'),

    path('Student/View_Attendance',Student_Views.STUDENT_VIEW_ATTENDANCE,name='student_view_attendance'),
    path('Student/View_Lesson',Student_Views.STUDENT_VIEW_LESSON,name='student_view_lesson'),
    path('Student/Edit_Assignment/<int:sub_id>/<int:les_id>',Student_Views.STUDENT_EDIT_ASSIGNMENT,name='student_edit_assignment'),
    path('Student/Send_Assignment',Student_Views.STUDENT_SEND_ASSINGMENT,name='student_send_assignment'),
    
    path('Student/View_All_Subject_Notes',Student_Views.VIEW_ALL_NOTES,name='view_all_notes'),
    path('Student/View_Subject_Notes/<int:sub_id>',Student_Views.VIEW_NOTES,name='view_notes'),
    path('Student/Add_Notes/<int:sub_id>',Student_Views.ADD_NOTES,name='add_notes'),
    path('Student/Delete_Notes/<int:sub_id>/<int:note_id>',Student_Views.DELETE_NOTES,name='delete_notes'),
    path('Student/Notes/Edit/<int:sub_id>/<int:note_id>',Student_Views.EDIT_NOTE,name='student_edit_note'),
    path('Student/Notes/Update',Student_Views.UPDATE_NOTE,name='student_update_note'),

    path('create-pdf-attendance-staff',Staff_Views.pdf_create_attendance,name="create_pdf_attendance_staff"),
    path('create-pdf-result-student',Student_Views.pdf_create_result,name="create_pdf_result_student"),


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)