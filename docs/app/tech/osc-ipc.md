# OSC messaging between app and service (oscpy)

**Used for:** sending commands from the Kivy app to the Timer service and state back (US-010 onward, ADR-002).
**Official docs:** https://github.com/kivy/oscpy (README)   **Version covered:** README on GitHub as of 2026-10-12 (the latest release number couldn't be confirmed; check PyPI)
**Sources (fetched 2026-10-12):**
- https://github.com/kivy/oscpy
- https://python-for-android.readthedocs.io/en/latest/services.html

## What it is
**IPC** (inter-process communication) is how two separate programs exchange
information. Our app and service are separate processes (p4a docs), so they need it.

**OSC** (Open Sound Control) is a simple message format originally made for music
software. A message has an **address** (like `/pause`) and a list of **values**. It's
usually sent over **UDP**, a network protocol that's fast but doesn't guarantee
delivery. Here it only travels inside the phone (localhost).

**oscpy** is an OSC library from the Kivy organization. Per its README:
- `OSCThreadServer()` listens on a port in a background thread. You `bind` an address
  to a callback (or use its decorator).
- `OSCClient(address, port)` sends with `send_message(address, [values])`.
- By default addresses and strings are **bytes**. Passing `encoding='utf8'` makes
  it encode and decode strings for you.
- A server can also send and answer messages.

## Why we use it here
The p4a services docs suggest OSC as a lightweight option (Twisted as a heavier one).
oscpy is from the same organization as Kivy. The common alternative,
`python-osc`, is also fine. We chose oscpy for its fit with the Kivy ecosystem.

## Set up
1. Desktop: `pip install oscpy` (README).
2. Android: add it to `requirements` in `buildozer.spec` so it's packaged (standard
   Buildozer practice; confirm it builds in US-010).
3. **Verify (desktop):** two terminal windows: one script listening, one sending. See
   the message arrive. (Do this as a throwaway experiment outside the app's source.)

## First steps to explore
1. Read the oscpy README fully.
2. Experiment: what happens if you send when nobody is listening? (UDP: nothing, and
   no error. Remember this for US-010.)
3. Experiment with and without `encoding='utf8'`. What type does your callback receive?

## Common problems
- **Bytes vs. str** confusion (see `encoding`).
- **Port already in use.** Pick ports deliberately and handle failure.
- **Lost messages / nobody listening.** Design the protocol so the UI can always
  re-ask for the current state.
- **Blocking the UI thread** while waiting for a reply freezes the Kivy app.

## Going deeper
- oscpy repo: https://github.com/kivy/oscpy
- OSC specification (UNVERIFIED link, so search "OpenSoundControl 1.0 specification").
