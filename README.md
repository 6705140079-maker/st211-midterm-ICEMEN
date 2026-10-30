# ICEMEN — Bookstore QA Midterm

Automated Software Testing (192-211)

## Group

**Group:** ICEMEN

**Members:**
- Aung Zay Oo — 6705140079
- Thet Naing Tun — 6705140062
- Aung Khant Ko — 6705140063
- Thet Htoo San — 6705140080
- Nyan Moe Aung — 6705140058

## Project Overview

This project tests and fixes an online bookstore application using Pytest. The test suite includes smoke, regression, and slow tests covering user accounts, catalogue operations, cart behaviour, checkout, bulk import, and search.

The project also includes an audit of the supplied AI-generated tests and a GitHub Actions workflow for continuous integration.

## Project Structure

```text
bookstore_app/       Application code
tests/               Smoke, regression, slow, and bonus tests
ai_review/           Supplied AI-generated tests for the Part D3 audit
worked_example/      Instructor-provided worked example
templates/           Original documentation templates
FINDINGS.md          Bug-hunt findings
REPORT.md            Test-type, scenario, and team-reflection report
AI_USAGE.md          AI usage declaration and supplied-test audit
.github/workflows/   GitHub Actions CI workflow
pytest.ini           Pytest marker configuration
requirements.txt     Python dependencies
```

## Setup

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Tests

Run the full student test suite:

```bash
python -m pytest tests/ -v
```

Run smoke tests:

```bash
python -m pytest -m smoke tests/test_bookstore.py -v
```

Run regression tests:

```bash
python -m pytest -m regression tests/test_bookstore.py -v
```

Run slow tests:

```bash
python -m pytest -m slow tests/test_bookstore.py -v --durations=0
```

## Bonus Test

The project includes `test_large_order_processing()`, which carries both the `regression` and `slow` markers. It checks previously discovered bulk-processing defects while processing a large workload and is intended for the nightly full CI test suite.
