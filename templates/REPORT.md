# REPORT.md

**Group:** ICEMEN

**Members:**
- Aung Zay Oo — 6705140079
- Thet Naing Tun — 6705140062
- Aung Khant Ko — 6705140063
- Thet Htoo San — 6705140080
- Nyan Moe Aung — 6705140058

## Part A -- Test types
For smoke, regression, and slow: define it, say when it runs, give two
bookstore-relevant examples.

Smoke testing is a quick check of the most important functions of an application to make sure the basic system is working before more detailed testing is performed. Smoke tests should be fast and should check core features.

In this bookstore project, examples of smoke tests are checking that a new user can register successfully and checking that a known product can be added to the cart.

## Part B -- Scenario classification
For each of the six scenarios: smoke / regression / slow (may be more than one)
with a 2-3 sentence justification.

Scenario: Verify that the payment page loads after every deployment.

Classification: Smoke test.

Reason: This is a smoke test because it quickly checks whether an important part of the system is working after deployment. If the payment page cannot load, there is no reason to continue with deeper testing until the basic problem is fixed.

## Part F -- Team reflection
1. Why is running only regression tests before every commit inefficient?

   Running only regression tests before every commit can be inefficient because regression test suites can become large and take more time to complete. Developers usually need quick feedback after making a change. Smoke tests can run first to quickly confirm that the most important features still work, while the larger regression and slow test suites can be run later or through CI.

2. Why do smoke tests usually run first in a CI/CD pipeline?
4. What risks arise if slow tests are never run?
5. Can one test belong to two categories? Give an example.
6. Bug-finders and bug-fixers are often different people in a real QA team.
   What does that separation change about how a bug report must be written?
