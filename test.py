from fpdf import FPDF
import streamlit as st
import openai
import os
import pandas as pd
import time
openai.api_key = "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"
def get_completion(prompt, model="gpt-3.5-turbo"):

    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(

    model=model,

    messages=messages,

    temperature=0,

)
    return response.choices[0].message["content"]

response = ""
def generate():
    return get_completion(prompt=f'make a assignment on {topic} for class {grade} of {questions} questions that is {level}')

#Layout
st.title("Assignment Generator")
board = st.selectbox("Choose Your Board :- ",("ICSE","CBSE","IGSCE"))
grade = st.selectbox("Choose Your Class :- ",("1",'2','3','4','5','6','7','8','9','10','11','12'))
topic = st.text_input("Choose Your Topic :- ")
questions = st.number_input("Number of Questions :- ", min_value=1,max_value=10)
special = st.text_input("Any Special Requirements? :- ")
level = st.selectbox("Choose Level :- ",("Easy","Moderate","Hard"))
button = st.button("Generate!", on_click= None)

if(button==True):
    response = generate()
    print(response)
    pdf = FPDF(unit="mm",orientation="portrait")

    pdf.add_page()
    pdf.set_font('helvetica','',12)

    pdf.write(10, response)
    pdf.output('testPdf.pdf')
    # st.text(response)
    with open('testPdf.pdf', 'rb') as f:
        st.download_button('Download PDF', f, file_name=f'Class{grade}_Assignment_{topic}.pdf')

