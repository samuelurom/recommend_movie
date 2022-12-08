# Recommend movies to watch based on the word vector similarity of movies descriptions using spaCy

# import spaCy
import spacy


def recommended_movies(movie_description):

    """
    Function returns recommended movies for a user based on the description of movie they have watched
    :param: movie_description
    :return: recommended
    """

    # Load the medium-sized English language model
    nlp = spacy.load('en_core_web_md')

    # Empty list to store movies and similarity to movie_description param
    similar_movies = []

    # Read external file with movies and descriptions
    with open('movies.txt', 'r') as f:

        for line in f:
            # For loop splits each line into list containing movie title and description
            # Extracts description, removes new line string and creates new nlp object
            title_description = line.split(' :')
            description = title_description[1].replace('\n', '')

            # Add movie to similar_movies list with similarity score
            # by comparing movie_description param and description nlp objects
            similar_movies.append({
                'title': title_description[0],
                'description': description,
                'similarity': nlp(movie_description).similarity(nlp(description))
            })

    # Sort similar_movies list in descending order by similarity using lambda function - Ref: https://shorturl.at/hAET5
    sorted_similar_movies = sorted(similar_movies, key=lambda k: k['similarity'], reverse=True)

    # Get the most similar movie from the sorted list
    recommended = f"Title:        {sorted_similar_movies[0]['title']} \nDescription:  {sorted_similar_movies[0]['description']}"

    # Return the recommended movie
    return recommended


# Current movie
planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, " \
              "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live " \
              "in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a " \
              "gladiator. "

print("Recommended Movies \n————————————————————————————————")

# Call recommended_movies function and pass in a movie description
print(recommended_movies(planet_hulk))
