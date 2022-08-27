from django.shortcuts import render, redirect

from konlpy.tag import Okt
from collections import Counter
import stylecloud


def text(request):
    return render(request, 'cloudian/wordcloud.html')


def wc_create(request):
    wc_text = request.POST.get('content')
    wc_shape = request.POST.get('shapes')
    if " " in wc_text:
        lists = [wc_text]

        okt = Okt()
        morphs = []

        for sentence in lists:
            morphs.append(okt.pos(sentence))

        noun_adj_adv_list = []

        for sentence in morphs:
            for word, tag in sentence:
                if tag in ['Noun'] and ("것" not in word) and ("내" not in word) and ("나" not in word) and (
                        "수" not in word) and ("게" not in word) and ("말" not in word) and ("로서" not in word):
                    noun_adj_adv_list.append(word)

        if len(noun_adj_adv_list) != 0:
            count = Counter(noun_adj_adv_list)

            words = dict(count.most_common())

            stylecloud.gen_stylecloud(text=words,
                                      icon_name=wc_shape,
                                      background_color="white",
                                      font_path="/home/cloba/cloudian/cloudian/BMHANNAPro.ttf",
                                      output_name="cloudian.png",)

    return redirect('cloudian:main')
