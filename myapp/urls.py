from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [

    path('', home, name='home'),
    path('deploy_contract', DeployContractManager.as_view(), name='deploy_contract'),

    # path('lock-tokens/', lock_tokens, name='lock_tokens'),

    
]


