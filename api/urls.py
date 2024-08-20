from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import ClassesListView
from .views import CoursesListView
from .views import ClassperiodListView
from .views import StudentDetailview
from .views import ClassesDetailview
from .views import CoursesDetailview
from .views import ClassPeriodDetailview
from .views import TeacherDetailview 
from .views import WeeklyTimetable


urlpatterns=[
    path("students/",StudentListView.as_view(),name="student_list_view"),
    # path("students/",StudentListView.as_views),name="student_list_view"
    path("teachers/", TeacherListView.as_view(),name="teacher_list_view"),
    path("classes/", ClassesListView.as_view(),name="class_list_view"),
    path("courses/", CoursesListView.as_view(),name="course_list_view"),
    path("classPeriod/",ClassperiodListView.as_view(),name="class_Period_list_view"),
    path("students/<int:id>/",StudentDetailview.as_view(),name="student_detailview"),
    path("classes/<int:id>/",ClassesDetailview.as_view(),name="Class_detailview"),
    path("courses/<int:id>/",CoursesDetailview.as_view(),name="course_list_view" ),
    path("classPeriod/<int:id>/",ClassPeriodDetailview.as_view(),name="class_Period_detailview"),
    path("teachers/<int:id>/",TeacherDetailview.as_view(),name="teacher_detailview"),
   path("views/timetable/", WeeklyTimetable.as_view(), name='weekly_timetable'),
]