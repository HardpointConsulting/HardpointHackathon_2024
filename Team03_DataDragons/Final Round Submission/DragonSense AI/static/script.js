let mic, recorder, soundFile;
let isRecording = false;

function setup() {
    mic = new p5.AudioIn();
    mic.start();
    recorder = new p5.SoundRecorder();
    recorder.setInput(mic);
    soundFile = new p5.SoundFile();
}
function toggleRecording() {
    if (!isRecording) {
        recorder.record(soundFile);
        console.log('Recording started...');
        document.getElementById('recordButton').innerText = 'Stop Recording';
    } else {
        recorder.stop();
        console.log('Recording stopped.');
        document.getElementById('voice').innerText = 'Record';
        saveSound(soundFile, 'recorded_audio.wav');
    }
    isRecording = !isRecording;
}
$(document).ready(()=>{
    $("#submit").click((ev)=>{
        ev.preventDefault();
        // alert("hihi")
        var text = $("#text").val()
        $("#text").val("")
        var existingContent = $("#answer").html();
        var newContent = existingContent  + "<p class='question mb-2'><span class='user'>User: </span>"+ text + "</p>"; // Concatenate
        console.log(existingContent, newContent)
        $("#answer").html(newContent);
        var req = $.ajax({
            type: 'POST',
            url: '/',
            data: {'message':text}
        })
        req.done((data)=>{
            // $("#answer").text(data.result)
            var existingContent = $("#answer").html(); // Get existing content
            var newContent = existingContent + "<p class='answer mb-4'><span class='ai'>DragonSense: </span>"+data.result+"</p>"; // Concatenate
            console.log(newContent)
            $("#answer").html(newContent);
            
        })

    })
})