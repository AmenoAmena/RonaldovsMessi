from django.db import models

class Ronaldo(models.Model):

    score_r = models.PositiveIntegerField(default=0)

    def increase_score_r(self):
        self.score_r += 1
        self.save()



class Messi(models.Model):

    score_m = models.PositiveIntegerField(default=0)

    def increase_score_m(self):
        self.score_m += 1
        self.save()
