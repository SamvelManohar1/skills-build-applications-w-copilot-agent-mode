from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta
import logging

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        logger = logging.getLogger(__name__)

        # Create users
        users = [
            User(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(_id=ObjectId(), username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(_id=ObjectId(), username='crashoverride', email='crashoverride@mhigh.edu', password='crashoverridepassword'),
            User(_id=ObjectId(), username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        logger.info(f"Creating users: {users}")
        User.objects.bulk_create(users)
        logger.info("Users created successfully.")

        # Create teams
        team1 = Team(_id=ObjectId(), name='Blue Team')
        team2 = Team(_id=ObjectId(), name='Gold Team')
        logger.info(f"Creating teams: {team1}, {team2}")
        team1.save()
        team2.save()
        logger.info("Teams created successfully.")
        team1.members.set([users[0], users[1]])
        team2.members.set([users[2], users[3], users[4]])

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        logger.info(f"Creating activities: {activities}")
        Activity.objects.bulk_create(activities)
        logger.info("Activities created successfully.")

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
            Leaderboard(_id=ObjectId(), user=users[2], score=95),
            Leaderboard(_id=ObjectId(), user=users[3], score=85),
            Leaderboard(_id=ObjectId(), user=users[4], score=80),
        ]
        logger.info(f"Creating leaderboard entries: {leaderboard_entries}")
        Leaderboard.objects.bulk_create(leaderboard_entries)
        logger.info("Leaderboard entries created successfully.")

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        logger.info(f"Creating workouts: {workouts}")
        Workout.objects.bulk_create(workouts)
        logger.info("Workouts created successfully.")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
