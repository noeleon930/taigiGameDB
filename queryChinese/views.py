from django.shortcuts import render
from django.http import HttpResponse
from queryChinese.models import ChineseWord


def query(request, wordQ):

    theAnswer = ChineseWord.objects.filter(word = wordQ)

    if(len(theAnswer) >= 1):
        tmp = ""
        for answer in theAnswer:
            tmp = tmp + answer.word + " : " + answer.pronounce + "<br>"

        return HttpResponse(tmp)

    else:
        return HttpResponse("No results")
