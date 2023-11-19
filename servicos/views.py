
from django.shortcuts import render, get_object_or_404
from .forms import FormServico
from django.http import HttpResponse, FileResponse
from .models import Servico, ServicoAdicional
from fpdf import FPDF
from io import BytesIO

def novo_servico(request):
    if request.method == "GET":
        form = FormServico()
        return render(request, 'novo_servico.html', {'form': form})
    elif request.method == "POST":
        form = FormServico(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Salvo com sucesso')
        else:
            return render(request, 'novo_servico.html', {'form': form})

def listar_servico(request):
    if request.method == "GET":
        servicos = Servico.objects.all()    
        return render(request, 'listar_servico.html', {'servicos': servicos})
    
def servico(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)
    return render(request, 'servico.html', {'servico': servico})

def gerar_os(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 12)

    pdf.set_fill_color(240,240,240)
    pdf.cell(48, 10, 'TAG Equipamento:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.veiculo.tag}', 1, 1, 'L', 1)

    pdf.cell(48, 10, 'Operação Executada:', 1, 0, 'L', 1)

    operacoes = servico.operacao.all()
    for i, manutencao in enumerate(operacoes):
        pdf.cell(0, 10, f'- {manutencao.get_titulo_display()}', 1, 1, 'L', 1)
        if not i == len(operacoes) -1:
            pdf.cell(35, 10, '', 0, 0)

    pdf.cell(48, 10, 'Data/Hora de início:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.hora_inicio}', 1, 1, 'L', 1)
    pdf.cell(48, 10, 'Data/Hora do fim:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.hora_fim}', 1, 1, 'L', 1)
    pdf.cell(48, 10, 'Identificador:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.identificador}', 1, 1, 'L', 1)
    
    pdf_content = pdf.output(dest='S').encode('latin1')
    pdf_bytes = BytesIO(pdf_content)
   
    return FileResponse(pdf_bytes, as_attachment=True, filename=f"os-{servico.identificador}.pdf")

def servico_adicional(request):
    identificador_servico = request.POST.get('identificador_servico')
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    hora_inicio = request.POST.get('hora_inicio')
    hora_fim = request.POST.get('hora_fim')

    servico_adicional = ServicoAdicional(titulo=titulo,
                                        descricao=descricao,
                                        hora_inicio=hora_inicio,
                                        hora_fim = hora_fim)
    
    servico_adicional.save()

    servico = Servico.objects.get(identificador=identificador_servico)
    servico.servicos_adicionais.add(servico_adicional)
    servico.save()

    return HttpResponse("Salvo")