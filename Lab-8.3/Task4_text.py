# Test cases for ShoppingCart class from Task4.py

from Task4 import ShoppingCart

def run_tests():
    cart = ShoppingCart()

    # Test 1: Add single item
    cart.add_item("apple", 1.5)
    assert cart.items == {"apple": [1.5]}, f"Test 1 Failed: {cart.items}"
    assert cart.total_cost() == 1.5, f"Test 1 Failed: {cart.total_cost()}"

    # Test 2: Add another item
    cart.add_item("banana", 2.0)
    assert cart.items == {"apple": [1.5], "banana": [2.0]}, f"Test 2 Failed: {cart.items}"
    assert cart.total_cost() == 3.5, f"Test 2 Failed: {cart.total_cost()}"

    # Test 3: Add same item again
    cart.add_item("apple", 1.0)
    assert cart.items == {"apple": [1.5, 1.0], "banana": [2.0]}, f"Test 3 Failed: {cart.items}"
    assert cart.total_cost() == 4.5, f"Test 3 Failed: {cart.total_cost()}"

    # Test 4: Remove item (should remove last added apple)
    cart.remove_item("apple")
    assert cart.items == {"apple": [1.5], "banana": [2.0]}, f"Test 4 Failed: {cart.items}"
    assert cart.total_cost() == 3.5, f"Test 4 Failed: {cart.total_cost()}"

    # Test 5: Remove item until gone
    cart.remove_item("apple")
    assert cart.items == {"banana": [2.0]}, f"Test 5 Failed: {cart.items}"
    assert cart.total_cost() == 2.0, f"Test 5 Failed: {cart.total_cost()}"

    # Test 6: Remove non-existent item (should do nothing)
    cart.remove_item("orange")
    assert cart.items == {"banana": [2.0]}, f"Test 6 Failed: {cart.items}"
    assert cart.total_cost() == 2.0, f"Test 6 Failed: {cart.total_cost()}"

    # Test 7: Add multiple of same item
    cart.add_item("banana", 2.5)
    cart.add_item("banana", 3.0)
    assert cart.items == {"banana": [2.0, 2.5, 3.0]}, f"Test 7 Failed: {cart.items}"
    assert cart.total_cost() == 7.5, f"Test 7 Failed: {cart.total_cost()}"

    # Test 8: Remove all bananas
    cart.remove_item("banana")
    cart.remove_item("banana")
    cart.remove_item("banana")
    assert cart.items == {}, f"Test 8 Failed: {cart.items}"
    assert cart.total_cost() == 0, f"Test 8 Failed: {cart.total_cost()}"

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
