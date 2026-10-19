# ADR-004 — Build desktop-first, then Android

**Date:** 2026-10-12 **Status:** accepted

## Context
The learner is new to both Kivy and Android and has a few hours a week. Building an
APK and installing it on a phone is slow compared with running `python main.py` on
the desktop. Kivy is cross-platform.
Source: https://kivy.org/doc/stable/gettingstarted/installation.html

## Options considered
1. **Desktop first:** pure-Python timer core with pytest (US-001–003), then the Kivy
   UI, settings, and alarm on desktop (US-004–007), then the first APK (US-008),
   then the Android-only parts (US-009–014).
2. **Android hello-world first:** get a blank APK onto the phone before any logic,
   so build problems surface on day one.

## Decision
Option 1, with one adjustment: US-008 (first APK) depends only on US-004. It can be
pulled forward right after the main screen works, so build problems still show up
early.

## Consequences
- Fast feedback while learning Kivy basics; one new concept per story.
- Android-specific problems (permissions, services) come later, but the logic is
  already tested by then, so they're easier to tell apart.
- The core must stay free of Kivy/Android imports so it runs in pytest and later
  inside the service (ADR-002).
