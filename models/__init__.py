#!/usr/bin/python3
""" initializing filestorage package"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
