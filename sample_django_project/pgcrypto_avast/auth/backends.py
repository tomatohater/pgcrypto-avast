# -*- coding: utf-8 -*-
"""A Django authentication backend based on legacy_users table."""

from django.contrib.auth.models import User
from django.db import connection

class LegacyAuthBackend(object):

    def authenticate(self, username=None, password=None):
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM legacy_users WHERE username=%s AND \
                            password=CRYPT(%s, password)",
                            [username, password])
            row = cursor.fetchone()
        if row:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. Set an unusable password because only the
                # legacy_users password is checked.
                user = User(username=username)
                user.set_unusable_password()
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
