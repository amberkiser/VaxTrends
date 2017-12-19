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

class VaxIncidenceRate(models.Model):
    year = models.IntegerField()
    disease = models.CharField(max_length = 200)
    vaccine = models.CharField(max_length = 200)
    incidence_rate = models.FloatField()
    
    def __str__(self):
        return '%s %d Vaccine: %s Incidence Rate: %d'%(self.disease, self.year,
                                                       self.vaccine, 
                                                       self.incidence_rate)

class DiseaseChoices(models.Model):
    disease = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.disease
    
class VaxHistory(models.Model):
    disease = models.CharField(max_length = 200)
    current_vaccine = models.CharField(max_length = 200)
    first_available = models.IntegerField()
    
    def __str__(self):
        return '%s Vaccine: %s First Available: %d'%(self.disease,
                                                     self.current_vaccine,
                                                     self.first_available)
