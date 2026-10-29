# Bug-Hunt Findings Log

Fill in one entry per bug you find, AS YOU FIND IT (before doing the AI
comparison). Write in your own words, like a detective's notebook. Show the real
path -- including things you tried that did not work.

Group: <your group name>
Members: <names>

---

## Bug 1

- **Module / function:** <e.g. cart.py -> total()>
- **What we suspected and why:** <what made you look here?>
- **What we did:** <the input or test you tried>
- **What we observed (the wrong result):** <actual output>
- **What we expected instead:** <correct behaviour>
- **The fix we made:** <what you changed>
- **Author of this finding:** <name>

---

## Bug 2

- **Module / function:** `cart.py -> checkout()`
- **What we suspected and why:** The checkout docstring says an empty cart should return `None`,
but the function appeared to copy and record the cart even when it contained no items.
- **What we did:** Created a new empty cart, called `checkout()`, and checked the order history.
- **What we observed (the wrong result):** `checkout()` returned `[]` and `history()` became
`[[]]`.
- **What we expected instead:** `checkout()` should return `None` for an empty cart and the
history should remain `[]` because no order was placed.
- **The fix we made:** Not fixed yet. The failing regression test was committed first so the
original defect is demonstrated.
- **Author of this finding:** Thet Naing Tun
---

## Bug 3

(copy the block above for each additional bug you find)
