from django.shortcuts import render
def input_form(request):
    return render(request,'input_form.htm',{})

from nltk.corpus import wordnet
def draw(request):
    query_word=request.POST['input']
    links=[]
    for synset in wordnet.synsets(query_word):
        definition=synset.name()+': '+synset.definition()
        example=''
        if synset.examples():example=synset.examples()[0]
        for hyponym in synset.hyponyms():
            links.append({'source':definition+'. '+example,'target':hyponym.name,'type':'hyponym'})
        for hypernym in synset.hypernyms():
            links.append({'source':definition+'. '+example,'target':hypernym.name,'type':'hypernym'})
        for nym in synset.part_meronyms():
            links.append({'source':definition+'. '+example,'target':nym.name,'type':'part_meronym'})
        for nym in synset.substance_meronyms():
            links.append({'source':definition+'. '+example,'target':nym.name,'type':'substance_meronym'})
        for nym in synset.member_holonyms():
            links.append({'source':definition+'. '+example,'target':nym.name,'type':'member_holonym'})
        for nym in synset.part_holonyms():
            links.append({'source':definition+'. '+example,'target':nym.name,'type':'part_holonym'})
        for nym in synset.substance_holonyms():
            links.append({'source':definition+'. '+example,'target':nym.name,'type':'substance_holonym'})
        for nym in synset.entailments():
            links.append({'source':definition+'. '+example,'target':nym.name,'type':'entailment'})
    return render(request,'wnvis.htm',{'links':links})
