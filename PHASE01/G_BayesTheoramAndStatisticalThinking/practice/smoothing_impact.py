"""
Question:
    Smoothing impact. Run the spam classifier with smoothing
    values of 0.01, 0.1, 1.0, and 10.0.
        a. How do the top word probabilities change?
        b. What happens with smoothing=0 and a word that appears only in ham?
"""

import sys

sys.path.append(r"E:\ML\PHASE01\G_BayesTheoramAndStatisticalThinking\core")

from helper import test_messages, train_docs, train_labels
from naive_bayes_classifier import NaiveBayes, show_top_words

smoothing_values = [0.01, 0.1, 1.0, 10.0]


def run_smoothing(
    show_top_words, smoothing_values, train_docs, train_labels, test_messages
):
    print("=" * 60)
    print("PART (a): Effect of smoothing on top word probabilities")
    print("=" * 60)

    for s in smoothing_values:
        print(f"\n---smoothing = {s} ---")
        clf = NaiveBayes(smoothing=s)
        clf.train(documents=train_docs, labels=train_labels)

        print("Top spam words :")
        show_top_words(clf, "spam")
        print("Top ham words :")
        show_top_words(clf, "ham")

    print("Predictions")
    for msg in test_messages:
        print(f"{msg}--->{clf.predict(msg)}")


print(
    run_smoothing(
        show_top_words=show_top_words,
        smoothing_values=smoothing_values,
        train_docs=train_docs,
        train_labels=train_labels,
        test_messages=test_messages,
    )
)

print("\n" + "=" * 60)
print("PART (b): smoothing = 0, word seen only in ham")
print("=" * 60)

clf = NaiveBayes(smoothing=0.0)
clf.train(documents=train_docs, labels=train_labels)

ham_words = None
for w in clf.vocab:
    if clf.word_counts["ham"].get(w, 0) > 0 and clf.word_counts["spam"].get(w, 0) == 0:
        ham_words = w
        break

    print(f"Chosen ham-only word :{ham_words}")

try:
    result = clf.predict(ham_words)
    print(f"Predict('{ham_words}') --> {result}")
except ValueError as e:
    print(f"ValueError raised: {e}")
