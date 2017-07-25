from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class Event(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    title = models.TextField()
    description = models.TextField()
    time = models.DateTimeField()
    speaker_first_name = models.CharField(max_length=100)
    speaker_last_name = models.CharField(max_length=100)
    projected_attendance = models.IntegerField()
    venue = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    # link fields
    facebook_link = models.CharField(max_length=300)
    eventbrite_link = models.CharField(max_length=300)
    elf_link = models.CharField(max_length=300)
    elf_exemption_link = models.CharField(max_length=300)
    fbcover_link = models.CharField(max_length=300)
    websitephoto_link = models.CharField(max_length=300)
    seal_link = models.CharField(max_length=300)

    def get_speaker_name(self):
        return '%s %s' % (speaker_first_name, speaker_last_name)

semester_validator = RegexValidator(r'(fa|sp)20[0-9][0-9]')

class Member(AbstractUser):
    semester_joined = models.CharField([semester_validator], max_length=6, blank=True)
    status = models.IntegerField(default=0)
    bio = models.TextField(blank=True)
    attendance = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def get_status(self):
        if self.status == 0:
            return 'active'
        elif self.status == 1:
            return 'first semester associate'
        elif self.status == 2:
            return 'second semester associate'
        else:
            return 'alumni'

class Group(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    friendly_name = models.CharField(max_length=200)

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
