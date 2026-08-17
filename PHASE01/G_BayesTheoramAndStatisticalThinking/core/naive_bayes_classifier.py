import math
from collections import defaultdict


class NaiveBayes:
    def __init__(self, smoothing=1.0):
        self.smoothing = smoothing
        self.class_counts = defaultdict(int)
        self.word_counts = defaultdict(lambda: defaultdict(int))
        self.class_word_totals = defaultdict(int)
        self.vocab = set()

    def train(self, documents, labels):
        """
        train the model on the given data
            docs = ["cheap pills now", "cheap watches now", "meeting agenda tomorrow", "project meeting tomorrow"]
            labels = ["spam", "spam", "ham", "ham"]

        Result:
                                        spam	                                     ham
            class_counts	          2	                                         2
            class_word_totals	          6	                                       6
            word_counts	           cheap:2,pills:1,now:2,watches:1	meeting:2,agenda:1,tomorrow:2,project:1


            vocab = {cheap, pills, now, watches, meeting, agenda, tomorrow, project}
            len(vocab) = 8
        """
        for doc, label in zip(documents, labels):
            self.class_counts[label] += 1
            words = doc.lower().split()

            for word in words:
                self.word_counts[label][word] += 1
                self.class_word_totals[label] += 1
                self.vocab.add(word)

    def predict(self, document):
        """
        Bayes-Therom in log-space

            this will help us do the probality multiply without getting
            zero as with log the multiplication will change to addition
            this will be better for the machine
        """
        words = document.lower().split()
        total_docs = sum(self.class_counts.values())
        vocab_size = len(self.vocab)
        best_class = None
        best_score = float("-inf")

        for cls in self.class_counts:
            score = math.log(self.class_counts[cls] / total_docs)

            for word in words:
                count = self.word_counts[cls].get(word, 0)
                total = self.class_word_totals[cls]
                score += math.log(
                    (count + self.smoothing) / (total + self.smoothing * vocab_size)
                )

            if score > best_score:
                best_score = score
                best_class = cls

        return best_class


if __name__ == "__main__":
    from helper import test_messages, train_docs, train_labels

    classifier = NaiveBayes()
    classifier.train(documents=train_docs, labels=train_labels)

    for msg in test_messages:
        print(f"'{msg}'->{classifier.predict(msg)}")

    def show_top_words(classifier, cls, n=5):
        vocab_size = len(classifier.vocab)
        total = classifier.class_word_totals[cls]
        probs = {}

        for word in classifier.vocab:
            count = classifier.word_counts[cls].get(word, 0)
            probs[word] = (count + classifier.smoothing) / (
                total + classifier.smoothing * vocab_size
            )

        sorted_words = sorted(probs.items(), key=lambda x: x[1], reverse=True)

        for word, prob in sorted_words[:n]:
            print(f"{word}:{prob:.4f}")

    print("\nTop spam words:")
    show_top_words(classifier, "spam")

    print("\nTop ham words:")
    show_top_words(classifier, "ham")
