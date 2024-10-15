import streamlit as st
import  pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b44362af595759bb2227673e9d7dac7f'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500"+ data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_poster


movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.set_page_config(page_title="Movies Recommender",page_icon=':clapper:')



st.subheader("Welcome :wave:")
st.title(':red[Movie] Recommender System :clapper:')
st.write('Welcome, to this Content based movie recommender system.')
st.write("---")

selected_movie_name = st.selectbox(
    "Select your desired movie",
    movies['title'].values,

)


if st.button("Recommend"):
    st.write("---")
    names,poster=recommend(selected_movie_name)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])

    col4,col5,col6= st.columns(3)
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
    with col6:
        st.text(names[5])
        st.image(poster[5])

