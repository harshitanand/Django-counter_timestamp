from django.db import models

# Create your models here.
class counter (models.Model):
	hit_count = models.IntegerField(max_length=999)
	time_count = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return u'%s %s' % (self.time_count, str(self.hit_count))
