var inputNumber = $('#number');
var inputUrl = $('#url');
var videoInputId = $('#videosub-input-id');

$('.update-btn').click(function(){
    var videoSubId = $(this).attr('data-id');
    var videoSubNUmber = parseInt($(this).attr('data-number'));
    var videoSubUrl = $(this).attr('data-url');

    inputNumber.val(videoSubNUmber);
    inputUrl.val(videoSubUrl);
    videoInputId.val(videoSubId);
});