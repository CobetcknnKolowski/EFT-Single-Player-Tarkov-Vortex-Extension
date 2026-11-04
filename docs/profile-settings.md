# Profile Settings

[← Back to the README](../README.md)

The extension adds these settings to each SPT profile. Open **Profiles** and edit a profile to change them. They only appear while SPT is the active game.

| Setting | Used for |
|---|---|
| **SPT Version** | The SPT version this profile plays on, for example `4.1.6`. Used for update checks on mods that have no SPT version of their own, and to warn when the profile and your SPT folder disagree. **Set this.** |
| **Fika Profile?** | A label for profiles that hold a Fika-compatible mod list. Not used by the extension yet. |
| **GitHub Token** | optional; see below |
| **GitLab Token** | optional; see below |
| **Codeberg Token** | optional; see below |

## SPT Version

Each mod file's own SPT version (from The Forge, shown as Vortex's **Variant**) is preferred. The profile's SPT Version is the fallback, and the reference for the layout check:

| SPT Version | Expected SPT folder layout |
|---|---|
| `3.x` | SPT 3.11 and older |
| `4.0.x` | SPT 4.0 |
| `4.1.x` and newer | SPT 4.1 and newer |

When the profile and the detected layout disagree, you get **"SPT Version Mismatch"** when the game is activated, and **"Deploying With SPT Version Mismatch"** before a deployment. Vortex cannot stop a deployment that has already started, so fix the profile or the SPT folder and deploy again. See [Deployment](deployment.md#the-spt-version-guard).

## Source host tokens

Without a token, these hosts allow a limited number of requests from your computer. GitHub's limit is **60 an hour**, which a large mod list can use up in one update check. When a host's limit is reached, the remaining lookups on *that* host are skipped (other hosts carry on), and you are told when the host will accept requests again.

A token raises the limit (GitHub: **5,000 an hour**). It only needs to **read public repositories**; give it no other permissions.

| Setting | Where to create it | Permissions |
|---|---|---|
| **GitHub Token** | GitHub → Settings → Developer settings → Personal access tokens (a fine-grained token is fine) | none: public repositories only, read-only |
| **GitLab Token** | GitLab.com → Preferences → Access tokens | `read_api` |
| **Codeberg Token** | Codeberg → Settings → Applications → Access tokens | repository: read |

Tokens are stored in the Vortex profile and sent only to that host. They are never written to the log.

Self-hosted **Gitea/Forgejo** servers get no token. The server is whatever a mod's link names, and a token must never be sent to a server you did not choose.
