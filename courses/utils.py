import asyncio

from asgiref.sync import sync_to_async
from courses.models import *


@sync_to_async
def get_all_courses():
    return Course.objects.all()


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        section = asyncio.run(get_all_courses())
        context['section'] = section
        if 'sect_selected' not in context:
            context['sect_seslected'] = 0
        return context