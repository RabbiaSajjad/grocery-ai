import { useState } from "react";
import api from "../api/axios";

function Planner() {
  const [prompt, setPrompt] = useState("");
  const [plan, setPlan] = useState(null);
  const [loading, setLoading] = useState(false);

  const generatePlan = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await api.post("/planner/generate/", {
        prompt,
      });

      setPlan(response.data);
    } catch (error) {
      alert("Failed to generate plan");
      console.error(error.response?.data || error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>AI Grocery Planner</h2>

      <form onSubmit={generatePlan}>
        <textarea
          placeholder="Example: Create a 3-day cheap meal plan under 20 euros"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          rows="4"
          cols="50"
        />

        <br />

        <button type="submit" disabled={loading}>
          {loading ? "Generating..." : "Generate Plan"}
        </button>
      </form>

      {plan && (
        <div>
          <h3>Meal Plan</h3>

          {plan.meal_plan?.map((day, index) => (
            <div key={index}>
              <strong>{day.day}</strong>
              <ul>
                {day.meals?.map((meal, i) => (
                  <li key={i}>{meal}</li>
                ))}
              </ul>
            </div>
          ))}

          <h3>Grocery List</h3>

          <ul>
            {plan.grocery_list?.map((item, index) => (
              <li key={index}>
                {item.item} - {item.quantity} - {item.category} - €
                {item.estimated_price}
              </li>
            ))}
          </ul>

          <h3>Estimated Total Cost</h3>
          <p>€{plan.estimated_cost || plan.estimated_total_cost}</p>

          <h3>Budget Tips</h3>
          <ul>
            {plan.budget_tips?.map((tip, index) => (
              <li key={index}>{tip}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default Planner;