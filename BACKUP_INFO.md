# BACKUP INFO

Everything the repository's documentation said before the single-page README, kept so text and screenshots can be copied out later. **Nothing here is maintained**: it may not match the current extension, and links between pages no longer work.

| Part | Source |
|---|---|
| [Part 1](#part-1-original-readme-v120) | the original README, for the v1.2.0 extension |
| [Part 2](#part-2-documentation-rewrite-november-2026) | the November 2026 README and `docs/` pages (extension v0.5.13) |

---

## Part 1: Original README (v1.2.0)


### EFT-Single-Player-Tarkov-Vortex-Extension
This is an Extension for the Vortex Modding platform Created by Nexus Mods that allows you to use Vortex to manage your Single Player Tarkov mods.

Please Pardon the mess, This is all new to me from the Developer side. <br/>
Also, this page assumes you know how to use Vortex Mod Manager, If there's enough demand, I will attach a guide to using it. <br/>
---
<details open>
<summary>Installing/Updating the extension </summary>
  <div align="left">
    Go to the "Extensions" List in the Vortex app <br/>   
    <img width="238" height="410" alt="image" src="https://github.com/user-attachments/assets/1415c11c-7e1a-411f-a295-4d017e8e7b37" /> <br/> <br/>
    Click on the button in the bottom right and select the zip file you downloaded, "EFT - Single Player Tarkov Vortex Extension vx.x.x". <br/> 
    <img width="1297" height="155" alt="image" src="https://github.com/user-attachments/assets/f973fea5-ee8e-45d0-a0e7-357024a621ae" /> <br/> <br/>  
    Restart Vortex, and Search the "Extensions" List, if you see it, it successfuly installed, If not, Repeat install and restart. (I do not know why Multiple install attempts is needed sometimes) <br/> 
    <img width="612" height="187" alt="image" src="https://github.com/user-attachments/assets/193c7021-bb59-4ee2-8862-dfe9097e0e09" /> <br/> <br/>
    Go to the "Games" tab <br/> 
    <img width="259" height="544" alt="image" src="https://github.com/user-attachments/assets/f871b75a-c84b-4b9c-9788-c9c68a31dc0b" /> <br/> <br/>
    Search for "Tarkov" <br/>
    <img width="330" height="195" alt="image" src="https://github.com/user-attachments/assets/51401b8b-102c-43c7-889b-ea5a358feaba" /> <br/> <br/>
    Click on it to Activate and it should ask you where you have SPT installed, (Where are SPT.Server.exe and SPT.Launcher located). <br/> <br/>
    Congrats! Vortex can now handle your mod installs as well as activating or deactivating mods. <br/> <br/>
    To see where Vortex is downloading and staging your mods, go to the "Settings" List and check the "Mods" and "Download" Tabs, you can also change the paths for both if you have somewhere else you'd rather mods be stored. <br/> 
    <img width="1027" height="587" alt="image" src="https://github.com/user-attachments/assets/01885f83-763a-4b93-ac4f-8cd88f4e87b6" /> <br/>
  </div>
</details>

---
 
<details open>
<summary>Supported Tools</summary>
  <div align="left">
    Vortex allows you to create shortcuts to tools that can easily be accessed from your Vortex dashboard <br/>
    <img width="1924" height="357" alt="image" src="https://github.com/user-attachments/assets/40fa8a1a-53cb-4951-ad9a-dea6848558bf" /> <br/>  <br/>
    Included in the extension is the "SPT Server" and "SPT Launcher" shortcut's as well as the foundation for other popular Mod tools. <br/> 
    1. Server Value Manager, https://hub.sp-tarkov.com/files/file/379-server-value-modifier-svm/ <br/> 
    2. Load Order Editor Drag'n'Drop, https://hub.sp-tarkov.com/files/file/1923-load-order-editor-drag-drop/ <br/> 
    3. LOE - Load Order Editor, https://hub.sp-tarkov.com/files/file/1082-loe-load-order-editor/ <br/> 
    4. Acid's Bot Placement System, https://hub.sp-tarkov.com/files/file/2782-abps-acid-s-bot-placement-system/ <br/> <br/>
    
   **You will still need to download and install any of the above mods you wish to use into their expected (default) locations, I merely laid the basic file structure and pointers so that Vortex will instantly recognize and populate the shortcuts. Yes, Installing them as Vortex mods is fine and in fact is preferred.**

  Note: If there is a tool you wish to see added to the list, Let me know and I can add it.
  </div>
</details>

---

<details open>
<summary>Installing Mods</summary>
    <div align="left">
Unfortunately, It is not a completely hands off endeavour if you want to take advantage of all the features of Vortex: Proper Deployment, Dependencies and the Variants systems. <br/> <br/>

On a basic level, We will need to make sure that the mod is packaged as Vortex expects. Let's use [Server Value Modifier](https://hub.sp-tarkov.com/files/file/379-server-value-modifier-svm/) as an example that requires manual intervention, Apologies for putting you on blast GhostFenixx xP.
<img width="769" height="55" alt="image" src="https://github.com/user-attachments/assets/0b448fd4-9ba4-4be6-b4da-7fc6624c25ac" /> <br/>

First, we will open the Archive to check if the top level of the archive contains "user" and/or "BepInEx" folders or other files that need to deployed into the root EFT install Folder. As you can see, SVM is packaged to be extracted into the user/mods folder. <br/>
<img width="525" height="117" alt="image" src="https://github.com/user-attachments/assets/a1857f8f-11a0-4f98-924b-c56ce7e008e7" />

In your workspace, Create a 'user' Folder, Go inside, Create a 'mods' Folder, Go inside and Extract SVM. <br/>
Go back 2 levels to your workspace area and package the 'user' folder into an archive, <br/>
The top level of the Archive is now 'user' and th emod has been moved 2 levels down into the 'mods' Folder. <br/>
<img width="436" height="77" alt="image" src="https://github.com/user-attachments/assets/dd044842-dc03-466a-a451-e76a37b4046a" />
<img width="516" height="76" alt="image" src="https://github.com/user-attachments/assets/e2e79007-3d25-43c5-bdb1-dc70c73b970f" />

And That's it! Use Vortex to install this mod and once you Activate it for your Profile and Deploy, you will see the SVM tool shortcut show up on your dashboard and in the Upper Left shortcuts menu.
  </div>
</details>

---

<details open>
<summary>Creating Dependencies, <sup> or Why I did all this work in the first place </sup> </summary>
  <div align="left">
Alright, Let's start making use of the powerful features of Vortex, Creating links between mods so that Vortex can keep track of which mods Require other mods, Must Load After (or Before), or Shouldn't be Deployed with each other (Incompatible with). <sup> To those familiar with Vortex, the Variants system isn't available at this time. </sup> <br/> <br/>
    
Let's use Everyone's favorite AI overhaul mod. [SAIN - Solarint's AI Modifications - Full AI Combat System Replacement](https://hub.sp-tarkov.com/files/file/1062-sain-solarint-s-ai-modifications-full-ai-combat-system-replacement/) <br/>
    As you can see, Sain requires both [BigBrain](https://hub.sp-tarkov.com/files/file/1219-bigbrain/) and [Waypoints](https://hub.sp-tarkov.com/files/file/1119-waypoints-expanded-navmesh/). <br/>
    <sup> Because Solarint and DrakiaXYZ are GOATs, you only need to make filename changes to prep them for Vortex handling. </sup> <br/>

**Important Note: Vortex handles mod relationships by reading the file name so it would benefit us to do some formating ahead of time.**

To begin with, I like to put a unique identifier of the mod inside tildes, (I also like to add brackets too, but those are purely an Aesthetic choice) as well as it's dependents inside parentheses like so, <br/>
<img width="340" height="28" alt="image" src="https://github.com/user-attachments/assets/526d050f-c70e-4fc3-9e19-ed332174a12a" />
    
After installing, use the dependency button to create links between SAIN, BigBrain, and Waypoints, (if you have other versions of SAIN, you can add "Conflicts With" Link). <br/>
    Example of telling Vortex that SAIN 4.1.3 should not be loaded with other verions of SAIN (More specifically, It should not be loaded with ANY other mod that uses \~SAIN\~ in its file name) <br/>
    <img width="689" height="392" alt="image" src="https://github.com/user-attachments/assets/e08c33e8-402a-4935-b3e8-c6bdfdd90aa5" /> <br/> <br/>
When finished, you should see something similar to this, Notice how the links are made using the Unique ID we set earlier? That means if the mod auther changes the file name (hopefully to make vortex integration easier xP), the link will still work just fine.
    <img width="2380" height="293" alt="image" src="https://github.com/user-attachments/assets/b2783934-c7b7-4ef8-8fd8-76f67bd5734a" /> <br/> <br/>
Generally, I make 2 connections between mods,  <br/>
1. "Requires": using the version match notation, (SAIN 4.1.3 requires at least Version 1.3.2 of Bigbrain) <br/>
    <img width="686" height="387" alt="image" src="https://github.com/user-attachments/assets/674b09ef-4773-4361-add8-aa5ed0cb3333" /> <br/> <br/>
2. "Must Deploy After": using any version notation, (SAIN 4.1.3 Must Deploy After ANY version of Bigbrain) <br/>
    <img width="688" height="386" alt="image" src="https://github.com/user-attachments/assets/4c1e0fb3-50e3-4179-ba12-8ba2f85d40ad" /> <br/> <br/>

A great thing about having Vortex handle Dependency like this is that not only will it flag a warning that "Hey, some mod dependencies are not fulfilled"  <br/>
    <img width="509" height="71" alt="image" src="https://github.com/user-attachments/assets/5e0b4832-5e07-4abe-92bb-a248f89d3314" /> <br/> <br/>
But it will also let you know that "Hey, The mod you enabled depends on other mods, do you want to enable those as well?" <br/>
    <img width="915" height="536" alt="image" src="https://github.com/user-attachments/assets/327d5988-1a13-49e8-9981-7e97b9f368c6" /> <br/> <br/>
The same for is true for the other direction, No longer using SAIN? Do you also want to diasble BigBrain and WAypoints now as well? (It even leaves them alone if something else you have enabled still requires them) <br/>
   <img width="916" height="535" alt="image" src="https://github.com/user-attachments/assets/26fe48d1-f097-4400-bd99-668da0d1859f" /> <br/>

  </div>
</details>

---


---

## Part 2: Documentation rewrite (November 2026)


<!-- Source: README.md -->
### EFT - Single Player Tushonka (SPT) Vortex Extension

A game extension for [Vortex](https://www.nexusmods.com/about/vortex/), the mod manager by Nexus Mods, that lets you manage your **Single Player Tarkov (SPT)** mods: install, enable and disable, deploy, keep dependencies in order, and check for updates. Mod information and updates come from [The Forge](https://forge.sp-tarkov.com) and from each mod's source code repository.

> This page assumes you already know the basics of Vortex (profiles, deploying, the Mods page). If you would like a beginner's guide to Vortex itself, let me know.

---

#### What it does

| Feature | In short | Details |
|---|---|---|
| **SPT-aware installer** | Detects your SPT folder layout (3.11, 4.0 or 4.1+), strips extra wrapper folders from archives, moves loose readme/license files into the mod's folder and keeps empty folders a mod needs. | [Installing Mods](docs/installing-mods.md) |
| **Update Mod Information** | One click fills in a mod's name, author, picture, category, description, Fika compatibility and dependency rules from The Forge, then from its GitHub, GitLab, Codeberg or Gitea repository. | [Update Mod Information](docs/mod-information.md) |
| **Update checks** | Vortex's "Check for updates" asks The Forge and the mod's source repository for newer versions. It also runs by itself when the game is activated and every 8 hours. | [Update Checks](docs/update-checks.md) |
| **Dependencies built for you** | "Requires", "load after" and Fika "conflicts" rules are created from The Forge's data. | [File Naming](docs/file-naming.md) |
| **Tool shortcuts** | SPT Server, SPT Launcher, Server Value Modifier, Fika Installer and Give-UI in the Vortex dashboard. | [Tools and Configs](docs/tools-and-configs.md) |
| **Config backups** | "Write Configs" copies your BepInEx, SPT settings and mod configs into a timestamped folder; it also runs by itself when your SPT session ends. | [Tools and Configs](docs/tools-and-configs.md) |
| **SPT columns** | Forge ID, GUID, Addon ID, Fika Compatibility, Source Code Link and more on the Mods page. | [Mod Columns](docs/mod-columns.md) |

---

#### Requirements

- **Vortex** (a current release).
- **SPT** installed with one of the supported layouts: SPT 3.11, SPT 4.0, or SPT 4.1 and newer.
- **[Vortex Library - Cobet's Utilities](https://github.com/CobetcknnKolowski/Vortex-Library-Cobets-Utilities)** (a second extension). It reads and writes each mod's `modinfo.json` and adds the Rules List editor. *Update Mod Information needs it*; everything else works without it.

---

#### Installing or updating the extension

1. Download the extension `.zip` from the [Releases](../../releases) page, and the Library extension from [its Releases page](https://github.com/CobetcknnKolowski/Vortex-Library-Cobets-Utilities/releases).
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

#### Documentation

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

#### Feedback

Found a bug, or want a tool shortcut added? [Open an issue](../../issues). Please include the Vortex log around the problem; [Troubleshooting](docs/troubleshooting.md) explains how to find it.


<!-- Source: docs/README.md -->
### Documentation

New here? Start with [Getting Started](getting-started.md).

#### Using the extension

| Page | Read it when |
|---|---|
| [Getting Started](getting-started.md) | you are setting the extension up for the first time |
| [File Naming](file-naming.md) | you want dependencies to work (read this one) |
| [Installing Mods](installing-mods.md) | an archive installs to the wrong place |
| [Update Mod Information](mod-information.md) | you want to fill in a mod's details, or understand where they came from |
| [Update Checks](update-checks.md) | an update shows, or doesn't, and you want to know why |
| [Profile Settings](profile-settings.md) | you are setting the SPT Version or a GitHub token |
| [Mod Columns](mod-columns.md) | you want to know what a column means |
| [Tools and Configs](tools-and-configs.md) | a tool shortcut is missing, or you want your config backups |
| [Deployment](deployment.md) | you see an SPT Version warning, or wonder about empty folders |
| [Troubleshooting](troubleshooting.md) | something went wrong |

#### Working on the extension

| Page | Covers |
|---|---|
| [Architecture](developer/architecture.md) | how `index.js` is organized, the update pipeline, logging conventions, how to extend it |


<!-- Source: docs/getting-started.md -->
### Getting Started

This walks through first-time setup after the extension is installed (see [Installing or updating the extension](../README.md#installing-or-updating-the-extension)).

#### 1. Activate the game

Open **Games** in Vortex, search for **SPT** and activate it. When Vortex asks where the game is, choose your SPT folder: the one that contains `EscapeFromTarkov.exe`.

The extension then checks which SPT layout you have:

| Layout | How it is recognized |
|---|---|
| SPT 3.11 and older | `SPT.Server.exe` and `SPT.Launcher.exe` next to `EscapeFromTarkov.exe` |
| SPT 4.0 | the server and launcher inside an `SPT` folder |
| SPT 4.1 and newer | the server and launcher inside an `SPT_Runtime` folder |

If none match, you get an **"SPT Installation Not Recognized"** message and Vortex will not manage the game until the folder is corrected. See [Deployment](deployment.md#spt-layout-detection).

#### 2. Set your profile's SPT Version

Open **Profiles**, edit the active SPT profile and fill in **SPT Version** (for example `4.1.6`).

This is used to:
- ask The Forge for updates that fit your SPT version,
- warn you when the profile's SPT Version and your installed SPT layout disagree (for example a profile set to `4.0.13` on an SPT 4.1 folder).

The other profile settings are optional. See [Profile Settings](profile-settings.md).

#### 3. Name your mod archives (recommended)

Before installing a mod from The Forge, add its Forge ID to the archive name in a `[~M####~]` tag:

```
ExampleMod-v1.2.0 [~M1234~].7z
```

This lets the extension identify the mod without asking you, **and it is what makes dependency rules find each other**. [File Naming](file-naming.md) explains the full convention, including addons (`[~A####~]`).

#### 4. Install a mod

Install the archive as usual (drag it into Vortex, or **Install From File** on the Mods page). Shortly after the install, the extension updates the mod's information by itself if it could identify the mod from its file name. If it could not, nothing happens; run **Update Mod Information** yourself (step 5).

#### 5. Update Mod Information

Select one or more mods on the **Mods** page and choose **Update Mod Information** (the *i* icon). Leave "Review each mod individually" unticked to let it work through the selection by itself. See [Update Mod Information](mod-information.md).

#### 6. Enable, deploy, play

Enable the mods for your profile and **Deploy**. Launch the **SPT Server** and **SPT Launcher** from the Vortex dashboard. When the server and everything you started from Vortex close, your configs are backed up to `Mod Configs` automatically (see [Tools and Configs](tools-and-configs.md)).

#### 7. Check for updates

Use Vortex's **Check for updates** on the Mods page whenever you like. The extension also checks by itself 30 seconds after the game is activated, then every 8 hours. A mod with an update shows the update icon; click it to open the page where the update is. See [Update Checks](update-checks.md).


<!-- Source: docs/file-naming.md -->
### File Naming

Vortex links mods to each other by **matching their archive file names**. The extension builds those links (dependency rules) for you, but it can only point them at a name pattern. So a small naming convention does a lot of work: it identifies the mod for [Update Mod Information](mod-information.md), and it is what dependency rules look for.

#### The tag

Put a tag in square brackets with tildes anywhere in the archive name:

| Tag | Meaning | Example |
|---|---|---|
| `[~M1234~]` | a **mod**: `1234` is its Forge ID (the number in its Forge page address, `forge.sp-tarkov.com/mod/1234/...`) | `ExampleMod-v1.2.0 [~M1234~].7z` |
| `[~A567~]` | an **addon**: `567` is its Forge addon ID | `ExampleAddon-v1.0.0 [~A567~].7z` |
| `[~NAME~]` | a free-form grouping name, for mods that are not on The Forge | `MyTweaks-v2.0 [~MYTWEAKS~].zip` |
| `[~M1234~NAME~]` | both: the ID identifies the mod, the name is just for you | `ExampleMod-v1.2.0 [~M1234~EXMOD~].7z` |

**Use a capital `M` or `A`.** Vortex compares names case-sensitively, so `~m1234~` would not be found by a rule looking for `~M1234~`.

The square brackets are optional (only the `~...~` part is matched), but they make the tag easy to spot.

#### Why the tag matters for dependencies

When Update Mod Information reads a mod's dependencies from The Forge, it adds rules like these:

| Rule | Points at | Meaning |
|---|---|---|
| requires | `*~M1219~*`, version range from The Forge | this mod needs mod 1219 |
| load after | `*~M1219~*`, any version | deploy this mod after mod 1219 |

`*~M1219~*` means "any mod whose archive name contains `~M1219~`". **If the dependency's archive is not tagged, Vortex cannot find it** and reports the dependency as missing, even when it is installed. Tag every Forge mod you install, including dependencies.

Addons get a **requires** and **load after** rule on their parent mod (`*~M<parent ID>~*`, using the mod version range The Forge gives for the addon).

Mods that The Forge marks as **incompatible with Fika** get "conflicts" rules against `*~M2326~*`, `*~M2357~*`, `*~FIKA~*` and `*~FIKA_Server~*`. Tag your Fika archives with one of those so Vortex can warn you.

Vortex matches the archive name **without its extension**, and ignores a duplicate-download suffix such as ` (1)` or `.1` at the end.

#### What else is read from the file name

When a mod is installed (and whenever you run Update Mod Information), the file name is also read for its **version**:

1. The tag and the archive extension are removed.
2. SPT version pieces are removed, so they are never mistaken for the mod's version: `-SPT-4.1.5`, `_SPT4.1`, `spt-v4.1` and similar.
3. A version with a `v` in front wins: `-v1.7.0`, `_v2.0.5`, `.v2.1.0`.
4. Otherwise the first dotted number that is not glued to letters is used: `-3.1.0`, `_1.1.1`. (`WW2` and `7Bpencil` are not versions.)

| File name | Version found |
|---|---|
| `ExampleMod-v1.2.0-SPT-4.1.5 [~M1234~].7z` | `1.2.0` |
| `Example_Mod_3.1.0.zip` | `3.1.0` |
| `Example Mod [~M1234~].7z` | none (asked in the dialog) |

A tag and a version together are what let a mod be updated **without any dialog**, right after it is installed.

#### Grouping (Vortex "Logical File Name")

Vortex groups versions of the same mod by their *Logical File Name* (shown by the Library extension as **Logical File Name (Vortex Grouping ID)**). The extension fills it from the tag: `~M1234~` for a mod, `~A567~` for an addon, or the free-form `~NAME~` when there is no ID. Grouping is what lets Vortex treat a newer archive as an update of the one you have.

#### Optional notes in the name

Anything in `( )` or `{ }` is left alone by the extension. The Library extension drops it when it names the `Mod Metadata` folder inside a mod. It is a handy place to note dependencies or the SPT version for yourself:

```
ORBIT-Fika-Addon-v1.2.0 [~A123~ORBIT_FIKA~] {ORBIT-3.0.0 FIKA-2.4.3}.7z
```


<!-- Source: docs/installing-mods.md -->
### Installing Mods

Install SPT mods the usual Vortex way: drag the archive into Vortex, or use **Install From File** on the Mods page. The extension's installer handles every archive installed for SPT. This page explains what it does, so you know when an archive needs a hand.

Before installing, [tag the archive name](file-naming.md) (`[~M1234~]`). It costs a few seconds and lets everything else work automatically.

#### What the installer does

Files are placed **relative to your SPT folder** (the one with `EscapeFromTarkov.exe`), following the archive's own folder layout, after these clean-ups:

1. **`modinfo.json` is handed to the Library extension.** If the archive contains one, it is stored inside the mod (in a `Mod Metadata` folder) instead of being deployed, and its information is applied to the mod after the install.
2. **Wrapper folders are removed.** Many archives put everything inside an extra folder, such as `ExampleMod-1.2.0/BepInEx/plugins/...`. The installer looks for the first real SPT folder (`user`, `BepInEx`, `EscapeFromTarkov_Data` or `SPT_Data`) and drops everything in front of it. An `SPT` or `SPT_Runtime` folder right in front of it is kept, because that is where those files belong on SPT 4.0 and 4.1.
3. **Readme and license files stay with the mod.** That means a file named `license` with any extension, and `.txt`, `.md` or extension-less files whose name contains "license" or "readme".
   - One that is already inside the mod's folders (for example `SPT_Runtime/user/mods/ExampleMod/README.md`) is installed where it is.
   - One that is loose (at the top of the archive, or in a folder outside the SPT structure such as `Docs/`) is moved into the mod's folder, keeping that subfolder: `README.md` → `SPT_Runtime/user/mods/ExampleMod/README.md`, `Docs/readme.txt` → `.../ExampleMod/Docs/readme.txt`.
   - The mod's folder is the server mod folder (`user/mods/<Mod>`) when the archive has one, otherwise its client plugin folder (`BepInEx/plugins/<Mod>`). A plugin that is just a `.dll` in `BepInEx/plugins` gets a folder named after it for these files: `BepInEx/plugins/MyMod.dll` puts its readme in `BepInEx/plugins/MyMod/` (the `.dll` itself stays where it is).
   - If the mod's folder already has a file with that name, the mod's own copy is kept. If the archive has neither a mod folder nor a plugin `.dll` (a config-only mod, say), loose readme and license files are left out rather than put in your SPT folder.
4. **Empty folders are kept.** Vortex only deploys files, so a folder a mod needs but ships empty would otherwise be lost. The installer records these folders, and they are created after every deployment (see [Deployment](deployment.md#empty-folders)).

Then, about 1.5 seconds after the install, **Update Mod Information runs by itself** for the new mod, with no dialog. This only happens when the mod could be identified: a Forge ID or Addon ID plus a version from the file name, or a saved source code link. Otherwise it is skipped quietly, and you can run it yourself.

#### When an archive needs a hand

The installer can only remove wrapper folders when the archive contains a real SPT folder somewhere. Some archives are packed to be extracted *into* `user/mods` (or `BepInEx/plugins`) instead of into the SPT folder, so their top level is just the mod's own folder. Those are installed exactly as packed, which puts them in the wrong place.

You get a warning, **"Unusual Mod Structure Detected"**, when an archive's top level is a folder that normally lives inside another one (`plugins`, `mods` or `profiles`). Other archives without an SPT folder are listed in the log at INFO level ("Installed files outside the recognized user/BepInEx structure").

**Fix it by repacking the archive** so its top level is the folder the files belong in. For example, [Server Value Modifier](https://forge.sp-tarkov.com/mod/236/server-value-modifier-svm) is packed for `user/mods`:

<img width="525" alt="SVM archive packed for the user/mods folder" src="https://github.com/user-attachments/assets/a1857f8f-11a0-4f98-924b-c56ce7e008e7" />

1. Create a `user` folder, and a `mods` folder inside it.
2. Extract the archive into `user/mods`.
3. Pack the `user` folder into a new archive (keep the tag in its name).

<img width="436" alt="Creating user/mods" src="https://github.com/user-attachments/assets/dd044842-dc03-466a-a451-e76a37b4046a" />
<img width="516" alt="The repacked archive" src="https://github.com/user-attachments/assets/e2e79007-3d25-43c5-bdb1-dc70c73b970f" />

> On SPT 4.0 and 4.1 the server's `user` folder sits inside `SPT` (4.0) or `SPT_Runtime` (4.1). Pack server mods to match your SPT folder: `SPT/user/mods/...` on 4.0, `SPT_Runtime/user/mods/...` on 4.1. An archive whose top level is `user` installs to `<SPT folder>/user`, which is only right for SPT 3.11.

#### Dependencies

You do not need to create dependency rules by hand anymore. **Update Mod Information** adds them from The Forge, as long as the archives are [tagged](file-naming.md#why-the-tag-matters-for-dependencies). Vortex then:

- warns you when a mod's dependencies are not installed or enabled,
- offers to enable a mod's dependencies when you enable it,
- offers to disable dependencies nothing else needs when you disable a mod.

You can still add, change or remove rules yourself: in the mod's details panel (**Rules List**, from the Library extension) or with Vortex's own dependency icon. Rules you made are kept when the mod's information is updated, unless you tick **Force Refresh**.


<!-- Source: docs/mod-information.md -->
### Update Mod Information

**Update Mod Information** fills in a mod's details: name, author, picture, description, category, Fika compatibility, its source code link and its dependency rules. It needs the **Library extension** (see [Requirements](../README.md#requirements)), which saves the result in the mod's `modinfo.json`.

#### Running it

On the **Mods** page, either select one or more mods and choose **Update Mod Information** from the bar at the bottom, or click the *i* icon on a single mod.

It also runs by itself, with no dialogs, right after a mod is installed, when the mod can be identified (see [Installing Mods](installing-mods.md#what-the-installer-does)).

##### The first dialog

| Option | Unticked (default) | Ticked |
|---|---|---|
| **Review each mod individually** | *Automatic*: mods that can be identified are updated without asking. The rest get the per-mod dialog. | Every mod gets the per-mod dialog. |
| **Force Refresh** | Values already saved in Vortex are kept; Forge data saved earlier is reused. | Everything is fetched again and replaces what is saved, including the mod's rules. |

In Automatic mode a mod is identified by **a Forge ID or Addon ID plus a version** (from its [file name tag](file-naming.md) or its saved values), or by a saved **source code link** when it has no Forge ID.

##### The per-mod dialog

| Field | Notes |
|---|---|
| Mod Name | the name shown in Vortex |
| Forge ID | needed for The Forge, unless an Addon ID or a Source Code Link is given |
| Addon ID | for addons; the addon's parent mod is found from The Forge |
| Version | recommended: without it only the mod's page information is fetched, not the information for this exact file (SPT version, Fika compatibility, dependencies) |
| Grouping ID | Vortex's Logical File Name (see [File Naming](file-naming.md#grouping-vortex-logical-file-name)) |
| Source Code Link | optional; overrides the automatic choice (see below) |
| Force Refresh | the same as in the first dialog, for this mod only |

**Skip** moves on to the next mod; **Cancel** stops the whole run.

#### Where the information comes from

Sources are used in order. A later source only fills what an earlier one left empty:

1. **What is already saved in Vortex**, including anything you typed in yourself. *Force Refresh* turns this off.
2. **The Forge**: the mod's page, and the exact file version you have.
3. **The mod's source code repository** on GitHub, GitLab, Codeberg or a Gitea/Forgejo server: name, picture, page link and author.

A mod that is not on The Forge can be updated from its source code link alone.

##### From The Forge

| For | Information |
|---|---|
| the mod's page | name, author and co-authors, uploader, picture, short description, page link, category, contains ads, cheat notice, GUID, Forge ID, the list of source code links |
| the exact version (needs a version) | version, the SPT versions it supports (saved as Vortex's **Variant**), Fika compatibility, Forge file ID, **dependency rules** |
| an addon | name, authors, picture, short description, page link, contains ads, Addon ID, **Parent Mod ID**, the category **Addon**; with a version, the parent mod versions it supports and a **requires** rule on the parent |

Dependency and Fika rules are explained in [File Naming](file-naming.md#why-the-tag-matters-for-dependencies). New rules never replace rules the mod already has for the same mod. With *Force Refresh*, the mod's rules are replaced by the freshly built ones, but only when the exact version was found, so a failed lookup cannot wipe your rules.

##### From the source code repository

The author is whoever made the **most recent commit** on the linked branch (or the main branch), because SPT mods are often handed on between authors for different SPT versions. The picture is the repository's own avatar, or its owner's.

#### Choosing the source code link

The Forge lists every source code link a mod has ever had, often one per SPT version. The extension saves the one that fits **this mod file** in the **Source Code Link** column, choosing in this order:

1. a link you typed in the dialog;
2. the link already saved on the mod (unless *Force Refresh* is ticked);
3. the only link, if The Forge lists just one;
4. the link whose label or address names this file's SPT version: `4.1.6`, `4-1-6` or `4_1_6`, or else the same `4.1` / `4.1.x`;
5. the newest link whose label names a version not newer than this file's SPT version, so a link labelled `4.0+` serves a 4.1 file.

If several links exist and none fits, you get **"Source Code Link Not Chosen"**. Set one in the dialog, or in the mod's details panel.

Use the **Source Host** column to say which kind of server a link is on, when it cannot be told from the address (self-hosted Gitea), or choose **None** to stop using a mod's link altogether.

#### The local Forge cache

Forge data is cached, so updating the same mods again does not ask The Forge again. The cache is kept in Vortex's own folder, so changing your staging folder, SPT install or profile does not lose it:

```
%APPDATA%\Vortex\eft-singleplayertushonka\Forge Cache\forge-cache.json
```

The cache only ever grows. Saves are merged and written safely, and an unreadable file is never overwritten (a corrupt one is copied to a `.corrupt-<time>.json` backup first). *Force Refresh* skips the cache for that run. Deleting the file is safe; it is rebuilt as you go.

#### Messages you may see

| Message | Meaning |
|---|---|
| **Mod Information Updated** | It worked. The message says whether full file information or only the mod's page information was retrieved, and what the source repository filled in. |
| **Forge Version Not Found** | The Forge has the mod but not the version you gave. The page information was still saved. |
| **Source Code Link Not Chosen** | see [Choosing the source code link](#choosing-the-source-code-link) |
| **GitHub / GitLab / … Rate Limit Reached** | The host stopped answering for a while; the remaining lookups on that host were skipped. A token raises the limit (see [Profile Settings](profile-settings.md#source-host-tokens)). |
| **No Information Retrieved** | The mod has no Forge ID, and its source code link could not be used. |
| **Mod Information Failed** | Something went wrong for that mod; the message says what. Details are in the log ([Troubleshooting](troubleshooting.md)). |

A *Force Refresh* that worked also records today's date in the **Last Updated Date** column.


<!-- Source: docs/update-checks.md -->
### Update Checks

The extension answers Vortex's **Check for updates** for SPT mods. It asks **The Forge** first, then each mod's **source code repository** (GitHub, GitLab, Codeberg or Gitea), and shows an update only when it is sure the update is new to you.

#### When checks run

| Trigger | When |
|---|---|
| **Check for updates** on the Mods page | whenever you click it (for all mods, or for the ones selected) |
| **Automatic** | 30 seconds after the SPT game is activated (including when Vortex starts with SPT active), then **every 8 hours** while SPT stays active |

The automatic timing is counted from the **last check of any kind**. A check you run yourself pushes the next automatic one back to 8 hours after it, and activating the game again within 5 minutes of a check does not check again. Switching to another game stops the automatic checks until SPT is active again.

Only one check runs at a time. If you click **Check for updates** while one is running, you get "Update Check Already Running" and the running check's results show when it finishes.

#### Step by step

##### 1. The Forge

A mod is checked on The Forge when it has a **GUID or Forge ID** and a **version** (both filled in by [Update Mod Information](mod-information.md)). Nexus Mods mods are left to Vortex, and mods marked *user-generated* are not checked.

Each mod is checked against **its own SPT version**: the SPT versions saved with the mod file (Vortex's **Variant**, for example `~4.1.6`). When the mod has none, the profile's **SPT Version** is used. So a 4.0 build and a 4.1 build of the same mod each get the update meant for them.

Addons are not checked on The Forge (it has no update check for addons). They can still be checked through their own source repository.

##### 2. Source code repositories

A mod is also checked in its repository when it has a **Source Code Link** on a supported host and a version. Mods that share a repository cost one request. **Check for updates** always reads the repository again; the automatic checks reuse what was read in the last hour.

From the repository's releases (or its tags, when it has no releases), the **most recently published one without a reason against it** is taken. Reasons against a release:

- it is a pre-release (on GitLab: a release scheduled for a future date);
- it names a different SPT version than the mod file's (an `SPT 4.0.13` release for a 4.1.6 file);
- its version looks like an SPT version (`4.1.5`) while the mod's own version does not. If the release *name* carries a real mod version (tag `4.1.5`, name `AutoKeycard v1.0.1`), the name's version is used instead.

A tag that names an SPT line with a wildcard, such as `v4.1.x`, never counts as a version; the release name is used instead.

An **addon whose source link points at its main mod's repository** (for example a Fika addon linking the main mod's repository) is not checked there, because that repository's releases are versions of the main mod, not of the addon.

##### 3. The final decision

Each source only *proposes* an update. If both do, the higher version wins, and The Forge wins a tie. An update is shown only when:

- it is **newer** than the version you have installed, **and**
- that version is **not already installed** as another mod entry for the same mod (same GUID, Forge ID or Addon ID; the same repository only for mods with none of those) at the same SPT major.minor.

Every update shown or held back is listed in the log with the reason.

#### The update icon

A mod with an update shows Vortex's update icon. These mods do not come from Nexus Mods, so Vortex cannot download the update itself. **Click the icon to open the page where the update is**: the release page in the repository, or the mod's Forge page. Download the new archive there, keep its [tag](file-naming.md), and install it.

#### Messages you may see

| Message | Meaning |
|---|---|
| **Mod Updates Available** | an automatic check found updates that were not showing before |
| **Source Updates Found** | a check you ran found updates in source repositories |
| **Forge Update Check Incomplete** | some requests to The Forge failed, so some mods were not checked there |
| **GitHub / GitLab / … Rate Limit Reached** | the host stopped answering for a while; repositories on other hosts were still checked. See [tokens](profile-settings.md#source-host-tokens). |
| **Update Check Failed** | the check stopped with an error; see [Troubleshooting](troubleshooting.md) |


<!-- Source: docs/profile-settings.md -->
### Profile Settings

The extension adds these settings to each SPT profile. Open **Profiles** and edit a profile to change them. They only appear while SPT is the active game.

| Setting | Used for |
|---|---|
| **SPT Version** | The SPT version this profile plays on, for example `4.1.6`. Used for update checks on mods that have no SPT version of their own, and to warn when the profile and your SPT folder disagree. **Set this.** |
| **Fika Profile?** | A label for profiles that hold a Fika-compatible mod list. Not used by the extension yet. |
| **GitHub Token** | optional; see below |
| **GitLab Token** | optional; see below |
| **Codeberg Token** | optional; see below |

#### SPT Version

Each mod file's own SPT version (from The Forge, shown as Vortex's **Variant**) is preferred. The profile's SPT Version is the fallback, and the reference for the layout check:

| SPT Version | Expected SPT folder layout |
|---|---|
| `3.x` | SPT 3.11 and older |
| `4.0.x` | SPT 4.0 |
| `4.1.x` and newer | SPT 4.1 and newer |

When the profile and the detected layout disagree, you get **"SPT Version Mismatch"** when the game is activated, and **"Deploying With SPT Version Mismatch"** before a deployment. Vortex cannot stop a deployment that has already started, so fix the profile or the SPT folder and deploy again. See [Deployment](deployment.md#the-spt-version-guard).

#### Source host tokens

Without a token, these hosts allow a limited number of requests from your computer. GitHub's limit is **60 an hour**, which a large mod list can use up in one update check. When a host's limit is reached, the remaining lookups on *that* host are skipped (other hosts carry on), and you are told when the host will accept requests again.

A token raises the limit (GitHub: **5,000 an hour**). It only needs to **read public repositories**; give it no other permissions.

| Setting | Where to create it | Permissions |
|---|---|---|
| **GitHub Token** | GitHub → Settings → Developer settings → Personal access tokens (a fine-grained token is fine) | none: public repositories only, read-only |
| **GitLab Token** | GitLab.com → Preferences → Access tokens | `read_api` |
| **Codeberg Token** | Codeberg → Settings → Applications → Access tokens | repository: read |

Tokens are stored in the Vortex profile and sent only to that host. They are never written to the log.

Self-hosted **Gitea/Forgejo** servers get no token. The server is whatever a mod's link names, and a token must never be sent to a server you did not choose.


<!-- Source: docs/mod-columns.md -->
### Mod Columns

The extension adds these columns to the **Mods** page and the mod details panel while SPT is the active game. The table columns are **hidden by default**; turn them on from the column picker in the table header. Most values are filled in by [Update Mod Information](mod-information.md), and all of them except **Source Code** and **Last Updated Date** can be edited by hand.

| Column | Shown in | What it holds |
|---|---|---|
| **Forge ID** | table, details | the mod's Forge ID |
| **GUID** | table, details | the mod's GUID (used by The Forge's update check) |
| **Addon ID** | table, details | the addon's Forge ID; empty for mods |
| **Parent Mod ID** | table, details | for addons: the Forge ID of the mod the addon belongs to |
| **Fika Compatibility** | table, details | Compatible / Incompatible / Unknown, for this mod file |
| **Contains ADs?** | table, details | True / False / Unknown, as reported by the author |
| **AI Content?** | table, details | True / False / Unknown. *Legacy:* The Forge no longer supplies it; saved values still show. |
| **AI Disclosure** | details | the author's notes on AI content. *Legacy*, like AI Content? |
| **Source Code** | details | every source code link The Forge lists for the mod, as a table |
| **Source Code Link** | table, details | the one link used for **this mod file**: for its information and its [update checks](update-checks.md#2-source-code-repositories) |
| **Source Host** | table, details | the host of the Source Code Link. **Auto** detects it from the address. Choose a host to override it (needed for self-hosted Gitea), or **None** to stop using the link. |
| **Last Updated Date** | table, details | the date of the last *Force Refresh* that updated the mod (read-only) |

Mods updated from The Forge also get Vortex's standard fields filled in: name, author, picture, short description, category (addons get the category **Addon**), version, and **Variant** (the SPT versions the file supports).

#### Added by the Library extension

| Column | Shown in | What it holds |
|---|---|---|
| **Logical File Name (Vortex Grouping ID)** | details | how Vortex groups versions of the same mod; see [File Naming](file-naming.md#grouping-vortex-logical-file-name) |
| **Variant** | table | Vortex's variant field; for SPT mods, the SPT versions the file supports |
| **Rules List** | details | an editable table of the mod's rules (requires, after, before, conflicts) |
| **Generate Modinfo File** | details | writes the mod's current information and rules to its `modinfo.json` |


<!-- Source: docs/tools-and-configs.md -->
### Tools and Configs

#### Tool shortcuts

Vortex shows shortcuts to a game's tools on the dashboard and in the tools menu. A shortcut appears once its program is found in the expected place.

| Tool | Program | Expected location |
|---|---|---|
| **SPT Server** | `SPT.Server.exe` | the SPT runtime folder: the SPT folder itself (3.11), `SPT` (4.0) or `SPT_Runtime` (4.1) |
| **SPT Launcher** | `SPT.Launcher.exe` | the same folder as the server |
| **Server Value Modifier** ([SVM](https://forge.sp-tarkov.com/mod/236/server-value-modifier-svm)) | `Greed.exe` | `BepInEx/plugins/spt` (3.11), or the SPT folder itself (4.0 and 4.1) |
| **Fika Installer/Updater** ([Fika](https://project-fika.gitbook.io/wiki/installing-fika)) | `Fika-Installer.exe` | the SPT folder |
| **Give-UI** ([Give-UI](https://forge.sp-tarkov.com/mod/1617/give-ui)) | `give-ui_x64-portable.exe` | `user/mods/give-ui` inside the SPT runtime folder |

You still install SVM, Fika and Give-UI yourself; installing them as Vortex mods is the preferred way. The SPT Server and the Fika Installer run in a shell window, which they need to work.

Want another tool added? [Open an issue](../../../issues).

#### Write Configs

**Write Configs** (the archive icon in the Mods page toolbar) copies your configuration files into a new, timestamped folder, so you can keep or compare setups:

```
<SPT folder>\Mod Configs\SPT_Configs_<SPT Version>-v<year.month.day-hour.minute.second>\
```

| Copied from | What is copied |
|---|---|
| `BepInEx/Config` | everything |
| `<runtime>/user/sptSettings` | everything |
| `<runtime>/user/mods` | config files only: `.ini` and `.cfg`, and `.json`/`.jsonc` files with "config" in their path |

`<runtime>` is the SPT runtime folder from the table above. SPT's own base settings in `<runtime>/SPT_Data/configs` are deliberately **not** copied; only advanced users should change those. The folder layout is kept inside the backup, so a file can be copied straight back to where it came from.

##### Automatic backups after playing

Write Configs also runs **by itself when your SPT session ends**: once the **SPT Server** you started from Vortex has closed, together with every other tool started from Vortex. It waits 5 seconds first, so restarting the server does not count as the end of a session.

Only programs started through Vortex are seen. A server started outside Vortex does not trigger a backup.


<!-- Source: docs/deployment.md -->
### Deployment

What the extension does around Vortex's deployment, and why.

#### SPT layout detection

SPT has moved its server files between versions, so the extension checks which layout you have:

| Layout | Server and launcher location | Server mods (`user/mods`) |
|---|---|---|
| SPT 3.11 and older | the SPT folder itself | `user/mods` |
| SPT 4.0 | `SPT/` | `SPT/user/mods` |
| SPT 4.1 and newer | `SPT_Runtime/` | `SPT_Runtime/user/mods` |

This runs when the game is activated, and again whenever you **switch profile** or **change the game folder**, so the tool shortcuts and Write Configs always use the right folders. If no layout matches, you get **"SPT Installation Not Recognized"** and Vortex stops managing the game until the folder is fixed. Check that Vortex points at the folder with `EscapeFromTarkov.exe` and that SPT is installed there.

#### The SPT Version guard

Your profile's [SPT Version](profile-settings.md#spt-version) says which layout to expect. If it disagrees with the detected layout (a profile set to `4.0.13` on an SPT 4.1 folder, say), mods may be deployed to the wrong folders:

- When the game is activated: **"SPT Version Mismatch"** (a warning).
- Before every deployment: **"Deploying With SPT Version Mismatch"**. Vortex does not let an extension cancel a deployment, so the deployment still happens. Fix the profile or the folder, then deploy again.

Nothing is checked when the profile has no SPT Version.

#### Empty folders

Vortex deploys files, not folders, so an empty folder in a mod's archive never reaches the game. Some mods need one (a folder they write into, for example). The installer records each mod's empty folders, and after every deployment the extension:

- **creates** the empty folders of every enabled mod that are missing,
- **removes** the folders it created earlier that are no longer wanted (their mod was disabled or removed), but **only if they are still empty**.

A **purge** removes all the folders it created (again, only empty ones). Folders that already existed are never touched. What it created is remembered per SPT folder in:

```
%APPDATA%\Vortex\eft-singleplayertushonka\Empty Folders\empty-folders.json
```

#### Folder marker files

When Vortex creates a folder during deployment, it leaves a small marker file in it (`__folder_managed_by_vortex`). SPT does not need these and they clutter mod folders, so the extension removes them after each deployment. It only looks in the folders that hold deployed files.

Trade-off: without the markers, Vortex may leave the empty folders it created behind after a purge. They are harmless.


<!-- Source: docs/troubleshooting.md -->
### Troubleshooting

#### How the extension reports things

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

#### Finding the log

The Vortex log is `vortex.log` in Vortex's folder, `%APPDATA%\Vortex`. It always includes DEBUG messages, so nothing needs turning on: reproduce the problem, then open the log (older logs are kept next to it).

When you report a problem, please attach the part of the log from just before to just after it.

#### Common problems

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


<!-- Source: docs/developer/architecture.md -->
### Architecture

How the extension is put together, for anyone reading or changing `index.js`. The extension is meant to double as a worked example of a full Vortex game extension, so the code favors being readable from top to bottom over being short.

#### Files

| File | Purpose |
|---|---|
| `index.js` | all of the code |
| `info.json` | the extension's name, author and version, read by Vortex |
| `gameart.png` | the game tile in Vortex |
| `SPT-Server.ico`, `SPT-Launcher.ico`, `Greed.ico`, `Fika.ico`, `Give-UI.ico` | tool shortcut icons |

#### Conventions

**One function per feature.** Each feature lives in one larger function that does the whole job from start to finish, in numbered steps. Small helpers are avoided unless several features share them (`compareVersions`, `parseSourceLink`, `forgeRequest`). Some duplication is accepted when it keeps a function readable on its own.

**Function markers.** Every function is wrapped in a labelled block with a version that is raised whenever the function changes:

```js
//	/*	// Function, syncEmptyFolders v1, Recreate empty folders after a deployment ...
// <what it does, the rules it follows>
// Logging: Toast = ... | INFO = ... | WARN = ... | DEBUG = ...
async function syncEmptyFolders(context, mode, profileId) { ... }
//	*/	// Function, syncEmptyFolders v1
```

Removing the leading `//` from both marker lines turns the whole function into a block comment, which makes it easy to switch one off while testing. The `Logging:` line in each header says what the function reports at each level.

**Three logging levels.** Each tier repeats the one above and adds detail:

| Level | Used for | Example |
|---|---|---|
| Toast (`sendNotification`) | what the user must know now | "Mod: Example, Forge ID: 1234, v1.2.3: Forge does not have this version" |
| `info` / `warn` / `error` | the toast's message, plus what failed; summary counts | `warn`: "Mod file version request failed; listing data will still be saved" |
| `debug` | the exact request and full response; every decision and why | the request URL, HTTP status and response body from `forgeRequest` |

Rules that keep the log useful:
- Every message starts with its area (`Installer:`, `Step 4:`, `Source Updates:` ...), so it can be searched.
- `error` and `warn` carry `errorMessage`; the stack trace goes on a separate `debug` line.
- Lists (every mod, every update, every request) go to `debug`; `info` gets the counts.
- Repeated per-mod problems log once at `warn` and count the rest at `debug` (for example, rate limits).
- Tokens are never logged.

#### Startup

`main(context)` registers everything with Vortex:

| Registration | What |
|---|---|
| `registerGame` | the game; `setup` runs `SPTCheck`; the tool shortcuts |
| `registerInstaller` | `installMod`, for every archive installed for SPT |
| `registerModAttributesUI` | the SPT columns |
| `registerProfileFeature` | SPT Version, Fika Profile?, and the three host tokens |
| `registerAction` | Update Mod Information (multi-select bar and the *i* icon), Write Configs (toolbar) |
| `registerSptSessionHook` | a start hook that sees every tool Vortex launches |

and, in `context.once`, the event handlers:

| Event | Handler |
|---|---|
| `check-mods-version` | `checkModUpdates` |
| `gamemode-activated` | `syncForgeCategories`, `checkSptVersionConsistency`, `watchAutoUpdateCheck` |
| `will-deploy` | `checkSptVersionConsistency` (mode `deploy`) |
| `did-deploy` | `removeFolderMarkers`, then `syncEmptyFolders` |
| `did-purge` | `syncEmptyFolders` (mode `purge`) |
| `did-install-mod` | queued, silent `updateModInformation` |
| `open-mod-page` | `openUpdatePage` |
| profile / game-folder state changes | `watchSptStructure` re-runs `SPTCheck` |

Handlers check the game ID first and leave other games alone.

#### Function map

In file order:

| Function | Job |
|---|---|
| `SPTCheck` | detect the SPT layout (`sptStructure`), used by the path helpers `getSPTRuntimePath`, `getSVMPath`, `getmodsPath` |
| `checkSptVersionConsistency` | compare a profile's SPT Version with the detected layout (modes `activation`, `deploy`) |
| `watchSptStructure` | re-detect the layout when the profile or game folder changes |
| `registerModAttributesUI` | the SPT columns and their editors |
| `forgeRequest` | one Forge API GET: waits out HTTP 429, parses JSON, throws on failure, logs request and response at `debug` |
| `syncForgeCategories` | merge The Forge's categories into Vortex's and fix mods' category attributes |
| `installMod` | archive file list → install instructions |
| `compareVersions` | numeric dotted-version comparison |
| `parseSourceLink` | source code link → host, owner, repo, branch/tag, repository key and API address |
| `sourceRequest` | one GET to a source host's API, with its token and rate-limit tracking |
| `fetchSourceRepoInfo` | repository name, link, picture, latest-commit author |
| `fetchSourceReleases` | recent releases (or tags), with the version in each tag and name |
| `setUpdateLink` / `openUpdatePage` | remember where an update is / open it from the update icon |
| `updateModInformation` | Update Mod Information (below) |
| `checkSourceUpdates` | Step 5 of the update check |
| `checkModUpdates` | the update check (below) |
| `watchAutoUpdateCheck` | the automatic update checks |
| `registerSptSessionHook` | run Write Configs when the SPT session ends |
| `removeFolderMarkers` | delete Vortex's folder marker files after a deployment |
| `syncEmptyFolders` | create and remove tracked empty folders |
| `writeConfigs` | copy config files into `Mod Configs` |
| `main` | registrations |

#### Update Mod Information (`updateModInformation`)

1. **Settings dialog** (skipped when `options.silent`): Automatic or review, Force Refresh.
2. **Collect a job per mod.** Read the file name once (version, `[~M~]`/`[~A~]` tag, grouping) and pick a *track*: `addon`, `mod` or `source` (source code link only). Ask in a dialog only when the mod cannot be identified.
3. **Per job:** load the Forge cache → Forge details and file version (on a cache miss) → build attributes and rules → save the cache (merge-only, locked, atomic) → choose the source code link → fill missing fields from the source repository → merge onto the latest state → write through the Library (`modMetadataWrite`, then `modMetadataRead` with `replaceRules` on a Force Refresh) → tell the user.

Precedence: saved Vortex values → The Forge → source repository, unless Force Refresh.

#### The update check (`checkModUpdates`)

| Step | What |
|---|---|
| 0 | guard against overlapping checks; record `lastFullCheckAt` |
| 0.5 | remove the previous check's update attributes; remember what was flagged |
| 1 | sort mods into Nexus / Forge mods / addons / not checked |
| 2 | Forge requests grouped by each mod's SPT version, in batches of 100 |
| 3 | normalize and de-duplicate the Forge responses |
| 4 | match Forge updates to installed mods → `proposeUpdate` |
| 5 | `checkSourceUpdates` → `proposeUpdate` (only a higher version replaces Forge's) |
| 6 | final decision: newer than installed, and not already installed as another entry of the same mod and SPT major.minor; write `newestVersion` and the update link |

Only Step 6 writes update attributes, so nothing is shown that a later step would have ruled out.

#### The Library extension's API

The Library extension (Vortex Library - Cobet's Utilities) registers these on `context.api.ext`:

| Call | Used by | Purpose |
|---|---|---|
| `modMetadataInstallInstructions(files, destinationPath)` | `installMod` | stage `modinfo.json` into the mod's `Mod Metadata` folder; returns `{instructions, remainingFiles, modName}` |
| `modMetadataWrite(gameId, modId, modInfo)` | `updateModInformation` | write attributes and `rules` to `modinfo.json` |
| `modMetadataRead(gameId, modId, {replaceRules})` | `updateModInformation` | apply `modinfo.json` to the mod; `replaceRules: true` makes the mod's rules match the file exactly |
| `modMetadataExcludeAttributes(gameId, keys)` | (not used yet) | keep attributes out of `modinfo.json` |

`installMod` works without the Library; `updateModInformation` stops with a clear error if it is missing.

#### Module-level state

| Variable | Holds |
|---|---|
| `sptStructure` | the detected SPT layout |
| `autoUpdateQueue` | serializes the after-install updates |
| `forgeCacheLock` | serializes Forge cache saves |
| `sourceReleaseCache`, `sourceRateLimits` | repository releases (1 hour, per session) and each API server's rate limit |
| `lastFullCheckAt`, `updateCheckRunning`, `autoCheckTimer` | update-check timing, the overlap guard, and the next automatic check |

#### Extending

**A new source host.** Add one entry to `SOURCE_HOSTS`. If it speaks one of the known APIs (`github`, `gitlab`, `gitea`), that is all: give it a `label`, its `hostnames`, `api`, `apiBase(origin)` and, if it supports tokens, a `tokenFeature` (and register that profile feature in `main`). A new API family needs one branch in each of `parseSourceLink`, `sourceRequest`, `fetchSourceRepoInfo` and `fetchSourceReleases`.

**A new SPT layout.** Add it to `SPT_STRUCTURES` and `SPT_STRUCTURE_PATHS`, add its detection test in `SPTCheck`, map its versions in `checkSptVersionConsistency`, and add its major.minor to `KNOWN_SPT_MINORS`.

**A new tool shortcut.** Add it to `supportedTools` in `main` with its icon file.
