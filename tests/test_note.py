import unittest
from src.Notes import Note

"""
        if type(name) != str:
            raise Exception("name nie jest typu string")
        if type(note) != float:
            raise Exception("Note nie jest typu float")
        if name == None:
            raise Exception("name ma wartość null co jest niedopuszczalne")
        if name == "":
            raise Exception("wartość name nie może być pusta")
        if note < 2 or note > 6:
            raise Exception("niepoprawna wartość note, dopuszczalna to od 2.0 do 6.0")

"""


class TestNote(unittest.TestCase):
    def setUp(self):
        self.temp = Note("wiktor", 5.5)

    def test_note_getName_equal_wiktor(self):
        self.assertEqual(self.temp.get_name(), "wiktor")

    def test_note_getNote_equal_5_5(self):
        self.assertEqual(self.temp.get_note(), 5.5)

    def test_note_name_not_string_but_int(self):
        with self.assertRaisesRegex(Exception, "name nie jest typu string"):
            Note(12, 5.5)

    def test_note_name_not_string_but_float(self):
        with self.assertRaisesRegex(Exception, "name nie jest typu string"):
            Note(0.12, 2.5)

    def test_note_name_not_string_minus_int(self):
        with self.assertRaisesRegex(Exception, "name nie jest typu string"):
            Note(-1, 3)

    def test_note_name_not_string_but_list_of_two(self):
        with self.assertRaisesRegex(Exception, "name nie jest typu string"):
            Note(["wik", "tor"], 3.5)

    def test_note_name_not_string_but_dictionary_of_two(self):
        with self.assertRaisesRegex(Exception, "name nie jest typu string"):
            Note({"wik", "tor"}, 4)

    def test_note_name_not_string_but_list_of_one(self):
        with self.assertRaisesRegex(Exception, "name nie jest typu string"):
            Note(["wiktor"], 4.5)

    def test_note_name_not_string_but_dictionary_of_one(self):
        with self.assertRaisesRegex(Exception, "name nie jest typu string"):
            Note({"wiktor"}, 5.0)

    def test_note_Name_equal_None(self):
        with self.assertRaisesRegex(Exception, "name ma wartość null co jest niedopuszczalne"):
            Note(None, 5.0)

    def test_note_Name_equal_empty_string(self):
        with self.assertRaisesRegex(Exception, "wartość name nie może być pusta"):
            Note("", 5.0)

    def test_note_Note_not_float_but_int(self):
        with self.assertRaisesRegex(Exception, "Note nie jest typu float"):
            Note("wiktor", 5)

    def test_note_Note_not_float_but_minus_int(self):
        with self.assertRaisesRegex(Exception, "Note nie jest typu float"):
            Note("wiktor", -5)

    def test_note_Note_not_float_but_string(self):
        with self.assertRaisesRegex(Exception, "Note nie jest typu float"):
            Note("andrzej", '5')

    def test_note_Note_not_float_but_list(self):
        with self.assertRaisesRegex(Exception, "Note nie jest typu float"):
            Note("filip", [2])

    def test_note_Note_not_float_but_dictionary(self):
        with self.assertRaisesRegex(Exception, "Note nie jest typu float"):
            Note("Kamil Ślimak", {4})

    def test_note_Note_not_float_but_list_of_2(self):
        with self.assertRaisesRegex(Exception, "Note nie jest typu float"):
            Note("Slimak Kamil", [2, 4])

    def test_note_Note_not_float_but_dictionary_of_2(self):
        with self.assertRaisesRegex(Exception, "Note nie jest typu float"):
            Note("Kamilowy Ślimak", {4, 5})

    def test_note_Note_lower_than_2(self):
        with self.assertRaisesRegex(Exception, "niepoprawna wartość note, dopuszczalna to od 2.0 do 6.0"):
            Note("Kamil Ślimak", 1.0)

    def test_note_Note_higher_than_6(self):
        with self.assertRaisesRegex(Exception, "niepoprawna wartość note, dopuszczalna to od 2.0 do 6.0"):
            Note("Kamil Ślimak", 6.5)

    def tearDown(self):
        self.temp = None


if __name__ == "__main__":
    unittest.main()
