import urllib.request
import json
import datetime

# ضع رابط المودل السري الخاص بك هنا
URL = "https://moodle.alaqsa.edu.ps/calendar/export_execute.php?userid=98170&authtoken=424e45628e2332692e02432f61a91720bfae7424&preset_what=all&preset_time=recentupcoming"

status_data = {
    "status": "success",
    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
    "error_msg": ""
}

try:
    req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req, timeout=30)
    
    if response.getcode() == 200:
        with open("moodle_data.ics", "wb") as f:
            f.write(response.read())
    else:
        raise Exception(f"HTTP Error: {response.getcode()}")
        
except Exception as e:
    status_data["status"] = "error"
    status_data["error_msg"] = str(e)
    print(f"Error: {e}")

# حفظ ملف الحالة بشكل إجباري
with open("sync_status.json", "w", encoding="utf-8") as f:
    json.dump(status_data, f)
