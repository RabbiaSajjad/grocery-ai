import { useEffect, useState } from "react";
import api from "../api/axios";

function Pantry() {
  const [items, setItems] = useState([]);
  const [form, setForm] = useState({
    name: "",
    quantity: "",
    category: "",
  });

  const fetchItems = async () => {
    const response = await api.get("/pantry/items/");
    setItems(response.data);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    await api.post("/pantry/items/", form);

    setForm({
      name: "",
      quantity: "",
      category: "",
    });

    fetchItems();
  };

  useEffect(() => {
    fetchItems();
  }, []);

  return (
    <div>
      <h2>Pantry</h2>

      <form onSubmit={handleSubmit}>
        <input
          placeholder="Item name"
          value={form.name}
          onChange={(e) =>
            setForm({ ...form, name: e.target.value })
          }
        />

        <input
          placeholder="Quantity"
          value={form.quantity}
          onChange={(e) =>
            setForm({ ...form, quantity: e.target.value })
          }
        />

        <input
          placeholder="Category"
          value={form.category}
          onChange={(e) =>
            setForm({ ...form, category: e.target.value })
          }
        />

        <button type="submit">
          Add Item
        </button>
      </form>

      <hr />

      <ul>
        {items.map((item) => (
          <li key={item.id}>
            {item.name} - {item.quantity} ({item.category})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Pantry;