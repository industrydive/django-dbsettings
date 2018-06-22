from django.db import models

from dbsettings.settings import USE_SITES, VALUE_LENGTH

if USE_SITES:
    from django.contrib.sites.models import Site

    class SettingManager(models.Manager):
        def get_queryset(self):
            sup = super(SettingManager, self)
            qs = sup.get_queryset() if hasattr(sup, 'get_queryset') else sup.get_query_set()
            return qs.filter(site=Site.objects.get_current())
        get_query_set = get_queryset


class Setting(models.Model):
    if USE_SITES:
        site = models.ForeignKey(Site)
        objects = SettingManager()
        all_sites = models.Manager()
    module_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255, blank=True)
    attribute_name = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True)





    class Meta:
        unique_together = ('site', 'module_name', 'class_name', 'attribute_name')
        app_label = 'dbsettings'


    def __bool__(self):
        return self.pk is not None
    if USE_SITES:
        def save(self, *args, **kwargs):
            if not self.site_id:
                self.site = Site.objects.get_current()
            return super(Setting, self).save(*args, **kwargs)
