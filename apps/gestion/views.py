from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView , CreateView , UpdateView , DeleteView , DetailView ,TemplateView


from apps.gestion.models import Mercancia , RegistroCliente , Wehrehouse
from apps.gestion.forms import register_merchandiser_Form , register_werehouse_Form
from apps.usuario.models import  Usuario



class home(TemplateView):
    template_name = 'index.html'


#this class will create the merchandiseregister  than arrive to the company 



# **********************NOTA : THE CLIENT REGISTER AND MERCHANDISE REGISTER MUST BE DONE AT SAME TIME*********************************

class create_merchandise(CreateView):
    model = Mercancia
    #fields = '__all__'
    template_name = 'gestion/merchandise_register.html'
    form_class = register_merchandiser_Form

    #success_url = '/merchandise_register'



    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return render(self.request , self.template_name , {"form":self.form_class})
    


    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:

        
        form = self.form_class(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            print(info)
            user  = request.user.id 
            object_to_save = self.model()
            object_to_save.usuario_id = request.user.id 
            object_to_save.trakin = info['trakin']   
            object_to_save.regisro_cliente = RegistroCliente.objects.latest('id') # i should do better, 
            object_to_save.save()   

            print("it is valid" , user)
            return redirect('gestionurls:merchandiser_registerName')
        else:
            return render(self.request , self.template_name , {"form":form})
        



#this class create a werehouse
class create_warehouse(CreateView):
    model = Wehrehouse
    template_name = "gestion/create_warehouse_template.html"
    form_class = register_werehouse_Form



    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return render(self.request , self.template_name , {"form":self.form_class})
    

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:

        form = self.form_class(request.POST)
        if form.is_valid():

            print("it is ok")
            data = form.cleaned_data
            data['usuario_id']=request.user.id
            object_to_create = self.model(**data)
            object_to_create.save()
            return redirect('gestionurls:merchandiser_registerName')

        else:
            print("it is not ok")    

        return super().post(request, *args, **kwargs)
    



#this class will show each warehouse previously created
class show_werehouse(ListView):
    model= Wehrehouse 
    template_name =  "gestion/show_werehose_templete.html"

