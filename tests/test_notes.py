import unittest
from unittest.mock import *
from src.Notes import NotesStorage, NotesService, Note


class TestNotesServiceMock(unittest.TestCase):
    @patch.object(NotesStorage, 'add')
    def test_note_service_add_equal(self, mock_method):
        mock_method.return_value = 'added'
        temp = NotesService()
        self.assertEqual(temp.add(Note("wiktor", 5.5)), 'added')

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_note_service_averageOf_equal(self, mock_method):
        mock_method.return_value = [5.0, 4.5]
        temp = NotesService()
        self.assertEqual(temp.averageOf("Krzysiek"), 4.75)

    def test_note_service_averageOf_name_not_string(self):
        temp = NotesService()
        with self.assertRaisesRegex(Exception, "nazwa niepoprawna"):
            temp.averageOf(1)
    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_note_service_getAllNotesOf_empty_table(self, mock_method):
        mock_method.return_value = []
        temp = NotesService()
        with self.assertRaisesRegex(Exception, "Pusty zbiór ocen"):
            temp.averageOf("Zdzisiek")




if __name__ == "__main__":
    unittest.main()
