from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from wax.models import Wax

@csrf_exempt
def DabGifter(request):
	waxs = Wax.objects.all().order_by('name')
	context = {'waxs': waxs}
        return render_to_response('dabgifter.html', context, context_instance=RequestContext(request))
		
