# coding: utf-8
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from bancodobrasil.models import BB


def example1(request):

    bb = BB(
        refTran='0000000001',
        valor='100',
        tpPagamento=3,
        dtVenc=u'10102014',
        nome=u'Willem Allan',
        endereco=u'Rua Franca',
        cidade=u'Ribeirão Preto',
        uf=u'SP',
        cep=u'14090250'
    )

    bb = bb.form()
    VARS = {
        'bb': bb,
    }

    return render_to_response("bancodobrasil/bb.html", VARS )

def example2(request):

    bb = BB(
        refTran='0000000001',
        valor='100',
        tpPagamento=3,
        dtVenc=u'10102014',
        nome=u'Willem Allan',
        endereco=u'Rua Franca',
        cidade=u'Ribeirão Preto',
        uf=u'SP',
        cep=u'14090250'
    )

    bb = bb.envia()
    VARS = {
        'bb': u"%s" % bb.decode('iso-8859-1'),
    }

    return render_to_response("bancodobrasil/bb.html", VARS )
