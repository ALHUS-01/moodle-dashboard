import urllib.request
import json
import datetime

# ضع رابط المودل السري الخاص بك بين علامتي التنصيص أسفله
URL = "https://moodle.alaqsa.edu.ps/calendar/export_execute.php?userid=98170&authtoken=424e45628e2332692e02432f61a91720bfae7424&preset_what=all&preset_time=recentupcoming"

status_data = {
    "status": "success",
    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
    "error_msg": ""
}

try:
    # محاولة الاتصال بالمودل وسحب البيانات
    req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req, timeout=30)
    
    if response.getcode() == 200:
        with open("moodle_data.ics", "wb") as f:
            f.write(response.read())
    else:
        raise Exception(f"HTTP Error: {response.getcode()}")
        
except Exception as e:
    # في حال حدوث أي خطأ (حظر، انقطاع سيرفرات الجامعة، الخ)
    status_data["status"] = "error"
    status_data["error_msg"] = str(e)
    print(f"Error occurred: {e}")

# كتابة "تقرير الحالة" في ملف جديد ليقرأه موقعك
with open("sync_status.json", "w", encoding="utf-8") as f:
    json.dump(status_data, f)
