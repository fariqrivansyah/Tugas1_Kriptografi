function toggleTheme() {
  document.body.classList.toggle("light-mode");
}

function showFields() {
  let algo = document.getElementById("algorithm").value;

  document.getElementById("singleKey").style.display = "none";
  document.getElementById("affineFields").style.display = "none";
  document.getElementById("hillField").style.display = "none";

  if (algo === "caesar" || algo === "vigenere" || algo === "playfair") {
    document.getElementById("singleKey").style.display = "block";
  }

  if (algo === "affine") {
    document.getElementById("affineFields").style.display = "block";
  }

  if (algo === "hill") {
    document.getElementById("hillField").style.display = "block";
  }
}
