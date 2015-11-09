var cell = -1;
function SelectRow( row ) {
	if( cell != -1 ) {
		cell.removeAttribute( "class" );
	}
	cell = document.getElementById( row );
	cell.setAttribute( "class", "selected" );
}
function GetIdFromRow() {
	return cell.id;
}
function GetEditForm() {
	if( cell == -1 ) {
		alert( "Zum Bearbeiten ihrer Anmeldung müssen Sie ihren Namen in der Liste selektieren!" );
		return;
	}
	var link = "./edit_form?ident=";
	link += GetIdFromRow();
	window.location.href=link;
}


/*
$(document).ready(function() {
	$("tr").click(function(){
		$(this).addClass("selected").siblings().removeClass("selected");
	});
});
*/