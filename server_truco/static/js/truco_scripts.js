/*
 * This function insert a row in a datatable table.
 * For automatic insertion
 */
function addrow(oTable,id,data) {
   var row = oTable.fnAddData( data );
   console.info(row[0].nTr);
   var theNode = oTable.fnSettings().aoData[row[0]].nTr;
   theNode.setAttribute('id',id);
   theNode.setAttribute('class','dirty');
}

function addMarker(map_id, markers){}

function deleteMarker(map_id, markers){}

function load_modal(modal_id,params,partial_load){
	$(modal_id).modal('show');
	$(modal_id).load(partial_load+param);		
}

function show_message(selector,message,type){
	$(selector).noty({text: message,type:type})	
}