from django.test import TestCase
from .models import Scenarios

class ScenariosModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Scenarios.objects.create(
            scenario_level=1,
            scenario_title="Test Scenario",
            Background_info="This is some background information.",
            Decision_options="Option 1, Option 2, Option 3",
            Reward_points=100
        )

    def test_scenario_level(self):
        scenario = Scenarios.objects.get(id=1)
        self.assertEqual(scenario.scenario_level, 1)

    def test_scenario_title_max_length(self):
        scenario = Scenarios.objects.get(id=1)
        max_length = scenario._meta.get_field('scenario_title').max_length
        self.assertEqual(max_length, 255)

    def test_background_info_max_length(self):
        scenario = Scenarios.objects.get(id=1)
        max_length = scenario._meta.get_field('Background_info').max_length
        self.assertEqual(max_length, 255)

    def test_decision_options_max_length(self):
        scenario = Scenarios.objects.get(id=1)
        max_length = scenario._meta.get_field('Decision_options').max_length
        self.assertEqual(max_length, 255)

    def test_reward_points(self):
        scenario = Scenarios.objects.get(id=1)
        self.assertEqual(scenario.Reward_points, 100)

    def test_str_representation(self):
        scenario = Scenarios.objects.get(id=1)
        expected_str = scenario.scenario_title
        self.assertEqual(str(scenario), expected_str)
