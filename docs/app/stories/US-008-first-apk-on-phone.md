# US-008 — First APK on your phone

**Status:** ready
**Depends on:** US-004
**Learner practices:** Buildozer via Docker; `buildozer.spec`; installing with adb; reading logs with logcat

## Story
As the developer, I want the desktop app running on my Android phone, so that I know
the build pipeline works before adding Android-only features.

## Why this matters
Android builds fail in ways desktop runs never do: missing requirements, permissions,
assets that weren't packaged. Finding that out with a simple app is much less painful
than finding it out with a service and notifications. You can pull this story forward
right after US-004 (ADR-004).

## Acceptance criteria
1. **Given** the project **When** you run the Buildozer Docker image to build a
   debug APK **Then** an `.apk` file appears in the project's output folder.
2. **Given** a phone with USB debugging enabled **When** you install the APK with adb
   **Then** the app icon appears and the app opens to the main screen.
3. **Given** the app on the phone **When** you start, pause, resume, and reset
   **Then** it behaves as in US-004, with a readable layout on the phone screen.
4. **Given** the app is running **When** you watch logcat filtered to Python output
   **Then** you can see your app's log messages (and Python tracebacks if it
   crashes).
5. **Given** a rebuild after a code change **When** it finishes **Then** it's
   noticeably faster than the first build, because the SDK/NDK are cached outside
   the container.
6. **Given** the steps you used **When** you're done **Then** they're written down in
   a short "how to build" note in the docs (in your own words).

## Out of scope
- Background running, notifications, alarms on Android (US-009+).
- Signing a release build or publishing.

## Mentor notes
- **Concepts to understand first:** [tech/buildozer-docker.md](../tech/buildozer-docker.md),
  [tech/android-basics-adb-logcat.md](../tech/android-basics-adb-logcat.md); what an APK is;
  what `package.name` / `package.domain` mean (they form your app's ID).
- **Approach options to consider:**
  - Run the container by typing the full `docker run` each time, or keep it in a small
    shell alias or script outside the app's source. What will you have forgotten in three weeks?
  - Pick your `package.domain` / `package.name` carefully now. They're part of the
    service class name later (US-009). Why might changing them later hurt?
- **Common pitfalls:** files you didn't commit to the spec's included extensions (e.g.
  `.kv`, sound files) silently missing from the APK; first build taking a long time
  (that's normal); Docker file ownership in the mounted folder; reading only the last
  line of a long build log.
- **Questions to ask yourself before coding:**
  - Which `requirements` does your app actually have so far?
  - When the app crashes on launch, where will you look first?

## References
- Tech guides: [tech/buildozer-docker.md](../tech/buildozer-docker.md),
  [tech/android-basics-adb-logcat.md](../tech/android-basics-adb-logcat.md)
- Related: ADR-001, ADR-004
- Official docs: https://github.com/kivy/buildozer — "Buildozer Docker image" section;
  https://developer.android.com/tools/adb — enabling USB debugging, `adb install`;
  https://developer.android.com/tools/logcat — filtering by tag.

## Definition of done
- [ ] Every acceptance criterion verified on a real phone
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
