import streamlit as st
import pickle 
import pandas as pd 


def recommend(book):
    book_index = df[df['Book']==book].index[0]
    distances = similarity[book_index]
    book_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]


    recommend_books = [] 
    for i in book_list:
        recommend_books.append(df.iloc[i[0]].Book)
    return recommend_books

book_dict = pickle.load(open('book_dict.pkl','rb'))
df = pd.DataFrame(book_dict)


similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Book Recommendation System')

selected_book_name = st.selectbox(
    'Select the movie to be recommended:',
    df['Book'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_book_name)
    for i in recommendations:
        st.write(i)