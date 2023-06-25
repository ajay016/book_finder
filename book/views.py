from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from .forms import *

def home(request):

    books = Book.objects.all()
    # harry_potter = Book.objects.get(name='Harry Potter')
    # lord_of_the_rings = Book.objects.get(name='The Lord of the Rings')
    # test3 = Book.objects.get(name='Test3')
    # test3 = Book.objects.get(name='Test7')

    # harry_potter_author = harry_potter.author_set.all()
    # lord_of_the_rings_author = lord_of_the_rings.author_set.all()
    # test3_author = test3.author_set.all()

    # print('Books: ', books)
    # print('harry_potter: ', harry_potter)
    # print('lord_of_the_rings: ', lord_of_the_rings)
    # print('harry_potter_author: ', harry_potter_author)
    # print('lord_of_the_rings_author: ', lord_of_the_rings_author)
    # print('test3: ', test3)
    # print('test3_author: ', test3_author)

    return  render(request, 'book/home.html')

def admin_view(request):
    return render(request, 'book/admin_page.html')

def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            authors = request.POST.getlist('authors')
            print('Authors:', authors)

            book.save()

            # authors_list = []
            for name in authors:
                author, created_at = Author.objects.get_or_create(name=name)
                book.author_set.add(author)
                # authors_list.append(author)

            # book.author_set.set(authors_list)           # .set(authors_list) takes a list of authors and assign it to the corrsponding book or else for loop can be used

            print('Added book')

            return JsonResponse({'success': 'success'})

    else:
        form = AddBookForm()
        print('Book not added')

    context = {'form': form}
    return render(request, 'book/add_book.html', context)

def ajax_test(request):
    books = Book.objects.all()
    serialized_books = serialize('json', books)
    
    return JsonResponse({'books': serialized_books}, safe=False)

def book_search(request):
    print(request.GET)
    search = request.GET.get('term')
    payload = []
    if search:
        objs = Book.objects.filter(name__icontains=search)
        for obj in objs:
            payload.append(obj.name)


    return JsonResponse(payload, safe=False)

def add_author(request):
    form = AddAuthorForm()

    context = {'form': form}

    return render(request, 'book/add_author.html', context)


