# Tech Stack

What the app is built with, and one line on why. The details are in each linked page.

| Technology                            | Role                                   | Why                                                                                                                                                                      | Guide                                                  |
| ------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| Python 3                              | Language                               | You already know it, and Kivy 2.3.1 supports Python 3.8–3.13                                                                                                             | [kivy](tech/kivy.md)                                   |
| uv                                    | Python version + dependency management | Installs and pins a Kivy-compatible Python (3.13) separately from Arch's newer system Python, and runs tests and the app without activating a venv                       | [kivy](tech/kivy.md), [pytest](tech/pytest.md)         |
| Kivy 2.3.1                            | UI framework                           | Cross-platform Python UI that packages to Android, so you can build and test on desktop first                                                                            | [kivy](tech/kivy.md)                                   |
| Kivy JsonStore                        | Saving settings                        | Built into Kivy, stores simple key-value data in a JSON file in the app's data folder                                                                                    | [kivy](tech/kivy.md)                                   |
| pytest                                | Testing                                | The standard Python test runner; tests for the timer core run without a phone                                                                                            | [pytest](tech/pytest.md)                               |
| Buildozer (Docker image)              | Building APKs                          | Kivy's official packaging tool. The Docker image avoids installing it natively on Arch, which isn't a documented host ([ADR-001](decisions/ADR-001-buildozer-docker.md)) | [buildozer-docker](tech/buildozer-docker.md)           |
| adb + logcat                          | Installing and debugging on the phone  | Android's own tools for installing APKs and reading logs                                                                                                                 | [android-basics](tech/android-basics-adb-logcat.md)    |
| python-for-android services           | Background timer                       | The documented way to keep Python code running when the app is closed ([ADR-002](decisions/ADR-002-service-owns-timer.md))                                               | [p4a services](tech/python-for-android-services.md)    |
| oscpy                                 | App ↔ service messages                 | Small OSC library from the Kivy organization; the p4a docs suggest OSC for talking to a service                                                                          | [osc-ipc](tech/osc-ipc.md)                             |
| PyJNIus                               | Calling Android APIs                   | Needed for features Plyer doesn't cover, such as an updatable notification with action buttons                                                                           | [pyjnius](tech/pyjnius.md)                             |
| Android notification APIs             | Session notification                   | Channels, action buttons, updating in place                                                                                                                              | [android-notifications](tech/android-notifications.md) |
| Plyer (vibrator) + Android audio APIs | Alarm                                  | Plyer has a simple vibrate API; checking silent mode needs Android APIs through PyJNIus                                                                                  | [alarm](tech/android-alarm-audio-vibrate.md)           |

## Deferred (not needed yet)

- Publishing to Google Play (signing, store review of the foreground service type).
- iOS.
