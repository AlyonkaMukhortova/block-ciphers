import typing
import unittest

import numpy as np
from parameterized import parameterized

from ciphers import common


class TestCommon(unittest.TestCase):
    @parameterized.expand([
        [np.array([1, 2, 3, 4]), '0x1234', 4, 4],
        [np.array([1, 2, 3, 4]), '0x01020304', 4, 8]
    ])
    def test_hex_string_to_cells(self, expected: np.ndarray[int], input_string: str, ncells: int, nbits: int) -> None:
        self.assertTrue(np.all(expected == common.hex_string_to_cells(input_string, ncells, nbits)))

    @parameterized.expand([
        [0b001, 0b100, 3, 1],
        [0b100, 0b001, 3, 2],
        [0b001, 0b001, 3, 3],
        [0b_0010_1001, 0b_1001_0010, 8, 4],
        [0b_0010_1001, 0b_1001_0010, 8, 12]
    ])
    def test_rotate_left(self, expected: int, number: int, number_size_bits: int, amount: int) -> None:
        result = common.rotate_left(number, number_size_bits, amount)
        self.assertEqual(expected, result)

    @parameterized.expand([
        [0b1, 1],
        [0b_11111, 5],
        [0b_1111_1111, 8],
        [0b_1001, 4, [0, 3]],
        [0b_1100_0010, 8, [1, 6, 7]]
    ])
    def test_get_mask(self, expected: int, mask_size: int, bit_indices: typing.Union[list[int], None] = None) -> None:
        self.assertEqual(expected, common.get_mask(mask_size, bit_indices))


if __name__ == '__main__':
    unittest.main()
