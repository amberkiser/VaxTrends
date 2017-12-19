from django.db import models

class VaxCoverage(models.Model):
    year = models.IntegerField()
    vaccine = models.CharField(max_length = 200)
    ci_lower = models.FloatField()
    ci_upper = models.FloatField()
    coverage = models.FloatField()
    
    def __str__(self):
        return '%s   %d   Coverage: %d CI_Lower: %d CI_Upper: %d'\
    %(self.vaccine, self.year, self.coverage, self.ci_lower, self.ci_upper)
    
class VaxChoices(models.Model):
    vaccine = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.vaccine

