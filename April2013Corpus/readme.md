# German April 2013 Twitter Corpus

This corpus contains a snapshot of German-language Twitter posts from the month of April, 2013. The posts have been automatically collected and filtered by language (see paper). The collection method guarantees a near-complete (>90%) sample of all tweets in German sent during that time period.

## Reference

If you use this corpus, please cite:

Tatjana Scheffler. 2014. A German Twitter Snapshot. In: Proceedings of LREC, Reykjavik, Iceland. [[Link to pdf]](http://www.lrec-conf.org/proceedings/lrec2014/pdf/1146_Paper.pdf)

## How to Use

Because of terms of service restrictions, only the tweet ids can be provided. They have been extracted using [twarc](https://github.com/DocNow/twarc). You can rehydrate the tweets (= reconstruct the tweet text and metadata) using the Twitter API. Twarc provides functionality for this as well (`rehydrate`).

