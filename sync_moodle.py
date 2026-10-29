import urllib.request

# الرابط الخاص بك من المودل
MOODLE_URL = "https://moodle.alaqsa.edu.ps/calendar/export_execute.php?userid=98170&authtoken=424e45628e2332692e02432f61a91720bfae7424&preset_what=all&preset_time=recentupcoming"

def fetch_data():
    try:
        # السر لتخطي جدار الحماية (Cloudflare):
        # نقوم بإنشاء "ترويسة" (Header) تنتحل شخصية متصفح حقيقي (Google Chrome)
        # هكذا لن تعتقد خوادم الجامعة أننا "بوت" أو "بروكسي"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Accept': 'text/calendar'
        }
        
        # إرسال الطلب الخفي
        req = urllib.request.Request(MOODLE_URL, headers=headers)
        
        with urllib.request.urlopen(req) as response:
            ics_data = response.read().decode('utf-8')
            
            # إذا نجحنا وحصلنا على الملف، نحفظه كملف نصي
            if "BEGIN:VCALENDAR" in ics_data:
                # نحفظ البيانات في ملف ليقرأه ملف الـ HTML الخاص بلوحتك لاحقاً
                with open('moodle_data.ics', 'w', encoding='utf-8') as f:
                    f.write(ics_data)
                print("تم تخطي الحماية وسحب البيانات بنجاح!")
            else:
                print("فشل في السحب، قد يكون الرابط منتهي الصلاحية.")
                
    except Exception as e:
        print(f"حدث خطأ أثناء الاتصال: {e}")

if __name__ == "__main__":
    fetch_data()
