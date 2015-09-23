from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from collections import Counter
from posts.models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from blog import settings
import sys
import re
import time
import datetime
import random
import json
import os

def home(request):
	posts = []
	admin = True if request.user.is_superuser else False
	print admin
	for post in Post.objects.all().order_by('-created')[:50]:
		obj = {}
		obj['id'] = post.id
		obj['title'] = post.title
		obj['content'] = post.content
		obj['created'] = post.created
		obj['tags'] = [tag for tag in post.tags.all()]
		posts.append(post)
	return render(request, 'main/index.html', {'rp': '.', 'posts': posts, 'admin': admin })

def tag(request, tag_id):
	tag = Tag.objects.get(id=tag_id)
	posts = [post for post in Post.objects.filter(tags=tag)]
	print 'posts', posts
	return render(request, 'main/tag.html', {'rp': '../..', 'posts': posts, 'tag': tag })

@csrf_exempt
def edit_post(request):
	data = json.loads(request.body)
	try:
		post = Post.objects.get(id=data['id'])
		post.content = data['content']
		post.updated = datetime.datetime.now()
		post.save()
		return HttpResponse("success")
	except Exception as ex:
		print str(ex)
		return HttpResponse("fail")













