from django.urls import path
from hr import views

urlpatterns=[
    path("",views.SignInView.as_view(),name="sign_in"),
    path("index",views.DashboardView.as_view(),name="index"),
    path("signout",views.SignOutView.as_view(),name="sign_out"),
    path("category",views.CategoryListCreateView.as_view(),name="category"),
    path("category/<int:pk>/remove/",views.CategoryDeleteView.as_view(),name="category_delete"),
    path("jobs/add",views.JobCreateView.as_view(),name="job_add"),
    path("jobs/all",views.JobListView.as_view(),name="job_list"),
    path("jobs/<int:pk>/remove",views.JobDeleteView.as_view(),name="delete"),
    path("jobs/<int:pk>/change",views.JobUpdateView.as_view(),name="job_edit"),
    path("jobs/<int:pk>/applications/",views.JobApplicationListView.as_view(),name="application_list"),
    path("applications/<int:pk>/",views.ApplicationDetailView.as_view(),name="application_detail"),
    path("applications/<int:pk>/change/",views.ApplicationUpdateView.as_view(),name="application_edit"),

]