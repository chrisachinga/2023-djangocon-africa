from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    """
    An extension of the base user model from Django
    """
    USER_TYPE_CHOICES = (
        ('Mentor', 'Mentor'),
        ('Mentee', 'Mentee'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='Mentee')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Prefer not to say')
    year_of_birth = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.username

    # Overriding the groups field to resolve reverse accessor clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="customuser_set",
        related_query_name="user",
    )

    # Overriding the user_permissions field to resolve reverse accessor clashes
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="user",
    )


class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} at {self.company_name}"

class Education(models.Model):
    institution_name = models.CharField(max_length=255, verbose_name='Institution Name')
    field_of_study = models.CharField(max_length=255, verbose_name='Field of Study')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} from {self.institution_name}"
        
# Profile model for Mentor users with a one-to-one relation to CustomUser
class MentorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, related_name='mentor_profiles', blank=True)
    work_experience = models.ManyToManyField(WorkExperience, related_name='mentor_work_experience', blank=True)
    
    def __str__(self):
        return f"Mentor Profile of {self.user.username}"
    
# Profile model for Mentee users with a one-to-one relation to CustomUser
class MenteeProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, related_name='mentee_profiles', blank=True)
    education = models.ManyToManyField(Education, related_name='mentee_education', blank=True)
    
    def __str__(self):
        return f"Mentee Profile of {self.user.username}"
        
def validate_dates(sender, **kwargs):
    if sender.end_date and sender.end_date < sender.start_date:
        raise ValidationError("End date should be after start date.")
      
models.signals.pre_save.connect(validate_dates, sender=WorkExperience)
models.signals.pre_save.connect(validate_dates, sender=Education)

# Signal to create a profile instance whenever a CustomUser instance is created
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'Mentor':
            MentorProfile.objects.create(user=instance)
        else:
            MenteeProfile.objects.create(user=instance)

# Signal to save the profile instance whenever the related CustomUser instance is saved
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 'Mentor':
        instance.mentorprofile.save()
    else:
        instance.menteeprofile.save()
