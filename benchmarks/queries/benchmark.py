import time

from django.core.management import call_command

from queries.models import Book

call_command("syncdb")

start = time.time()

for i in xrange(10):
    Book.objects.create(title=unicode(i))


print time.time() - start
