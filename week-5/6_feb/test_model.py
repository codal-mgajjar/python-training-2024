from blog.models import Blog, Entry


#creating foreign key object
from datetime import date
codal = Blog.objects.create(name='codal')
pop = Blog.objects.create(name='pop')
Entry.objects.create(blog=codal,headline='codal welcomes you',pub_date=date(2024,1,1))


# Updating foreign key field
entry = Entry.objects.get(pk=1)
cheese_blog = Blog.objects.get(name='Codal')
entry.blog = cheese_blog
entry.save()

#adding many to many data
from blog.models import Author
joe = Author.objects.create(name='joe')
entry.authors.add(joe)

#retrieving all objects
a = Entry.objects.all()

#retrieving specific using filter
Entry.objects.filter(pub_date__year=2024)
Entry.objects.all().filter(pub_date__year=2024)

#filter querysets are unique
q1 = Entry.objects.filter(headline__startswith='What')
q2 = q1.exclude(pub_date__gte= date.today())
q3 = q1.filter(pub_date__gte= date.today())

#Retrieving a single object with get()
one_entry = Entry.objects.get(pk=1)
one_entry = Entry.objects.filter(pk=2)[0]

#Limiting querysets
Entry.objects.all()[:5]
Entry.objects.all()[5:10]

#order by
Entry.objects.order_by('headline')[0]

#exact and iexact
Entry.objects.get(headline__exact='codal welcomes meshw')
Entry.objects.get(headline__iexact='codal welcomes meshw')

# contains
Entry.objects.get(headline__contains='meshw')

#istartswith and iendswith
Entry.objects.filter(headline__istartswith='codal')
Entry.objects.filter(headline__iendswith='meshw')

#lookups
Entry.objects.filter(blog__name='codal')
Blog.objects.filter(entry__headline__contains='codal')
Blog.objects.filter(entry__authors__name__isnull=True)
Blog.objects.filter(entry__headline__contains='codal', entry__pub_date__year=2024)
Blog.objects.exclude(entry__headline__contains='codal',entry__pub_date__year=2024)


#pk shortcuts
Blog.objects.get(id__exact=2)
Blog.objects.get(pk=2)
Blog.objects.get(id=2)

#caching and querysets
print([e.headline for e in Entry.objects.all()])
querysets = Entry.objects.all()
list(querysets)
bool(querysets)


# storing none values
from blog.models import Dog
Dog.objects.create(name='max',data=None)
Dog.objects.filter(data__isnull=True)
Dog.objects.create(name='Meg', data={'breed': 'collie', 'owner': None})
Dog.objects.filter(data__breed='collie')



#contains and contained
Dog.objects.filter(data__contains={'owner': 'Bob'})
Dog.objects.filter(data__contained_by={'breed': 'collie', 'owner': 'Bob'})

#has_key and has_keys and has_any_keys
Dog.objects.filter(data__has_key='owner')
Dog.objects.filter(data__has_keys=['breed', 'owner'])
Dog.objects.filter(data__has_any_keys=['owner', 'breed'])

#comparison
Entry1 = Entry.objects.get(pk=2)
Entry2 = Entry.objects.get(pk=3)
Entry1 == Entry2

#deleting object
Entry1.delete()
Entry.objects.filter(pub_date__year=2024).delete()

#updating objects
Entry.objects.filter(pub_date__year=2024).update(headline='codal')


#Aggregation

# average
from django.db.models import Avg
from blog.models import *
Book.objects.aggregate(Avg('price'))
Book.objects.aggregate(average_price=Avg('price'))

#min and max
from django.db.models import Max, Min
Book.objects.aggregate(Max('price'), Min('price'))

# Counting specific argument
from django.db.models import Count
q = Book.objects.annotate(Count('authors'))
q[0]
q[0].authors__count

# Combining multiple aggregations
q = Book.objects.annotate(Count('authors'), Count('store'))
q[0].authors__count
q[0].store__count

#To avoid duplicate items we can use distinct parameter
q = Book.objects.annotate(Count('authors', distinct=True), Count('store', distinct=True))

#Join and aggregates

Store.objects.aggregate(min_price=Min('books__price'), max_price=Max('books__price'))
Store.objects.annotate(min_price=Min('books__price'), max_price=Max('books__price'))

#Following relationship backwards

Publisher.objects.annotate(Count('book'))
Publisher.objects.aggregate(oldest_pubdate=Min('book__pubdate'))

#order of annotate
a, b = Publisher.objects.filter(book__rating__gt=3.0).annotate(avg_rating=Avg('book__rating'))


#Relationships

#One to one relation
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(models.Model):
    place = models.OneToOneField(Place,on_delete=models.CASCADE,primary_key=True)
    serves_pizza = models.BooleanField(default=False)

#One to many relation
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()

#Many to many relation

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

class Entry(models.Model):
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    authors = models.ManyToManyField(Author)

#Raw queries

for p in Entry.manager.raw('SELECT * FROM blog_entry'):
     print(p)

#index lookup
Entry.manager.raw('SELECT * FROM blog_entry')[:]
Entry.manager.raw('SELECT * FROM blog_entry')[0]
