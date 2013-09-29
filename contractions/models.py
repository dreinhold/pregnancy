from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Contraction(models.Model):
  start_ts  = models.DateTimeField();
  end_ts    = models.DateTimeField(blank=True, null=True)
  intensity = models.SmallIntegerField(blank=True, null=True)
  notes     = models.TextField(blank=True, null=True)

  class Meta:
    ordering = ["-start_ts"]

  def __unicode__(self):
    return str(self.start_ts)

  def length(self):
    if(self.end_ts):
      return str(self.end_ts - self.start_ts)
    else:
      return "NA"

  def get_url_update_intensity(self):
    return reverse('UpdateIntensity', kwargs={'pk': self.id})
 
  def get_url_stop_contraction(self):
    return reverse('StopContraction', kwargs={'pk': self.id})
