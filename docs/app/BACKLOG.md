# Backlog

Statuses: `ready`, `in-progress`, `done`, `blocked`, `superseded`. Update the status
as you work.

| ID                                                      | Title                                                 | Status      | Depends on     |
| ------------------------------------------------------- | ----------------------------------------------------- | ----------- | -------------- |
| [US-001](stories/US-001-interval-plan.md)               | Interval plan from settings                           | done        | none           |
| [US-002](stories/US-002-start-pause-reset-core.md)      | Start, pause, resume, reset in the timer core         | in-progress | US-001         |
| [US-003](stories/US-003-auto-advance-and-complete.md)   | Auto-advance and "Session complete"                   | ready       | US-002         |
| [US-004](stories/US-004-desktop-main-screen.md)         | Desktop main screen                                   | ready       | US-003         |
| [US-005](stories/US-005-settings-screen-validation.md)  | Settings screen with validation                       | ready       | US-004         |
| [US-006](stories/US-006-persist-settings.md)            | Remember settings between launches                    | ready       | US-005         |
| [US-007](stories/US-007-alarm-choice-desktop.md)        | Alarm mode choice, played on desktop                  | ready       | US-004, US-006 |
| [US-008](stories/US-008-first-apk-on-phone.md)          | First APK on your phone                               | ready       | US-004         |
| [US-009](stories/US-009-foreground-service-skeleton.md) | Foreground service skeleton + notification permission | blocked     | US-008         |
| [US-010](stories/US-010-timer-in-service-osc.md)        | Move the timer into the service, talk over OSC        | blocked     | US-009, US-003 |
| [US-011](stories/US-011-live-notification.md)           | Live Session notification                             | blocked     | US-010         |
| [US-012](stories/US-012-notification-pause-resume.md)   | Pause/Resume button in the notification               | blocked     | US-011         |
| [US-013](stories/US-013-android-alarm-ringer-mode.md)   | Android alarm that follows ringer mode                | blocked     | US-010, US-007 |
| [US-014](stories/US-014-notification-lifecycle-e2e.md)  | Notification lifecycle + end-to-end check             | blocked     | US-012, US-013 |

"Ready" means the story can be started once the stories it depends on are done. Start with US-001.
