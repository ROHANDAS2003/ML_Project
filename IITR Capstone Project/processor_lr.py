from sentence_transformers import SentenceTransformer
import joblib


transformer_model = SentenceTransformer('all-MiniLm-L6-v2')
classifier_model = joblib.load('./Model/log_clf.joblib')


def classify_with_logistic_regression(log_message):

    embeddings = transformer_model.encode(log_message)
    probabilities = classifier_model.predict_proba([embeddings])[0]
    if max(probabilities) < 0.5:
        return "Unknown"
    predict_class = classifier_model.predict([embeddings])[0]
    return predict_class


if __name__ == "__main__":
    print(classify_with_logistic_regression('Invoice generation process aborted for order ID 8910 due to invalid tax calculation module.'))