# Coding with Sudhir - Master Video Production Tracker

Updated: 2026-11-27
Master Rules & Operating System: [CHANNEL_MASTER_OPERATING_SYSTEM.md](file:///C:/Users/sudhi/Desktop/study/CHANNEL_MASTER_OPERATING_SYSTEM.md)

## 📊 Daily Production Log (Channel Rule: Quality > Quantity)
- **Today's Date:** 2026-11-27
- **Videos Completed Today:** 1 Video (Go 1.27.4 on Windows 11)
  1. `How to Download and Install Go on Windows 11 (v1.27.4)` (16:9 Long 2m 20s + 9:16 Short 46.5s) - 🚀 Ready for Upload
- **Yesterday's Date (2026-11-26):** 3 Videos (Bun 1.4.5, Ruby 4.0.10, PHP 8.6.0) - ✅ Uploaded
  1. `How to Download and Install Bun on Windows 11 (v1.4.5)` (16:9 Long 1m 26s + 9:16 Short 46.5s) - ✅ Uploaded
  2. `How to Download and Install Ruby on Windows 11 (v4.0.10)` (16:9 Long 2m 56s + 9:16 Short 46.5s) - ✅ Uploaded
  3. `How to Download and Install PHP on Windows 11 (v8.6.0)` (16:9 Long 2m 16s + 9:16 Short 46.5s) - ✅ Uploaded
- **2026-11-25:** 2 Videos (XAMPP on Windows 11 & Port 3306 Fix) - ✅ Uploaded
- **2026-11-24:** 4 Videos (WinRAR 7.23, 7-Zip 26.06, VirtualBox 7.2.22 & Ollama 0.40.18) - ✅ Uploaded
- **Yesterday's Date (2026-11-23):** 1 Video
  1. `How to Download and Install Typing Master 12 on Windows 11` (16:9 Long + 9:16 Short) - ✅ Uploaded
- **Yesterday's Date (2026-11-22):** 2 Videos
  1. `How to Reset Forgotten MySQL Root Password in Windows 11` (16:9 Long + 9:16 Short) - ✅ Uploaded
  2. `Fix 'Access Denied for user root@localhost' (MySQL Error 1045) in MySQL Workbench` (16:9 Long + 9:16 Short) - ✅ Uploaded
- **Yesterday's Date (2026-11-21):** 5 Videos
  1. `Fix 'running scripts is disabled' in Windows 11 PowerShell` (16:9 + 9:16) - ✅ Uploaded
  2. `How to Install MySQL Server and Workbench on Windows 11` (16:9 + 9:16) - ✅ Uploaded
  3. `How to Setup Python in VS Code on Windows 11` (16:9 + 9:16) - ✅ Uploaded
  4. `How to Connect Python to MySQL in VS Code` (16:9 + 9:16) - ✅ Uploaded
  5. `How to Connect MySQL in Java / NetBeans using JDBC` (16:9 + 9:16) - ✅ Uploaded
- **Yesterday's Date (2026-11-20):** 1 Video
  1. `Gemini 4 Neon: New #1 on Models Engineering Index` (16:9 + 9:16) - ✅ Uploaded
- **2026-11-19:** 3 Videos
  1. `Fix 'irm' is not recognized in Windows 11` (16:9 + 9:16) - ✅ Uploaded
  2. `How to Run DeepSeek-R1 Locally on Windows 11` (16:9 + 9:16) - ✅ Uploaded
  3. `Fix 'npm' is not recognized in Windows 11` (16:9 + 9:16) - ✅ Uploaded
- **Daily Status:** 🎯 Goal Achieved (Daily consistency maintained with high-search evergreen fix!).

---

## 🧭 Production Strategy & Trigger Rules
1. **Priority #1 (Breaking / Day-0 News):** Only record when Tech Radar Bot triggers a new CVE, critical security bug, or major new AI tool release with zero/low competition.
2. **Priority #2 (Fallback / Quiet Days):** If a day passes with NO fresh breaking news, pick 1 high-demand error fix from the evergreen backlog so daily upload rhythm stays active.
3. **Priority #3 (YouTube Shopping & Product Tagging):**
   - Product tagging must be done directly inside YouTube Studio ("Shopping" / "Earn" tab).
   - **STRICT RULE:** NEVER add placeholder/fake links (`amzn.to/example...`) in video descriptions. Only include official software/documentation links unless user explicitly provides actual affiliate links.
4. **Priority #4 (PERMANENT STRICT SHORTS STANDARD - ZERO EXPERIMENTATION):**
   - **Duration:** Strictly 45.0s to 50.0s (NEVER > 60s, so YouTube mobile app always recognizes as Short).
   - **Pixel Aspect Ratio (SAR):** Always force `setsar=1:1` and `DAR 9:16` (`1080x1920`). Never let ffmpeg output non-1:1 SAR.
   - **Background:** `scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5,setsar=1:1[bg]`.
   - **Foreground:** `scale=1080:-1,setsar=1:1[fg]` placed at `overlay=0:(1920-h)/2`.
   - **Top Banner:** `y=180:w=1080:h=310:color=black@0.75` (White 52px, Neon Green 66px, Yellow 40px). NEVER put year in banner.
   - **Bottom Banner:** `y=1420:w=1080:h=230:color=black@0.75` (Yellow 52px, White 36px).

---

## 1. Completed & Uploaded Videos
| # | Video Topic | Type | Format | Voice | Status |
|---|---|---|---|---|---|
| 1 | Fix 'python' is not recognized in Windows 11 | Error Fix | 16:9 Long + 9:16 Short | PrabhatNeural (English) | ✅ Uploaded |
| 2 | Fix 'pip' is not recognized in Windows 11 | Error Fix | 16:9 Long + 9:16 Short | PrabhatNeural (English) | ✅ Uploaded |
| 3 | Java4Shell (CVE-2026-114938) 10s Alert | Critical Bug Alert | 9:16 Short (Gemini AI) | English Urgent Tone | ✅ Live & Ranking in Search! |
| 4 | How to Install Java JDK & Fix 'java' Not Recognized | Install + Error Fix | 16:9 Long + 9:16 Short | PrabhatNeural (English) | ✅ Uploaded |
| 5 | Java4Shell (CVE-2026-114938) Full Fix Guide | Security Vulnerability | 16:9 Long (1080p) | PrabhatNeural (English) | ✅ Uploaded |
| 6 | How to Install Apache NetBeans 32 on Windows 11 | Version-Wise Install | 16:9 Long (1080p) | PrabhatNeural (English) | ✅ Uploaded |
| 7 | Critical Git Security Bug (CVE-2026-111760) Patch | Security Vulnerability | 16:9 Long + 9:16 Short | PrabhatNeural (English) | ✅ Uploaded |
| 8 | Fix 'irm' is not recognized in Windows 11 | Error Fix | 16:9 Long + 9:16 Short | PrabhatNeural (English) | ✅ Uploaded |
| 9 | How to Run DeepSeek-R1 Locally on Windows 11 (Ollama) | Viral Local AI Tool | 16:9 Long + 9:16 Short | PrabhatNeural (English) | ✅ Uploaded |
| 10 | Fix 'npm' is not recognized in Windows 11 | Error Fix | 16:9 Long + 9:16 Short | PrabhatNeural (English) | ✅ Uploaded |
| 11 | Gemini 4 Neon: New #1 on Models Engineering Index | Trending AI / Benchmark | 16:9 Long + 9:16 Short | PrabhatNeural (English) | ✅ Uploaded |
| 12 | Fix 'running scripts is disabled' in Windows 11 PowerShell | Error Fix / Developer Setup | 16:9 Long + 9:16 Short | PrabhatNeural (English) | ✅ Uploaded |
| 13 | How to Install MySQL Server & Workbench on Windows 11 | Developer Database Setup | 16:9 Long + 9:16 Short | PrabhatNeural (English) | ✅ Uploaded |
| 14 | How to Setup Python in VS Code on Windows 11 | IDE & Python Environment | 16:9 Long + 9:16 Short | PrabhatNeural (English) | ✅ Uploaded |
| 15 | How to Connect Python to MySQL in VS Code | Database & Python Connection | 16:9 Long + 9:16 Short | PrabhatNeural (English) | ✅ Uploaded |
| 16 | How to Connect MySQL in Java / NetBeans using JDBC | Database & Java JDBC | 16:9 Long (6m 08s) + 9:16 Short (48.0s) | PrabhatNeural (English) | ✅ Uploaded |
| 17 | Critical Ghostscript Zero-Day (CVE-2026-125396) Patch | Day-0 Security Alert (RCE) | 16:9 Long (48.0s) | PrabhatNeural (English) | ✅ Uploaded |
| 18 | How to Reset Forgotten MySQL Root Password in Windows 11 | Password Recovery | 16:9 Long (3m 49s) + 9:16 Short (68.0s) | PrabhatNeural (English) | ✅ Uploaded |
| 19 | Fix 'Access Denied for user root@localhost' (MySQL Error 1045) | Error 1045 Fix | 16:9 Long (3m 10s) + 9:16 Short (66.5s) | PrabhatNeural (English) | ✅ Uploaded |
| 20 | How to Download and Install Typing Master 12 on Windows 11 | Software Installation | 16:9 Long (2m 33s) + 9:16 Short (46.3s) | PrabhatNeural (English) | ✅ Uploaded |
| 21 | How to Download and Install WinRAR 7.23 on Windows 11 | Software Installation | 16:9 Long (1m 07s) + 9:16 Short (46.5s) | PrabhatNeural (English) | ✅ Uploaded |
| 22 | How to Download and Install 7-Zip 26.06 on Windows 11 | Software Installation | 16:9 Long (1m 01s) + 9:16 Short (46.5s) | PrabhatNeural (English) | ✅ Uploaded |
| 23 | How to Download and Install VirtualBox 7.2.22 on Windows 11 | Software Installation | 16:9 Long (2m 00s) + 9:16 Short (46.5s) | PrabhatNeural (English) | ✅ Uploaded |
| 24 | How to Install Ollama 0.40.18 on Windows 11 | AI Tool / Local LLM | 16:9 Long (3m 26s) + 9:16 Short (46.5s) | PrabhatNeural (English) | ✅ Uploaded |
| 25 | How to Download and Install XAMPP on Windows 11 | Web Server / PHP & MySQL | 16:9 Long (2m 20s) + 9:16 Short (46.5s) | PrabhatNeural (English) | ✅ Uploaded |
| 26 | Fix XAMPP MySQL Error: Port 3306 in use by Unable to open process | Error Fix / Web Server | 16:9 Long (59.9s) + 9:16 Short (46.5s) | PrabhatNeural (English) | ✅ Uploaded |
| 27 | How to Download and Install Bun on Windows 11 (v1.4.5) | JavaScript Runtime / Dev Tools | 16:9 Long (1m 26s) + 9:16 Short (46.5s) | PrabhatNeural (English) | ✅ Uploaded |
| 28 | How to Download and Install Ruby on Windows 11 (v4.0.10) | Programming Language / Dev Tools | 16:9 Long (2m 56s) + 9:16 Short (46.5s) | PrabhatNeural (English) | ✅ Uploaded |
| 29 | How to Download and Install PHP on Windows 11 (v8.6.0) | Backend / Web Development | 16:9 Long (2m 16s) + 9:16 Short (46.5s) | PrabhatNeural (English) | ✅ Uploaded |
| 30 | How to Download and Install Go on Windows 11 (v1.27.4) | Programming Language / Dev Tools | 16:9 Long (2m 20s) + 9:16 Short (46.5s) | PrabhatNeural (English) | 🚀 Ready for Upload |
| 31 | How to Download and Install PostgreSQL 19 on Windows 11 (with pgAdmin 4) | Relational Database / Dev Tools | 16:9 Long (2m 29s) + 9:16 Short (49.3s) | PrabhatNeural (English) | 🚀 Ready for Upload |

---

## 2. Active Production Queue (Ranked by Competition & Search Demand)

### 🥇 Priority 1: Google Genie 4: World-Building AI (Day 0 Breaking News)
- **Category:** Viral Generative AI
- **Search Demand:** Surging (Just launched by Google DeepMind!)
- **YouTube Competition:** Very Low (First-mover advantage)
- **Target Duration:** 2.5 Minutes (Screen Recording)

### 🥈 Priority 2: How to Install MySQL 9.2 Community Server on Windows 11
- **Category:** Version-Wise Install / High Search Demand
- **Search Demand:** High (Evergreen developer setup)
- **YouTube Competition:** Low for latest 9.2 version
- **Target Duration:** 2 Minutes (Screen Recording)

### 🥉 Priority 3: SolveIt by Fast.ai Walkthrough
- **Category:** Trending AI Workspace
- **Search Demand:** Niche / Medium
- **YouTube Competition:** Very Low (First-mover advantage)
- **Target Duration:** 2 Minutes
