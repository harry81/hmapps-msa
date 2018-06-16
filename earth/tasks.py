# -*- coding: utf-8 -*-
from .utils import update_deals


def celery_load_deals(self,  **kwargs):
    update_deals(**kwargs)
