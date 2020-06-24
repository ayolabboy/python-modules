from django.conf.urls import url, include 
from django.urls import path 

from wholethingAPI import gov24FamilyRegiApply
from wholethingAPI import default




urlpatterns = [ 
    path('', default.index), 
    path('gov24FamilyRegiApply/', gov24FamilyRegiApply.index), 

]

