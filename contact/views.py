from django.shortcuts import render, redirect
from django.urls import reverse  
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    # print('tipo de peticion: {}'.format(request.method))

    contact_form = ContactForm()

    if request.method == 'POST':
        #estoy enviando el formulario
        contact_form = ContactForm(data = request.POST)

        if contact_form.is_valid():
            name =  request.POST.get('name', '')
            email =  request.POST.get('email', '')
            message =  request.POST.get('message', '')

            # enviar el correo electronico
            email = EmailMessage(
                'Mensaje de contacto recibido', # Asunto
                'Mensaje enviado por {} <{}>:\n\n{}'.format(name,email,message), # Estructura de como nos llegaria el mensaje
                email, # El correo electronico del usuario (al cual yo puedo responder)
                ['ea404a49aaf410@inbox.mailtrap.io'],
                reply_to=[email],
            )

            try:
                email.send()
                # si envio y esta todo ok              
                # contact es el que esta definido en las urls (name='contact') y lo concatena con un ok
                return redirect(reverse('contact')+'?ok') # si el correo se envio con exito
            except:
                # Ha habido un error y retorno a ERROR
                return redirect(reverse('contact')+'?error') # si el correo no se envio con exito



    # envio al contact.html la variable form que contiene el formulario creado en (forms.py)
    return render(request, 'contact/contact.html', {'form':contact_form})