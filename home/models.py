from django.db import models


# Create your models here.


class Banner(models.Model):
    name = models.CharField(max_length=100, verbose_name='Full Name')
    degree = models.CharField(max_length=100, verbose_name='Education or Expertise')
    short_desc = models.TextField(blank=True, null=True, verbose_name='Short Description (optional)')
    about_me = models.TextField(default='Write a description about yourself and your goals', verbose_name='About Me')
    birthday = models.DateField(blank=True, null=True, verbose_name='Birthday Date (optional)')
    phone_number = models.IntegerField(blank=True, null=True, verbose_name='Phone Number (optional)')
    email = models.EmailField(blank=True, null=True, verbose_name='Email (optional)')
    linkedin_url = models.CharField(max_length=200, blank=True, null=True, verbose_name='LinkedIn Link (optional)')
    telegram_url = models.CharField(max_length=200, blank=True, null=True, verbose_name='Telegram Link (optional)')
    instagram_url = models.CharField(max_length=200, blank=True, null=True, verbose_name='Instagram Link (optional)')
    image = models.ImageField(upload_to='Avatar', verbose_name='Profile Photo')
    image_2 = models.ImageField(upload_to='Avatar', verbose_name='Second Profile Photo ', default='logo.png')
    cv = models.FileField(upload_to='CV', null=True, blank=True, verbose_name='CV')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'

class Activity(models.Model):
    title = models.CharField(max_length=25, verbose_name='Title')
    desc = models.TextField(null=True, blank=True, verbose_name='Description (optional)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Activity and Interest'
        verbose_name_plural = 'Activities and Interests'

class Skill(models.Model):
    skill = models.CharField(max_length=50, verbose_name='Skill')
    level = models.IntegerField(verbose_name='Level of expertise (between 0 and 100)')

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'




class Language(models.Model):
    language = models.CharField(max_length=50, verbose_name='Language')
    level = models.IntegerField(verbose_name='Level of expertise (between 0 and 100)')

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class MyExperience(models.Model):
    title = models.CharField(max_length=20, verbose_name='Title')
    desc = models.CharField(max_length=100, verbose_name='Little Description')
    date = models.DateField(verbose_name='Date')
    desc_2 = models.TextField(blank=True, null=True, verbose_name='Description (optional)')
    image = models.ImageField(upload_to='Experience', verbose_name='Photo (optional)', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'My Experience'
        verbose_name_plural = 'My Experiences'


class MyEducation(models.Model):
    title = models.CharField(max_length=20, verbose_name='Title')
    desc = models.CharField(max_length=100, verbose_name='Little Description')
    date = models.DateField(verbose_name='Date')
    desc_2 = models.TextField(blank=True, null=True, verbose_name='Description (optional)')
    image = models.ImageField(upload_to='Education', verbose_name='Photo (optional)', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'My Education'
        verbose_name_plural = 'My Educations'


class Research(models.Model):
    title = models.CharField(max_length=30, verbose_name='Title')
    description = models.TextField(default='Description')
    opinion = models.TextField(default='Opinion', verbose_name='My opinion about this (optional)')
    link = models.CharField(null=True, blank=True, max_length=50, verbose_name='Link', default='https://')
    file = models.FileField(null=True, blank=True, upload_to='Researches',
                            verbose_name='Article (PDF or Word file)(optional)')
    references = models.FileField(null=True, blank=True, upload_to='Researches',
                                  verbose_name='References (.txt file)(optional)')
    image = models.ImageField(null=True, blank=True, upload_to='Researches', verbose_name='Photo (optional)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Research'
        verbose_name_plural = 'Researches'


class ContactMe(models.Model):
    name = models.CharField(max_length=20, verbose_name='Full Name')
    email = models.EmailField(max_length=25, verbose_name='Email')
    subject = models.CharField(max_length=20, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    is_read = models.BooleanField(default=False, verbose_name='Readed / Not Readed')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
