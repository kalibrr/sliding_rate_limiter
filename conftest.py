# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import


def pytest_addoption(parser):
    parser.addoption('--redis', action='store_true', dest="redis",
                     default=False, help="enable redis-related tests")


def pytest_configure(config):
    if not config.option.redis:
        setattr(config.option, 'markexpr', 'not redis')
