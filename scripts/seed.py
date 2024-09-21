from app.user.models import AppUser
from app.exercise.models import Exercise
from app.musclegroup.models import MuscleGroup
from app import app, db


@app.cli.command("seed")
def seed_data():
    user1 = AppUser(username='test1', email='test1@test.com')
    user2 = AppUser(username='test2', email='test2@test.com')

    users = [user1, user2]

    muscle_group_names = ["Chest", "Back", "Shoulders", "Triceps", "Biceps", "Legs"]
    muscle_groups = [MuscleGroup(id=idx + 1, name=mg_name) for idx, mg_name in enumerate(muscle_group_names)]

    exercises_array = [
        {
            'muscle_group_id': 1,
            'exercise_names': ["Bench Press", "Incline Dumbbell Press", "Chest Fly"]
        },
        {
            'muscle_group_id': 2,
            'exercise_names': ["Pull Up", "Lat Pulldown", "Barbell Row"]
        },
        {
            'muscle_group_id': 3,
            'exercise_names': ["Shoulder Press", "Lateral Raise", "Rear Delt Fly"]
        },
        {
            'muscle_group_id': 4,
            'exercise_names': ["Rope Pushdown", "Cable Overhead Triceps Extension", "Skull Crusher"]
        },
        {
            'muscle_group_id': 5,
            'exercise_names': ["Dumbbell Curl", "Hammer Curl", "Incline Dumbbell Curl"]
        },
        {
            'muscle_group_id': 6,
            'exercise_names': ["Barbell Squat", "Bulgarian Split Squat", "Leg Extension"]
        },

    ]
    all_exercises = [Exercise(name=exercise_name, muscle_group_id=exercises_dict['muscle_group_id'])
                     for exercises_dict in exercises_array
                     for exercise_name in exercises_dict['exercise_names']]

    db.session.add_all(users)
    db.session.add_all(muscle_groups)
    db.session.add_all(all_exercises)
    db.session.commit()
