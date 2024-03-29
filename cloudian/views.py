from django.shortcuts import render, redirect

from konlpy.tag import Okt
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import stylecloud
import random


def main(request):
    return redirect('cloudian:main_en')


def output(request, img_id):
    return redirect('cloudian:wc_output_en', img_id=img_id)


def wc_create(request):
    return redirect('cloudian:wc_create_en')


def main_kr(request):
    return render(request, 'cloudian/base_kr.html')


def main_en(request):
    return render(request, 'cloudian/base.html')


def main_es(request):
    return render(request, 'cloudian/base_es.html')


def output_kr(request, img_id):
    context = {'img_id': img_id}
    return render(request, 'cloudian/wordcloud_kr.html', context)


def output_en(request, img_id):
    context = {'img_id': img_id}
    return render(request, 'cloudian/wordcloud.html', context)


def output_es(request, img_id):
    context = {'img_id': img_id}
    return render(request, 'cloudian/wordcloud_es.html', context)


def wc_create_kr(request):
    wc_text = request.POST.get('content')
    wc_shape = request.POST.get('shapes')
    rannum = random.randint(1, 10000000)
    name = "cloudian_" + str(rannum) + "_kr.png"

    if " " in wc_text:
        lists = [wc_text]

        okt = Okt()
        morphs = []

        for sentence in lists:
            morphs.append(okt.pos(sentence))

        noun_adj_adv_list = []

        for sentence in morphs:
            for word, tag in sentence:
                if (tag in ['Noun']) and ("것" not in word) and ("내" not in word) and ("나" not in word) and (
                        "수" not in word) and ("게" not in word) and ("말" not in word) and ("로서" not in word):
                    noun_adj_adv_list.append(word)
                if tag in ['Adjective']:
                    noun_adj_adv_list.append(word)
                if tag in ['Adverb']:
                    noun_adj_adv_list.append(word)
                if (tag in ['Foreign']) and ("(" not in word) and (")" not in word) and ("!" not in word) and (
                        "?" not in word) and ("." not in word) and ("," not in word) and (
                        "\'" not in word) and ("\\" not in word) and ("\n" not in word) and ("\r" not in word):
                    noun_adj_adv_list.append(word)
                if (tag in ['Alpha']) and ("(" not in word) and (")" not in word) and ("!" not in word) and (
                        "?" not in word) and ("." not in word) and ("," not in word) and (
                        "\'" not in word) and ("\"" not in word):
                    noun_adj_adv_list.append(word)

        if len(noun_adj_adv_list) != 0:
            count = Counter(noun_adj_adv_list)

            words = dict(count.most_common())

            stylecloud.gen_stylecloud(text=words,
                                      icon_name=wc_shape,
                                      background_color="white",
                                      font_path="/home/cloba/cloudian/static/BMHANNAPro.ttf",
                                      output_name="/home/cloba/cloudian/static/cloudImage/" + name, )

    return redirect('cloudian:wc_output_kr', img_id=rannum)


def wc_create_en(request):
    wc_text = request.POST.get('content')
    wc_shape = request.POST.get('shapes')
    rannum = random.randint(1, 10000000)
    name = "cloudian_" + str(rannum) + ".png"

    if wc_text is not None:
        eng_stop_words = list(stopwords.words("english"))
        filtered_list = []

        lists = [wc_text]
        words_list = []

        for sentence in lists:
            words_list.append(word_tokenize(sentence))

        for sentence in words_list:
            for word in sentence:
                if (word.casefold() not in eng_stop_words) and ("(" not in word) and (")" not in word) and ("!" not in word) and (
                        "?" not in word) and ("." not in word) and ("," not in word) and ("\'" not in word) and (
                        "\"" not in word) and ("\\" not in word) and ("\n" not in word) and ("\r" not in word) and (
                        ":" not in word) and (";" not in word) and ("{" not in word) and ("}" not in word) and (
                        "[" not in word) and ("]" not in word) and ("-" not in word) and ("=" not in word):
                    filtered_list.append(word)

        if len(filtered_list) != 0:
            count = Counter(filtered_list)

            texts = dict(count.most_common())

            stylecloud.gen_stylecloud(text=texts,
                                      icon_name=wc_shape,
                                      background_color="white",
                                      font_path="/home/cloba/cloudian/static/IBMPlexSans-SemiBold.ttf",
                                      output_name="/home/cloba/cloudian/static/cloudImage/" + name, )

    return redirect('cloudian:wc_output', img_id=rannum)


def wc_create_es(request):
    wc_text = request.POST.get('content')
    wc_shape = request.POST.get('shapes')
    rannum = random.randint(1, 10000000)
    name = "cloudian_" + str(rannum) + "_es.png"

    if wc_text is not None:
        es_stop_words = list(stopwords.words("spanish"))
        filtered_list = []

        lists = [wc_text]
        words_list = []

        for sentence in lists:
            words_list.append(word_tokenize(sentence))

        for sentence in words_list:
            for word in sentence:
                if (word.casefold() not in es_stop_words) and ("(" not in word) and (")" not in word) and ("!" not in word) and (
                        "?" not in word) and ("." not in word) and ("," not in word) and ("\'" not in word) and (
                        "\"" not in word) and ("\\" not in word) and ("\n" not in word) and ("\r" not in word) and (
                        ":" not in word) and (";" not in word) and ("{" not in word) and ("}" not in word) and (
                        "[" not in word) and ("]" not in word) and ("-" not in word) and ("=" not in word):
                    filtered_list.append(word)

        if len(filtered_list) != 0:
            count = Counter(filtered_list)

            texts = dict(count.most_common())

            stylecloud.gen_stylecloud(text=texts,
                                      icon_name=wc_shape,
                                      background_color="white",
                                      font_path="/home/cloba/cloudian/static/IBMPlexSans-SemiBold.ttf",
                                      output_name="/home/cloba/cloudian/static/cloudImage/" + name, )

    return redirect('cloudian:wc_output_es', img_id=rannum)
