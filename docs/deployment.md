# Deployment

[← Back to the README](../README.md)

What the extension does around Vortex's deployment, and why.

## SPT layout detection

SPT has moved its server files between versions, so the extension checks which layout you have:

| Layout | Server and launcher location | Server mods (`user/mods`) |
|---|---|---|
| SPT 3.11 and older | the SPT folder itself | `user/mods` |
| SPT 4.0 | `SPT/` | `SPT/user/mods` |
| SPT 4.1 and newer | `SPT_Runtime/` | `SPT_Runtime/user/mods` |

This runs when the game is activated, and again whenever you **switch profile** or **change the game folder**, so the tool shortcuts and Write Configs always use the right folders. If no layout matches, you get **"SPT Installation Not Recognized"** and Vortex stops managing the game until the folder is fixed. Check that Vortex points at the folder with `EscapeFromTarkov.exe` and that SPT is installed there.

## The SPT Version guard

Your profile's [SPT Version](profile-settings.md#spt-version) says which layout to expect. If it disagrees with the detected layout (a profile set to `4.0.13` on an SPT 4.1 folder, say), mods may be deployed to the wrong folders:

- When the game is activated: **"SPT Version Mismatch"** (a warning).
- Before every deployment: **"Deploying With SPT Version Mismatch"**. Vortex does not let an extension cancel a deployment, so the deployment still happens. Fix the profile or the folder, then deploy again.

Nothing is checked when the profile has no SPT Version.

## Empty folders

Vortex deploys files, not folders, so an empty folder in a mod's archive never reaches the game. Some mods need one (a folder they write into, for example). The installer records each mod's empty folders, and after every deployment the extension:

- **creates** the empty folders of every enabled mod that are missing,
- **removes** the folders it created earlier that are no longer wanted (their mod was disabled or removed), but **only if they are still empty**.

A **purge** removes all the folders it created (again, only empty ones). Folders that already existed are never touched. What it created is remembered per SPT folder in:

```
%APPDATA%\Vortex\eft-singleplayertushonka\Empty Folders\empty-folders.json
```

## Folder marker files

When Vortex creates a folder during deployment, it leaves a small marker file in it (`__folder_managed_by_vortex`). SPT does not need these and they clutter mod folders, so the extension removes them after each deployment. It only looks in the folders that hold deployed files.

Trade-off: without the markers, Vortex may leave the empty folders it created behind after a purge. They are harmless.
