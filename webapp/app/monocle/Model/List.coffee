class List extends Monocle.Model
    @fields "name", "description"
	validate: ->
	        unless @name
	            "name is required"