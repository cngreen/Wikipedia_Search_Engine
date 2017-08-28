import MySQLdb
import MySQLdb.cursors
import config
import os
import uuid
import hashlib
from flask import Flask, session, abort, redirect, render_template, url_for

def connect_to_database():
  options = {
    'host': config.env['host'],
    'user': config.env['user'],
    'passwd': config.env['password'],
    'db': config.env['db'],
    'cursorclass' : MySQLdb.cursors.DictCursor
  }
  db = MySQLdb.connect(**options)
  db.autocommit(True)
  return db

db = connect_to_database()
