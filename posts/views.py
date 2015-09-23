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
	for post in Post.objects.all()[:50]:
		obj = {}
		obj['id'] = post.id
		obj['title'] = post.title
		obj['content'] = post.content
		obj['created'] = post.created
		obj['tags'] = [tag.title for tag in post.tags.all()]
		posts.append(post)
	return render(request, 'main/index.html', {'rp': '.', 'posts': posts })