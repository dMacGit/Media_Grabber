from django.http import HttpResponse
from django.template import loader
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage


private_link_path = "home/private_data/"
private_link_file = "private_link.txt"

# Create your views here.
def frontend(request):

    #return HttpResponse("Welcome to the Media Grabber Frontend!")
    template = loader.get_template('frontend/media_grabber_home.html')

    context = {"output_data": "<p>Done!</p>"}
    return HttpResponse(template.render(context, request))

    """
    template = loader.get_template('home/index.html')
    private_link = open_private()
    link_string = private_link.split('=')[1].replace("'","").strip()
    #print(link_string)
    output_data = grab_mApe_wishList(link_string)
    context = {"output_data": output_data }
    return HttpResponse(template.render(context, request))
    """

def logs(request):
    #return HttpResponse("This is the logs page!")
    template = loader.get_template('frontend/media_grabber_logs.html')
    context = {"output_data": None}
    return HttpResponse(template.render(context, request))
    """
    template = loader.get_template('home/index.html')
    private_link = open_private()
    link_string = private_link.split('=')[1].replace("'","").strip()
    #print(link_string)
    output_data = grab_mApe_wishList(link_string)
    context = {"output_data": output_data }
    return HttpResponse(template.render(context, request))
    """