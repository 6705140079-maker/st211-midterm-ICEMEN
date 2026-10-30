# Bug-Hunt Findings Log

Fill in one entry per bug you find, AS YOU FIND IT (before doing the AI comparison). Write in your own words, like a detective's notebook. Show the real path -- including things you tried that did not work.

**Group:** ICEMEN  
**Members:** Aung Zay Oo (6705140079), Thet Naing Tun (6705140062), Aung Khant Ko (6705140063), Thet Htoo San (6705140080), Nyan Moe Aung (6705140058)

---

## Bug 1

- **Module / function:** `cart.py -> total()`
- **What we suspected and why:** The loop in `total()` uses `range(len(self.items) - 1)`, so it looked like the final cart item would never be included.
- **What we did:** Added two products priced 10 and 20, added both products to the cart, and ran the regression test for `cart.total()`.
- **What we observed (the wrong result):** The cart total returned 10 instead of 30.
- **What we expected instead:** The total should be 30 because both products, priced 10 and 20, are currently in the cart.
- **The fix we made:** Not fixed yet. The failing regression test was committed first to demonstrate the original defect.
- **Author of this finding:** Aung Zay Oo

---

## Bug 2

- **Module / function:**
- **What we suspected and why:**
- **What we did:**
- **What we observed (the wrong result):**
- **What we expected instead:**
- **The fix we made:**
- **Author of this finding:**

---

## Bug 3

- **Module / function:**
- **What we suspected and why:**
- **What we did:**
- **What we observed (the wrong result):**
- **What we expected instead:**
- **The fix we made:**
- **Author of this finding:**

---

## Bug 4

- **Module / function:**
- **What we suspected and why:**
- **What we did:**
- **What we observed (the wrong result):**
- **What we expected instead:**
- **The fix we made:**
- **Author of this finding:**

---

## Bug 5

- **Module / function:**
- **What we suspected and why:**
- **What we did:**
- **What we observed (the wrong result):**
- **What we expected instead:**
- **The fix we made:**
- **Author of this finding:**
