# """
# Question:
#     Add features.
#         a. Extend the NaiveBayes class to also use message
#         length (short/long) as a feature alongside word counts.

#         b. Estimate P(short|spam) and P(short|ham) from the training
#         data and fold it into the prediction score.
# """
# import sys

# sys.path.append(r"E:\ML\PHASE01\G_BayesTheoramAndStatisticalThinking\core")

# from naive_bayes_classifier import NaiveBayes
# from helper import threshold

# def get_type_of_length(self, doc):
#     word_count = len(doc.split())

#     if (word_count>threshold):
#         return 1 #long word
#     elif(self.word_count<threshold):
#         return 0 #short word
