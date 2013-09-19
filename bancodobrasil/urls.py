#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from django.conf import settings

def bancodobrasil_urlpatterns():
    """
        URL para o retorno do bancodobrasil baseado na configuração do settings.

        A configuração da URL de retorno é obrigatória, exemplo:
            settings.BB_URL_RETORNO = '/bancodobrasil/retorno/'
    """
    url_example1 = settings.BB_URL_FINALIZA_EXAMPLE1.lstrip('/')
    url_example2 = settings.BB_URL_FINALIZA_EXAMPLE2.lstrip('/')
    url_sonda = settings.BB_URL_FINALIZA_SONDA.lstrip('/')
    urlpatterns = patterns('bancodobrasil.views',
        url(r'^%s$' % url_example1, 'example1', name='example1'),
        url(r'^%s$' % url_example2, 'example2', name='example2'),
        url(r'^%s$' % url_sonda, 'sonda', name='sonda'),
    )
    return urlpatterns

urlpatterns = bancodobrasil_urlpatterns()
