
1) viz.ipynb:
Characters list
Data Pre-processing
Basic Vizualisation
Book-indices - ends
Dictionary of books
 
2) src\components.py
List of Characters
NLTK Text objects
Book to Text mappings (dictionary : unprocessed)
books_to_chaps : Dictionary of book mapped to list of chapters in it

proc_data -> redundant(except doesnt have 's removed and is all .lower())

Data with Text: ('s removal has been done locally-at the isage point)
c_b_t.csv
final_data.csv
data.csv

==> cpo.csv -> clusts.csv(removed 's)
==> freq_occs_by_book.csv -> static(ie., blocks of words) co-occurences, book wise
==> freq_occs.csv -> static co-occs, chapter wise
==> cooccs_final -> sensible co-occs(ie., from word dist and context)(calculated canto wise), by book

======> Sentiments_books and cooccc_books can be merged
Same for chaps

=====================================================================================================

DELIVERABLES

C - Chapter wise metric
B - Book wise metric

1) Dendograms(C)
2) Networks(B)
3) Theme(+ve/-ve)(B)
5) Deg centralitiy graph over books | (add chars to ch list to analyse more) | labels over graph
6) DC per char per book | get from orig dict - deg
7) Summarization - per chapter against dendogram, per book against k core



too slow!
4) K-means clusters scatter(C) | Need mod -> on-hover label | or include in network
