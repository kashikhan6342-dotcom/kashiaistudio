const button = document.querySelector("button");

button.addEventListener("click", async function () {

    const prompt = document.getElementById("prompt").value;

    const response = await fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            prompt: prompt
        })
    });

    const data = await response.text();

    document.getElementById("result").innerText = data;

});