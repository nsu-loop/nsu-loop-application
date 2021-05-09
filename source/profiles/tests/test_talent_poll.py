import pytest

from django.urls import reverse, resolve


class TestUrls:

    # This method will test of the right talent poll url
    def test_talent_poll_url(self):
        path = reverse('talent-poll')

        assert resolve(path).view_name == 'talent-poll'


class TestTalentPollFeature(TestCase):

    # Prepare setup for testing. It is a framework defined method.
    # The method name has to be setUp(), otherwise it will not work.
    def setUp(self):
        Skill.objects.create(name="c++")
        Skill.objects.create(name="c")
        Skill.objects.create(name="c#")
        Skill.objects.create(name="java")
        Skill.objects.create(name="python")

        User.objects.create(username="abc def", password="12345678abc")
        User.objects.create(username="def ghi", password="12345678abc")
        User.objects.create(username="ghi jkl", password="12345678abc")
        User.objects.create(username="jkl mno", password="12345678abc")
        User.objects.create(username="mno pqr", password="12345678abc")

        self.selected_skill = None
        self.selected_friends = None
        self.selected_friend = None

    # This method will test whether selected skill exist in predefined skills or not
    def test_skill(self):
        skills = Skill.objects.all()
        skill_index = random.sample(range(0, len(skills)), 1)[0]
        self.skills = skills
        self.selected_skill = skills[skill_index]

        self.assertIn(self.selected_skill, self.skills)
        print("skill selection passed")

    # This method will test whether friends number for selecting talent poll is equal to choice number
    def test_friends(self):
        friends = Profile.objects.all()
        self.choice_number = 5
        if len(friends) < self.choice_number:
            self.choice_number = len(friends)
        friend_indexes = random.sample(range(0, len(friends)), self.choice_number)
        friends = [friends[i] for i in friend_indexes]
        self.selected_friends = friends

        self.assertEqual(len(self.selected_friends), self.choice_number)
        print("friend selection passed")
