# -*- coding: utf-8 -*-

"""Service definitions that handle business logic."""

from __future__ import unicode_literals


def includeme(config):
    config.register_service_factory('.settings.settings_factory', name='settings')