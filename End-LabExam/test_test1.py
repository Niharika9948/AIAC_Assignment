import unittest
import random
from test1 import (
    insertion_sort,
    ai_merge_sort,
    ai_quick_sort,
    choose_and_sort,
    fastest_driver
)

class TestSorting(unittest.TestCase):

    # -----------------------------
    # 1) Basic insertion sort test
    # -----------------------------
    def test_insertion_sort(self):
        print("\nTest 1: Insertion Sort")
        data = [41.14, 96.6, 199.31, 147.31, 190.45, 140.13, 64.48, 177.94, 8.59, 167.06, 167.67, 160.32]
        print("Original ETAs:", data)
        sorted_list = insertion_sort(data)
        print("Sorted ETAs:", sorted_list)
        print("Fastest Driver ETA:", fastest_driver(sorted_list))

    # --------------------------------------------
    # 2) Merge sort and Quick sort correctness
    # --------------------------------------------
    def test_merge_and_quick_sort(self):
        print("\nTest 2: Merge & Quick Sort")
        data = [20, 7, 15, 2, 30, 11]
        print("Original ETAs:", data)
        sorted_merge = ai_merge_sort(data)
        print("Merge Sorted ETAs:", sorted_merge)
        print("Fastest Driver ETA (Merge):", fastest_driver(sorted_merge))

        sorted_quick = ai_quick_sort(data)
        print("Quick Sorted ETAs:", sorted_quick)
        print("Fastest Driver ETA (Quick):", fastest_driver(sorted_quick))

    # -----------------------------
    # 3) Fastest driver test
    # -----------------------------
    def test_fastest_driver(self):
        print("\nTest 3: Fastest Driver")
        data = [25.5, 31.1, 57.7, 90.0]
        print("Original ETAs:", data)
        sorted_list = choose_and_sort(data)
        print("Sorted ETAs:", sorted_list)
        print("Fastest Driver ETA:", fastest_driver(sorted_list))

    # -------------------------------------
    # 4) Test duplicates handling correctly
    # -------------------------------------
    def test_duplicates(self):
        print("\nTest 4: Duplicates Handling")
        data = [5, 1, 5, 3, 1]
        print("Original ETAs:", data)
        sorted_list = choose_and_sort(data)
        print("Sorted ETAs:", sorted_list)
        print("Fastest Driver ETA:", fastest_driver(sorted_list))

    # ----------------------------------------
    # 5) Test reverse-sorted input (worst case)
    # ----------------------------------------
    def test_reverse_sorted(self):
        print("\nTest 5: Reverse Sorted")
        data = [9, 7, 5, 3, 1]
        print("Original ETAs:", data)
        sorted_list = choose_and_sort(data)
        print("Sorted ETAs:", sorted_list)
        print("Fastest Driver ETA:", fastest_driver(sorted_list))

    # --------------------------------------------------
    # 6) Test choose_and_sort to ensure correct method
    # --------------------------------------------------
    def test_choose_and_sort(self):
        print("\nTest 6: Choose and Sort")
        data = [4, 2, 7, 1, 9]
        print("Original ETAs:", data)
        sorted_list = choose_and_sort(data)
        print("Sorted ETAs:", sorted_list)
        print("Fastest Driver ETA:", fastest_driver(sorted_list))

    # -----------------------------------------------------
    # 7) Empty list edge case (sorting + fastest_driver)
    # -----------------------------------------------------
    def test_empty_list(self):
        print("\nTest 7: Empty List")
        data = []
        print("Original ETAs:", data)
        sorted_list = choose_and_sort(data)
        print("Sorted ETAs:", sorted_list)
        try:
            fastest_driver(sorted_list)
        except Exception as e:
            print("Fastest Driver ETA: Error -", e)

    # -----------------------------------------------------
    # 8) Large random list for stress testing correctness
    # -----------------------------------------------------
    def test_large_random_list(self):
        print("\nTest 8: Large Random List")
        random.seed(10)
        data = [round(random.randint(1, 200) + random.randint(0, 99)/100, 2) for _ in range(12)]
        print("Original ETAs:", data)
        sorted_list = choose_and_sort(data)
        print("Sorted ETAs:", sorted_list)
        print("Fastest Driver ETA:", fastest_driver(sorted_list))


if __name__ == "__main__":
    unittest.main()
