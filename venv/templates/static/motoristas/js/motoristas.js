function add_carro(){

    container = document.getElementById("form-carro")

    html = "<br> <div class='row'> <div class='col-md'><input type='text' placeholder='Veiculo' class='form-control' name='carro'</div> <div class='col-md'><input type='text' placeholder='Placa' class='form-control' name='placa'</div> <div class='col-md'> <input type='number' placeholder='ano' class='form-control' name='ano'></div>    <div class='col-md'> <input type='number' placeholder='Km Troca de Oleo' class='form-control' name='kmdeoleo'> </div></div> "

    container.innerHTML += html
}