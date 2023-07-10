import datetime
from datetime import date
from django.shortcuts import render
from .models import Category, Story
from django.http import HttpResponse
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


now = datetime.datetime.now()
today = date.today()
d1 = today.strftime("%b. %d,%Y")

def index(request):
    story_list = Story.objects.order_by("-id")
    newest = story_list[0]
    next_4_newest = story_list[1:5]
    newest_list = story_list[0:4]
    most_viewed_stories = story_list[3:6]

    young_children = Story.objects.filter(category=1).order_by("-id")
    older_children = Story.objects.filter(category=2).order_by("-id")
    
    return render(request, "stories/index.html", 
                {'today':now,
                'd1': d1,
                'newest': newest,
                'next_4_newest': next_4_newest,
                'newest_list': newest_list,
                'young': young_children,
                'older': older_children,
                'most_viewed_stories': most_viewed_stories,})

def category(request, pk):
    story_list = Story.objects.filter(category=pk).order_by("-id")
    for story in story_list:
        story.content = re.sub('<[^<]+?>', '', story.content)

    page = request.GET.get('page', 1) # trang bắt đầu    

    paginator = Paginator(story_list, 3) # số story/trang


    
    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)


    newest = Story.objects.filter(category=pk).order_by("-id")[0]
    newest_stories = Story.objects.filter(category=pk).order_by("-id")[0:4]
    most_viewed_stories = Story.objects.order_by("-id")[3:6]

    return render(request, "stories/category.html", 
                {'today':now,
                'stories': stories,
                'newest': newest,
                'pk': pk,
                'newest_stories': newest_stories,
                'most_viewed_stories': most_viewed_stories,
                })

def story(request, pk):
    story_select = Story.objects.get(pk=pk)
    stories = Story.objects.filter(category=story_select.category).order_by("-id")
    newest = Story.objects.order_by("-id")[0]
    newest_stories = Story.objects.order_by("-id")[0:4]
    most_viewed_stories = Story.objects.order_by("-id")[3:6]
    return render(request, "stories/story.html", 
                {'today':now,
                'story': story_select,
                'stories': stories,
                'newest': newest,
                'newest_stories': newest_stories,
                'most_viewed_stories': most_viewed_stories,
                })

def contact(request):
    newest = Story.objects.order_by("-id")[0]
    newest_stories = Story.objects.order_by("-id")[0:4]
    most_viewed_stories = Story.objects.order_by("-id")[3:6]
    return render(request, "stories/contact.html", {'today':now, 'newest': newest, 'newest_stories': newest_stories, 'most_viewed_stories': most_viewed_stories})
    
