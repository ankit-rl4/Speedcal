from django.shortcuts import render
from .form import sd



def speedup(request):
    m1 = 0
    m3 = 0
    m5 = 0

    m10 = 0

    m15 = 0

    m30 = 0
    h1 = 0

    h3 = 0

    h8 = 0

    h15 = 0

    h24 = 0

    d3 = 0

    d7 = 0
    t = 0

    if request.method == 'POST':
        form = sd(request.POST)
        if form.is_valid():
            form.save()
            m1 = form.cleaned_data['m1']
            m3 = form.cleaned_data['m3']
            m5 = form.cleaned_data['m5']
            m10 = form.cleaned_data['m10']
            m15 = form.cleaned_data['m15']
            m30 = form.cleaned_data['m30']
            h1 = form.cleaned_data['h1']
            h3 = form.cleaned_data['h3']
            h8 = form.cleaned_data['h8']
            h15 = form.cleaned_data['h15']
            h24 = form.cleaned_data['h24']
            d3 = form.cleaned_data['d3']
            d7 = form.cleaned_data['d7']
    else:
        form = sd()

    m1 = m1 / 60
    m3 = m3 / 20
    m5 = m5 / 12
    m10 = m10 / 6
    m15 = 15 / 4
    m30 = m30 / 2
    h3 = h3 * 3
    h8 = h8 * 8
    h15 = h15 * 15
    h24 = h24 * 24
    d3 = d3 * 3 * 24
    d7 = d7 * 7 * 24
    t = m1 + m3 + m5 + m10 + m15 + m30 + h1 + h3 + h8 + h15 + h24 + d3 + d7
    t = t / 24

    return render(request, 'speed.html', {'days': t}, {'form': form})
