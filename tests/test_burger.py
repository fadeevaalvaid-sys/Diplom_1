
import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun_mock = Mock()

        burger.set_buns(bun_mock)

        assert burger.bun is bun_mock

    def test_add_ingredient_adds_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock()

        burger.add_ingredient(ingredient_mock)

        assert burger.ingredients == [ingredient_mock]

    @pytest.mark.parametrize(
        "remove_index, remaining_index",
        [
            (0, 1),
            (1, 0)
        ]
    )
    def test_remove_ingredient_removes_ingredient(
        self, remove_index, remaining_index
    ):
        burger = Burger()
        ingredient_mock_1 = Mock()
        ingredient_mock_2 = Mock()

        burger.add_ingredient(ingredient_mock_1)
        burger.add_ingredient(ingredient_mock_2)

        burger.remove_ingredient(remove_index)

        ingredients = [ingredient_mock_1, ingredient_mock_2]

        assert burger.ingredients == [ingredients[remaining_index]]

    def test_move_ingredient_moves_ingredient(self):
        burger = Burger()
        ingredient_mock_1 = Mock()
        ingredient_mock_2 = Mock()
        ingredient_mock_3 = Mock()

        burger.add_ingredient(ingredient_mock_1)
        burger.add_ingredient(ingredient_mock_2)
        burger.add_ingredient(ingredient_mock_3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [
            ingredient_mock_2,
            ingredient_mock_3,
            ingredient_mock_1
        ]

    def test_get_price_with_only_bun(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_price.return_value = 100

        burger.set_buns(bun_mock)

        result = burger.get_price()

        assert result == 200

    def test_get_price_returns_correct_price(self):
        burger = Burger()

        bun_mock = Mock()
        bun_mock.get_price.return_value = 100

        ingredient_mock_1 = Mock()
        ingredient_mock_1.get_price.return_value = 50

        ingredient_mock_2 = Mock()
        ingredient_mock_2.get_price.return_value = 70

        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock_1)
        burger.add_ingredient(ingredient_mock_2)

        result = burger.get_price()

        assert result == 320

    def test_get_receipt_returns_correct_receipt(self):
        burger = Burger()

        bun_mock = Mock()
        bun_mock.get_name.return_value = 'black bun'
        bun_mock.get_price.return_value = 100

        ingredient_mock = Mock()
        ingredient_mock.get_type.return_value = 'sauce'
        ingredient_mock.get_name.return_value = 'hot sauce'
        ingredient_mock.get_price.return_value = 50

        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)

        result = burger.get_receipt()

        expected_receipt = (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '(==== black bun ====)\n\n'
            'Price: 250'
        )

        assert result == expected_receipt
