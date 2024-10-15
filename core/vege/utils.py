from django.utils.text import slugify
import uuid

def generate_slugify(title):
    title = slugify(title)
    from .models import Recipe

    while (Recipe.objects.filter(slug = title).exists()):
        title = f'{slugify(title)}-{str(uuid.uuid4())[0:4]}'

    return title