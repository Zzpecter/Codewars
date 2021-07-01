class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.set_persons = []
        self.actual_count = 0

    def how_many(self, new_persons):
        print(new_persons)
        for person in new_persons:
            self.set_persons.append(person.lower())
        print(self.set_persons)
        self.set_persons = list(set(self.set_persons))
        print(self.set_persons)

        new_ones = len(self.set_persons) - self.actual_count
        self.actual_count = len(self.set_persons)

        return new_ones
