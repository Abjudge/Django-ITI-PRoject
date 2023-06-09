

from django.urls import path

from  .views import *
urlpatterns = [

    path('', traineelist, name='traineelist'),
    path('Add', traineeadd, name='traineeadd'),
    path('Update/<int:ID>', traineeupdate, name='traineeupdate'),
    path('Delete/<int:ID>', traineedelete, name='traineedelete'),
    path("alltrainee/", alltrainee, name="alltrainee"),
    path ("trainee/<int:id>/", TraineeDetail ),
    path("addtrainee/", addtrainee, name="addtrainee"),

    path("deletetrainee/<int:id>/", deletetrainee, name="deletetrainee"),
    path("updatetrainee/<int:id>/", updatetrainee, name="updatetrainee"),
]