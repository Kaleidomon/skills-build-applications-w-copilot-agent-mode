from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import connection
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users (super heroes)
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', first_name='Steve', last_name='Rogers'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='password', first_name='Diana', last_name='Prince'),
        ]

        # Assign users to teams
        marvel.members.add(users[0], users[1])
        dc.members.add(users[2], users[3])

        # Create Activities
        Activity.objects.create(user=users[0], type='Run', duration=30, calories=300)
        Activity.objects.create(user=users[1], type='Swim', duration=45, calories=400)
        Activity.objects.create(user=users[2], type='Bike', duration=60, calories=500)
        Activity.objects.create(user=users[3], type='Yoga', duration=50, calories=200)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio workout for all levels')
        Workout.objects.create(name='Strength Training', description='Strength workout for superheroes')

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], points=1000)
        Leaderboard.objects.create(user=users[1], points=900)
        Leaderboard.objects.create(user=users[2], points=1100)
        Leaderboard.objects.create(user=users[3], points=950)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
