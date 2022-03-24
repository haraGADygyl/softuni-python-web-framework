from django.test import TestCase
from django.urls import reverse

from tests_demo.web.models import Profile


class ProfilesListViewTests(TestCase):
    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('list profiles'))

        self.assertTemplateUsed(response, 'profiles/list.html')

    def test_get__when_two_profiles__expect_context_to_contain_two_profiles(self):
        profiles_to_create = (
            Profile(first_name='Doncho', last_name='Minkov', age=15),
            Profile(first_name='Minko', last_name='Donchev', age=17),
        )

        Profile.objects.bulk_create(profiles_to_create)

        response = self.client.get(reverse('list profiles'))

        profiles = response.context['object_list']

        self.assertEqual(len(profiles), 2)
