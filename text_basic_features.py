import json
from pathlib import Path

import nltk
from nltk.tokenize import word_tokenize
from textstat import wiener_sachtextformel
from textblob_de import TextBlobDE as TextBlob
from germansentiment import SentimentModel

from src.utils.files import all_files_in_directory


nltk.download('punkt_tab')
german_sentiment_model = SentimentModel()
SENTIMENTS_TO_NUMBERS = {'positive': 1, 'neutral': 0, 'negative': -1}


def tokenized_text(text: str) -> list:
    return word_tokenize(text)

def simple_quantitative_features(tokenized_interaction_text:str, interaction_lengths: list, complexities: list, polarities: list, subjectivities: list, sentiments: list) -> dict:
    interaction_lengths.append(len(tokenized_interaction_text))
    tokenized_interaction_text = ' '.join(tokenized_interaction_text)
    complexities.append(wiener_sachtextformel(tokenized_interaction_text, 1)) # A value of 4 means very easy text, whereas 15 means very difficult text. Check https://de.wikipedia.org/wiki/Lesbarkeitsindex#Wiener_Sachtextformel
    blob = TextBlob(tokenized_interaction_text)
    polarity = blob.sentiment.polarity # [-1.0, 1.0]
    subjectivity = blob.sentiment.subjectivity # [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
    polarities.append(polarity)
    subjectivities.append(subjectivity)
    curr_sentiments = [SENTIMENTS_TO_NUMBERS[s] for s in german_sentiment_model.predict_sentiment(tokenized_interaction_text)]
    sentiment = sum(curr_sentiments) / len(curr_sentiments)
    sentiment = round(sentiment, 2)
    sentiments.append(sentiment)

    return interaction_lengths, complexities, polarities, subjectivities, sentiments


# Linear features extraction -> counting length of chat history, number of interactions, etc.
data_dir = 'data'
all_chat_history_files = all_files_in_directory(data_dir, extensions_to_include=['.json'])

for f in all_chat_history_files:
    if 'chat_history' in f:
        print(f)
        p = Path(f)
        f_dir = p.parent
        json_dir = f'{f_dir}/quantitative_features.json'
        # User
        n_user_interactions = 0
        user_interaction_lengths = []
        user_complexities = []
        user_polarities = []
        user_subjectivities = []
        user_sentiments = []
        # Bot
        n_agent_interactions = 0
        agent_interaction_lengths = []
        agent_complexities = []
        agent_polarities = []
        agent_subjectivities = []
        agent_sentiments = []
        with open(f, 'r') as file:
            chat_history = json.load(file)
        for interaction in chat_history[2:]:
            content = interaction['content']
            role = interaction['role']
            tokenized_interaction_text:list = tokenized_text(content)
            if len(tokenized_interaction_text) == 0:
                continue
            if role == 'user':
                n_user_interactions += 1
                user_interaction_lengths, user_complexities, user_polarities, user_subjectivities, user_sentiments = \
                    simple_quantitative_features(tokenized_interaction_text, user_interaction_lengths, user_complexities, user_polarities, user_subjectivities, user_sentiments)
            else:
                n_agent_interactions += 1
                agent_interaction_lengths, agent_complexities, agent_polarities, agent_subjectivities, agent_sentiments = \
                    simple_quantitative_features(tokenized_interaction_text, agent_interaction_lengths, agent_complexities, agent_polarities, agent_subjectivities, agent_sentiments)
        analysis = {
                'n_user_interactions': n_user_interactions,
                'user_interaction_lengths': user_interaction_lengths,
                'user_complexities': user_complexities,
                'user_polarities': user_polarities,
                'user_subjectivities': user_subjectivities,
                'user_sentiments': user_sentiments,
                'n_agent_interactions': n_agent_interactions,
                'agent_interaction_lengths': agent_interaction_lengths,
                'agent_complexities': agent_complexities,
                'agent_polarities': agent_polarities,
                'agent_subjectivities': agent_subjectivities,
                'agent_sentiments': agent_sentiments
            }
        with open(json_dir, 'w') as file:
            json.dump(analysis, file)
