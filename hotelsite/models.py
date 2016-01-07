from django.db import models
from google.appengine.api import datastore_types
from google.appengine.ext import db
from google.appengine.api import users
import webapp2
import datetime
from google.appengine.ext import ndb


class TestModel(ndb.Model):
  foo = ndb.JsonProperty()

# Create your models here.
class Review(db.Model):
	location 			= db.StringProperty(required=True)
	descriptions 	= db.StringProperty()
	title 				= db.StringProperty(required=True)
#	likes = db.JSONProperty()

	star_rating 	= db.IntegerProperty(default=0)
	date					= db.DateProperty()

	meta = {
		'indexes': [
			'location',
			'descriptions',
			
			'title',
			'star_rating'
		]
	}