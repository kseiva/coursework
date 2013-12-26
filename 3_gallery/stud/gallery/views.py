# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from gallery.models import Gallery

from PIL import Image
import os

def upload(request):
	if request.method == 'POST':
		g = Gallery(original = request.FILES['image'], title = request.POST['title'])
		g.save()

		img = Image.open(g.original.path)

		oldW, oldH = img.size
		oldRatio = oldW / float(oldH)
		newW = 100
		newH = 100
		newRatio = 1

		left = (oldW - newW) / 2
		top = (oldH - newH) / 2
		right = (oldW + newW) / 2
		bottom = (oldH + newH) / 2

		path, f = os.path.split(g.original.name)

		if(newRatio > oldRatio):
			img = img.resize((newW, newW * oldH / oldW), Image.ANTIALIAS)
		else:
			img = img.resize((newH * oldW / oldH, newH), Image.ANTIALIAS)
		img.save(settings.MEDIA_ROOT + "uploads/preview/" + f)

		return HttpResponseRedirect("/gallery/lists")

	return render(request, 'upload.html')

def lists(request):
  context = {'lists': Gallery.objects.all()}
  return render(request, 'lists.html', context)