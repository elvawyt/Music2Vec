# Music2Vec: Music Recommendation System based on GloVe
Course project for Text Mining class 2018

Global Vectors for Word Representation [(GloVe)](https://github.com/FengyangZhang/GloVe) is a new global log-bilinear regression model that trains only on the nonzero elements in a word-word co-occurrence matrix, it produces a vector space with meaningful substructure and outperforms related models on similarity and analogy tasks. In this paper we investigate its use in music recommendation system. First we propose a way to use GloVe on songs instead of on words to learn vector embeddings of them, then we introduce our method to do recommendation based on the learned vectors. As a result, we show our model generates useful and meaningful embeddings for songs that can be applied to recommendation and many other tasks like similarity and categorization.

The frontend of our project looks as follows:

Where the user input his/her netease music ID:
![frontendQuery](https://github.com/elvawyt/TextMining2018/blob/master/front_end/front1.png)

The returned recommendations:
![frontendReturned](https://github.com/elvawyt/TextMining2018/blob/master/front_end/front2.png)

Note that currently the backend is just reading the .json files in ./testData, if you want to query with your own ID that's not in there, you will need to run code in Pipeline.ipynb, generate your .json file.

To start the backend:
```
python glove_flask.py
```


Then go to index.html to see the frontend.


We are using [NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi) to get our data.
