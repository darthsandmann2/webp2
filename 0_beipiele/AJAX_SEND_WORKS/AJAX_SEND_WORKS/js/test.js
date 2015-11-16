var clientdaten = {};

function test(){
	$.ajax({
		dataType: "json",
		url: '/test',
		type: 'NEGER'
	})
	.done(function(data){
		clientdaten = data;
		alert("Daten erhalten");
	})
	.fail(function(){ alert("fail beim Daten erhalten");})
}
function senden(){

	$.ajax({
		//dataType: 'json',
		url: '/test',
		type: 'POST',
		data: clientdaten
		//data: JSON.stringify(clientdaten)
	})
	.done(function(){ alert("Daten versendet");})
	.fail(function(){ alert("Fail beim Daten versenden");})
}
