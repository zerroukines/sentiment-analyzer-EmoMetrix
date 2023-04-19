const inputElement = document.getElementById("file-upload");
const fileNameElement = document.getElementById("file-name");

inputElement.addEventListener("change", function() {
  const fileName = inputElement.files[0].name;
  fileNameElement.textContent = fileName;
});
