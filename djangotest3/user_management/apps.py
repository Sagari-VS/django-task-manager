# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


from django.apps import AppConfig
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class UserManagementConfig(AppConfig):
    """
    To run signals
    """
    name = 'user_management'

    def ready(self, signals=None):
        from . import signals
        



class MtasksConfig(AppConfig):
    name = 'mtasks'
    verbose_name = _(' Task Management')
