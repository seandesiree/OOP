class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participant_count = 0

        def add_participant(self):
            self.participant_count += 1

        def get_participant_count(self):
            return self.participant_count


event1 = Event("Birthday Party", "2021-05-15")
event2 = Event("Conference", "2021-06-10")


event1.add_participant()
event1.add_participant()
event2.add_participant()

print("Participant count for event1:", event1.get_participant_count())
print("Participant count for event2:", event2.get_participant_count())
