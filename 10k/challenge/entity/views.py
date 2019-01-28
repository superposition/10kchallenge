from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Entity
from .forms import PostForm
from django.shortcuts import redirect

##

import requests
import lxml
from lxml import html
import pandas as pd 

##

def getUrlfromTicker(tick):
    filelist = []
    url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=' + tick + '&type=10-k&dateb=&owner=exclude&count=40'

    r = requests.get(url)
    tree = lxml.html.fromstring(r.content)
    results = tree.xpath("//a[@id='documentsbutton']")

    for res in results:
        parse = res.values()
        if (parse == 0):
            print ('NULL')
        filelist.append(parse[0])
    try:
        if (filelist[0] != 0):
             return 'https://www.sec.gov' + filelist[0]
    except IndexError:
        return False

def getCikReport(ticker):
    try:
        url = getUrlfromTicker(ticker)
        fields = url.split('/')
        cik = fields[6]
        reportId = fields[7]
        return (cik, reportId)
    except AttributeError:
        return 'False'

def getFinancialReport(cik, reportId):
    query = 'https://www.sec.gov/Archives/edgar/data/' + cik + '/' + reportId + '/Financial_Report.xlsx'
    return query


# Create your views here.
def entity_list(request):
	entities = Entity.objects.all()
	return render(request, 'entity/entity_list.html', {'entities': entities})

def entity_query(request):
    ticker = ''
    if request.method == "POST":

        form = PostForm(request.POST)

        if form.is_valid():
            entities = form.save(commit=False)

            unfiltered_list = form.cleaned_data['symbol']
            tickerlist = [x.strip() for x in unfiltered_list.split(',')]

            for ticker in tickerlist:
                load = getCikReport(ticker)
                if (load[0] != 'F'):    
                    reportUrl = getFinancialReport(load[0], load[1])
                print (reportUrl)

            entities.published_date = timezone.now()
            entities.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'entity/entity_query.html', {'form': form})