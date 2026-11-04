# Installing Mods

[← Back to the README](../README.md)

Install SPT mods the usual Vortex way: drag the archive into Vortex, or use **Install From File** on the Mods page. The extension's installer handles every archive installed for SPT. This page explains what it does, so you know when an archive needs a hand.

Before installing, [tag the archive name](file-naming.md) (`[~M1234~]`). It costs a few seconds and lets everything else work automatically.

## What the installer does

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

## When an archive needs a hand

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

## Dependencies

You do not need to create dependency rules by hand anymore. **Update Mod Information** adds them from The Forge, as long as the archives are [tagged](file-naming.md#why-the-tag-matters-for-dependencies). Vortex then:

- warns you when a mod's dependencies are not installed or enabled,
- offers to enable a mod's dependencies when you enable it,
- offers to disable dependencies nothing else needs when you disable a mod.

You can still add, change or remove rules yourself: in the mod's details panel (**Rules List**, from the Library extension) or with Vortex's own dependency icon. Rules you made are kept when the mod's information is updated, unless you tick **Force Refresh**.
