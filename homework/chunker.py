"""Level 1: fix the orphan-chunk bug.

Dog-Ear Books, a late-night Brooklyn bookstore, wants a clerk bot that answers
questions about its October table. Before indexing, every book card is sliced
into chunks. Right now it cuts the text every `max_words` words, so the title
only lands in the FIRST chunk. Every later chunk is an orphan: it knows what
happened, but not which book it happened in.

Fix chunk_book() so that:
  1. EVERY chunk starts with the book's header, e.g. "Shelf B01: The Haunting of Hill House by Shirley Jackson (1959)."
  2. No chunk is longer than max_words words, header included.
  3. Every word of the body appears exactly once, in order, across the chunks.
  4. If max_words is too small to fit the header plus at least one body word,
     raise ValueError.

Run the tests: python -m unittest -v
"""

import json
from pathlib import Path

SHELF = json.loads((Path(__file__).parent / "books.json").read_text())


def header(book: dict) -> str:
    return f"Shelf {book['shelf']}: {book['title']} by {book['author']} ({book['year']})."


def body(book: dict) -> str:
    return (
        f"Section: {book['section']}. Setting: {book['setting']}. "
        f"Summary: {book['summary']} How it ends: {book['ending']} Bookseller's note: {book['note']}"
    )


def chunk_book(book: dict, max_words: int = 60) -> list[str]:
    hdr = header(book)
    hdr_words = hdr.sysplit() if hasattr(hdr, 'sysplit') else hdr.split() # standard split works fine
    hdr_len = len(hdr_words)
    
    if max_words <= hdr_len:
        raise ValueError("max_words is too small to fit the header and at least one body word.")
        
    body_words = body(book).split()
    chunk_capacity = max_words - hdr_len
    
    chunks = []
    for i in range(0, len(body_words), chunk_capacity):
        chunk_body_words = body_words[i : i + chunk_capacity]
        chunk_words = hdr_words + chunk_body_words
        chunks.append(" ".join(chunk_words))
        
    return chunks
