import collections
import random

class ActivityPlannerAgent:
    def __init__(self):
        self.activity_categories = {
            'lavoro': [9, 17],
            'colazione': [7, 9],
            'pranzo': [12, 14],
            'cena': [18, 21],
            'allenamento': [16, 17],
            'tempo libero': [10, 22],
            'sonno': [0, 6]
        }
        self.user_preferences = collections.defaultdict(list)

    def suggest_schedule(self, activities):
        schedule = []
        skipped_activities = []
        for activity, duration in activities:
            # Trova la categoria dell'attività
            category = None
            for key, value in self.activity_categories.items():
                if activity in key:
                    category = value
                    break

            # Scegli un orario a caso all'interno della categoria per svolgere l'attività
            # o usa un orario preferito dall'utente se disponibile
            start_hour, end_hour = category
            if activity in self.user_preferences:
                suggested_hour = random.choice(self.user_preferences[activity])
                # Verifica che ci sia abbastanza tempo per svolgere l'attività
                if suggested_hour + duration > end_hour:
                    skipped_activities.append(activity)
                    continue
            else:
                for i in range(len(activity)):
                    suggested_hour = random.randint(start_hour, end_hour - duration)
                    # Verifica che l'orario scelto non sia già stato utilizzato
                    if not any(
                        suggested_hour >= s and suggested_hour < s + d or suggested_hour + duration > s and suggested_hour + duration <= s + d
                        for _, s, d in schedule
                    ):
                        break
                else:
                    # Se non è possibile trovare un orario disponibile, salta l'attività
                    user_input = input(f"{activity} non può essere aggiunto al planner, vuoi modificare l'orario? (s/n)")
                    if user_input == 's':
                        new_hour = int(input("Inserisci un nuovo orario: "))
                        if new_hour + duration <= end_hour:
                            for i in range(len(activity)):
                                suggested_hour = new_hour
                                if not any(
                                        suggested_hour >= s and suggested_hour < s + d or suggested_hour + duration > s and suggested_hour + duration <= s + d
                                        for _, s, d in schedule
                                ):
                                    break
                            else:
                                skipped_activities.append(activity)
                    continue

            schedule.append((activity, suggested_hour, duration))

        return schedule, skipped_activities

    def learn_from_user(self, schedule):
        for activity, suggested_hour, activity_duration in schedule:
            user_input = input(f"Vuoi modificare l'orario per {activity}? (s/n)")
            if user_input == 's':
                new_hour = int(input("Inserisci un nuovo orario: "))
                self.user_preferences[activity].append(new_hour)

agent = ActivityPlannerAgent()
activities = [('lavoro', 8), ('colazione', 1), ('pranzo', 2), ('cena', 2), ('allenamento', 1)]

schedule, skipped_activities = agent.suggest_schedule(activities)
print("Il seguente è il piano proposto dall'agente:")
for activity, hour, duration in schedule:
    print(f"{activity}: {hour}:00 per {duration} ore")

if skipped_activities:
    print("Le seguenti attività sono state saltate:")
    for activity in skipped_activities:
        print(activity)

agent.learn_from_user(schedule)

#vedere se la modifica orario delle att saltate poi le fa inserire nel planner
