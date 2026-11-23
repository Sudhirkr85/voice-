# 🎙️ Universal Voice Studio & Voice Cloning Engine (Permanent Memory)

> **Core Philosophy:** This engine is **100% topic-agnostic**. The topic, questions, subject (Science, Math, Social Science, Hindi, GK, Navodaya, NMMS, Engineering, Medical, etc.) can be **anything**. These rules apply universally to any content generated in this workspace.

---

## 1. Chatterbox Multilingual TTS & Voice Cloning Rules
* **Model Engine:** `ChatterboxMultilingualTTS` from `chatterbox-tts`.
* **Two Official Master Voice References (Permanent Anchors):**
  1. **Primary Master Voice (Sudhir Sir):** `sudhir_master_ref.wav` (Located at `NMMS_Video_Studio/custom_voice_ref/sudhir_master_ref.wav`).
     - Extracted from Akanksha Junior Classes (`DWIdV8QTKNU` 1:31–1:51.5).
     - 20.50s, 24kHz, 28.8 dB SNR, crystal-clear, calm, and measured explanation pace.
     - **Default choice** for majority of upcoming marathons, classes, and videos.
  2. **Secondary Master Voice (Shravan Sir):** `shravan_sir_master_ref.wav` (Located at `NMMS_Video_Studio/custom_voice_ref/shravan_sir_master_ref.wav` / `intro_0_20.wav`).
     - 20.01s, 16kHz, authoritative teacher voice for Sagar Coaching Centre Bhagwanpur content.
  * **Rule:** ONLY these 2 official master voices are used. Every project must explicitly choose between Sudhir Sir (Default) or Shravan Sir.

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

* **Zero Raw Digits (0-9) Rule (Absolute Strictness):**
  * NEVER leave bare ASCII digits (`0-9`) or decimals in spoken text (`voice_q`, `voice_ans`, intros, outros).
  * Digits cause Chatterbox phonemizer to either speak in English (e.g., "ten", "five hundred", "point five") or trigger tokenization loops on decimal points (`0.25`, `35.5`).
  * **MANDATORY:** ALWAYS spell out every number in 100% pure Devanagari Hindi words:
    * `0` $\rightarrow$ `शून्य`
    * `2` $\rightarrow$ `दो`, `4` $\rightarrow$ `चार`, `5` $\rightarrow$ `पांच`, `6` $\rightarrow$ `छह`, `7` $\rightarrow$ `सात`, `9` $\rightarrow$ `नौ`
    * `10` $\rightarrow$ `दस`, `12` $\rightarrow$ `बारह`, `17` $\rightarrow$ `सत्रह`, `24` $\rightarrow$ `चौबीस`, `27` $\rightarrow$ `सत्ताईस`, `29` $\rightarrow$ `उनतीस`
    * `36` $\rightarrow$ `छत्तीस`, `40` $\rightarrow$ `चालीस`, `48` $\rightarrow$ `अड़तालीस`, `50` $\rightarrow$ `पचास`, `90` $\rightarrow$ `नब्बे`, `96` $\rightarrow$ `छियानवे`
    * `162` $\rightarrow$ `एक सौ बासठ`, `576` $\rightarrow$ `पांच सौ छिहत्तर`, `748` $\rightarrow$ `सात सौ अड़तालीस`, `1000` $\rightarrow$ `एक हजार`, `1296` $\rightarrow$ `बारह सौ छियानवे`
    * Decimals: `0.25` $\rightarrow$ `शून्य दशमलव दो पांच`, `35.5` $\rightarrow$ `पैंतीस दशमलव पांच`

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
      exaggeration=0.35,
      cfg_weight=0.55,
      temperature=0.38,
      repetition_penalty=2.0
  )
  ```

---

## 2. Universal Script Sanitization Tool
* Always run the universal sanitizer on any new question set or script before passing it to TTS.
* Never assume raw question text is clean; science, math, and bilingual questions frequently contain hidden ASCII letters, digits, or dangerous punctuation.

---

## 3. Kaggle Execution & Notebook Standards (100% Proven Setup)
* **Single Standard Pip Install Command (DO NOT CHANGE):**
  ```python
  !pip install -q chatterbox-tts torchvision==0.21.0 "setuptools<81"
  ```
  * ❌ **NEVER** use `git+https://...` URLs (they prompt for interactive GitHub username/password and freeze the notebook).
  * ℹ️ Pip warnings regarding `dopamine-rl`, `python-fasthtml`, `google-adk` are harmless pre-installed environment notices and can be safely ignored.
* **Self-Contained Notebooks:**
  * Master voice reference MUST be embedded directly as base64 in the notebook (zero manual file upload friction).
* **Auto-Resume Enabled:**
  * Check `if os.path.exists(out_path) and os.path.getsize(out_path) > 2000: continue` before generating each clip.
* **Environment Configuration:**
  * Always set `torch.backends.cudnn.enabled = False` before loading Chatterbox on Kaggle GPU.
  * Check GPU with `assert torch.cuda.is_available()`.
* **Calm Teacher Cadence Controller:**
  * Use `CALM_SPEED = 0.85` via `atempo=0.85` in ffmpeg to enforce measured, calm explanation pace.

---

## 4. Video UI & Presentation Standards (YouTube Long Videos)
* **100% Pure White Background:**
  * ❌ NEVER use dark AI template blue/slate gradients (`#0f172a`), neon borders, or dashed boxes.
  * ✅ ALWAYS use clean, pure white background (`#ffffff`).
* **Active Visual Countdown Timer:**
  * ❌ NEVER use static placeholder buttons like "8s Timer".
  * ✅ ALWAYS use an active animated ticking countdown ring (10... 9... 8... 1... 0) during student thinking window.
* **Solution Box:**
  * High-contrast Emerald Green card displaying the correct option, step-by-step shortcut trick, and scientific formula.
* **Clean CBT Screenshot Footer:**
  * Crop top status bar (battery/wifi) and bottom nav buttons.
  * Patch footer to a single clean line: `© 2026 Online Examination System. All rights reserved.` with zero double text or ghosting.
* **Spoken Student Addressing:**
  * For uploaded videos: ALWAYS ask students to reply in **"कमेंट बॉक्स"** (NEVER "लाइव चैट").

---

## 5. Workspace & File System Boundaries
* Do NOT copy, write, move, or store working project assets into `C:\Users\sudhi\Downloads\`.
* Delete temporary audit/patch scripts immediately after execution.

---

## 6. Proven Real-World Edge Cases & Post-Mortem Lessons (CRITICAL)
*Based on comprehensive audit of 402 clips (394 passed 100%, 8 failed with tail loop due to the following exact patterns):*

1. **Negative Numbers / Raw Minus Signs:**
   * NEVER write raw minus before numbers like `-1`, `-2`, `-5`.
   * The Chatterbox tokenizer misinterprets raw `-` as a hyphen or unknown token, breaking `<EOS>`.
   * ALWAYS spell out in Devanagari: `माइनस 1`, `माइनस 2`, `माइनस 5` or `माइनस एक अंक`.
2. **Commas Inside Numbers:**
   * NEVER write commas inside numbers (e.g., `20,000`, `1,000`).
   * Commas inside numbers cause phonemizer breakdown and looping.
   * ALWAYS write as `20000` or `बीस हजार`.
3. **Alphanumeric Hyphenated Compounds & Chemicals:**
   * NEVER leave patterns like `2,4-D` or `2,4-डी`.
   * ALWAYS spell phonetically: `टू फोर डी`.
   * NEVER leave hyphens in Hindi words like `कौन-सी` $\rightarrow$ ALWAYS write `कौन सी`.
4. **Question Mark Followed by Run-on Sentences:**
   * Avoid compound queries in one clip like `विद्युत प्रतिरोध का मात्रक क्या है? देखते हैं किसका जवाब सबसे पहले आता है, चैट में लिखिए।`
   * Keep interrogative sentences crisp and natural: `विद्युत प्रतिरोध का मात्रक क्या होता है? कमेंट बॉक्स में फटाफट अपना उत्तर लिखिए।`
5. **Missing Punctuation Between Clauses:**
   * Run-on sentences without punctuation (e.g., `बदला जा सकता अनुत्क्रमणीय`) confuse prosody and timing.
   * ALWAYS place a comma or purna viram between independent clauses.
6. **Sentence Word Count Ceiling:**
   * Keep spoken audio clips under **45 words**. Extremely long clips (> 50 words) with complex sub-clauses have higher risk of neural alignment degradation.
7. **Never Repeat Identical Complex Formulas in the Same Clip:**
   * NEVER repeat an identical complex math/physics formula twice in the same clip.
   * Repeating an identical complex phoneme sequence triggers self-attention looping. State the formula in the explanation and close crisply: `सही उत्तर है विकल्प सी।`
8. **Large Numbers (>9999) and Boundary Closures:**
   * Never leave numbers bare at the end of a sentence before purna viram.
   * Always write in Hindi words and close with a natural postposition (e.g. `बीस हजार हर्ट्ज तक।`).

---

## 7. Live Marathon Pacing & Video Cadence Standards (Student Feedback Calibrated)
1. **Question Thinking Window:**
   * Standard: `pad_dur = 8.0` to `10.0` seconds (NEVER 4.5s for interactive classes).
   * Students need at least 8-10 seconds to read 4 options on mobile, decide, and type in comment/chat box.
2. **Solution Box Retention Time:**
   * Standard: `pad_dur = 2.5` to `3.0` seconds after `voice_ans` finishes.
   * Allows students to read the shortcut trick and formula peacefully before the slide scrolls.
3. **Spoken Cadence & Comma Spacing:**
   * Insert commas between thought clauses (e.g., `ध्यान से देखिए, और दस सेकंड में अपना उत्तर कमेंट में लिखिए।`).
   * Commas introduce natural breath pauses in Chatterbox, slowing down rapid delivery.

---

## 8. Bihar Coaching Tone & Spoken Addressing Vocabulary (CRITICAL)
* ❌ **STRICTLY FORBIDDEN:** NEVER use the word **"बच्चों"** (Bachhon) — this word is not used in Bihar coaching/student culture.
* ✅ **NATURAL BIHAR ADDRESSING WORDS:**
  * **"साथियों"** (e.g. *नमस्कार साथियों, स्वागत है आप सभी का...*)
  * **"विद्यार्थियों"** / **"छात्रों"** (e.g. *सभी विद्यार्थी ध्यान दीजिए...*)
  * **"दोस्तों"** (e.g. *चलिए दोस्तों, देखते हैं किसका उत्तर सही आता है...*)
  * **"आप लोग"** / **"सभी लोग"** (e.g. *आप लोग कमेंट बॉक्स में फटाफट बताइए...*)
