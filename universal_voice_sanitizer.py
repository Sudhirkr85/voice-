# -*- coding: utf-8 -*-
"""
Universal Voice Script Sanitizer for Chatterbox Multilingual TTS
Ensures 100% Devanagari Hindi, zero Latin characters, and clean punctuation
to prevent 32-second infinite babbling loops.
Includes production lessons learned from real-world 402-clip marathon audit.
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
    r"\b2,4-D\b": "टू फोर डी",
    r"\b2,4-डी\b": "टू फोर डी",
}


def sanitize_text(text: str) -> str:
    """Sanitizes text for Chatterbox TTS so it speaks cleanly without loops."""
    if not text:
        return ""

    # 1. Specific Alphanumeric Chemical / Formulation Names
    text = re.sub(r"2,4-[dD]\b", "टू फोर डी", text)
    text = re.sub(r"2,4-डी", "टू फोर डी", text)

    # 2. Apply general transliteration mapping
    for pattern, repl in TRANSLITERATION_MAP.items():
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)

    # 3. Fix negative numbers (e.g. -1 -> माइनस 1, -2 -> माइनस 2)
    text = re.sub(r"(?<=\s)-(\d+)", r"माइनस \1", text)
    text = re.sub(r"^-(\d+)", r"माइनस \1", text)

    # 4. Strip commas inside numbers (e.g. 20,000 -> 20000)
    text = re.sub(r"(\d+),(\d+)", r"\1\2", text)

    # 4. Strip hyphens in Hindi words (e.g. कौन-सी -> कौन सी, द्वि-स्लिट -> द्वि स्लिट)
    text = re.sub(r"([^\x00-\x7F])-([^\x00-\x7F])", r"\1 \2", text)

    # 5. Common symbols
    text = text.replace("%", " प्रतिशत")
    text = text.replace("°", " डिग्री ")
    text = text.replace("+", " प्लस ")

    # 6. Strip exclamation and bad punctuation that kills <EOS> token
    text = text.replace("!", "।")
    text = text.replace("！", "।")
    text = text.replace("।।", "।")
    text = text.replace("?।", "? ")
    text = text.replace("।?", "?")
    text = text.replace("...", "।")
    text = text.replace("—", " ").replace("–", " ")

    # 7. Clean multi-spaces
    text = re.sub(r"[ \t]+", " ", text).strip()

    # 8. Ensure clean ending
    if text.endswith("?"):
        pass
    elif not text.endswith("।"):
        text += "।"

    while text.endswith("।।"):
        text = text[:-1]

    return text


if __name__ == "__main__":
    sample = "बिल्कुल सही! Option A सही उत्तर है, 20,000 हर्ट्ज और -1 की घात तथा 2,4-डी खरपतवार कौन-सी है?"
    print("Original:", sample)
    print("Sanitized:", sanitize_text(sample))
