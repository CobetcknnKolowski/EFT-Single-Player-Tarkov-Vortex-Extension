# Tools and Configs

[← Back to the README](../README.md)

## Tool shortcuts

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

## Write Configs

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

### Automatic backups after playing

Write Configs also runs **by itself when your SPT session ends**: once the **SPT Server** you started from Vortex has closed, together with every other tool started from Vortex. It waits 5 seconds first, so restarting the server does not count as the end of a session.

Only programs started through Vortex are seen. A server started outside Vortex does not trigger a backup.
