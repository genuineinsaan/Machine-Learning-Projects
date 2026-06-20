from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

movies = pickle.load(
    open('movie_list.pkl', 'rb')
)

similarity = pickle.load(
    open('similarity.pkl', 'rb')
)


def recommend(movie):

    movie_index = movies[
        movies['title'] == movie
    ].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movies_list:
        recommendations.append(
            movies.iloc[i[0]].title
        )

    return recommendations


@app.route('/')
def home():
    return render_template(
        'index.html',
        movie_list=movies['title'].values
    )


@app.route('/recommend', methods=['POST'])
def recommendation():

    movie = request.form['movie']

    recommended_movies = recommend(movie)

    return render_template(
        'result.html',
        movie=movie,
        recommendations=recommended_movies
    )


if __name__ == '__main__':
    app.run(debug=True)