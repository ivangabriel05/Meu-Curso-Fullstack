
// O RESUTADO DA BUSCAR ESTA SENDO ATRIBUIDA A LISTA
async function buscar(){
  let procura = await  fetch("tarefas.json")
  let lista = await procura.json()

  for (let x in lista)
      alert(lista[x])


}
buscar()