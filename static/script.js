document.getElementById("predict-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const payload = {
    Event_Type: document.getElementById("eventType").value,
    Attendees: parseInt(document.getElementById("attendees").value),
    Duration: parseInt(document.getElementById("duration").value),
    Venue: document.getElementById("venue").value,
    Decoration: document.getElementById("decoration").value,
    Entertainment: document.getElementById("entertainment").value,
    Season: document.getElementById("season").value
  };

  document.getElementById("loading").style.display = "block";
  document.getElementById("result").textContent = "";

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await response.json();
    document.getElementById("result").textContent = `Estimated Budget: ₹${data.budget}`;
  } catch (error) {
    document.getElementById("result").textContent = "Error fetching prediction.";
  }

  document.getElementById("loading").style.display = "none";
});
