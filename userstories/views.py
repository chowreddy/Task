from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from userstories.models import Stories, Comment, Vote
from django.template import RequestContext
from django.db.models import Max
# Create your views here.

def add_story_form(request):
	return render(request, 'add_story.html', context_instance=RequestContext(request))

def add_story(request):
	try:
		story = Stories.objects.get(title=request.POST.get('title_name'))
		if story:
			return HttpResponse('Story already exists,use different story')
	except:
		story = Stories.objects.create(title=request.POST.get('title_name'),
									   link=request.POST.get('link'))
		story.save()
		return HttpResponseRedirect('/')

def home(request):
	stories = Stories.objects.all()
	return render_to_response('home.html', {'stories': stories[:5]}, context_instance=RequestContext(request))

def search_update(request, id_):
	story = Stories.objects.get(id=id_)
	return render_to_response('show.html', {'story': story}, context_instance=RequestContext(request))

def vote(request):
	#import pdb
	#pdb.set_trace()
	if request.POST.get('vote_') == 'Upvote':
		vote_obj = Vote.objects.create(upvote=int(Vote.objects.all().aggregate(Max('upvote'))) + 1,
									   downvote=int(Vote.objects.all().aggregate(Max('downvote'))))
		vote_obj.save()
	else:
		vote_obj = Vote.objects.create(downvote=int(Vote.objects.all().aggregate(Max('downvote'))) + 1,
									   upvote=int(Vote.objects.all().aggregate(Max('upvote'))))
		vote_obj.save()

def comment(request, id_):
	import pdb
	pdb.set_trace()
	obj = Comment.objects.create(comment=request.POST.get('comment'), story=Stories.objects.get(id=id_))
	obj.save()
