$(document).ready(function(){

	$(".slider").roundSlider({
	    radius: 80,
	    width: 24,
	    handleSize: "+8",
	    handleShape: "dot",
	    sliderType: "min-range",
	    circleShape: "half-top",
	    value: 90,
	    min:10,
        max:170
	});

    // until we go ajax - need to set the slider object position to what comes back in input values
    var obj1 =  $("#base-slider").data("roundSlider");
    obj1.setValue($("#base").val());

    var obj2 =  $("#shoulder-slider").data("roundSlider");
    obj2.setValue($("#shoulder").val());

    var obj3 =  $("#elbow-slider").data("roundSlider");
    obj3.setValue($("#elbow").val());

    var obj4 =  $("#wrist-slider").data("roundSlider");
    obj4.setValue($("#wrist").val());

    var obj5 =  $("#grip-rot-slider").data("roundSlider");
    obj5.setValue($("#grip_rotation").val());
    
    var obj6 =  $("#gripper-slider").data("roundSlider");
    obj6.setValue($("#gripper").val());

    // update input values for now from slider input 
	$("#base-slider").on("change", function (e) {
	    $("#base").val(e.value); 
	});
	$("#shoulder-slider").on("change", function (e) {
	    $("#shoulder").val(e.value); 
	});
	$("#elbow-slider").on("change", function (e) {
	    $("#elbow").val(e.value); 
	});
	$("#wrist-slider").on("change", function (e) {
	    $("#wrist").val(e.value); 
	});
	$("#grip-rot-slider").on("change", function (e) {
	    $("#grip_rotation").val(e.value); 
	});
	$("#gripper-slider").on("change", function (e) {
	    $("#gripper").val(e.value); 
	});
});