# Buildozer (via the official Docker image)

**Used for:** packaging the Kivy app into an Android APK (US-008 onward).
**Official docs:** https://buildozer.readthedocs.io/en/latest/ · Docker image: https://github.com/kivy/buildozer (README)   **Version covered:** `latest` docs / `kivy/buildozer:latest` image as of 2026-10-12
**Sources (fetched 2026-10-12):**
- https://buildozer.readthedocs.io/en/latest/installation/
- https://github.com/kivy/buildozer
- https://docs.docker.com/engine/install/linux-postinstall/

## What it is
**Buildozer** is Kivy's packaging tool. It reads a config file, `buildozer.spec`,
downloads the Android SDK and NDK (Google's toolkits for building Android apps),
and uses **python-for-android** to bundle Python, Kivy, and your code into an
**APK** (the file format Android installs).

**Docker** runs programs in **containers**: isolated environments with their own
files and installed tools. An **image** is the template a container starts from.
The Kivy team publishes an image with Buildozer and its dependencies already set up.

## Why we use it here
Buildozer's docs cover installing on Linux and macOS, with step-by-step instructions
for Ubuntu. Arch Linux isn't mentioned. The Docker image keeps you on the documented
path without converting Ubuntu package lists to Arch ones (ADR-001). The alternative
is an Ubuntu 24.04 container or VM that follows the documented Ubuntu steps.

## Set up
1. **Install Docker on Arch.** UNVERIFIED: the Arch Wiki Docker page couldn't be
   fetched (bot protection), so it isn't linked here. Search for the "Docker" page on
   the Arch Wiki and follow its "Installation" section (the `docker` package and starting the Docker
   service). Bring the mentor what it says.
2. **(Optional) Run Docker without sudo** (source:
   https://docs.docker.com/engine/install/linux-postinstall/):
   `sudo groupadd docker`, then `sudo usermod -aG docker $USER`, then log out and back in.
   Verify with `docker run hello-world`.
   ⚠️ Docker's docs warn: "The `docker` group grants root-level privileges to the
   user." Decide consciously. Using `sudo docker ...` is the alternative.
3. **Get the image** (source: Buildozer README, "Buildozer Docker image"):
   `docker pull kivy/buildozer:latest`
4. **Verify** (source: Buildozer README):
   ```
   docker run --interactive --tty --rm \
       --volume "$PWD":/home/user/hostcwd \
      kivy/buildozer --version
   ```
   You should see a Buildozer version.
5. **Building:** the README shows mounting `"$HOME/.buildozer"` into the container
   (so the SDK/NDK download once) and running `kivy/buildozer android debug`. Read
   that section and assemble the full command yourself. Note: the README doesn't say
   where output ends up or whether `buildozer.spec` must be in the mounted folder, so
   find out on your first build and write it down (US-008 criterion 6).
6. **Creating `buildozer.spec`:** Buildozer generates a default spec with its `init`
   command. Run it through the container the same way (UNVERIFIED in the fetched
   pages: confirm `init` in the Buildozer docs' quickstart).

## First steps to explore
1. Read the generated `buildozer.spec` top to bottom. Each option has a comment. Find
   `title`, `package.name`, `package.domain`, `source.include_exts`, `requirements`,
   `android.permissions`, and `services`.
2. Do a first build of the unchanged US-004 app. Expect it to be slow the first time.
3. Install it with adb (see [android-basics-adb-logcat.md](android-basics-adb-logcat.md)).

## Common problems
- **Python versions:** the install page says Buildozer is tested on Python 3.10+,
  and python-for-android "master" is stable up to 3.12 (develop needs 3.14). The
  Docker image handles this for you. That's one reason we use it.
- **Files missing from the APK:** check `source.include_exts` covers `.kv` and your
  sound file types.
- **File ownership** in the mounted folder after a build: check with `ls -l` (Docker
  behaviour; ask the mentor if it bites).
- **Read the whole build log**, not just the last line. The first error is usually the
  real one.

## Going deeper
- Buildozer docs: https://buildozer.readthedocs.io/en/latest/
- Buildozer repo & Docker section: https://github.com/kivy/buildozer
