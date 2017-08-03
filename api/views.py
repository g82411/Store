from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
# Create your views here.
from .models import Author
from .models import Article
from .models import Board
from traceback import format_exc
import logging
logger = logging.getLogger("sourceDns.webdns.views")
@csrf_exempt
def addPost(request):
    content = request.POST.get("content", "")
    date = request.POST.get("date", "")
    author = request.POST.get("author", "")
    label = request.POST.get("label", "")
    title = request.POST.get("title", "")
    logger.debug(author)
    try:
        labelObject = Board.objects.get(BoardName=label)
    except ObjectDoesNotExist:
        labelObject = Board(BoardName=label)
        labelObject.save()
    try:
        authorObject = Author.objects.get(authorName=author)
    except ObjectDoesNotExist:
        authorObject = Author(authorName=author)
        authorObject.save()
    try:
        article = Article(title=title, text=content, dateTime=date,
                          author=authorObject, label=labelObject)
        article.save()
        result = {
            "msg":"Add success"
        }
        return JsonResponse(result)
    except:
        logger.error(format_exc())
        result = {
            "msg":"Error"
        }
        return JsonResponse(result)
    
    