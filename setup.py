# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="ListFilesMP3",
    version="1.0",
    description="Listado de los archivos de mp3",
    author="Renzo Elias",
    author_email="",
    url="",
    license="MIT",
    scripts=["application.py"],
    console=["application.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)