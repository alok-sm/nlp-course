from featurefunctions import get_functions
from getcomments import get_comments_fvs
import json

function_vector = get_functions()
comments, fvs = get_comments_fvs()

vectors = [[function(comment) for function in function_vector] for comment in comments]

json.dump(vectors, open("vectors.txt", "w"))
json.dump(fvs, open("fv.txt", "w"))

print len(fvs)
print len(vectors)
