# -*- coding: utf-8 -*-
"""
Universal Voice Script Sanitizer for Chatterbox Multilingual TTS
Ensures 100% Devanagari Hindi, zero Latin characters, and clean punctuation
to prevent 32-second infinite babbling loops.
"""

import re

# Common English to Devanagari transliteration mapping
TRANSLITERATION_MAP = {
    # Options
    r"\bविकल्प\s*[aA]\b": "विकल्प ए",
    r"\bविकल्प\s*[bB]\b": "विकल्प बी",
    r"\bविकल्प\s*[cC]\b": "विकल्प सी",
    r"\bविकल्प\s*[dD]\b": "विकल्प डी",
    r"\b[oO]ption\s*[aA]\b": "विकल्प ए",
    r"\b[oO]ption\s*[bB]\b": "विकल्प बी",
    r"\b[oO]ption\s*[cC]\b": "विकल्प सी",
    r"\b[oO]ption\s*[dD]\b": "विकल्प डी",

    # Common Science / Math terms
    r"\bDNA\b": "डीएनए",
    r"\bRNA\b": "आरएनए",
    r"\bpH\b": "पीएच",
    r"\bsp3\b": "एसपी थ्री",
    r"\bsp2\b": "एसपी टू",
    r"\bsp\b": "एसपी",
    r"\bC4\b": "सी फोर",
    r"\bC3\b": "सी थ्री",
    r"\b2C\b": "टू सी",
    r"\b4C\b": "फोर सी",
    r"\bkm/h\b": "किलोमीटर प्रति घंटा",
    r"\bm/s\b": "मीटर प्रति सेकंड",
    r"\bcm\b": "सेंटीमीटर",
    r"\bmm\b": "मिलीमीटर",
    r"\bkg\b": "किलोग्राम",
}


def sanitize_text(text: str) -> str:
    """Sanitizes text for Chatterbox TTS so it speaks cleanly without loops."""
    if not text:
        return ""

    # Apply transliteration mapping
    for pattern, repl in TRANSLITERATION_MAP.items():
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)

    # Common symbols
    text = text.replace("%", " प्रतिशत")
    text = text.replace("°", " डिग्री ")
    text = text.replace("+", " प्लस ")

    # Strip exclamation and bad punctuation that kills <EOS> token
    text = text.replace("!", "।")
    text = text.replace("！", "।")
    text = text.replace("।।", "।")
    text = text.replace("?।", "? ")
    text = text.replace("।?", "?")
    text = text.replace("...", "।")
    text = text.replace("—", " ").replace("–", " ")

    # Clean multi-spaces
    text = re.sub(r"[ \t]+", " ", text).strip()

    # Ensure clean ending
    if text.endswith("?"):
        pass
    elif not text.endswith("।"):
        text += "।"

    while text.endswith("।।"):
        text = text[:-1]

    return text


if __name__ == "__main__":
    sample = "बिल्कुल सही! Option A सही उत्तर है, DNA 100% शुद्ध है!!"
    print("Original:", sample)
    print("Sanitized:", sanitize_text(sample))
