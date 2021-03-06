# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 7/19/15.
from datetime import datetime
from flask.ext.admin.contrib.sqla import ModelView
from app import db

__author__ = 'Vito'


class BaseModel(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class BaseModelView(ModelView):
    form_widget_args = {
        'created_at': {
            'readonly': True
        },
        'updated_at': {
            'readonly': True
        }
    }
    column_exclude_list = ('created_at', 'updated_at')
