import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogger.settings")  
django.setup()

from blog.models import Post
from django.utils import timezone

post = Post.objects.create(
    title='My First Post',
    slug='my-first-post',
    body='This is the body of my first post.',
    publish=timezone.now()
)
