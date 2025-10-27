document.getElementById('budgetForm').addEventListener('submit', async function(e) {
  e.preventDefault();
  const formData = new FormData(this);
  const data = Object.fromEntries(formData.entries());
  data.Attendees = parseInt(data.Attendees);
  data.Duration = parseInt(data.Duration);

  const response = await fetch('https://event-budget-api.onrender.com', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  document.getElementById('result').innerText = `💰 Estimated Budget: ₹${result.predicted_budget}`;
});
