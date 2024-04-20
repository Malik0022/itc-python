## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR get_types_counts() FUNCTION GOES HERE ###
def get_types_counts(d):
    
    result = {}
    for new_dict in d:
        result[new_dict] = len(d[new_dict])
    return result
    
#### End OF MARKER

### YOUR CODE FOR get_types() FUNCTION GOES HERE ###
def get_types(d):
    
    # for key in d.keys():
    #     key_list = list(key)
    # return key_list

    key = list(d.keys())
    return key

#### End OF MARKER

### YOUR CODE FOR get_author_count() FUNCTION GOES HERE ###
def get_author_count(d,authorname,item=None):


    counter = 0
    for dict_1 in d.values():
        for item in dict_1:
            if item["author"]["username"] == authorname:
                counter += 1
        
    return counter

#### End OF MARKER
if __name__ == '__main__':
    d = {
            "articles": [{
                "slug": "how-to-train-your-mule",
                "title": "How to train your mule",
                "description": "Ever wonder how?",
                "body": "It takes a Jacobian",
                "tagList": ["mules", "training"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 0,
                "author": {
                  "username": "jake",
                  "bio": "I work at statefarm",
                  "following": False
                }
            }, {
                "slug": "and another article",
                "body": "I'm getting bored",
                "tagList": ["bored", "article"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 20,
                "author": {
                  "username": "cap",
                  "following": True
                }
            }],
            "tweets": [{
                "body": "See my article on training mules.",
                "author": {
                  "username": "jake"
                }
            }]
        }

    print (get_types(d))
    print (get_types_counts(d))
    print (get_author_count(d, 'cap'))
    print (get_author_count(d, 'jake', ['articles', 'tweets']))
