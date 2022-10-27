from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.city_name


# class Date(models.Model):
#     city_name = models.ForeignKey(City, on_delete=models.CASCADE)
#     pub_date = models.DateField('date published')
#     def __str__(self):
#         return self.city_name


class Temperature(models.Model):
    city_name = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.CharField(max_length=200)
    def __str__(self):
        return self.city_name
    