# EFT - Single Player Tushonka (SPT) Vortex Extension

A game extension for [Vortex](https://www.nexusmods.com/about/vortex/), the mod manager by Nexus Mods, that lets you manage your **Single Player Tarkov (SPT)** mods: install, enable and disable, deploy, keep dependencies in order, and check for updates. Mod information and updates come from [The Forge](https://forge.sp-tarkov.com) and from each mod's source code repository.

> This page assumes you already know the basics of Vortex (profiles, deploying, the Mods page). If you would like a beginner's guide to Vortex itself, let me know.

---

## What it does

| Feature | In short | Details |
|---|---|---|
| **SPT-aware installer** | Detects your SPT folder layout (3.11, 4.0 or 4.1+), strips extra wrapper folders from archives, drops readme/license files and keeps empty folders a mod needs. | [Installing Mods](docs/installing-mods.md) |
| **Update Mod Information** | One click fills in a mod's name, author, picture, category, description, Fika compatibility and dependency rules from The Forge, then from its GitHub, GitLab, Codeberg or Gitea repository. | [Update Mod Information](docs/mod-information.md) |
| **Update checks** | Vortex's "Check for updates" asks The Forge and the mod's source repository for newer versions. It also runs by itself when the game is activated and every 8 hours. | [Update Checks](docs/update-checks.md) |
| **Dependencies built for you** | "Requires", "load after" and Fika "conflicts" rules are created from The Forge's data. | [File Naming](docs/file-naming.md) |
| **Tool shortcuts** | SPT Server, SPT Launcher, Server Value Modifier, Fika Installer and Give-UI in the Vortex dashboard. | [Tools and Configs](docs/tools-and-configs.md) |
| **Config backups** | "Write Configs" copies your BepInEx, SPT settings and mod configs into a timestamped folder; it also runs by itself when your SPT session ends. | [Tools and Configs](docs/tools-and-configs.md) |
| **SPT columns** | Forge ID, GUID, Addon ID, Fika Compatibility, Source Code Link and more on the Mods page. | [Mod Columns](docs/mod-columns.md) |

---

## Requirements

- **Vortex** (a current release).
- **SPT** installed with one of the supported layouts: SPT 3.11, SPT 4.0, or SPT 4.1 and newer.
- **Vortex Library - Cobet's Utilities** (a second extension). It reads and writes each mod's `modinfo.json` and adds the Rules List editor. *Update Mod Information needs it*; everything else works without it. <!-- TODO: add the download link for the Library extension -->

---

## Installing or updating the extension

1. Download the extension `.zip` from the [Releases](../../releases) page, and the Library extension (see Requirements).
2. In Vortex, open **Extensions**.<br/>
   <img width="238" alt="Extensions in the Vortex sidebar" src="https://github.com/user-attachments/assets/1415c11c-7e1a-411f-a295-4d017e8e7b37" />
3. Use the button in the bottom right to install the extension from the `.zip` file. Do the same for the Library extension.<br/>
   <img width="900" alt="Install extension from file" src="https://github.com/user-attachments/assets/f973fea5-ee8e-45d0-a0e7-357024a621ae" />
4. Restart Vortex and search the Extensions list to confirm both are installed. If one is missing, install it again and restart.<br/>
   <img width="612" alt="Extension shown in the list" src="https://github.com/user-attachments/assets/193c7021-bb59-4ee2-8862-dfe9097e0e09" />
5. Open **Games**, search for **SPT**, and activate it. Point Vortex at your SPT folder (the folder with `EscapeFromTarkov.exe`).<br/>
   <img width="259" alt="Games in the Vortex sidebar" src="https://github.com/user-attachments/assets/f871b75a-c84b-4b9c-9788-c9c68a31dc0b" />

Then follow [Getting Started](docs/getting-started.md): set your profile's **SPT Version** and install your first mod.

---

## Documentation

**Using the extension**
- [Getting Started](docs/getting-started.md): first-time setup, step by step
- [File Naming](docs/file-naming.md): the `[~M1234~]` tags, and why they matter for dependencies
- [Installing Mods](docs/installing-mods.md): what the installer does with an archive
- [Update Mod Information](docs/mod-information.md): filling in mod details from The Forge and source repositories
- [Update Checks](docs/update-checks.md): how updates are found and when an update is shown
- [Profile Settings](docs/profile-settings.md): SPT Version, Fika Profile and the GitHub/GitLab/Codeberg tokens
- [Mod Columns](docs/mod-columns.md): every SPT column and details-panel entry
- [Tools and Configs](docs/tools-and-configs.md): dashboard shortcuts and Write Configs
- [Deployment](docs/deployment.md): SPT layout detection, the version guard, empty folders
- [Troubleshooting](docs/troubleshooting.md): reading the logs and common messages

**Working on the extension**
- [Architecture](docs/developer/architecture.md): how `index.js` is organized, the update pipeline and the logging conventions

---

## Feedback

Found a bug, or want a tool shortcut added? [Open an issue](../../issues). Please include the Vortex log around the problem; [Troubleshooting](docs/troubleshooting.md) explains how to find it.
