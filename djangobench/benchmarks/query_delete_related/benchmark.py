from djangobench.utils import run_benchmark

def benchmark():
    global Book
    Book.objects.all().delete()

def setup():
    global Book
    from query_delete_related.models import Book, Chapter
    b1 = Book.objects.create(title='hi')
    b2 = Book.objects.create(title='hi')
    b3 = Book.objects.create(title='hi')
    for i in range(0, 5):
        Chapter.objects.create(book=b1, title='chapter%d' % i)
        Chapter.objects.create(book=b2, title='chapter%d' % i)
        Chapter.objects.create(book=b3, title='chapter%d' % i)

run_benchmark(
    benchmark,
    meta={
        'description': 'Delete an object via QuerySet.delete(), '
                       'objects deleted have related objects.',
    },
    setup=setup
)
