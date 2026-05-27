import streamlit as st
import google.generativeai as genai

# إعداد المحرك بالمفتاح مباشرة
genai.configure(api_key="AIzaSyBXCxlQC4B5qRlLsNgwKmj1lfbjEDnA1-4")
model = genai.GenerativeModel('gemini-1.0-pro')


st.title("نظام الإدارة الذكي")

report = st.text_area("أدخل تقرير العمل اليومي:")

if st.button("تحليل وتوليد التوصيات"):
    if report:
        try:
            with st.spinner("جاري التحليل..."):
                response = model.generate_content(f"حلل هذا التقرير: {report}")
                st.write(response.text)
        except Exception as e:
            st.error(f"خطأ في الاتصال: {e}")
    else:
        st.warning("يرجى كتابة التقرير.")
      
