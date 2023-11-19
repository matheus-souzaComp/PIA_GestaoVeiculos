function exibir_form_motorista(tipo){

    add_motorista = document.getElementById('adicionar-motorista')
    att_motorista = document.getElementById('att_motorista')

    if(tipo == "1"){
        att_motorista.style.display = "none"
        add_motorista.style.display = "block"

    }else if(tipo == "2"){
        add_motorista.style.display = "none";
        att_motorista.style.display = "block"
    }

}


function dados_motorista(){
    motorista = document.getElementById('motorista-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_motorista = motorista.value
    console.log(motorista.value)

    data = new FormData()
    data.append('id_motorista', id_motorista)
    

    fetch("/motoristas/atualiza_motorista/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data
   
    }).then(function(result){
        console.log(result)
        return result.json()

    }).then(function(data){
        
        document.getElementById('form-att-motorista').style.display = 'block'
        
        id = document.getElementById('id')
        id.value = data['motorista_id']

        nome = document.getElementById('nome')
        nome.value = data['motorista']['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['motorista']['sobrenome']

        email = document.getElementById('email')
        email.value = data['motorista']['email']

        cpf = document.getElementById('cpf')
        cpf.value = data['motorista']['cpf']
        
    })

    
    

}


function update_motorista(){
    nome = document.getElementById('nome').value
    sobrenome = document.getElementById('sobrenome').value
    email = document.getElementById('email').value
    cpf = document.getElementById('cpf').value
    id = document.getElementById('id').value
   
    fetch('/motoristas/update_motorista/' + id, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            nome: nome,
            sobrenome: sobrenome,
            email: email,
            cpf: cpf,
        })

    }).then(function(result){
        return result.json()
    }).then(function(data){

        if(data['status'] == '200'){
            nome = data['nome']
            sobrenome = data['sobrenome']
            email = data['email']
            cpf = data['cpf']
            console.log('Dados alterado com sucesso')
        }else{
            console.log('Ocorreu algum erro')
        }

    })

}