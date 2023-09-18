from django.test import TestCase
from .models import Scenarios
class ScenariosModelTest(TestCase):
    def test_create_scenario(self):
        scenario = Scenarios(
            scenario_level=1,
            scenario_title="Sample Scenario",
            Background_info="Background information for the scenario",
            Decision_options="Option 1, Option 2, Option 3",
            Reward_points=100
        )
        scenario.save()
        saved_scenario = Scenarios.objects.get(pk=scenario.pk)
        self.assertEqual(saved_scenario.scenario_level, 1)
        self.assertEqual(saved_scenario.scenario_title, "Sample Scenario")
        self.assertEqual(saved_scenario.Background_info, "Background information for the scenario")
        self.assertEqual(saved_scenario.Decision_options, "Option 1, Option 2, Option 3")
        self.assertEqual(saved_scenario.Reward_points, 100)
    def test_scenario_str(self):
        scenario = Scenarios(
            scenario_level=1,
            scenario_title="Sample Scenario",
            Background_info="Background information for the scenario",
            Decision_options="Option 1, Option 2, Option 3",
            Reward_points=100
        )
        self.assertEqual(str(scenario), "Sample Scenario")