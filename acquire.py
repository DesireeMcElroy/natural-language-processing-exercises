from requests import get
from bs4 import BeautifulSoup
import os

import pandas as pd
import numpy as np


def get_blog_articles(url):
    '''
    This function takes in a url and pull the necessary elements off the website
    then creates a dictionary with those elements
    '''

    # create an empty dictionary to append to
    blog_dict = {}
    
    # fetch the data
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    
    # pull the elements from the soup
    article = soup.find('div', class_='jupiterx-post-content') # pulling body of text
    title = soup.find('h1', class_='jupiterx-post-title') # pulling title as text
    
    # append the elements to the dictionary
    blog_dict = {'title': title.text,
                'content': article.text}
    
    # return dictionary
    return blog_dict


def get_article(article, category):
    '''
    This function takes in an article and category and pulls
    the elements from the article of that category to be
    utilized within another function
    '''
    # Attribute selector
    title = article.select("[itemprop='headline']")[0].text
    
    # article body
    content = article.select("[itemprop='articleBody']")[0].text
    
    output = {}
    output["title"] = title
    output["content"] = content
    output["category"] = category
    
    return output


def get_articles(category, base ="https://inshorts.com/en/read/"):
    """
    This function takes in a category as a string. Category must be an available category in inshorts
    Returns a list of dictionaries where each dictionary represents a single inshort article
    """
    
    # We concatenate our base_url with the category
    url = base + category
    
    # Set the headers
    headers = {"User-Agent": "Mozilla/4.5 (compatible; HTTrack 3.0x; Windows 98)"}

    # Get the http response object from the server
    response = get(url, headers=headers)

    # Make soup out of the raw html
    soup = BeautifulSoup(response.text)
    
    # Ignore everything, focusing only on the news cards
    articles = soup.select(".news-card")
    
    output = []
    
    # Iterate through every article tag/soup 
    for article in articles:
        
        # Returns a dictionary of the article's title, body, and category
        article_data = get_article(article, category) 
        
        # Append the dictionary to the list
        output.append(article_data)
    
    # Return the list of dictionaries
    return output


def get_all_news_articles(categories):
    """
    Takes in a list of categories where the category is part of the URL pattern on inshorts
    Returns a dataframe of every article from every category listed
    Each row in the dataframe is a single article
    """
    all_inshorts = []

    for category in categories:
        all_category_articles = get_articles(category)
        all_inshorts = all_inshorts + all_category_articles

    df = pd.DataFrame(all_inshorts)
    return df