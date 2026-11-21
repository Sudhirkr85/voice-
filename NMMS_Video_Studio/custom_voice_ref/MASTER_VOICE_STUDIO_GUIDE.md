# 🎙️ Master Voice Studio & Video Pipeline Guide

## Overview
This directory (`NMMS_Video_Studio/custom_voice_ref/`) contains all verified assets, notebooks, and scripts for generating teacher-clone voiceovers for Sir C.V. Raman and NMMS Marathon videos.

---

## Key Assets in this Directory
1. **`CV_Raman_200_Human_Script_FINAL.json`**
   - All 200 questions, classes, formulas, options, and spoken texts (`voice_q` and `voice_ans`).
   - 100% Devanagari Hindi, 0 English/Latin letters, 0 exclamation marks, standard purna viram (`।`).
2. **`CV_Raman_Full_Marathon_Kaggle.ipynb`**
   - 1-Click Kaggle Notebook to generate all 402 audio clips.
   - 100% self-contained (all 200 questions embedded internally; no manual dataset upload needed).
   - Auto-detects reference audio `/kaggle/input/**/shravan_sir_master_ref.wav` or downloads clean sample.
   - Built-in Auto-Resume and auto-zipping to `cv_raman_200_audios_final.zip`.
3. **`CV_Raman_Voice_Cloning_Kaggle.ipynb`**
   - 10-Second single clip test notebook to quickly verify voice clarity and ending tone.
4. **`intro_0_20.wav`**
   - Clean 20-second reference audio sample of Shravan Sir's teaching voice from YouTube (`0:00-0:20` of `ixCAZT2vHcM`).

---

## Critical Rules to Prevent AI Hallucination & Looping
1. **Never use Latin characters in spoken fields:**
   - Say `विकल्प ए/बी/सी/डी`, never `विकल्प A/B/C/D`.
   - Say `पीएच मान`, never `pH`.
   - Say `एसपी थ्री`, never `sp3`.
2. **Never use `!` or `।।`:**
   - In Chatterbox TTS, `!` prevents `<EOS>` (End Of Sequence) emission, which causes the AI to babble in a loop until reaching the 32.76s limit.
   - Every sentence MUST end with `।`.
3. **Calibrated Inference Parameters:**
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

## Full Video Build Instructions
1. Run `CV_Raman_Full_Marathon_Kaggle.ipynb` in Kaggle (GPU T4 x2, Internet ON).
2. Download `cv_raman_200_audios_final.zip`.
3. Extract all `.wav` files into:
   `NMMS_Video_Studio/cv_raman_200_live_marathon_build/audio/`
4. Run video assembly script:
   ```bash
   python build_cv_raman_200_live_marathon.py
   ```
5. The final output video will be generated at:
   `NMMS_Video_Studio/output/CV_Raman_200Q_Live_Mahamarathon_CBT.mp4`
