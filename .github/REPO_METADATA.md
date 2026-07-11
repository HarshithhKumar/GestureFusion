# Repository metadata for GitHub "About" panel

Use these fields to populate the repository About section on GitHub (Settings → General → About).

Description

End-to-end gesture-interaction prototype combining ESP32 sensors, MATLAB processing, and Python ML training.

Website

https://your-website.example.com

Topics (comma-separated)

gesture-recognition, embedded-music, esp32, signal-processing, machine-learning, demo

---

# Quick commands (optional)

If you have the `gh` CLI installed and are an admin on this repository, you can set the description and homepage from the command line (replace `OWNER/REPO`):

```bash
# Set description and homepage
gh repo edit OWNER/REPO --description "End-to-end gesture-interaction prototype combining ESP32 sensors, MATLAB processing, and Python ML training." --homepage "https://your-website.example.com"

# Add topics (example; call once per topic or adapt to add multiple)
gh api -X PUT repos/OWNER/REPO/topics -f names='["gesture-recognition","embedded-music","esp32","signal-processing","machine-learning","demo"]'
```
