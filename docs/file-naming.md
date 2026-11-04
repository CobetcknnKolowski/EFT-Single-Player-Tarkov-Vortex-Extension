# File Naming

[← Back to the README](../README.md)

Vortex links mods to each other by **matching their archive file names**. The extension builds those links (dependency rules) for you, but it can only point them at a name pattern. So a small naming convention does a lot of work: it identifies the mod for [Update Mod Information](mod-information.md), and it is what dependency rules look for.

## The tag

Put a tag in square brackets with tildes anywhere in the archive name:

| Tag | Meaning | Example |
|---|---|---|
| `[~M1234~]` | a **mod**: `1234` is its Forge ID (the number in its Forge page address, `forge.sp-tarkov.com/mod/1234/...`) | `ExampleMod-v1.2.0 [~M1234~].7z` |
| `[~A567~]` | an **addon**: `567` is its Forge addon ID | `ExampleAddon-v1.0.0 [~A567~].7z` |
| `[~NAME~]` | a free-form grouping name, for mods that are not on The Forge | `MyTweaks-v2.0 [~MYTWEAKS~].zip` |
| `[~M1234~NAME~]` | both: the ID identifies the mod, the name is just for you | `ExampleMod-v1.2.0 [~M1234~EXMOD~].7z` |

**Use a capital `M` or `A`.** Vortex compares names case-sensitively, so `~m1234~` would not be found by a rule looking for `~M1234~`.

The square brackets are optional (only the `~...~` part is matched), but they make the tag easy to spot.

## Why the tag matters for dependencies

When Update Mod Information reads a mod's dependencies from The Forge, it adds rules like these:

| Rule | Points at | Meaning |
|---|---|---|
| requires | `*~M1219~*`, version range from The Forge | this mod needs mod 1219 |
| load after | `*~M1219~*`, any version | deploy this mod after mod 1219 |

`*~M1219~*` means "any mod whose archive name contains `~M1219~`". **If the dependency's archive is not tagged, Vortex cannot find it** and reports the dependency as missing, even when it is installed. Tag every Forge mod you install, including dependencies.

Addons get a **requires** and **load after** rule on their parent mod (`*~M<parent ID>~*`, using the mod version range The Forge gives for the addon).

Mods that The Forge marks as **incompatible with Fika** get "conflicts" rules against `*~M2326~*`, `*~M2357~*`, `*~FIKA~*` and `*~FIKA_Server~*`. Tag your Fika archives with one of those so Vortex can warn you.

Vortex matches the archive name **without its extension**, and ignores a duplicate-download suffix such as ` (1)` or `.1` at the end.

## What else is read from the file name

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

## Grouping (Vortex "Logical File Name")

Vortex groups versions of the same mod by their *Logical File Name* (shown by the Library extension as **Logical File Name (Vortex Grouping ID)**). The extension fills it from the tag: `~M1234~` for a mod, `~A567~` for an addon, or the free-form `~NAME~` when there is no ID. Grouping is what lets Vortex treat a newer archive as an update of the one you have.

## Optional notes in the name

Anything in `( )` or `{ }` is left alone by the extension. The Library extension drops it when it names the `Mod Metadata` folder inside a mod. It is a handy place to note dependencies or the SPT version for yourself:

```
ORBIT-Fika-Addon-v1.2.0 [~A123~ORBIT_FIKA~] {ORBIT-3.0.0 FIKA-2.4.3}.7z
```
