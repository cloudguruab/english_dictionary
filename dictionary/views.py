from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    """[endpoint to render home page]"""
    return render(request, 'index.html')

def word(request):
    """[endpoint to render word bank]"""
    
    # parsed word from index.html form
    search = request.GET.get('search')
    
    # dictionary
    dictionary = PyDictionary()
    
    # stored variable
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)
    context = {
        'meaning': meaning['Noun'][0],
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    
    return render(request, 'word.html', context)