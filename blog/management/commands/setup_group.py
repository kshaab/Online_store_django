from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from blog.models import BlogPost


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name="Контент-менеджер")
        content_type = ContentType.objects.get_for_model(BlogPost)
        can_add = Permission.objects.get(codename="add_blogpost", content_type=content_type)
        can_change = Permission.objects.get(codename="change_blogpost", content_type=content_type)
        can_delete = Permission.objects.get(codename="delete_blogpost", content_type=content_type)
        group.permissions.add(can_add, can_change, can_delete)
        self.stdout.write(self.style.SUCCESS("The group 'Контент-менеджер' was successfully created"))
