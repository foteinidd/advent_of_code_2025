import unittest
import tempfile
import os
from day1 import find_password_part1, find_password_part2


class TestDay1(unittest.TestCase):
    """Test cases for Day 1: Secret Entrance"""

    def setUp(self):
        """Create a temporary file with example input"""
        self.example_input = """L68
                                L30
                                R48
                                L5
                                R60
                                L55
                                L1
                                L99
                                R14
                                L82"""

        # Create a temporary file
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
        self.temp_file.write(self.example_input)
        self.temp_file.close()

    def tearDown(self):
        """Clean up temporary file"""
        os.unlink(self.temp_file.name)

    def test_part1_example(self):
        """Test Part 1 with the provided example"""
        result = find_password_part1(self.temp_file.name)
        self.assertEqual(result, 3, "Part 1 should return 3 for the example input")

    def test_part2_example(self):
        """Test Part 2 with the provided example"""
        result = find_password_part2(self.temp_file.name)
        self.assertEqual(result, 6, "Part 2 should return 6 for the example input")

    def test_part1_single_rotation_to_zero(self):
        """Test Part 1 with a single rotation that ends at 0"""
        test_input = "R50"
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
        temp_file.write(test_input)
        temp_file.close()

        try:
            result = find_password_part1(temp_file.name)
            self.assertEqual(result, 1, "Should count 1 when dial ends at 0")
        finally:
            os.unlink(temp_file.name)

    def test_part1_no_zeros(self):
        """Test Part 1 with rotations that don't land on 0"""
        test_input = "R5\nR10"
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
        temp_file.write(test_input)
        temp_file.close()

        try:
            result = find_password_part1(temp_file.name)
            self.assertEqual(result, 0, "Should return 0 when dial never lands on 0")
        finally:
            os.unlink(temp_file.name)

    def test_part2_large_rotation_crossing_zero(self):
        """Test Part 2 with a large rotation that crosses 0 multiple times"""
        # R1000 from position 50 should cross 0 ten times
        test_input = "R1000"
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
        temp_file.write(test_input)
        temp_file.close()

        try:
            result = find_password_part2(temp_file.name)
            self.assertEqual(result, 10, "R1000 from 50 should cross 0 ten times")
        finally:
            os.unlink(temp_file.name)


if __name__ == '__main__':
    unittest.main()
