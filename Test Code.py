__author__ = 'Evan'
import Engine
import UI
import unittest


class TestEngine(unittest.TestCase):

    def setUp(self):
        self.test_engine = Engine.Engine
        self.test_engine.init()

    def test_UI_Element_List(self):
        text1 = UI.Text(self.test_engine)
        self.assertEqual(len(self.test_engine._UIElements), 1)
        self.test_engine.add_ui_element(text1)
        self.assertEqual(len(self.test_engine._UIElements), 1)
        self.test_engine.add_ui_element(text1)
        self.assertEqual(len(self.test_engine._UIElements), 1)
        self.test_engine.remove_ui_element(text1)
        self.assertEqual(len(self.test_engine._UIElements), 0)
        self.test_engine.add_ui_element(text1)
        self.assertEqual(len(self.test_engine._UIElements), 1)
        text2 = UI.Text(self.test_engine)
        text3 = UI.Text(self.test_engine)
        text4 = UI.Text(self.test_engine)
        self.assertEqual(len(self.test_engine._UIElements), 4)
        self.test_engine.remove_all_ui_elements()
        self.assertEqual(len(self.test_engine._UIElements), 0)
        self.test_engine.add_ui_element(text2)
        self.assertEqual(len(self.test_engine._UIElements), 1)
        self.test_engine.add_ui_element(text3)
        self.assertEqual(len(self.test_engine._UIElements), 2)
        self.test_engine.add_ui_element(text4)
        self.assertEqual(len(self.test_engine._UIElements), 3)
        self.test_engine.add_ui_element(text1)
        self.assertEqual(len(self.test_engine._UIElements), 4)



if __name__ == '__main__':
    unittest.main()