from django.shortcuts import render

from Beauty.models import Beauty


masters = [
    {
        "id": 1,
        "name": "Olga Mykhailenko",
        "experience_years": 7,
        "phone": "+380-67-111-2222",
        "salon": "Beauty Studio Lotus",
        "services": ["Манікюр", "Педикюр", "Нарощування нігтів"],
    },
    {
        "id": 2,
        "name": "Iryna Koval",
        "experience_years": 4,
        "phone": "+380-50-333-4444",
        "salon": "Beauty Studio Lotus",
        "services": ["Макіяж", "Брови", "Ламінування вій"],
    },
    {
        "id": 3,
        "name": "Andriy Petrenko",
        "experience_years": 5,
        "phone": "+380-93-555-6666",
        "salon": "Beauty Studio Lotus",
        "services": ["Чоловіча стрижка", "Борода", "Фейд"],
    },
] 

# Create your views here.
def list(request):
    # barbers = Barber.objects.all()
    return render(request, "Beauty/list.html", {"masters": masters})


def detail(request, pk):
    #barber = get_object_or_404(Barber, pk=pk)
    return render(request, "Beauty/detail.html", {"master": masters[pk - 1]})
   
    
     
      
       
        
         
          
           
            
             
              
               
                 
                   
                    
                     
                      
                       
                        
                         
                           
                            
                             
                               

                                
                                  

                                   