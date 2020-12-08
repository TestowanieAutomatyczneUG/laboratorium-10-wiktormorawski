class Note:
    def __init__(self, name, note):
        if name == None:
            raise Exception("name ma wartość null co jest niedopuszczalne")
        if type(name) != str:
            raise Exception("name nie jest typu string")
        if type(note) != float:
            raise Exception("Note nie jest typu float")
        if name == "":
            raise Exception("wartość name nie może być pusta")
        if note < 2 or note > 6:
            raise Exception("niepoprawna wartość note, dopuszczalna to od 2.0 do 6.0")

        self.name = name
        self.note = note

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note


class NotesStorage:
    def add(self, note):
        pass

    def clear(self):
        pass

    def getAllNotesOf(self, name):
        pass


class NotesService:
    def __init__(self):
        self.storage = NotesStorage()

    def add(self, note):
        self.storage.add(note)
        return

    def averageOf(self, name):
        if type(name) != str:
            raise Exception("nazwa niepoprawna")
        notes = self.storage.getAllNotesOf(name)
        sum_of_notes = 0
        amount_of_notes = 0
        for i in notes:
            sum_of_notes += i
            amount_of_notes += 1
        return sum_of_notes/amount_of_notes

    def clear(self):
        self.storage.clear()
