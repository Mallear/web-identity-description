// Need user to give permissions
// https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/readText#browser_compatibility
try {
  navigator.clipboard
  .readText()
  .then(
    (clipText) => (document.querySelector("#clipboard").innerText += clipText)
  );
} catch (error) {
  console.error(error);
  document.querySelector("#clipboard").innerText = " Le contenu du presse-papier n'est pas accessible."
  document.querySelector("#clipboard").style.color = "green"
}

document.querySelector("#screen-size").innerText += window.screen.width + "x" + window.screen.height