import re
from django.test import TestCase
from django.urls import reverse

from .models import Mineral

#  Create your tests here.
class MineralModelTests(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name="Something",
            image_filename="Something",
            image_caption="Something",
            category="Something",
            formula="Something",
            strunz_classification="Something",
            color="Something",
            crystal_system="Something",
            unit_cell="Something",
            crystal_symmetry="Something",
            cleavage="Something",
            mohs_scale_hardness="Something",
            luster="Something",
            streak="Something",
            diaphaneity="Something",
            optical_properties="Something",
            refractive_index="Something",
            crystal_habit="Something",
            specific_gravity="Something"
        )
        name = "Something"
        self.assertEqual(mineral.name, name)

class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Something",
            image_filename="Something",
            image_caption="Something",
            category="Something",
            formula="Something",
            strunz_classification="Something",
            color="Something",
            crystal_system="Something",
            unit_cell="Something",
            crystal_symmetry="Something",
            cleavage="Something",
            mohs_scale_hardness="Something",
            luster="Something",
            streak="Something",
            diaphaneity="Something",
            optical_properties="Something",
            refractive_index="Something",
            crystal_habit="Something",
            specific_gravity="Something",
        )

    def test_minerals_home(self):
        resp = self.client.get(reverse('minerals:minerals-home'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/minerals_home.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse(
            'minerals:minerals-detail',
            kwargs={'pk': self.mineral.pk}
        ))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])

    def test_mineral_random_view(self):
        resp = self.client.get(reverse('minerals:minerals-random'))
        self.assertEqual(resp.status_code, 200)
        self.assertNotEqual(self.mineral.name, resp.context['mineral'])


class MineralSearchViewsTests(TestCase):
    def test_search_first_letter(self):
        letter = 'A'
        resp = self.client.get(reverse('minerals:minerals-home'))
        self.assertNotEqual(letter, resp.context['letter'])
