import pandas as pd
import os

# مسار ملف البيانات داخل حاوية الـ Docker
data_path = '/app/data/dataset.csv'

print("=== بدء معالجة بيانات Big Data داخل الحاوية ===")

if os.path.exists(data_path):
    # قراءة البيانات باستخدام pandas
    df = pd.read_csv(data_path)
    print(f"تم بنجاح تحميل البيانات! عدد السطور: {df.shape[0]}, عدد الأعمدة: {df.shape[1]}")
    print("\nعينة من أعمدة البيانات:")
    print(df.columns.tolist())
    print("\nمعلومات سريعة حول البيانات:")
    print(df.info())
else:
    print(f"خطأ: لم يتم العثور على ملف البيانات في المسار {data_path}")

print("=== تم الانتهاء بنجاح ===")

# --- إضافة هذا الجزء لإبقاء الحاوية نشطة بشكل دائم ---
print("الحاوية في حالة انتظار وتعمل بنجاح (Running)...")
while True:
    time.sleep(60)