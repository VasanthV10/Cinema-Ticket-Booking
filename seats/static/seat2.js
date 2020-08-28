function onLoaderFunc()
	{
		$(".seatStructure *").prop("disabled", true);
		$(".displayerBoxes *").prop("disabled", true);
	}
	function takeData()
	{
		if (( $("#Numseats").val().length == 0 ))
		{
			alert("Please Enter your Number of Seats");
		}
		else
		{
			$(".inputForm *").prop("disabled", false);
			$(".seatStructure *").prop("disabled", false);
			document.getElementById("notification").innerHTML = "<b style='margin-bottom:0px;background:yellow;'>Please Select your Seats NOW!</b>";
		}
	}
	
        function updateTextArea() {

            if ($("#place").length == ($("#Numseats").val())) {
                $(".seatStructure *").prop("disabled", true);

                var allNumberVals = [];
                var allSeatsVals = [];

                allNumberVals.push($("#Numseats").val());
                $('#seatsBlock :checked').each(function () {
                    allSeatsVals.push($(this).val());
                });

                //Displaying 
                $('#NumberDisplay').val(allNumberVals);
                $('#seatsDisplay').val(allSeatsVals);
            } else {
                alert("Please select " + ($("#Numseats").val()) + " seats")
            }
        }


        function myFunction() {
            alert($("input:checked").length);
        }

        $(":checkbox").click(function () {
            if ($("input:checked").length == ($("#Numseats").val())) {
                $(":checkbox").prop('disabled', true);
                $(':checked').prop('disabled', false);
            } else {
                $(":checkbox").prop('disabled', false);
            }
        });
