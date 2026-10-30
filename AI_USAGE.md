# AI Usage Declaration and Audit

**Group:** ICEMEN  
**Members:** Aung Zay Oo (6705140079), Thet Naing Tun (6705140062), Aung Khant Ko (6705140063), Thet Htoo San (6705140080), Nyan Moe Aung (6705140058)

**Part D3 of the midterm — 20 marks.**

Before submission:

- [x] Part 1 declaration complete
- [x] All eight tests appear in the summary table with a verdict
- [x] All eight have shipped-code and fixed-code evidence
- [x] Part 3 coverage table is filled in against `FINDINGS.md`
- [x] Part 4 verdict is under 400 words
- [x] Every audit entry names the member responsible
- [x] Claims are tied to observed pytest results
- [x] File is named `AI_USAGE.md` in the repository root

---

## Part 1 — AI usage declaration

| Tool | What we used it for | Where in the project | How we checked it before relying on it |
|---|---|---|---|
| ChatGPT | Helped with test ideas, debugging, Git workflow, candidate fixes, documentation structure, bonus-test design, CI guidance, and checking the supplied AI-test audit | `tests/test_bookstore.py`, bug investigation/fixes, `FINDINGS.md`, `REPORT.md`, `AI_USAGE.md`, and CI workflow guidance | Suggestions were reviewed against the supplied project behavior and validated with pytest. Regression tests were checked against buggy behavior and the fixed application before conclusions were recorded. |

The group used AI as an assistant, not as a substitute for testing. Final claims in this file are based on observed pytest behavior.

---

## Part 2 — Audit of the supplied test set

The supplied file in this repository is `ai_review/test_ai_generated.py` and contains eight tests. We compared the same tests against the shipped buggy behavior and the final fixed application.

### Classification rules

| Shipped Code | Fixed Code | Verdict |
|---|---|---|
| FAIL | PASS | **Genuine detection** |
| PASS | PASS | **Detects nothing** |
| PASS | FAIL | **Locks in the bug** |
| FAIL | FAIL | **Invented requirement** |

### Summary table

| # | Test | What it claims to catch | Shipped | Fixed | Verdict | Auditor |
|---|---|---|---|---|---|---|
| 1 | `test_cart_total_sums_items` | Incorrect cart total | FAIL | PASS | **Genuine detection** | Aung Zay Oo |
| 2 | `test_login_rejects_wrong_password` | Wrong password is accepted | PASS | PASS | **Detects nothing** | Aung Zay Oo |
| 3 | `test_search_finds_exact_title` | Search cannot find a product | PASS | PASS | **Detects nothing** | Thet Naing Tun |
| 4 | `test_import_returns_count` | Bulk import returns the wrong count | FAIL | PASS | **Genuine detection** | Thet Naing Tun |
| 5 | `test_register_duplicate_returns_false` | Duplicate registration is accepted | PASS | PASS | **Detects nothing** | Aung Khant Ko |
| 6 | `test_checkout_empty_returns_none` | Empty checkout returns the wrong value | FAIL | PASS | **Genuine detection** | Aung Khant Ko |
| 7 | `test_add_to_cart_returns_true_for_known_product` | A known product cannot be added to the cart | PASS | PASS | **Detects nothing** | Thet Htoo San |
| 8 | `test_search_is_limited_to_ten_results` | Search should return at most ten results | FAIL | FAIL | **Invented requirement** | Nyan Moe Aung |

### Evidence runs

For the shipped state, the full supplied set produced these observed results:

```text
$ python -m pytest ai_review/test_ai_generated.py -v
ai_review/test_ai_generated.py::test_cart_total_sums_items FAILED
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED
ai_review/test_ai_generated.py::test_import_returns_count FAILED
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED
ai_review/test_ai_generated.py::test_checkout_empty_returns_none FAILED
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED
========================= 4 failed, 4 passed ==========================
```

Relevant shipped-state failure evidence:

```text
test_cart_total_sums_items:
E       assert 10 == 30

test_import_returns_count:
E       AssertionError: assert 3 == 2

test_checkout_empty_returns_none:
E       assert [] is None

test_search_is_limited_to_ten_results:
E       AssertionError: assert 20 <= 10
```

For the final fixed state, the full supplied set produced these observed results:

```text
$ python -m pytest ai_review/test_ai_generated.py -v
ai_review/test_ai_generated.py::test_cart_total_sums_items PASSED
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED
ai_review/test_ai_generated.py::test_import_returns_count PASSED
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED
ai_review/test_ai_generated.py::test_checkout_empty_returns_none PASSED
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED
========================= 1 failed, 7 passed ==========================
```

Relevant fixed-state failure evidence:

```text
test_search_is_limited_to_ten_results:
E       AssertionError: assert 20 <= 10
```

---

### Test 1 — `test_cart_total_sums_items` (`ai_review/test_ai_generated.py:12`)

**Audited by:** Aung Zay Oo

**1. What it claims to catch:** It claims that `Cart.total()` should sum the prices of every item currently in the cart.

**2. Evidence — shipped code**

```text
ai_review/test_ai_generated.py::test_cart_total_sums_items FAILED
E       assert 10 == 30
```

**3. Evidence — fixed code**

```text
ai_review/test_ai_generated.py::test_cart_total_sums_items PASSED
```

**4. What the pair proves:** This is a **genuine detection**. It fails when the shipped `Cart.total()` omits the final item and passes after `total()` is fixed to include every item.

**5. Verdict:** [x] Genuine detection — FAIL then PASS

---

### Test 2 — `test_login_rejects_wrong_password` (`ai_review/test_ai_generated.py:19`)

**Audited by:** Aung Zay Oo

**1. What it claims to catch:** It checks that login rejects an ordinary incorrect password.

**2. Evidence — shipped code**

```text
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED
```

**3. Evidence — fixed code**

```text
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED
```

**4. What the pair proves:** This test **detects nothing** about the planted login bug. The shipped login bug concerns special-character handling, but this test only uses simple alphanumeric passwords. A useful test for that defect must register a password such as `p@ss!123` and verify that the exact password works while the cleaned version does not.

**5. Verdict:** [x] Detects nothing — PASS then PASS

---

### Test 3 — `test_search_finds_exact_title` (`ai_review/test_ai_generated.py:25`)

**Audited by:** Thet Naing Tun

**1. What it claims to catch:** It checks that catalog search can find a product by its title.

**2. Evidence — shipped code**

```text
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED
```

**3. Evidence — fixed code**

```text
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED
```

**4. What the pair proves:** This test **detects nothing** about the case-sensitivity defect because it searches for `Python Testing` with exactly the same capitalization as the stored title. To expose the bug it would need to search with a different case, for example `python`.

**5. Verdict:** [x] Detects nothing — PASS then PASS

---

### Test 4 — `test_import_returns_count` (`ai_review/test_ai_generated.py:31`)

**Audited by:** Thet Naing Tun

**1. What it claims to catch:** It checks that `import_products()` returns the exact number of products imported.

**2. Evidence — shipped code**

```text
ai_review/test_ai_generated.py::test_import_returns_count FAILED
E       AssertionError: assert 3 == 2
```

**3. Evidence — fixed code**

```text
ai_review/test_ai_generated.py::test_import_returns_count PASSED
```

**4. What the pair proves:** This is a **genuine detection**. The shipped implementation incorrectly returned `count + 1`, and the test passed once the method returned the true count.

**5. Verdict:** [x] Genuine detection — FAIL then PASS

---

### Test 5 — `test_register_duplicate_returns_false` (`ai_review/test_ai_generated.py:37`)

**Audited by:** Aung Khant Ko

**1. What it claims to catch:** It checks that an already-used username cannot be registered again.

**2. Evidence — shipped code**

```text
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED
```

**3. Evidence — fixed code**

```text
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED
```

**4. What the pair proves:** This test **detects nothing** about the planted registration bug. Duplicate rejection already worked in the shipped code; the actual defect was that empty usernames or passwords were accepted. The test would need empty credentials to detect that bug.

**5. Verdict:** [x] Detects nothing — PASS then PASS

---

### Test 6 — `test_checkout_empty_returns_none` (`ai_review/test_ai_generated.py:43`)

**Audited by:** Aung Khant Ko

**1. What it claims to catch:** It checks that checking out an empty cart returns `None`.

**2. Evidence — shipped code**

```text
ai_review/test_ai_generated.py::test_checkout_empty_returns_none FAILED
E       assert [] is None
```

**3. Evidence — fixed code**

```text
ai_review/test_ai_generated.py::test_checkout_empty_returns_none PASSED
```

**4. What the pair proves:** This is a **genuine detection**. The shipped implementation returned an empty list and recorded an empty order, while the corrected implementation returns `None` without creating an order.

**5. Verdict:** [x] Genuine detection — FAIL then PASS

---

### Test 7 — `test_add_to_cart_returns_true_for_known_product` (`ai_review/test_ai_generated.py:48`)

**Audited by:** Thet Htoo San

**1. What it claims to catch:** It checks that adding a product that exists in the catalog succeeds.

**2. Evidence — shipped code**

```text
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED
```

**3. Evidence — fixed code**

```text
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED
```

**4. What the pair proves:** This test **detects nothing** about any planted defect because `Cart.add()` already behaved correctly in the shipped application. It is a reasonable smoke-style check, but it is not evidence of a planted bug.

**5. Verdict:** [x] Detects nothing — PASS then PASS

---

### Test 8 — `test_search_is_limited_to_ten_results` (`ai_review/test_ai_generated.py:55`)

**Audited by:** Nyan Moe Aung

**1. What it claims to catch:** It assumes catalog search should return no more than ten matching results.

**2. Evidence — shipped code**

```text
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED
E       AssertionError: assert 20 <= 10
```

**3. Evidence — fixed code**

```text
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED
E       AssertionError: assert 20 <= 10
```

**4. What the pair proves:** This is an **invented requirement**. Neither the catalog API nor the project requirements define a ten-result limit. The search method is intended to return the matching product IDs, so returning all 20 matching products is valid.

**5. Verdict:** [x] Invented requirement — FAIL then FAIL

---

## Part 3 — Coverage against our own bug hunt

| Bug (our description) | We found it | The supplied set catches it | Which test, and how we established that |
|---|---|---|---|
| `Cart.total()` omits the final cart item | Yes | Yes | `test_cart_total_sums_items` failed on shipped code with `10 != 30` and passed after the fix. |
| `Cart.checkout()` accepts an empty cart and records an empty order | Yes | Yes | `test_checkout_empty_returns_none` failed with `[] is None` and passed after the empty-cart fix. |
| `Cart.import_products()` returns one too many | Yes | Yes | `test_import_returns_count` failed with `3 != 2` and passed after returning `count`. |
| `Users.login()` mishandles passwords containing special characters | Yes | No | `test_login_rejects_wrong_password` passed in both states because it never uses a password containing symbols. |
| `Catalog.search()` is case-sensitive | Yes | No | `test_search_finds_exact_title` passed in both states because it uses identical capitalization instead of testing different case. |

The separate empty-credentials registration defect was also found by our regression suite, but it was not added as a sixth `FINDINGS.md` entry because the assignment limits `FINDINGS.md` to five entries. The supplied AI set does not detect that defect either; its registration test only checks duplicate usernames.

---

## Part 4 — Verdict

The most common failure mode in the supplied AI-generated set was **detects nothing**, which occurred in **4 of the 8 tests**. Three tests were genuine detections: cart total, bulk-import count, and empty checkout. One test invented a requirement by assuming catalog search must be limited to ten results.

A test that passes against buggy code can be more dangerous than a test that crashes because a passing test creates false confidence. In this project, the wrong-password, exact-title search, duplicate-registration, and add-to-cart tests all passed on the shipped application even though planted bugs still existed elsewhere in the same areas. A crashing or failing test attracts attention, while a weak passing test can make the team believe the relevant behavior has already been validated.

The supplied set did not reveal a planted defect that our own bug hunt had missed. Instead, our regression tests covered additional cases that the supplied set failed to exercise, especially empty registration credentials, special-character passwords, and case-insensitive search.

Before trusting a generated test in future, we will run it against both the known-buggy and fixed versions, inspect the exact assertion and input data, confirm that the asserted behavior exists in the requirements or API behavior, and check whether the test actually exercises the edge case associated with the suspected defect. This audit showed that a plausible test name is not enough; observed before/after behavior is the evidence that matters.

---

## Appendix

ChatGPT was used as declared in Part 1. The group reviewed the generated suggestions and relied on pytest results and the project requirements before accepting conclusions.
