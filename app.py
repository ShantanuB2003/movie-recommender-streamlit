# import pickle
# import streamlit as st
# import pandas as pd

# def recommend(movie):
#     index = movie[movie['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

#     recommended_movies = []

#     for i in distances[1:6]:
#         recommended_movies.append(movie.iloc[i[0]].title)

#     return recommended_movies


# st.title('Movie Recommender System')

# movies_list = pickle.load(open('movies.pkl','rb'))

# similarity = pickle.load(open('similarity.pkl','rb'))

# movies_list= movies_list['title'].values

# selected_movie_name = st.selectbox(
#     'How would you like to be contacted?',
#     movies_list)

# if st.button("Recommend"):

#     recommendations = recommend(selected_movie_name)

#     for i in recommendations:
#         st.write(selected_movie_name)







import pickle
import streamlit as st

# Load pickles
movies = pickle.load(open('data.pkl', 'rb'))   # MUST be DataFrame
similarity = pickle.load(open('compressed_similarity.pkl', 'rb'))

def recommend(movie_name):
    index = data[data['title'] == movie_name].index[0]

    distances = sorted(
        list(enumerate(compressed_similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []
    for i in distances[1:6]:
        movie_id = i[0]

        #fetch poster from api

        


        recommended_movies.append(data.iloc[i[0]]['title'])

    return recommended_movies

st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a movie",
    data['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    if recommendations:
        st.subheader("Recommended Movies:")
        for movie in recommendations:
            st.write(movie)
    else:

        st.warning("No recommendations found.")




