import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

# Create test users
def create_users():
    users = []
    for i in range(1, 4):
        user, created = User.objects.get_or_create(username=f'user{i}', defaults={'email': f'user{i}@test.com'})
        users.append(user)
    return users

# Create test teams
def create_teams(users):
    team, _ = Team.objects.get_or_create(name='Test Team')
    team.members.set(users)
    team.save()
    return [team]

# Create test activities
def create_activities(users):
    for user in users:
        Activity.objects.get_or_create(user=user, activity_type='Running', duration=30, calories_burned=250, date='2025-12-01')

# Create test workouts
def create_workouts(users):
    workout, _ = Workout.objects.get_or_create(name='Cardio', description='Cardio workout', difficulty='Easy')
    workout.suggested_for.set(users)
    workout.save()

# Create test leaderboard
def create_leaderboard(users):
    for idx, user in enumerate(users, start=1):
        Leaderboard.objects.get_or_create(user=user, score=100-idx*10, rank=idx)

def main():
    users = create_users()
    create_teams(users)
    create_activities(users)
    create_workouts(users)
    create_leaderboard(users)
    print('Test data created successfully.')

if __name__ == '__main__':
    main()
