""" livrets/admin.py """

from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    """ Overwrite admin.AdminSite. """
    site_url = 'http://localhost:8005/livrets/'
