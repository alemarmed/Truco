class ListCtrller extends Monocle.Controller

	events:
		"swipeLeft article#current_lists" : "toDoneList" 
		"swipeRight article#done_lists" : "toCurrentList"
		"hold li" : "showListOptions"
		"tap li" : "showList"

	toDoneList : (event) ->
		Lungo.Router.article("list","done_lists")

	toCurrentList : (event) ->
		Lungo.Router.article("list","current_lists")

	showList : (event) ->
		Lungo.Router.section('list_detail')
	showListOptions : (event) ->
		console.log $$('#list_options_mini')
		Lungo.Router.aside('list', 'list_options_mini')
		Lungo.Notification.success("Success", "Successful operation", "check", 7)


__Controller.list = new ListCtrller "section#list"
__Controller.done = new ListCtrller "section#list "