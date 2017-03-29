# -*- coding: utf-8 -*-
"""A Django password hasher that leverages Postgres pgcrypto encryption."""

from collections import OrderedDict

from django.db import connection
from django.contrib.auth.hashers import (BasePasswordHasher, mask_hash)
from django.utils.crypto import constant_time_compare
from django.utils.translation import ugettext_noop as _


class LegacyPasswordHasher(BasePasswordHasher):
    """
    Password hasher which is intended to provide password continuity from the
    legacy pgcrypto-encoded password

    pgcrypto$pghash

    Configured to use the crypt() method from the Postgres pgcrypto extension.
    NOTE: Postgres and pgcrypto are required.
    """
    algorithm = 'pgcrypto'

    def salt(self):
        """
        Generates a salt via pgcrypto.gen_salt().
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT gen_salt('md5')")
            _salt = cursor.fetchall()[0][0]
            return _salt

    def encode(self, password, salt=None):
        assert password
        if not salt:
            salt = self.salt()
        with connection.cursor() as cursor:
            cursor.execute("SELECT crypt(%s, %s)", [password, salt])
            pghash = cursor.fetchall()[0][0]
            return "%s$%s" % (self.algorithm, pghash)

    def verify(self, password, encoded):
        algorithm, pghash = encoded.split('$', 1)
        assert algorithm == self.algorithm
        encoded_2 = self.encode(password, pghash)
        return constant_time_compare(encoded, encoded_2)

    def safe_summary(self, encoded):
        algorithm, pghash = encoded.split('$', 1)
        assert algorithm == self.algorithm
        return OrderedDict([
            (_('algorithm'), algorithm),
            (_('hash'), mask_hash(pghash)),
        ])

    def harden_runtime(self, password, encoded):
        pass
