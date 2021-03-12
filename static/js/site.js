var cameraOn = true;

function ChangeCamera() {

    if (cameraOn) {
        cameraOn = false;
        switch_butt = document.getElementById('camera-switch');
        switch_butt.innerHTML = 'Turn On Camera';
        $.ajax({
            dataType: "json",
            url: '/turn_off_camera',
            type: "POST",
            success: function() {
                console.log('Retrieved Data')
                video = document.getElementById('videoElement');
                video.style.display = 'none';
                video.src = '';

            },
            error: function() {
                window.location.href = '/'
                video = document.getElementById('videoElement');
                video.style.display = 'none';
                video.src = '';
            }
            
        })
    }
    else {
        cameraOn = true;
        switch_butt = document.getElementById('camera-switch');
        switch_butt.innerHTML = 'Turn Off Camera';
        $.ajax({
            dataType: "json",
            url: '/turn_on_camera',
            type: "POST",
            success: function() {
                console.log('Retrieved Data')
                video = document.getElementById('videoElement');
                video.style.display = 'block';
                video.src = '/video_feed';
            },
            error: function() {
                window.location.href = '/'
                video = document.getElementById('videoElement');
                video.style.display = 'block';
                video.src = '/video_feed';
            }
            
        })
    }
}