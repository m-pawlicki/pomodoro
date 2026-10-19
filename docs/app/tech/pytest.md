# pytest

**Used for:** automated tests for the timer core (US-001–003) that run on your desktop in seconds.
**Official docs:** https://docs.pytest.org/en/stable/   **Version covered:** "stable" docs as of 2026-10-12
**Sources (fetched 2026-10-12):** https://docs.pytest.org/en/stable/getting-started.html
**uv sources (fetched 2026-10-13):** https://docs.astral.sh/uv/concepts/projects/dependencies/#development-dependencies,
https://docs.astral.sh/uv/guides/projects/#running-commands

## What it is
pytest is a test runner for Python. You write small functions that check your code
with plain `assert` statements, and pytest finds and runs them and shows you exactly
what failed.

## Why we use it here
The timer core is pure Python (no Kivy, no Android), so it can be tested without
a phone. Tests let you change the core confidently when you move it into the
service in US-010. The alternative is Python's built-in `unittest`, which works fine
but needs more boilerplate. pytest is the more common choice today.

## Set up

### With uv (this project's choice)
The project uses uv to manage Python and dependencies, so you don't create or
activate a virtualenv yourself.

1. Add pytest as a **development dependency**: `uv add --dev pytest`. It goes into
   the `dev` group under `[dependency-groups]` in `pyproject.toml`, which uv syncs by
   default (source: "Development dependencies" in
   https://docs.astral.sh/uv/concepts/projects/dependencies/#development-dependencies).
   Dev dependencies are tools for working on the app, not part of what it ships.
2. Run tests with `uv run pytest`. `uv run` checks that the environment matches the
   lockfile before running, so you don't need to activate anything (source:
   https://docs.astral.sh/uv/guides/projects/#running-commands).
3. **Verify:** `uv run pytest --version` prints a version.

### With venv + pip (for reference)
With your project's virtualenv active (source:
https://docs.pytest.org/en/stable/getting-started.html):

1. `pip install -U pytest`
2. **Verify:** `pytest --version` prints a version.

## First steps to explore
1. Read "Get Started" (link above). pytest runs files named `test_*.py` or
   `*_test.py` in the current directory and below, and runs functions whose names
   start with `test`. Test classes must start with `Test`.
2. Write one deliberately failing test and read pytest's output carefully. That
   output is what you'll be reading every day.
3. Then look up these topics in the pytest docs: **fixtures** (shared setup) and
   **parametrize** (one test, many inputs). Both are handy for US-001's N=1/2/4 cases.
4. **Check your tests catch bugs:** break your code on purpose (e.g. drop the long
   break) and confirm a test fails. If none fail, the tests aren't checking enough.

## Common problems
- **Tests not discovered:** check the file and function name prefixes (above).
- **Import errors from your package:** usually a project layout or working-directory
  issue. Ask the mentor; it's worth understanding rather than patching.
- **Tests that wait in real time:** if a test sleeps, the design probably needs a way
  to control "now" (see US-002, ADR-003).

## Going deeper
- pytest docs home: https://docs.pytest.org/en/stable/
