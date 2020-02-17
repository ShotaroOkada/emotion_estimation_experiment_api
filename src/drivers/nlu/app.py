from ibm_watson import NaturalLanguageUnderstandingV1
from src.drivers.nlu.config import Natural_language_understanding_api_key, Natural_language_understanding_url
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator(Natural_language_understanding_api_key)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)
natural_language_understanding.set_service_url(
    Natural_language_understanding_url)
