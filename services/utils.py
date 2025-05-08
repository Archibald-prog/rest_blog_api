from pytils.translit import slugify


def create_slug(instance, slug):
    model = instance.__class__
    unique_slug = slugify(slug)
    qs = model.objects.filter(slug=unique_slug).order_by('-id')
    while qs.exists():
        unique_slug = f'{unique_slug}-{qs.first().id}'
    return unique_slug
