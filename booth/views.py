from django.http import HttpResponse
from django.shortcuts import render
from load_csv import load
from secret import MAP_KEY
from .models import Booth, Company

'''
def make_booth(request):
    booth_list = load('./data.csv')
    for booth in booth_list:
        name = booth[3]
        try:
            company = Company.objects.get(name=name)
        except Company.DoesNotExist:
            company = Company(name=name)
            company.save()
        Booth.objects.create(
            name=booth[0],  # 시설명
            road_address=booth[1],  # 소재지도로명주소
            land_address=booth[2],  # 소재지지번주소
            company=company,  # 운영기관명
            contact=booth[4],  # 전화번호
            place=booth[5],  # 급식장소
            target=booth[6],  # 급식대상
            time=booth[7],  # 급식시간
            date=booth[8],  # 급식일
            latitude=booth[11],  # 위도
            longitude=booth[12]  # 경도
        )
    return HttpResponse('load complete!')
'''


def maps(request):
    booths = Booth.objects.all()
    return render(request, 'booth/maps.html', {'booths': booths, 'MAP_KEY': MAP_KEY})
