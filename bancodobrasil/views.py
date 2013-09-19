# coding: utf-8
import datetime
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from bancodobrasil.models import BB


def example1(request):

    '''
    Conforme a modalidade de pagamento:

    0 – Todas as modalidades contratadas pelo convenente
    2 – Boleto bancário
    21 – 2ª Via de boleto bancário, já gerado anteriormente
    3 – Débito em Conta via Internet – PF e PJ
    5 – BB Crediário Internet
    7 - Débito em Conta via Internet PF
    '''

    data = datetime.datetime.now()

    bb = BB(
        refTran='1',
        valor='100',
        tpPagamento=3,
        dtVenc=data,
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

    '''
    Conforme a modalidade de pagamento:

    0 – Todas as modalidades contratadas pelo convenente
    2 – Boleto bancário
    21 – 2ª Via de boleto bancário, já gerado anteriormente
    3 – Débito em Conta via Internet – PF e PJ
    5 – BB Crediário Internet
    7 - Débito em Conta via Internet PF
    '''

    data = datetime.datetime.now()

    bb = BB(
        refTran='1',
        valor='100',
        tpPagamento=3,
        dtVenc=data,
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

def sonda(request):

    '''
        OBS: campo situacao só funciona formato XML


        Formato de retorno dos formulários de consulta submetidos ao banco:
        01 – HTML (Retorno visual em página do Banco para controle manual).
        02 – XML (Retorno em tag XML).
        03 – String (Retorno em forma de String).
    '''

    bb = BB(
        refTran='1',
        valor='100',
        formato='02',
    )

    '''
        RETORNO CAMPO SITUACAO VALORES - ALTERAR STATUS DO PEDIDO DE ACORDO:

        00 – pagamento efetuado
        01 – pagamento não autorizado/transação recusada
        02 – erro no processamento da consulta
        03 – pagamento não localizado
        10 – campo “idConv” inválido ou nulo
        11 – valor informado é inválido, nulo ou não confere com o valor registrado
        21 – Pagamento Web não autorizado
        22 – erro no processamento da consulta
        23 – erro no processamento da consulta
        24 - Convênio não cadastrado
        25 - Convênio não ativo
        26 - Convênio não permite debito em conta
        27 - Serviço inválido
        28 - Boleto emitido
        29 – pagamento não efetuado
    '''
    xml = bb.sonda()
    '''
        OBS: campo situacao só funciona formato XML

        fazer atualização do status do pedido da loja
    '''
    if bb.situacao == '00':
        pass
    elif bb.situacao == '01':
        pass

    VARS = {
        'bb': u"%s" % xml.decode('iso-8859-1'),
    }

    return render_to_response("bancodobrasil/bb.html", VARS )
