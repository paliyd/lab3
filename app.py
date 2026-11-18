import streamlit as st
import pandas as pd

st.set_page_config(page_title="Фото та відео", page_icon="📁")

st.title("Будемо завантажувати фото та відео")
st.write("Давай спробуємо!")

# --- Фото ---
photo = st.file_uploader("Оберіть фото", type=["jpg", "jpeg", "png"])
if photo is not None:
    st.image(photo, caption=photo.name, use_container_width=True)
    st.success(f"Фото «{photo.name}» завантажено ({photo.size / 1024:.1f} КБ)")

# --- Відео ---
video = st.file_uploader("Оберіть відео", type=["mp4", "mov", "avi"])
if video is not None:
    st.video(video)
    st.success(f"Відео «{video.name}» завантажено ({video.size / 1024 / 1024:.2f} МБ)")

# --- Excel ---
table = st.file_uploader("Оберіть таблицю Excel", type=["xlsx", "xls"])
if table is not None:
    try:
        df = pd.read_excel(table)
        st.success(f"Таблицю «{table.name}» завантажено: {df.shape[0]} рядків, {df.shape[1]} стовпців")
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Не вдалося прочитати файл: {e}")
