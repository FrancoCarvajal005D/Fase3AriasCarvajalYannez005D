from django.test import TestCase
from noticia.forms import formularioForm
from noticia.models import formulario
from django.core.files.uploadedfile import SimpleUploadedFile


class formularioFormsTest(TestCase):
    def test_valid_form(self):
        genre = Genre.objects.create(name='1', message='Prueba')
        genre = Genre.objects.get(pk=1).pk
        m = noticia.objects.create(name='Prueba1', message='Prueba',)
        m.save()
        data = {'name': m.name, 'email': m.email, 'telefono': m.telefono, 'message' : m.message, }
        
        with open('noticia/static/img/logo.png',) as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/png')
        
        form = noticiaForm(data, {'image': document})
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Genre.objects.create(name='Accion', message='Prueba')
        m = noticia.objects.create(title='', summary='Prueba', genre=g, url='https://www.youtube.com/embed/rslZ-fHiSuI')
        data = {'name': m.name, 'email': m.email, 'telefono': m.telefono, 'message' : m.message, }
        form = noticiaForm(data=data)
        self.assertFalse(form.is_valid())