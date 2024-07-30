async function generatePoem() {
    const userInput = document.getElementById('userInput').value;
    if (!userInput) {
        alert("Please enter a word or phrase.");
        return;
    }

    document.querySelector('.input-container').style.display = 'none';
    document.getElementById('loadingAnimation').style.display = 'block';

    const response = await fetch('/generate-poem/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ userInput: userInput })
    });

    const data = await response.json();
    const loadingMessage = data.loadingMessage;
    const poem = data.poem;
    const title = data.title;

    document.getElementById('loadingMessage').innerText = loadingMessage;
    document.getElementById('loadingMessage').style.display = 'block';

    setTimeout(() => {
        document.getElementById('poemOutput').style.display = 'block';
        document.getElementById('poemOutputP').innerText = poem;
        document.getElementById('poemOutputH').innerText = title;

        document.getElementById('word').style.display = 'none';

        document.getElementById('loadingAnimation').style.display = 'none';
        document.getElementById('loadingMessage').style.display = 'none';

        document.getElementById('tryAgainButton').style.display = 'block';
    }, 5000);
}

function reloadPage() {
    location.reload();
}
