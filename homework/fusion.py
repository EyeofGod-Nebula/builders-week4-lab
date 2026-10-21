"""Level 2 (challenge): write Reciprocal Rank Fusion yourself.

In class, LlamaIndex's QueryFusionRetriever merged the vector list and the BM25
list for you. Now write the merge by hand.

    score(doc) = sum over every list the doc appears in of  1 / (k + rank)

rank starts at 1. A doc that's missing from a list gets nothing from that list.
Return doc ids sorted by score, highest first. If two docs tie, keep the one
that showed up first (reading list 1 top to bottom, then list 2, and so on).

Step 1: change ATTEMPTING to True. The fusion tests will start running.
Step 2: replace the NotImplementedError with your code.
"""

ATTEMPTING = True


def rrf(ranked_lists, k=60):
    scores = {}
    
    for ranked_list in ranked_lists:
        for rank, doc in enumerate(ranked_list, start=1):
            if doc not in scores:
                scores[doc] = 0.0
            scores[doc] += 1.0 / (k + rank)
            
    # Sort documents by their total score from highest to lowest
    sorted_docs = sorted(scores.keys(), key=lambda doc: scores[doc], reverse=True)
    return sorted_docs


if __name__ == "__main__":
    vector = ["B05", "B02", "B11"]  # Strangers on a Train, Dracula, Station Eleven
    bm25 = ["B11", "B05", "B14"]  # Station Eleven, Strangers on a Train, Bird Box
    print(rrf([vector, bm25]))
