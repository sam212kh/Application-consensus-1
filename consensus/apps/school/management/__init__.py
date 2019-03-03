from django.db.models.signals import post_migrate
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.apps import apps


# noinspection PyUnusedLocal,PyUnusedLocal
def add_app_content_type(sender, **kwargs):
    for app in apps.get_app_configs():
        appname = app.name
        try:
            ContentType.objects.get(model='', app_label=appname)
        except ContentType.DoesNotExist:
            ct = ContentType(model='', app_label=appname)
            ct.save()


# noinspection PyUnusedLocal
def add_view_permissions(sender, **kwargs):
    """
    This migrate hooks takes care of adding a view permission too all our
    content types.
    """
    # for each of our content types
    for content_type in ContentType.objects.all():
        # build our permission slug
        if content_type.model == '':
            codename = "view_%s_app" % content_type.app_label
        else:
            codename = "view_%s" % content_type.model

        # if it doesn't exist..
        if not Permission.objects.filter(content_type=content_type,
                                         codename=codename):
            # add it
            Permission.objects.create(content_type=content_type,
                                      codename=codename,
                                      name="Can view %s" % content_type.name)
            # print("Added view permission for %s" % content_type.name)


# check for all our view permissions after a migrate
post_migrate.connect(add_app_content_type)
post_migrate.connect(add_view_permissions)
