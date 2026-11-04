# Architecture

[← Back to the README](../../README.md)

How the extension is put together, for anyone reading or changing `index.js`. The extension is meant to double as a worked example of a full Vortex game extension, so the code favors being readable from top to bottom over being short.

## Files

| File | Purpose |
|---|---|
| `index.js` | all of the code |
| `info.json` | the extension's name, author and version, read by Vortex |
| `gameart.png` | the game tile in Vortex |
| `SPT-Server.ico`, `SPT-Launcher.ico`, `Greed.ico`, `Fika.ico`, `Give-UI.ico` | tool shortcut icons |

## Conventions

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

## Startup

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

## Function map

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

## Update Mod Information (`updateModInformation`)

1. **Settings dialog** (skipped when `options.silent`): Automatic or review, Force Refresh.
2. **Collect a job per mod.** Read the file name once (version, `[~M~]`/`[~A~]` tag, grouping) and pick a *track*: `addon`, `mod` or `source` (source code link only). Ask in a dialog only when the mod cannot be identified.
3. **Per job:** load the Forge cache → Forge details and file version (on a cache miss) → build attributes and rules → save the cache (merge-only, locked, atomic) → choose the source code link → fill missing fields from the source repository → merge onto the latest state → write through the Library (`modMetadataWrite`, then `modMetadataRead` with `replaceRules` on a Force Refresh) → tell the user.

Precedence: saved Vortex values → The Forge → source repository, unless Force Refresh.

## The update check (`checkModUpdates`)

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

## The Library extension's API

The Library extension (Vortex Library - Cobet's Utilities) registers these on `context.api.ext`:

| Call | Used by | Purpose |
|---|---|---|
| `modMetadataInstallInstructions(files, destinationPath)` | `installMod` | stage `modinfo.json` into the mod's `Mod Metadata` folder; returns `{instructions, remainingFiles, modName}` |
| `modMetadataWrite(gameId, modId, modInfo)` | `updateModInformation` | write attributes and `rules` to `modinfo.json` |
| `modMetadataRead(gameId, modId, {replaceRules})` | `updateModInformation` | apply `modinfo.json` to the mod; `replaceRules: true` makes the mod's rules match the file exactly |
| `modMetadataExcludeAttributes(gameId, keys)` | (not used yet) | keep attributes out of `modinfo.json` |

`installMod` works without the Library; `updateModInformation` stops with a clear error if it is missing.

## Module-level state

| Variable | Holds |
|---|---|
| `sptStructure` | the detected SPT layout |
| `autoUpdateQueue` | serializes the after-install updates |
| `forgeCacheLock` | serializes Forge cache saves |
| `sourceReleaseCache`, `sourceRateLimits` | repository releases (1 hour, per session) and each API server's rate limit |
| `lastFullCheckAt`, `updateCheckRunning`, `autoCheckTimer` | update-check timing, the overlap guard, and the next automatic check |

## Extending

**A new source host.** Add one entry to `SOURCE_HOSTS`. If it speaks one of the known APIs (`github`, `gitlab`, `gitea`), that is all: give it a `label`, its `hostnames`, `api`, `apiBase(origin)` and, if it supports tokens, a `tokenFeature` (and register that profile feature in `main`). A new API family needs one branch in each of `parseSourceLink`, `sourceRequest`, `fetchSourceRepoInfo` and `fetchSourceReleases`.

**A new SPT layout.** Add it to `SPT_STRUCTURES` and `SPT_STRUCTURE_PATHS`, add its detection test in `SPTCheck`, map its versions in `checkSptVersionConsistency`, and add its major.minor to `KNOWN_SPT_MINORS`.

**A new tool shortcut.** Add it to `supportedTools` in `main` with its icon file.
