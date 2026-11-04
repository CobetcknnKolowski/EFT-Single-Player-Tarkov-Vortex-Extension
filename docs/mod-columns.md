# Mod Columns

[← Back to the README](../README.md)

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

## Added by the Library extension

| Column | Shown in | What it holds |
|---|---|---|
| **Logical File Name (Vortex Grouping ID)** | details | how Vortex groups versions of the same mod; see [File Naming](file-naming.md#grouping-vortex-logical-file-name) |
| **Variant** | table | Vortex's variant field; for SPT mods, the SPT versions the file supports |
| **Rules List** | details | an editable table of the mod's rules (requires, after, before, conflicts) |
| **Generate Modinfo File** | details | writes the mod's current information and rules to its `modinfo.json` |
