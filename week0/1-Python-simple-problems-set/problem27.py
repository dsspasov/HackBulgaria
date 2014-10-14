#problem27.py
months={
	0:31,
	1:29,
	2:31,
	3:30,
	4:31,
	5:30,
	6:31,
	7:31,
	8:30,
	9:31,
	10:30,
	11:31
}
zodia ={
	"Aries":(81,111),
	"Taurus":(112,142),
	"Gemini":(143,173),
	"Cancer":(174,204),
	"Leo":(205,235),
	"Virgo":(236,267),
	"Libra":(268,297),
	"Scorpio":(298,327),
	"Sagittarius":(328,356),
	"Capricorn":(357,366),
	"Aquarius":(21,50),
	"Pisces":(51,80)

}
def what_is_my_sign(day, month):
	day_of_year = day
	for d in range(month-1):
		day_of_year += months[d]
	if day_of_year<21:
		print ("Capricorn")
	else:
		for key in zodia:
			if(zodia[key][0]<=day_of_year) and (zodia[key][1]>=day_of_year):
				print(key)
def main():
	#print(months)
	what_is_my_sign(2,12)

if __name__ == '__main__':
	main()


"""

    Aries: 21 March – 20 April//81-111
    Taurus: 21 April – 21 May//112-142
    Gemini: 22 May – 21 June//143-173
    Cancer: 22 June – 22 July//174-204
    Leo: 23 July – 22 August//205-235
    Virgo: 23 August – 23 September//236-267
    Libra: 24 September – 23 October//268-297
    Scorpio: 24 October – 22 November//298-327
    Sagittarius: 23 November – 21 December//328-356
    Capricorn: 22 December – 20 January//0-20 357-366
    Aquarius: 21 January – 19 February//21-50
    Pisces: 20 February – 20 March//51-81


"""