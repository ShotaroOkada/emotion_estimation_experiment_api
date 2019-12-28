from ibm_watson import NaturalLanguageUnderstandingV1
from src.drivers.nlu.config import Natural_language_understanding_api_key, Natural_language_understanding_url

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    iam_apikey=Natural_language_understanding_api_key,
    url=Natural_language_understanding_url
)
