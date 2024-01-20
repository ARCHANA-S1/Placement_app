from django.urls import path
from jobseeker import views

urlpatterns=[

    path("register/",views.SignUpView.as_view(),name="sign_up"),
    path("index/",views.StudentIndexView.as_view(),name="seeker_index"),
    path("profiles/add",views.ProfileCreateView.as_view(),name="profile_add"),
    path("profiles/<int:pk>/",views.ProfileDetailView.as_view(),name="profile_detail"),
    path("profile/<int:pk>/",views.ProfileEditView.as_view(),name="profile_edit"),
    path("signout/",views.SignOutView.as_view(),name="sign_out"),
    path("jobs/<int:pk>/detail",views.JobDetailView.as_view(),name="job_detail"),
    path("jobs/<int:pk>/apply",views.ApplyJobView.as_view(),name="job_apply"),
    path("application/all",views.ApplicationListView.as_view(),name="my_applications"),
    path("jobs/<int:pk>/save",views.JobSaveView.as_view(),name="job_save"),
    path("jobs/saved/all",views.SavedJobListView.as_view(),name="saved_jobs"),
]