"""Your test suite. Write smoke, regression, and slow tests here.

Every test MUST carry a marker (@pytest.mark.smoke / regression / slow)
and name its author in the docstring.
"""

import pytest
from bookstore_app import Users, Catalog, Cart


# =========================================================
# Aung Zay Oo - 6705140079 - 6705140079-maker
# =========================================================

@pytest.mark.smoke
def test_smoke_user_registration():
    """Author: Aung Zay Oo (6705140079-maker). Smoke: a new user can register and duplicate registration is rejected."""
    u = Users()

    assert u.register("aungzayoo", "secret123") is True
    assert "aungzayoo" in u.users
    assert u.register("aungzayoo", "secret123") is False


@pytest.mark.regression
def test_regression_cart_total_includes_all_items():
    """Author: Aung Zay Oo (6705140079-maker).
    Function: Cart.total().
    Wrong behaviour: the final item in the cart is omitted from the total.
    Correct behaviour: every item currently in the cart must be included.
    """
    cat = Catalog()
    cat.add_product(1, "Book A", 10)
    cat.add_product(2, "Book B", 20)

    cart = Cart(cat)
    cart.add(1)
    cart.add(2)

    assert cart.total() == 30


@pytest.mark.regression
def test_regression_register_rejects_empty_credentials():
    """Author: Aung Zay Oo (6705140079-maker).
    Function: Users.register().
    Wrong behaviour: an empty username or empty password is accepted.
    Correct behaviour: empty credentials should be rejected by returning False.
    """
    u = Users()

    assert u.register("", "validpass") is False
    assert u.register("validuser", "") is False


# =========================================================
# Thet Naing Tun - 6705140062 - ThetNH
# =========================================================

@pytest.mark.smoke
def test_smoke_login_validates_password():
    """Author: Thet Naing Tun (ThetNH). Smoke: login accepts the correct password and rejects an incorrect password."""
    u = Users()
    u.register("thetnaing", "pass1234")

    assert u.login("thetnaing", "pass1234") is True
    assert u.login("thetnaing", "wrongpass") is False


@pytest.mark.regression
def test_regression_checkout_empty_cart_returns_none():
    """Author: Thet Naing Tun (ThetNH).
    Function: Cart.checkout().
    Wrong behaviour: checking out an empty cart returns [] and records an empty order.
    Correct behaviour: it should return None and should not record an order.
    """
    cart = Cart(Catalog())

    assert cart.checkout() is None
    assert cart.history() == []


@pytest.mark.slow
def test_slow_bulk_import_50000_products():
    """Author: Thet Naing Tun (ThetNH). Slow: imports 50,000 products and verifies the resulting catalog."""
    cat = Catalog()
    cart = Cart(cat)

    products = [
        (i, f"Book {i}", 10)
        for i in range(50_000)
    ]

    cart.import_products(products)

    assert len(cat.products) == 50_000
    assert cat.products[49_999]["title"] == "Book 49999"


   @pytest.mark.smoke
def test_smoke_add_product_saves_to_catalog():
    """Author: Aung Khant Ko (6705140063-wq). Smoke: adding a product stores it in the catalog."""
    cat = Catalog()
    cat.add_product(101, "Software Testing Guide", 45)
    assert 101 in cat.products
    assert cat.products[101]["title"] == "Software Testing Guide"
    assert cat.search("Software") == [101]

@pytest.mark.regression
def test_regression_import_products_returns_exact_count():
    """Author: Aung Khant Ko (6705140063-wq).
    Function: Cart.import_products().
    Wrong behaviour: importing two products returns 3.
    Correct behaviour: the returned count must equal the number actually imported.
    """
    cart = Cart(Catalog())
    count = cart.import_products([
        (1, "Book 1", 10),
        (2, "Book 2", 15),
    ])
    assert count == 2

@pytest.mark.slow
def test_slow_large_catalog_search():
    """Author: Aung Khant Ko (6705140063-wq). Slow: imports a large catalog and repeatedly searches it."""
    cat = Catalog()
    cart = Cart(cat)
    products = [
        (i, f"Software Engineering Book {i}", 10)
        for i in range(30_000)
    ]
    cart.import_products(products)
    for _ in range(50):
        result = cat.search("Software Engineering Book 29999")
        assert result == [29999]