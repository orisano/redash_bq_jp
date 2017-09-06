#!/usr/bin/env python

from setuptools import setup

setup(
        name="redash_bq_jp",
        version="1.0",
        description="redash big_query runner patch for japanese columns",
        author="Nao YONASHIRO",
        author_email="owan.orisano@gmail.com",
        py_modules = ["redash_bq_jp"],
        install_requires = ["six"],
)
