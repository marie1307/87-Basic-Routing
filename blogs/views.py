from django.shortcuts import render

# Create your views here.
def blogs(request):
    blogs_lst = [
        {
            "title": "Suliko", 
            "text":"sakvarlis saflavs vedzebdi..", 
            "author":"Akaki Tsereteli"
        },
        {
            "title": "Sakure", 
            "text":"vita pepla arxevs nel-nela..", 
            "author":"Nikoloz Baratashvili"
        },
        {
            "title":"Ia", 
            "text":"ias bnel xevshi mosulsa..", 
            "author":"Vazha-fshavela"
        },
        {
            "title":"droshebi chqara", 
            "text":"gatenda, cenxlis mze aento, acurda..", 
            "author":"Vazha-fshavela"
        },
    ]
        
    return render(request, 'blogs/nblog.html', {'blogs_lst': blogs_lst})

