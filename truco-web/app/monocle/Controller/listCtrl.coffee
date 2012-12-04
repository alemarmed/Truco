class ListCtrller extends Monocle.Controller

	events:
		"tap li" : "showLista"

	showLista : (event) ->
		console.log event
		alert "yeaahh!!!"

__Controller.NewList = new ListCtrller "article#myList"
