# EFT - Single Player Tushonka (SPT) Vortex Extension

A game extension for [Vortex](https://www.nexusmods.com/about/vortex/), the mod manager by Nexus Mods, for managing **Single Player Tarkov (SPT)** mods.

## AI Disclaimer

Much of this extension's code was written with the help of AI. Every feature was planned, directed and reviewed by me, and the extension has been through hundreds of hours of hands-on testing with real mod lists and profiles from SPT 3.11.4 to 4.1.6. If something does not behave the way this page says, please [open an issue](../../issues).

____

<a name="faq"></a>
<details open>
<summary><h2>FAQ</h2></summary>

<a name="who-is-this-for"></a>
<details open>
<summary><h3>Who is this for?</h3></summary>

This extension is for people who want a mod manager, but are willing to put in some personal effort to maintain their mod lists: naming archives so they can be recognized, checking that mods are packaged correctly, and keeping an eye on updates.

</details>

----

<a name="storage-space"></a>
<details open>
<summary><h3>Why does Vortex "use" so much storage space?</h3></summary>

A Mod for Vortex "shows up" in up to four places:

1. **The archive you downloaded**, wherever your browser saved it.
2. **Vortex's copy of that archive**, in Vortex's own archive folder.
3. **The unpacked archive in the "Staging" folder**, where Vortex keeps every installed mod.
4. **The unpacked archive "Deployed" to your game folder**, where the game actually uses it.

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

</details>

----

<a name="what-is-a-dependency"></a>
<details open>
<summary><h3>What is a Dependency?</h3></summary>

A **dependency** is another mod that a mod needs in order to work. For example, many mods need a shared library mod such as WTT-CommonLib to be enabled too.

Vortex handles dependencies by **creating a rule for a mod**. A rule says what kind of relationship it is, and which other mod(s) it is about. When a mod's information is updated, the extension creates these rules from The Forge for you, and they show in the **Dependencies** column of the Mods page:

| Rule | Vortex calls it | Meaning |
|---|---|---|
| `requires` | Requires | This mod needs a matching mod to be **enabled**. Vortex warns you when there is none. |
| `after` | Must deploy after | When both mods contain the same file, this mod's copy wins. |
| `before` | Must deploy before | When both mods contain the same file, the other mod's copy wins. |
| `conflicts` | Conflicts with / Can't be deployed together with | The two mods must not be enabled together. Used for mods The Forge marks as incompatible with Fika. |

A rule finds the other mod in one of two ways:

- **By a piece of its archive name** (the rule's `fileExpression`). `*~M1219~*` means "any mod whose archive name contains `~M1219~`": the `*` stands for anything else in the name, such as the mod's name and version. This is why it is useful to put the Forge ID tag, `[~M####~]` or `[~A####~]`, in every archive name: one rule then finds every version of that mod, and the extension can make that rule for you (see [Getting a mod](#getting-a-mod)).
- **By its Logical File Name** (the rule's `logicalFileName`, Vortex's grouping name). Say several different mods can each satisfy a requirement: give them all the same Logical File Name, and one rule looking for that name is satisfied by any of them.

`after` and `before` only decide which mod's files win in Vortex. They do not change the order in which SPT loads mods.

</details>

----

<a name="what-is-a-variant"></a>
<details open>
<summary><h3>What is a Variant?</h3></summary>

**Variant** is a Vortex system that lets you have **multiple versions of the same mod** installed and neatly stacked together, or **the same mod installed with different options** selected. (Those of you familiar with modding Bethesda games and FOMODs will have seen this in action.) In our case, it makes an excellent organizer for **multiple SPT versions of a mod**.

The extension fills in a mod's Variant with the versions that file is made for, as The Forge reports them:

- For a **mod**, it is the SPT versions the file supports, for example `4.1.6` or `~4.1.6`.
- For an **addon**, it is the versions of its **parent mod** that it supports.

The update checks use a mod's Variant to ask The Forge for the update that fits *that* file, so a 4.0 build and a 4.1 build of the same mod each get the right update. When a mod has no Variant, the SPT Version set on your Vortex profile is used.

The value is a version range:

| Variant | Means |
|---|---|
| `4.1.6` | exactly 4.1.6 |
| `~4.1.6` | 4.1.6 or a newer 4.1.x |
| `^4.1.0` | 4.1.0 or newer, below 5.0.0 |
| `>=4.0.0 <4.2.0` | from 4.0.0 up to, but not including, 4.2.0 |

</details>

----

<a name="how-do-i-use-the-rules-table"></a>
<details open>
<summary><h3>How do I use the Rules table?</h3></summary>

The **Rules List** table in the mod details panel comes from my [Utilities Library](https://github.com/CobetcknnKolowski/Vortex-Library-Cobets-Utilities). How to use it is explained in [its FAQ](https://github.com/CobetcknnKolowski/Vortex-Library-Cobets-Utilities#how-do-i-use-the-rules-list). In Vortex, the round **i** beside the Rules List name shows a short version.

Without the Library, use Vortex's own dependency tool instead (see [Making your own rules](#making-your-own-rules)).

</details>

<!-- More FAQ entries go here: a ---- line, then a collapsible block like the ones above. -->

</details>

____

<a name="quick-guide"></a>
<details open>
<summary><h2>Quick Guide</h2></summary>

<details open>
<summary><h3>Part 1: Vortex and Extension Installation</h3></summary>

<!-- TODO: test a fresh ("virgin") Vortex install and confirm the exact steps and labels below. -->

**Step 1.** Download and install [Vortex](https://www.nexusmods.com/about/vortex/).

**Step 2.** Download the extension `.zip` from the [Releases](../../releases) page, drop it into the **"Drop File(s)"** box on Vortex's **Extensions** tab, and restart Vortex.
- **2.1** You can also download my [Utilities Library](https://github.com/CobetcknnKolowski/Vortex-Library-Cobets-Utilities) now if you wish, and add it to Vortex the same way. It is another, optional extension for power users: it lets you use a `modinfo.json` file to prefill a mod's information (useful when you are offline, or for your own personal mods), and adds the Rules List table editor to the mod details panel.
<!-- Screenshot: the Extensions tab with the Drop File(s) box -->

**Step 3.** If you are not asked to find the game's location automatically:
- **3.1** Go to the **Home** tab, **Games** section.
- **3.2** Search for **SPT** in the search bar in the top right.
- **3.3** Open the menu (⋮) in the top right of the SPT game box, and choose **Manually Set Location**.
- **3.4** Select the root of the game folder where you installed SPT: the folder that holds `SPT_Runtime`, `BepInEx`, `EscapeFromTarkov_Data` and so on.
- **3.5** If it asks for a game store, choose **Other**, even if you bought the game on Steam.
<!-- Screenshot: Manually Set Location in the SPT game box -->

**Step 4.** Go to the **SPT** tab in the left menu, **Game Settings** section. Review the **Staging Folder**, and make sure the **Deployment** method is **Hardlink**. In other words, the staging folder should be on the same drive as your game folder.
<!-- Screenshot: Game Settings with the staging folder and Hardlink deployment -->

**Step 5.** On the **Profiles** tab, edit your SPT profile and set its **SPT Version** (for example `4.1.6`).

</details>

<details open>
<summary><h3>Part 2: Mod Installation</h3></summary>

**Step 1.** When you download a mod from [The Forge](https://forge.sp-tarkov.com) (or anywhere, really), make sure of a few things:
- **1.1** The file name has a readable version: `My SPT Mod-vX.Y.Z`.
- **1.2** If the file is from The Forge, the name has the Forge ID with a **M**od or **A**ddon label: `My SPT Mod-vX.Y.Z [~M5247~]` or `My SPT Addon-vX.Y.Z [~A201~]`.
- **1.3** The mod is packaged correctly. If the author put an extra folder above `SPT_Runtime` or `BepInEx`, no worries: my extension's installer fixes that automatically. If it is *missing* a folder (for example a 4.1.x mod with `user` at the top of the archive), you will need to fix it yourself by repacking it. You can also take the opportunity to repack it as a `.7z` to save some space.
<!-- Screenshot: a correctly packed archive, and one that needs repacking -->

**Step 2.** Head to the **Mods** section and drag the archive onto the **"Drop File(s)"** area at the bottom.

**Step 3.** The mod starts in the **Never Installed** category (a copy of the archive has been saved to Vortex's archive folder). Click the blue button to **Install** it, which moves it to the **Disabled** category. Or use the drop-down and choose **Enabled** to move it straight to the **Enabled** category.
<!-- Screenshot: a mod in Never Installed with the Install button and its drop-down -->

**Step 4.** If your archive was named correctly, the extension automatically asks The Forge (and the mod's source code repository) for the mod's information and fills it into Vortex for you: its thumbnail, short description, version, Variant, Forge GUID and category, Addon ID and Parent Mod ID, its dependency rules, and links to its source code and web page.

**Step 5.** If you received no warnings about any issues, go to the menu in the top right and click the rocket symbol to **Deploy** your mods.

**Step 6.** After deploying, start the **SPT Server** and **SPT Launcher** with their shortcuts in the lower left.
- **6.1** The server may complain about empty folders with "missing" assemblies. As long as none of them is a mod you expected to be installed, you can safely ignore these warnings. (As somebody with four 4.1.x profiles, I have quite a few empty folders for mods I am not currently using.)

</details>

</details>

____

<a name="detailed-guide"></a>
<details open>
<summary><h2>Detailed Guide</h2></summary>

The same journey as the Quick Guide, from downloading a mod to playing, then keeping it up to date, with the details of each part.

<a name="getting-a-mod"></a>
<details open>
<summary><h3>1. Getting a mod</h3></summary>

Vortex links mods to each other by **matching their archive names**, so a small naming convention does a lot of work. Before installing, rename the archive:

| Part | Example | Why |
|---|---|---|
| Version | `-v1.2.0` | Read as the mod's version. A `v` in front wins; otherwise the first dotted number not glued to letters is used. SPT versions in the name (`-SPT-4.1.5`, `_SPT4.1`) are ignored. |
| Forge ID tag | `[~M1234~]` | `1234` is the number in the mod's Forge page address (`forge.sp-tarkov.com/mod/1234/...`). Lets the extension look the mod up, and lets other mods' rules find it. |
| Addon tag | `[~A567~]` | The same, for an addon. |
| Grouping name (optional) | `[~M1234~MYMOD~]` or `[~MYMOD~]` | A name for mods that are not on The Forge, or just for you. |
| Notes (optional) | `{WTTCL-3.0.6}` | Anything in `( )` or `{ }` is ignored, handy for noting dependencies or SPT versions. |

Use a **capital** `M` or `A`: Vortex matches names case-sensitively, so `~m1234~` would not be found by a rule looking for `~M1234~`.

```
ExampleMod-v1.2.0 [~M1234~].7z
ExampleAddon-v1.0.0 [~A567~].7z
```

#### Checking how it is packed

Open the archive and look at its top level:

| Top level | What happens |
|---|---|
| `SPT_Runtime`, `BepInEx`, `user`, `EscapeFromTarkov_Data` or `SPT_Data` | Installed as is. |
| A single extra folder around those (`ExampleMod-1.2.0/BepInEx/...`) | The installer removes the extra folder for you. |
| The mod's own folder (`ExampleMod/...`), or `plugins`, `mods` or `profiles` | Packed to be extracted *into* a folder. **Repack it** (below). You get an "Unusual Mod Structure Detected" warning for `plugins`, `mods` and `profiles`. |

On SPT 4.1 the server's `user` folder lives inside `SPT_Runtime` (inside `SPT` on 4.0). An archive with `user` at the top only fits SPT 3.11.

**To repack:** create the missing folders (for example `SPT_Runtime/user/mods`), extract the archive into them, and pack the top folder into a new archive, keeping the name and tag. `.7z` is usually smallest.

</details>

<a name="installing-a-mod"></a>
<details open>
<summary><h3>2. Installing it</h3></summary>

Drag the archive onto the **Drop File(s)** area of the **Mods** page. It appears under **Never Installed**; click **Install** (or choose **Enabled** from its drop-down).

While installing, the extension's installer:
- removes extra wrapper folders in front of the real SPT folders;
- keeps **readme and license files** with the mod: loose ones at the top of the archive are moved into the mod's own folder (`SPT_Runtime/user/mods/<Mod>/`, or `BepInEx/plugins/<Mod>/`; for a plugin that is just a `.dll`, a folder named after the `.dll`);
- keeps **empty folders** the mod needs; Vortex only deploys files, so the extension creates them after every deployment;
- hands a `modinfo.json` in the archive to the Utilities Library, if it is installed.

About 1.5 seconds after the install, **Update Mod Information** runs by itself for the new mod, if it can be identified (a tag and a version in its name, or a saved source code link).

</details>

<a name="updating-mod-information"></a>
<details open>
<summary><h3>3. Updating mod information</h3></summary>

Select one or more mods on the **Mods** page and choose **Update Mod Information** from the bar at the bottom, or right-click a single mod and choose **Update Mod Information**.

To update **every installed mod** at once, use **Update All Mod Information** on the Mods page toolbar (beside Write Configs). It starts with Force Refresh ticked, and it also reaches the versions and variants tucked inside a group, which selecting the group does not. You get one summary notification at the end instead of one per mod.

**The first dialog:**

| Option | Unticked (default) | Ticked |
|---|---|---|
| Review each mod individually | Mods that can be identified are updated without any more input from you. If something is unclear, you are asked to fill in the missing information. | Every mod gets the per-mod dialog. |
| Force Refresh | Values already saved in Vortex are kept; Forge data saved earlier is reused. | Everything is fetched again and replaces what is saved, including the mod's rules. |

**The per-mod dialog** asks for the Mod Name, Forge ID, Addon ID, Version, Grouping ID and Source Code Link, and has two checkboxes:
- **Force Refresh**, for this mod only;
- **Skip Update**, to leave this mod out of update checks (see [Keeping mods up to date](#keeping-mods-up-to-date)). A mod with no Forge ID or link (Google Drive, Discord, your own) can still be saved this way.

**Where the information comes from**, in order (a later source only fills what an earlier one left empty):
1. what is already saved in Vortex, including anything you typed in yourself (unless Force Refresh);
2. **The Forge**: the mod's page, and the exact file version you have (SPT versions, Fika compatibility, dependencies);
3. the mod's **source code repository** on GitHub, GitLab, Codeberg or a Gitea server: name, picture, page link and author.

**Choosing the source code link:** The Forge lists every link a mod has had, often one per SPT version. The extension picks the one for *this* file: one you typed; the one already saved; the only one listed; the one whose label or address names this file's SPT version; links that all point at one repository count as that repository's front page; and finally, the repository that has a release with this file's version. If nothing settles it, you are asked to choose.

</details>

<a name="dependencies-and-rules"></a>
<details open>
<summary><h3>4. Dependencies and rules</h3></summary>

#### Reading the rules

Updating a mod's information adds its dependency rules (see [What is a Dependency?](#what-is-a-dependency) above for what each type means). In the **Dependencies** column, Vortex shows a mod's rules and warns about any that are not met. Rules are only checked against **enabled** mods: a required mod that is installed but disabled does not count. Rules you made yourself are kept when the information is updated, unless you tick Force Refresh.

A rule's **version match** says which versions of the other mod count. It follows [SemVer](https://semver.org) versioning and pattern matching (`*` is any version).

#### Making your own rules

- **With Vortex (always available):** on the Mods page, drag the dependency icon of one mod onto another, then choose the rule type in the popup that opens.
- **With the Utilities Library:** edit the **Rules List** table in the mod's details panel ([how to](https://github.com/CobetcknnKolowski/Vortex-Library-Cobets-Utilities#how-do-i-use-the-rules-list)).

#### File conflicts

When two enabled mods contain the same file, Vortex shows a conflict and wants it settled before you deploy: decide which mod's copy wins with a `before` or `after` rule. This is exactly what you do for a config mod made from your own settings (see [Making a config mod](#making-a-config-mod)).

</details>

<a name="deploying"></a>
<details open>
<summary><h3>5. Deploying</h3></summary>

Click **Deploy** (the rocket). Around every deployment the extension:
- **checks your SPT Version**: if the profile's SPT Version does not match the SPT folder layout (3.11, 4.0 or 4.1), you get a warning. Vortex won't stop the deployment, so fix any outstanding issues and deploy again;
- **creates the empty folders** your enabled mods need, and removes the ones it created for mods you disabled (only if they are still empty);
- **removes Vortex's folder marker files** (`__folder_managed_by_vortex`) from the deployed folders.

</details>

<a name="playing"></a>
<details open>
<summary><h3>6. Playing</h3></summary>

Start the **SPT Server** and **SPT Launcher** from Vortex's tool shortcuts. Shortcuts also appear for the **Server Value Modifier**, the **Fika Installer/Updater** and **Give-UI** if they are installed.

Start them **from Vortex**: that is how the extension knows when your session ends, to back up your configs.

</details>

<a name="backing-up-your-configs"></a>
<details open>
<summary><h3>7. Backing up your configs</h3></summary>

#### Running Write Configs

**Write Configs** copies your configuration files into a new, dated folder:

```
<SPT folder>\Mod Configs\SPT_Configs_<SPT Version>-v<year.month.day-hour.minute.second>\
```

| Copied from | What |
|---|---|
| `BepInEx/Config` | everything |
| `SPT_Runtime/user/sptSettings` | everything |
| `SPT_Runtime/user/mods` | only config files: `.ini`, `.cfg`, and `.json`/`.jsonc` files with "config" in their path |

(`SPT_Runtime` is `SPT` on 4.0, and the SPT folder itself on 3.11.) SPT's own base settings in `SPT_Data/configs` are left out on purpose. The folder layout is kept inside the backup.

It runs **by itself** when your SPT session ends: once the SPT Server you started from Vortex, and every other tool started from Vortex, have closed (it waits 5 seconds, so a server restart does not count). You can also run it any time from the **Write Configs** button on the Mods page toolbar.

#### Making a config mod

Because a backup keeps the game's folder layout, it is a ready-made starting point for a mod holding your own settings, which you can enable per profile or share:

1. Open the newest folder in `Mod Configs` and keep only the files you want (for example `BepInEx/Config/com.example.mod.cfg` and `SPT_Runtime/user/mods/ExampleMod/config/config.json`), **with their folders**.
2. Pack those top folders into an archive, named like any mod: `MyConfigs-v1.0.0 [~MYCONFIGS~].7z`.
3. Install it. Vortex reports a **file conflict** with the mods whose files it replaces: give your config mod an `after` rule on them, so your copies win.
4. Tick **Skip Update** for it, since there is nowhere to check it for updates.

</details>

<a name="keeping-mods-up-to-date"></a>
<details open>
<summary><h3>8. Keeping mods up to date</h3></summary>

Use **Check for updates** on the Mods page whenever you like. The extension also checks by itself **30 seconds** after SPT is activated, then **every 8 hours** while it stays active (counted from the last check of any kind).

Each mod is checked on **The Forge** (it needs a GUID or Forge ID, and a version) and in its **source code repository** (it needs a Source Code Link and a version). An update is shown only when it is newer than what you have, and that newer version is not already installed as another copy of the same mod for the same SPT version.

When a mod has an update, its **version becomes a clickable link** that takes you directly to where the update is (The Forge, or the source code repository). Download the update, and repeat the file readiness steps from [Getting a mod](#getting-a-mod) before installing it.

**Skip Update:** tick it at the bottom of a mod's details panel (or in the Update Mod Information dialog) for mods that cannot be checked: released on Google Drive or Discord, or made by you. The update checks then leave the mod alone.

#### Rate limits and tokens

Without a token, GitHub allows 60 requests an hour, which a big mod list can use up in one check. A **GitHub Token** on your profile raises that to 5,000. The token only needs to *read public repositories*, so it needs no permissions at all.

**Creating a GitHub token:**
1. On GitHub, click your profile picture (top right), then **Settings**.
2. At the bottom of the left sidebar, click **Developer settings**.
3. Under **Personal access tokens**, click **Fine-grained tokens**, then **Generate new token**.
4. Give it a **Token name** (for example `Vortex SPT`) and choose an **Expiration**.
5. Under **Repository access**, choose **Public repositories**.
6. Leave **Permissions** empty, and click **Generate token**.
7. Copy the token now: GitHub only shows it once.
8. In Vortex, go to the **Profiles** tab, edit your SPT profile, and paste it into **GitHub Token**. Each profile has its own token box.

GitLab and Codeberg rarely need a token. If they ask for one: on **GitLab**, click your avatar, then **Edit profile** > **Access tokens**, and create a token with only the `read_api` scope; on **Codeberg**, go to **Settings** > **Applications**, generate a token for **public repositories only** with **repository: Read** access. Paste them into **GitLab Token** or **Codeberg Token** on the profile.

</details>

<a name="when-something-goes-wrong"></a>
<details open>
<summary><h3>9. When something goes wrong</h3></summary>

The extension reports at three levels: a **notification** (what happened, to which mod), an **INFO / WARN / ERROR** line in the Vortex log (the same, plus what failed), and **DEBUG** lines (every request and answer, and every decision).

To find the log, use **Open Logs Folder** in the Mods page toolbar's **Open...** menu, and open `vortex.log`. When you [open an issue](../../issues), please attach the part of the log around the problem.

</details>

</details>

____

Older documentation, kept for reference, is in [BACKUP_INFO.md](BACKUP_INFO.md).
