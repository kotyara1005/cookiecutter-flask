# -*- coding: UTF-8 -*-
DEBUG = True

STATIC_FOLDER = None

try:
    from {{ cookiecutter.repo_name }}.config.local_settings import *
except ImportError:
    pass
