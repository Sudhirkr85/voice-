# 🎙️ Universal AI Voice Cloning & Video Studio Engine

A robust, production-calibrated Hindi AI voice cloning framework powered by **Chatterbox Multilingual TTS** (`chatterbox-tts`).

* **Default Master Voice:** Shravan Sir's natural teaching voice (`shravan_sir_master_ref.wav` / `intro_0_20.wav`). Used by default across all future topics unless a different reference is explicitly specified.
* **Scope:** Designed to generate clear, broadcast-quality educational voiceovers for **ANY topic, ANY subject, and ANY exam** (Science, Math, Social Science, Hindi, GK, Navodaya, NMMS, Competitive Exams, etc.).

---

## 🌟 Key Architecture & The 32s Hallucination Prevention

Autoregressive TTS models (like Chatterbox MTL) generate audio tokens sequentially. When given mixed Latin/English characters, exclamation marks (`!`), raw minus signs, or comma-separated numbers, the neural network fails to predict the `<EOS>` (End Of Sequence) token, causing the AI to babble in a repetition loop until hitting the 32.76-second hard limit.

This repository enforces strict rules and post-mortem lessons that guarantee **zero loops and zero hallucinations**:

1. **Pure Devanagari Hindi (Zero Latin Letters):**
   - Options are always `विकल्प ए/बी/सी/डी` (never `विकल्प A/B/C/D`).
   - Science/math acronyms and units are transliterated phonetically into Devanagari (`डीएनए`, `पीएच`, `एसपी थ्री`, `किलोमीटर प्रति घंटा`).
2. **Punctuation & Syntax Rules:**
   - Every spoken sentence MUST end with a single purna viram (`।`) or clean question mark (`?`).
   - Exclamation marks (`!`), double danda (`।।`), and ellipses (`...`) are strictly stripped.
   - Raw minus in numbers (`-1`, `-2`) is transliterated to `माइनस 1`, `माइनस 2`.
   - Commas inside numbers (`20,000`) are stripped to `20000` or written in words.
   - Alphanumeric compounds (`2,4-डी`, `कौन-सी`) are converted to clean words (`टू फोर डी`, `कौन सी`).
   - Clips are capped under 45 words to prevent neural alignment drift.
3. **Calibrated Inference Hyperparameters:**
   ```python
   wav = model.generate(
       text=clean_hindi_text,
       language_id="hi",
       audio_prompt_path=voice_ref_sample,
       exaggeration=0.45,
       cfg_weight=0.55,
       temperature=0.45,
       repetition_penalty=2.0
   )
   ```

---

## 📁 Repository Structure

* **`GEMINI.md`**: Master memory and permanent guidelines for Antigravity AI agents.
* **`universal_voice_sanitizer.py`**: Automated script sanitizer for any text or JSON question bank.
* **`NMMS_Video_Studio/custom_voice_ref/`**:
  * `CV_Raman_Voice_Cloning_Kaggle.ipynb`: 10-second single clip quick test notebook.
  * `CV_Raman_Full_Marathon_Kaggle.ipynb`: Self-contained 1-click batch generation notebook.
  * `MASTER_VOICE_STUDIO_GUIDE.md`: Detailed engineering guide and parameters.

---

## 🚀 How to Use for ANY New Topic or Project

1. Prepare your questions or script in JSON or text format.
2. Run `python universal_voice_sanitizer.py` to ensure 100% Devanagari compliance.
3. Run the Kaggle Notebook with your clean script to batch generate audios with Shravan Sir's cloned voice.
