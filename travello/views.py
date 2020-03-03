from django.shortcuts import render
from .models import destination

# Create your views here.#
def index(request):
	# dest1=destination()
	# dest1.name='Viriyur'
	# dest1.desc='Thevillage'
	# dest1.img='destination_1.jpg'
	# dest1.price=8000
	# dest1.offer=False

	# dest2=destination()
	# dest2.name='Viriyur'
	# dest2.desc='The village'
	# dest2.img='destination_2.jpg'
	# dest2.price=7000
	# dest2.offer=False

	# dest3=destination()
	# dest3.name='Viriyur'
	# dest3.desc='The village'
	# dest3.img='destination_3.jpg'
	# dest3.price=8000
	# dest3.offer=True

	# dests=[dest1,dest2,dest3]
	dests=destination.objects.all()

	return render(request,"index.html",{'dests': dests})
