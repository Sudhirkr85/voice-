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

---

## 5. Proven Real-World Edge Cases & Post-Mortem Lessons (CRITICAL)
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
   * Keep interrogative sentences crisp and natural: `विद्युत प्रतिरोध का मात्रक क्या होता है? चैट बॉक्स में फटाफट अपना उत्तर लिखिए।`
5. **Missing Punctuation Between Clauses:**
   * Run-on sentences without punctuation (e.g., `बदला जा सकता अनुत्क्रमणीय`) confuse prosody and timing.
   * ALWAYS place a comma or purna viram between independent clauses.
6. **Sentence Word Count Ceiling:**
   * Keep spoken audio clips under **45 words**. Extremely long clips (> 50 words) with complex sub-clauses have higher risk of neural alignment degradation.
7. **Never Repeat Identical Complex Formulas in the Same Clip:**
   * NEVER repeat an identical complex math/physics formula twice in the same clip (e.g. formula in explanation and then repeated word-for-word in the option closure).
   * Repeating an identical complex phoneme sequence triggers self-attention looping. State the formula in the explanation and close crisply: `सही उत्तर है विकल्प सी।`
8. **Large Numbers (>9999) and Boundary Closures:**
   * Never leave numbers like `20000` bare at the end of a sentence before purna viram.
   * Always write in Hindi words (`20 हजार`) and close with a natural postposition (e.g. `20 हर्ट्ज से 20 हजार हर्ट्ज तक।`).

---

## 6. Live Marathon Pacing & Video Cadence Standards (Student Feedback Calibrated)
*Real-world student feedback from YouTube Live Chat showed standard pacing was too fast ("fast h sir"):*

1. **Question Thinking & Chat Response Window (CRITICAL):**
   * Standard: `pad_dur = 8.0` to `10.0` seconds (NEVER 4.5s for live interactive marathons).
   * Students need at least 8-10 seconds to read 4 options on mobile, decide, and type in live chat.
2. **Solution Box Retention Time:**
   * Standard: `pad_dur = 2.5` to `3.0` seconds after `voice_ans` finishes.
   * Allows students to read the shortcut trick and scientific formula peacefully before the slide scrolls.
3. **Spoken Cadence & Comma Spacing:**
   * Insert commas between thought clauses (e.g., `ध्यान से देखिए, और 10 सेकंड में अपना उत्तर चैट में लिखिए।`).
   * Commas introduce natural breath pauses in Chatterbox, slowing down rapid delivery.

---

## 7. Voice Reference & Audio Prompt Standards (Best Practice Protocol)
1. **Dedicated Mic Recording vs YouTube Audio:**
   * A dedicated 15–22 second dry studio voice recording (quiet room, close mic, no echo) is vastly superior to YouTube extracts.
   * YouTube clips often carry room reverb, compression artifacts, or varying mic gain that Chatterbox clones into every token.
2. **Golden Voice Sample Requirements:**
   * Duration: **18 to 22 seconds**.
   * Delivery: Calm, confident, authoritative teacher tone at a relaxed, measured speaking rate.
   * Content: 2-3 natural sentences covering welcoming, question presentation, and explanation cadence.
   * Format: Mono `.wav` or high-bitrate `.m4a`/`.mp3` with clean background (SNR > 30dB).

