from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

semester_validator = RegexValidator(r'(fa|sp)20[0-9][0-9]')

class Member(AbstractUser):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('associate_first', 'First Semester Associate'),
        ('associate_second', 'Second Semester Associate'),
        ('alumni', 'Alumni'),
    )

    semester_joined = models.CharField([semester_validator], max_length=6, blank=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
    bio = models.TextField(blank=True)
    attendance = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    title = models.TextField(default='General Member')

    # contact/social info
    cell_phone = models.CharField(max_length=11, blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    instagram = models.CharField(max_length=300, blank=True)
    snapchat = models.CharField(max_length=300, blank=True)

    def __unicode__(self):
        return u'%s' % self.username

class Event(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    title = models.TextField()
    description = models.TextField()
    time = models.DateTimeField()
    speaker_first_name = models.CharField(max_length=100)
    speaker_last_name = models.CharField(max_length=100)
    speaker_bio = models.TextField()
    projected_attendance = models.IntegerField()
    venue = models.TextField(default='TBD')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='created_events')
    point_person = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='pp_events')
    confirmed = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    # link fields
    facebook_link = models.CharField(max_length=300, blank=True)
    eventbrite_link = models.CharField(max_length=300, blank=True)
    elf_link = models.CharField(max_length=300, blank=True)
    elf_exemption_link = models.CharField(max_length=300, blank=True)
    fbcover_link = models.CharField(max_length=300, blank=True)
    website_photo_link = models.CharField(max_length=300, blank=True)
    seal_link = models.CharField(max_length=300, blank=True)

    @property
    def speaker_full_name(self):
        return u'%s %s' % (self.speaker_first_name, self.speaker_last_name)

    def __unicode__(self):
        return u'%s' % self.name

class Group(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    friendly_name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name

class Committee(Group):
    members = models.ManyToManyField(Member, related_name='committees')
    vp = models.ForeignKey(Member, on_delete=models.CASCADE)

class SubCommittee(Group):
    parent_committee = models.ForeignKey(Committee, on_delete=models.CASCADE,
                                  related_name='subcommittees')
    members = models.ManyToManyField(Member, related_name='subcommittees')
    project_manager = models.ForeignKey(Member, on_delete=models.CASCADE)

class Division(Group):
    members = models.ManyToManyField(Member, related_name='divisions')
    director = models.ForeignKey(Member, on_delete=models.CASCADE)
