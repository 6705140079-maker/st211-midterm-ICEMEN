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

# =========================================================
# Aung Khant Ko - 6705140063 - 6705140063-wq
# =========================================================

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


# =========================================================
# Thet Htoo San - 6705140080 - 6705140080-thomas
# =========================================================

@pytest.mark.smoke
def test_smoke_add_item_reaches_cart():
    """Author: Thet Htoo San (6705140080-thomas). Smoke: adding a known product places it in the cart."""
    cat = Catalog()
    cat.add_product(202, "Pytest Essentials", 30)

    cart = Cart(cat)

    assert cart.add(202) is True
    assert 202 in cart.items


@pytest.mark.regression
def test_regression_login_preserves_special_characters():
    """Author: Thet Htoo San (6705140080-thomas).
    Function: Users.login().
    Wrong behaviour: special characters are removed from the supplied password.
    Correct behaviour: login must compare the exact password string.
    """
    u = Users()
    u.register("alice", "p@ss!123")

    assert u.login("alice", "p@ss!123") is True
    assert u.login("alice", "pass123") is False


# =========================================================
# Nyan Moe Aung - 6705140058 - NyanMoeAung-6705140058
# =========================================================

@pytest.mark.smoke
def test_smoke_checkout_non_empty_cart():
    """Author: Nyan Moe Aung (NyanMoeAung-6705140058). Smoke: checkout returns and records a non-empty order."""
    cat = Catalog()
    cat.add_product(303, "Clean Code", 50)

    cart = Cart(cat)
    cart.add(303)

    order = cart.checkout()

    assert order == [303]
    assert cart.items == []
    assert cart.history() == [[303]]


@pytest.mark.regression
def test_regression_search_is_case_insensitive():
    """Author: Nyan Moe Aung (NyanMoeAung-6705140058).
    Function: Catalog.search().
    Wrong behaviour: lowercase searches do not match titles containing uppercase letters.
    Correct behaviour: matching should be case-insensitive.
    """
    cat = Catalog()
    cat.add_product(1, "Python Testing", 30)

    assert cat.search("python") == [1]


@pytest.mark.regression
@pytest.mark.slow
def test_large_order_processing():
    """Author: Aung Zay Oo (6705140079-maker).

    Regression:
    This test checks two previously discovered bugs:
    1. Cart.import_products() must return the exact number of imported products.
    2. Cart.total() must include every item in the cart.

    Slow:
    This test processes 100,000 products and performs 100,000 cart additions,
    making it significantly heavier than the normal smoke tests.

    CI/CD:
    Because this test performs a large amount of work, it belongs in the
    scheduled nightly full test suite rather than the fast smoke test run
    executed on every push.
    """
    cat = Catalog()
    cart = Cart(cat)

    products = [
        (i, f"Book_{i}", 2)
        for i in range(100_000)
    ]

    imported = cart.import_products(products)

    for i in range(100_000):
        cart.add(i)

    calculated_total = cart.total()

    assert imported == 100_000
    assert calculated_total == 200_000

