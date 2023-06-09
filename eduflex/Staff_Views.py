from django.shortcuts import render,redirect
from django.contrib import messages
from eduflexApp.models import Lesson,Attendance_Report,Attendance,Session_Year,Student,Staff,Subject,Staff_Notification,Staff_leave,Staff_Feedback,StudentResult,Submission
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



@login_required(login_url='login/')
def HOME(request):
    
    staff = Staff.objects.get(admin = request.user.id)
    total_subject = Subject.objects.filter(staff = staff).count()
    total_lessons = Lesson.objects.filter(subject_id__in=Subject.objects.filter(staff=staff)).count()
    total_students = Student.objects.filter(course_id__in=Subject.objects.filter(staff=staff).values('course_id')).count()
    unread_notification_total = Staff_Notification.objects.filter(staff_id=staff,status=0).count()

    # Data for subject enrollment chart
    subject_enrollments = []
    subject_names = []
    subjects = Subject.objects.filter(staff=staff)
    for subject in subjects:
        enrollment = Student.objects.filter(course_id=subject.course).count()
        subject_enrollments.append(enrollment)
        subject_names.append(subject.name)

    context = {
        'total_subject':total_subject,
        'total_students':total_students,
        'total_lessons':total_lessons,
        'unread_notification_total': unread_notification_total,
        'subject_enrollments': subject_enrollments,
        'subject_names': subject_names,
    }

    return render(request,'Staff/home.html',context=context)

@login_required(login_url='login/')
def NOTIFICATIONS(request):

    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        notification = Staff_Notification.objects.filter(staff_id = staff_id)

        context = {
            'notification':notification,
        }


    return render(request,'Staff/notification.html',context)


@login_required(login_url='login/')
def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):

    notification = Staff_Notification.objects.get( id = status )
    notification.status = 1
    notification.save()

    return redirect('notifications')
    
@login_required(login_url='login/')
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        staff_leave_history = Staff_leave.objects.filter(staff_id = staff_id)

        context = {
            'staff_leave_history' : staff_leave_history
        }

        return render(request,'Staff/apply_leave.html',context)

@login_required(login_url='login/')
def STAFF_APPLY_LEAVE_SAVE(request):
    
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff  = Staff.objects.get(admin = request.user.id)

        leave = Staff_leave(
            staff_id = staff,
            data = leave_date,
            message = leave_message
        )

        leave.save()
        messages.success(request,'Leave Successfully Sent')
        return redirect('staff_apply_leave')


@login_required(login_url='login/')
def STAFF_FEEDBACK(request):
    staff_id = Staff.objects.get(admin = request.user.id)

    feedback_history = Staff_Feedback.objects.filter(staff_id = staff_id)

    context = {
        'feedback_history' : feedback_history,

    }

    return render(request,'Staff/feedback.html',context)


@login_required(login_url='login/')
def STAFF_FEEDBACK_SAVE(request):
    
    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        staff = Staff.objects.get(admin = request.user.id)
        feedback = Staff_Feedback(
            staff_id = staff, 
            feedback = feedback,
            feedback_reply = "",
        )

        feedback.save()
        return redirect('staff_feedback')
    

@login_required(login_url='login/')
def STAFF_TAKE_ATTENDANCE(request):

    staff_id = Staff.objects.get(admin = request.user.id)

    subject = Subject.objects.filter(staff = staff_id)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    students = None
    get_subject = None
    get_session_year = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = Session_Year.objects.get(id = session_year_id)

            subject = Subject.objects.filter(id = subject_id)
            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id = student_id)

    context = {
        'subject':subject,
        'session_year':session_year,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'action':action,
        'students':students,
    }

    return render(request,'Staff/take_attendance.html',context)


@login_required(login_url='login/')
def STAFF_SAVE_ATTENDANCE(request):
    
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')

        get_subject = Subject.objects.get(id = subject_id)
        get_session_year = Session_Year.objects.get(id = session_year_id)

        attendance = Attendance(
            subject_id = get_subject,
            attendance_data = attendance_date,
            session_year_id = get_session_year,
        )
        attendance.save()

        for i in student_id:
            stud_id = i
            int_stud = int(stud_id)

            p_students = Student.objects.get(id = int_stud)
            attendance_report = Attendance_Report(
                student_id = p_students,
                attendance_id = attendance,
            )

            attendance_report.save()
            messages.success(request,'Attendance Are Successfully Taken')


    return redirect('staff_take_attendance')

@login_required(login_url='login/')
def STAFF_VIEW_ATTENDANCE(request):

    staff = Staff.objects.get(admin = request.user.id)
    subject = Subject.objects.filter(staff = staff)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None


    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = Session_Year.objects.get(id = session_year_id)
            attendance = Attendance.objects.filter(subject_id = get_subject, attendance_data = attendance_date )
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id = attendance_id)


    context = {
    'subject':subject,
    'session_year':session_year,
    'action':action,
    'get_subject':get_subject,
    'get_session_year':get_session_year,
    'attendance_date':attendance_date,
    'attendance_report':attendance_report,
   }
    return render(request,'Staff/view_attendance.html',context)


@login_required(login_url='login/')
def STAFF_ADD_RESULT(request):

    staff = Staff.objects.get(admin = request.user.id)

    subjects = Subject.objects.filter(staff_id = staff)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id = subject_id)
            get_session = Session_Year.objects.get(id = session_year_id)

            subjects = Subject.objects.filter(id = subject_id)

            for i in subjects:
                student_id = i.course.id
                students = Student.objects.filter(course_id = student_id)
            
    context = {
        'subjects':subjects,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session,
        'students':students,
    }

    return render(request,'Staff/add_result.html',context)


@login_required(login_url='login/')
def STAFF_SAVE_RESULT(request):
    
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        Exam_mark = request.POST.get('Exam_mark')

        get_student = Student.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id = subject_id)

        check_exists = StudentResult.objects.filter(subject_id = get_subject, student_id = get_student).exists()
        if check_exists:
            result = StudentResult.objects.get(subject_id = get_subject, student_id = get_student)
            result.assignment_mark = assignment_mark
            result.exam_mark = Exam_mark
            result.save()
            messages.success(request,'Result Are Successfully Updated')
            return redirect('staff_add_result')

        else:
            result = StudentResult(
                student_id=get_student, 
                subject_id=get_subject, 
                exam_mark=Exam_mark,
                assignment_mark=assignment_mark)
            result.save()
            messages.success(request,'Result Are Successfully Added')
            return redirect('staff_add_result')
        
def gradebook(request):

    staff_id = Staff.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(staff = staff_id)
    action = request.GET.get('action')
    get_subject = None
    result = None
    subject_marks = []
    subject_names = []
    

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id = subject_id)
            subject = Subject.objects.get(id = subject_id)
            result = StudentResult.objects.filter(subject_id = subject)
            for student_result in result:
                subject_marks.append(student_result.assignment_mark + student_result.exam_mark)
                subject_names.append(student_result.student_id.admin.username)

    context = {
        'subjects':subjects,
        'action':action,
        'get_subject':get_subject,
        'result':result,
        'subject_marks': subject_marks,
        'subject_names': subject_names
        
    }

    return render(request,'Staff/gradebook.html',context=context)


@login_required(login_url='login/')
def STAFF_VIEW_LESSON(request):

    staff_id = Staff.objects.get(admin = request.user.id)
    subject = Subject.objects.filter(staff = staff_id)
    action = request.GET.get('action')
    lessons = None
    get_subject = None

    if action is not None:
        subject_id = request.POST.get('subject_id')
        get_subject = Subject.objects.get(id = subject_id)
        
        lessons = Lesson.objects.filter(subject_id = subject_id)

    context = {
        'subject':subject,
        'action':action,
        'get_subject':get_subject,
        'lessons':lessons
    }


    return render(request,'Staff/view_lesson.html',context=context)

@login_required(login_url='login/')
def STAFF_ADD_LESSON(request):

    staff = Staff.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(staff_id = staff)

    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        lesson_title = request.POST.get('lesson_title')
        notes = request.FILES.get('lesson_file')
        assignment = request.FILES.get('assignment_file')

        subject = Subject.objects.get(id = subject_id)

        if assignment != None:

            lesson = Lesson(
                subject_id = subject,
                lesson_title = lesson_title,
                notes = notes,
                assignment = assignment,
                assignment_status = 1
            )
        else:
             lesson = Lesson(
                subject_id = subject,
                lesson_title = lesson_title,
                notes = notes,
                assignment = assignment,
                assignment_status = 0
            )

        lesson.save()
        messages.success(request,'Lesson Are Successfully Added')
        return redirect('staff_add_lesson')
    
    context = {
        'subjects':subjects
    }

    return render(request,'Staff/add_lesson.html',context=context)

@login_required(login_url='login/')
def delete_lesson(request,id):

   lesson = Lesson.objects.get(id=id)
   lesson.delete()
   messages.success(request,'Lesson Successfully Deleted!')

   return redirect('staff_view_lesson')

@login_required(login_url='login/')
def STAFF_EDIT_LESSON(request,sub_id,les_id):

    subject = Subject.objects.get(id = sub_id)
    lesson = Lesson.objects.get(id = les_id)


    context = {
        'sub': subject,
        'lesson':lesson,
    }

    return render(request,'Staff/edit_lesson.html',context=context)

@login_required(login_url='login/')
def STAFF_UPDATE_LESSON(request):
   if request.method == "POST":
       lesson_id = request.POST.get('lesson_id')
       subject_id = request.POST.get('subject_id')
       lesson_title = request.POST.get('lesson_title')
       notes = request.FILES.get('lesson_file')
       assignment = request.FILES.get('assignment_file')

       subject = Subject.objects.get(id = subject_id)
       lesson = Lesson.objects.get(id = lesson_id)

       lesson.id = lesson_id
       lesson.subject_id = subject
       lesson.lesson_title = lesson_title

       if notes!=None and notes!="":
           lesson.notes = notes
        
       if assignment!=None and assignment!="":
           lesson.assignment = assignment
       
       if assignment != None:
           assignment_status = 1
        
       else:
           assignment_status = 0
           
       lesson.assignment_status = assignment_status
       lesson.save()
       messages.success(request,'Lesson Successfully Updated!')
       return redirect('staff_view_lesson')
   
   return render(request,'Staff/view_lesson.html')

@login_required(login_url='login/')
def STAFF_VIEW_ASSIGNMENTS(request,sub_id,les_id):

    submission = Submission.objects.filter(lesson_id = les_id)
    submission_count = Submission.objects.filter(lesson_id = les_id).count()

    subject = Subject.objects.filter(id = sub_id)
    for i in subject:
        student_id = i.course.id
        students = Student.objects.filter(course_id = student_id)
        student_count = Student.objects.filter(course_id = student_id).count()

        context = {
            'students':students,
            'student_count':student_count,
            'submission':submission,
            'submission_count':submission_count,
        }    
    

    return render(request,'Staff/view_assignments.html',context=context)


def pdf_create_attendance(request):

    attendance = Attendance_Report.objects.all()
    template_path = 'Staff/view_attendance_pdf.html'
    context = {
        'attendance':attendance
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="attendance_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response