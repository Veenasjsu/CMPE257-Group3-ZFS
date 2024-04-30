import json
import numpy as np

from match_with_embedding import get_embedding
from retrieval import retrieval

def vectorize(dict):
    vec = []
    for value in dict.values():
        try:
            vec.append(get_embedding(value))
        except:
            print(f"Error: {value}")
            exit(1)
    return np.array(vec)

def euclidean_distance(v1, v2):
    return np.linalg.norm(v1 - v2)

def manhattan_distance(v1, v2):
    return np.sum(np.abs(v1 - v2))

def distance(post, usr_query):
    post_dict = json.loads(retrieval(post))
    usr_dict = json.loads(retrieval(usr_query))
    post_vec = vectorize(post_dict)
    usr_vec = vectorize(usr_dict)
    return manhattan_distance(post_vec, usr_vec)

def distance_bk(post, usr_query):
    post_vec = np.array(get_embedding(post))
    usr_vec = np.array(get_embedding(usr_query))
    return manhattan_distance(post_vec, usr_vec)

def recommendation_list(posts, usr_query, number):
    results = []
    for i in range(len(posts)):
        dist = distance(posts[i], usr_query)
        results.append((i, dist))
    
    results = sorted(results, key=lambda item : item[1], reverse=False)
    print(results)
    return [item[0] for item in results][:number]
