# Bug-Hunt Findings Log

Fill in one entry per bug you find, AS YOU FIND IT (before doing the AI comparison). Write in your own words, like a detective's notebook. Show the real path -- including things you tried that did not work.

**Group:** ICEMEN  
**Members:** Aung Zay Oo (6705140079), Thet Naing Tun (6705140062), Aung Khant Ko (6705140063), Thet Htoo San (6705140080), Nyan Moe Aung (6705140058)

---

## Bug 1

- **Module / function:** cart.py -> total()
- **What we suspected and why:** The loop in total() uses `range(len(self.items) - 1)`, so it looked like the final cart item would never be included.
- **What we did:** Added two products priced 10 and 20, added both products to the cart, and ran the regression test for `cart.total()`.
- **What we observed (the wrong result):** The cart total returned 10 instead of 30.
- **What we expected instead:** The total should be 30 because both products, priced 10 and 20, are currently in the cart.
- **The fix we made:** Changed `Cart.total()` so it iterates through every item in the cart instead of stopping before the final item. After the fix, the regression test passed and returned the expected total of 30.
- **Author of this finding:** Aung Zay Oo

---

## Bug 2

- **Module / function:** cart.py -> checkout()
- **What we suspected and why:** The checkout docstring says an empty cart should return `None`, but the function appeared to copy and record the cart even when it contained no items.
- **What we did:** Created a new empty cart, called `checkout()`, and checked the order history.
- **What we observed (the wrong result):** checkout() returned `[]` and history() became `[[]]`.
- **What we expected instead:** checkout() should return None for an empty cart and the history should remain `[]` because no order was placed.
- **The fix we made:** Not fixed yet. The failing regression test was committed first so the original defect is demonstrated.
- **Author of this finding:** Thet Naing Tun

---

## Bug 3

- **Module / function:** `cart.py -> import_products()`
- **What we suspected and why:** The method counts each imported product, but the return statement adds one extra to the total.
- **What we did:** Imported two products and checked the value returned by `import_products()`.
- **What we observed (the wrong result):** The function returned 3 after importing only 2 products.
- **What we expected instead:** It should return 2 because exactly two products were imported.
- **The fix we made:** Not fixed yet. The failing regression test was committed first to demonstrate the original defect.
- **Author of this finding:** Aung Khant Ko

---

## Bug 4

- **Module / function:** users.py -> login()
- **What we suspected and why:** login() removes special characters from the password before comparing it with the stored password, so valid passwords containing symbols may not work correctly.
- **What we did:** Registered a user with the password p@ss!123 and then attempted to log in using that exact password.
- **What we observed (the wrong result):** Login returned False even though the exact registered password was supplied.
- **What we expected instead:** Login should return True when the supplied password exactly matches the stored password, including special characters.
- **The fix we made:** Not fixed yet. The failing regression test was committed first to demonstrate the original defect.
- **Author of this finding:** Thet Htoo San

---

## Bug 5

- **Module / function:** catalog.py -> search()
- **What we suspected and why:** search() compares the keyword directly with the product title, so the comparison appears to be case-sensitive.
- **What we did:** Added a product titled Python Testing and searched using the lowercase keyword `python`.
- **What we observed (the wrong result):** The search returned an empty list `[]`.
- **What we expected instead:** The search should return [1] because python should match Python Testing regardless of letter case.
- **The fix we made:** Not fixed yet. The failing regression test was committed first to demonstrate the original defect.
- **Author of this finding:** Nyan Moe Aung
