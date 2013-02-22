from django.db import models

class Wish (models.Model):
    mystery = models.CharField(max_length=140)
    goal = models.CharField(max_length=140)
    place = models.CharField(max_length=140)

    class Meta (object):
        verbose_name_plural = 'Wishes'

    def __unicode__(self):
        return 'If we knew {0} then we could {1} in {2}'.format(
            self.mystery, self.goal, self.place)
