from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieClubForm
from django.template.defaultfilters import slugify
from .models import MovieClub

# passes the form to the template depending on whether you've already submitted it
# or just coming to a new form
def create_club(request):
	
	# if info already entered into the form
	if request.method == "POST":
	    form = MovieClubForm(request.POST)
	    if form.is_valid():
	        club = form.save()
	        return redirect('club_page', slug=club.slug)
	
	# display new form
	else:
	    form = MovieClubForm()
	

	return render(request, 'createclub/create_club.html', {'form': form}) # passing info to the actual form

def club_page(request, slug):

	club_details = get_object_or_404(MovieClub, slug=slug)
	return render(request, 'createclub/club_detail.html', {'club_details': club_details}) # passing info to the actual form

