import json
import os


class Notebook:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_notes(self):
        with open(self.filename, 'w') as f:
            json.dump(self.notes, f, indent=2)

    def add_note(self, title, content):
        note = {
            'id': len(self.notes) + 1,
            'title': title,
            'content': content
        }
        self.notes.append(note)
        self.save_notes()
        return note

    def list_notes(self):
        return self.notes

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note['id'] != note_id]
        self.save_notes()