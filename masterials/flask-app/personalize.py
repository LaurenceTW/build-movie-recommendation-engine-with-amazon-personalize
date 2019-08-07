# import requests, boto3, json library to this project
import requests
import boto3
import json

personalizeRt = boto3.client('personalize-runtime','us-east-1')

# predict movie via Amazon Personalize
def predict_movie(user_id):
    # url list for store poster url
    url_list = []
    # name list for store movie name
    name_list = []

    # get recommendations via campaign Arn
    response = personalizeRt.get_recommendations(
        campaignArn = '<campaignArn>',
        userId = user_id)
    # setting your api key and use OMDB API to get poster
    url = '<omdbapi api url with api-key>'
    
    # list Recommended items
    print("Recommended items")
    for i in range(0,3):
        # get each item
        item = response['itemList'][i]
        print (item['itemId'])

        # reformat movie name, no ',' '()' , and replace '' with '+'
        search_name = item['itemId'].split(',')[0].split('(')[0].replace('\"','').replace(' ','+')
        print(search_name.rstrip('+'))  
        
        # setting movie url for api url
        movie_url = url + search_name.rstrip('+')

        # get response from OMDB API and get movie info 
        r = requests.get(movie_url)
        print('Url:',movie_url)
    
        print("Response:",r.text)    
        r_json = json.loads(r.text)
        print(r_json['Poster'])
        
        # add poster link to url_list, movie name to name_list
        url_list.append(r_json['Poster'])
        name_list.append(item['itemId'])
    
    return url_list,name_list