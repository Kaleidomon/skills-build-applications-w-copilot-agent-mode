from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.team.members.add(self.user)
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=30, calories=300)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100)

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertIn(self.user, self.team.members.all())

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Run')
        self.assertEqual(self.activity.calories, 300)

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 100)
