from django.test import TestCase
from scenario_collection.models import ScenarioCollection
from .models import Scenarios, Answer
class ModelsTest(TestCase):
    def setUp(self):
        self.collection = ScenarioCollection.objects.create(
            name='Sample Collection',
            description='This is a sample scenario collection'
        )
        self.scenario = Scenarios.objects.create(
            scenario_level=1,
            scenario_title='Scenario 1',
            Background_info='Background info',
            Decision_options=Scenarios.RIGHT_CHOICE,
            Reward_points=10,
            scenario_collection=self.collection
        )
        self.answer1 = Answer.objects.create(
            scenario=self.scenario,
            text='Answer 1',
            is_correct=True
        )
        self.answer2 = Answer.objects.create(
            scenario=self.scenario,
            text='Answer 2',
            is_correct=False
        )
    def test_scenario_creation(self):
        self.assertEqual(self.scenario.scenario_level, 1)
        self.assertEqual(self.scenario.scenario_title, 'Scenario 1')
        self.assertEqual(self.scenario.Background_info, 'Background info')
        self.assertEqual(self.scenario.Decision_options, Scenarios.RIGHT_CHOICE)
        self.assertEqual(self.scenario.Reward_points, 10)
        self.assertEqual(self.scenario.scenario_collection, self.collection)
    def test_answer_creation(self):
        self.assertEqual(self.answer1.scenario, self.scenario)
        self.assertEqual(self.answer1.text, 'Answer 1')
        self.assertTrue(self.answer1.is_correct)
        self.assertEqual(self.answer2.scenario, self.scenario)
        self.assertEqual(self.answer2.text, 'Answer 2')
        self.assertFalse(self.answer2.is_correct)