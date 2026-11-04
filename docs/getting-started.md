# Getting Started

[← Back to the README](../README.md)

This walks through first-time setup after the extension is installed (see [Installing or updating the extension](../README.md#installing-or-updating-the-extension)).

## 1. Activate the game

Open **Games** in Vortex, search for **SPT** and activate it. When Vortex asks where the game is, choose your SPT folder: the one that contains `EscapeFromTarkov.exe`.

The extension then checks which SPT layout you have:

| Layout | How it is recognized |
|---|---|
| SPT 3.11 and older | `SPT.Server.exe` and `SPT.Launcher.exe` next to `EscapeFromTarkov.exe` |
| SPT 4.0 | the server and launcher inside an `SPT` folder |
| SPT 4.1 and newer | the server and launcher inside an `SPT_Runtime` folder |

If none match, you get an **"SPT Installation Not Recognized"** message and Vortex will not manage the game until the folder is corrected. See [Deployment](deployment.md#spt-layout-detection).

## 2. Set your profile's SPT Version

Open **Profiles**, edit the active SPT profile and fill in **SPT Version** (for example `4.1.6`).

This is used to:
- ask The Forge for updates that fit your SPT version,
- warn you when the profile's SPT Version and your installed SPT layout disagree (for example a profile set to `4.0.13` on an SPT 4.1 folder).

The other profile settings are optional. See [Profile Settings](profile-settings.md).

## 3. Name your mod archives (recommended)

Before installing a mod from The Forge, add its Forge ID to the archive name in a `[~M####~]` tag:

```
ExampleMod-v1.2.0 [~M1234~].7z
```

This lets the extension identify the mod without asking you, **and it is what makes dependency rules find each other**. [File Naming](file-naming.md) explains the full convention, including addons (`[~A####~]`).

## 4. Install a mod

Install the archive as usual (drag it into Vortex, or **Install From File** on the Mods page). Shortly after the install, the extension updates the mod's information by itself if it could identify the mod from its file name. If it could not, nothing happens; run **Update Mod Information** yourself (step 5).

## 5. Update Mod Information

Select one or more mods on the **Mods** page and choose **Update Mod Information** (the *i* icon). Leave "Review each mod individually" unticked to let it work through the selection by itself. See [Update Mod Information](mod-information.md).

## 6. Enable, deploy, play

Enable the mods for your profile and **Deploy**. Launch the **SPT Server** and **SPT Launcher** from the Vortex dashboard. When the server and everything you started from Vortex close, your configs are backed up to `Mod Configs` automatically (see [Tools and Configs](tools-and-configs.md)).

## 7. Check for updates

Use Vortex's **Check for updates** on the Mods page whenever you like. The extension also checks by itself 30 seconds after the game is activated, then every 8 hours. A mod with an update shows the update icon; click it to open the page where the update is. See [Update Checks](update-checks.md).
