import streamlit as st
import google.generativeai as genai

# إعداد المفتاح
genai.configure(api_key="AIzaSyBXCxlQC4B5qRlLsNgwKmj1lfbjEDnA1-4")

# استخدام النموذج المحدث والمتاح للجميع
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("نظام الإدارة الذكي")

report = st.text_area("أدخل تقرير العمل اليومي:")

if st.button("تحليل وتوليد التوصيات"):
    if report:
        try:
            with st.spinner("جاري التحليل..."):
                # استخدام طريقة استدعاء أكثر عمومية
                response = model.generate_content(report)
                st.write(response.text)
        except Exception as e:
            st.error(f"خطأ: {e}")
            st.info("نصيحة: تأكد من أن مفتاح الـ API الخاص بك مفعل في Google AI Studio للنموذج gemini-1.5-flash")
    else:
        st.warning("يرجى كتابة التقرير أولاً.")
        
