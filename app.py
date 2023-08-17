import streamlit as st
import pickle
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer

ps=PorterStemmer()


def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)

    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text=y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)        




tfidf=pickle.load(open('TfidfVectorizer.pkl','rb'))
model=pickle.load(open('movi.pkl','rb'))

st.title("Movie Review-Sentiment Analysis Model")
review=st.text_area("give your review :)")
if st.button('Predict'):
    

  
    clean=transform_text(review)
    vector_input=tfidf.transform([clean]).toarray()
    result=model.predict(vector_input)[0]

    if result==1:
        st.header("Positive :heart_eyes:")
        st.text("Maaza aa gaya")
    else :
        st.header("negative :rage:")
        st.text("Paisa barbaad")
        
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="white",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
       
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
       
        
    
        
              
        link("https://www.linkedin.com/in/adnan-patel-b78ba521b/", "@adnanpatel"),
        br(),
        
    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()