from django.shortcuts import render, redirect
from time import strftime,gmtime
from apps.dashboard.models import *

# things that are done
    # can add books
    # can add authors
    # able to list all the authors on the correct template
    # able to view all the books on the correct template

# things to work on
    # able to drop down all the author that are not assiciated with the already chosen book
    # able to drop down all the books that are not assiciated with the already chosen author
    # more css
    # maybe create an edit page for both books and authors


def homePg(request):
    print('**************inside the homePg aka the showBooks area function********')

    context = {
        "books": Book.objects.all()
    }

    # we need to get all the books from the DB to out put on the HTML Webpag for the UI
    
    print('**************end of the homePg aka the showBooks area function********')
    return render(request,'dashboard/homePg.html', context)

def addBook(request, methods = 'POST'):
    print("********inside of the addBook function*******")

    print(request.POST)

    if request.POST['title'] is not '' and request.POST['description'] is not '':
        Book.objects.create(title = request.POST['title'], desc = request.POST['description'])

    

    print("********end of the addBook function*******")
    return redirect('/')





def showAuthors(request):
    print("********inside of the showAuthors function*******")

    context = {
        "authors" : Author.objects.all()
    }
    
    print("********end of the showAuthors function*******")
    return render(request, 'dashboard/homePgAuthors.html',context)

def addAuthor(request, methods = 'POST'):
    print("********inside of the addAuthor function*******")
    
    print(request.POST)

    # this prevents the making authors with out a first and last name
    if request.POST['first_name'] is not '' and request.POST['last_name'] is not'':
        Author.objects.create(first_name = request.POST['first_name'], 
                              last_name = request.POST['last_name'],
                              notes = request.POST['notes'])

    print("********end of the addAuthor function*******")
    return redirect('/authors')







def bookDetails(request,id_book):
    print("********inside of the bookDetails function*******")

    # take the id_book and pass it back into the HTML
    # in oder to display stuff on the screen

    b = Book.objects.get(id=id_book)
    print(b)

    authors_of_the_book = b.authors.all()
    print('\t all the authors that have worked on this book',authors_of_the_book)

    # creating an arry to save all the ids of authors that have already worked on this book
    # so we can exclude them from another list
    arr=[] 

    # variable 'a' in this for loop is an already assiciated author with the book, thus we need to call upon 
    # the ojbect Author's id and put it into the array
    for a in authors_of_the_book:
        arr.append(a.id)    
    # now this is an array of already assicated authors with the chosen book we are examining


    # this new variable is a list of authors that are not assicated with the chosen book
    authors_we_can_add = Author.objects.exclude(id__in=arr)

    # therefore, take note that authors_of_the_book joined with authors_we_add is the entire BD of authors
    # they should be muttuially exclusive


    # now lets make a single dictonary to pass back into the HTML and call apon the information by the context's keys
    context = {
        "chosen_book" : b,
        "authors_from_chosen_book" : authors_of_the_book,
        'authors_we_can_add' : authors_we_can_add,
    }
    
    print("********end of the bookDetails function*******")
    return render(request, 'dashboard/details.html', context)


def authorDetails(request, id_author):
    print("********inside of the authorDetails function*******")
    
    a = Author.objects.get(id=id_author)

    print(a)

    books_of_the_author = a.books.all()
    print("\tall the books the authors has written ", books_of_the_author)

    arr = []
    for book in books_of_the_author:
        arr.append(book.id)
    
    print('\tarray of indexes of all the books the author has written',arr)


    books_we_can_add = Book.objects.exclude(id__in=arr)
    # usally .exclude needs a books listed with comma inbetween, but using id__in we can pass an array

    print("\t authors to add to the drop down",books_we_can_add)

    context = {
        'chosen_author' : a,
        'books_from_chosen_author' : books_of_the_author,
        'books_we_can_add' : books_we_can_add
    }

    print("********end of the authorDetails function*******")
    return render(request, 'dashboard/detailsAuthor.html', context)









def addBookToAuthor(request):
    print('*-*--*-*-*-*-*addAuthorToBook function-*-*-*-*-*-*-*-*-*')

    # everything that got passed to us from the form submission
    print(request.POST)

    # getting the two objects that we are chaging
    author = Author.objects.get(id=request.POST['id_author'])
    book= Book.objects.get(id=request.POST['id_book'])

    # joining them and manipulating the DB
    author.books.add(book)

    print('*-*--*-*-*-*-*end of addAuthorToBook function-*-*-*-*-*-*')
    return redirect(f'/author/{author.id}')
















def addAuthorToBook(request):
    # print('*-*--*-*-*-*-*addAuthorToBook function-*-*-*-*-*-*-*-*-*')
    print(request.POST)

    

    # get both of the objects that we are joining together
    book = Book.objects.get(id=request.POST['id_book'])
    author = Author.objects.get(id=request.POST['id_author'])

    # join the author to the book
    book.authors.add(author)

    # now we have manipulated the DB

    
    # print('*-*--*-*-*-*-*end of addAuthorToBook function-*-*-*-*-*-*')
    return redirect(f'/book/{book.id}')
