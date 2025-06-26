# recommender.py

import bz2
import pickle
import pandas as pd

# Load compressed pickle file
with bz2.BZ2File("recommender.pbz2", "rb") as f:
    data = pickle.load(f)

df = data['df']
cosine_sim = data['cosine_sim']
indices = data['indices']

# Recommendation function
def get_tag_recommendations(title, cosine_sim=cosine_sim):
    if title not in indices:
        return "Anime not found.", df

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Skip itself
    anime_indices = [i[0] for i in sim_scores]

    return df['name'].iloc[anime_indices].tolist(), df
