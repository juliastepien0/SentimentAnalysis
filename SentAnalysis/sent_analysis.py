"""
Executing this function requests sentiment analysis data from the model and returns
label and score stored as dictionary.
"""
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
from ibm_cloud_sdk_core.api_exception import ApiException

nlu = NaturalLanguageUnderstandingV1(version='2024-12-04')

def sentiment_analyzer(text_to_analyse):
    """
    :param text_to_analyse:
    :return: dictionary of label and score
    """
    response = nlu.analyze(text=text_to_analyse,
                           features=Features(sentiment=SentimentOptions())).get_result()
    if response.status_code == 200:
        label = response['sentiment']['document']['label']
        score = response['sentiment']['document']['score']
    elif response.status_code == 400 or response.status_code == 500:
        label = None
        score = None
    print(response.status_code)
    response_dict = { 'label': label, 'score': score }
    return response_dict
