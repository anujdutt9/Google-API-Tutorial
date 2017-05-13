from google.cloud import language

def language_analysis(text):
    client = language.Client()
    document = client.document_from_text(text)
    senti = document.analyze_sentiment()
    print(dir(senti))
    sentiment = senti.sentiment
    ent_analysis = document.analyze_entities()
    entities = ent_analysis.entities
    return sentiment, entities

t = '''It quickly became obvious that such an effort would require nothing less than Google-scale data and computing power. “I could try to give $
Kurzweil was attracted not just by Google’s computing resources but also by the startling progress the company has made in a branch of AI called $
The basic idea—that software can simulate the neocortex’s large array of neurons in an artificial “neural network”—is decades old, and it has led$'''

sentiment, entities = language_analysis(t)

print('\nSentiments:\n')
print(sentiment.score, sentiment.magnitude)


print('\nEntities:\n')
for ent in entities:
    print(ent.name, ent.entity_type, ent.metadata, ent.salience)
print('\n')
