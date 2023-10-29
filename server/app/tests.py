from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from app.models import CustomUser, Skill, WorkExperience, Education, MentorProfile, MenteeProfile

class CustomUserTestCase(TestCase):
    def test_crud_custom_user(self):
        # Create
        user = CustomUser.objects.create(username='testuser', user_type='Mentor', gender='Male', year_of_birth=1990)
        # Read
        user = CustomUser.objects.get(username='testuser')
        self.assertEqual(str(user), 'testuser')
        # Update
        user.username = 'updateduser'
        user.save()
        self.assertEqual(user.username, 'updateduser')
        # Delete
        user.delete()
        with self.assertRaises(CustomUser.DoesNotExist):
            CustomUser.objects.get(username='updateduser')

class SkillTestCase(TestCase):
    def test_crud_skill(self):
        # Create
        skill = Skill.objects.create(name='Python', description='Programming Language')
        # Read
        skill = Skill.objects.get(name='Python')
        self.assertEqual(str(skill), 'Python')
        # Update
        skill.name = 'Updated Python'
        skill.save()
        self.assertEqual(skill.name, 'Updated Python')
        # Delete
        skill.delete()
        with self.assertRaises(Skill.DoesNotExist):
            Skill.objects.get(name='Updated Python')


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user_mentor = CustomUser.objects.create(username='mentoruser', user_type='Mentor')
        self.user_mentee = CustomUser.objects.create(username='menteeuser', user_type='Mentee')

    def test_profile_creation(self):
        self.assertIsNotNone(self.user_mentor.mentorprofile)
        self.assertIsNotNone(self.user_mentee.menteeprofile)

    def test_profile_str(self):
        self.assertEqual(str(self.user_mentor.mentorprofile), 'Mentor Profile of mentoruser')
        self.assertEqual(str(self.user_mentee.menteeprofile), 'Mentee Profile of menteeuser')

    def test_crud_mentor_profile(self):
        # Read
        mentor_profile = MentorProfile.objects.get(user=self.user_mentor)
        # Update
        skill = Skill.objects.create(name='New Skill')
        mentor_profile.skills.add(skill)
        mentor_profile.save()
        self.assertIn(skill, mentor_profile.skills.all())
        # Delete
        mentor_profile.delete()
        with self.assertRaises(MentorProfile.DoesNotExist):
            MentorProfile.objects.get(user=self.user_mentor)

    def test_crud_mentee_profile(self):
        # Read
        mentee_profile = MenteeProfile.objects.get(user=self.user_mentee)
        # Update
        education = Education.objects.create(
            institution_name='Tech University',
            field_of_study='Computer Science',
            start_date=timezone.now().date()
        )
        mentee_profile.education.add(education)
        mentee_profile.save()
        self.assertIn(education, mentee_profile.education.all())
        # Delete
        mentee_profile.delete()
        with self.assertRaises(MenteeProfile.DoesNotExist):
            MenteeProfile.objects.get(user=self.user_mentee)
