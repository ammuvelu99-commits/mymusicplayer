const playlist = document.getElementById("playlist");
const player = document.getElementById("audioPlayer");

fetch("/api/songs")
.then(res => res.json())
.then(data => {

    data.forEach(song => {

        const li = document.createElement("li");

        li.innerText = song.title;

        li.onclick = () => {
            player.src = song.file;
            player.play();
        };

        playlist.appendChild(li);
    });

});