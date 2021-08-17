from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    #path('details/',views.details,name="details"),
    path('patientcomplaints/',views.patientcomplaints,name="patientcomplaints"),
    path('patientINcomplaints/',views.patientINcomplaints,name="patientINcomplaints"),
    path('Feedbackform/',views.Feedbackform,name="Feedbackform"),
    path('patientfeedback/',views.patientfeedback,name="patientfeedback"),
    path('patientcomplaints/change/<int:patient_id>/',views.change,name="change"),
    path('patientcomplaints/details/<int:patient_id>/',views.details,name="details"),
    path('patientcomplaints/detailsIN/<int:patient_id>/',views.detailsIN,name="detailsIN"),
    path('patientINcomplaints/change2/<int:patient_id>/',views.change2,name="change2"),
    path('patientcomplaints/forward/<int:pat_id>/',views.forward,name="forward"),
    path('patientINcomplaints/forward2/<int:pat_id>/',views.forward2,name="forward2"),
    path('patientINfeedback/',views.patientINfeedback,name="patientINfeedback"),
    path('admindashboard/',views.dashboard,name="dashboard"),
    path('thankyou/',views.thankyou,name="thankyou"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('IPDFeedbackform/',views.IPDFeedbackForm,name="IPDFeedbackForm"),
    path('askingpage/',views.askingpage,name="askingpage"),
    path('otpverify/',views.verifyotp,name="verifyotp"),

]


