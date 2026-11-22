# -*- coding: utf-8 -*-
"""
Full Master Builder for 200 Questions CV Raman Live Mahamarathon (CBT Format).
Key Features:
- 200 Questions across Classes 6 to 12.
- Clean CBT Layout (BCST Bihar Online CBT Test UI with Haryana 2-question continuous vertical scroll).
- Zero robotic language, pure conversational teacher tone.
- 4.5-second natural thinking pause on question phase.
- Highlighted answer + solution box on answer phase.
- Ultrafast TS clip encoding & concat into final MP4.
"""

import os
import sys
import json
import time
import subprocess
import concurrent.futures
import imageio_ffmpeg
from playwright.sync_api import sync_playwright

ROOT = r"C:\Users\sudhi\OneDrive\Desktop\Google_Drive_Backup"
BUILD_DIR = os.path.join(ROOT, "NMMS_Video_Studio", "cv_raman_200_live_marathon_build")
AUDIO_DIR = os.path.join(BUILD_DIR, "audio")
FRAMES_DIR = os.path.join(BUILD_DIR, "frames")
CLIPS_DIR = os.path.join(BUILD_DIR, "clips")
OUT_DIR = os.path.join(ROOT, "NMMS_Video_Studio", "output")

os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(CLIPS_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

with open("CV_Raman_200_Live_Marathon_FINAL.json", "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

print(f"Loaded {len(QUESTIONS)} questions for the Mahamarathon.")

def build_html_pages():
    # 1. Intro Page HTML
    intro_html = f"""<!DOCTYPE html>
    <html lang='hi'><head><meta charset='UTF-8'>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Nirmala+UI:wght@400;700;800;900&display=swap');
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        width: 1920px; height: 1080px; background: radial-gradient(circle at center, #1e293b, #090d16);
        display: flex; align-items: center; justify-content: center; font-family: 'Nirmala UI', sans-serif;
      }}
      .cover-card {{
        width: 1720px; height: 980px; background: #ffffff; border-radius: 16px;
        box-shadow: 0 35px 80px rgba(0,0,0,0.8); display: flex; flex-direction: column;
        align-items: center; justify-content: center; padding: 60px; text-align: center; border: 4px solid #1e3a8a;
      }}
      .badge-top {{
        background: #1e3a8a; color: #f8fafc; font-size: 26pt; font-weight: 900;
        padding: 12px 42px; border-radius: 50px; margin-bottom: 25px; letter-spacing: 1px;
      }}
      .title-main {{ font-size: 52pt; font-weight: 900; color: #0f172a; margin-bottom: 15px; line-height: 1.2; }}
      .sub-title {{ font-size: 34pt; font-weight: 800; color: #dc2626; margin-bottom: 25px; }}
      .features-row {{
        display: flex; gap: 30px; margin-bottom: 40px;
      }}
      .feat-box {{
        background: #f1f5f9; border: 2px solid #cbd5e1; border-radius: 12px; padding: 16px 32px;
        font-size: 22pt; font-weight: 800; color: #334155;
      }}
      .live-banner {{
        background: #ef4444; color: #fff; font-size: 28pt; font-weight: 900;
        padding: 12px 60px; border-radius: 8px; animation: pulse 1.5s infinite;
      }}
    </style></head><body>
      <div class='cover-card'>
        <div class='badge-top'>बिहार विज्ञान एवं प्रौद्योगिकी परिषद (BCST) • ऑनलाइन CBT परीक्षा</div>
        <div class='title-main'>सर सी.वी. रमन टैलेंट सर्च टेस्ट in Science</div>
        <div class='sub-title'>🔥 200 प्रश्न महामैराथन • कक्षा 6 से 12 (Special Live Set 2027-28)</div>
        <div class='features-row'>
          <div class='feat-box'>⏱️ परीक्षा समय: 180 मिनट</div>
          <div class='feat-box'>🎯 अंकन: +4 सही / -1 गलत</div>
          <div class='feat-box'>💡 शॉर्टकट ट्रिक्स व वैज्ञानिक तथ्य</div>
        </div>
        <div class='live-banner'>🔴 LIVE CBT TEST SESSION</div>
      </div>
    </body></html>"""

    # 2. Outro Page HTML
    outro_html = f"""<!DOCTYPE html>
    <html lang='hi'><head><meta charset='UTF-8'>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Nirmala+UI:wght@400;700;800;900&display=swap');
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        width: 1920px; height: 1080px; background: radial-gradient(circle at center, #1e293b, #090d16);
        display: flex; align-items: center; justify-content: center; font-family: 'Nirmala UI', sans-serif;
      }}
      .cover-card {{
        width: 1720px; height: 980px; background: #ffffff; border-radius: 16px;
        box-shadow: 0 35px 80px rgba(0,0,0,0.8); display: flex; flex-direction: column;
        align-items: center; justify-content: center; padding: 60px; text-align: center; border: 4px solid #16a34a;
      }}
      .badge-top {{
        background: #16a34a; color: #f8fafc; font-size: 26pt; font-weight: 900;
        padding: 12px 42px; border-radius: 50px; margin-bottom: 25px;
      }}
      .title-main {{ font-size: 54pt; font-weight: 900; color: #0f172a; margin-bottom: 20px; }}
      .sub-title {{ font-size: 32pt; font-weight: 800; color: #1e3a8a; margin-bottom: 35px; }}
      .stat-box {{
        background: #f0fdf4; border: 3px solid #86efac; border-radius: 16px; padding: 30px 60px;
        font-size: 30pt; font-weight: 900; color: #166534; margin-bottom: 35px;
      }}
      .footer-note {{ font-size: 24pt; font-weight: 800; color: #64748b; }}
    </style></head><body>
      <div class='cover-card'>
        <div class='badge-top'>🎉 महामैराथन सफलतापूर्वक संपन्न!</div>
        <div class='title-main'>शानदार प्रदर्शन साथियों!</div>
        <div class='sub-title'>पूरे 200 महत्वपूर्ण प्रश्न लाइव पूरे हो चुके हैं</div>
        <div class='stat-box'>🏆 अपना कुल स्कोर लाइव चैट में जरूर साझा करें!</div>
        <div class='footer-note'>सर सी.वी. रमन टैलेंट सर्च परीक्षा में आपकी विजय निश्चित है! ऑल द बेस्ट!</div>
      </div>
    </body></html>"""

    # 3. Continuous Scroll Paper HTML
    units_html = ""
    for q in QUESTIONS:
        num = q["num"]
        hi = q["hi"]
        en = q["en"]
        opts = q["options"]
        
        opt_blocks = ""
        for k in ["A", "B", "C", "D"]:
            val = opts.get(k, "")
            opt_blocks += f"""
            <div class='opt-item' id='opt_{num}_{k}'>
              <span class='opt-tag'>{k}</span>
              <span class='opt-text'>{val}</span>
              <span class='tick-mark' id='tick_{num}_{k}' style='display:none;'>✔</span>
            </div>"""
            
        units_html += f"""
        <div class='q-unit' id='qunit_{num}'>
          <div class='q-meta'>
            <span class='class-pill'>{q['class_tag']}</span>
            <span class='marks-pill'>सही: +4 अंक | गलत: -1 अंक</span>
          </div>
          <div class='q-text-hi'>{num}. {hi}</div>
          <div class='q-text-en'>{en}</div>
          <div class='options-grid'>{opt_blocks}</div>
          <div class='solution-slot' id='sol_{num}'></div>
        </div>"""

    continuous_html = f"""<!DOCTYPE html>
    <html lang='hi'><head><meta charset='UTF-8'>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Nirmala+UI:wght@400;700;800;900&display=swap');
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        width: 1920px; height: 1080px; background: #0b1329;
        display: flex; align-items: center; justify-content: center;
        font-family: 'Nirmala UI', sans-serif;
      }}
      .cbt-container {{
        width: 1780px; height: 1010px; background: #ffffff;
        border-radius: 12px; box-shadow: 0 30px 80px rgba(0,0,0,0.7);
        padding: 24px 50px 0 50px; display: flex; flex-direction: column; overflow: hidden;
      }}
      .header {{
        border-bottom: 2.5px solid #0f172a; padding-bottom: 12px; text-align: center; flex-shrink: 0;
      }}
      .header-l1 {{ font-size: 24pt; font-weight: 900; color: #1e3a8a; margin-bottom: 4px; }}
      .header-l2 {{ font-size: 19pt; font-weight: 800; color: #dc2626; margin-bottom: 6px; }}
      .header-l3 {{
        font-size: 16pt; font-weight: 700; color: #334155; display: flex; justify-content: space-between;
        background: #f1f5f9; padding: 6px 18px; border-radius: 6px; border: 1px solid #cbd5e1;
      }}
      .viewport {{
        flex: 1; overflow: hidden; position: relative; padding-top: 14px;
      }}
      .scroll-track {{
        display: flex; flex-direction: column;
      }}
      .q-unit {{
        height: 610px; flex-shrink: 0; border-bottom: 2.5px dashed #94a3b8; padding-bottom: 15px; margin-bottom: 25px;
      }}
      .q-meta {{
        display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;
      }}
      .class-pill {{
        background: #1d4ed8; color: #fff; font-size: 16pt; font-weight: 800;
        padding: 5px 18px; border-radius: 6px;
      }}
      .marks-pill {{
        background: #fef2f2; border: 1.5px solid #f87171; color: #b91c1c;
        font-size: 15pt; font-weight: 800; padding: 4px 14px; border-radius: 6px;
      }}
      .q-text-hi {{
        font-size: 27pt; font-weight: 900; color: #0f172a; line-height: 1.4; margin-bottom: 6px;
      }}
      .q-text-en {{
        font-size: 20pt; font-weight: 700; color: #475569; font-style: italic; line-height: 1.35; margin-bottom: 16px;
      }}
      .options-grid {{
        display: grid; grid-template-columns: 1fr 1fr; gap: 14px 40px; margin-bottom: 16px;
      }}
      .opt-item {{
        font-size: 24pt; font-weight: 700; color: #1e293b; display: flex; align-items: center;
        background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 10px; padding: 10px 18px;
      }}
      .opt-item.correct {{
        background: #ecfdf5; border-color: #16a34a; color: #15803d;
      }}
      .opt-tag {{
        font-weight: 900; background: #0f172a; color: #fff; border-radius: 6px;
        width: 38px; height: 38px; display: flex; align-items: center; justify-content: center;
        font-size: 18pt; margin-right: 14px; flex-shrink: 0;
      }}
      .opt-item.correct .opt-tag {{
        background: #16a34a;
      }}
      .tick-mark {{
        color: #16a34a; font-weight: 900; font-size: 32pt; margin-left: auto; line-height: 1;
      }}
      .solution-slot {{
        height: 115px; display: flex; align-items: center;
      }}
      .sol-box {{
        width: 100%; background: #f0fdf4; border: 2px solid #bbf7d0; border-left: 8px solid #16a34a;
        border-radius: 8px; padding: 10px 18px;
      }}
      .sol-title {{
        font-size: 16pt; font-weight: 800; color: #15803d; margin-bottom: 4px;
      }}
      .sol-body {{
        font-size: 20pt; font-weight: 800; color: #0f172a; line-height: 1.3;
      }}
    </style></head><body>
      <div class='cbt-container'>
        <div class='header'>
          <div class='header-l1'>बिहार विज्ञान एवं प्रौद्योगिकी परिषद (BCST) • पटना</div>
          <div class='header-l2'>सर सी.वी. रमन टैलेंट सर्च टेस्ट in Science 2027-28 • ऑनलाइन परीक्षा (CBT Mahamarathon)</div>
          <div class='header-l3'>
            <span>📚 कुल प्रश्न: 200 (कक्षा 6 से 12)</span>
            <span>⏱️ परीक्षा समय: 180:00 मिनट</span>
            <span>🎯 सही उत्तर: (+4) अंक | गलत उत्तर: (-1) अंक</span>
          </div>
        </div>
        <div class='viewport'>
          <div class='scroll-track' id='track'>
            {units_html}
          </div>
        </div>
      </div>
    </body></html>"""

    return intro_html, outro_html, continuous_html

def render_slides_with_playwright(intro_html, outro_html, continuous_html):
    print("\n--- 2. Rendering CBT Frames with Playwright ---")
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        # 1. Intro frame
        path_intro = os.path.join(FRAMES_DIR, "frame_intro.png")
        if not os.path.exists(path_intro):
            page.set_content(intro_html)
            page.screenshot(path=path_intro)
            
        # 2. Outro frame
        path_outro = os.path.join(FRAMES_DIR, "frame_outro.png")
        if not os.path.exists(path_outro):
            page.set_content(outro_html)
            page.screenshot(path=path_outro)

        # 3. Continuous Scroll Slides
        page.set_content(continuous_html)
        page.wait_for_timeout(400)

        UNIT_STEP = 635  # 610px height + 25px margin

        for i, q in enumerate(QUESTIONS):
            num = q["num"]
            ans = q["ans"]
            trick = q["sol_body"]

            path_q = os.path.join(FRAMES_DIR, f"frame_q_{num:03d}.png")
            path_ans = os.path.join(FRAMES_DIR, f"frame_ans_{num:03d}.png")

            # 1. Question Frame (Unsolved state)
            if not os.path.exists(path_q):
                page.screenshot(path=path_q)

            # 2. Answer Frame (Solved state)
            if not os.path.exists(path_ans):
                page.evaluate("""({num, ans, trick}) => {
                    const tick = document.getElementById('tick_' + num + '_' + ans);
                    if (tick) tick.style.display = 'inline';
                    const opt = document.getElementById('opt_' + num + '_' + ans);
                    if (opt) opt.classList.add('correct');
                    const sol = document.getElementById('sol_' + num);
                    if (sol) {
                        sol.innerHTML = `
                          <div class='sol-box'>
                            <div class='sol-title'>💡 वैज्ञानिक तथ्य एवं शॉर्टकट व्याख्या:</div>
                            <div class='sol-body'>` + trick + `</div>
                          </div>`;
                    }
                }""", {"num": num, "ans": ans, "trick": trick})
                page.wait_for_timeout(30)
                page.screenshot(path=path_ans)

            # 3. Transition scroll frame to next question
            if num < len(QUESTIONS):
                scroll_offset = num * UNIT_STEP
                path_scroll = os.path.join(FRAMES_DIR, f"frame_scroll_{num:03d}.png")
                page.evaluate(f"document.getElementById('track').style.transform = 'translateY(-{scroll_offset}px)';")
                page.wait_for_timeout(30)
                if not os.path.exists(path_scroll):
                    page.screenshot(path=path_scroll)

            if num % 25 == 0 or num == len(QUESTIONS):
                print(f"  Playwright rendered {num}/200 question slides...")

        browser.close()
    print("All slides and scroll frames rendered successfully!\n")

def mux_one_clip(cmd, clip_path):
    need_mux = not os.path.exists(clip_path)
    if not need_mux:
        for i, arg in enumerate(cmd):
            if arg == "-i" and i + 1 < len(cmd):
                inp = cmd[i + 1]
                if inp.endswith((".wav", ".mp3")) and os.path.exists(inp):
                    if os.path.getmtime(inp) > os.path.getmtime(clip_path):
                        need_mux = True
                        break
    if need_mux:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return clip_path

def mux_and_assemble_video():
    print("--- 3. Muxing Clips with FFmpeg in Parallel (8 Workers) ---")
    concat_list_path = os.path.join(BUILD_DIR, "concat.txt")
    final_video = os.path.join(OUT_DIR, "CV_Raman_200Q_Live_Mahamarathon_CBT.mp4")
    
    def find_audio(name):
        for ext in [".wav", ".mp3"]:
            p = os.path.join(AUDIO_DIR, f"{name}{ext}")
            if os.path.exists(p):
                return p
        return os.path.join(AUDIO_DIR, f"{name}.wav")

    tasks = []
    concat_order = []

    # 1. Intro Clip
    intro_img = os.path.join(FRAMES_DIR, "frame_intro.png")
    intro_audio = find_audio("speech_intro")
    intro_clip = os.path.join(CLIPS_DIR, "clip_intro.ts")
    cmd_intro = [
        FFMPEG, "-y", "-loop", "1", "-i", intro_img,
        "-i", intro_audio,
        "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
        "-shortest", "-preset", "ultrafast", intro_clip
    ]
    tasks.append((cmd_intro, intro_clip))
    concat_order.append(intro_clip)

    # 2. Questions 1 to 200
    for q in QUESTIONS:
        num = q["num"]
        img_q = os.path.join(FRAMES_DIR, f"frame_q_{num:03d}.png")
        img_ans = os.path.join(FRAMES_DIR, f"frame_ans_{num:03d}.png")
        scroll_img = os.path.join(FRAMES_DIR, f"frame_scroll_{num:03d}.png")

        audio_q = find_audio(f"speech_q_{num:03d}")
        audio_ans = find_audio(f"speech_ans_{num:03d}")

        clip_q = os.path.join(CLIPS_DIR, f"clip_q_{num:03d}.ts")
        clip_ans = os.path.join(CLIPS_DIR, f"clip_ans_{num:03d}.ts")

        # Question clip (with 4.5s natural thinking pause)
        cmd_q = [
            FFMPEG, "-y", "-loop", "1", "-i", img_q,
            "-i", audio_q,
            "-af", "apad=pad_dur=4.5",
            "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
            "-shortest", "-preset", "ultrafast", clip_q
        ]
        tasks.append((cmd_q, clip_q))
        concat_order.append(clip_q)

        # Answer clip (with 1.0s pause)
        cmd_ans = [
            FFMPEG, "-y", "-loop", "1", "-i", img_ans,
            "-i", audio_ans,
            "-af", "apad=pad_dur=1.0",
            "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
            "-shortest", "-preset", "ultrafast", clip_ans
        ]
        tasks.append((cmd_ans, clip_ans))
        concat_order.append(clip_ans)

        # Smooth paper scroll clip (0.4s)
        if num < len(QUESTIONS):
            scroll_clip = os.path.join(CLIPS_DIR, f"clip_scroll_{num:03d}.ts")
            cmd_scroll = [
                FFMPEG, "-y",
                "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
                "-loop", "1", "-i", scroll_img,
                "-t", "0.4",
                "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
                "-preset", "ultrafast", scroll_clip
            ]
            tasks.append((cmd_scroll, scroll_clip))
            concat_order.append(scroll_clip)

    # 3. Outro Clip (With Heartfelt Teacher Voiceover)
    outro_img = os.path.join(FRAMES_DIR, "frame_outro.png")
    outro_clip = os.path.join(CLIPS_DIR, "clip_outro.ts")
    outro_audio = find_audio("speech_outro")
    cmd_outro = [
        FFMPEG, "-y", "-loop", "1", "-i", outro_img,
        "-i", outro_audio,
        "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
        "-shortest", "-preset", "ultrafast", outro_clip
    ]
    tasks.append((cmd_outro, outro_clip))
    concat_order.append(outro_clip)

    # Run in parallel with 8 workers
    print(f"Executing {len(tasks)} video mux tasks across 8 threads...")
    completed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(mux_one_clip, cmd, path): path for cmd, path in tasks}
        for future in concurrent.futures.as_completed(futures):
            completed += 1
            if completed % 50 == 0 or completed == len(tasks):
                print(f"  Muxed {completed}/{len(tasks)} clips...")

    # Write concat.txt in precise sequential order
    with open(concat_list_path, "w", encoding="utf-8") as clist:
        for p in concat_order:
            clist.write(f"file '{p.replace(chr(92), '/')}'\n")

    print("\n--- 4. Final Fast Stream Concatenation ---")
    cmd_concat = [
        FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", concat_list_path,
        "-c", "copy", final_video
    ]
    res = subprocess.run(cmd_concat, capture_output=True, text=True)
    if res.returncode == 0:
        size_mb = os.path.getsize(final_video) / (1024 * 1024)
        print(f"SUCCESS! Final 200Q Mahamarathon Video (Year 2027-28) built at:\n{final_video} ({size_mb:.2f} MB)")
    else:
        print(f"Error during concatenation: {res.stderr}")

if __name__ == "__main__":
    t0 = time.time()
    intro_h, outro_h, cont_h = build_html_pages()
    render_slides_with_playwright(intro_h, outro_h, cont_h)
    mux_and_assemble_video()
    print(f"Entire build completed in {(time.time() - t0)/60:.2f} minutes.")
