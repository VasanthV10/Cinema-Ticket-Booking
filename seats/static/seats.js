var settings = {
               rows: 20,
               cols: 20,
               rowCssPrefix: 'row-',
               colCssPrefix: 'col-',
               seatWidth: 35,
               seatHeight: 35,
               seatCss: 'seat',
               selectedSeatCss: 'selectedSeat',
               selectingSeatCss: 'selectingSeat'
           };

var init = function (reservedSeat) {
                var str = [], seatNo, className;
                for (i = 0; i < settings.rows; i++) {
                    for (j = 1; j <= settings.cols; j++) {
                        seatNo = String.fromCharCode('A'.charCodeAt() + i) + j;
                        className = settings.seatCss + ' ' + settings.rowCssPrefix + i.toString() + ' ' + settings.colCssPrefix + j.toString();
                        if ($.isArray(reservedSeat) && $.inArray(seatNo, reservedSeat) != -1) {
                            className += ' ' + settings.selectedSeatCss;
                        }
                        str.push('<li class="' + className + '"' +
                                  'style="top:' + (i * settings.seatHeight).toString() + 'px;left:' + (j * settings.seatWidth).toString() + 'px">' +
                                  '<a title="' + seatNo + '">' + seatNo + '</a>' +
                                  '</li>');
                    }
                }
                $('#place').html(str.join(''));
            };
            //case I: Show from starting
            init();
 
            //Case II: If already booked
            //var bookedSeats = [5, 10, 25];
            //init(bookedSeats);
$('.' + settings.seatCss).click(function () {
if ($(this).hasClass(settings.selectedSeatCss)){
    alert('This seat is already reserved');
}
else{
    $(this).toggleClass(settings.selectingSeatCss);
    }
});
 
$('#btnShowNew').click(function () {
    var str = [], item;
    $.each($('#place li.' + settings.selectingSeatCss + ' a'), function (index, value) {
        item = $(this).attr('title');                   
        str.push(item); 
        $('#seatsDisplay').val(str); 
        console.log(str);                   
    });
    alert(str.join(','));
})

	
       // function updateTextArea() {

         //   if ($('#place .seat:checked').length == ($("#Numseats").val())) {
           //     $("#place").prop("disabled", true);

             //   var allNumberVals = [];
               // var allSeatsVals = [];

                //allNumberVals.push($("#Numseats").val());
                //$('#place .seat:checked').each(function () {
                  //  allSeatsVals.push($(this).val());
                //});

                //$('#NumberDisplay').val(allNumberVals);
               // $('#seatsDisplay').val(allSeatsVals);
            //} else {
              //  alert("Please select " + ($("#Numseats").val()) + " seats")
            //}
        //}
