# 🎙️ Universal Voice Studio & Voice Cloning Engine (Permanent Memory)

> **Core Philosophy:** This engine is **100% topic-agnostic**. The topic, questions, subject (Science, Math, Social Science, Hindi, GK, Navodaya, NMMS, Engineering, Medical, etc.) can be **anything**. These rules apply universally to any content generated in this workspace.

---

## 1. Chatterbox Multilingual TTS & Voice Cloning Rules
* **Model Engine:** `ChatterboxMultilingualTTS` from `chatterbox-tts` (based on Shravan Sir's reference audio `shravan_sir_master_ref.wav` / `intro_0_20.wav`).
* **Zero Latin / English Letter Rule (Absolute Strictness):**
  * NEVER leave Latin characters (`A-Z`, `a-z`) in spoken text (`voice_q`, `voice_ans`, narration, dialogues).
  * Options: ALWAYS use `विकल्प ए/बी/सी/डी` (NEVER `विकल्प A/B/C/D`).
  * Variables, symbols, units: ALWAYS Devanagari transliteration:
    * `g` $\rightarrow$ `जी`
    * `pH` $\rightarrow$ `पीएच`
    * `c, v, n` $\rightarrow$ `सी, वी, एन`
    * `sp3` $\rightarrow$ `एसपी थ्री`
    * `2C, 4C` $\rightarrow$ `टू सी, फोर सी`
    * `DNA` $\rightarrow$ `डीएनए`
    * `RNA` $\rightarrow$ `आरएनए`
    * `km/h` $\rightarrow$ `किलोमीटर प्रति घंटा`
    * `m/s` $\rightarrow$ `मीटर प्रति सेकंड`
    * Formulas: Transliterate phonetically into natural Devanagari Hindi.

* **Punctuation & The 32s Hallucination Loop Prevention (CRITICAL):**
  * **Root Cause:** Exclamation marks (`!`), double danda (`।।`), ellipses (`...`), or question marks attached to danda (`?।`) prevent the neural autoregressive model from predicting the `<EOS>` (End Of Sequence) token. When `<EOS>` fails, the model babbles random phonetic tokens until hitting the 32.76-second hard cutoff limit.
  * **Rule:** Every spoken sentence MUST end with a single purna viram (`।`) or a clean question mark (`?`).
  * Strip all `!`, `।।`, `...`, and trailing dangling punctuation before generation.

* **Math & Symbols:**
  * `%` $\rightarrow$ `प्रतिशत`
  * `+` $\rightarrow$ `प्लस` (or `और` when used as chemical connector)
  * `-` $\rightarrow$ `माइनस`
  * `3°` $\rightarrow$ `थ्री डिग्री` (or `तृतीयक`)

* **Exact Model Generation Parameters (Proven & Calibrated):**
  ```python
  wav = model.generate(
      text=scene["text"],
      language_id="hi",
      audio_prompt_path=voice_ref,
      exaggeration=0.45,
      cfg_weight=0.55,
      temperature=0.45,
      repetition_penalty=2.0
  )
  ```

---

## 2. Universal Script Sanitization Tool
* Always run the universal sanitizer on any new question set or script before passing it to TTS.
* Never assume raw question text is clean; science, math, and bilingual questions frequently contain hidden ASCII letters or dangerous punctuation.

---

## 3. Kaggle Execution & Notebook Standards
* **Self-Contained Notebooks:**
  * Notebooks should never require manual file upload friction or multiple dataset creation steps.
* **Auto-Resume Enabled:**
  * Check `if os.path.exists(out_path) and os.path.getsize(out_path) > 2000: continue` before generating each clip.
* **Environment Configuration:**
  * Always set `torch.backends.cudnn.enabled = False` before loading Chatterbox on Kaggle GPU.
  * Check GPU with `assert torch.cuda.is_available()`.

---

## 4. Workspace & File System Boundaries
* Do NOT copy, write, move, or store working project assets into `C:\Users\sudhi\Downloads\`.
* Delete temporary audit/patch scripts immediately after execution.
