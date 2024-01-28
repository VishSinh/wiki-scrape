from traceback import print_exc
from django.shortcuts import render,redirect
from .models import *
from .utils import scrap_wiki
from django.http import HttpResponse,JsonResponse

def home(requests):
    try:
        if requests.method == 'POST':
            url = requests.POST.get('wiki_url')
            print("From view:",url)
            id = scrap_wiki(url)
            return redirect('summary',pk=id)
           
        return render(requests,'home.html')    

    except Exception as e:
        print_exc(e)
        return JsonResponse({'message':'Somethingdsada went wrong!'})



def scrap_summary(requests,pk):
    scrap_data = WebScrape.objects.get(pk=pk)
    return render(requests,'api.html',{"data":scrap_data})


def scrap_api(requests):
    try:
        objs = WebScrape.objects.all()
        payload = []
        for obj in objs:
            payload.append({
                "id":obj.id,
                "title":obj.title,
                "url":obj.url,
                "data":obj.info

            })
        return JsonResponse(payload,safe=False)    

    except Exception as e:
        print(e)
        return JsonResponse({"message":"Something saddwent wrong!"})    
