from django.http import HttpResponse
from django.template import loader

private_link_path = "home/private_data/"
private_link_file = "private_link.txt"

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Media Grabber Frontend!")
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
    return HttpResponse("This is the Logs page!")
    """
    template = loader.get_template('home/index.html')
    private_link = open_private()
    link_string = private_link.split('=')[1].replace("'","").strip()
    #print(link_string)
    output_data = grab_mApe_wishList(link_string)
    context = {"output_data": output_data }
    return HttpResponse(template.render(context, request))
    """