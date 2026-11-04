# Troubleshooting

[← Back to the README](../README.md)

## How the extension reports things

Everything is reported at three levels, so you can stop reading as soon as you know enough:

| Level | Where | What you get |
|---|---|---|
| **Notification** | the toast in Vortex | what happened, to which mod (name, Forge ID, version) |
| **INFO / WARN / ERROR** | the Vortex log | the same message, plus what failed (for example "the second Forge request returned HTTP 500") |
| **DEBUG** | the Vortex log | every request sent and the full answer, every decision and why it was made |

Every message starts with the area it comes from, so you can search the log for it:

| Prefix | Area |
|---|---|
| `SPT Check:`, `SPT Structure Watch:` | [layout detection](deployment.md#spt-layout-detection) |
| `SPT Version Check:` | [the SPT Version guard](deployment.md#the-spt-version-guard) |
| `Installer:` | [installing mods](installing-mods.md) |
| `Mod Information:`, `Forge Cache:` | [Update Mod Information](mod-information.md) |
| `Auto Update:` | Update Mod Information running by itself after an install |
| `Forge API:`, `GitHub:`, `GitLab:`, `Codeberg:`, `Gitea:` | individual requests (DEBUG) |
| `Step 0:` … `Step 6:`, `Update Proposals:`, `Source Updates:`, `Auto Check:` | [update checks](update-checks.md) |
| `Update Page:` | the update icon |
| `Category Sync:`, `Game Activation:` | Forge categories and the checks run at game activation |
| `UI:` | the SPT columns |
| `Empty Folders:`, `Folder Markers:`, `Deploy Guard:` | [deployment](deployment.md) |
| `Write Configs:`, `Session Hook:` | [Write Configs](tools-and-configs.md#write-configs) |
| `Mod Metadata:` | the Library extension (`modinfo.json`) |

## Finding the log

The Vortex log is `vortex.log` in Vortex's folder, `%APPDATA%\Vortex`. It always includes DEBUG messages, so nothing needs turning on: reproduce the problem, then open the log (older logs are kept next to it).

When you report a problem, please attach the part of the log from just before to just after it.

## Common problems

| Problem | What to check |
|---|---|
| A dependency shows as missing, but it is installed | The dependency's archive name needs its tag (`~M1234~`, capital M). See [File Naming](file-naming.md#why-the-tag-matters-for-dependencies). |
| Update Mod Information says the Library is not available | Install the Library extension and restart Vortex ([Requirements](../README.md#requirements)). |
| Nothing happens after installing a mod | The automatic update only runs when the file name has a tag and a version. Run Update Mod Information yourself. |
| "Forge Version Not Found" | The version in Vortex (often taken from the file name) does not exist on The Forge. Correct it in the dialog. |
| No updates ever show for a mod | It needs a GUID or Forge ID and a version, or a Source Code Link and a version. Run Update Mod Information. Check the log for `Step 6: Update not shown` and its reason. |
| An update shows that you already have | The newer version must be installed as an entry with the same GUID / Forge ID / Addon ID, and for the same SPT major.minor (its Variant), to count. |
| "Rate Limit Reached" | Wait for the time in the message, or add a [token](profile-settings.md#source-host-tokens). |
| Mods deployed to the wrong place | Check the profile's SPT Version and the "SPT installation ready" line in the log; see [Deployment](deployment.md). An archive may also need [repacking](installing-mods.md#when-an-archive-needs-a-hand). |
| A tool shortcut is missing | Its program must be in the expected place; see [Tool shortcuts](tools-and-configs.md#tool-shortcuts). |
