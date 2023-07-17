from django.shortcuts import render
import pymongo
import ssl

connection_string = 'mongodb+srv://irisminami0307:538167294@itamiworld.svqaz2d.mongodb.net/'
client = pymongo.MongoClient(connection_string)
db = client['test']
Books = db['books']

# Create your views here.
def index(request):
    books = Books.find({})
    return render(request, 'index.html', context={ 'books': books })

def save(request):
    if request.method == 'POST':
        if request.POST is not None:
            Books.insert_one({
                "title": request.POST['title'],
                'author': request.POST['author'],
                'description': request.POST['description']
            })
        return render(request, 'index.html')
    
    return render(request, 'new.html')
    
def edit(request):
    return render(request, 'edit.html')

def remove(request):
    return render(request, 'remove.html')