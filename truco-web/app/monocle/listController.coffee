class ListCtrller extends Monocle.Controller

	events:
		"tap li" : "showLista"

	showLista : (event) ->
		console.log event
		alert "yeaahh!!!"

};

Lungo.Data.Sql.select('twitter', {account: 'Lungojs'}, showInfo);

__Controller.NewList = new ListCtrller "article#myList"
