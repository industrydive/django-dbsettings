from django.db import models
from django.contrib.sites.models import Site


class SettingManager(models.Manager):
    def get_query_set(self):
        all = super(SettingManager, self).get_query_set()
        return all.filter(site=Site.objects.get_current())

    # Not passing in class_name, because for some reason the 
    # class_name column is blank for every row
    def get_all_sites(self, group_obj, attribute_name):
        return self._get_all_sites(group_obj.__module__, attribute_name)

    def _get_all_sites(self, module_name, attribute_name):
        results = super(SettingManager, self).get_query_set().filter(
            module_name__exact=module_name,
            attribute_name__exact=attribute_name
        ).values('site_id', 'value')

        ret_val = dict()
        for r in results:
            ret_val[r['site_id']] = r['value']

        return ret_val


class Setting(models.Model):
    site = models.ForeignKey(Site)
    module_name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255, blank=True)
    attribute_name = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True)

    objects = SettingManager()
    all_sites = models.Manager()


    class Meta:
        unique_together = ('site', 'module_name', 'class_name', 'attribute_name')


    def __nonzero__(self):
        return self.pk is not None

    def save(self, *args, **kwargs):
        self.site = Site.objects.get_current()
        return super(Setting, self).save(*args, **kwargs)
