# -*- coding: utf-8 -*-

"""
WSGI config for learning_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling  # 正确提供静态文件

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

application = Cling(get_wsgi_application())