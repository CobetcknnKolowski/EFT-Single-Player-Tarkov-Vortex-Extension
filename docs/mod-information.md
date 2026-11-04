# Update Mod Information

[← Back to the README](../README.md)

**Update Mod Information** fills in a mod's details: name, author, picture, description, category, Fika compatibility, its source code link and its dependency rules. It needs the **Library extension** (see [Requirements](../README.md#requirements)), which saves the result in the mod's `modinfo.json`.

## Running it

On the **Mods** page, either select one or more mods and choose **Update Mod Information** from the bar at the bottom, or click the *i* icon on a single mod.

It also runs by itself, with no dialogs, right after a mod is installed, when the mod can be identified (see [Installing Mods](installing-mods.md#what-the-installer-does)).

### The first dialog

| Option | Unticked (default) | Ticked |
|---|---|---|
| **Review each mod individually** | *Automatic*: mods that can be identified are updated without asking. The rest get the per-mod dialog. | Every mod gets the per-mod dialog. |
| **Force Refresh** | Values already saved in Vortex are kept; Forge data saved earlier is reused. | Everything is fetched again and replaces what is saved, including the mod's rules. |

In Automatic mode a mod is identified by **a Forge ID or Addon ID plus a version** (from its [file name tag](file-naming.md) or its saved values), or by a saved **source code link** when it has no Forge ID.

### The per-mod dialog

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

## Where the information comes from

Sources are used in order. A later source only fills what an earlier one left empty:

1. **What is already saved in Vortex**, including anything you typed in yourself. *Force Refresh* turns this off.
2. **The Forge**: the mod's page, and the exact file version you have.
3. **The mod's source code repository** on GitHub, GitLab, Codeberg or a Gitea/Forgejo server: name, picture, page link and author.

A mod that is not on The Forge can be updated from its source code link alone.

### From The Forge

| For | Information |
|---|---|
| the mod's page | name, author and co-authors, uploader, picture, short description, page link, category, contains ads, cheat notice, GUID, Forge ID, the list of source code links |
| the exact version (needs a version) | version, the SPT versions it supports (saved as Vortex's **Variant**), Fika compatibility, Forge file ID, **dependency rules** |
| an addon | name, authors, picture, short description, page link, contains ads, Addon ID, **Parent Mod ID**, the category **Addon**; with a version, the parent mod versions it supports and a **requires** rule on the parent |

Dependency and Fika rules are explained in [File Naming](file-naming.md#why-the-tag-matters-for-dependencies). New rules never replace rules the mod already has for the same mod. With *Force Refresh*, the mod's rules are replaced by the freshly built ones, but only when the exact version was found, so a failed lookup cannot wipe your rules.

### From the source code repository

The author is whoever made the **most recent commit** on the linked branch (or the main branch), because SPT mods are often handed on between authors for different SPT versions. The picture is the repository's own avatar, or its owner's.

## Choosing the source code link

The Forge lists every source code link a mod has ever had, often one per SPT version. The extension saves the one that fits **this mod file** in the **Source Code Link** column, choosing in this order:

1. a link you typed in the dialog;
2. the link already saved on the mod (unless *Force Refresh* is ticked);
3. the only link, if The Forge lists just one;
4. the link whose label or address names this file's SPT version: `4.1.6`, `4-1-6` or `4_1_6`, or else the same `4.1` / `4.1.x`;
5. the newest link whose label names a version not newer than this file's SPT version, so a link labelled `4.0+` serves a 4.1 file.

If several links exist and none fits, you get **"Source Code Link Not Chosen"**. Set one in the dialog, or in the mod's details panel.

Use the **Source Host** column to say which kind of server a link is on, when it cannot be told from the address (self-hosted Gitea), or choose **None** to stop using a mod's link altogether.

## The local Forge cache

Forge data is cached, so updating the same mods again does not ask The Forge again. The cache is kept in Vortex's own folder, so changing your staging folder, SPT install or profile does not lose it:

```
%APPDATA%\Vortex\eft-singleplayertushonka\Forge Cache\forge-cache.json
```

The cache only ever grows. Saves are merged and written safely, and an unreadable file is never overwritten (a corrupt one is copied to a `.corrupt-<time>.json` backup first). *Force Refresh* skips the cache for that run. Deleting the file is safe; it is rebuilt as you go.

## Messages you may see

| Message | Meaning |
|---|---|
| **Mod Information Updated** | It worked. The message says whether full file information or only the mod's page information was retrieved, and what the source repository filled in. |
| **Forge Version Not Found** | The Forge has the mod but not the version you gave. The page information was still saved. |
| **Source Code Link Not Chosen** | see [Choosing the source code link](#choosing-the-source-code-link) |
| **GitHub / GitLab / … Rate Limit Reached** | The host stopped answering for a while; the remaining lookups on that host were skipped. A token raises the limit (see [Profile Settings](profile-settings.md#source-host-tokens)). |
| **No Information Retrieved** | The mod has no Forge ID, and its source code link could not be used. |
| **Mod Information Failed** | Something went wrong for that mod; the message says what. Details are in the log ([Troubleshooting](troubleshooting.md)). |

A *Force Refresh* that worked also records today's date in the **Last Updated Date** column.
