import unittest
import main


class TestModules(unittest.TestCase):
    def test_00_exists(self):
        self.assertTrue(1)

    # def test_01_check_main_py(self):
    #     mars = main.SurfaceOfMars(50, 50)
    #     outcome = main.MyRover([5, 11], "N", mars)
    #     self.assertEqual(outcome, 100)
    #
    # def test_02_check_wrong_variable_type(self):
    #     mars = main.SurfaceOfMars(50, 50)
    #     outcome = main.MyRover("Woof n floof", "haha", mars)
    #     self.assertEqual(outcome, -1)
    #
    # def test_03_create_a_mars(self):
    #     mars = main.SurfaceOfMars(50, 50)
    #     mars_size = mars.confirm_mars()
    #     self.assertEqual(mars_size, (50, 50))

    def test_04_move_forward(self):
        mars = main.SurfaceOfMars(50, 50)
        outcome = main.MyRover([5, 11], "N", mars)
        outcome.move_x_axis("f")

    def test_05_move_backward(self):
        mars = main.SurfaceOfMars(50, 50)
        outcome = main.MyRover([5, 11], "N", mars)
        outcome.move_x_axis("b")

    def test_06_move_forward_twice(self):
        mars = main.SurfaceOfMars(50, 50)
        outcome = main.MyRover([5, 11], "N", mars)
        outcome.move_x_axis("f")
        outcome.move_x_axis("f")

    # def test_07_move_backward_off_map(self):
    #     mars = main.SurfaceOfMars(50, 50)
    #     outcome = main.MyRover([5, 11], "N", mars)
    #     outcome.move_x_axis("b")
    #     outcome.move_x_axis("b")
    #     outcome.move_x_axis("b")
    #     outcome.move_x_axis("b")
    #     outcome.move_x_axis("b")
    #     outcome.move_x_axis("b")
    #     outcome.move_x_axis("b")
    #     outcome.move_x_axis("b")

    def test_08_move_based_on_string_of_characters(self):
        mars = main.SurfaceOfMars(50, 50)
        outcome = main.MyRover([5, 11], "N", mars)
        outcome.move_x_axis("bbbbbbbbbbbb")