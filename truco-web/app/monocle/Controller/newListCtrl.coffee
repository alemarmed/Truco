class ListCtrller extends Monocle.Controller

	events:
		"tap a[data-action=cancell]" : "cancelled"
		"tap a[data-action=saveList]" : "saved"
	cancelled : (event) ->
		Lungo.Router.back()
		Lungo.Notification.alert("Error", "Cancelaste la creación", "warning", 7)
	saved : (event) ->
		Lungo.Notification.success("Success", "Successful operation", "check", 7)
__Controller.createList = new ListCtrller "section#list_detail"