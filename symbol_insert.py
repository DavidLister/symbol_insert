#!/usr/bin/env python3

# symbol_insert.py
#
# A tool for inserting symbols anywhere using Rofi.
# 
# David Lister
# May 2025
#

import subprocess

# AI generaterion helps a lot here :)
latex_map = {
    # --- base symbols -------------------------------------------------------
    r'\infty': '∞',  r'\int': '∫',      r'\sqrt': '√',    r'\sum': '∑',
    r'\times': '×',  r'\rightarrow': '→', r'\leftarrow': '←',
    r'\leq': '≤',    r'\geq': '≥',      r'\approx': '≈',  r'\neq': '≠',
    r'\degree': '°', r'\pm': '±',       r'\cdot': '⋅',

    # --- blackboard-bold sets ----------------------------------------------
    r'\mathbb{N}': 'ℕ', r'\mathbb{Z}': 'ℤ',
    r'\mathbb{Q}': 'ℚ', r'\mathbb{R}': 'ℝ',
    r'\mathbb{C}': 'ℂ',

    # --- lowercase Greek ----------------------------------------------------
    r'\alpha': 'α',  r'\beta': 'β',   r'\gamma': 'γ',   r'\delta': 'δ',
    r'\epsilon': 'ε',r'\zeta': 'ζ',   r'\eta': 'η',     r'\theta': 'θ',
    r'\iota': 'ι',   r'\kappa': 'κ',  r'\lambda': 'λ',  r'\mu': 'μ',
    r'\nu': 'ν',     r'\xi': 'ξ',     r'\omicron': 'ο', r'\pi': 'π',
    r'\rho': 'ρ',    r'\sigma': 'σ',  r'\tau': 'τ',     r'\upsilon': 'υ',
    r'\phi': 'φ',    r'\chi': 'χ',    r'\psi': 'ψ',     r'\omega': 'ω',
    # variant forms
    r'\varepsilon': 'ϵ', r'\vartheta': 'ϑ', r'\varkappa': 'ϰ',
    r'\varpi': 'ϖ',      r'\varrho': 'ϱ',   r'\varsigma': 'ς',
    r'\varphi': 'ϕ',

    # --- uppercase Greek ----------------------------------------------------
    # (only the 11 “classical” macros exist in TeX; others added for completeness)
    r'\Gamma': 'Γ',   r'\Delta': 'Δ',   r'\Theta': 'Θ',   r'\Lambda': 'Λ',
    r'\Xi': 'Ξ',      r'\Pi': 'Π',      r'\Sigma': 'Σ',   r'\Upsilon': 'Υ',
    r'\Phi': 'Φ',     r'\Psi': 'Ψ',     r'\Omega': 'Ω',
    r'\Alpha': 'Α',   r'\Beta': 'Β',    r'\Epsilon': 'Ε', r'\Zeta': 'Ζ',
    r'\Eta': 'Η',     r'\Iota': 'Ι',    r'\Kappa': 'Κ',   r'\Mu': 'Μ',
    r'\Nu': 'Ν',      r'\Omicron': 'Ο', r'\Rho': 'Ρ',     r'\Tau': 'Τ',
    r'\Chi': 'Χ',

    # --- mathematical script / calligraphic (uppercase) --------------------
    r'\mathcal{A}': '𝒜', r'\mathscr{A}': '𝒜',
    r'\mathcal{B}': 'ℬ', r'\mathscr{B}': 'ℬ',
    r'\mathcal{C}': '𝒞', r'\mathscr{C}': '𝒞',
    r'\mathcal{D}': '𝒟', r'\mathscr{D}': '𝒟',
    r'\mathcal{E}': 'ℰ', r'\mathscr{E}': 'ℰ',
    r'\mathcal{F}': 'ℱ', r'\mathscr{F}': 'ℱ',
    r'\mathcal{G}': '𝒢', r'\mathscr{G}': '𝒢',
    r'\mathcal{H}': 'ℋ', r'\mathscr{H}': 'ℋ',
    r'\mathcal{I}': 'ℐ', r'\mathscr{I}': 'ℐ',
    r'\mathcal{J}': '𝒥', r'\mathscr{J}': '𝒥',
    r'\mathcal{K}': '𝒦', r'\mathscr{K}': '𝒦',
    r'\mathcal{L}': 'ℒ', r'\mathscr{L}': 'ℒ',
    r'\mathcal{M}': 'ℳ', r'\mathscr{M}': 'ℳ',
    r'\mathcal{N}': '𝒩', r'\mathscr{N}': '𝒩',
    r'\mathcal{O}': '𝒪', r'\mathscr{O}': '𝒪',
    r'\mathcal{P}': '𝒫', r'\mathscr{P}': '𝒫',
    r'\mathcal{Q}': '𝒬', r'\mathscr{Q}': '𝒬',
    r'\mathcal{R}': 'ℛ', r'\mathscr{R}': 'ℛ',
    r'\mathcal{S}': '𝒮', r'\mathscr{S}': '𝒮',
    r'\mathcal{T}': '𝒯', r'\mathscr{T}': '𝒯',
    r'\mathcal{U}': '𝒰', r'\mathscr{U}': '𝒰',
    r'\mathcal{V}': '𝒱', r'\mathscr{V}': '𝒱',
    r'\mathcal{W}': '𝒲', r'\mathscr{W}': '𝒲',
    r'\mathcal{X}': '𝒳', r'\mathscr{X}': '𝒳',
    r'\mathcal{Y}': '𝒴', r'\mathscr{Y}': '𝒴',
    r'\mathcal{Z}': '𝒵', r'\mathscr{Z}': '𝒵',

    # --- mathematical script (lowercase) -----------------------------------
    # TeX has no lowercase \mathcal, so only \mathscr keys are provided.
    r'\mathscr{a}': '𝒶', r'\mathscr{b}': '𝒷', r'\mathscr{c}': '𝒸',
    r'\mathscr{d}': '𝒹', r'\mathscr{e}': 'ℯ', r'\mathscr{f}': '𝒻',
    r'\mathscr{g}': 'ℊ', r'\mathscr{h}': '𝒽', r'\mathscr{i}': '𝒾',
    r'\mathscr{j}': '𝒿', r'\mathscr{k}': '𝓀', r'\mathscr{l}': '𝓁',
    r'\mathscr{m}': '𝓂', r'\mathscr{n}': '𝓃', r'\mathscr{o}': 'ℴ',
    r'\mathscr{p}': '𝓅', r'\mathscr{q}': '𝓆', r'\mathscr{r}': '𝓇',
    r'\mathscr{s}': '𝓈', r'\mathscr{t}': '𝓉', r'\mathscr{u}': '𝓊',
    r'\mathscr{v}': '𝓋', r'\mathscr{w}': '𝓌', r'\mathscr{x}': '𝓍',
    r'\mathscr{y}': '𝓎', r'\mathscr{z}': '𝓏',
}

accented_map = {
    # ——— acute accents ————————————————————————————
    r"\'a": 'á', r'\aacute': 'á',
    r"\'e": 'é', r'\eacute': 'é',
    r"\'i": 'í', r'\iacute': 'í',
    r"\'o": 'ó', r'\oacute': 'ó',
    r"\'u": 'ú', r'\uacute': 'ú',
    r"\'y": 'ý', r'\yacute': 'ý',
    r"\'A": 'Á', r'\Aacute': 'Á',
    r"\'E": 'É', r'\Eacute': 'É',
    r"\'I": 'Í', r'\Iacute': 'Í',
    r"\'O": 'Ó', r'\Oacute': 'Ó',
    r"\'U": 'Ú', r'\Uacute': 'Ú',
    r"\'Y": 'Ý', r'\Yacute': 'Ý',
    r"\'c": 'ć', r'\cacute': 'ć',
    r"\'n": 'ń', r'\nacute': 'ń',
    r"\'s": 'ś', r'\sacute': 'ś',
    r"\'z": 'ź', r'\zacute': 'ź',
    r"\'C": 'Ć', r'\Cacute': 'Ć',
    r"\'N": 'Ń', r'\Nacute': 'Ń',
    r"\'S": 'Ś', r'\Sacute': 'Ś',
    r"\'Z": 'Ź', r'\Zacute': 'Ź',

    # ——— grave accents ————————————————————————————
    r"\`a": 'à', r'\agrave': 'à',
    r"\`e": 'è', r'\egrave': 'è',
    r"\`i": 'ì', r'\igrave': 'ì',
    r"\`o": 'ò', r'\ograve': 'ò',
    r"\`u": 'ù', r'\ugrave': 'ù',
    r"\`A": 'À', r'\Agrave': 'À',
    r"\`E": 'È', r'\Egrave': 'È',
    r"\`I": 'Ì', r'\Igrave': 'Ì',
    r"\`O": 'Ò', r'\Ograve': 'Ò',
    r"\`U": 'Ù', r'\Ugrave': 'Ù',

    # ——— circumflex ————————————————————————————————
    r"\^a": 'â', r'\acirc': 'â',
    r"\^e": 'ê', r'\ecirc': 'ê',
    r"\^i": 'î', r'\icirc': 'î',
    r"\^o": 'ô', r'\ocirc': 'ô',
    r"\^u": 'û', r'\ucirc': 'û',
    r"\^A": 'Â', r'\Acirc': 'Â',
    r"\^E": 'Ê', r'\Ecirc': 'Ê',
    r"\^I": 'Î', r'\Icirc': 'Î',
    r"\^O": 'Ô', r'\Ocirc': 'Ô',
    r"\^U": 'Û', r'\Ucirc': 'Û',

    # ——— tilde ————————————————————————————————————————
    r"\~a": 'ã', r'\atilde': 'ã',
    r"\~n": 'ñ', r'\ntilde': 'ñ',
    r"\~o": 'õ', r'\otilde': 'õ',
    r"\~A": 'Ã', r'\Atilde': 'Ã',
    r"\~N": 'Ñ', r'\Ntilde': 'Ñ',
    r"\~O": 'Õ', r'\Otilde': 'Õ',

    # ——— diaeresis / umlaut ————————————————————————
    r'\"a': 'ä', r'\auml': 'ä',
    r'\"e': 'ë', r'\euml': 'ë',
    r'\"i': 'ï', r'\iuml': 'ï',
    r'\"o': 'ö', r'\ouml': 'ö',
    r'\"u': 'ü', r'\uuml': 'ü',
    r'\"y': 'ÿ', r'\yuml': 'ÿ',
    r'\"A': 'Ä', r'\Auml': 'Ä',
    r'\"E': 'Ë', r'\Euml': 'Ë',
    r'\"I': 'Ï', r'\Iuml': 'Ï',
    r'\"O': 'Ö', r'\Ouml': 'Ö',
    r'\"U': 'Ü', r'\Uuml': 'Ü',
    r'\"Y': 'Ÿ', r'\Yuml': 'Ÿ',

    # ——— ring above ————————————————————————————————
    r'\aa': 'å',   r'\r{a}': 'å',
    r'\AA': 'Å',   r'\r{A}': 'Å',

    # ——— cedilla ————————————————————————————————
    r'\c{c}': 'ç', r'\ccedil': 'ç',
    r'\c{C}': 'Ç', r'\Ccedil': 'Ç',

    # ——— caron / háček ————————————————————————————
    r'\v{c}': 'č', r'\ccaron': 'č',
    r'\v{s}': 'š', r'\scaron': 'š',
    r'\v{z}': 'ž', r'\zcaron': 'ž',
    r'\v{C}': 'Č', r'\Ccaron': 'Č',
    r'\v{S}': 'Š', r'\Scaron': 'Š',
    r'\v{Z}': 'Ž', r'\Zcaron': 'Ž',

    # ——— ogonek ————————————————————————————————
    r'\k{a}': 'ą', r'\aogonek': 'ą',
    r'\k{e}': 'ę', r'\eogonek': 'ę',
    r'\k{A}': 'Ą', r'\Aogonek': 'Ą',
    r'\k{E}': 'Ę', r'\Eogonek': 'Ę',

    # ——— dot-above ——————————————————————————————
    r'\.{z}': 'ż', r'\zdot': 'ż',
    r'\.{Z}': 'Ż', r'\Zdot': 'Ż',

    # ——— slashed letters —————————————————————————
    r'\o': 'ø',  r'\O': 'Ø',

    # ——— ligatures ——————————————————————————————
    r'\ae': 'æ', r'\AE': 'Æ',
    r'\oe': 'œ', r'\OE': 'Œ',

    # ——— special consonants ——————————————————————
    r'\ss': 'ß',
    r'\dh': 'ð', r'\DH': 'Ð',
    r'\th': 'þ', r'\TH': 'Þ',
}

# Configure as you like
character_map = {}
character_map.update(latex_map)
character_map.update(accented_map)

# Build list for rofi with preview
rofi_options = [f"{k} → {v}" for k, v in character_map.items()]
rofi_input = "\n".join(rofi_options)

# Show rofi prompt
rofi_cmd = ["rofi", "-dmenu", "-i", "-p", "Symbol"]
proc = subprocess.run(rofi_cmd, input=rofi_input.encode(), stdout=subprocess.PIPE)
selection = proc.stdout.decode().strip()

# Extract LaTeX command from "key → value"
if "→" in selection:
    key = selection.split("→")[0].strip()
    char = character_map.get(key)
    if char:
        subprocess.run(["xdotool", "type", "--delay", "0", char])

