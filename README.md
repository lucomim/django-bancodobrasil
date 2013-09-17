django-bancodobrasil
========================

Pagamento via debito

Installation
------------

pip install git+git://github.com/willemallan/django-bancodobrasil.git


Utilizando
-----

# settings.py

    BB_ID_CONV = '123456'
    BB_URL_FINALIZA_EXAMPLE1 = '/bancodobrasil/example1/'
    BB_URL_FINALIZA_EXAMPLE2 = '/bancodobrasil/example2/'
    BB_URL_BB_PAGAMENTO = 'https://mpag.bb.com.br/site/mpag/'
    BB_URL_RETORNO = 'https://www.loja.com.br/retorno/'
    BB_URL_INFORMA = 'https://www.loja.com.br/informa/'



-----
# views.py

example 1

    from bancodobrasil.models import BB

    bb = BB(
        refTran=123456,
        valor='100',
        tpPagamento=3,
        dtVenc=u'10102014',
        nome=u'Willem Allan',
        endereco=u'Rua Franca',
        cidade=u'Ribeirão Preto',
        uf=u'SP',
        cep=u'14090250',
        msgLoja=u'lol lol lol'
    )

    # form example
    bb = bb.form()
    VARS = {
        'bb': bb,
    }



-----
# views.py

example 2

    from bancodobrasil.models import BB

    bb = BB(
        refTran=123456,
        valor='100',
        tpPagamento=3,
        dtVenc=u'10102014',
        nome=u'Willem Allan',
        endereco=u'Rua Franca',
        cidade=u'Ribeirão Preto',
        uf=u'SP',
        cep=u'14090250',
        msgLoja=u'lol lol lol'
    )

    # urllib2 example
    bb = bb.envia()
    VARS = {
        'bb': u"%s" % bb.decode('iso-8859-1'),
    }



-----
# urls.py

não precisa importar apenas para visualizar os exemplos

    from bancodobrasil.urls import bancodobrasil_urlpatterns
    urlpatterns += bancodobrasil_urlpatterns()







