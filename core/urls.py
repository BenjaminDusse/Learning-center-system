# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route

    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line
    path("", include("center.urls", namespace='center')),
    path("accounts/", include("users.urls")),

]
