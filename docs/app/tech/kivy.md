# Kivy

**Used for:** the app's user interface (main screen, settings), timing the display refresh, loading sounds, and saving settings.
**Official docs:** https://kivy.org/doc/stable/   **Version covered:** 2.3.1 (per the installation page)
**Sources (fetched 2026-10-12):**
- https://kivy.org/doc/stable/gettingstarted/installation.html
- https://kivy.org/doc/stable/guide/basic.html
- https://kivy.org/doc/stable/guide/lang.html
- https://kivy.org/doc/stable/api-kivy.clock.html
- https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html
- https://kivy.org/doc/stable/api-kivy.storage.html
- https://kivy.org/doc/stable/api-kivy.app.html
- https://kivy.org/doc/stable/api-kivy.core.audio.html
**uv sources (fetched 2026-10-13):**
- https://docs.astral.sh/uv/guides/install-python/
- https://docs.astral.sh/uv/concepts/python-versions/#python-version-files
- https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-specifiers

## What it is
Kivy is a Python framework for building apps with touch-friendly user interfaces. The
same Python code runs on desktop (Linux, Windows, macOS) and can be packaged for
Android. You describe the screen as a tree of **widgets** (buttons, labels, layouts),
and Kivy draws them and passes you events like "button pressed".

## Why we use it here
You already know Python, and Kivy lets you build and test on your desktop before
touching Android (ADR-004). The usual alternative for Android is Kotlin with Android
Studio. It's better supported on Android, but you'd be learning a new language and a
new UI system at the same time.

## Set up
Prerequisite: Python 3.8–3.13 ("Kivy 2.3.1 officially supports Python versions
3.8 - 3.13"). Check with `python --version`.

### With uv (this project's choice)
Arch's system Python (3.14 at the time of writing) is newer than Kivy supports.
uv can provide a separate Python for this project without touching the system one.

1. Install a supported Python: `uv python install 3.13` (source:
   "Installing a specific version" in https://docs.astral.sh/uv/guides/install-python/).
2. Pin the project to it: `uv python pin 3.13` writes a `.python-version` file that uv
   uses as the project's default Python (source:
   https://docs.astral.sh/uv/concepts/python-versions/#python-version-files).
   Check the file is there and says 3.13.
3. Add Kivy with the `base` extra: `uv add "kivy[base]"`. The square brackets are the
   standard extras syntax (source: "Dependency specifiers" in
   https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-specifiers).
   The uv page doesn't show `uv add` with an extra directly, so if this fails, read
   the error and check `uv add --help`. `kivy_examples` is optional; add it the same
   way if you want the demo apps.

**Verify:** `uv run python --version` shows 3.13.x, and
`uv run python -c "import kivy; print(kivy.__version__)"` prints a version number.

### With venv + pip (for reference)
These steps come from the installation
page (source: https://kivy.org/doc/stable/gettingstarted/installation.html):

1. Upgrade the packaging tools:
   `python -m pip install --upgrade pip setuptools virtualenv`
2. Create a virtual environment in your project folder:
   `python -m venv kivy_venv`
3. Activate it (Linux): `source kivy_venv/bin/activate`
4. Install Kivy: `python -m pip install "kivy[base]" kivy_examples`

**Verify:** with the venv active, `python -c "import kivy; print(kivy.__version__)"`
should print a version number. (This check isn't from the docs; it's a plain Python
import.)

Arch note: Arch's system Python may be newer than 3.13. If `pip install` fails, check
`python --version` against the supported range above first. (This is the main reason
the project uses uv; see the uv steps above.)

## First steps to explore
1. **Create an application** (https://kivy.org/doc/stable/guide/basic.html): subclass
   `App`, have `build()` return a root widget, call `run()`. Try the Hello World there.
2. **KV language** (https://kivy.org/doc/stable/guide/lang.html): lays out the widget
   tree declaratively, separate from logic. A `.kv` file named after your App class
   (minus "App", lowercased) loads automatically. Learn what `root`, `app`, and
   `self` refer to.
3. **Properties**: Kivy properties update the UI automatically when they change.
   Find "Properties" in the Kivy programming guide.
4. **Clock** (https://kivy.org/doc/stable/api-kivy.clock.html):
   `Clock.schedule_interval(callback, timeout)` runs a callback repeatedly. The docs
   say timing is approximate: callbacks can come early or late, which is why we use
   an End time (ADR-003).
5. **ScreenManager** (https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html):
   holds several `Screen`s, each with a unique `name`. Setting `current` to a name
   switches to that screen.
6. **Storage** (https://kivy.org/doc/stable/api-kivy.storage.html): `JsonStore`
   keeps key-value data in a JSON file.
7. **App.user_data_dir** (https://kivy.org/doc/stable/api-kivy.app.html): a
   directory your app may write to. On Android it's the app's private files
   directory. Also read the `on_pause` warning: after `on_pause`, `on_resume` may
   never be called, so save important data early.
8. **Audio** (https://kivy.org/doc/stable/api-kivy.core.audio.html):
   `SoundLoader.load()` returns a `Sound` with `play()` and `stop()`. The page doesn't
   list supported formats, so test your files.

Try: the `kivy_examples` package you installed contains demo apps. Run a few and
read their source.

## Common problems
- **Logic creeping into KV files.** Keep KV for layout and simple bindings.
- **Relative file paths** that work from your terminal but not when packaged. Build
  paths from a known base.
- **Expecting Clock to be exact.** It isn't (Clock docs).

## Going deeper
- Kivy programming guide: https://kivy.org/doc/stable/ (Programming Guide section)
- API reference: open the docs home above and go to "API Reference" (the index URL
  wasn't fetched, so it isn't linked here).
