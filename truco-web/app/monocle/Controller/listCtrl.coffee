class ListCtrller extends Monocle.Controller

	events:
		"swipeLeft article#current_lists li" : "toDoneList" 
		"swipeRight article#done_lists li" : "toCurrentList"
		"hold li" : "showListOptions"

	toDoneList : (event) ->
		Lungo.Router.article("list","done_lists")

	toCurrentList : (event) ->
		Lungo.Router.article("list","current_lists")

	showListOptions : (event) ->
		Lungo.Router.aside('list', 'list_options_mini')
		Lungo.dom('#list_options_mini').show()

__Controller.list = new ListCtrller "section#list"
__Controller.done = new ListCtrller "section#list "