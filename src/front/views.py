from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import pdb

import os
from django.conf import settings
# Create your views here.

def index(request):

    repertoire_de_travail = os.getcwd()
    print("Répertoire de travail actuel :", repertoire_de_travail)
    # pdb.set_trace() 
    file_path = os.path.join(settings.BASE_DIR, 'front/static/data/best_films.csv')
    print("============= ", file_path)
    df = pd.read_csv(file_path, sep=";")
    films_list = df.to_dict(orient='records')
    context = {'films_list': films_list}
    return render(request, "index.html", context)