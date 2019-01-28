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

def entity_detail(request, sym):
    print (request)
    print (sym)
    entities = Entity.objects.filter(symbol=sym)
    return render(request, 'entity/entity_detail.html', {'entities': entities})

def entity_query(request):
    ticker = ''
    db = ''
    reportUrl = ''
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

                try:
                    ## None of the spreadsheets are standardized?
                    readfromweb = pd.ExcelFile(reportUrl)   
                    data = pd.read_excel(readfromweb, 'Consolidated Statements of Cash')
                    datavalues = data.values

                    for value in datavalues:
                        db += "\t" + " ".join(map(str, value)) + "\n"

                    print(db)
                    print(ticker)
                    print(load[0])
                    entities.symbol = ticker
                    entities.CIK = load[0]
                    entities.payload = db         
                    entities.published_date = timezone.now()
                    entities.save() 

                except:

                    print(ticker + " did not have a associated file on hand")                   

            return redirect('/list/')
    else:
        form = PostForm()
    return render(request, 'entity/entity_query.html', {'form': form})