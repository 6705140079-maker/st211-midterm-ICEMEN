# REPORT.md

**Group:** ICEMEN

**Members:**
- Aung Zay Oo — 6705140079
- Thet Naing Tun — 6705140062
- Aung Khant Ko — 6705140063
- Thet Htoo San — 6705140080
- Nyan Moe Aung — 6705140058

---

## Part A -- Test Types

### 1. Smoke Testing
**Prepared by: Aung Zay Oo**

Smoke testing is a quick check that the most important functions of an application work at a basic level. It normally runs early in the testing process, such as after a new build or deployment, before running larger and more detailed test suites.

Two bookstore examples are:
1. Checking that a new user can register successfully.
2. Checking that a known product can be added to the cart.

Smoke tests should be quick and should confirm that important features are still working.

### 2. Regression Testing
**Prepared by: Thet Naing Tun**

Regression testing checks that a known bug remains fixed and that later changes have not caused the same problem to return. Regression tests are usually run after bug fixes or code changes and are also useful as part of continuous integration.

Two bookstore examples are:
1. Checking that Cart.total() includes every item in the cart after the missing-final-item bug has been fixed.
2. Checking that catalogue searching remains case-insensitive after the search bug has been fixed.

A good regression test should fail when the original bug is present and pass after the correct fix is applied.

### 3. Slow Testing
**Prepared by: Aung Khant Ko**

Slow testing checks behaviour using large amounts of data, repeated operations, or processing that takes noticeably longer than normal tests. Slow tests are usually placed in scheduled or nightly test runs because running them after every small change can make development feedback too slow.

Two bookstore examples are:
1. Importing tens of thousands of products into the catalogue and checking that all products are imported correctly.
2. Performing many repeated catalogue searches over a very large set of products.

Slow tests are useful for finding problems that may only appear when the application handles large workloads.

---

## Part B -- Scenario Classification

### Scenario 1
**Scenario:** Verify that a password-reset email is delivered within one minute.  
**Classification:** Slow  
**Prepared by: Thet Htoo San**

This is mainly a slow test because it may need to wait for an external email system and measure whether the message arrives within a time limit. Waiting for email delivery makes it much slower and less predictable than a normal smoke test.

### Scenario 2
**Scenario:** Verify that a previously fixed bug in shipping-cost calculation has not returned.  
**Classification:** Regression  
**Prepared by: Thet Naing Tun**

This is a regression test because it checks a specific problem that was already discovered and fixed. The purpose is to make sure later changes have not caused the shipping-cost bug to appear again.

### Scenario 3
**Scenario:** Verify that a nightly job can generate a sales report from ten years of orders.  
**Classification:** Slow  
**Prepared by: Aung Khant Ko**

This is a slow test because it processes a very large amount of historical data. It is suitable for a nightly test run because processing ten years of orders may take much longer than normal functional tests.

### Scenario 4
**Scenario:** Verify that the payment page loads after every deployment.  
**Classification:** Smoke  
**Prepared by: Aung Zay Oo**

This is a smoke test because it quickly checks whether an important feature of the system is available after deployment. If the payment page cannot load, deeper testing should not continue until the basic problem is fixed.

### Scenario 5
**Scenario:** Verify that a refund issued twice does not credit the customer twice — a fault reported by a customer last quarter.  
**Classification:** Regression  
**Prepared by: Nyan Moe Aung**

This is a regression test because it checks a previously reported fault. The test makes sure the old double-refund problem does not return after it has been fixed.

### Scenario 6
**Scenario:** Verify that the recommendation engine still responds when the catalogue holds one million titles.  
**Classification:** Slow  
**Prepared by: Thet Htoo San**

This is a slow test because it requires the system to work with a very large catalogue containing one million titles. The large amount of data creates a heavy workload, so this test is more suitable for a scheduled or nightly test run than for every small code change.

---

## Part F -- Team Reflection

### 1. Why is running only regression tests before every commit inefficient?
**Prepared by: Aung Zay Oo**

Running only regression tests before every commit can be inefficient because the regression suite may become large and take more time to complete. Developers need fast feedback while working, so quick smoke tests can run first to check important features while larger regression and slow suites can run later through CI.

### 2. Why do smoke tests usually run first in a CI/CD pipeline?
**Prepared by: Thet Naing Tun**

Smoke tests usually run first because they are fast and check the most important functions of the application. If a basic feature is already broken, the pipeline can detect the problem quickly instead of spending time running larger test suites first.

### 3. What risks arise if slow tests are never run?
**Prepared by: Aung Khant Ko**

If slow tests are never run, problems that only appear with large datasets or heavy workloads may remain undetected. The application may appear correct with small test data but fail when it is used with realistic or large amounts of information.

### 4. Can one test belong to two categories? Give an example.
**Prepared by: Thet Htoo San**

Yes. A test can have more than one characteristic. For example, our test_large_order_processing() test can be both a regression test and a slow test because it checks that known bulk-processing defects remain fixed while also processing a very large number of products and cart operations.

### 5. Bug-finders and bug-fixers are often different people in a real QA team. What does that separation change about how a bug report must be written?
**Prepared by: Nyan Moe Aung**

When the person finding the bug is different from the person fixing it, the bug report must be clear enough for another developer to reproduce and understand the problem without additional explanation. It should include the affected function, steps or input used, the actual wrong result, the expected result, and useful evidence so the developer can investigate and verify the fix.
