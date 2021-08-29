# Add this line to the beginning of relative.py file
import sys
sys.path.append('..')
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from io import StringIO
from Portfoliomgr.analytics.msci import msci_bchmk_graph
import matplotlib.pyplot as plt

def msci_graph():
    context = {}
    fig = plt.figure()
    plt.rcParams["figure.figsize"] = (9,5)
    imgdata = StringIO()

    msci_dat = msci_bchmk_graph()
    msci_dat.plot()
    msci_dat.plot().legend()
    fig = msci_dat.plot(). get_figure()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()

    context['graph'] = data
    return context

@login_required(login_url='/accounts/login/')
def index(request):
    context = {}
    context = msci_graph()
    return render(request, 'main.html', context)

def graph(request):
    context = {}
    context = msci_graph()
    return render(request, 'graphs/graph.html', context)
