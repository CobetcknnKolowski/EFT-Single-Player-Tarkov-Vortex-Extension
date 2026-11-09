"""Build README_PLAIN.md from README.md: the same text without GitHub's collapsible sections.

Edit README.md, then run:  python tools/make_plain_readme.py
- <details>/<summary> blocks become ordinary headings (an <h2> summary becomes "## ...").
- The one-cell tables that draw a box around each section are removed; a line (---) separates the main sections instead.
- Hidden notes (<!-- ... -->) are removed.
- Links that only work on GitHub (../../issues, ../../releases, other files in the repository) become full web addresses,
  so the plain copy also works outside GitHub (inside the release zip, or on a mod page).
"""
import pathlib
import re

REPOSITORY = 'https://github.com/CobetcknnKolowski/EFT-Single-Player-Tarkov-Vortex-Extension'
root = pathlib.Path(__file__).resolve().parent.parent
text = (root / 'README.md').read_text(encoding='utf-8')

# Step 1: Remove hidden notes and the box and collapsible wrappers; turn each summary into a heading of the same level.
text = re.sub(r'<!--.*?-->\n?', '', text, flags=re.S)
text = re.sub(r'^\s*</?details[^>]*>\s*$\n?', '', text, flags=re.M)
text = re.sub(r'^\s*(<table[^>]*><tr><td>|</td></tr></table>)\s*$\n?', '', text, flags=re.M)
text = re.sub(r'<summary><h([1-6])>(.*?)</h\1></summary>', lambda match: '#' * int(match.group(1)) + ' ' + match.group(2), text)

# Separate the main (##) sections with a line, since the boxes are gone. A section's <a name> anchor stays above it.
text = re.sub(r'\n((?:<a name="[^"]*"></a>\n)?## )', r'\n\n---\n\n\1', text)

# Step 2: Make GitHub-relative links absolute.
text = text.replace('](../../issues)', f']({REPOSITORY}/issues)').replace('](../../releases)', f']({REPOSITORY}/releases)')
text = re.sub(r'\]\((?!https?://|#)([^)]+)\)', lambda match: f']({REPOSITORY}/blob/main/{match.group(1)})', text)

# Step 3: Tidy blank lines, and say where the text comes from.
text = re.sub(r'\n{3,}', '\n\n', text).strip() + '\n'
header = '<!-- Generated from README.md by tools/make_plain_readme.py. Edit README.md, not this file. -->\n'
(root / 'README_PLAIN.md').write_text(header + text, encoding='utf-8')
print('README_PLAIN.md written:', len(text.splitlines()), 'lines')
