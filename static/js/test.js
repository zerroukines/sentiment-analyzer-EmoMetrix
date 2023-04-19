
document.getElementById("clear-btn").addEventListener("click", function() {
    document.getElementById("input-field").value = "";
});
  

const inputField = document.querySelector('#input-field');
  const sentimentField = document.querySelector('#sentiment-field');

  document.querySelector('#submit-btn').addEventListener('click', function() {
    const inputFieldValue = inputField.value.trim();

if (inputFieldValue) {
    const sentimentFieldValue = sentiment_analyzer(inputFieldValue);
    sentimentField.value = sentimentFieldValue;
}
});



