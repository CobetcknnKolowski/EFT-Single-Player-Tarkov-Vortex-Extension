# Update Checks

[← Back to the README](../README.md)

The extension answers Vortex's **Check for updates** for SPT mods. It asks **The Forge** first, then each mod's **source code repository** (GitHub, GitLab, Codeberg or Gitea), and shows an update only when it is sure the update is new to you.

## When checks run

| Trigger | When |
|---|---|
| **Check for updates** on the Mods page | whenever you click it (for all mods, or for the ones selected) |
| **Automatic** | 30 seconds after the SPT game is activated (including when Vortex starts with SPT active), then **every 8 hours** while SPT stays active |

The automatic timing is counted from the **last check of any kind**. A check you run yourself pushes the next automatic one back to 8 hours after it, and activating the game again within 5 minutes of a check does not check again. Switching to another game stops the automatic checks until SPT is active again.

Only one check runs at a time. If you click **Check for updates** while one is running, you get "Update Check Already Running" and the running check's results show when it finishes.

## Step by step

### 1. The Forge

A mod is checked on The Forge when it has a **GUID or Forge ID** and a **version** (both filled in by [Update Mod Information](mod-information.md)). Nexus Mods mods are left to Vortex, and mods marked *user-generated* are not checked.

Each mod is checked against **its own SPT version**: the SPT versions saved with the mod file (Vortex's **Variant**, for example `~4.1.6`). When the mod has none, the profile's **SPT Version** is used. So a 4.0 build and a 4.1 build of the same mod each get the update meant for them.

Addons are not checked on The Forge (it has no update check for addons). They can still be checked through their own source repository.

### 2. Source code repositories

A mod is also checked in its repository when it has a **Source Code Link** on a supported host and a version. Mods that share a repository cost one request. **Check for updates** always reads the repository again; the automatic checks reuse what was read in the last hour.

From the repository's releases (or its tags, when it has no releases), the **most recently published one without a reason against it** is taken. Reasons against a release:

- it is a pre-release (on GitLab: a release scheduled for a future date);
- it names a different SPT version than the mod file's (an `SPT 4.0.13` release for a 4.1.6 file);
- its version looks like an SPT version (`4.1.5`) while the mod's own version does not. If the release *name* carries a real mod version (tag `4.1.5`, name `AutoKeycard v1.0.1`), the name's version is used instead.

A tag that names an SPT line with a wildcard, such as `v4.1.x`, never counts as a version; the release name is used instead.

An **addon whose source link points at its main mod's repository** (for example a Fika addon linking the main mod's repository) is not checked there, because that repository's releases are versions of the main mod, not of the addon.

### 3. The final decision

Each source only *proposes* an update. If both do, the higher version wins, and The Forge wins a tie. An update is shown only when:

- it is **newer** than the version you have installed, **and**
- that version is **not already installed** as another mod entry for the same mod (same GUID, Forge ID or Addon ID; the same repository only for mods with none of those) at the same SPT major.minor.

Every update shown or held back is listed in the log with the reason.

## The update icon

A mod with an update shows Vortex's update icon. These mods do not come from Nexus Mods, so Vortex cannot download the update itself. **Click the icon to open the page where the update is**: the release page in the repository, or the mod's Forge page. Download the new archive there, keep its [tag](file-naming.md), and install it.

## Messages you may see

| Message | Meaning |
|---|---|
| **Mod Updates Available** | an automatic check found updates that were not showing before |
| **Source Updates Found** | a check you ran found updates in source repositories |
| **Forge Update Check Incomplete** | some requests to The Forge failed, so some mods were not checked there |
| **GitHub / GitLab / … Rate Limit Reached** | the host stopped answering for a while; repositories on other hosts were still checked. See [tokens](profile-settings.md#source-host-tokens). |
| **Update Check Failed** | the check stopped with an error; see [Troubleshooting](troubleshooting.md) |
