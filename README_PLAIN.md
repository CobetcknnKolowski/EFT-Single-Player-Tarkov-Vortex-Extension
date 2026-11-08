<!-- Generated from README.md by tools/make_plain_readme.py. Edit README.md, not this file. -->
# EFT - Single Player Tushonka (SPT) Vortex Extension

A game extension for [Vortex](https://www.nexusmods.com/about/vortex/), the mod manager by Nexus Mods, for managing **Single Player Tarkov (SPT)** mods.

## AI Disclaimer

Much of this extension's code was written with the help of AI. Every feature was planned, directed and reviewed by me, and the extension has been through hundreds of hours of hands-on testing with real mod lists and profiles from SPT 3.11.4 to 4.1.6. If something does not behave the way this page says, please [open an issue](https://github.com/CobetcknnKolowski/EFT-Single-Player-Tarkov-Vortex-Extension/issues).
## FAQ
### Who is this for?

This extension is for people who want a mod manager, but are willing to put in some personal effort to maintain their mod lists: naming archives so they can be recognized, checking that mods are packaged correctly, and keeping an eye on updates.
### Why does Vortex use so much storage space?

Modding with Vortex can use almost **three times** the space of the mods themselves, because each mod can exist in up to four places:

1. **The archive you downloaded**, wherever your browser saved it.
2. **Vortex's copy of that archive**, in Vortex's own archive folder.
3. **The unpacked archive in the "Staging" folder**, where Vortex keeps every installed mod.
4. **The unpacked archive "Deployed" to your game folder**, where the game actually uses it.

For example, my downloaded archives folder is 64 GB, my Vortex archives folder is 79 GB, my staging folder is 102 GB, and my game folder is 84 GB (26 GB of which is not default EFT/SPT). That may seem like a lot, but I have multiple profiles from SPT 3.11.4 to 4.1.6, and many versions of the same mods, from stress testing every YouTuber modpack I could find as well as several of my own profiles for each version.

The staging and game folders are not really two full copies. With Vortex's **Hardlink Deployment**, a deployed file and its staged file share the same data on the drive, so the numbers can look larger or smaller depending on your file system and on the program you use to check them. In Vortex's own words:

> File Systems store files in two parts:
> - an index entry that contains the file name, access rights, change and creating times and so on
> - the actual file data
>
> Hard Links work by creating a second index entry referencing the same data as the original. The second index is a full-fledged index, so there is no differentiation between "original" and "link" after the link was created.
>
> Advantages:
> - perfect compatibility with all applications
> - no performance penalty
> - Wide OS and FS support
>
> Disadvantages:
> - mods have to be on the same partition as the game
> - Due to fact hard links are so "compatible", a lot of applications will act as if original and link were separate files. This includes some backup solutions, tools that measure used disk space and so on, so it will often look like the link was actually a copy.
## Quick Guide
### Part 1: Vortex and Extension Installation

**3.0** Download and install [Vortex](https://www.nexusmods.com/about/vortex/) to the **same drive** as the games you plan to manage.

- **3.0.1** You can save space by having Vortex save its copies of your archives to a different drive.

**3.1.a** Download the extension `.zip` from the [Releases](https://github.com/CobetcknnKolowski/EFT-Single-Player-Tarkov-Vortex-Extension/releases) page, drop it into the **"Drop File(s)"** box on Vortex's **Extensions** tab, and restart Vortex.

**3.1.b** You can also download my [Utilities Library](https://github.com/CobetcknnKolowski/Vortex-Library-Cobets-Utilities) now if you wish, and add it to Vortex the same way. It is optional: it saves each mod's information to a `modinfo.json` file and adds an editable Rules List to the mod details panel.

**3.2** If you are not asked to find the game's location automatically:
1. Go to the **Home** tab, **Games** section.
2. Search for **SPT** in the search bar in the top right.
3. Open the menu (⋮) in the top right of the SPT game box, and choose **Manually Set Location**.
4. Select the root of the game folder where you installed SPT: the folder that holds `SPT_Runtime`, `BepInEx`, `EscapeFromTarkov_Data` and so on.
5. If it asks for a game store, choose **Other**, even if you bought the game on Steam.

**3.3** Go to the **SPT** tab in the left menu, **Game Settings** section. Choose a **Staging Folder**, and make sure the **Deployment** method is **Hardlink**. In other words, the staging folder should be on the same drive as your game folder.
### Part 2: Mod Installation

**3.4** When you download a mod from [The Forge](https://forge.sp-tarkov.com) (or anywhere, really), make sure of a few things:

- **3.4.1** The file name has a readable version: `My SPT Mod-vX.Y.Z`.
- **3.4.2** If the file is from The Forge, the name has the Forge ID with a **M**od or **A**ddon label: `My SPT Mod-vX.Y.Z [~M5247~]` or `My SPT Addon-vX.Y.Z [~A201~]`. Use a capital `M` or `A`: Vortex matches dependency rules against archive names, and the match is case-sensitive.
- **3.4.3** The mod is packaged correctly. If the author put an extra folder above `SPT_Runtime` or `BepInEx`, no worries: my extension's installer fixes that automatically. If it is *missing* a folder (for example a 4.1.x mod with `user` at the top of the archive), you will need to fix it yourself by repacking it. You can also take the opportunity to repack it as a `.7z` to save some space.

**3.5** Head to the **Mods** section and drag the archive onto the **"Drop File(s)"** area at the bottom.

**3.6** The mod starts in the **Never Installed** category (a copy of the archive has been saved to Vortex's archive folder). Click the blue button to **Install** it, which moves it to the **Disabled** category. Or use the drop-down and choose **Enabled** to move it straight to the **Enabled** category.

**3.7** If your archive was named correctly, the extension automatically asks The Forge (and the mod's source code repository) for the mod's information and fills it into Vortex for you. This includes, but is not limited to:
- the mod's thumbnail and short description,
- its version, and its **Variant** (which SPT versions this mod file is for),
- its Forge GUID and Forge category,
- for addons, its Addon ID and Parent Mod ID,
- its dependencies, as Vortex rules,
- links to its source code, and to its web page.

**3.8** If you received no warnings about any issues, go to the menu in the top right and click the rocket symbol to **Deploy** your mods.

**3.9** After deploying, start the **SPT Server** and **SPT Launcher** with their shortcuts in the lower left.

**3.10** The server may complain about empty folders with "missing" assemblies. As long as none of them is a mod you expected to be installed, you can safely ignore these warnings. (As somebody with four 4.1.x profiles, I have quite a few empty folders for mods I am not currently using.)
---

Older documentation, kept for reference, is in [BACKUP_INFO.md](https://github.com/CobetcknnKolowski/EFT-Single-Player-Tarkov-Vortex-Extension/blob/main/BACKUP_INFO.md).
