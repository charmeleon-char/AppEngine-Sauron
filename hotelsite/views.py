from django.shortcuts import render
from hotelsite.models import TestModel
from django.shortcuts import redirect
from google.appengine.ext import ndb

import datetime
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
	return render(request, "hotelsite/home.html")


def about(request):
	return render(request, "hotelsite/about.html")


def reviews(request):
	res = TestModel.query()
	logger.info(res)
	return render(request, "hotelsite/reviews.html", {'TestModel': res})

def add_review(request):
	if request.method == 'POST':
		items = request.POST
		t = TestModel(foo={"primeraDimesion":"primeraDimesionContenido", "primeraDimesion": "primeraDimesion",'InicioSegunda':{'ValorSegundaDimension':'Comentario de segunda dimension','TerceraDimension':{'LLaveTercera':'comentario de la tercera Dimension'}},'primeraDimesionS2':{"primeraDimesionS2":"primeraDimesionS2?", "about": "11111111111"}})
		t.put()
		#data = Review(location=items['location'], descriptions=items['review'], title=items['title'], star_rating=int(items['stars']))
		#test = Review(likes={"Ubicacion":{"lugar":items['location'],"Nombre"=items['title']}})
		#test.put()
		#data.date = datetime.datetime.now().date()
		#data.put()
		return redirect('/reviews')
	else:
		return render(request, 'hotelsite/add_review.html')