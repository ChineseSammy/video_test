
var videoEreaStatus = false;
var videoEditArea = $('#video-edit-area');

$('#open-add-video-btn').click(function(){
      if (!videoEreaStatus) {
            videoEditArea.show();
            videoEreaStatus = true;
      } else {
            videoEditArea.hide();
            videoEreaStatus = false;
      }
});