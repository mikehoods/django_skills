from django.db import models

# Create your models here.


class Skill(models.Model):
    description = models.CharField(max_length=200)
    skill_level = models.IntegerField()
    # user_id = models.ForeignKey()

    def __str__(self):
        return '%s %s' % (self.description, self.skill_level)

    def save(self, *args, **kwargs):
        return super(Skill, self).save(*args, **kwargs)