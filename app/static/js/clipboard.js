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
  document.querySelector("#clipboard").innerText = "Congratulations, we cannot read your clipboard !"
}