from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name="Модератор продуктов")
        can_unpublish = Permission.objects.get(codename="can_unpublish_product")
        delete_product = Permission.objects.get(codename="delete_product")
        group.permissions.add(can_unpublish, delete_product)
        self.stdout.write(self.style.SUCCESS("The group 'Модератор продуктов' was successfully created"))
