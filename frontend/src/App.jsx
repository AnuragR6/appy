import React, { useState } from "react";
import axios from "axios";

function App() {
    const [input, setInput] = useState("");
    const [items, setItems] = useState([]);

    const addItem = () => {
        axios.post("http://localhost:5000/add-item", { item: input })
            .then(() => axios.get("http://localhost:5000/get-items"))
            .then((res) => setItems(res.data))
            .catch((err) => console.error(err));
    };

    return (
        <div>
            <h1>Item List App</h1>
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Enter an item"
            />
            <button onClick={addItem}>Add Item</button>
            <ul>
                {items.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
