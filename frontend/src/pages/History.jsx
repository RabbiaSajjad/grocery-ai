import { useEffect, useState } from "react";
import api from "../api/axios";

function History() {
  const [plans, setPlans] = useState([]);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      const response = await api.get("/planner/history/");
      setPlans(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Plan History</h2>

      {plans.map((plan) => (
        <div
          key={plan.id}
          style={{
            border: "1px solid gray",
            padding: "10px",
            marginBottom: "10px",
          }}
        >
          <h3>{plan.prompt}</h3>

          <p>
            Created:
            {" "}
            {new Date(plan.created_at).toLocaleString()}
          </p>

          <p>
            Estimated Cost:
            €{plan.estimated_cost}
          </p>

          <h4>Meal Plan</h4>

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
        </div>
      ))}
    </div>
  );
}

export default History;