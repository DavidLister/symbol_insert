# symbol_insert
Uses Rofi to insert symbols easily in any text field. Includes Latex symbols and accents.

## Install
Requires:
- Rofi
- xdotools

Right now, it only works on X (untested on Wayland). Will add Wayland support at some point.

## Use
Run by calling with `python symbol_insert.py`. It will open Rofi and you can fuzzy-find a symbol.

This is only really useful if you can call it with a hotkey. I have mine mapped to `Meta + Space` and it's a very convinient way to add synmbols wherever needed.

## Modification
Modifying the script is easy. Just modify the dictionaries to add or remove cases as needed. Right now, I have them mainly indexed using latex syntax, however any combination of "name": "character" work.
