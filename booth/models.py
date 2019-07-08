from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Booth(models.Model):
    name = models.CharField(max_length=50)  # 시설명
    road_address = models.CharField(max_length=100)  # 소재지도로명주소
    land_address = models.CharField(max_length=100)  # 소재지지번주소
    company = models.ForeignKey('Company', on_delete=models.CASCADE)  # 운영기관명
    contact = models.CharField(max_length=20)  # 전화번호
    place = models.CharField(max_length=100)  # 급식장소
    target = models.CharField(max_length=100)  # 급식대상
    time = models.CharField(max_length=50)  # 급식시간
    date = models.CharField(max_length=50)  # 급식일
    latitude = models.DecimalField(max_digits=10, decimal_places=8)  # 위도
    longitude = models.DecimalField(max_digits=11, decimal_places=8)  # 경도

    def __str__(self):
        return self.name
