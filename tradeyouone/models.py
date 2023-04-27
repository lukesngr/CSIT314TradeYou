from django.db import models
from django.contrib.auth.models import User

#Models so far have no idea what they are going to be created by

class TradeYouUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)

class TradeYouProfessional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)

class MembershipPlan(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField()
    maxAssistanceCallouts = models.IntegerField()
    user = models.ForeignKey(TradeYouUser, on_delete=models.CASCADE)

class Review(models.Model):
    description = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(TradeYouUser, on_delete=models.CASCADE)
    professional = models.ForeignKey(TradeYouProfessional, on_delete=models.CASCADE)

class Rating(models.Model):
    value = models.IntegerField()
    user = models.ForeignKey(TradeYouUser, on_delete=models.CASCADE)
    professional = models.ForeignKey(TradeYouProfessional, on_delete=models.CASCADE)

class BillingHistory(models.Model):
    amount = models.FloatField()
    dateTime = models.DateTimeField()
    user = models.ForeignKey(TradeYouUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, null=True, blank=False)

class ServiceRequest(models.Model):
    dateTime = models.DateTimeField()
    status = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(TradeYouUser, on_delete=models.CASCADE)
    professional = models.ForeignKey(TradeYouProfessional, on_delete=models.CASCADE)

class Service(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=20, null=True, blank=True)
    price = models.FloatField()
    serviceRequest = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    billingHistory = models.ForeignKey(BillingHistory, on_delete=models.CASCADE)

class Payment(models.Model):
    user = models.ForeignKey(TradeYouUser, on_delete=models.CASCADE)
    service = models.ManyToManyField(Service, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=30, null=True, blank=True)

class Notification(models.Model):
    user = models.ForeignKey(TradeYouUser, on_delete=models.CASCADE)
    professional = models.ForeignKey(TradeYouProfessional, on_delete=models.CASCADE)
    message = models.CharField(max_length=50, null=True, blank=True)
    dateTime = models.DateField()