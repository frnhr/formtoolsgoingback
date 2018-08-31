from django.db import models


class WizardResponse(models.Model):
    response_1_1 = models.CharField(null=False, blank=False, max_length=254)
    response_1_2 = models.CharField(null=False, blank=False, max_length=254)
    response_2_1 = models.CharField(null=False, blank=False, max_length=254)
    response_2_2 = models.CharField(null=False, blank=False, max_length=254)
    response_3_1 = models.CharField(null=False, blank=False, max_length=254)
    response_3_2 = models.CharField(null=False, blank=False, max_length=254)

    @property
    def data(self):
        data = {}
        for field in self._meta.fields[1:]:
            data[field.name] = getattr(self, field.name)
        return data
