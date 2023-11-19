function exibir_form(tipo){

    add_veiculo = document.getElementById('adicionar-veiculo')
    att_veiculo = document.getElementById('att_veiculo')

    if(tipo == "1"){
        att_veiculo.style.display = "none"
        add_veiculo.style.display = "block"

    }else if(tipo == "2"){
        add_veiculo.style.display = "none";
        att_veiculo.style.display = "block"
    }

}


function dados_veiculo(){
    veiculo = document.getElementById('veiculo-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_veiculo = veiculo.value

    data = new FormData()
    data.append('id_veiculo', id_veiculo)

    fetch("/veiculos/atualiza_veiculo/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data

    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('form-att-veiculo').style.display = 'block'
        
        id = document.getElementById('id')
        id.value = data['veiculo_id']

        modelo = document.getElementById('modelo')
        modelo.value = data['veiculo']['modelo']

        tag = document.getElementById('tag')
        tag.value = data['veiculo']['tag']

        placa = document.getElementById('placa')
        placa.value = data['veiculo']['placa']

        nSerie = document.getElementById('nSerie')
        nSerie.value = data['veiculo']['nSerie']
        
        
    })

}


function update_veiculo(){
    modelo = document.getElementById('modelo').value
    tag = document.getElementById('tag').value
    placa = document.getElementById('placa').value
    nSerie = document.getElementById('nSerie').value
    id = document.getElementById('id').value

    fetch('/veiculos/update_veiculo/' + id, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            modelo: modelo,
            tag: tag,
            placa: placa,
            nSerie: nSerie,
        })

    }).then(function(result){
        return result.json()
    }).then(function(data){

        if(data['status'] == '200'){
            modelo = data['modelo']
            tag = data['tag']
            placa = data['placa']
            nSerie = data['nSerie']
            console.log('Dados alterado com sucesso')
        }else{
            console.log('Ocorreu algum erro')
        }

    })

}