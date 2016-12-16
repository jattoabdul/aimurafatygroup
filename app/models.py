from django.db import models
from django.utils import timezone


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=500, verbose_name='Company Name')
    history = models.CharField(max_length=500, verbose_name='History')
    whatwedo = models.CharField(max_length=500, verbose_name='What We Do')
    whoweare = models.TextField(verbose_name='Who We Are')
    mission = models.CharField(max_length=500, verbose_name='Our Mission')
    vision = models.CharField(max_length=500, verbose_name='our Vision')
    corevalues = models.CharField(max_length=500, verbose_name='our Core Values')

    def __str__(self):
        return '%s' % self.history


class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=250)
    bio = models.TextField()
    email = models.EmailField(verbose_name='Staff Email')
    phone_number = models.CharField(max_length=15, verbose_name='Mobile Phone Number')
    office_number = models.CharField(max_length=15, verbose_name='Work/Office Phone Number')
    fb_username = models.CharField(max_length=100, verbose_name='Facebook Username', blank=True)
    twitter_handle = models.CharField(max_length=100, verbose_name='Twitter Handle', blank=True)
    linkedin_username = models.CharField(max_length=100, verbose_name='Linkedin Username', blank=True)
    dribble_username = models.CharField(max_length=100, verbose_name='Dribble Username', blank=True)
    image_url = models.ImageField(upload_to='staff', verbose_name='Staff Profile Image')

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class AboutFeed(models.Model):
    client_name = models.CharField(max_length=100, verbose_name='Client Name')
    client_feed = models.TextField(verbose_name='Client Feedback', blank=True)
    job_desc = models.TextField(verbose_name='Client\'s Job Description', blank=True)
    client_position = models.CharField(max_length=100, verbose_name='Client Position/Rank')
    client_company = models.CharField(max_length=250, verbose_name='Client Company')
    client_url = models.URLField(verbose_name='Project URL', blank=True)
    client_logo = models.ImageField(upload_to='clients/logo', verbose_name='Client Company Logo')
    client_image = models.ImageField(upload_to='clients/pics', verbose_name='Client\'s Profile Picture')

    def __str__(self):
        return u'%s %s' % (self.client_name, self.client_position)


class Service(models.Model):
    service_name = models.CharField(max_length=100, verbose_name='Service Name')
    service_desc = models.CharField(max_length=500, verbose_name='Service Brief Description')
    service_detail = models.TextField(verbose_name='Service Details')
    service_icon = models.CharField(max_length=50, verbose_name='Service Icon', default='desktop')
    service_percent = models.IntegerField(blank=True, verbose_name='Service Proficiency Percent')
    service_image = models.ImageField(upload_to='services', verbose_name='Service Image')

    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service_name


class Consultancyservice(models.Model):
    cservice_name = models.CharField(max_length=100, verbose_name='Consultancy Service Name')
    cservice_desc = models.CharField(max_length=500, verbose_name='Consultancy Service Brief Description')
    cservice_detail = models.TextField(verbose_name='Consultancy Service Details')
    cservice_icon = models.CharField(max_length=50, verbose_name='Consultancy Service Icon', default='user')

    class Meta:
        verbose_name_plural = 'Consultancyservices'

    def __str__(self):
        return self.cservice_name
