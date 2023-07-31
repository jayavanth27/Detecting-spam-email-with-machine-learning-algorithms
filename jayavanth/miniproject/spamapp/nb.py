def nb(email):
    # import numpy as n
    import pandas as pd
    # import sklearn
    from sklearn.feature_extraction.text import CountVectorizer
    df=pd.read_csv('messages.csv')
    # df.head()
    message=df['message'].tolist()
    label=df['label'].tolist()
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split( message, label, test_size=0.4, random_state=0)
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer=CountVectorizer()
    X_train=vectorizer.fit_transform(X_train)
    X_test=vectorizer.transform(X_test)
    classifier=MultinomialNB()
    classifier.fit(X_train,y_train)
    examples=[]
    examples.append(email)
    example_counts=vectorizer.transform(examples)
    predictions=classifier.predict(example_counts)
    return predictions[0]

