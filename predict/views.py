import cloudpickle
import pandas as pd
from django.shortcuts import render
from .models import Review




with open('data/predict.bin', 'rb') as file:
    predict_func = cloudpickle.load(file)


def index_page(request):
    predict = {'rating': None, 'sentiment': None}
    if request.method == 'POST':
        text = request.POST['text']
        is_tf_idf = request.POST['model'] == 'tf-idf'
        pred = predict_func(pd.Series(text), is_tf_idf)

        predict['sentiment'] = 'positive' if pred['sentiment'][0] == 1 else 'negative'
        predict['rating'] = pred['rating'][0] if is_tf_idf else pred['rating'][0][0]

        review = Review(text=text, pred_sentiment=predict['sentiment'], 
                        pred_rating=predict['rating'], model=request.POST['model'])
        review.save()

    return render(request, 'index.html', context=predict)
