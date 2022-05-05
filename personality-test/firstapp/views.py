from lib2to3.refactor import MultiprocessingUnsupported
from pydoc_data.topics import topics
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

menus=[
    {'id':1, 'title':'start menu'},
    {'id':2, 'title': 'share'}
]



def index(request):
    global menus
    ul=''
    for menu in menus:
        ul+=f'<li><a href="/read/{menu["id"]}>{menu["title"]} </li>'
        print(ul)
        
    return HttpResponse(f'''
        <html>
        <body>
        <ul>
        {ul}
        </ul>
        </body>
        </html>
                        ''')
    
'''
def index(request):
    return HttpResponse("Welcome") #response by http to client
'''

def result(request, type):
    return HttpResponse("Result: "+type)