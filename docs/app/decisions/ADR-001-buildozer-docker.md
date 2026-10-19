# ADR-001 — Build APKs with the official Buildozer Docker image

**Date:** 2026-10-12 **Status:** accepted

## Context
US-008 onward needs Android APKs. Buildozer's install docs cover Linux (with
step-by-step instructions for Ubuntu) and macOS; Windows users go through WSL. The
learner's machine runs **Arch Linux**, which the install docs don't mention.
Source: https://buildozer.readthedocs.io/en/latest/installation/

## Options considered
1. **Official Docker image `kivy/buildozer`**: documented in the Buildozer README,
   published to Docker Hub and GHCR. Mount the project folder into the container and
   run Buildozer there. Source: https://github.com/kivy/buildozer
2. **Ubuntu 24.04 in distrobox or a VM**: follow the documented Ubuntu steps exactly.
   Closest to the official guide, but more to set up.
3. **Native install on Arch**: translate the Ubuntu package list to Arch by hand.
   Not documented, so problems are hard to search for.

## Decision
Option 1, the Docker image.

## Consequences
- The Android SDK/NDK and Java stay out of the host system. Mount `~/.buildozer` as
  a cache so they download only once (this pattern is shown in the README).
- The learner has to learn basic Docker (images, containers, volume mounts).
- Joining the `docker` group gives root-level privileges. That's a known trade-off,
  see the tech guide.
- `adb` runs on the host, not in the container, to install the APK.
- Fallback: if the image causes trouble, switch to option 2.
