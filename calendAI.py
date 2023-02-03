import collections
import random

class ActivityPlannerAgent:
    def __init__(self):
        self.activity_categories = {
            'lavoro': [9, 17],
            'colazione': [7, 9],
            'studio' : [16, 18]
            'pranzo': [12, 14],
            'cena': [18, 20],
            'allenamento': [6, 8],
            'tempo libero': [10, 22],
            'sonno': [0, 6]
        }
        self.user_preferences = collections.defaultdict(list)

    def suggest_schedule(self, activities):
        schedule = []
        for activity in activities:
            # Trova la categoria dell'attività
            activity_name, activity_duration = activity
            category = None
            for key, value in self.activity_categories.items():
                if activity_name in key:
                    category = value
                    break

            # Scegli un orario a caso all'interno della categoria per svolgere l'attività
            # o usa un orario preferito dall'utente se disponibile
            start_hour, end_hour = category
            if activity_name in self.user_preferences:
                suggested_hour = random.choice(self.user_preferences[activity_name])
            else:
                suggested_hour = random.randint(start_hour, end_hour)
            schedule.append((activity_name, suggested_hour, activity_duration))

        return schedule


    def learn_from_user(self, schedule):
        for activity, suggested_hour, activity_duration in schedule:
            user_input = input(f"Vuoi modificare l'orario per {activity}? (s/n)")
            if user_input == 's':
                new_hour = int(input("Inserisci un nuovo orario: "))
                self.user_preferences[activity].append(new_hour)
x=1
while x==1 :
    agent = ActivityPlannerAgent()
    activities = [('lavoro', 8), ('colazione', 1), ('pranzo', 2), ('cena', 2), ('allenamento', 1)]
    schedule = agent.suggest_schedule(activities)
    print("Il seguente è il piano proposto dall'agente:")
    for activity, hour, duration in schedule:
        print(f"{activity}: {hour}:00 per {duration} ore")

    agent.learn_from_user(schedule)